from __future__ import annotations
"""
Test Suite — Multi-Domain Calibration Pipeline
================================================
Validates that calibration scripts produce valid outputs.
"""

import sys
import os
import json
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path

passed = 0
failed = 0


def check(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print("  PASS: %s" % name)
    else:
        failed += 1
        print("  FAIL: %s %s" % (name, ("— " + detail) if detail else ""))


PARSED_DIR = Path(__file__).parent.parent / "calibration" / "parsed"
RESULTS_DIR = Path(__file__).parent.parent / "calibration" / "results"


# ═══════════════════════════════════════════════════════════════════════════════
# 1. download_datasets.py produced >0 samples from each available source
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Dataset Parser Output ===")

unified_path = PARSED_DIR / "unified_dataset.jsonl"
check("unified_dataset.jsonl exists", unified_path.exists())

if unified_path.exists():
    samples = []
    with open(unified_path) as f:
        for line in f:
            if line.strip():
                samples.append(json.loads(line))

    check("total samples > 0", len(samples) > 0, "count=%d" % len(samples))

    sources = {}
    for s in samples:
        sources[s["source"]] = sources.get(s["source"], 0) + 1

    check("daily_persuasion has >0 samples",
          sources.get("daily_persuasion", 0) > 0,
          "count=%d" % sources.get("daily_persuasion", 0))

    check("hcp has >0 samples",
          sources.get("hcp", 0) > 0,
          "count=%d" % sources.get("hcp", 0))

    # Validate sample format
    s0 = samples[0]
    check("sample has 'text' field", "text" in s0)
    check("sample has 'outcome' field", "outcome" in s0)
    check("sample has 'domain' field", "domain" in s0)
    check("sample has 'source' field", "source" in s0)
    check("outcome is float", isinstance(s0["outcome"], (int, float)))
    check("outcome in [0, 1]", 0.0 <= s0["outcome"] <= 1.0)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. fit_domain_weights.py produced valid fitted weights
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Fitted Weights Validation ===")

fit_results_path = RESULTS_DIR / "fit_results.json"
check("fit_results.json exists", fit_results_path.exists())

if fit_results_path.exists():
    with open(fit_results_path) as f:
        fit_results = json.load(f)

    # Check for per-source results
    for src in ["daily_persuasion", "hcp"]:
        if src in fit_results:
            data = fit_results[src]
            check("%s: has AUC" % src, "auc_cv" in data)
            check("%s: AUC is finite" % src,
                  isinstance(data.get("auc_cv"), (int, float)) and not math.isnan(data["auc_cv"]),
                  "auc=%s" % data.get("auc_cv"))
            check("%s: AUC > 0.5 (above chance)" % src,
                  data.get("auc_cv", 0) > 0.5,
                  "auc=%.3f" % data.get("auc_cv", 0))
            check("%s: has weights dict" % src, "weights" in data)

            if "weights" in data:
                for name, val in data["weights"].items():
                    check("%s weight %s: no NaN" % (src, name[:20]),
                          not math.isnan(val) and not math.isinf(val),
                          "value=%s" % val)
                    break  # just check first one for brevity

            if "confidence_intervals" in data:
                cis = data["confidence_intervals"]
                check("%s: has CIs" % src, len(cis) > 0)
                for name, ci in list(cis.items())[:1]:
                    check("%s CI %s: finite bounds" % (src, name[:20]),
                          ci.get("ci_lower") is not None and ci.get("ci_upper") is not None
                          and not math.isnan(ci["ci_lower"]) and not math.isnan(ci["ci_upper"]))

    # Transfer matrix
    check("transfer_matrix exists", "transfer_matrix" in fit_results)
    if "transfer_matrix" in fit_results:
        tm = fit_results["transfer_matrix"]
        check("transfer_matrix has entries", len(tm) > 0)

    # Ablation
    check("ablation results exist", "ablation" in fit_results)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. discover_interactions.py — top interaction has AUC lift > 0
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Interaction Discovery Validation ===")

interaction_path = RESULTS_DIR / "interaction_discovery.json"
check("interaction_discovery.json exists", interaction_path.exists())

if interaction_path.exists():
    with open(interaction_path) as f:
        inter_results = json.load(f)

    check("has base_auc", "base_auc" in inter_results)
    check("base_auc > 0.5", inter_results.get("base_auc", 0) > 0.5)

    top_30 = inter_results.get("top_30_interactions", [])
    check("has top interactions", len(top_30) > 0)

    if top_30:
        top1 = top_30[0]
        check("top interaction has positive AUC lift",
              top1.get("auc_lift", 0) > 0,
              "lift=%.5f" % top1.get("auc_lift", 0))
        check("top interaction has feature names",
              "feature_a" in top1 and "feature_b" in top1)

    # Stacking results
    stacking = inter_results.get("stacking_results", [])
    check("has stacking results", len(stacking) > 0)
    if stacking:
        check("stacking lift > 0",
              stacking[0].get("lift_over_linear", 0) > 0,
              "lift=%.4f" % stacking[0].get("lift_over_linear", 0))


# ═══════════════════════════════════════════════════════════════════════════════
# 4. compare_domains.py — at least 1 DOMAIN-SPECIFIC feature
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Domain Comparison Validation ===")

domain_path = RESULTS_DIR / "domain_comparison.json"
check("domain_comparison.json exists", domain_path.exists())

if domain_path.exists():
    with open(domain_path) as f:
        domain_results = json.load(f)

    counts = domain_results.get("classification_counts", {})
    check("has classification counts", len(counts) > 0)

    n_domain_specific = counts.get("DOMAIN-SPECIFIC", 0)
    check("at least 1 DOMAIN-SPECIFIC feature (validates domain registries)",
          n_domain_specific >= 1,
          "count=%d" % n_domain_specific)

    n_universal = counts.get("UNIVERSAL", 0)
    check("at least 1 UNIVERSAL feature",
          n_universal >= 1,
          "count=%d" % n_universal)

    # Check stability matrix
    matrix = domain_results.get("stability_matrix", {})
    check("stability matrix has entries", len(matrix) > 0)


# ═══════════════════════════════════════════════════════════════════════════════
# Summary
# ═══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("RESULTS: %d passed, %d failed, %d total" % (passed, failed, passed + failed))
if failed == 0:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED — review above")
print("=" * 60)

sys.exit(1 if failed > 0 else 0)
