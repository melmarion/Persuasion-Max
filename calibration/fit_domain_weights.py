#!/usr/bin/env python3
"""
Multi-Domain Weight Fitter — Fit logistic regression per domain
=================================================================
For each domain subset:
    1. Extract 7 appraisal + 12 linguistic + 40 technique features = 59 per stimulus
    2. Fit logistic regression with L2 regularization
    3. Extract weights with 95% CIs via bootstrap
    4. Cross-domain transfer test: train on A, test on B → AUC matrix

Usage:
    python calibration/fit_domain_weights.py
"""

import sys
import os
import json
import time
import math
import numpy as np
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

from core.appraisal_extractor import AppraisalExtractor
from core.technique_detector import TechniqueDetector, TECHNIQUES
from core.linguistic_surface import extract_linguistic_features

OUTPUT_DIR = Path(__file__).parent.parent / "calibration" / "results"
PARSED_DIR = Path(__file__).parent.parent / "calibration" / "parsed"


APPRAISAL_DIMS = ["novelty", "valence", "goal_relevance", "coping_potential",
                  "agency", "certainty", "temporal_proximity"]

LINGUISTIC_DIMS = ["word_count", "emotionality", "concreteness",
                   "analytical_thinking", "lexical_diversity", "hedge_density",
                   "certainty_markers", "self_reference", "other_reference",
                   "reading_difficulty", "tone_positive", "tone_negative"]

TECHNIQUE_NAMES = list(TECHNIQUES.keys())

ALL_FEATURE_NAMES = APPRAISAL_DIMS + LINGUISTIC_DIMS + TECHNIQUE_NAMES


def extract_features(text, extractor, detector):
    """Extract 59-dimensional feature vector from text."""
    # 7 appraisal features
    appraisal = extractor.extract(text, mode="heuristic")
    appraisal_vec = appraisal.to_vector()

    # 12 linguistic features (matches LinguisticFeatures.to_vector())
    ling = extract_linguistic_features(text)
    ling_vec = ling.to_vector()

    # 40 technique binary features
    techniques = detector.detect(text, mode="heuristic")
    tech_vec = []
    for name in TECHNIQUE_NAMES:
        t = techniques.techniques.get(name, {})
        tech_vec.append(t.get("confidence", 0.0) if t.get("detected") else 0.0)

    return appraisal_vec + ling_vec + tech_vec


def load_samples():
    """Load parsed unified dataset."""
    path = PARSED_DIR / "unified_dataset.jsonl"
    if not path.exists():
        print("ERROR: Run calibration/download_datasets.py first")
        sys.exit(1)

    samples = []
    with open(path) as f:
        for line in f:
            if line.strip():
                samples.append(json.loads(line))
    return samples


def featurize_samples(samples, max_n=None):
    """Extract features for all samples."""
    extractor = AppraisalExtractor()
    detector = TechniqueDetector()

    if max_n and len(samples) > max_n:
        # Stratified subsample
        np.random.seed(42)
        indices = np.random.choice(len(samples), max_n, replace=False)
        samples = [samples[i] for i in indices]

    print("  Extracting features for %d samples..." % len(samples))
    t0 = time.time()

    features = []
    outcomes = []
    valid_samples = []

    for i, s in enumerate(samples):
        try:
            vec = extract_features(s["text"], extractor, detector)
            if any(math.isnan(v) or math.isinf(v) for v in vec):
                continue
            features.append(vec)
            # Binarize outcome for logistic regression
            outcomes.append(1.0 if s["outcome"] > 0.5 else 0.0)
            valid_samples.append(s)
        except Exception:
            continue

        if (i + 1) % 1000 == 0:
            print("    %d/%d extracted (%.1fs)" % (i + 1, len(samples), time.time() - t0))

    elapsed = time.time() - t0
    print("  Featurized %d samples in %.1fs" % (len(features), elapsed))

    return np.array(features), np.array(outcomes), valid_samples


def fit_and_evaluate(X_train, y_train, X_test, y_test, feature_names=None):
    """Fit logistic regression with L2 and evaluate."""
    if len(np.unique(y_train)) < 2 or len(np.unique(y_test)) < 2:
        return None

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
    model.fit(X_train_s, y_train)

    y_prob = model.predict_proba(X_test_s)[:, 1]
    try:
        auc = roc_auc_score(y_test, y_prob)
    except ValueError:
        auc = 0.5

    result = {
        "auc": round(auc, 4),
        "n_train": len(y_train),
        "n_test": len(y_test),
        "pos_rate_train": round(y_train.mean(), 4),
        "pos_rate_test": round(y_test.mean(), 4),
    }

    if feature_names:
        coefs = model.coef_[0]
        result["weights"] = {
            name: round(float(coefs[i]), 4)
            for i, name in enumerate(feature_names)
        }

    return result


def bootstrap_ci(X, y, n_bootstrap=50, feature_names=None):
    """Bootstrap 95% CIs for logistic regression coefficients."""
    n = len(y)
    all_coefs = []

    scaler = StandardScaler()
    X_s = scaler.fit_transform(X)

    for b in range(n_bootstrap):
        idx = np.random.choice(n, n, replace=True)
        X_b, y_b = X_s[idx], y[idx]

        if len(np.unique(y_b)) < 2:
            continue

        model = LogisticRegression(C=1.0, max_iter=1000, random_state=b)
        try:
            model.fit(X_b, y_b)
            all_coefs.append(model.coef_[0])
        except Exception:
            continue

    if not all_coefs:
        return {}

    coef_matrix = np.array(all_coefs)
    ci_results = {}
    for i, name in enumerate(feature_names or range(X.shape[1])):
        vals = coef_matrix[:, i]
        ci_results[name] = {
            "mean": round(float(np.mean(vals)), 4),
            "ci_lower": round(float(np.percentile(vals, 2.5)), 4),
            "ci_upper": round(float(np.percentile(vals, 97.5)), 4),
            "std": round(float(np.std(vals)), 4),
        }
    return ci_results


def run_domain_fitting(all_features, all_outcomes, all_samples):
    """Fit weights per domain and compute cross-domain transfer matrix."""
    results = {}

    # Group by source
    sources = defaultdict(list)
    for i, s in enumerate(all_samples):
        sources[s["source"]].append(i)

    # Group by domain
    domains = defaultdict(list)
    for i, s in enumerate(all_samples):
        domains[s["domain"]].append(i)

    # 1. Per-source fitting with cross-validation
    print("\n--- Per-Source Fitting ---")
    for src, indices in sorted(sources.items()):
        if len(indices) < 50:
            print("  %s: skipped (N=%d < 50)" % (src, len(indices)))
            continue

        X = all_features[indices]
        y = all_outcomes[indices]

        if len(np.unique(y)) < 2:
            print("  %s: skipped (single class)" % src)
            continue

        scaler = StandardScaler()
        X_s = scaler.fit_transform(X)
        model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)

        try:
            cv_scores = cross_val_score(model, X_s, y, cv=5, scoring="roc_auc")
            auc = cv_scores.mean()
        except Exception:
            auc = 0.5

        # Fit on full data for weights
        model.fit(X_s, y)
        coefs = model.coef_[0]

        # Bootstrap CIs
        print("  %s: N=%d, 5-fold AUC=%.3f, bootstrapping CIs..." % (src, len(indices), auc))
        cis = bootstrap_ci(X, y, n_bootstrap=50, feature_names=ALL_FEATURE_NAMES)

        results[src] = {
            "auc_cv": round(auc, 4),
            "n": len(indices),
            "pos_rate": round(float(y.mean()), 4),
            "weights": {
                ALL_FEATURE_NAMES[i]: round(float(coefs[i]), 4)
                for i in range(len(ALL_FEATURE_NAMES))
            },
            "confidence_intervals": cis,
        }

    # 2. Per-domain fitting
    print("\n--- Per-Domain Fitting ---")
    for dom, indices in sorted(domains.items()):
        if len(indices) < 50:
            print("  %s: skipped (N=%d < 50)" % (dom, len(indices)))
            continue

        X = all_features[indices]
        y = all_outcomes[indices]

        if len(np.unique(y)) < 2:
            print("  %s: skipped (single class)" % dom)
            continue

        scaler = StandardScaler()
        X_s = scaler.fit_transform(X)
        model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)

        try:
            cv_scores = cross_val_score(model, X_s, y, cv=5, scoring="roc_auc")
            auc = cv_scores.mean()
        except Exception:
            auc = 0.5

        model.fit(X_s, y)
        coefs = model.coef_[0]

        print("  %s: N=%d, 5-fold AUC=%.3f" % (dom, len(indices), auc))

        results["domain_" + dom] = {
            "auc_cv": round(auc, 4),
            "n": len(indices),
            "pos_rate": round(float(y.mean()), 4),
            "weights": {
                ALL_FEATURE_NAMES[i]: round(float(coefs[i]), 4)
                for i in range(len(ALL_FEATURE_NAMES))
            },
        }

    # 3. Cross-domain transfer matrix
    print("\n--- Cross-Domain Transfer Matrix ---")
    transfer_matrix = {}
    source_keys = [s for s in sources if len(sources[s]) >= 50]

    for train_src in source_keys:
        transfer_matrix[train_src] = {}
        train_idx = sources[train_src]
        X_train = all_features[train_idx]
        y_train = all_outcomes[train_idx]

        if len(np.unique(y_train)) < 2:
            continue

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
        model.fit(X_train_s, y_train)

        for test_src in source_keys:
            test_idx = sources[test_src]
            X_test = all_features[test_idx]
            y_test = all_outcomes[test_idx]

            if len(np.unique(y_test)) < 2:
                transfer_matrix[train_src][test_src] = 0.5
                continue

            X_test_s = scaler.transform(X_test)
            y_prob = model.predict_proba(X_test_s)[:, 1]

            try:
                auc = roc_auc_score(y_test, y_prob)
            except ValueError:
                auc = 0.5

            transfer_matrix[train_src][test_src] = round(auc, 4)

        print("  Train on %s → %s" % (
            train_src,
            "  ".join("%s=%.3f" % (t, transfer_matrix[train_src][t])
                     for t in source_keys),
        ))

    results["transfer_matrix"] = transfer_matrix

    # 4. Feature set ablation: appraisal-only → +linguistic → +technique
    print("\n--- Feature Set Ablation ---")
    ablation = {}
    appraisal_idx = list(range(7))
    linguistic_idx = list(range(7, 19))
    technique_idx = list(range(19, 59))

    feature_sets = {
        "appraisal_only": appraisal_idx,
        "appraisal+linguistic": appraisal_idx + linguistic_idx,
        "appraisal+technique": appraisal_idx + technique_idx,
        "all_59_features": appraisal_idx + linguistic_idx + technique_idx,
    }

    for fs_name, fs_idx in feature_sets.items():
        for src, indices in sorted(sources.items()):
            if len(indices) < 50:
                continue

            X = all_features[np.ix_(indices, fs_idx)]
            y = all_outcomes[indices]

            if len(np.unique(y)) < 2:
                continue

            scaler = StandardScaler()
            X_s = scaler.fit_transform(X)
            model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)

            try:
                cv_scores = cross_val_score(model, X_s, y, cv=5, scoring="roc_auc")
                auc = cv_scores.mean()
            except Exception:
                auc = 0.5

            key = "%s_%s" % (fs_name, src)
            ablation[key] = round(auc, 4)

    print("  Feature set ablation:")
    for key, auc in sorted(ablation.items()):
        print("    %-45s AUC=%.3f" % (key, auc))

    results["ablation"] = ablation

    return results


def save_fitted_weights(results):
    """Save fitted weights per domain as JSON."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for key, data in results.items():
        if key in ("transfer_matrix", "ablation"):
            continue
        if not isinstance(data, dict) or "weights" not in data:
            continue

        out_path = OUTPUT_DIR / ("fitted_weights_%s.json" % key)
        fitted = []
        for name, value in data["weights"].items():
            ci = data.get("confidence_intervals", {}).get(name, {})
            fitted.append({
                "weight_name": name,
                "value": value,
                "CI_lower": ci.get("ci_lower", None),
                "CI_upper": ci.get("ci_upper", None),
                "corpus": key,
                "N": data["n"],
                "provenance": "FITTED",
                "domain": key,
            })

        with open(out_path, "w") as f:
            json.dump(fitted, f, indent=2)

    # Save full results
    with open(OUTPUT_DIR / "fit_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nFitted weights saved to %s" % OUTPUT_DIR)


def main():
    samples = load_samples()
    print("Loaded %d samples" % len(samples))

    # Limit to manageable size for speed — use all HCP but subsample if huge
    max_per_source = 5000
    sampled = []
    source_counts = defaultdict(int)
    np.random.seed(42)

    # Shuffle to get representative sample
    indices = np.random.permutation(len(samples))
    for i in indices:
        s = samples[i]
        if source_counts[s["source"]] < max_per_source:
            sampled.append(s)
            source_counts[s["source"]] += 1

    print("After sampling (max %d per source): %d samples" % (max_per_source, len(sampled)))

    # Extract features
    features, outcomes, valid_samples = featurize_samples(sampled)

    if len(features) == 0:
        print("ERROR: No valid features extracted")
        sys.exit(1)

    # Run fitting
    results = run_domain_fitting(features, outcomes, valid_samples)

    # Save
    save_fitted_weights(results)

    return results


if __name__ == "__main__":
    main()
