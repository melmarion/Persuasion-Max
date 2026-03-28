#!/usr/bin/env python3
"""
Full Validation Audit — Layer ablation × corpus AUC with 5-fold CV
====================================================================
Runs the FULL pipeline on every available corpus with every layer
ablation configuration. Reports calibration curves and marginal
layer contributions.

Usage:
    python validation/full_audit.py
"""

import sys
import os
import json
import time
import numpy as np
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.calibration import calibration_curve

from calibration.fit_domain_weights import (
    load_samples, extract_features, ALL_FEATURE_NAMES,
    APPRAISAL_DIMS, LINGUISTIC_DIMS, TECHNIQUE_NAMES,
)
from core.appraisal_extractor import AppraisalExtractor
from core.technique_detector import TechniqueDetector
from core.linguistic_surface import extract_linguistic_features

OUTPUT_DIR = Path(__file__).parent.parent / "results"


def featurize_with_interactions(samples, max_n=5000):
    """Extract features + top-5 interaction terms."""
    extractor = AppraisalExtractor()
    detector = TechniqueDetector()

    np.random.seed(42)
    if len(samples) > max_n:
        idx = np.random.choice(len(samples), max_n, replace=False)
        samples = [samples[i] for i in idx]

    print("  Extracting features for %d samples..." % len(samples))
    t0 = time.time()

    features = []
    outcomes = []
    valid_samples = []
    import math

    for i, s in enumerate(samples):
        try:
            vec = extract_features(s["text"], extractor, detector)
            if any(math.isnan(v) or math.isinf(v) for v in vec):
                continue
            features.append(vec)
            outcomes.append(1.0 if s["outcome"] > 0.5 else 0.0)
            valid_samples.append(s)
        except Exception:
            continue

        if (i + 1) % 2000 == 0:
            print("    %d/%d (%.1fs)" % (i + 1, len(samples), time.time() - t0))

    print("  Featurized %d in %.1fs" % (len(features), time.time() - t0))

    X = np.array(features)
    y = np.array(outcomes)

    # Add top-5 interaction terms from Session 4
    interactions = [
        (1, 16),   # valence × reading_difficulty
        (7, 20),   # word_count × evidence_based
        (2, 14),   # goal_relevance × self_reference
        (16, 24),  # reading_difficulty × bandwagon
        (16, 34),  # reading_difficulty × gain_frame
    ]

    interaction_cols = []
    for a, b in interactions:
        if a < X.shape[1] and b < X.shape[1]:
            interaction_cols.append(X[:, a] * X[:, b])

    if interaction_cols:
        X_interactions = np.column_stack(interaction_cols)
    else:
        X_interactions = np.zeros((X.shape[0], 0))

    return X, y, X_interactions, valid_samples


def cv_auc(X, y, n_folds=5):
    """5-fold stratified cross-validated AUC."""
    if len(np.unique(y)) < 2:
        return 0.5, []

    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)
    aucs = []
    all_probs = np.zeros(len(y))

    for train_idx, test_idx in skf.split(X, y):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
        try:
            model.fit(X_train_s, y_train)
            probs = model.predict_proba(X_test_s)[:, 1]
            auc = roc_auc_score(y_test, probs)
            aucs.append(auc)
            all_probs[test_idx] = probs
        except Exception:
            aucs.append(0.5)

    return round(np.mean(aucs), 4), all_probs


def compute_calibration(y_true, y_prob, n_bins=10):
    """Compute calibration curve data."""
    try:
        prob_true, prob_pred = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy="uniform")
        return {
            "bin_predicted": [round(float(p), 4) for p in prob_pred],
            "bin_observed": [round(float(p), 4) for p in prob_true],
            "n_bins": len(prob_true),
        }
    except Exception:
        return {"bin_predicted": [], "bin_observed": [], "n_bins": 0}


def run_audit():
    """Main audit: layer ablation × corpus with 5-fold CV."""
    samples = load_samples()
    print("Loaded %d total samples" % len(samples))

    # Group by source
    sources = defaultdict(list)
    for s in samples:
        sources[s["source"]].append(s)

    results = {}

    # Feature index ranges
    appraisal_idx = list(range(7))
    linguistic_idx = list(range(7, 19))
    technique_idx = list(range(19, 59))

    # Layer ablation configs
    configs = {
        "L2_appraisal_only": appraisal_idx,
        "L1+L2_ling+appraisal": appraisal_idx + linguistic_idx,
        "L1+L2+L3_all_59": appraisal_idx + linguistic_idx + technique_idx,
        "L2_no_L1_appraisal+tech": appraisal_idx + technique_idx,
    }

    for source_name, source_samples in sorted(sources.items()):
        if len(source_samples) < 100:
            print("\n  Skipping %s (N=%d < 100)" % (source_name, len(source_samples)))
            continue

        print("\n=== Corpus: %s (N=%d) ===" % (source_name, len(source_samples)))
        X, y, X_inter, valid = featurize_with_interactions(source_samples)

        if len(X) < 100:
            print("  Too few valid samples after featurization")
            continue

        corpus_results = {"n": len(X), "pos_rate": round(float(y.mean()), 4)}

        # Standard layer ablations
        for config_name, feat_idx in configs.items():
            X_config = X[:, feat_idx]
            auc, probs = cv_auc(X_config, y)
            cal = compute_calibration(y, probs) if probs.any() else {}
            corpus_results[config_name] = {"auc": auc, "calibration": cal}
            print("  %-35s AUC=%.4f" % (config_name, auc))

        # With interactions
        if X_inter.shape[1] > 0:
            X_with_inter = np.hstack([X[:, appraisal_idx + linguistic_idx], X_inter])
            auc, probs = cv_auc(X_with_inter, y)
            cal = compute_calibration(y, probs) if probs.any() else {}
            corpus_results["L1+L2+interactions"] = {"auc": auc, "calibration": cal}
            print("  %-35s AUC=%.4f" % ("L1+L2+interactions (top-5)", auc))

        results[source_name] = corpus_results

    # Marginal contribution analysis
    print("\n=== Marginal Layer Contributions ===")
    for source_name, cr in results.items():
        if "L2_appraisal_only" not in cr:
            continue
        base = cr["L2_appraisal_only"]["auc"]
        print("\n  %s (base appraisal AUC=%.4f):" % (source_name, base))

        if "L1+L2_ling+appraisal" in cr:
            lift = cr["L1+L2_ling+appraisal"]["auc"] - base
            print("    +L1 (linguistic):     %+.4f" % lift)

        if "L1+L2+L3_all_59" in cr and "L1+L2_ling+appraisal" in cr:
            lift = cr["L1+L2+L3_all_59"]["auc"] - cr["L1+L2_ling+appraisal"]["auc"]
            print("    +L3 (technique):      %+.4f" % lift)

        if "L1+L2+interactions" in cr and "L1+L2_ling+appraisal" in cr:
            lift = cr["L1+L2+interactions"]["auc"] - cr["L1+L2_ling+appraisal"]["auc"]
            print("    +interactions (top-5): %+.4f" % lift)

    # Save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Sanitize numpy types
    def sanitize(obj):
        if isinstance(obj, (np.bool_, np.integer)):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, dict):
            return {k: sanitize(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [sanitize(v) for v in obj]
        return obj

    with open(OUTPUT_DIR / "full_audit_results.json", "w") as f:
        json.dump(sanitize(results), f, indent=2)

    print("\nResults saved to %s" % (OUTPUT_DIR / "full_audit_results.json"))
    return results


if __name__ == "__main__":
    run_audit()
