#!/usr/bin/env python3
"""
Weight Stability Analysis — Universal vs Domain-Specific vs Insignificant
==========================================================================
For each of the 59 features:
    - Fit weight separately on each corpus
    - Compute coefficient of variation across corpora
    - Classify: UNIVERSAL / DOMAIN-SPECIFIC / INSIGNIFICANT

This determines which weights belong in the shared core vs domain registries.

Usage:
    python calibration/compare_domains.py
"""

import sys
import os
import json
import numpy as np
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from calibration.fit_domain_weights import (
    load_samples, featurize_samples, ALL_FEATURE_NAMES,
)

OUTPUT_DIR = Path(__file__).parent.parent / "calibration" / "results"


def fit_per_corpus(features, outcomes, samples):
    """Fit weights separately per corpus and per domain."""
    # Group by source
    sources = defaultdict(list)
    for i, s in enumerate(samples):
        sources[s["source"]].append(i)

    # Group by domain
    domains = defaultdict(list)
    for i, s in enumerate(samples):
        domains[s["domain"]].append(i)

    corpus_weights = {}

    for group_name, groups in [("source", sources), ("domain", domains)]:
        for name, indices in groups.items():
            if len(indices) < 50:
                continue

            X = features[indices]
            y = outcomes[indices]

            if len(np.unique(y)) < 2:
                continue

            scaler = StandardScaler()
            X_s = scaler.fit_transform(X)

            model = LogisticRegression(C=1.0, max_iter=1000, random_state=42)
            model.fit(X_s, y)

            key = "%s_%s" % (group_name, name)
            corpus_weights[key] = {
                "n": len(indices),
                "weights": {
                    ALL_FEATURE_NAMES[i]: round(float(model.coef_[0][i]), 4)
                    for i in range(len(ALL_FEATURE_NAMES))
                },
            }

    return corpus_weights


def classify_features(corpus_weights):
    """Classify each feature as UNIVERSAL, DOMAIN-SPECIFIC, or INSIGNIFICANT."""
    if not corpus_weights:
        return {}

    corpus_names = list(corpus_weights.keys())
    feature_classifications = {}

    for feat_name in ALL_FEATURE_NAMES:
        values = []
        for cn in corpus_names:
            w = corpus_weights[cn]["weights"].get(feat_name, 0.0)
            values.append(w)

        values = np.array(values)
        mean_val = np.mean(values)
        std_val = np.std(values)
        abs_mean = np.abs(mean_val)

        # Check sign consistency
        signs = np.sign(values[values != 0]) if any(values != 0) else np.array([0])
        sign_consistent = len(np.unique(signs)) <= 1

        # Coefficient of variation (handle zero mean)
        if abs_mean > 0.001:
            cv = std_val / abs_mean
        else:
            cv = float("inf") if std_val > 0.01 else 0.0

        # Magnitude ratio across corpora
        nonzero = values[np.abs(values) > 0.001]
        if len(nonzero) >= 2:
            magnitude_ratio = np.max(np.abs(nonzero)) / np.min(np.abs(nonzero))
        else:
            magnitude_ratio = 1.0

        # Classification
        if abs_mean < 0.01 and std_val < 0.02:
            classification = "INSIGNIFICANT"
            reason = "near-zero weight across all corpora (|mean|=%.4f, std=%.4f)" % (abs_mean, std_val)
        elif not sign_consistent or magnitude_ratio > 3.0:
            classification = "DOMAIN-SPECIFIC"
            reason = "sign flips or magnitude varies >3x across corpora (CV=%.2f, ratio=%.1f)" % (cv, magnitude_ratio)
        elif sign_consistent and cv < 0.5:
            classification = "UNIVERSAL"
            reason = "consistent sign and CV < 0.5 (CV=%.2f, mean=%.4f)" % (cv, mean_val)
        elif sign_consistent:
            classification = "UNIVERSAL"  # consistent but high variance
            reason = "consistent sign but high CV (CV=%.2f, mean=%.4f)" % (cv, mean_val)
        else:
            classification = "DOMAIN-SPECIFIC"
            reason = "mixed evidence"

        feature_classifications[feat_name] = {
            "classification": classification,
            "reason": reason,
            "mean_weight": round(float(mean_val), 4),
            "std_weight": round(float(std_val), 4),
            "cv": round(float(cv), 4) if cv != float("inf") else "inf",
            "sign_consistent": bool(sign_consistent),
            "magnitude_ratio": round(float(magnitude_ratio), 2),
            "per_corpus": {
                cn: round(float(corpus_weights[cn]["weights"].get(feat_name, 0.0)), 4)
                for cn in corpus_names
            },
        }

    return feature_classifications


def generate_stability_matrix(corpus_weights, classifications):
    """Generate weight stability matrix: feature × corpus → fitted_value."""
    if not corpus_weights:
        return {}

    corpus_names = sorted(corpus_weights.keys())
    matrix = {}

    for feat_name in ALL_FEATURE_NAMES:
        row = {}
        for cn in corpus_names:
            row[cn] = corpus_weights[cn]["weights"].get(feat_name, 0.0)
        row["classification"] = classifications.get(feat_name, {}).get("classification", "UNKNOWN")
        matrix[feat_name] = row

    return matrix


def main():
    samples = load_samples()
    print("Loaded %d samples" % len(samples))

    # Subsample for speed
    np.random.seed(42)
    max_n = 8000
    if len(samples) > max_n:
        indices = np.random.choice(len(samples), max_n, replace=False)
        samples = [samples[i] for i in indices]

    features, outcomes, valid_samples = featurize_samples(samples)
    if len(features) == 0:
        print("ERROR: No valid features")
        sys.exit(1)

    # Fit per corpus
    print("\n=== Per-Corpus Fitting ===")
    corpus_weights = fit_per_corpus(features, outcomes, valid_samples)

    for name, data in sorted(corpus_weights.items()):
        print("  %s: N=%d" % (name, data["n"]))

    # Classify features
    print("\n=== Feature Classification ===")
    classifications = classify_features(corpus_weights)

    # Count by category
    counts = defaultdict(int)
    for feat, info in classifications.items():
        counts[info["classification"]] += 1

    print("  UNIVERSAL:       %d features" % counts.get("UNIVERSAL", 0))
    print("  DOMAIN-SPECIFIC: %d features" % counts.get("DOMAIN-SPECIFIC", 0))
    print("  INSIGNIFICANT:   %d features" % counts.get("INSIGNIFICANT", 0))

    # Print domain-specific features (most interesting)
    print("\n  Domain-specific features (validate Session 3 registries):")
    for feat, info in sorted(classifications.items(), key=lambda x: x[1]["classification"]):
        if info["classification"] == "DOMAIN-SPECIFIC":
            print("    %-30s %s" % (feat[:30], info["reason"][:60]))

    # Generate stability matrix
    matrix = generate_stability_matrix(corpus_weights, classifications)

    # Save results
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {
        "n_features": len(ALL_FEATURE_NAMES),
        "n_corpora": len(corpus_weights),
        "classification_counts": dict(counts),
        "classifications": classifications,
        "stability_matrix": matrix,
        "corpus_sample_sizes": {
            name: data["n"] for name, data in corpus_weights.items()
        },
    }

    with open(OUTPUT_DIR / "domain_comparison.json", "w") as f:
        json.dump(results, f, indent=2)

    # Print top universal features
    print("\n  Top universal features (highest |mean weight|):")
    universal = [(f, c) for f, c in classifications.items() if c["classification"] == "UNIVERSAL"]
    universal.sort(key=lambda x: abs(x[1]["mean_weight"]), reverse=True)
    for feat, info in universal[:15]:
        print("    %-30s mean=%.4f  CV=%.2f" % (feat[:30], info["mean_weight"],
              info["cv"] if info["cv"] != "inf" else 99.99))

    print("\nResults saved to %s" % (OUTPUT_DIR / "domain_comparison.json"))
    return results


if __name__ == "__main__":
    main()
