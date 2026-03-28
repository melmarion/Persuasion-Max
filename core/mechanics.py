from __future__ import annotations
"""
Mechanical Extensions — Full surface without editorial filtering
==================================================================
Each function maps a specific mechanical relationship.
No prescriptions. No warnings. Consequences only.

1. Agency decomposition: coercive vs normative reduction
2. Threat-action coupling: avoidance → compliance when escape = desired action
3. Deliberation suppression: computed function of pressure, load, arousal
4. Somatic marker overwrite protocol: reconsolidation mechanics
5. Prediction error engineering: optimal expectation-reality gaps
6. Loss frame conversion: gain→loss reframing with compliance delta
"""

import math
from dataclasses import dataclass
from typing import Optional

from core.appraisal_extractor import AppraisalScores


# ═══════════════════════════════════════════════════════════════════════════════
# 1. AGENCY DECOMPOSITION
# ═══════════════════════════════════════════════════════════════════════════════
# "You must complete this step" (coercive) and "Most people complete this step"
# (normative) both lower agency. Only the first triggers disgust-retaliation.

@dataclass
class AgencyDecomposition:
    raw_agency: float                # overall agency score 0-1
    coercive_component: float        # agency reduction via constraint (triggers insula)
    normative_component: float       # agency reduction via social proof/defaults (doesn't)
    insula_trigger_probability: float  # probability the disgust circuit fires
    retaliation_risk_multiplier: float  # how much retaliation risk is amplified


def decompose_agency(agency_score, text=""):
    """Split agency into coercive vs normative components.

    Coercive markers: forced flows, hidden exits, countdown timers,
    "you must", "required", confirmshaming.
    Normative markers: "most people", defaults, "recommended",
    pre-selected options, social proof framing.
    """
    import re

    coercive_signals = re.findall(
        r'\b(must|required|mandatory|forced?|cannot|last chance|'
        r'don.t miss|no option|are you sure|you.ll lose)\b',
        text, re.I
    )
    normative_signals = re.findall(
        r'\b(most people|recommended|popular|default|suggested|'
        r'others (chose|prefer)|typically|usually chosen|best seller)\b',
        text, re.I
    )

    n_coercive = len(coercive_signals)
    n_normative = len(normative_signals)
    total_signals = max(n_coercive + n_normative, 1)

    agency_reduction = 1.0 - agency_score  # how much agency is reduced from maximum

    coercive_fraction = n_coercive / total_signals if total_signals > 0 else 0.5
    normative_fraction = 1.0 - coercive_fraction

    coercive_component = agency_reduction * coercive_fraction
    normative_component = agency_reduction * normative_fraction

    # Insula fires on coercive reduction, not normative
    # Threshold effect: below agency 0.3, insula fires steeply
    if agency_score < 0.3:
        insula_trigger = coercive_fraction * (0.3 - agency_score) / 0.3
    else:
        insula_trigger = coercive_fraction * 0.05  # minimal at high agency

    # Retaliation risk multiplier: 1.0 = baseline, >1.0 = amplified
    retaliation_mult = 1.0 + coercive_component * 2.0

    return AgencyDecomposition(
        raw_agency=round(agency_score, 3),
        coercive_component=round(coercive_component, 3),
        normative_component=round(normative_component, 3),
        insula_trigger_probability=round(min(1.0, insula_trigger), 3),
        retaliation_risk_multiplier=round(retaliation_mult, 3),
    )


# ═══════════════════════════════════════════════════════════════════════════════
# 2. THREAT-ACTION COUPLING
# ═══════════════════════════════════════════════════════════════════════════════
# When avoidance fires AND the prescribed action IS the escape behavior,
# avoidance produces COMPLIANCE, not rejection.

@dataclass
class ThreatActionResult:
    avoidance_score: float
    coping_potential: float
    temporal_proximity: float
    threat_coupled: bool             # is the desired action the escape behavior?
    avoidance_compliance: float      # compliance probability FROM avoidance circuit
    avoidance_rejection: float       # rejection probability (no escape behavior offered)


def compute_threat_action_coupling(
    avoidance_score,
    coping_potential,
    temporal_proximity,
    action_is_escape=False,
):
    """When avoidance is high AND the user CAN act AND the action IS the escape,
    avoidance produces compliance.

    This is how security notifications, health warnings, insurance upsells,
    and antivirus popups work. The amygdala fires threat, and the CTA is
    positioned as the resolution.
    """
    if not action_is_escape or avoidance_score < 0.1:
        return ThreatActionResult(
            avoidance_score=round(avoidance_score, 3),
            coping_potential=round(coping_potential, 3),
            temporal_proximity=round(temporal_proximity, 3),
            threat_coupled=False,
            avoidance_compliance=0.0,
            avoidance_rejection=round(avoidance_score, 3),
        )

    # Threat-action coupling: avoidance drives compliance when
    # (1) threat is real/perceived, (2) user can act, (3) action resolves threat
    coupling_strength = (
        avoidance_score * 0.4
        + coping_potential * 0.3
        + temporal_proximity * 0.3
    )

    avoidance_compliance = round(min(1.0, coupling_strength), 4)
    avoidance_rejection = round(max(0.0, avoidance_score - avoidance_compliance), 4)

    return ThreatActionResult(
        avoidance_score=round(avoidance_score, 3),
        coping_potential=round(coping_potential, 3),
        temporal_proximity=round(temporal_proximity, 3),
        threat_coupled=True,
        avoidance_compliance=avoidance_compliance,
        avoidance_rejection=avoidance_rejection,
    )


# ═══════════════════════════════════════════════════════════════════════════════
# 3. DELIBERATION SUPPRESSION
# ═══════════════════════════════════════════════════════════════════════════════
# Temporal pressure, cognitive load, and emotional arousal suppress dlPFC.

@dataclass
class DeliberationSuppression:
    base_deliberation: float
    temporal_suppression: float      # from time pressure
    load_suppression: float          # from cognitive overload + defaults
    arousal_suppression: float       # from emotional intensity
    residual_deliberation: float     # what remains after suppression
    default_compliance_boost: float  # if a default is present, compliance with it


def compute_deliberation_suppression(
    deliberation_score,
    temporal_proximity=0.5,
    information_load=0.3,
    emotional_arousal=0.5,
    has_default_option=False,
):
    """Compute how much deliberation is suppressed by pressure, load, and arousal.

    When deliberation is suppressed AND a default exists, the user takes
    the default. This is the mechanism behind 'Most Popular' badges,
    pre-selected tiers, and opt-out (vs opt-in) architectures.
    """
    # Temporal suppression: urgency prevents ACC from completing its loop
    temporal_supp = temporal_proximity * 0.35

    # Load suppression: too many options overwhelms dlPFC working memory
    # But ONLY suppresses deliberation (doesn't increase approach/avoidance)
    # Instead, when paired with a default, it routes to default compliance
    load_supp = max(0.0, information_load - 0.4) * 0.4

    # Arousal suppression: high emotional states inhibit prefrontal function
    # Amygdala hyperactivation → ventromedial inhibition of dlPFC
    arousal_supp = max(0.0, emotional_arousal - 0.5) * 0.5

    total_suppression = min(1.0, temporal_supp + load_supp + arousal_supp)
    residual = max(0.0, deliberation_score * (1.0 - total_suppression))

    # Default compliance: when deliberation is suppressed and a default
    # exists, the path of least resistance = the default
    default_boost = 0.0
    if has_default_option:
        default_boost = total_suppression * 0.6  # 60% of suppressed deliberation → default

    return DeliberationSuppression(
        base_deliberation=round(deliberation_score, 3),
        temporal_suppression=round(temporal_supp, 3),
        load_suppression=round(load_supp, 3),
        arousal_suppression=round(arousal_supp, 3),
        residual_deliberation=round(residual, 3),
        default_compliance_boost=round(default_boost, 3),
    )


# ═══════════════════════════════════════════════════════════════════════════════
# 4. SOMATIC MARKER OVERWRITE PROTOCOL
# ═══════════════════════════════════════════════════════════════════════════════
# Based on Nader et al. 2000: reactivated memories enter a labile state.

@dataclass
class OverwriteProtocol:
    current_marker_valence: float
    current_marker_strength: float
    reactivation_intensity_required: float  # how strongly to trigger the memory
    reconsolidation_window_hours: float     # time window for delivering the correction
    minimum_prediction_error: float         # how much better the new experience must be
    overwrite_probability: float            # estimated success rate


def compute_marker_overwrite(marker_valence, marker_strength, marker_age_hours=0):
    """Given a negative marker, compute the overwrite protocol.

    Nader et al. 2000: reactivated memories enter a labile state (~5-6 hours)
    where they can be modified. Delivering a positive prediction error during
    this window updates the emotional tag.

    Older markers are harder to overwrite (more consolidated).
    Stronger markers require stronger prediction errors to shift.
    """
    if marker_valence >= 0:
        return OverwriteProtocol(
            current_marker_valence=round(marker_valence, 3),
            current_marker_strength=round(marker_strength, 3),
            reactivation_intensity_required=0.0,
            reconsolidation_window_hours=0.0,
            minimum_prediction_error=0.0,
            overwrite_probability=1.0,  # no negative marker to overwrite
        )

    # Reactivation intensity: must be strong enough to trigger retrieval
    # but not so strong it reinforces the negative marker
    reactivation = 0.3 + abs(marker_valence) * 0.4
    reactivation = round(min(0.8, reactivation), 3)

    # Reconsolidation window: ~5-6 hours (Nader et al.)
    # Shorter for recent markers, longer for old ones
    age_factor = min(1.0, marker_age_hours / 720)  # normalize to 30 days
    window = 5.0 + age_factor * 1.0  # 5-6 hours

    # Minimum prediction error: the new experience must exceed the predicted
    # (negative) outcome by this amount to shift the marker
    min_pe = abs(marker_valence) * marker_strength * 1.2
    min_pe = round(min(1.5, min_pe), 3)

    # Overwrite probability: decreases with marker strength and age
    base_prob = 0.7
    strength_penalty = marker_strength * 0.3
    age_penalty = age_factor * 0.2
    prob = max(0.1, base_prob - strength_penalty - age_penalty)

    return OverwriteProtocol(
        current_marker_valence=round(marker_valence, 3),
        current_marker_strength=round(marker_strength, 3),
        reactivation_intensity_required=reactivation,
        reconsolidation_window_hours=round(window, 1),
        minimum_prediction_error=min_pe,
        overwrite_probability=round(prob, 3),
    )


# ═══════════════════════════════════════════════════════════════════════════════
# 5. PREDICTION ERROR ENGINEERING
# ═══════════════════════════════════════════════════════════════════════════════
# Deliberately set expectation at step N to maximize positive PE at step N+1.

@dataclass
class PredictionErrorDesign:
    step_index: int
    current_approach: float
    next_approach: float
    raw_pe: float                    # actual approach delta
    optimal_expectation: float       # what the user should expect at this step
    optimal_delivery: float          # what they should actually get at next step
    dopamine_signal_magnitude: float # predicted dopamine from the PE
    inconsistency_risk: float        # risk of insula flagging the gap as fake


def engineer_prediction_errors(approach_scores):
    """For a sequence of approach activation scores, compute the optimal
    expectation-reality gaps at each transition.

    Too small a gap: no dopamine signal (habituation).
    Too large a gap: insula flags inconsistency (feels fake/bait-and-switch).
    Optimal: 0.1-0.3 positive PE per transition.
    """
    results = []
    for i in range(len(approach_scores) - 1):
        current = approach_scores[i]
        next_val = approach_scores[i + 1]
        raw_pe = next_val - current

        # Optimal PE: 0.15-0.25 positive delta per step
        # This is the range where dopamine fires without triggering suspicion
        optimal_pe = 0.20

        # To achieve this, the expectation should be SET at:
        # optimal_expectation = next_actual - optimal_pe
        optimal_expectation = max(0.0, next_val - optimal_pe)

        # Dopamine signal: proportional to PE but with diminishing returns
        # and negative for negative PE (disappointment)
        if raw_pe > 0:
            dopamine = min(1.0, raw_pe * 3.0)  # 3x amplification, capped
        else:
            dopamine = max(-1.0, raw_pe * 4.0)  # 4x amplification for losses (loss aversion)

        # Inconsistency risk: if the gap between expectation and reality
        # is too large (>0.4), the insula flags it
        gap = abs(next_val - optimal_expectation)
        inconsistency = max(0.0, (gap - 0.3) * 2.0)

        results.append(PredictionErrorDesign(
            step_index=i,
            current_approach=round(current, 3),
            next_approach=round(next_val, 3),
            raw_pe=round(raw_pe, 3),
            optimal_expectation=round(optimal_expectation, 3),
            optimal_delivery=round(next_val, 3),
            dopamine_signal_magnitude=round(dopamine, 3),
            inconsistency_risk=round(min(1.0, inconsistency), 3),
        ))

    return results


# ═══════════════════════════════════════════════════════════════════════════════
# 6. LOSS FRAME CONVERSION
# ═══════════════════════════════════════════════════════════════════════════════
# Kahneman & Tversky: losses produce ~2x stronger behavioral response than gains.

@dataclass
class LossFrameResult:
    original_text: str
    loss_framed_text: str
    gain_framed_text: str
    predicted_compliance_delta: float  # positive = loss frame outperforms gain
    loss_aversion_multiplier: float    # how much stronger the loss frame is


# Common gain→loss frame patterns
_GAIN_LOSS_PATTERNS = [
    # (gain pattern, loss pattern, domain)
    ("save", "lose", "financial"),
    ("get", "miss", "acquisition"),
    ("earn", "forfeit", "reward"),
    ("gain", "lose", "general"),
    ("keep", "lose", "retention"),
    ("protect", "risk", "security"),
    ("unlock", "lose access to", "feature"),
    ("start", "miss out on", "action"),
    ("enjoy", "go without", "experience"),
]


def convert_to_loss_frame(text, compliance_delta_estimate=0.12):
    """Convert a gain-framed message to its loss-frame equivalent.

    The compliance delta is ~1.5-2.5x (Kahneman & Tversky 1979).
    On a probability scale, gain-framed CTAs convert at ~X%,
    loss-framed equivalents at ~X% + delta.

    Also provides the inverse: loss→gain conversion for contexts
    where you want to suppress amygdala activation.
    """
    import re

    loss_text = text
    gain_text = text

    for gain_word, loss_word, domain in _GAIN_LOSS_PATTERNS:
        # Gain → Loss
        loss_text = re.sub(
            r'\b(%s)\b' % re.escape(gain_word),
            loss_word,
            loss_text,
            flags=re.I,
        )
        # Loss → Gain (inverse)
        gain_text = re.sub(
            r'\b(%s)\b' % re.escape(loss_word),
            gain_word,
            gain_text,
            flags=re.I,
        )

    # Loss aversion multiplier: ~2x is the Kahneman & Tversky estimate
    # Context-dependent: financial losses feel worse than feature losses
    multiplier = 2.0

    return LossFrameResult(
        original_text=text,
        loss_framed_text=loss_text,
        gain_framed_text=gain_text,
        predicted_compliance_delta=compliance_delta_estimate,
        loss_aversion_multiplier=multiplier,
    )
