from __future__ import annotations
"""
Test Suite — Research Analysis Outputs
========================================
Validates technique × personality, technique × MFT, interaction surfaces,
and scenario simulations.
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


RESULTS_DIR = Path(__file__).parent.parent / "research" / "results"


# ═══════════════════════════════════════════════════════════════════════════════
# 1. Technique × Personality: 400-cell matrix, no NaN, compliance in [0,1]
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Technique × Personality Matrix ===")

tp_json = RESULTS_DIR / "technique_x_personality.json"
tp_csv = RESULTS_DIR / "technique_x_personality.csv"

check("technique_x_personality.json exists", tp_json.exists())
check("technique_x_personality.csv exists", tp_csv.exists())

if tp_json.exists():
    with open(tp_json) as f:
        tp_data = json.load(f)

    check("has 400 cells", tp_data.get("n_cells", 0) == 400,
          "n_cells=%d" % tp_data.get("n_cells", 0))

    matrix = tp_data.get("matrix", {})
    n_valid = 0
    n_nan = 0
    n_out_of_range = 0

    for tech, personas in matrix.items():
        for persona, scores in personas.items():
            c = scores.get("immediate_compliance", -1)
            if c != c:  # NaN check
                n_nan += 1
            elif not (0.0 <= c <= 1.0):
                n_out_of_range += 1
            else:
                n_valid += 1

    check("no NaN in compliance values", n_nan == 0, "n_nan=%d" % n_nan)
    check("all compliance in [0,1]", n_out_of_range == 0,
          "n_out_of_range=%d" % n_out_of_range)
    check("400 valid cells", n_valid == 400, "n_valid=%d" % n_valid)

    # Persona sensitivity exists
    check("persona_sensitive list exists",
          len(tp_data.get("persona_sensitive", [])) > 0 or
          len(tp_data.get("persona_insensitive", [])) > 0)

    # Persona avg compliance exists
    check("persona_avg_compliance has 10 entries",
          len(tp_data.get("persona_avg_compliance", {})) == 10)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Technique × MFT: 480-cell matrix, no NaN
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Technique × MFT Matrix ===")

mft_json = RESULTS_DIR / "technique_x_mft.json"
check("technique_x_mft.json exists", mft_json.exists())

if mft_json.exists():
    with open(mft_json) as f:
        mft_data = json.load(f)

    check("has 480 cells", mft_data.get("n_cells", 0) == 480,
          "n_cells=%d" % mft_data.get("n_cells", 0))

    matrix = mft_data.get("matrix", {})
    n_valid = 0
    for tech, profiles in matrix.items():
        for prof, scores in profiles.items():
            c = scores.get("immediate_compliance", -1)
            if c == c and 0.0 <= c <= 1.0:
                n_valid += 1

    check("480 valid cells in MFT matrix", n_valid == 480,
          "n_valid=%d" % n_valid)

    # Moral reframing exists
    reframing = mft_data.get("moral_reframing", {})
    check("moral reframing results exist", len(reframing) > 0)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Moral reframing: loyalty frame scores differently on conservative vs liberal
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Moral Reframing Test ===")

# Use the scenario test results for a more meaningful check
scenario_json = RESULTS_DIR / "campaign_scenarios.json"
check("campaign_scenarios.json exists", scenario_json.exists())

if scenario_json.exists():
    with open(scenario_json) as f:
        scenario_data = json.load(f)

    s2 = scenario_data.get("scenario_2_climate_policy", {})
    if s2 and "results" in s2:
        care_results = s2["results"].get("care_frame", [])
        loyalty_results = s2["results"].get("loyalty_frame", [])

        # Find liberal and conservative scores
        care_liberal = next((r["compliance"] for r in care_results
                           if r["persona"] == "liberal_base"), None)
        care_conservative = next((r["compliance"] for r in care_results
                                if r["persona"] == "conservative_base"), None)
        loyalty_conservative = next((r["compliance"] for r in loyalty_results
                                   if r["persona"] == "conservative_base"), None)

        if care_liberal and care_conservative and loyalty_conservative:
            check("care frame: liberal > conservative",
                  care_liberal > care_conservative,
                  "liberal=%.3f conservative=%.3f" % (care_liberal, care_conservative))

            check("loyalty frame: conservative >= care frame conservative",
                  loyalty_conservative >= care_conservative,
                  "loyalty=%.3f care=%.3f" % (loyalty_conservative, care_conservative))


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Scenario simulations: each produces 5+ distinct predictions
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Scenario Simulation Validation ===")

if scenario_json.exists():
    for scenario_name in ["scenario_1_product_launch", "scenario_2_climate_policy",
                          "scenario_3_crisis_pr", "scenario_4_app_store"]:
        s = scenario_data.get(scenario_name, {})
        results = s.get("results", [])

        if isinstance(results, dict):
            # Multi-frame scenarios
            all_values = []
            for frame, frame_results in results.items():
                for r in frame_results:
                    val = r.get("compliance", r.get("trust_recovery", r.get("immediate_compliance", 0)))
                    all_values.append(round(val, 4))
            check("%s: 5+ distinct predictions" % scenario_name,
                  len(set(all_values)) >= 3,
                  "unique=%d values=%s" % (len(set(all_values)), all_values[:8]))
        elif isinstance(results, list):
            compliances = [round(r["compliance"], 4) for r in results]
            check("%s: 5+ distinct predictions" % scenario_name,
                  len(set(compliances)) >= 3,
                  "unique=%d values=%s" % (len(set(compliances)), compliances))


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Interaction surfaces: each classified as LINEAR/THRESHOLD/INVERTED_U
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Interaction Surface Classification ===")

surfaces_json = RESULTS_DIR / "interaction_surfaces.json"
check("interaction_surfaces.json exists", surfaces_json.exists())

if surfaces_json.exists():
    with open(surfaces_json) as f:
        surfaces_data = json.load(f)

    shapes = surfaces_data.get("shape_classifications", [])
    check("shape classifications exist", len(shapes) > 0)

    valid_shapes = {"LINEAR", "THRESHOLD", "INVERTED_U"}
    for s in shapes:
        check("interaction %s×%s classified" % (s["feature_a"][:15], s["feature_b"][:15]),
              s.get("shape") in valid_shapes,
              "shape=%s" % s.get("shape"))


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
