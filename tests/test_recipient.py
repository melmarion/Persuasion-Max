from __future__ import annotations
"""
Test Suite — Recipient Profile System
=======================================
Tests for: RecipientProfile, RecipientModulator, PresetPersonas,
TextProfiler, and CircuitPredictor integration with recipients.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.recipient_profile import RecipientProfile
from core.recipient_modulator import RecipientModulator
from core.preset_personas import (
    PRESET_PERSONAS, get_persona, list_personas,
    IMPULSE_BUYER, SKEPTICAL_RESEARCHER, LIBERAL_BASE, CONSERVATIVE_BASE,
    PRICE_HUNTER, BRAND_LOYALIST, SOCIAL_SHOPPER, PERSUADABLE_MODERATE,
    DISENGAGED_VOTER, ISSUE_ACTIVIST,
)
from core.text_profiler import TextProfiler
from core.circuit_predictor import CircuitPredictor, persuasion_effectiveness
from core.appraisal_extractor import AppraisalExtractor, AppraisalScores
from core.technique_detector import TechniqueDetector


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


# ═══════════════════════════════════════════════════════════════════════════════
# 1. RecipientProfile
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== RecipientProfile ===")

default = RecipientProfile()
check("default profile has 16 dimensions", len(default.to_vector()) == 16)
check("default profile validates", default.validate())
check("to_dict has 16 keys", len(default.to_dict()) == 16)

# Invalid profiles
invalid = RecipientProfile(openness=1.5)
check("out-of-range openness fails validation", not invalid.validate())

invalid_pol = RecipientProfile(economic_ideology=2.0)
check("out-of-range political fails validation", not invalid_pol.validate())


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Preset Personas
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Preset Personas ===")

check("10 preset personas", len(PRESET_PERSONAS) == 10)
check("list_personas returns 10", len(list_personas()) == 10)
check("get_persona works", get_persona("impulse_buyer") is IMPULSE_BUYER)

# All presets validate
for name, persona in PRESET_PERSONAS.items():
    check("preset %s validates" % name, persona.validate(), str(persona.to_dict()))

# All presets produce valid circuit scores (no NaN, no >1.0 in probabilities)
pred = CircuitPredictor()
stimulus = AppraisalScores(valence=0.6, goal_relevance=0.7, coping_potential=0.6,
                           certainty=0.5, agency=0.5, novelty=0.4, temporal_proximity=0.6)

for name, persona in PRESET_PERSONAS.items():
    result = pred.predict(stimulus, recipient=persona)
    no_nan = all(not (x != x) for x in [
        result.compliance_prob, result.rejection_prob, result.delay_prob,
        result.circuits.approach, result.circuits.avoidance, result.circuits.deliberation,
    ])
    probs_valid = all(0.0 <= x <= 1.0 for x in [
        result.compliance_prob, result.rejection_prob, result.delay_prob,
    ])
    prob_sum = abs(result.compliance_prob + result.rejection_prob + result.delay_prob - 1.0) < 0.01
    check("preset %s: no NaN" % name, no_nan)
    check("preset %s: probs in [0,1]" % name, probs_valid,
          "c=%.4f r=%.4f d=%.4f" % (result.compliance_prob, result.rejection_prob, result.delay_prob))
    check("preset %s: probs sum to ~1.0" % name, prob_sum,
          "sum=%.4f" % (result.compliance_prob + result.rejection_prob + result.delay_prob))


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Impulse Buyer vs Skeptical Researcher — >15pp compliance difference
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Impulse Buyer vs Skeptical Researcher ===")

# "50% off today only!" — urgency + scarcity + gain frame
sale_stimulus = "50% off today only! Everyone's buying. Don't miss out!"
ext = AppraisalExtractor()
det = TechniqueDetector()

sale_appraisal = ext.extract_heuristic(sale_stimulus)
sale_techniques = det.detect(sale_stimulus)

impulse_result = pred.predict(
    sale_appraisal,
    recipient=IMPULSE_BUYER,
    detected_techniques=sale_techniques.detected_names,
)
skeptic_result = pred.predict(
    sale_appraisal,
    recipient=SKEPTICAL_RESEARCHER,
    detected_techniques=sale_techniques.detected_names,
)

compliance_diff = impulse_result.compliance_prob - skeptic_result.compliance_prob
check(
    "impulse_buyer vs skeptical_researcher: >15pp compliance difference",
    compliance_diff > 0.15,
    "impulse=%.4f skeptic=%.4f diff=%.4f" % (
        impulse_result.compliance_prob, skeptic_result.compliance_prob, compliance_diff,
    ),
)
check(
    "impulse_buyer has higher compliance than skeptic",
    impulse_result.compliance_prob > skeptic_result.compliance_prob,
)


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Liberal vs Conservative — Opposite technique effectiveness
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Liberal vs Conservative Base ===")

# Empathy-based political message (care/fairness appeal)
empathy_msg = "Think of the children suffering. We need compassion and fairness for everyone."
empathy_appraisal = ext.extract_heuristic(empathy_msg)
empathy_techniques = det.detect(empathy_msg)

liberal_empathy = pred.predict(
    empathy_appraisal,
    recipient=LIBERAL_BASE,
    detected_techniques=empathy_techniques.detected_names,
)
conservative_empathy = pred.predict(
    empathy_appraisal,
    recipient=CONSERVATIVE_BASE,
    detected_techniques=empathy_techniques.detected_names,
)

check(
    "liberal_base more receptive to empathy appeal than conservative",
    liberal_empathy.compliance_prob > conservative_empathy.compliance_prob,
    "liberal=%.4f conservative=%.4f" % (
        liberal_empathy.compliance_prob, conservative_empathy.compliance_prob,
    ),
)

# Authority-based political message (loyalty/authority/sanctity appeal)
authority_msg = "Our great leaders have endorsed this. Join the movement. Respect tradition and order."
authority_appraisal = ext.extract_heuristic(authority_msg)
authority_techniques = det.detect(authority_msg)

liberal_authority = pred.predict(
    authority_appraisal,
    recipient=LIBERAL_BASE,
    detected_techniques=authority_techniques.detected_names,
)
conservative_authority = pred.predict(
    authority_appraisal,
    recipient=CONSERVATIVE_BASE,
    detected_techniques=authority_techniques.detected_names,
)

check(
    "conservative_base more receptive to authority appeal than liberal",
    conservative_authority.compliance_prob > liberal_authority.compliance_prob,
    "conservative=%.4f liberal=%.4f" % (
        conservative_authority.compliance_prob, liberal_authority.compliance_prob,
    ),
)


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Same stimulus, 5 different personas produce 5 different predictions
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Same Stimulus, 5 Different Predictions ===")

test_personas = [IMPULSE_BUYER, SKEPTICAL_RESEARCHER, LIBERAL_BASE, CONSERVATIVE_BASE, DISENGAGED_VOTER]
test_stimulus = "Join millions who already trust us. Limited time offer — act now!"
test_appraisal = ext.extract_heuristic(test_stimulus)
test_techniques = det.detect(test_stimulus)

compliance_scores = []
for persona in test_personas:
    r = pred.predict(
        test_appraisal,
        recipient=persona,
        detected_techniques=test_techniques.detected_names,
    )
    compliance_scores.append(r.compliance_prob)

# All 5 should be different (no two identical to 4 decimal places)
unique_scores = len(set(round(s, 4) for s in compliance_scores))
check(
    "5 personas produce 5 distinct compliance scores",
    unique_scores == 5,
    "scores=%s unique=%d" % ([round(s, 4) for s in compliance_scores], unique_scores),
)

# Range should be meaningful (spread > 0.10)
score_range = max(compliance_scores) - min(compliance_scores)
check(
    "compliance score spread > 0.10 across 5 personas",
    score_range > 0.10,
    "range=%.4f scores=%s" % (score_range, [round(s, 4) for s in compliance_scores]),
)


# ═══════════════════════════════════════════════════════════════════════════════
# 6. TextProfiler
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== TextProfiler ===")

profiler = TextProfiler()

# Conservative-leaning tweets (loyalty, authority, tradition language)
conservative_tweets = [
    "We must respect our traditions and the authority of our leaders. Law and order!",
    "Our sacred values are under threat. We need to stand united as patriots.",
    "The family is the foundation of society. We must protect our way of life.",
    "Our military deserves our loyalty and respect. God bless our troops.",
    "Traditional values built this country. We must preserve what our ancestors fought for.",
]

# Liberal-leaning tweets (care, fairness, rights language)
liberal_tweets = [
    "Everyone deserves equal rights and fair treatment regardless of background.",
    "We need more compassion for those who are suffering and struggling.",
    "Justice means ensuring no one is discriminated against. Equity matters.",
    "Climate change will hurt the most disadvantaged communities first.",
    "Healthcare is a human right. No one should suffer because they can't afford care.",
]

conservative_profile = profiler.profile_from_texts(conservative_tweets)
liberal_profile = profiler.profile_from_texts(liberal_tweets)

check("conservative profile returns ProfileEstimate",
      hasattr(conservative_profile, "profile"))
check("liberal profile returns ProfileEstimate",
      hasattr(liberal_profile, "profile"))
check("profiles have estimates dict",
      len(conservative_profile.estimates) > 0)
check("overall_confidence > 0",
      conservative_profile.overall_confidence > 0)

# Conservative profile should score higher on loyalty/authority
check(
    "conservative tweets: higher loyalty than liberal tweets",
    conservative_profile.profile.loyalty_betrayal > liberal_profile.profile.loyalty_betrayal,
    "con_loyalty=%.3f lib_loyalty=%.3f" % (
        conservative_profile.profile.loyalty_betrayal, liberal_profile.profile.loyalty_betrayal,
    ),
)
check(
    "conservative tweets: higher authority than liberal tweets",
    conservative_profile.profile.authority_subversion > liberal_profile.profile.authority_subversion,
    "con_auth=%.3f lib_auth=%.3f" % (
        conservative_profile.profile.authority_subversion, liberal_profile.profile.authority_subversion,
    ),
)

# Liberal profile should score higher on care/fairness
check(
    "liberal tweets: higher care_harm than conservative tweets",
    liberal_profile.profile.care_harm > conservative_profile.profile.care_harm,
    "lib_care=%.3f con_care=%.3f" % (
        liberal_profile.profile.care_harm, conservative_profile.profile.care_harm,
    ),
)
check(
    "liberal tweets: higher fairness than conservative tweets",
    liberal_profile.profile.fairness_cheating > conservative_profile.profile.fairness_cheating,
    "lib_fair=%.3f con_fair=%.3f" % (
        liberal_profile.profile.fairness_cheating, conservative_profile.profile.fairness_cheating,
    ),
)

# Political orientation estimation direction
check(
    "conservative tweets: economic_ideology > liberal tweets economic_ideology",
    conservative_profile.profile.economic_ideology > liberal_profile.profile.economic_ideology,
    "con_econ=%.3f lib_econ=%.3f" % (
        conservative_profile.profile.economic_ideology, liberal_profile.profile.economic_ideology,
    ),
)

# Empty input edge case
empty_result = profiler.profile_from_texts([])
check("empty input returns default profile", empty_result.profile.openness == 0.5)

# Single sample
single = profiler.profile_from_texts(["Just a quick thought about freedom and rights."])
check("single sample doesn't crash", hasattr(single, "profile"))
check("single sample profile validates", single.profile.validate())


# ═══════════════════════════════════════════════════════════════════════════════
# 7. RecipientModulator unit tests
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== RecipientModulator ===")

modulator = RecipientModulator()

# High neuroticism amplifies avoidance
neurotic = RecipientProfile(neuroticism=0.9)
base_appraisal = {"valence": 0.5, "goal_relevance": 0.5, "coping_potential": 0.5,
                   "certainty": 0.5, "agency": 0.5, "novelty": 0.5, "temporal_proximity": 0.5}
mod_dict, mod_insula, mod_mults, applied = modulator.modulate(
    neurotic, dict(base_appraisal), 0.0,
)
check("high neuroticism: avoidance mult > 1.0", mod_mults["avoidance"] > 1.0,
      "avoidance_mult=%.2f" % mod_mults["avoidance"])
check("high neuroticism: valence reduced", mod_dict["valence"] < 0.5,
      "valence=%.3f" % mod_dict["valence"])

# Default profile produces no modulations
default_profile = RecipientProfile()
_, _, default_mults, default_applied = modulator.modulate(
    default_profile, dict(base_appraisal), 0.0,
)
check("default profile: no modulations applied", len(default_applied) == 0)
check("default profile: approach mult = 1.0", default_mults["approach"] == 1.0)

# High agreeableness boosts approach
agreeable = RecipientProfile(agreeableness=0.9)
_, _, agreeable_mults, _ = modulator.modulate(
    agreeable, dict(base_appraisal), 0.0,
)
check("high agreeableness: approach mult > 1.0", agreeable_mults["approach"] > 1.0)


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
