#!/usr/bin/env python3
"""
Technique × Moral Foundations Interaction Matrix
==================================================
40 techniques × 12 MFT profiles = 480-cell matrix.
Quantifies moral reframing effect (Feinberg & Willer 2015).

Usage:
    python research/technique_x_mft.py
"""

import sys
import os
import json
import csv
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.appraisal_extractor import AppraisalExtractor
from core.circuit_predictor import CircuitPredictor
from core.technique_detector import TechniqueDetector, TECHNIQUES
from core.technique_to_circuit import TechniqueCircuitMapper
from core.recipient_profile import RecipientProfile

OUTPUT_DIR = Path(__file__).parent / "results"

# ═══════════════════════════════════════════════════════════════════════════════
# 12 SYNTHETIC MFT PROFILES
# ═══════════════════════════════════════════════════════════════════════════════

MFT_PROFILES = {
    "care_dominant": RecipientProfile(
        care_harm=0.9, fairness_cheating=0.3, loyalty_betrayal=0.3,
        authority_subversion=0.3, sanctity_degradation=0.3, liberty_oppression=0.3,
    ),
    "fairness_dominant": RecipientProfile(
        care_harm=0.3, fairness_cheating=0.9, loyalty_betrayal=0.3,
        authority_subversion=0.3, sanctity_degradation=0.3, liberty_oppression=0.3,
    ),
    "loyalty_dominant": RecipientProfile(
        care_harm=0.3, fairness_cheating=0.3, loyalty_betrayal=0.9,
        authority_subversion=0.3, sanctity_degradation=0.3, liberty_oppression=0.3,
    ),
    "authority_dominant": RecipientProfile(
        care_harm=0.3, fairness_cheating=0.3, loyalty_betrayal=0.3,
        authority_subversion=0.9, sanctity_degradation=0.3, liberty_oppression=0.3,
    ),
    "sanctity_dominant": RecipientProfile(
        care_harm=0.3, fairness_cheating=0.3, loyalty_betrayal=0.3,
        authority_subversion=0.3, sanctity_degradation=0.9, liberty_oppression=0.3,
    ),
    "liberty_dominant": RecipientProfile(
        care_harm=0.3, fairness_cheating=0.3, loyalty_betrayal=0.3,
        authority_subversion=0.3, sanctity_degradation=0.3, liberty_oppression=0.9,
    ),
    "liberal_mft": RecipientProfile(
        care_harm=0.9, fairness_cheating=0.9, loyalty_betrayal=0.3,
        authority_subversion=0.3, sanctity_degradation=0.2, liberty_oppression=0.8,
        economic_ideology=-0.6, social_ideology=-0.5,
    ),
    "conservative_mft": RecipientProfile(
        care_harm=0.5, fairness_cheating=0.5, loyalty_betrayal=0.8,
        authority_subversion=0.8, sanctity_degradation=0.8, liberty_oppression=0.4,
        economic_ideology=0.6, social_ideology=0.5,
    ),
    "balanced_mft": RecipientProfile(
        care_harm=0.5, fairness_cheating=0.5, loyalty_betrayal=0.5,
        authority_subversion=0.5, sanctity_degradation=0.5, liberty_oppression=0.5,
    ),
    "low_moral": RecipientProfile(
        care_harm=0.2, fairness_cheating=0.2, loyalty_betrayal=0.2,
        authority_subversion=0.2, sanctity_degradation=0.2, liberty_oppression=0.2,
    ),
    "high_moral": RecipientProfile(
        care_harm=0.9, fairness_cheating=0.9, loyalty_betrayal=0.9,
        authority_subversion=0.9, sanctity_degradation=0.9, liberty_oppression=0.9,
    ),
    "inverted": RecipientProfile(
        care_harm=0.2, fairness_cheating=0.2, loyalty_betrayal=0.9,
        authority_subversion=0.9, sanctity_degradation=0.9, liberty_oppression=0.2,
    ),
}

# Import technique stimuli from the personality module
from research.technique_x_personality import TECHNIQUE_STIMULI


def score_technique_against_mft(technique_name, profile, extractor, predictor, detector, mapper):
    """Score stimuli for a technique against an MFT profile."""
    stimuli = TECHNIQUE_STIMULI.get(technique_name, [])
    if not stimuli:
        return None

    compliance_scores = []
    retaliation_scores = []
    insula_scores = []

    for text in stimuli:
        appraisal = extractor.extract(text, mode="heuristic")
        techniques = detector.detect(text, mode="heuristic")
        mod_appraisal, insula, circuit_mults = mapper.apply(
            appraisal.to_dict(), techniques, 0.0)

        from core.appraisal_extractor import AppraisalScores
        result = predictor.predict(
            AppraisalScores(**mod_appraisal),
            insula_disgust_signal=insula,
            recipient=profile,
            detected_techniques=techniques.detected_names,
        )

        compliance_scores.append(result.compliance_prob)
        retaliation_scores.append(result.retaliation_probability)
        # Compute insula from prediction context
        insula_scores.append(min(1.0, max(0.0, insula)))

    return {
        "immediate_compliance": round(sum(compliance_scores) / len(compliance_scores), 4),
        "retaliation_probability": round(sum(retaliation_scores) / len(retaliation_scores), 4),
        "insula_activation": round(sum(insula_scores) / len(insula_scores), 4),
    }


def quantify_moral_reframing():
    """Quantify the Feinberg & Willer (2015) moral reframing effect.

    Same environmental policy, two frames:
        Frame 1 (care/fairness): appeals to protecting communities
        Frame 2 (loyalty/sanctity): appeals to national heritage

    Score each against liberal_mft vs conservative_mft.
    The crossover is the moral reframing effect.
    """
    extractor = AppraisalExtractor()
    predictor = CircuitPredictor()
    detector = TechniqueDetector()
    mapper = TechniqueCircuitMapper()

    care_frame = (
        "Our children deserve clean air and water. This environmental policy "
        "protects the most vulnerable communities from suffering. We have a "
        "moral obligation to care for those who cannot protect themselves."
    )
    loyalty_frame = (
        "Protecting our natural heritage is a matter of national pride. "
        "Americans have always been stewards of this great land. This policy "
        "preserves the sacred beauty of our homeland for future generations."
    )

    results = {}
    for frame_name, frame_text in [("care_frame", care_frame), ("loyalty_frame", loyalty_frame)]:
        for profile_name in ["liberal_mft", "conservative_mft"]:
            profile = MFT_PROFILES[profile_name]

            appraisal = extractor.extract(frame_text, mode="heuristic")
            techniques = detector.detect(frame_text, mode="heuristic")
            mod_appraisal, insula, circuit_mults = mapper.apply(
                appraisal.to_dict(), techniques, 0.0)

            from core.appraisal_extractor import AppraisalScores
            result = predictor.predict(
                AppraisalScores(**mod_appraisal),
                insula_disgust_signal=insula,
                recipient=profile,
                detected_techniques=techniques.detected_names,
            )

            key = "%s_%s" % (frame_name, profile_name)
            results[key] = round(result.compliance_prob, 4)

    # Compute reframing effect
    # For conservatives: loyalty_frame should work better than care_frame
    conservative_lift = results["loyalty_frame_conservative_mft"] - results["care_frame_conservative_mft"]
    # For liberals: care_frame should work better than loyalty_frame
    liberal_lift = results["care_frame_liberal_mft"] - results["loyalty_frame_liberal_mft"]

    return {
        "scores": results,
        "conservative_reframing_lift_pp": round(conservative_lift * 100, 1),
        "liberal_reframing_lift_pp": round(liberal_lift * 100, 1),
        "crossover_exists": conservative_lift > 0 and liberal_lift > 0,
        "total_reframing_effect_pp": round((conservative_lift + liberal_lift) * 100, 1),
    }


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    extractor = AppraisalExtractor()
    predictor = CircuitPredictor()
    detector = TechniqueDetector()
    mapper = TechniqueCircuitMapper()

    technique_names = list(TECHNIQUES.keys())
    profile_names = list(MFT_PROFILES.keys())

    print("=== Technique × MFT Matrix ===")
    print("  %d techniques × %d MFT profiles = %d cells" % (
        len(technique_names), len(profile_names), len(technique_names) * len(profile_names)))

    matrix = {}
    all_cells = []

    for i, tech in enumerate(technique_names):
        matrix[tech] = {}
        for prof_name in profile_names:
            profile = MFT_PROFILES[prof_name]
            result = score_technique_against_mft(
                tech, profile, extractor, predictor, detector, mapper)
            if result:
                matrix[tech][prof_name] = result
                all_cells.append({"technique": tech, "mft_profile": prof_name, **result})

        if (i + 1) % 10 == 0:
            print("  %d/%d techniques scored" % (i + 1, len(technique_names)))

    print("  %d cells computed" % len(all_cells))

    # Highest insula per MFT profile
    print("\n=== Highest Insula Activation per MFT Profile ===")
    for prof_name in profile_names:
        prof_cells = [c for c in all_cells if c["mft_profile"] == prof_name]
        if prof_cells:
            top = max(prof_cells, key=lambda x: x["insula_activation"])
            print("  %-20s: %-25s insula=%.2f" % (
                prof_name, top["technique"], top["insula_activation"]))

    # Moral reframing quantification
    print("\n=== Moral Reframing Quantification (Feinberg & Willer 2015) ===")
    reframing = quantify_moral_reframing()
    print("  Care frame + liberal:       %.1f%% compliance" % (reframing["scores"]["care_frame_liberal_mft"] * 100))
    print("  Care frame + conservative:  %.1f%% compliance" % (reframing["scores"]["care_frame_conservative_mft"] * 100))
    print("  Loyalty frame + liberal:    %.1f%% compliance" % (reframing["scores"]["loyalty_frame_liberal_mft"] * 100))
    print("  Loyalty frame + conservative: %.1f%% compliance" % (reframing["scores"]["loyalty_frame_conservative_mft"] * 100))
    print("  Conservative reframing lift: %.1fpp" % reframing["conservative_reframing_lift_pp"])
    print("  Liberal reframing lift:      %.1fpp" % reframing["liberal_reframing_lift_pp"])
    print("  Crossover exists:            %s" % reframing["crossover_exists"])

    # Save CSV
    csv_path = OUTPUT_DIR / "technique_x_mft.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["technique", "mft_profile", "immediate_compliance",
                        "retaliation_probability", "insula_activation"])
        for c in sorted(all_cells, key=lambda x: (x["technique"], x["mft_profile"])):
            writer.writerow([c["technique"], c["mft_profile"],
                           c["immediate_compliance"], c["retaliation_probability"],
                           c["insula_activation"]])

    # Save JSON
    results = {
        "matrix": matrix,
        "moral_reframing": reframing,
        "n_cells": len(all_cells),
    }
    with open(OUTPUT_DIR / "technique_x_mft.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nSaved to %s" % OUTPUT_DIR)
    return results


if __name__ == "__main__":
    main()
