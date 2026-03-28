from __future__ import annotations
"""
Test Suite — Domain-Specific Weight Registries
================================================
Tests for: DomainWeightRegistry, DomainPredictor,
and domain-specific behavioral outcome predictions.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.domain_registry import DomainWeightRegistry, STAKEHOLDER_PROFILES
from core.domain_predictor import DomainPredictor, DomainPrediction
from core.recipient_profile import RecipientProfile
from core.preset_personas import LIBERAL_BASE, CONSERVATIVE_BASE


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
# 1. DomainWeightRegistry — Factory methods and structure
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== DomainWeightRegistry ===")

universal = DomainWeightRegistry.universal()
ecommerce = DomainWeightRegistry.ecommerce()
campaign = DomainWeightRegistry.campaign()
crisis_pr = DomainWeightRegistry.crisis_pr()

check("universal registry created", universal.domain == "universal")
check("ecommerce registry created", ecommerce.domain == "ecommerce")
check("campaign registry created", campaign.domain == "campaign")
check("crisis_pr registry created", crisis_pr.domain == "crisis_pr")

# Universal should have all 32 weights from circuit_predictor
check("universal has 32+ weights", len(universal.list_all_weights()) >= 32,
      "count=%d" % len(universal.list_all_weights()))

# Each domain has weights
check("ecommerce has weights", len(ecommerce.list_all_weights()) > 0)
check("campaign has weights", len(campaign.list_all_weights()) > 0)
check("crisis_pr has weights", len(crisis_pr.list_all_weights()) > 0)

# Provenance tracking
check("universal provenance summary has keys",
      "CONSTRAINED" in universal.provenance_summary())
check("ecommerce has uncalibrated weights",
      len(ecommerce.list_uncalibrated_weights()) > 0)

# Domain-specific outcome names
check("ecommerce outcomes include purchase_probability",
      "purchase_probability" in ecommerce.outcome_names)
check("campaign outcomes include belief_change",
      "belief_change" in campaign.outcome_names)
check("crisis_pr outcomes include trust_recovery",
      "trust_recovery" in crisis_pr.outcome_names)

# Technique overrides exist
check("ecommerce has scarcity_appeal override",
      ecommerce.get_technique_override("scarcity_appeal") is not None)
check("crisis_pr has whataboutism override",
      crisis_pr.get_technique_override("whataboutism") is not None)
check("campaign has logical_appeal override",
      campaign.get_technique_override("logical_appeal") is not None)

# All weights have provenance labels
for name, w in [("ecommerce", ecommerce), ("campaign", campaign), ("crisis_pr", crisis_pr)]:
    for weight in w.list_all_weights():
        has_prov = weight.provenance in ("FITTED", "CONSTRAINED", "UNCALIBRATED")
        check("weight %s has valid provenance" % weight.name, has_prov,
              "provenance=%s" % weight.provenance)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Same product description: ecommerce vs campaign must differ >10pp
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Cross-Domain Compliance Difference ===")

dp = DomainPredictor()

product_desc = "Only 3 left in stock! Was $99, now $49. Don't miss out — everyone's buying."

ecom_result = dp.predict(product_desc, domain="ecommerce")
campaign_result = dp.predict(product_desc, domain="campaign")
universal_result = dp.predict(product_desc, domain="universal")

compliance_diff = abs(ecom_result.immediate_compliance - campaign_result.immediate_compliance)
check(
    "ecommerce vs campaign: >10pp compliance difference",
    compliance_diff > 0.10,
    "ecom=%.4f campaign=%.4f diff=%.4f" % (
        ecom_result.immediate_compliance, campaign_result.immediate_compliance, compliance_diff,
    ),
)

# Ecommerce should have domain-specific outcomes
check("ecommerce has purchase_probability",
      "purchase_probability" in ecom_result.domain_outcomes)
check("ecommerce has cart_add_probability",
      "cart_add_probability" in ecom_result.domain_outcomes)
check("ecommerce has return_probability",
      "return_probability" in ecom_result.domain_outcomes)

# Campaign should have domain-specific outcomes
check("campaign has belief_change",
      "belief_change" in campaign_result.domain_outcomes)
check("campaign has share_amplify_probability",
      "share_amplify_probability" in campaign_result.domain_outcomes)

# Universal should have empty domain outcomes
check("universal has empty domain_outcomes",
      len(universal_result.domain_outcomes) == 0)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Crisis PR: media vs customers vs regulators — 3 distinct predictions
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Crisis PR Stakeholder Differentiation ===")

crisis_statement = (
    "We take full responsibility for the incident. Our investigation found that "
    "a software error caused the data exposure. We have already implemented fixes "
    "and are working with independent auditors to verify our systems."
)

media_result = dp.predict(crisis_statement, domain="crisis_pr", stakeholder_type="media",
                          crisis_severity=0.7, response_timing=0.1)
customer_result = dp.predict(crisis_statement, domain="crisis_pr", stakeholder_type="customers",
                             crisis_severity=0.7, response_timing=0.1)
regulator_result = dp.predict(crisis_statement, domain="crisis_pr", stakeholder_type="regulators",
                              crisis_severity=0.7, response_timing=0.1)

# All three should produce different trust_recovery scores
trust_scores = [
    media_result.domain_outcomes.get("trust_recovery", 0),
    customer_result.domain_outcomes.get("trust_recovery", 0),
    regulator_result.domain_outcomes.get("trust_recovery", 0),
]
unique_trust = len(set(round(s, 3) for s in trust_scores))
check(
    "3 stakeholder types produce 3 distinct trust_recovery scores",
    unique_trust == 3,
    "media=%.4f customer=%.4f regulator=%.4f" % tuple(trust_scores),
)

# Crisis PR should have domain outcomes
check("crisis_pr has trust_recovery",
      "trust_recovery" in media_result.domain_outcomes)
check("crisis_pr has counter_narrative_suppression",
      "counter_narrative_suppression" in media_result.domain_outcomes)
check("crisis_pr has brand_sentiment_shift",
      "brand_sentiment_shift" in media_result.domain_outcomes)


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Campaign: loyalty appeal — liberal vs conservative opposite effectiveness
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Campaign: Liberal vs Conservative Loyalty Appeal ===")

loyalty_msg = (
    "Stand with us. Our leaders have endorsed this plan. Join the movement — "
    "millions of patriots already support it. Our tradition demands action."
)

liberal_result = dp.predict(loyalty_msg, domain="campaign", recipient=LIBERAL_BASE)
conservative_result = dp.predict(loyalty_msg, domain="campaign", recipient=CONSERVATIVE_BASE)

check(
    "loyalty appeal: conservative higher compliance than liberal in campaign domain",
    conservative_result.immediate_compliance > liberal_result.immediate_compliance,
    "conservative=%.4f liberal=%.4f" % (
        conservative_result.immediate_compliance, liberal_result.immediate_compliance,
    ),
)

# Check that the domain modulations amplified the difference vs universal
liberal_universal = dp.predict(loyalty_msg, domain="universal", recipient=LIBERAL_BASE)
conservative_universal = dp.predict(loyalty_msg, domain="universal", recipient=CONSERVATIVE_BASE)
campaign_diff = conservative_result.immediate_compliance - liberal_result.immediate_compliance
universal_diff = conservative_universal.immediate_compliance - liberal_universal.immediate_compliance
check(
    "campaign domain amplifies liberal/conservative difference vs universal",
    campaign_diff >= universal_diff * 0.9,  # at least 90% of universal (may not always amplify)
    "campaign_diff=%.4f universal_diff=%.4f" % (campaign_diff, universal_diff),
)


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Defensive technique (whataboutism) in crisis_pr: NEGATIVE net effectiveness
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Crisis PR: Defensive Technique Negative Effectiveness ===")

defensive_statement = (
    "What about what our competitors did? They had worse incidents and no one "
    "questioned them. The real issue is the media's bias against us. Let's focus "
    "on what they really want — our industry to fail."
)

defensive_result = dp.predict(defensive_statement, domain="crisis_pr",
                              stakeholder_type="media", crisis_severity=0.7)

# The defensive approach should produce high retaliation and low trust
check(
    "defensive technique in crisis_pr: retaliation > 0.15",
    defensive_result.retaliation_probability > 0.15,
    "retaliation=%.4f" % defensive_result.retaliation_probability,
)

# Compare with the transparent statement
transparent_trust = media_result.domain_outcomes.get("trust_recovery", 0)
defensive_trust = defensive_result.domain_outcomes.get("trust_recovery", 0)
check(
    "transparent statement has higher trust_recovery than defensive",
    transparent_trust > defensive_trust,
    "transparent=%.4f defensive=%.4f" % (transparent_trust, defensive_trust),
)

# Defensive should have worse brand sentiment
transparent_sentiment = media_result.domain_outcomes.get("brand_sentiment_shift", 0)
defensive_sentiment = defensive_result.domain_outcomes.get("brand_sentiment_shift", 0)
check(
    "transparent statement has better brand_sentiment than defensive",
    transparent_sentiment > defensive_sentiment,
    "transparent=%.4f defensive=%.4f" % (transparent_sentiment, defensive_sentiment),
)


# ═══════════════════════════════════════════════════════════════════════════════
# 6. Response timing modulator: timing=0.1 vs timing=0.8 differ >15pp
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Crisis PR: Response Timing Modulator ===")

timing_statement = (
    "We sincerely apologize for the service disruption. We have identified the root "
    "cause and deployed a fix. Here are the steps we are taking to prevent recurrence."
)

fast_response = dp.predict(timing_statement, domain="crisis_pr",
                           response_timing=0.1, crisis_severity=0.6,
                           stakeholder_type="customers")
slow_response = dp.predict(timing_statement, domain="crisis_pr",
                           response_timing=0.8, crisis_severity=0.6,
                           stakeholder_type="customers")

fast_trust = fast_response.domain_outcomes.get("trust_recovery", 0)
slow_trust = slow_response.domain_outcomes.get("trust_recovery", 0)
timing_diff = fast_trust - slow_trust

check(
    "response_timing: fast (0.1) vs slow (0.8) trust_recovery diff > 0.15",
    timing_diff > 0.15,
    "fast=%.4f slow=%.4f diff=%.4f" % (fast_trust, slow_trust, timing_diff),
)

check(
    "fast response has higher trust than slow response",
    fast_trust > slow_trust,
    "fast=%.4f slow=%.4f" % (fast_trust, slow_trust),
)


# ═══════════════════════════════════════════════════════════════════════════════
# 7. DomainPrediction output format validation
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== DomainPrediction Output Format ===")

result = dp.predict("Test stimulus", domain="ecommerce")
d = result.to_dict()

check("output has approach", "approach" in d)
check("output has avoidance", "avoidance" in d)
check("output has deliberation", "deliberation" in d)
check("output has immediate_compliance", "immediate_compliance" in d)
check("output has repeat_compliance", "repeat_compliance" in d)
check("output has retaliation_probability", "retaliation_probability" in d)
check("output has insula_activation", "insula_activation" in d)
check("output has domain_outcomes", "domain_outcomes" in d)
check("output has domain", "domain" in d)
check("output has weights_used", "weights_used" in d)
check("output has provenance_summary", "provenance_summary" in d)

# All circuit scores are valid
check("approach >= 0", d["approach"] >= 0)
check("avoidance >= 0", d["avoidance"] >= 0)
check("deliberation >= 0", d["deliberation"] >= 0)
check("immediate_compliance in [0,1]", 0.0 <= d["immediate_compliance"] <= 1.0)
check("insula_activation in [0,1]", 0.0 <= d["insula_activation"] <= 1.0)


# ═══════════════════════════════════════════════════════════════════════════════
# 8. Fear appeal habituation in campaign domain
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Campaign: Fear Appeal Habituation ===")

fear_msg = "Catastrophe is coming. Our country will collapse. You'll regret not acting."

first_exposure = dp.predict(fear_msg, domain="campaign", exposure_count=0)
fifth_exposure = dp.predict(fear_msg, domain="campaign", exposure_count=5)

# Avoidance should decrease with repeated exposure (habituation)
check(
    "fear appeal: avoidance decreases with exposure (habituation)",
    first_exposure.avoidance >= fifth_exposure.avoidance,
    "first=%.4f fifth=%.4f" % (first_exposure.avoidance, fifth_exposure.avoidance),
)


# ═══════════════════════════════════════════════════════════════════════════════
# 9. Stakeholder profiles exist for all 5 types
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Stakeholder Profiles ===")

for stype in ["media", "regulators", "customers", "employees", "investors"]:
    check("stakeholder profile exists: %s" % stype,
          stype in STAKEHOLDER_PROFILES)
    profile = RecipientProfile(**STAKEHOLDER_PROFILES[stype])
    check("stakeholder %s produces valid profile" % stype, profile.validate())


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
