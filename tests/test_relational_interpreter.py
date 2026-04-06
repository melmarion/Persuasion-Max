from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.appraisal_extractor import AppraisalScores
from core.circuit_predictor import CircuitPredictor
from core.relational_interpreter import RelationalInterpreter


def test_interpretation_is_user_only():
    pred = CircuitPredictor()
    interpreter = RelationalInterpreter()
    appraisal = AppraisalScores(
        valence=0.35,
        goal_relevance=0.7,
        coping_potential=0.4,
        certainty=0.2,
        agency=0.5,
        novelty=0.4,
        temporal_proximity=0.3,
    )
    result = pred.predict(appraisal, information_load=0.8, contradictory_signals=0.5)
    interpretation = interpreter.interpret("unclear message", appraisal, result.circuits, result)

    assert interpretation.user_only is True
    assert interpretation.suggested_outbound_text is None
    assert interpretation.pattern_label == "ambiguity_or_non-commitment"
    assert "non-commitment" in interpretation.clean_internal_translation
    assert "ambiguity" in interpretation.signal_present.lower()
    assert "narrow next-step question" in interpretation.calibrated_question_posture
    assert "make the next step smaller" in interpretation.next_move


def test_soft_rejection_translation_does_not_pathologize():
    pred = CircuitPredictor()
    interpreter = RelationalInterpreter()
    appraisal = AppraisalScores(
        valence=0.15,
        goal_relevance=0.5,
        coping_potential=0.2,
        certainty=0.3,
        agency=0.35,
        novelty=0.4,
        temporal_proximity=0.4,
    )
    result = pred.predict(appraisal, insula_disgust_signal=0.45)
    interpretation = interpreter.interpret("distancing text", appraisal, result.circuits, result)

    assert interpretation.pattern_label == "soft_rejection_or_distancing"
    assert "does not prove" in interpretation.what_this_does_not_prove.lower()
    assert "my value" in interpretation.what_this_does_not_prove.lower()
    assert "distance is being created" in interpretation.distancing_read
    assert "not cornering" in interpretation.autonomy_protection
