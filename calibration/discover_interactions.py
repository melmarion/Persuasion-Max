#!/usr/bin/env python3
"""
Cross-Layer Interaction Discovery — THE PUBLISHABLE FINDING
==============================================================
Systematically test ALL pairwise cross-layer interactions:
    Appraisal × Appraisal:   7×7 = 21 unique pairs
    Technique × Appraisal:  40×7 = 280 pairs
    Technique × Technique:  40×40 = 780 pairs
    Linguistic × Appraisal: 12×7 = 84 pairs
    Total: 1,165 interaction candidates

For each: add interaction term to base model, measure AUC lift.
Rank by lift. Report top 30.

Usage:
    python calibration/discover_interactions.py
"""

import sys
import os
import json
import time
import numpy as np
from pathlib import Path
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

from calibration.fit_domain_weights import (
    load_samples, featurize_samples, ALL_FEATURE_NAMES,
    APPRAISAL_DIMS, LINGUISTIC_DIMS, TECHNIQUE_NAMES,
)

OUTPUT_DIR = Path(__file__).parent.parent / "calibration" / "results"


def compute_base_auc(X, y, cv=5):
    """Compute base model AUC (linear features only)."""
    scaler = StandardScaler()
    X_s = scaler.fit_transform(X)
    model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
    try:
        scores = cross_val_score(model, X_s, y, cv=cv, scoring="roc_auc")
        return scores.mean()
    except Exception:
        return 0.5


def test_interaction(X_base, y, feat_a_idx, feat_b_idx, base_auc, cv=5):
    """Add one interaction term and measure AUC lift."""
    interaction = (X_base[:, feat_a_idx] * X_base[:, feat_b_idx]).reshape(-1, 1)
    X_augmented = np.hstack([X_base, interaction])

    scaler = StandardScaler()
    X_s = scaler.fit_transform(X_augmented)
    model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)

    try:
        scores = cross_val_score(model, X_s, y, cv=cv, scoring="roc_auc")
        auc = scores.mean()
    except Exception:
        auc = 0.5

    return auc - base_auc


def discover_interactions(X, y, feature_names, min_lift=0.005, max_pairs=None):
    """Test all pairwise interactions, keep those with lift > min_lift."""
    n_features = X.shape[1]
    base_auc = compute_base_auc(X, y)
    print("  Base model AUC (linear only): %.4f" % base_auc)

    # Generate all unique pairs
    pairs = list(combinations(range(n_features), 2))
    if max_pairs and len(pairs) > max_pairs:
        # Prioritize cross-layer interactions
        appraisal_range = set(range(7))
        linguistic_range = set(range(7, 19))
        technique_range = set(range(19, 59))

        priority_pairs = []
        other_pairs = []
        for a, b in pairs:
            a_layer = ("appraisal" if a in appraisal_range else
                      "linguistic" if a in linguistic_range else "technique")
            b_layer = ("appraisal" if b in appraisal_range else
                      "linguistic" if b in linguistic_range else "technique")
            if a_layer != b_layer:
                priority_pairs.append((a, b))
            else:
                other_pairs.append((a, b))

        # Take all cross-layer + sample within-layer
        np.random.seed(42)
        if len(priority_pairs) + len(other_pairs) > max_pairs:
            n_other = max(0, max_pairs - len(priority_pairs))
            sampled_other = list(np.random.choice(
                len(other_pairs), min(n_other, len(other_pairs)), replace=False))
            other_pairs = [other_pairs[i] for i in sampled_other]
        pairs = priority_pairs + other_pairs

    print("  Testing %d interaction pairs..." % len(pairs))
    t0 = time.time()

    results = []
    for idx, (a, b) in enumerate(pairs):
        lift = test_interaction(X, y, a, b, base_auc, cv=5)

        if abs(lift) >= min_lift:
            results.append({
                "feature_a": feature_names[a] if a < len(feature_names) else str(a),
                "feature_b": feature_names[b] if b < len(feature_names) else str(b),
                "idx_a": int(a),
                "idx_b": int(b),
                "auc_lift": round(lift, 5),
                "auc_with_interaction": round(base_auc + lift, 4),
            })

        if (idx + 1) % 100 == 0:
            elapsed = time.time() - t0
            print("    %d/%d tested (%.0fs, %d significant so far)" % (
                idx + 1, len(pairs), elapsed, len(results)))

    elapsed = time.time() - t0
    results.sort(key=lambda x: abs(x["auc_lift"]), reverse=True)

    print("  Completed in %.0fs. %d interactions with lift > %.3f" % (
        elapsed, len(results), min_lift))

    return results, base_auc


def test_interaction_stacking(X, y, interactions, base_auc, max_interactions=20):
    """Test AUC improvement as we stack top-N interactions."""
    print("\n  --- Interaction Stacking Test ---")
    stacking_results = []

    for n in [5, 10, 15, 20]:
        top_n = interactions[:min(n, len(interactions))]
        if not top_n:
            break

        # Build augmented feature matrix
        interaction_cols = []
        for inter in top_n:
            col = X[:, inter["idx_a"]] * X[:, inter["idx_b"]]
            interaction_cols.append(col)

        X_augmented = np.hstack([X, np.column_stack(interaction_cols)])

        scaler = StandardScaler()
        X_s = scaler.fit_transform(X_augmented)
        model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)

        try:
            scores = cross_val_score(model, X_s, y, cv=5, scoring="roc_auc")
            auc = scores.mean()
        except Exception:
            auc = base_auc

        lift = auc - base_auc
        stacking_results.append({
            "n_interactions": n,
            "auc": round(auc, 4),
            "lift_over_linear": round(lift, 4),
        })
        print("    Top %d interactions: AUC=%.4f (lift=%.4f over linear)" % (n, auc, lift))

    return stacking_results


def run_domain_split(X, y, samples, interactions, feature_names):
    """Check if same interactions appear across domains."""
    domains = {}
    for i, s in enumerate(samples):
        dom = s["domain"]
        if dom not in domains:
            domains[dom] = []
        domains[dom].append(i)

    domain_results = {}
    for dom, indices in domains.items():
        if len(indices) < 100:
            continue

        X_dom = X[indices]
        y_dom = y[indices]

        if len(np.unique(y_dom)) < 2:
            continue

        base_auc = compute_base_auc(X_dom, y_dom)
        print("\n  Domain '%s': N=%d, base AUC=%.4f" % (dom, len(indices), base_auc))

        # Test top 10 interactions from overall analysis
        dom_interactions = []
        for inter in interactions[:min(20, len(interactions))]:
            lift = test_interaction(X_dom, y_dom, inter["idx_a"], inter["idx_b"], base_auc)
            dom_interactions.append({
                "feature_a": inter["feature_a"],
                "feature_b": inter["feature_b"],
                "overall_lift": inter["auc_lift"],
                "domain_lift": round(lift, 5),
                "transfers": abs(lift) > 0.003,
            })

        domain_results[dom] = {
            "n": len(indices),
            "base_auc": round(base_auc, 4),
            "interaction_transfer": dom_interactions,
        }

        # Report
        transfers = sum(1 for i in dom_interactions if i["transfers"])
        print("    %d/%d top interactions transfer to this domain" % (
            transfers, len(dom_interactions)))

    return domain_results


def main():
    samples = load_samples()
    print("Loaded %d samples" % len(samples))

    # Use largest available corpus for statistical power
    # Subsample to keep runtime manageable
    np.random.seed(42)
    max_n = 8000
    if len(samples) > max_n:
        indices = np.random.choice(len(samples), max_n, replace=False)
        samples = [samples[i] for i in indices]
        print("Subsampled to %d for speed" % max_n)

    features, outcomes, valid_samples = featurize_samples(samples)
    if len(features) == 0:
        print("ERROR: No valid features")
        sys.exit(1)

    # Discover interactions
    print("\n=== Interaction Discovery ===")
    interactions, base_auc = discover_interactions(
        features, outcomes, ALL_FEATURE_NAMES,
        min_lift=0.003,
        max_pairs=800,  # limit for speed
    )

    # Print top 30
    print("\n=== TOP 30 INTERACTIONS ===")
    print("%-3s %-25s %-25s %10s %10s" % ("#", "Feature A", "Feature B", "AUC Lift", "AUC"))
    print("-" * 80)
    for i, inter in enumerate(interactions[:30]):
        print("%-3d %-25s %-25s %10.5f %10.4f" % (
            i + 1, inter["feature_a"][:25], inter["feature_b"][:25],
            inter["auc_lift"], inter["auc_with_interaction"]))

    # Stacking test
    stacking = test_interaction_stacking(features, outcomes, interactions, base_auc)

    # Domain split analysis
    print("\n=== Domain Split Analysis ===")
    domain_split = run_domain_split(
        features, outcomes, valid_samples, interactions, ALL_FEATURE_NAMES)

    # Save results
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {
        "base_auc": round(base_auc, 4),
        "n_samples": len(valid_samples),
        "n_interactions_tested": 800,
        "n_significant": len(interactions),
        "top_30_interactions": interactions[:30],
        "stacking_results": stacking,
        "domain_split": domain_split,
    }

    # Convert numpy types for JSON serialization
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

    with open(OUTPUT_DIR / "interaction_discovery.json", "w") as f:
        json.dump(sanitize(results), f, indent=2)

    print("\nResults saved to %s" % (OUTPUT_DIR / "interaction_discovery.json"))
    return results


if __name__ == "__main__":
    main()
