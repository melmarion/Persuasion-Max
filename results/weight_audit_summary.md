# Weight Registry Audit Summary

**Date:** 2026-03-28
**Total parameters:** 302

## Provenance Breakdown

| Status | Count | % |
|--------|-------|---|
| CALIBRATED | 2 | 0.7% |
| CONSTRAINED | 184 | 60.9% |
| FITTED | 3 | 1.0% |
| UNCALIBRATED | 113 | 37.4% |

**Empirically grounded (FITTED + CALIBRATED + CONSTRAINED):** 189 (62.6%)
**Uncalibrated (theoretical only):** 113 (37.4%)
**Flagged as potentially unreliable:** 53

## By Layer

| Layer | Count |
|-------|-------|
| L2_circuit | 32 |
| L3_technique | 209 |
| L4_recipient | 27 |
| L5_domain | 26 |
| detector | 8 |

## By Module

| Module | Count |
|--------|-------|
| circuit_predictor | 32 |
| domain_registry | 26 |
| influence_detector | 8 |
| recipient_modulator | 27 |
| technique_to_circuit | 209 |

## Flagged Weights

| Weight | Module | Value | Flags |
|--------|--------|-------|-------|
| tech.logical_appeal.circuit.deliberation | technique_to_circuit | 1.15 | OUTLIER |
| tech.expert_testimony.circuit.deliberati | technique_to_circuit | 0.85 | OUTLIER |
| tech.social_proof.circuit.deliberation | technique_to_circuit | 0.8 | OUTLIER |
| tech.authority_endorsement.circuit.delib | technique_to_circuit | 0.85 | OUTLIER |
| tech.bandwagon.circuit.deliberation | technique_to_circuit | 0.85 | OUTLIER |
| tech.emotional_appeal_positive.circuit.a | technique_to_circuit | 1.15 | OUTLIER |
| tech.emotional_appeal_positive.circuit.d | technique_to_circuit | 0.9 | OUTLIER |
| tech.emotional_appeal_negative.circuit.a | technique_to_circuit | 1.1 | OUTLIER |
| tech.reciprocity.circuit.approach | technique_to_circuit | 1.1 | OUTLIER |
| tech.scarcity_appeal.circuit.avoidance | technique_to_circuit | 1.1 | OUTLIER |
| tech.scarcity_appeal.circuit.deliberatio | technique_to_circuit | 0.85 | OUTLIER |
| tech.urgency_appeal.circuit.deliberation | technique_to_circuit | 0.8 | OUTLIER |
| tech.gain_frame.circuit.approach | technique_to_circuit | 1.05 | OUTLIER |
| tech.loss_frame.circuit.avoidance | technique_to_circuit | 1.15 | OUTLIER |
| tech.loss_frame.circuit.approach | technique_to_circuit | 1.1 | OUTLIER |
| tech.anchoring.circuit.deliberation | technique_to_circuit | 0.9 | OUTLIER |
| tech.emotional_manipulation.circuit.avoi | technique_to_circuit | 1.2 | OUTLIER |
| tech.gaslighting.circuit.deliberation | technique_to_circuit | 1.3 | OUTLIER |
| tech.false_equivalence.circuit.deliberat | technique_to_circuit | 1.1 | OUTLIER |
| tech.guilt_tripping.circuit.avoidance | technique_to_circuit | 1.15 | OUTLIER |
| tech.guilt_tripping.circuit.approach | technique_to_circuit | 1.05 | OUTLIER |
| tech.fear_mongering.circuit.avoidance | technique_to_circuit | 1.4 | OUTLIER |
| tech.false_scarcity.circuit.avoidance | technique_to_circuit | 1.1 | OUTLIER |
| tech.ad_hominem.circuit.avoidance | technique_to_circuit | 1.2 | OUTLIER |
| tech.name_calling.circuit.avoidance | technique_to_circuit | 1.25 | OUTLIER |
| tech.straw_man.circuit.deliberation | technique_to_circuit | 1.15 | OUTLIER |
| tech.whataboutism.circuit.deliberation | technique_to_circuit | 1.1 | OUTLIER |
| tech.false_dilemma.circuit.deliberation | technique_to_circuit | 0.8 | OUTLIER |
| tech.slippery_slope.circuit.avoidance | technique_to_circuit | 1.1 | OUTLIER |
| tech.appeal_to_ignorance.circuit.deliber | technique_to_circuit | 1.1 | OUTLIER |
| tech.manipulative_flattery.circuit.delib | technique_to_circuit | 0.8 | OUTLIER |
| tech.appeal_to_pity.circuit.avoidance | technique_to_circuit | 1.05 | OUTLIER |
| tech.appeal_to_pity.circuit.approach | technique_to_circuit | 1.05 | OUTLIER |
| tech.obfuscation.circuit.deliberation | technique_to_circuit | 1.3 | OUTLIER |
| tech.bandwagon_pressure.circuit.avoidanc | technique_to_circuit | 1.1 | OUTLIER |
| tech.bandwagon_pressure.circuit.delibera | technique_to_circuit | 0.85 | OUTLIER |
| tech.high_ground_maneuver.circuit.approa | technique_to_circuit | 1.15 | OUTLIER |
| tech.identity_lock.circuit.approach | technique_to_circuit | 1.2 | OUTLIER |
| tech.pacing_and_leading.circuit.approach | technique_to_circuit | 1.1 | OUTLIER |
| tech.pacing_and_leading.circuit.delibera | technique_to_circuit | 0.85 | OUTLIER |
| tech.future_pacing.circuit.approach | technique_to_circuit | 1.15 | OUTLIER |
| tech.contrast_principle.circuit.approach | technique_to_circuit | 1.1 | OUTLIER |
| tech.contrast_principle.circuit.delibera | technique_to_circuit | 0.9 | OUTLIER |
| tech.curiosity_gap.circuit.approach | technique_to_circuit | 1.15 | OUTLIER |
| tech.curiosity_gap.circuit.deliberation | technique_to_circuit | 0.8 | OUTLIER |
| tech.labeling.circuit.deliberation | technique_to_circuit | 0.85 | OUTLIER |
| tech.door_in_the_face.circuit.approach | technique_to_circuit | 1.1 | OUTLIER |
| tech.foot_in_the_door.circuit.approach | technique_to_circuit | 1.05 | OUTLIER |
| tech.thinking_past_the_sale.circuit.appr | technique_to_circuit | 1.15 | OUTLIER |
| tech.linguistic_kill_shot.circuit.avoida | technique_to_circuit | 1.3 | OUTLIER |
| tech.unity.circuit.approach | technique_to_circuit | 1.15 | OUTLIER |
| tech.unity.circuit.deliberation | technique_to_circuit | 0.85 | OUTLIER |
| tech.calibrated_question.circuit.deliber | technique_to_circuit | 1.2 | OUTLIER |