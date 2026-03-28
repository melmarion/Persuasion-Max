from __future__ import annotations
"""
Technique-to-Circuit Mapper — How each technique modifies brain circuits
=========================================================================
Each of the 40 techniques shifts specific appraisal dimensions and/or
directly modifies circuit activations. These modifiers are applied
AFTER appraisal extraction and BEFORE circuit computation.

Provenance:
    CONSTRAINED — modifier direction and magnitude bounded by literature
    UNCALIBRATED — direction from theory, magnitude invented
"""

from core.technique_detector import TechniqueResult


# ═══════════════════════════════════════════════════════════════════════════════
# MODIFIER MAP — Every technique's effect on the pipeline
# ═══════════════════════════════════════════════════════════════════════════════
# Format: technique_name → {appraisal_shifts: {dim: delta}, circuit_mods: {circuit: multiplier},
#                           insula_mod: float, provenance: str}

TECHNIQUE_MODIFIERS = {
    # ─── ETHICAL TECHNIQUES ──────────────────────────────────────────────

    "logical_appeal": {
        "appraisal_shifts": {"certainty": +0.15},
        "circuit_mods": {"deliberation": 1.15},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Petty & Cacioppo 1986 — central route processing increases with argument quality",
    },
    "evidence_based": {
        "appraisal_shifts": {"certainty": +0.20, "coping_potential": +0.05},
        "circuit_mods": {},
        "insula_mod": -0.05,
        "provenance": "CONSTRAINED: specific numbers increase perceived credibility (processing fluency)",
    },
    "expert_testimony": {
        "appraisal_shifts": {"certainty": +0.15},
        "circuit_mods": {"deliberation": 0.85},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Milgram 1963 — authority reduces independent evaluation",
    },
    "social_proof": {
        "appraisal_shifts": {"certainty": +0.20, "goal_relevance": +0.05},
        "circuit_mods": {"deliberation": 0.80},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: A/B data — social proof +34% conversion at decision point",
    },
    "authority_endorsement": {
        "appraisal_shifts": {"certainty": +0.15},
        "circuit_mods": {"deliberation": 0.85},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: same mechanism as expert_testimony, institutional source",
    },
    "bandwagon": {
        "appraisal_shifts": {"certainty": +0.10, "temporal_proximity": +0.05},
        "circuit_mods": {"deliberation": 0.85},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Salganik 2006 — social cascades are self-fulfilling",
    },
    "emotional_appeal_positive": {
        "appraisal_shifts": {"valence": +0.20},
        "circuit_mods": {"approach": 1.15, "deliberation": 0.90},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Brady 2017 — moral-emotional words +20% diffusion",
    },
    "emotional_appeal_negative": {
        "appraisal_shifts": {"valence": -0.15, "goal_relevance": +0.10},
        "circuit_mods": {"avoidance": 1.10},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: negative affect increases attention allocation",
    },
    "empathy_appeal": {
        "appraisal_shifts": {"goal_relevance": +0.15, "valence": +0.05},
        "circuit_mods": {},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: TPJ perspective-taking increases goal relevance assessment",
    },
    "storytelling": {
        "appraisal_shifts": {"valence": +0.10, "goal_relevance": +0.10},
        "circuit_mods": {"deliberation": 0.70},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Green & Brock 2000 — narrative transportation reduces critical evaluation",
    },
    "self_disclosure": {
        "appraisal_shifts": {"valence": +0.10, "agency": +0.05},
        "circuit_mods": {},
        "insula_mod": -0.10,
        "provenance": "CONSTRAINED: Collins & Miller 1994 — self-disclosure creates reciprocal liking",
    },
    "commitment_consistency": {
        "appraisal_shifts": {"certainty": +0.10, "agency": -0.05},
        "circuit_mods": {},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Cialdini 2001 — consistency principle",
    },
    "reciprocity": {
        "appraisal_shifts": {"valence": +0.15, "agency": -0.10},
        "circuit_mods": {"approach": 1.10},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: vmPFC debt-tracking activates compliance to restore balance",
    },
    "scarcity_appeal": {
        "appraisal_shifts": {"temporal_proximity": +0.25, "agency": -0.10},
        "circuit_mods": {"avoidance": 1.10, "deliberation": 0.85},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: real scarcity increases NAc valuation (variable-ratio)",
    },
    "urgency_appeal": {
        "appraisal_shifts": {"temporal_proximity": +0.25},
        "circuit_mods": {"deliberation": 0.80},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: A/B data — urgency 10-30% conversion lift when real",
    },
    "gain_frame": {
        "appraisal_shifts": {"valence": +0.10},
        "circuit_mods": {"approach": 1.05},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Kahneman & Tversky 1979 — gain framing produces moderate approach",
    },
    "loss_frame": {
        "appraisal_shifts": {"valence": -0.10},
        "circuit_mods": {"avoidance": 1.15, "approach": 1.10},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: loss aversion ~2x gain — avoidance AND approach both increase",
    },
    "anchoring": {
        "appraisal_shifts": {"certainty": +0.10},
        "circuit_mods": {"deliberation": 0.90},
        "insula_mod": 0.0,
        "provenance": "CONSTRAINED: Tversky & Kahneman 1974 — anchoring shifts reference point",
    },
    "rhetorical_question": {
        "appraisal_shifts": {"goal_relevance": +0.10},
        "circuit_mods": {},
        "insula_mod": 0.0,
        "provenance": "UNCALIBRATED: rhetorical questions activate self-referential processing",
    },
    "perspective_shifting": {
        "appraisal_shifts": {"novelty": +0.10, "goal_relevance": +0.10},
        "circuit_mods": {},
        "insula_mod": 0.0,
        "provenance": "UNCALIBRATED: reframing activates TPJ perspective-taking",
    },

    # ─── UNETHICAL TECHNIQUES ────────────────────────────────────────────

    "deceptive_information": {
        "appraisal_shifts": {"certainty": +0.15},
        "circuit_mods": {},
        "insula_mod": +0.20,
        "provenance": "CONSTRAINED: false certainty triggers insula when detected",
    },
    "emotional_manipulation": {
        "appraisal_shifts": {"valence": -0.15, "agency": -0.20},
        "circuit_mods": {"avoidance": 1.20},
        "insula_mod": +0.25,
        "provenance": "CONSTRAINED: Craig 2009 — agency violation + emotional exploitation = disgust",
    },
    "gaslighting": {
        "appraisal_shifts": {"certainty": -0.25, "agency": -0.30},
        "circuit_mods": {"deliberation": 1.30},
        "insula_mod": +0.30,
        "provenance": "CONSTRAINED: undermines confidence in own judgment, high insula activation",
    },
    "false_equivalence": {
        "appraisal_shifts": {"certainty": -0.10},
        "circuit_mods": {"deliberation": 1.10},
        "insula_mod": +0.10,
        "provenance": "UNCALIBRATED: creates false decision framework",
    },
    "guilt_tripping": {
        "appraisal_shifts": {"valence": -0.20, "agency": -0.15},
        "circuit_mods": {"avoidance": 1.15, "approach": 1.05},
        "insula_mod": +0.15,
        "provenance": "CONSTRAINED: guilt produces avoidance of the guilt state, compliance as escape",
    },
    "fear_mongering": {
        "appraisal_shifts": {"valence": -0.25, "certainty": -0.15},
        "circuit_mods": {"avoidance": 1.40},
        "insula_mod": +0.25,
        "provenance": "CONSTRAINED: amplified threat signal, high amygdala activation",
    },
    "false_urgency": {
        "appraisal_shifts": {"temporal_proximity": +0.30},
        "circuit_mods": {"deliberation": 0.70},
        "insula_mod": +0.20,
        "provenance": "CONSTRAINED: suppresses deliberation but triggers manipulation detection over time",
    },
    "false_scarcity": {
        "appraisal_shifts": {"temporal_proximity": +0.20, "agency": -0.20},
        "circuit_mods": {"avoidance": 1.10},
        "insula_mod": +0.30,
        "provenance": "CONSTRAINED: Booking.com data — disgust after 2-3 exposures, highest insula trigger",
    },
    "ad_hominem": {
        "appraisal_shifts": {"valence": -0.20},
        "circuit_mods": {"avoidance": 1.20},
        "insula_mod": +0.15,
        "provenance": "UNCALIBRATED: attacks person, not argument — triggers disgust in observers",
    },
    "name_calling": {
        "appraisal_shifts": {"valence": -0.25, "agency": -0.10},
        "circuit_mods": {"avoidance": 1.25},
        "insula_mod": +0.20,
        "provenance": "UNCALIBRATED: dehumanizing labels trigger strong avoidance",
    },
    "straw_man": {
        "appraisal_shifts": {"certainty": -0.10},
        "circuit_mods": {"deliberation": 1.15},
        "insula_mod": +0.15,
        "provenance": "UNCALIBRATED: misrepresentation detected by ACC conflict monitoring",
    },
    "whataboutism": {
        "appraisal_shifts": {"goal_relevance": -0.15},
        "circuit_mods": {"deliberation": 1.10},
        "insula_mod": +0.10,
        "provenance": "UNCALIBRATED: deflection reduces perceived relevance of original topic",
    },
    "false_dilemma": {
        "appraisal_shifts": {"agency": -0.20, "certainty": +0.10},
        "circuit_mods": {"deliberation": 0.80},
        "insula_mod": +0.15,
        "provenance": "CONSTRAINED: reduces perceived options, suppresses deliberation",
    },
    "slippery_slope": {
        "appraisal_shifts": {"certainty": -0.15, "valence": -0.10},
        "circuit_mods": {"avoidance": 1.10},
        "insula_mod": +0.10,
        "provenance": "UNCALIBRATED: exaggerated consequences trigger moderate avoidance",
    },
    "red_herring": {
        "appraisal_shifts": {"goal_relevance": -0.20},
        "circuit_mods": {},
        "insula_mod": +0.10,
        "provenance": "UNCALIBRATED: diversion reduces relevance assessment",
    },
    "appeal_to_ignorance": {
        "appraisal_shifts": {"certainty": -0.10},
        "circuit_mods": {"deliberation": 1.10},
        "insula_mod": +0.10,
        "provenance": "UNCALIBRATED: shifts burden of proof, creates false uncertainty",
    },
    "manipulative_flattery": {
        "appraisal_shifts": {"valence": +0.15, "agency": +0.10},
        "circuit_mods": {"deliberation": 0.80},
        "insula_mod": +0.15,
        "provenance": "CONSTRAINED: flattery suppresses critical evaluation but triggers insula when detected",
    },
    "appeal_to_pity": {
        "appraisal_shifts": {"valence": -0.15, "goal_relevance": +0.10},
        "circuit_mods": {"avoidance": 1.05, "approach": 1.05},
        "insula_mod": +0.10,
        "provenance": "CONSTRAINED: sympathy produces compliance as escape from discomfort",
    },
    "obfuscation": {
        "appraisal_shifts": {"certainty": -0.20, "coping_potential": -0.15},
        "circuit_mods": {"deliberation": 1.30},
        "insula_mod": +0.15,
        "provenance": "CONSTRAINED: complex language increases cognitive load and suspicion",
    },
    "bandwagon_pressure": {
        "appraisal_shifts": {"agency": -0.20, "certainty": +0.05},
        "circuit_mods": {"avoidance": 1.10, "deliberation": 0.85},
        "insula_mod": +0.20,
        "provenance": "CONSTRAINED: coercive social pressure — differs from legitimate bandwagon",
    },
}


class TechniqueCircuitMapper:
    """Map detected techniques to appraisal shifts and circuit modifiers."""

    def apply(self, appraisal_dict, technique_result, insula_signal=0.0):
        """Apply technique modifiers to appraisal scores and insula signal.

        Returns modified (appraisal_dict, insula_signal, circuit_multipliers).
        """
        modified = dict(appraisal_dict)
        circuit_mults = {"approach": 1.0, "avoidance": 1.0, "deliberation": 1.0}
        total_insula_mod = insula_signal

        for tech_name in technique_result.detected_names:
            mods = TECHNIQUE_MODIFIERS.get(tech_name)
            if not mods:
                continue

            # Apply appraisal shifts
            for dim, delta in mods.get("appraisal_shifts", {}).items():
                if dim in modified:
                    modified[dim] = round(min(1.0, max(0.0, modified[dim] + delta)), 3)

            # Accumulate circuit multipliers
            for circuit, mult in mods.get("circuit_mods", {}).items():
                circuit_mults[circuit] *= mult

            # Accumulate insula signal
            total_insula_mod += mods.get("insula_mod", 0.0)

        total_insula_mod = round(min(1.0, max(0.0, total_insula_mod)), 3)

        return modified, total_insula_mod, circuit_mults
