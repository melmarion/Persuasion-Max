#!/usr/bin/env python3
"""
Compound Technique Calibration — Measure actual co-occurrence effectiveness
===========================================================================
For each compound stack in compound_techniques.py:
    1. Find samples where ALL component techniques are detected
    2. Find samples where NONE of the component techniques are detected
    3. Compute empirical success rate for both groups
    4. The ratio = empirical multiplier (replaces hand-assigned estimate)

Also measures diminishing returns empirically:
    - Group samples by number of techniques detected (0, 1, 2, 3, 4, 5+)
    - Compute success rate per group
    - Fit the diminishing returns curve

Uses the pre-featurized 126K dataset from calibration/fit_domain_weights.

Usage:
    python calibration/calibrate_compounds.py
"""

import sys
import os
import json
import time
import numpy as np
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calibration.fit_domain_weights import (
    load_samples, extract_features, TECHNIQUE_NAMES, ALL_FEATURE_NAMES,
)
from core.technique_detector import TechniqueDetector, TECHNIQUES
from core.appraisal_extractor import AppraisalExtractor
from core.compound_techniques import COMPOUND_STACKS

OUTPUT_DIR = Path(__file__).parent.parent / "calibration" / "results"


def featurize_with_cache(samples, max_samples=20000):
    """Featurize samples with technique detection, using cache if available."""
    cache_path = OUTPUT_DIR / "featurized_cache.npz"

    if cache_path.exists():
        print("Loading cached features...")
        data = np.load(cache_path, allow_pickle=True)
        return data["X"], data["y"], data["tech_matrix"]

    print("Featurizing %d samples (this takes a few minutes)..." % min(len(samples), max_samples))
    extractor = AppraisalExtractor()
    detector = TechniqueDetector()

    subset = samples[:max_samples]
    X = []
    y = []
    tech_names = list(TECHNIQUES.keys())
    tech_matrix = []  # N × n_techniques binary matrix

    for i, sample in enumerate(subset):
        if i % 1000 == 0 and i > 0:
            print("  %d/%d..." % (i, len(subset)))

        text = sample["text"]
        outcome = sample["outcome"]

        features = extract_features(text, extractor, detector)
        X.append(features)
        y.append(outcome)

        # Also store binary technique detection for compound analysis
        techniques = detector.detect(text, mode="heuristic")
        tech_row = []
        for name in tech_names:
            t = techniques.techniques.get(name, {})
            tech_row.append(1.0 if t.get("detected") else 0.0)
        tech_matrix.append(tech_row)

    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    tech_matrix = np.array(tech_matrix, dtype=np.float64)

    # Cache for reuse
    np.savez(cache_path, X=X, y=y, tech_matrix=tech_matrix)
    print("Cached to %s" % cache_path)

    return X, y, tech_matrix


def calibrate_compounds(tech_matrix, y, tech_names):
    """Measure empirical effectiveness of each compound stack."""
    results = {}

    # Baseline: overall success rate
    baseline_rate = y.mean()
    print("\nBaseline success rate: %.1f%% (N=%d)" % (baseline_rate * 100, len(y)))

    for stack_name, stack in COMPOUND_STACKS.items():
        techniques = stack["techniques"]

        # Find indices for component techniques
        indices = []
        missing = []
        for t in techniques:
            if t in tech_names:
                indices.append(tech_names.index(t))
            else:
                missing.append(t)

        if missing:
            print("  %s: SKIP — techniques not in feature set: %s" % (stack_name, missing))
            results[stack_name] = {
                "status": "missing_techniques",
                "missing": missing,
            }
            continue

        # Samples where ALL component techniques detected
        all_present = np.all(tech_matrix[:, indices] > 0, axis=1)
        n_present = all_present.sum()

        # Samples where NONE of the component techniques detected
        none_present = np.all(tech_matrix[:, indices] == 0, axis=1)
        n_absent = none_present.sum()

        if n_present < 10:
            print("  %s: TOO FEW — only %d samples with all techniques" % (stack_name, n_present))
            results[stack_name] = {
                "status": "insufficient_data",
                "n_co_occurring": int(n_present),
                "hand_assigned_multiplier": stack["multiplier"],
            }
            continue

        rate_present = y[all_present].mean()
        rate_absent = y[none_present].mean() if n_absent > 10 else baseline_rate

        empirical_multiplier = rate_present / max(rate_absent, 0.01)

        results[stack_name] = {
            "status": "calibrated",
            "n_co_occurring": int(n_present),
            "n_absent": int(n_absent),
            "success_rate_present": round(float(rate_present), 4),
            "success_rate_absent": round(float(rate_absent), 4),
            "empirical_multiplier": round(float(empirical_multiplier), 3),
            "hand_assigned_multiplier": stack["multiplier"],
            "delta": round(float(empirical_multiplier - stack["multiplier"]), 3),
            "techniques": techniques,
        }

        print("  %s: empirical=%.2fx vs hand=%.2fx (N=%d co-occurring, rate=%.1f%% vs %.1f%%)" % (
            stack_name, empirical_multiplier, stack["multiplier"],
            n_present, rate_present * 100, rate_absent * 100))

    return results


def calibrate_diminishing_returns(tech_matrix, y):
    """Measure success rate by number of techniques detected."""
    tech_counts = tech_matrix.sum(axis=1).astype(int)

    results = {}
    print("\n=== Diminishing Returns Curve ===")

    for n in range(0, 8):
        if n < 7:
            mask = tech_counts == n
        else:
            mask = tech_counts >= 7

        count = mask.sum()
        if count < 20:
            continue

        rate = y[mask].mean()
        label = "%d" % n if n < 7 else "7+"
        results[label] = {
            "n_samples": int(count),
            "success_rate": round(float(rate), 4),
        }
        print("  %s techniques: %.1f%% success (N=%d)" % (label, rate * 100, count))

    # Compute per-technique marginal lift
    baseline = results.get("0", {}).get("success_rate", 0.5)
    print("\nMarginal lift per additional technique:")
    prev_rate = baseline
    for n in range(1, 7):
        label = str(n)
        if label in results:
            rate = results[label]["success_rate"]
            marginal = rate - prev_rate
            results[label]["marginal_lift"] = round(float(marginal), 4)
            print("  %s → %s: %+.1fpp" % (str(n - 1), label, marginal * 100))
            prev_rate = rate

    return results


def main():
    print("Loading dataset...")
    samples = load_samples()
    print("Loaded %d samples" % len(samples))

    tech_names = list(TECHNIQUES.keys())

    X, y, tech_matrix = featurize_with_cache(samples, max_samples=20000)
    print("Feature matrix: %s, Tech matrix: %s" % (X.shape, tech_matrix.shape))

    # Calibrate compound stacks
    print("\n=== Compound Stack Calibration ===")
    compound_results = calibrate_compounds(tech_matrix, y, tech_names)

    # Calibrate diminishing returns
    dr_results = calibrate_diminishing_returns(tech_matrix, y)

    # Save results
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output = {
        "n_samples": int(len(y)),
        "baseline_success_rate": round(float(y.mean()), 4),
        "compound_stacks": compound_results,
        "diminishing_returns": dr_results,
    }

    output_path = OUTPUT_DIR / "compound_calibration.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print("\nResults saved to %s" % output_path)

    # Summary
    calibrated = [k for k, v in compound_results.items() if v.get("status") == "calibrated"]
    insufficient = [k for k, v in compound_results.items() if v.get("status") == "insufficient_data"]
    missing = [k for k, v in compound_results.items() if v.get("status") == "missing_techniques"]

    print("\n=== Summary ===")
    print("Calibrated: %d stacks" % len(calibrated))
    print("Insufficient data: %d stacks" % len(insufficient))
    print("Missing techniques: %d stacks" % len(missing))

    if calibrated:
        print("\nCalibrated stacks (empirical vs hand-assigned):")
        for name in calibrated:
            r = compound_results[name]
            print("  %s: %.2fx empirical vs %.2fx hand (delta=%+.2f)" % (
                name, r["empirical_multiplier"], r["hand_assigned_multiplier"], r["delta"]))


if __name__ == "__main__":
    main()
