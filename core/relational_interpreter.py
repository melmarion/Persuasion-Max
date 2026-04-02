from __future__ import annotations
"""
Relational Interpreter — User-Only Behavioral Translation Layer
===============================================================
Converts mechanical persuasion outputs into private, plain-English
interpretations for the user. This module does NOT generate outbound
messages to send. It only explains the pattern being observed.
"""

from dataclasses import dataclass, asdict
from typing import Optional

from core.appraisal_extractor import AppraisalScores
from core.circuit_predictor import BehavioralPrediction, CircuitActivations


@dataclass
class RelationalInterpretation:
    """Private explanation surface for the user."""

    pattern_label: str
    confidence: str
    plain_english_inference: str
    clean_internal_translation: str
    what_this_does_not_prove: str
    response_style: str
    user_only: bool = True
    suggested_outbound_text: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


class RelationalInterpreter:
    """Translate behavioral mechanics into concise user-only explanations."""

    def interpret(
        self,
        stimulus: str,
        appraisal: AppraisalScores,
        circuits: CircuitActivations,
        prediction: BehavioralPrediction,
    ) -> RelationalInterpretation:
        pattern_label = self._pattern_label(appraisal, circuits, prediction)
        confidence = self._confidence(circuits)
        plain = self._plain_english(pattern_label, appraisal, prediction)
        translation = self._clean_translation(pattern_label, prediction)
        not_prove = self._what_this_does_not_prove(pattern_label)
        response_style = self._response_style(pattern_label, prediction)

        return RelationalInterpretation(
            pattern_label=pattern_label,
            confidence=confidence,
            plain_english_inference=plain,
            clean_internal_translation=translation,
            what_this_does_not_prove=not_prove,
            response_style=response_style,
        )

    def _pattern_label(
        self,
        appraisal: AppraisalScores,
        circuits: CircuitActivations,
        prediction: BehavioralPrediction,
    ) -> str:
        if prediction.retaliation_probability >= 0.18 and appraisal.agency < 0.3:
            return "hostile_or_trapped_dynamic"
        if prediction.predicted_behavior == "DELAY" or circuits.dominant == "deliberation":
            return "ambiguity_or_non-commitment"
        if prediction.predicted_behavior == "REJECTION" or circuits.dominant == "avoidance":
            return "soft_rejection_or_distancing"
        if prediction.immediate_compliance > prediction.repeat_compliance + 0.12:
            return "short_term_pull_low_durability"
        if prediction.compliance_prob >= 0.55 and prediction.repeat_compliance >= 0.45:
            return "clear_alignment"
        return "mixed_signal_pattern"

    def _confidence(self, circuits: CircuitActivations) -> str:
        if circuits.conflict_level < 0.35:
            return "high"
        if circuits.conflict_level < 0.6:
            return "medium"
        return "low"

    def _plain_english(
        self,
        pattern_label: str,
        appraisal: AppraisalScores,
        prediction: BehavioralPrediction,
    ) -> str:
        if pattern_label == "ambiguity_or_non-commitment":
            return (
                "The pattern points to hesitation, vagueness, or insufficient willingness "
                "to make a concrete move. The issue looks more logistical and motivational "
                "than emotional."
            )
        if pattern_label == "soft_rejection_or_distancing":
            return (
                "The pattern points to withdrawal or distancing. The person may be trying "
                "to keep things pleasant while still reducing closeness or commitment."
            )
        if pattern_label == "short_term_pull_low_durability":
            return (
                "There is enough positive pull for momentary engagement, but the structure "
                "does not look durable. This often shows up as chemistry without reliable follow-through."
            )
        if pattern_label == "hostile_or_trapped_dynamic":
            return (
                "The pattern points to pressure, low agency, and backlash risk. Even if the "
                "surface remains polite, the underlying dynamic is unstable."
            )
        if pattern_label == "clear_alignment":
            return (
                "The pattern points to genuine fit and relatively stable willingness. "
                "What is being signaled looks clearer than performative."
            )
        return (
            "The pattern is mixed. There are signs of interest or relevance, but not enough "
            "clarity to treat the situation as settled."
        )

    def _clean_translation(self, pattern_label: str, prediction: BehavioralPrediction) -> str:
        if pattern_label == "ambiguity_or_non-commitment":
            return "This is not a clarity-rich yes. Unless the behavior sharpens, treat it as non-commitment."
        if pattern_label == "soft_rejection_or_distancing":
            return "This may not be about my worth. It does look like they are creating distance."
        if pattern_label == "short_term_pull_low_durability":
            return "They may like the connection, but not enough to carry it in a reliable way."
        if pattern_label == "hostile_or_trapped_dynamic":
            return "Even if this gets a short-term result, it is likely to leave a bruise."
        if pattern_label == "clear_alignment":
            return "The behavior and the signal match. I do not need to over-interpret scraps."
        return "There is not enough consistency here to build certainty on top of it."

    def _what_this_does_not_prove(self, pattern_label: str) -> str:
        if pattern_label == "clear_alignment":
            return "It does not prove permanence, exclusivity, or deep emotional maturity."
        return "It does not prove what the other person feels deep down, and it does not measure my value."

    def _response_style(self, pattern_label: str, prediction: BehavioralPrediction) -> str:
        if pattern_label in {"ambiguity_or_non-commitment", "soft_rejection_or_distancing"}:
            return "brief_warm_boundaried"
        if pattern_label == "hostile_or_trapped_dynamic":
            return "calm_firm_exit"
        if pattern_label == "clear_alignment":
            return "open_specific_grounded"
        if pattern_label == "short_term_pull_low_durability":
            return "slow_down_and_require_consistency"
        return "measured_non-pursuing"
