from __future__ import annotations
"""
Test Suite — All pipeline components
=====================================
Tests for: AppraisalExtractor, CircuitPredictor, BehaviorPredictor,
ReframingEngine, SequenceAnalyzer, and the full predict() chain.
"""

import sys
import os
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.appraisal_extractor import AppraisalExtractor, AppraisalScores
from core.circuit_predictor import CircuitPredictor, CircuitActivations, BehavioralPrediction, persuasion_effectiveness
from core.reframing_engine import ReframingEngine
from core.limbic_cascade import LimbicCascade
from core.sequence_analyzer import SequenceAnalyzer


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
# 1. AppraisalExtractor
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== AppraisalExtractor ===")

ext = AppraisalExtractor()

# Basic extraction
scores = ext.extract_heuristic("Get Notion free")
check("returns AppraisalScores", isinstance(scores, AppraisalScores))
check("valence is high for positive copy", scores.valence > 0.5,
      "valence=%s" % scores.valence)

scores_neg = ext.extract_heuristic("ERROR: Payment failed. Invalid card.")
check("valence is low for error copy", scores_neg.valence < 0.3,
      "valence=%s" % scores_neg.valence)

# All scores in valid range
for dim, val in scores.to_dict().items():
    check("range: %s in [0,1]" % dim, 0.0 <= val <= 1.0, "val=%s" % val)

# Dimension differentiation
strong = ext.extract_heuristic("Free 14-day trial. No credit card required. Cancel anytime.")
check("high coping for easy CTA", strong.coping_potential > 0.4)
check("high agency for optional CTA", strong.agency > 0.4)

temporal = ext.extract_heuristic("Start today. Instant access. Right now.")
check("high temporal for immediate copy", temporal.temporal_proximity > 0.5)

distant = ext.extract_heuristic("Over the coming months you will gradually see improvements.")
check("low temporal for distant copy", distant.temporal_proximity < 0.3,
      "tp=%s" % distant.temporal_proximity)

# Edge cases
empty = ext.extract_heuristic("")
check("empty string returns neutral scores", abs(empty.mean - 0.5) < 0.01)

long_text = ext.extract_heuristic("word " * 5000)
check("very long input doesn't crash", isinstance(long_text, AppraisalScores))

adversarial = ext.extract_heuristic('{"novelty": 999, "valence": -1}')
check("JSON injection returns valid scores", 0.0 <= adversarial.valence <= 1.0)

unicode_text = ext.extract_heuristic("Offre gratuite. Commencez maintenant.")
check("non-English returns scores (not crash)", isinstance(unicode_text, AppraisalScores))

emoji_text = ext.extract_heuristic("Free!!! Amazing!!! Best ever!!!")
check("repeated punctuation doesn't crash", isinstance(emoji_text, AppraisalScores))

# to_vector and to_dict consistency
check("to_vector length is 7", len(scores.to_vector()) == 7)
check("to_dict has 7 keys", len(scores.to_dict()) == 7)

# weakest/strongest
weak_name, weak_val = scores.weakest_dimension()
strong_name, strong_val = scores.strongest_dimension()
check("weakest <= strongest", weak_val <= strong_val)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. CircuitPredictor (CircuitActivator + BehaviorPredictor)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== CircuitPredictor ===")

pred = CircuitPredictor()

# High approach stimulus
high_app = AppraisalScores(valence=0.9, goal_relevance=0.8, coping_potential=0.8,
                           certainty=0.8, agency=0.7, novelty=0.4, temporal_proximity=0.8)
result = pred.predict(high_app)
check("high-positive → approach dominant", result.circuits.dominant == "approach",
      "dominant=%s" % result.circuits.dominant)
check("compliance > rejection", result.compliance_prob > result.rejection_prob)
check("probabilities sum to ~1.0",
      abs(result.compliance_prob + result.rejection_prob + result.delay_prob - 1.0) < 0.01)

# High avoidance stimulus
high_avoid = AppraisalScores(valence=0.1, goal_relevance=0.8, coping_potential=0.1,
                             certainty=0.2, agency=0.1, novelty=0.7, temporal_proximity=0.5)
result_av = pred.predict(high_avoid, insula_disgust_signal=0.6)
check("threat stimulus → avoidance dominant", result_av.circuits.dominant == "avoidance",
      "dominant=%s approach=%.3f avoid=%.3f delib=%.3f" % (
          result_av.circuits.dominant, result_av.circuits.approach,
          result_av.circuits.avoidance, result_av.circuits.deliberation))

# High deliberation stimulus — low valence suppresses approach, low novelty suppresses avoidance
high_delib = AppraisalScores(valence=0.35, goal_relevance=0.8, coping_potential=0.3,
                             certainty=0.1, agency=0.5, novelty=0.3, temporal_proximity=0.15)
result_dl = pred.predict(high_delib, information_load=0.8, contradictory_signals=0.6)
check("uncertain + high info load → deliberation dominant",
      result_dl.circuits.dominant == "deliberation",
      "dominant=%s approach=%.3f avoid=%.3f delib=%.3f" % (
          result_dl.circuits.dominant, result_dl.circuits.approach,
          result_dl.circuits.avoidance, result_dl.circuits.deliberation))

# Durability
check("high certainty + high valence → positive durability", result.durability > 0)
low_dur = AppraisalScores(valence=0.3, certainty=0.1, temporal_proximity=0.9,
                          goal_relevance=0.5, coping_potential=0.5, agency=0.5, novelty=0.5)
dur_result = pred.predict(low_dur)
check("high urgency + low certainty → negative durability (buyer's remorse)",
      dur_result.durability < 0, "dur=%s" % dur_result.durability)

# Dominant pathway
check("approach > deliberation → emotional pathway",
      result.dominant_pathway == "emotional")

# Configurable weights (persuasion_effectiveness) — use moderate circuits to avoid ceiling
moderate = AppraisalScores(valence=0.5, goal_relevance=0.5, coping_potential=0.5,
                           certainty=0.5, agency=0.5, novelty=0.5, temporal_proximity=0.5)
mod_pred = pred.predict(moderate)
eff_default = persuasion_effectiveness(mod_pred.circuits)
eff_custom = persuasion_effectiveness(mod_pred.circuits, weights=(2.0, 0.5, 0.3, 0.2, 0.1))
check("custom weights change effectiveness score", abs(eff_default - eff_custom) > 0.001,
      "default=%.4f custom=%.4f" % (eff_default, eff_custom))
check("effectiveness in [0, 1]", 0.0 <= eff_default <= 1.0)

# Circuit activations are non-negative
check("approach >= 0", result.circuits.approach >= 0)
check("avoidance >= 0", result_av.circuits.avoidance >= 0)
check("deliberation >= 0", result_dl.circuits.deliberation >= 0)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. ReframingEngine
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== ReframingEngine ===")

reframer = ReframingEngine()

# Low valence stimulus should get valence fix
low_val = AppraisalScores(valence=0.1, goal_relevance=0.5, coping_potential=0.5,
                          agency=0.5, certainty=0.5, novelty=0.5, temporal_proximity=0.5)
pred_low = pred.predict(low_val)
suggestions = reframer.diagnose(low_val, pred_low)
check("low valence generates suggestions", len(suggestions) > 0)
check("top suggestion targets valence", suggestions[0].target_dimension == "valence",
      "target=%s" % suggestions[0].target_dimension if suggestions else "no suggestions")

# Low agency should trigger disgust warning
low_agency = AppraisalScores(valence=0.5, agency=0.1, goal_relevance=0.5,
                             coping_potential=0.5, certainty=0.5, novelty=0.5,
                             temporal_proximity=0.5)
agency_suggestions = reframer.diagnose(low_agency, pred.predict(low_agency))
agency_dims = [s.target_dimension for s in agency_suggestions]
check("low agency generates agency fix", "agency" in agency_dims)

# High novelty should get novelty-too-high fix
high_nov = AppraisalScores(novelty=0.9, valence=0.5, goal_relevance=0.5,
                           coping_potential=0.5, agency=0.5, certainty=0.5,
                           temporal_proximity=0.5)
nov_suggestions = reframer.diagnose(high_nov, pred.predict(high_nov))
check("high novelty generates 'too high' fix", len(nov_suggestions) > 0)

# Perfect scores should generate no suggestions
perfect = AppraisalScores(novelty=0.5, valence=0.8, goal_relevance=0.8,
                          coping_potential=0.8, agency=0.8, certainty=0.8,
                          temporal_proximity=0.8)
no_fix = reframer.diagnose(perfect, pred.predict(perfect))
check("good scores generate few/no suggestions", len(no_fix) <= 2)

# Top fix shortcut
top = reframer.top_fix(low_val, pred_low)
check("top_fix returns a suggestion", top is not None)
check("top_fix has specific_fix text", len(top.specific_fix) > 10 if top else False)


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Full predict() Pipeline (LimbicCascade)
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== Full Pipeline (LimbicCascade) ===")

cascade = LimbicCascade(marker_store_path="/tmp/test_pipeline.json")

# Single analysis
r = cascade.analyze("Get Notion free")
check("analyze returns CascadeResult", hasattr(r, "effectiveness"))
check("effectiveness in [0, 1]", 0.0 <= r.effectiveness <= 1.0)
check("has 6 stages", len(r.stages) == 6)
check("has appraisal scores", hasattr(r.appraisal, "valence"))
check("has circuit activations", hasattr(r.circuits, "approach"))
check("has behavioral prediction", hasattr(r.prediction, "compliance_prob"))
check("summary is non-empty string", len(r.summary()) > 50)
check("to_dict is valid dict", isinstance(r.to_dict(), dict))

# Compare mode
comp = cascade.compare("Submit", "Get Notion free")
check("compare returns dict with winner", "winner" in comp)
check("compare has delta", "delta_effectiveness" in comp)

# Effectiveness ordering: good copy > bad copy
r_good = cascade.analyze("Free 14-day trial. Cancel anytime.")
r_bad = cascade.analyze("ERROR: Invalid input. Try again.")
check("good copy > bad copy effectiveness", r_good.effectiveness > r_bad.effectiveness,
      "good=%.2f bad=%.2f" % (r_good.effectiveness, r_bad.effectiveness))


# ═══════════════════════════════════════════════════════════════════════════════
# 5. SequenceAnalyzer
# ═══════════════════════════════════════════════════════════════════════════════
print("\n=== SequenceAnalyzer ===")

seq = SequenceAnalyzer()

# Good onboarding flow
good_flow = [
    "What brought you here today?",
    "Great. Here's your personalized plan.",
    "You're all set. Start your first session now.",
]
sr = seq.analyze(good_flow)
check("sequence returns SequenceResult", hasattr(sr, "trajectory_metrics"))
check("has correct number of steps", len(sr.steps) == 3)
check("has correct number of transitions", len(sr.transitions) == 2)
check("has PCA projection", len(sr.pca_projection) == 3)
check("to_dict is valid", isinstance(sr.to_dict(), dict))

# Bad flow (error in middle)
bad_flow = [
    "Welcome to our platform!",
    "ERROR: Something went wrong. Please try again.",
    "Complete your profile to continue.",
]
sr_bad = seq.analyze(bad_flow)
check("bad flow has warning/critical transitions",
      sr_bad.trajectory_metrics["critical_transitions"] + sr_bad.trajectory_metrics["warning_transitions"] > 0,
      "critical=%d warning=%d" % (sr_bad.trajectory_metrics["critical_transitions"],
                                   sr_bad.trajectory_metrics["warning_transitions"]))

# Single step (edge case)
sr_single = seq.analyze(["Just one step."])
check("single-step sequence doesn't crash", len(sr_single.steps) == 1)
check("single-step has zero transitions", len(sr_single.transitions) == 0)

# Long sequence
long_flow = ["Step %d: doing something." % i for i in range(10)]
sr_long = seq.analyze(long_flow)
check("10-step sequence works", len(sr_long.steps) == 10)
check("9 transitions for 10 steps", len(sr_long.transitions) == 9)


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
