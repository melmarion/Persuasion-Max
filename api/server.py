"""
Persuasion-Max API Server
==========================
FastAPI server exposing the limbic cascade engine and training engine
as REST endpoints. Any React/Swift app can call these.

Run: uvicorn api.server:app --reload --port 8100
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional

from core.limbic_cascade import LimbicCascade
from core.circuit_predictor import persuasion_effectiveness
from core.appraisal_extractor import AppraisalScores
from core.ux_patterns import UXPatternLibrary
from core.technique_to_appraisal import apply_technique_impacts, TECHNIQUE_IMPACTS
from training.scorer import ResponseScorer
from training.techniques import TechniqueLibrary
from training.engagement import RewardSequencer, DifficultyEngine, SpacedRepetition

app = FastAPI(
    title="Persuasion-Max Engine",
    description="Limbic decision cascade analysis + persuasion training engine",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

cascade = LimbicCascade()
patterns = UXPatternLibrary()
scorer = ResponseScorer()
techniques = TechniqueLibrary()
reward_seq = RewardSequencer()
difficulty = DifficultyEngine()
srs = SpacedRepetition()


# ─── Analysis Endpoints ─────────────────────────────────────────────────────

class AnalyzeRequest(BaseModel):
    text: str
    context: Optional[str] = None
    mode: str = "heuristic"
    multimodal_channels: int = 1
    domain: str = "universal"

class CompareRequest(BaseModel):
    text_a: str
    text_b: str
    mode: str = "heuristic"


@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    """Run full 6-stage limbic cascade on a stimulus."""
    c = LimbicCascade(extraction_mode=req.mode)
    result = c.analyze(
        req.text,
        context=req.context,
        multimodal_channels=req.multimodal_channels,
    )
    return result.to_dict()


@app.post("/compare")
def compare(req: CompareRequest):
    """A/B compare two stimuli."""
    c = LimbicCascade(extraction_mode=req.mode)
    return c.compare(req.text_a, req.text_b)


@app.get("/patterns")
def get_patterns(
    category: Optional[str] = None,
    weak: Optional[str] = None,
    search: Optional[str] = None,
):
    """Search the UX pattern library."""
    if weak:
        results = patterns.for_weak_dimension(weak)
    elif category:
        results = patterns.by_category(category)
    elif search:
        results = patterns.search(search)
    else:
        return {"categories": patterns.categories(), "total": len(patterns.patterns)}
    return [
        {
            "category": p.category,
            "outcome": p.outcome,
            "product": p.product,
            "description": p.description,
            "circuit": p.circuit,
            "mechanism": p.mechanism,
            "appraisal_scores": p.appraisal_scores,
        }
        for p in results
    ]


class OptimizeRequest(BaseModel):
    goal: str
    context: str = "general"
    audience: str = "general web user"
    iterations: int = 3
    candidates_per_round: int = 5
    domain: str = "universal"

@app.post("/optimize")
def optimize_copy(req: OptimizeRequest):
    """Generate maximally persuasive copy via iterative scoring."""
    from core.optimization_engine import OptimizationEngine
    engine = OptimizationEngine(extraction_mode="heuristic")
    result = engine.optimize(
        goal=req.goal,
        context=req.context,
        audience=req.audience,
        iterations=req.iterations,
        candidates_per_round=req.candidates_per_round,
    )
    return result.to_dict()


class DomainPredictRequest(BaseModel):
    text: str
    domain: str = "universal"
    exposure_count: int = 0
    crisis_severity: float = 0.5
    response_timing: float = 0.5
    stakeholder_type: Optional[str] = None

@app.post("/domain-predict")
def domain_predict(req: DomainPredictRequest):
    """Run domain-aware prediction with domain-specific outcomes."""
    from core.domain_predictor import DomainPredictor
    dp = DomainPredictor()
    result = dp.predict(
        stimulus=req.text,
        domain=req.domain,
        exposure_count=req.exposure_count,
        crisis_severity=req.crisis_severity,
        response_timing=req.response_timing,
        stakeholder_type=req.stakeholder_type,
    )
    return result.to_dict()


@app.get("/techniques")
def get_technique_impacts():
    """Get all technique-to-appraisal mappings."""
    return {k: v.to_dict() for k, v in TECHNIQUE_IMPACTS.items()}


@app.post("/technique-bridge")
def technique_bridge(techniques_detected: list[str], base_appraisal: Optional[dict] = None):
    """Apply detected technique impacts to appraisal scores."""
    base = base_appraisal or AppraisalScores().to_dict()
    adjusted, disgust = apply_technique_impacts(base, techniques_detected)
    return {"adjusted_appraisal": adjusted, "aggregate_disgust_risk": disgust}


# ─── Training Engine Endpoints ──────────────────────────────────────────────

class ScoreRequest(BaseModel):
    response_text: str
    npc_id: str
    context: Optional[str] = None
    difficulty: str = "standard"

class ComboRequest(BaseModel):
    tags: list[str] = Field(..., min_length=2, max_length=5)

class SRSUpdateRequest(BaseModel):
    skill_id: str
    quality: int = Field(..., ge=1, le=5)


@app.post("/training/score")
def score_response(req: ScoreRequest):
    """Score a player response against NPC psychology."""
    return scorer.score(req.response_text, req.npc_id, req.difficulty)


@app.get("/training/techniques")
def list_techniques(category: Optional[str] = None):
    """List all techniques from the master library."""
    return techniques.list(category=category)


@app.get("/training/techniques/{technique_id}")
def get_technique(technique_id: str):
    """Get detailed technique info."""
    return techniques.get(technique_id)


@app.post("/training/combo")
def evaluate_combo(req: ComboRequest):
    """Evaluate a technique combo sequence."""
    return scorer.evaluate_combo(req.tags)


@app.get("/training/reward-sequence")
def get_reward_sequence(
    event_type: str = "breakthrough",
    intensity: str = "normal",
):
    """Get timing parameters for the 7-second reward sequence."""
    return reward_seq.get_sequence(event_type, intensity)


@app.get("/training/difficulty/{level}")
def get_difficulty(level: str):
    """Get difficulty modifiers for a level."""
    return difficulty.get_level(level)


@app.post("/training/srs/update")
def srs_update(req: SRSUpdateRequest):
    """Update spaced repetition card after practice."""
    return srs.update_card(req.skill_id, req.quality)


@app.get("/training/srs/due")
def srs_due():
    """Get skills due for review."""
    return srs.get_due_cards()


# ─── Sequence Analysis Endpoint ──────────────────────────────────────────────

class SequenceRequest(BaseModel):
    stimuli: list[str] = Field(..., min_length=2)

@app.post("/sequence")
def analyze_sequence(req: SequenceRequest):
    """Analyze an ordered sequence of stimuli as a trajectory."""
    from core.sequence_analyzer import SequenceAnalyzer
    analyzer = SequenceAnalyzer()
    result = analyzer.analyze(req.stimuli)
    return result.to_dict()


@app.get("/health")
def health():
    return {"status": "ok", "engine": "persuasion-max", "modules": ["limbic_cascade", "training_engine", "sequence_analyzer"]}
