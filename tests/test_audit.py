from __future__ import annotations
"""
Test Suite — Validation Audit Outputs
========================================
"""

import sys
import os
import json
import csv

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


RESULTS_DIR = Path(__file__).parent.parent / "results"


# ═══════════════════════════════════════════════════════════════════════════════
# 1. Full audit produced valid results
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Full Audit ===")

audit_path = RESULTS_DIR / "full_audit_results.json"
check("full_audit_results.json exists", audit_path.exists())

if audit_path.exists():
    with open(audit_path) as f:
        audit = json.load(f)

    for corpus in ["daily_persuasion", "hcp"]:
        if corpus in audit:
            data = audit[corpus]
            check("%s: has results" % corpus, "L2_appraisal_only" in data)
            if "L2_appraisal_only" in data:
                auc = data["L2_appraisal_only"]["auc"]
                check("%s: appraisal AUC > 0.5" % corpus, auc > 0.5, "auc=%.4f" % auc)
            if "L1+L2_ling+appraisal" in data:
                auc = data["L1+L2_ling+appraisal"]["auc"]
                check("%s: ling+appraisal AUC > appraisal" % corpus,
                      auc > data["L2_appraisal_only"]["auc"],
                      "ling=%.4f appraisal=%.4f" % (auc, data["L2_appraisal_only"]["auc"]))


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Weight registry is valid CSV
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Weight Registry ===")

csv_path = RESULTS_DIR / "weight_registry.csv"
check("weight_registry.csv exists", csv_path.exists())

if csv_path.exists():
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    check("registry has >100 entries", len(rows) > 100, "count=%d" % len(rows))

    # Check required columns
    required = ["weight_name", "module", "value", "provenance"]
    for col in required:
        check("has column: %s" % col, col in rows[0] if rows else False)

    # No empty weight names
    empty_names = sum(1 for r in rows if not r.get("weight_name", "").strip())
    check("no empty weight names", empty_names == 0, "empty=%d" % empty_names)

    # Provenance values are valid
    valid_prov = {"FITTED", "CALIBRATED", "CONSTRAINED", "UNCALIBRATED"}
    invalid_prov = sum(1 for r in rows if r.get("provenance", "") not in valid_prov)
    check("all provenance values valid", invalid_prov == 0, "invalid=%d" % invalid_prov)

summary_path = RESULTS_DIR / "weight_audit_summary.md"
check("weight_audit_summary.md exists", summary_path.exists())
if summary_path.exists():
    content = summary_path.read_text()
    check("summary >500 chars", len(content) > 500, "len=%d" % len(content))


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Ablation report identifies dead features
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Ablation Report ===")

ablation_json = RESULTS_DIR / "ablation_results.json"
check("ablation_results.json exists", ablation_json.exists())

if ablation_json.exists():
    with open(ablation_json) as f:
        ablation = json.load(f)

    trait = ablation.get("trait_ablation", {})
    check("trait ablation has results", len(trait.get("trait_impacts", {})) > 0)
    check("at least 1 dead trait identified",
          len(trait.get("dead_traits", [])) >= 1,
          "dead=%s" % trait.get("dead_traits", []))

    cat = ablation.get("technique_category_ablation", {})
    check("technique category ablation has results",
          len(cat.get("category_impacts", {})) > 0)

    domain = ablation.get("domain_weight_ablation", {})
    check("domain ablation has results", len(domain) > 0)
    if "ecommerce" in domain:
        check("ecommerce domain weights make >5pp difference",
              domain["ecommerce"]["difference_pp"] > 5,
              "diff=%.1f" % domain["ecommerce"]["difference_pp"])

ablation_md = RESULTS_DIR / "ablation_report.md"
check("ablation_report.md exists", ablation_md.exists())


# ═══════════════════════════════════════════════════════════════════════════════
# 4. README is paper-shaped
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== README ===")

readme_path = Path(__file__).parent.parent / "README.md"
check("README.md exists", readme_path.exists())

if readme_path.exists():
    content = readme_path.read_text()
    check("README >2000 words", len(content.split()) > 2000,
          "words=%d" % len(content.split()))

    sections = ["Abstract", "Architecture", "Related Work", "Running",
                "Honest Limitations", "References"]
    for section in sections:
        check("README has '%s' section" % section,
              section in content or section.lower() in content.lower())


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
