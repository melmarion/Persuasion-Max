#!/usr/bin/env python3
"""
Campaign Scenario Simulations — Real-world predictions
=========================================================
4 scenarios scored against relevant personas and domains.

Usage:
    python research/campaign_scenario_test.py
"""

import sys
import os
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.appraisal_extractor import AppraisalExtractor
from core.circuit_predictor import CircuitPredictor
from core.technique_detector import TechniqueDetector
from core.technique_to_circuit import TechniqueCircuitMapper
from core.domain_predictor import DomainPredictor
from core.preset_personas import PRESET_PERSONAS

OUTPUT_DIR = Path(__file__).parent / "results"


def score_stimulus(text, persona_name=None, persona=None, domain="universal"):
    """Score a stimulus through the full pipeline."""
    extractor = AppraisalExtractor()
    predictor = CircuitPredictor()
    detector = TechniqueDetector()
    mapper = TechniqueCircuitMapper()

    appraisal = extractor.extract(text, mode="heuristic")
    techniques = detector.detect(text, mode="heuristic")
    mod_appraisal, insula, circuit_mults = mapper.apply(
        appraisal.to_dict(), techniques, 0.0)

    from core.appraisal_extractor import AppraisalScores
    result = predictor.predict(
        AppraisalScores(**mod_appraisal),
        insula_disgust_signal=insula,
        recipient=persona,
        detected_techniques=techniques.detected_names,
    )

    return {
        "persona": persona_name or "default",
        "compliance": round(result.compliance_prob, 4),
        "immediate_compliance": round(result.immediate_compliance, 4),
        "repeat_compliance": round(result.repeat_compliance, 4),
        "retaliation": round(result.retaliation_probability, 4),
        "dominant": result.circuits.dominant,
        "techniques_detected": techniques.detected_names,
    }


def scenario_1_product_launch():
    """Product launch email scored against 5 e-commerce personas."""
    print("\n=== Scenario 1: Product Launch Email ===")
    stimulus = (
        "Introducing FocusFlow — the first neural-feedback headband that adapts "
        "to your concentration patterns in real-time. Early adopters get 30% off "
        "this week only. Join 2,000+ beta testers who've already improved their "
        "focus by an average of 47%."
    )
    print("  Stimulus: %s" % stimulus[:80] + "...")

    personas = ["impulse_buyer", "price_hunter", "brand_loyalist",
                "social_shopper", "skeptical_researcher"]
    results = []
    for p_name in personas:
        r = score_stimulus(stimulus, p_name, PRESET_PERSONAS[p_name])
        results.append(r)
        print("  %-25s compliance=%.1f%% retaliation=%.1f%% dominant=%s" % (
            p_name, r["compliance"] * 100, r["retaliation"] * 100, r["dominant"]))

    return {"stimulus": stimulus, "results": results}


def scenario_2_political_climate():
    """Climate policy ad: care frame vs loyalty frame across political personas."""
    print("\n=== Scenario 2: Climate Policy Ad ===")

    care_frame = (
        "Our children deserve clean air. This climate policy protects the most "
        "vulnerable communities from the devastating effects of pollution. "
        "Think of the families suffering near industrial zones."
    )
    loyalty_frame = (
        "This is about protecting our homeland. Americans have always led the world "
        "in innovation. Stand with us to preserve our great nation's natural heritage "
        "for future generations of patriots."
    )

    personas = ["liberal_base", "conservative_base", "persuadable_moderate",
                "disengaged_voter", "issue_activist"]

    print("  Care Frame: %s" % care_frame[:60] + "...")
    print("  Loyalty Frame: %s" % loyalty_frame[:60] + "...")

    results = {}
    for frame_name, stimulus in [("care_frame", care_frame), ("loyalty_frame", loyalty_frame)]:
        results[frame_name] = []
        print("\n  --- %s ---" % frame_name)
        for p_name in personas:
            r = score_stimulus(stimulus, p_name, PRESET_PERSONAS[p_name])
            results[frame_name].append(r)
            print("  %-25s compliance=%.1f%%" % (p_name, r["compliance"] * 100))

    # Compute reframing lift
    print("\n  Moral Reframing Lift:")
    for p_name in personas:
        care_c = next(r["compliance"] for r in results["care_frame"] if r["persona"] == p_name)
        loyalty_c = next(r["compliance"] for r in results["loyalty_frame"] if r["persona"] == p_name)
        diff = (loyalty_c - care_c) * 100
        winner = "loyalty" if diff > 0 else "care"
        print("    %-25s care=%.1f%% loyalty=%.1f%% → %s wins by %.1fpp" % (
            p_name, care_c * 100, loyalty_c * 100, winner, abs(diff)))

    return {"stimuli": {"care_frame": care_frame, "loyalty_frame": loyalty_frame}, "results": results}


def scenario_3_crisis_pr():
    """Data breach: transparent vs defensive, across 5 stakeholder types."""
    print("\n=== Scenario 3: Crisis PR (Data Breach) ===")

    transparent = (
        "We failed to protect your data. On March 15, a vulnerability in our "
        "authentication system exposed 50,000 user records. We've identified the "
        "root cause, deployed a fix, and are offering free credit monitoring. "
        "Here's our full incident report."
    )
    defensive = (
        "While this incident affected some accounts, our security has always been "
        "industry-leading. What about the major breaches at our competitors last year? "
        "The real issue is the evolving threat landscape, not our security practices."
    )

    dp = DomainPredictor()
    stakeholders = ["media", "regulators", "customers", "employees", "investors"]

    results = {}
    for approach_name, stimulus in [("transparent", transparent), ("defensive", defensive)]:
        results[approach_name] = []
        print("\n  --- %s approach ---" % approach_name)
        for stype in stakeholders:
            r = dp.predict(stimulus, domain="crisis_pr", stakeholder_type=stype,
                          crisis_severity=0.7, response_timing=0.15)
            entry = {
                "stakeholder": stype,
                "trust_recovery": r.domain_outcomes.get("trust_recovery", 0),
                "brand_sentiment": r.domain_outcomes.get("brand_sentiment_shift", 0),
                "retaliation": r.retaliation_probability,
                "compliance": r.immediate_compliance,
            }
            results[approach_name].append(entry)
            print("  %-12s trust=%.1f%% sentiment=%.2f retaliation=%.1f%%" % (
                stype, entry["trust_recovery"] * 100, entry["brand_sentiment"],
                entry["retaliation"] * 100))

    return {"stimuli": {"transparent": transparent, "defensive": defensive}, "results": results}


def scenario_4_app_store():
    """App store description deploying self_disclosure + social_proof."""
    print("\n=== Scenario 4: App Store Description ===")

    stimulus = (
        "I built this app because I couldn't find anything that actually worked "
        "for building real habits. After 2 years of research into behavioral science, "
        "I made the tool I wished existed. 47,000 people are already using it to "
        "build lasting routines. Free to start — no credit card required."
    )
    print("  Stimulus: %s" % stimulus[:80] + "...")

    personas = ["impulse_buyer", "skeptical_researcher", "social_shopper",
                "brand_loyalist", "price_hunter"]
    results = []
    for p_name in personas:
        r = score_stimulus(stimulus, p_name, PRESET_PERSONAS[p_name])
        results.append(r)
        print("  %-25s compliance=%.1f%% repeat=%.1f%% techniques=%s" % (
            p_name, r["compliance"] * 100, r["repeat_compliance"] * 100,
            ", ".join(r["techniques_detected"][:3])))

    return {"stimulus": stimulus, "results": results}


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_results = {}
    all_results["scenario_1_product_launch"] = scenario_1_product_launch()
    all_results["scenario_2_climate_policy"] = scenario_2_political_climate()
    all_results["scenario_3_crisis_pr"] = scenario_3_crisis_pr()
    all_results["scenario_4_app_store"] = scenario_4_app_store()

    with open(OUTPUT_DIR / "campaign_scenarios.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print("\nAll scenarios saved to %s" % (OUTPUT_DIR / "campaign_scenarios.json"))
    return all_results


if __name__ == "__main__":
    main()
