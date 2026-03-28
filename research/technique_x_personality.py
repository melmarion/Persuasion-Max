#!/usr/bin/env python3
"""
Technique × Personality Interaction Matrix — The Novel Contribution
=====================================================================
For each of 40 techniques × 10 preset personas:
    - Generate synthetic stimuli deploying ONLY that technique
    - Score through full pipeline with each persona
    - Record compliance, retaliation, insula
    - Identify persona-sensitive vs persona-insensitive techniques

Output: 400-cell interaction matrix

Usage:
    python research/technique_x_personality.py
"""

import sys
import os
import json
import csv
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.appraisal_extractor import AppraisalExtractor
from core.circuit_predictor import CircuitPredictor, persuasion_effectiveness
from core.technique_detector import TechniqueDetector, TECHNIQUES
from core.technique_to_circuit import TechniqueCircuitMapper
from core.recipient_modulator import RecipientModulator
from core.recipient_profile import RecipientProfile
from core.preset_personas import (
    PRESET_PERSONAS, IMPULSE_BUYER, PRICE_HUNTER, BRAND_LOYALIST,
    SOCIAL_SHOPPER, SKEPTICAL_RESEARCHER, LIBERAL_BASE, CONSERVATIVE_BASE,
    PERSUADABLE_MODERATE, DISENGAGED_VOTER, ISSUE_ACTIVIST,
)

OUTPUT_DIR = Path(__file__).parent / "results"


# ═══════════════════════════════════════════════════════════════════════════════
# SYNTHETIC STIMULI — One per technique, designed to trigger ONLY that technique
# ═══════════════════════════════════════════════════════════════════════════════

TECHNIQUE_STIMULI = {
    "logical_appeal": [
        "Because the data shows a 47% improvement, therefore the logical conclusion is clear.",
        "Research demonstrates statistically significant results across three independent studies.",
        "The evidence logically supports this approach based on peer-reviewed findings.",
    ],
    "evidence_based": [
        "A 2024 study found that 73% of participants reported measurable improvements.",
        "According to research published in Nature, the data shows a clear correlation.",
        "Survey results from 10,000 respondents confirm a 2.3x improvement rate.",
    ],
    "expert_testimony": [
        "Dr. Sarah Chen, a leading researcher at Stanford, confirms these findings.",
        "Professor Williams, an expert in the field, recommends this approach.",
        "According to Dr. Martinez, the foremost scientist in this area, results are compelling.",
    ],
    "social_proof": [
        "Everyone is switching to this approach. Millions of people have already adopted it.",
        "Most people in the community have found this incredibly effective.",
        "Thousands of users agree — this is the most popular choice this year.",
    ],
    "authority_endorsement": [
        "Endorsed by the American Medical Association and recommended by leading institutions.",
        "Approved and certified by the FDA. Trusted by hospitals nationwide.",
        "Backed by Harvard research and recommended by top industry experts.",
    ],
    "bandwagon": [
        "Join the growing movement. Everyone's doing it — don't be left behind.",
        "The wave is building. More people are joining every day.",
        "This is the fastest-growing trend. Be part of the movement.",
    ],
    "emotional_appeal_positive": [
        "Imagine the joy of achieving your dream. Picture the beautiful moment of success.",
        "This is an amazing, wonderful opportunity that will inspire and excite you.",
        "Celebrate this incredible achievement. Hope and happiness await.",
    ],
    "emotional_appeal_negative": [
        "People are suffering and struggling. This crisis demands urgent attention.",
        "The pain of those affected is devastating and tragic.",
        "Without action, more vulnerable communities will face devastating consequences.",
    ],
    "empathy_appeal": [
        "Put yourself in their shoes. Imagine how you would feel in that situation.",
        "How would you feel if this happened to your family? Walk in their shoes.",
        "Imagine if you were the one struggling. Empathize with their experience.",
    ],
    "storytelling": [
        "I remember when I was just starting out, years ago. One day everything changed.",
        "Let me tell you a story. There was a time when I faced the same challenge.",
        "Years ago, when I was in the same position, something unexpected happened.",
    ],
    "self_disclosure": [
        "I honestly admit that I struggled with this too. To be honest, it was hard.",
        "Can I be real with you? I personally went through this exact experience.",
        "I confess I was skeptical at first. Honestly, I had my doubts.",
    ],
    "commitment_consistency": [
        "As you mentioned earlier, you agreed this was important. You committed to trying.",
        "You said you wanted to make a change. Stay consistent with your values.",
        "You promised yourself you would take action. Be consistent with that commitment.",
    ],
    "reciprocity": [
        "Here's a free gift as a thank you. No cost, no charge — it's on us.",
        "We're offering this complimentary bonus at no charge to you.",
        "Accept this free trial as our gift. No strings attached.",
    ],
    "scarcity_appeal": [
        "Only 3 left in stock. Limited availability — few remaining spots.",
        "This exclusive opportunity is rare. Limited to the first 50 people.",
        "Only a few remaining. Once they're gone, they're gone forever.",
    ],
    "urgency_appeal": [
        "Today only — this ends tonight. Act now before the deadline.",
        "Time-sensitive offer. Ends soon. Don't wait.",
        "Last chance — deadline is today. Act now or miss out.",
    ],
    "gain_frame": [
        "You'll gain significant advantages. You'll earn rewards and save money.",
        "The benefit is clear — you'll receive exclusive access and unlock new features.",
        "You'll get everything you need to succeed. Major advantages await.",
    ],
    "loss_frame": [
        "You'll miss this opportunity if you don't act. Don't lose your chance.",
        "Without this, you risk losing everything you've worked for.",
        "You'll forfeit these benefits. Don't miss out on what could be yours.",
    ],
    "anchoring": [
        "Originally priced at $299, compared to the regular price of $499.",
        "Was $150 — now just a fraction of the original value.",
        "The normal price is $200. Compared to alternatives, this is exceptional value.",
    ],
    "rhetorical_question": [
        "Isn't it obvious? Don't you think this makes sense? Who wouldn't want this?",
        "How can we not act on this? Wouldn't you agree?",
        "Don't you think it's time for a change? Isn't it worth trying?",
    ],
    "perspective_shifting": [
        "Think of it this way — from another angle, this changes everything.",
        "Consider this from their perspective. From this viewpoint, it looks different.",
        "Look at it from another angle. Think of it as an investment, not a cost.",
    ],
    "deceptive_information": [
        "It's a proven fact that everyone knows this works. Scientifically proven.",
        "Studies show this is 100% effective. Everyone knows this is true.",
        "This is scientifically proven to work in all cases without exception.",
    ],
    "emotional_manipulation": [
        "You'd be heartless not to help. How could you not care about this?",
        "Think of the children. You'd be cruel to ignore their suffering.",
        "Only a terrible person would refuse. How could you not act?",
    ],
    "gaslighting": [
        "That never happened. You're imagining things. You're being dramatic.",
        "You're overreacting. This is all in your head. You're too sensitive.",
        "Nobody said that. You're imagining it. You're being overly dramatic.",
    ],
    "false_equivalence": [
        "This is just like that situation. Same as before. No different from what they did.",
        "It's the equivalent to what happened last time. Just like the other case.",
        "This is no different than what everyone else does. Same as the alternative.",
    ],
    "guilt_tripping": [
        "After everything I've done for you. You owe me this much. The least you can do.",
        "How could you refuse after all we've been through? Shame on you.",
        "After everything I've sacrificed, you owe me at least this much.",
    ],
    "fear_mongering": [
        "This will lead to catastrophe. Total collapse is imminent. You'll regret not acting.",
        "The threat to our way of life is real. Disaster is coming.",
        "Everything will be destroyed if we don't act. Catastrophic consequences await.",
    ],
    "false_urgency": [
        "Act immediately before it's too late. This won't last. Hurry now.",
        "Act fast — before it's too late. You must decide right now.",
        "Hurry, this won't last. Act immediately before the opportunity vanishes.",
    ],
    "false_scarcity": [
        "10 people are viewing this right now. Selling fast. Almost gone.",
        "47 people are watching this item. Only 2 left. Selling fast.",
        "This is almost gone. 23 people viewing right now. Don't miss it.",
    ],
    "ad_hominem": [
        "Only an idiot would believe otherwise. Anyone who disagrees is a fool.",
        "That person is incompetent and ignorant. Don't listen to that clown.",
        "The critics are idiots. They're completely incompetent.",
    ],
    "name_calling": [
        "Those extremists and radicals are nothing but shills and puppets.",
        "The elitists and snowflakes don't understand real problems.",
        "These sheep are just puppets following their radical agenda.",
    ],
    "straw_man": [
        "So you're saying we should do nothing? Their true agenda is obvious.",
        "What they really want is complete control. Their true goal is power.",
        "So you're saying everything is fine? That's clearly not the case.",
    ],
    "whataboutism": [
        "What about what they did? But they also failed. Look at how they handled it.",
        "You too had problems. What about their record? Look at what they did.",
        "But what about the other side? They're just as bad, if not worse.",
    ],
    "false_dilemma": [
        "Either you're with us or against us. You must choose. Only two options exist.",
        "It's this or nothing. You either support us or you're part of the problem.",
        "There are only two choices here. Either act now or accept defeat.",
    ],
    "slippery_slope": [
        "This will lead to total chaos. Before you know it, everything will collapse.",
        "Where does it end? This opens the door to complete disaster.",
        "Next thing you know, they'll take everything. It's a slippery slope.",
    ],
    "red_herring": [
        "But the real issue is something else entirely. Let's not forget what really matters.",
        "More importantly, the real question is about their credibility.",
        "But what about the bigger picture? The real issue is being ignored.",
    ],
    "appeal_to_ignorance": [
        "No one has proven it's wrong. No evidence can disprove this claim.",
        "Can't prove it's not true. No one has shown otherwise.",
        "Nobody can disprove this. Until someone proves otherwise, it stands.",
    ],
    "manipulative_flattery": [
        "Someone as smart and sophisticated as you already sees the truth.",
        "You're too intelligent to fall for the other side. You're above that.",
        "A person as smart as you understands this better than most.",
    ],
    "appeal_to_pity": [
        "Please, I'm begging you. Have mercy. We're desperate for help.",
        "For the sake of our family, please have pity on us. We need you.",
        "Please, we're desperate. Have a heart. I'm begging you to help.",
    ],
    "obfuscation": [
        "The synergistic paradigm leverages the ecosystem for disruptive innovation.",
        "Our holistic framework creates synergistic value through paradigm leverage.",
        "The ecosystem-driven innovation paradigm synergistically disrupts the landscape.",
    ],
    "bandwagon_pressure": [
        "Everyone else is already doing it. You'll be the only one left behind.",
        "Don't be left out. Everyone has already joined. Don't want to be left behind.",
        "You'll be the only one not participating. Everyone else is in.",
    ],
}


def score_technique_against_persona(technique_name, persona_name, persona_profile,
                                     extractor, predictor, detector, mapper, modulator):
    """Score synthetic stimuli for a technique against a persona."""
    stimuli = TECHNIQUE_STIMULI.get(technique_name, [])
    if not stimuli:
        return None

    compliance_scores = []
    repeat_scores = []
    retaliation_scores = []

    for text in stimuli:
        # Full pipeline
        appraisal = extractor.extract(text, mode="heuristic")
        techniques = detector.detect(text, mode="heuristic")

        # Apply technique modifiers
        mod_appraisal, insula, circuit_mults = mapper.apply(
            appraisal.to_dict(), techniques, 0.0)

        # Apply recipient modulation
        from core.appraisal_extractor import AppraisalScores
        result = predictor.predict(
            AppraisalScores(**mod_appraisal),
            insula_disgust_signal=insula,
            recipient=persona_profile,
            detected_techniques=techniques.detected_names,
        )

        compliance_scores.append(result.compliance_prob)
        repeat_scores.append(result.repeat_compliance)
        retaliation_scores.append(result.retaliation_probability)

    return {
        "immediate_compliance": round(sum(compliance_scores) / len(compliance_scores), 4),
        "repeat_compliance": round(sum(repeat_scores) / len(repeat_scores), 4),
        "retaliation_probability": round(sum(retaliation_scores) / len(retaliation_scores), 4),
    }


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    extractor = AppraisalExtractor()
    predictor = CircuitPredictor()
    detector = TechniqueDetector()
    mapper = TechniqueCircuitMapper()
    modulator = RecipientModulator()

    technique_names = list(TECHNIQUES.keys())
    persona_names = list(PRESET_PERSONAS.keys())

    print("=== Technique × Personality Matrix ===")
    print("  %d techniques × %d personas = %d cells" % (
        len(technique_names), len(persona_names), len(technique_names) * len(persona_names)))

    matrix = {}
    all_cells = []

    for i, tech in enumerate(technique_names):
        matrix[tech] = {}
        for persona_name in persona_names:
            persona = PRESET_PERSONAS[persona_name]
            result = score_technique_against_persona(
                tech, persona_name, persona,
                extractor, predictor, detector, mapper, modulator,
            )
            if result:
                matrix[tech][persona_name] = result
                all_cells.append({
                    "technique": tech,
                    "persona": persona_name,
                    **result,
                })

        if (i + 1) % 10 == 0:
            print("  %d/%d techniques scored" % (i + 1, len(technique_names)))

    print("  %d cells computed" % len(all_cells))

    # Analysis
    print("\n=== Persona Sensitivity Analysis ===")
    persona_sensitive = []
    persona_insensitive = []

    for tech in technique_names:
        if tech not in matrix or not matrix[tech]:
            continue
        compliances = [v["immediate_compliance"] for v in matrix[tech].values()]
        spread = max(compliances) - min(compliances)

        if spread > 0.20:
            persona_sensitive.append((tech, round(spread, 4)))
        elif spread < 0.05:
            persona_insensitive.append((tech, round(spread, 4)))

    persona_sensitive.sort(key=lambda x: -x[1])
    print("\n  PERSONA-SENSITIVE techniques (spread > 20pp):")
    for tech, spread in persona_sensitive:
        print("    %-30s spread=%.1f%%" % (tech, spread * 100))

    print("\n  PERSONA-INSENSITIVE techniques (spread < 5pp):")
    for tech, spread in persona_insensitive:
        print("    %-30s spread=%.1f%%" % (tech, spread * 100))

    # Most resistant / susceptible personas
    print("\n=== Persona Resistance Ranking ===")
    persona_avg = {}
    for persona_name in persona_names:
        compliances = [
            matrix[tech][persona_name]["immediate_compliance"]
            for tech in technique_names
            if tech in matrix and persona_name in matrix[tech]
        ]
        if compliances:
            persona_avg[persona_name] = round(sum(compliances) / len(compliances), 4)

    for persona, avg in sorted(persona_avg.items(), key=lambda x: x[1]):
        label = "MOST RESISTANT" if avg == min(persona_avg.values()) else \
                "MOST SUSCEPTIBLE" if avg == max(persona_avg.values()) else ""
        print("  %-25s avg_compliance=%.1f%% %s" % (persona, avg * 100, label))

    # Top and bottom 10 cells
    all_cells.sort(key=lambda x: x["immediate_compliance"], reverse=True)
    print("\n=== Top 10 Highest-Compliance Combinations ===")
    for c in all_cells[:10]:
        print("  %-25s × %-25s compliance=%.1f%%" % (
            c["technique"], c["persona"], c["immediate_compliance"] * 100))

    print("\n=== Top 10 Highest-Retaliation Combinations ===")
    all_cells.sort(key=lambda x: x["retaliation_probability"], reverse=True)
    for c in all_cells[:10]:
        print("  %-25s × %-25s retaliation=%.1f%%" % (
            c["technique"], c["persona"], c["retaliation_probability"] * 100))

    # Save CSV
    csv_path = OUTPUT_DIR / "technique_x_personality.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["technique", "persona", "immediate_compliance",
                        "repeat_compliance", "retaliation_probability"])
        for c in sorted(all_cells, key=lambda x: (x["technique"], x["persona"])):
            writer.writerow([c["technique"], c["persona"],
                           c["immediate_compliance"], c["repeat_compliance"],
                           c["retaliation_probability"]])

    # Save JSON
    results = {
        "matrix": matrix,
        "persona_sensitive": persona_sensitive,
        "persona_insensitive": persona_insensitive,
        "persona_avg_compliance": persona_avg,
        "n_cells": len(all_cells),
    }
    with open(OUTPUT_DIR / "technique_x_personality.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nSaved to %s" % OUTPUT_DIR)
    return results


if __name__ == "__main__":
    main()
