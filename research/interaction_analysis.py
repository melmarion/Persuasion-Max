#!/usr/bin/env python3
"""
Interaction Surface Analyzer — Shape classification for top interactions
=========================================================================
For each top interaction from Session 4:
    - Classify as LINEAR / THRESHOLD / INVERTED-U via binned analysis + BIC
    - Test 3-way interactions for top 5
    - Split by domain for stability check

Usage:
    python research/interaction_analysis.py
"""

import sys
import os
import json
import numpy as np
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, log_loss
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

from calibration.fit_domain_weights import (
    load_samples, featurize_samples, ALL_FEATURE_NAMES,
)

OUTPUT_DIR = Path(__file__).parent.parent / "research" / "results"
INTERACTION_FILE = Path(__file__).parent.parent / "calibration" / "results" / "interaction_discovery.json"


def classify_interaction_shape(X, y, idx_a, idx_b, n_bins=5):
    """Classify interaction shape: LINEAR, THRESHOLD, or INVERTED_U.

    Bin each variable into quintiles, compute outcome rate per bin pair.
    Compare linear vs threshold vs quadratic fits using BIC.
    """
    feat_a = X[:, idx_a]
    feat_b = X[:, idx_b]

    # Bin into quintiles
    try:
        bins_a = np.percentile(feat_a[feat_a > 0], np.linspace(0, 100, n_bins + 1)) if np.any(feat_a > 0) else np.linspace(feat_a.min(), feat_a.max(), n_bins + 1)
        bins_b = np.percentile(feat_b[feat_b > 0], np.linspace(0, 100, n_bins + 1)) if np.any(feat_b > 0) else np.linspace(feat_b.min(), feat_b.max(), n_bins + 1)
    except Exception:
        bins_a = np.linspace(feat_a.min(), max(feat_a.max(), feat_a.min() + 0.01), n_bins + 1)
        bins_b = np.linspace(feat_b.min(), max(feat_b.max(), feat_b.min() + 0.01), n_bins + 1)

    # Compute outcome rate per bin pair
    bin_rates = {}
    for i in range(n_bins):
        for j in range(n_bins):
            lo_a = bins_a[min(i, len(bins_a) - 2)]
            hi_a = bins_a[min(i + 1, len(bins_a) - 1)]
            lo_b = bins_b[min(j, len(bins_b) - 2)]
            hi_b = bins_b[min(j + 1, len(bins_b) - 1)]

            mask = (feat_a >= lo_a) & (feat_a <= hi_a) & (feat_b >= lo_b) & (feat_b <= hi_b)
            if mask.sum() > 0:
                bin_rates[(i, j)] = {
                    "n": int(mask.sum()),
                    "outcome_rate": float(y[mask].mean()),
                }

    # Fit three models and compare BIC
    n = len(y)
    interaction = (feat_a * feat_b).reshape(-1, 1)
    feat_a_sq = (feat_a ** 2).reshape(-1, 1)
    feat_b_sq = (feat_b ** 2).reshape(-1, 1)

    models = {}

    # Linear: A + B + A*B
    X_linear = np.column_stack([feat_a, feat_b, interaction.ravel()])
    models["LINEAR"] = _fit_bic(X_linear, y, n)

    # Threshold: A + B + (A > median) * B
    median_a = np.median(feat_a)
    thresh = ((feat_a > median_a).astype(float) * feat_b).reshape(-1, 1)
    X_thresh = np.column_stack([feat_a, feat_b, thresh.ravel()])
    models["THRESHOLD"] = _fit_bic(X_thresh, y, n)

    # Quadratic: A + B + A*B + A^2 + B^2
    X_quad = np.column_stack([feat_a, feat_b, interaction.ravel(), feat_a_sq.ravel(), feat_b_sq.ravel()])
    models["INVERTED_U"] = _fit_bic(X_quad, y, n)

    best = min(models, key=lambda k: models[k]["bic"])

    return {
        "shape": best,
        "bic_scores": {k: round(v["bic"], 2) for k, v in models.items()},
        "bin_rates": {str(k): v for k, v in bin_rates.items()},
        "n_bins": n_bins,
    }


def _fit_bic(X, y, n):
    """Fit logistic regression and compute BIC."""
    scaler = StandardScaler()
    X_s = scaler.fit_transform(X)
    model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
    try:
        model.fit(X_s, y)
        y_prob = model.predict_proba(X_s)[:, 1]
        ll = -log_loss(y, y_prob, normalize=False)
        k = X.shape[1] + 1  # features + intercept
        bic = k * np.log(n) - 2 * ll
    except Exception:
        bic = float("inf")
    return {"bic": bic}


def test_3way_interactions(X, y, top_interactions, base_auc, feature_names):
    """For top 5 pairs, test adding a 3rd feature."""
    results = []

    for inter in top_interactions[:5]:
        idx_a = inter["idx_a"]
        idx_b = inter["idx_b"]
        pair_name = "%s × %s" % (inter["feature_a"], inter["feature_b"])

        # Base: linear + this 2-way interaction
        interaction_2way = X[:, idx_a] * X[:, idx_b]
        X_base = np.column_stack([X, interaction_2way])

        scaler = StandardScaler()
        X_base_s = scaler.fit_transform(X_base)
        model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
        try:
            scores = cross_val_score(model, X_base_s, y, cv=5, scoring="roc_auc")
            auc_2way = scores.mean()
        except Exception:
            auc_2way = base_auc

        best_3way = {"feature": None, "lift": 0.0}

        # Test adding each other feature as 3rd term
        for k in range(min(X.shape[1], 30)):  # limit for speed
            if k == idx_a or k == idx_b:
                continue

            interaction_3way = X[:, idx_a] * X[:, idx_b] * X[:, k]
            X_aug = np.column_stack([X_base, interaction_3way])

            scaler3 = StandardScaler()
            X_aug_s = scaler3.fit_transform(X_aug)
            model3 = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
            try:
                scores3 = cross_val_score(model3, X_aug_s, y, cv=5, scoring="roc_auc")
                auc_3way = scores3.mean()
            except Exception:
                auc_3way = auc_2way

            lift = auc_3way - auc_2way
            if lift > best_3way["lift"]:
                best_3way = {
                    "feature": feature_names[k] if k < len(feature_names) else str(k),
                    "lift": round(lift, 5),
                    "auc_3way": round(auc_3way, 4),
                }

        results.append({
            "pair": pair_name,
            "auc_2way": round(auc_2way, 4),
            "best_3rd_feature": best_3way["feature"],
            "3way_lift": best_3way["lift"],
            "3way_auc": best_3way.get("auc_3way", auc_2way),
            "3way_significant": best_3way["lift"] > 0.005,
        })

    return results


def domain_stability(X, y, samples, top_interactions):
    """Check if interactions hold in both domains."""
    domains = defaultdict(list)
    for i, s in enumerate(samples):
        domains[s["domain"]].append(i)

    results = {}
    for inter in top_interactions[:7]:
        pair_name = "%s × %s" % (inter["feature_a"], inter["feature_b"])
        domain_aucs = {}

        for dom, indices in domains.items():
            if len(indices) < 100:
                continue
            X_dom = X[indices]
            y_dom = y[indices]
            if len(np.unique(y_dom)) < 2:
                continue

            # Base AUC
            scaler = StandardScaler()
            X_s = scaler.fit_transform(X_dom)
            model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
            try:
                base_scores = cross_val_score(model, X_s, y_dom, cv=5, scoring="roc_auc")
                base_auc = base_scores.mean()
            except Exception:
                base_auc = 0.5

            # With interaction
            interaction = X_dom[:, inter["idx_a"]] * X_dom[:, inter["idx_b"]]
            X_aug = np.column_stack([X_dom, interaction])
            scaler2 = StandardScaler()
            X_aug_s = scaler2.fit_transform(X_aug)
            model2 = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
            try:
                aug_scores = cross_val_score(model2, X_aug_s, y_dom, cv=5, scoring="roc_auc")
                aug_auc = aug_scores.mean()
            except Exception:
                aug_auc = base_auc

            domain_aucs[dom] = {
                "base_auc": round(base_auc, 4),
                "with_interaction_auc": round(aug_auc, 4),
                "lift": round(aug_auc - base_auc, 5),
                "holds": (aug_auc - base_auc) > 0.002,
            }

        all_hold = all(d.get("holds", False) for d in domain_aucs.values())
        results[pair_name] = {
            "domain_results": domain_aucs,
            "stable_across_domains": all_hold,
        }

    return results


def main():
    # Load interaction results from Session 4
    if not INTERACTION_FILE.exists():
        print("ERROR: Run calibration/discover_interactions.py first")
        sys.exit(1)

    with open(INTERACTION_FILE) as f:
        inter_data = json.load(f)

    top_interactions = inter_data.get("top_30_interactions", [])
    if not top_interactions:
        print("ERROR: No interactions found")
        sys.exit(1)

    # Load and featurize samples
    samples = load_samples()
    np.random.seed(42)
    max_n = 6000
    if len(samples) > max_n:
        indices = np.random.choice(len(samples), max_n, replace=False)
        samples = [samples[i] for i in indices]

    features, outcomes, valid_samples = featurize_samples(samples)
    if len(features) == 0:
        print("ERROR: No features")
        sys.exit(1)

    print("\n=== Interaction Shape Classification ===")
    shape_results = []
    for inter in top_interactions[:7]:
        print("  Classifying %s × %s..." % (inter["feature_a"], inter["feature_b"]))
        shape = classify_interaction_shape(
            features, outcomes, inter["idx_a"], inter["idx_b"]
        )
        shape_results.append({
            "feature_a": inter["feature_a"],
            "feature_b": inter["feature_b"],
            "shape": shape["shape"],
            "bic_scores": shape["bic_scores"],
        })
        print("    Shape: %s (BIC: %s)" % (shape["shape"], shape["bic_scores"]))

    print("\n=== 3-Way Interaction Tests ===")
    three_way = test_3way_interactions(
        features, outcomes, top_interactions, inter_data["base_auc"], ALL_FEATURE_NAMES
    )
    for tw in three_way:
        print("  %s + %s: lift=%.5f %s" % (
            tw["pair"], tw["best_3rd_feature"], tw["3way_lift"],
            "(SIGNIFICANT)" if tw["3way_significant"] else "",
        ))

    print("\n=== Domain Stability ===")
    stability = domain_stability(features, outcomes, valid_samples, top_interactions)
    for pair, data in stability.items():
        stable = "STABLE" if data["stable_across_domains"] else "UNSTABLE"
        domains_str = ", ".join(
            "%s: lift=%.4f" % (d, v["lift"])
            for d, v in data["domain_results"].items()
        )
        print("  %s: %s (%s)" % (pair, stable, domains_str))

    # Save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {
        "shape_classifications": shape_results,
        "three_way_interactions": three_way,
        "domain_stability": {
            k: {
                "stable": v["stable_across_domains"],
                "domains": {dk: {kk: vv for kk, vv in dv.items() if kk != "holds"}
                           for dk, dv in v["domain_results"].items()},
            }
            for k, v in stability.items()
        },
    }

    # Sanitize numpy types for JSON
    def sanitize(obj):
        import numpy as _np
        if isinstance(obj, (_np.bool_, _np.integer)):
            return int(obj)
        if isinstance(obj, _np.floating):
            return float(obj)
        if isinstance(obj, _np.ndarray):
            return obj.tolist()
        if isinstance(obj, dict):
            return {str(k): sanitize(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [sanitize(v) for v in obj]
        return obj

    with open(OUTPUT_DIR / "interaction_surfaces.json", "w") as f:
        json.dump(sanitize(results), f, indent=2)

    print("\nResults saved to %s" % (OUTPUT_DIR / "interaction_surfaces.json"))
    return results


if __name__ == "__main__":
    main()
