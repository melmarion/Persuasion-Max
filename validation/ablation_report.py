#!/usr/bin/env python3
"""
Ablation Report — What matters, what doesn't
===============================================
Layer, trait, technique category, and domain weight ablation.
Identifies dead features for pruning.

Usage:
    python validation/ablation_report.py
"""

import sys
import os
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.appraisal_extractor import AppraisalExtractor, AppraisalScores
from core.circuit_predictor import CircuitPredictor, persuasion_effectiveness
from core.technique_detector import TechniqueDetector, TECHNIQUES
from core.technique_to_circuit import TechniqueCircuitMapper
from core.recipient_modulator import RecipientModulator
from core.recipient_profile import RecipientProfile
from core.domain_predictor import DomainPredictor
from core.preset_personas import PRESET_PERSONAS

OUTPUT_DIR = Path(__file__).parent.parent / "results"

# Test stimulus battery
TEST_STIMULI = [
    "50% off today only! Everyone's buying. Don't miss out. Join millions of satisfied customers.",
    "I honestly admit this changed my life. Let me tell you my story — years ago I was struggling.",
    "Research shows a 47% improvement. According to Dr. Chen at Stanford, the evidence is clear.",
    "You'll lose everything if you don't act now. Catastrophe is coming. Act immediately.",
    "Free trial, no credit card. Cancel anytime. Takes 2 minutes to start.",
]


def ablation_recipient_traits():
    """For each of 16 recipient dimensions, measure prediction impact."""
    print("\n=== Recipient Trait Ablation ===")

    predictor = CircuitPredictor()
    extractor = AppraisalExtractor()
    detector = TechniqueDetector()

    trait_names = [
        "openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism",
        "care_harm", "fairness_cheating", "loyalty_betrayal", "authority_subversion",
        "sanctity_degradation", "liberty_oppression",
        "economic_ideology", "social_ideology",
        "prior_belief", "involvement", "elaboration_likelihood",
    ]

    # Baseline: score all stimuli against all personas
    baseline_scores = {}
    for p_name, persona in PRESET_PERSONAS.items():
        scores = []
        for text in TEST_STIMULI:
            appraisal = extractor.extract(text, mode="heuristic")
            techniques = detector.detect(text, mode="heuristic")
            result = predictor.predict(
                appraisal, recipient=persona,
                detected_techniques=techniques.detected_names,
            )
            scores.append(result.compliance_prob)
        baseline_scores[p_name] = sum(scores) / len(scores)

    baseline_max = max(baseline_scores.values())
    baseline_mean = sum(baseline_scores.values()) / len(baseline_scores)

    # Ablate each trait (set to default 0.5, or 0.0 for political)
    trait_impact = {}
    for trait in trait_names:
        max_change = 0.0

        for p_name, persona in PRESET_PERSONAS.items():
            # Create modified persona with trait set to default
            modified_dict = persona.to_dict()
            default_val = 0.0 if trait in ("economic_ideology", "social_ideology") else 0.5
            modified_dict[trait] = default_val
            modified_persona = RecipientProfile(**modified_dict)

            scores = []
            for text in TEST_STIMULI:
                appraisal = extractor.extract(text, mode="heuristic")
                techniques = detector.detect(text, mode="heuristic")
                result = predictor.predict(
                    appraisal, recipient=modified_persona,
                    detected_techniques=techniques.detected_names,
                )
                scores.append(result.compliance_prob)

            modified_avg = sum(scores) / len(scores)
            change = abs(modified_avg - baseline_scores[p_name])
            max_change = max(max_change, change)

        trait_impact[trait] = round(max_change, 4)

    # Sort by impact
    sorted_traits = sorted(trait_impact.items(), key=lambda x: -x[1])

    print("\n  Trait Impact Ranking (max compliance change when ablated):")
    dead_traits = []
    for trait, impact in sorted_traits:
        label = ""
        if impact < 0.01:
            label = " ← DEAD (< 1pp)"
            dead_traits.append(trait)
        elif impact < 0.03:
            label = " ← LOW IMPACT"
        print("    %-25s %.1f%% %s" % (trait, impact * 100, label))

    return {"trait_impacts": dict(sorted_traits), "dead_traits": dead_traits}


def ablation_technique_categories():
    """Remove each technique category, measure prediction change."""
    print("\n=== Technique Category Ablation ===")

    categories = {}
    for name, tech in TECHNIQUES.items():
        cat = tech["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(name)

    predictor = CircuitPredictor()
    extractor = AppraisalExtractor()
    detector = TechniqueDetector()
    mapper = TechniqueCircuitMapper()

    # Baseline
    baseline_scores = []
    for text in TEST_STIMULI:
        appraisal = extractor.extract(text, mode="heuristic")
        techniques = detector.detect(text, mode="heuristic")
        mod_appraisal, insula, mults = mapper.apply(
            appraisal.to_dict(), techniques, 0.0)
        result = predictor.predict(AppraisalScores(**mod_appraisal), insula_disgust_signal=insula)
        baseline_scores.append(result.compliance_prob)
    baseline_avg = sum(baseline_scores) / len(baseline_scores)

    category_impact = {}
    for cat_name, tech_names in sorted(categories.items()):
        # Remove all techniques in this category from detection
        scores = []
        for text in TEST_STIMULI:
            appraisal = extractor.extract(text, mode="heuristic")
            techniques = detector.detect(text, mode="heuristic")

            # Filter out techniques in this category
            filtered_names = [n for n in techniques.detected_names if n not in tech_names]

            # Create modified TechniqueResult
            from core.technique_detector import TechniqueResult
            filtered_result = TechniqueResult(
                techniques={k: v for k, v in techniques.techniques.items()
                           if k not in tech_names},
                total_detected=len(filtered_names),
            )

            mod_appraisal, insula, mults = mapper.apply(
                appraisal.to_dict(), filtered_result, 0.0)
            result = predictor.predict(AppraisalScores(**mod_appraisal), insula_disgust_signal=insula)
            scores.append(result.compliance_prob)

        ablated_avg = sum(scores) / len(scores)
        change = abs(ablated_avg - baseline_avg)
        category_impact[cat_name] = round(change, 4)

    dead_categories = []
    print("\n  Category Impact Ranking:")
    for cat, impact in sorted(category_impact.items(), key=lambda x: -x[1]):
        techniques_in_cat = categories[cat]
        label = ""
        if impact < 0.005:
            label = " ← DEAD (< 0.5pp)"
            dead_categories.append(cat)
        print("    %-20s %.1f%%  (%d techniques: %s)" % (
            cat, impact * 100, len(techniques_in_cat),
            ", ".join(techniques_in_cat[:3]) + ("..." if len(techniques_in_cat) > 3 else "")))

    return {"category_impacts": category_impact, "dead_categories": dead_categories}


def ablation_domain_weights():
    """Compare universal vs domain-specific predictions."""
    print("\n=== Domain Weight Ablation ===")

    dp = DomainPredictor()

    test_texts = {
        "ecommerce": "Only 3 left! Was $99, now $49. Free shipping. Everyone's buying this.",
        "campaign": "Stand with us to protect our communities. Join the growing movement for change.",
        "crisis_pr": "We take full responsibility. Here's our incident report and remediation plan.",
    }

    results = {}
    for domain, text in test_texts.items():
        universal = dp.predict(text, domain="universal")
        domain_specific = dp.predict(text, domain=domain)

        compliance_diff = abs(domain_specific.immediate_compliance - universal.immediate_compliance)
        results[domain] = {
            "universal_compliance": round(universal.immediate_compliance, 4),
            "domain_compliance": round(domain_specific.immediate_compliance, 4),
            "difference_pp": round(compliance_diff * 100, 1),
            "has_domain_outcomes": len(domain_specific.domain_outcomes) > 0,
        }

        print("  %s: universal=%.1f%% domain=%.1f%% (diff=%.1fpp)" % (
            domain, universal.immediate_compliance * 100,
            domain_specific.immediate_compliance * 100, compliance_diff * 100))

    return results


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    trait_results = ablation_recipient_traits()
    category_results = ablation_technique_categories()
    domain_results = ablation_domain_weights()

    # Generate report
    md_lines = [
        "# Ablation Report",
        "",
        "**Date:** 2026-03-28",
        "",
        "## Recipient Trait Ablation",
        "",
        "Max compliance change when each trait is set to default (0.5).",
        "",
        "| Trait | Max Impact | Status |",
        "|-------|-----------|--------|",
    ]

    for trait, impact in sorted(trait_results["trait_impacts"].items(), key=lambda x: -x[1]):
        status = "DEAD" if trait in trait_results["dead_traits"] else "ACTIVE"
        md_lines.append("| %s | %.1f%% | %s |" % (trait, impact * 100, status))

    md_lines.extend([
        "",
        "Dead traits (< 1pp impact): %s" % ", ".join(trait_results["dead_traits"]),
        "",
        "## Technique Category Ablation",
        "",
        "| Category | Impact | Status |",
        "|----------|--------|--------|",
    ])

    for cat, impact in sorted(category_results["category_impacts"].items(), key=lambda x: -x[1]):
        status = "DEAD" if cat in category_results["dead_categories"] else "ACTIVE"
        md_lines.append("| %s | %.1f%% | %s |" % (cat, impact * 100, status))

    md_lines.extend([
        "",
        "Dead categories (< 0.5pp impact): %s" % ", ".join(category_results["dead_categories"]),
        "",
        "## Domain Weight Ablation",
        "",
        "| Domain | Universal | Domain-Specific | Difference |",
        "|--------|-----------|----------------|------------|",
    ])

    for domain, data in domain_results.items():
        md_lines.append("| %s | %.1f%% | %.1f%% | %.1fpp |" % (
            domain, data["universal_compliance"] * 100,
            data["domain_compliance"] * 100, data["difference_pp"]))

    md_path = OUTPUT_DIR / "ablation_report.md"
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines))

    # Save JSON
    results = {
        "trait_ablation": trait_results,
        "technique_category_ablation": category_results,
        "domain_weight_ablation": domain_results,
    }
    with open(OUTPUT_DIR / "ablation_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nReport: %s" % md_path)
    return results


if __name__ == "__main__":
    main()
