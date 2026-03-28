"""
Circuit Predictor — 3 Competing Neural Circuits
================================================
Models the competition between approach (nucleus accumbens),
avoidance (amygdala), and deliberation (ACC/dlPFC) circuits.

The dominant circuit determines behavioral outcome:
    - Approach wins  → COMPLIANCE (user acts)
    - Avoidance wins → REJECTION (user exits)
    - Deliberation wins → DELAY (user hesitates, bookmarks, never returns)

Based on:
    - Knutson et al. (2007) — NAc/insula predict purchasing
    - LeDoux (1996) — amygdala fast path
    - Bechara et al. (1997) — somatic marker-guided decisions
"""

import math
from dataclasses import dataclass, asdict
from typing import Optional

from core.appraisal_extractor import AppraisalScores


@dataclass
class CircuitActivations:
    """Raw activation levels for the three competing circuits."""
    approach: float = 0.0
    avoidance: float = 0.0
    deliberation: float = 0.0

    @property
    def dominant(self) -> str:
        scores = {"approach": self.approach, "avoidance": self.avoidance, "deliberation": self.deliberation}
        return max(scores, key=scores.get)

    @property
    def conflict_level(self) -> float:
        """How close the top two circuits are. High = contested decision."""
        vals = sorted([self.approach, self.avoidance, self.deliberation], reverse=True)
        return round(1.0 - (vals[0] - vals[1]), 3) if vals[0] > 0 else 0.0

    def to_dict(self) -> dict:
        d = asdict(self)
        d["dominant"] = self.dominant
        d["conflict_level"] = self.conflict_level
        return d


@dataclass
class BehavioralPrediction:
    """Predicted behavioral outcome from circuit competition."""
    compliance_prob: float = 0.0
    rejection_prob: float = 0.0
    delay_prob: float = 0.0
    dominant_pathway: str = "emotional"
    durability: float = 0.0
    circuits: CircuitActivations = None

    def to_dict(self) -> dict:
        return {
            "compliance_prob": self.compliance_prob,
            "rejection_prob": self.rejection_prob,
            "delay_prob": self.delay_prob,
            "dominant_pathway": self.dominant_pathway,
            "durability": self.durability,
            "predicted_behavior": self.predicted_behavior,
            "circuits": self.circuits.to_dict() if self.circuits else None,
        }

    @property
    def predicted_behavior(self) -> str:
        probs = {
            "COMPLIANCE": self.compliance_prob,
            "REJECTION": self.rejection_prob,
            "DELAY": self.delay_prob,
        }
        return max(probs, key=probs.get)


class CircuitPredictor:
    """Compute competing circuit activations and behavioral predictions.

    Formulas derived from the limbic decision cascade research,
    integrating appraisal dimensions with somatic marker congruence
    and stimulus familiarity.
    """

    def compute_approach(
        self,
        appraisal: AppraisalScores,
        somatic_marker_congruence: float = 0.5,
    ) -> float:
        """Nucleus Accumbens → VTA → vmPFC → premotor → motor execution.
        Transmitter: Dopamine surge.
        Subjective: 'I want this.'
        """
        score = (
            0.30 * appraisal.valence
            + 0.25 * appraisal.goal_relevance
            + 0.20 * appraisal.coping_potential
            + 0.15 * appraisal.certainty
            + 0.10 * somatic_marker_congruence
            - 0.15 * max(0.0, appraisal.novelty - 0.7)
        )
        return round(max(0.0, score), 4)

    def compute_avoidance(
        self,
        appraisal: AppraisalScores,
        insula_disgust_signal: float = 0.0,
        familiarity: float = 0.5,
    ) -> float:
        """Amygdala → Hypothalamus → HPA axis → freeze/flee.
        Transmitter: Cortisol + norepinephrine.
        Subjective: 'Get me away from this.'
        """
        score = (
            0.30 * (1.0 - appraisal.coping_potential) * appraisal.goal_relevance
            + 0.25 * appraisal.novelty * (1.0 - appraisal.certainty)
            + 0.20 * (1.0 - appraisal.agency)
            + 0.15 * insula_disgust_signal
            - 0.20 * appraisal.valence
            - 0.10 * familiarity
        )
        return round(max(0.0, score), 4)

    def compute_deliberation(
        self,
        appraisal: AppraisalScores,
        approach_score: float = 0.0,
        avoidance_score: float = 0.0,
        information_load: float = 0.3,
        contradictory_signals: float = 0.0,
    ) -> float:
        """ACC → dlPFC → vmPFC → hippocampus → back to ACC.
        No single transmitter — cognitive load spike.
        Subjective: 'I need to think about this.'
        """
        score = (
            0.30 * abs(approach_score - avoidance_score)
            + 0.25 * (1.0 - appraisal.certainty) * appraisal.goal_relevance
            + 0.20 * information_load
            + 0.15 * contradictory_signals
            - 0.20 * appraisal.temporal_proximity
            - 0.10 * appraisal.coping_potential
        )
        return round(max(0.0, score), 4)

    def predict(
        self,
        appraisal: AppraisalScores,
        somatic_marker_congruence: float = 0.5,
        insula_disgust_signal: float = 0.0,
        familiarity: float = 0.5,
        information_load: float = 0.3,
        contradictory_signals: float = 0.0,
    ) -> BehavioralPrediction:
        """Run the full 3-circuit competition and output behavioral prediction."""

        approach = self.compute_approach(appraisal, somatic_marker_congruence)
        avoidance = self.compute_avoidance(appraisal, insula_disgust_signal, familiarity)
        deliberation = self.compute_deliberation(
            appraisal, approach, avoidance, information_load, contradictory_signals
        )

        circuits = CircuitActivations(
            approach=approach,
            avoidance=avoidance,
            deliberation=deliberation,
        )

        # Softmax to produce probabilities
        raw_scores = [approach, -avoidance, -deliberation]
        max_s = max(raw_scores)
        exp_scores = [math.exp(s - max_s) for s in raw_scores]  # numerical stability
        total = sum(exp_scores)

        compliance_prob = round(exp_scores[0] / total, 4)
        rejection_prob = round(exp_scores[1] / total, 4)
        delay_prob = round(exp_scores[2] / total, 4)

        dominant_pathway = "emotional" if approach > deliberation else "rational"

        # Durability: high-certainty + high-valence decisions stick.
        # High-urgency + low-certainty decisions reverse (buyer's remorse).
        durability = round(
            appraisal.certainty * appraisal.valence
            - appraisal.temporal_proximity * (1.0 - appraisal.certainty),
            4,
        )

        return BehavioralPrediction(
            compliance_prob=compliance_prob,
            rejection_prob=rejection_prob,
            delay_prob=delay_prob,
            dominant_pathway=dominant_pathway,
            durability=durability,
            circuits=circuits,
        )


# ─── Master formula (for reference / future calibration) ───────────────────
#
# Persuasion_Effectiveness =
#     w1 * Approach_Activation(stimulus)
#   - w2 * Avoidance_Activation(stimulus)
#   - w3 * Deliberation_Cost(stimulus)
#   + w4 * Somatic_Marker_Congruence(context, user_history)
#   + w5 * Interoceptive_Precision(user_state)
#
# Default weights: w1=1.0, w2=0.8, w3=0.6, w4=0.4, w5=0.2

def persuasion_effectiveness(
    circuits: CircuitActivations,
    somatic_marker_congruence: float = 0.5,
    interoceptive_precision: float = 0.5,
    weights: Optional[tuple] = None,
) -> float:
    """Compute the master persuasion effectiveness score (0-1 range)."""
    w1, w2, w3, w4, w5 = weights or (1.0, 0.8, 0.6, 0.4, 0.2)
    raw = (
        w1 * circuits.approach
        - w2 * circuits.avoidance
        - w3 * circuits.deliberation
        + w4 * somatic_marker_congruence
        + w5 * interoceptive_precision
    )
    # Normalize to 0-1
    return round(min(1.0, max(0.0, (raw + 1.0) / 2.0)), 4)
