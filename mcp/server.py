"""
Persuasion-Max MCP Server
==========================
Model Context Protocol server exposing the limbic cascade engine
and training engine as MCP tools. Any MCP-compatible client
(Claude Desktop, OpenClaw, etc.) can call these.

Run: python mcp/server.py
"""

import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp.server_lib import MCPServer, tool


class PersuasionMaxMCP(MCPServer):
    """MCP server wrapping the full Persuasion-Max engine."""

    def __init__(self):
        super().__init__(
            name="persuasion-max",
            description="Limbic decision cascade analysis + persuasion training engine. "
                        "Neuroanatomical circuit-level persuasion analysis with 7 cognitive "
                        "appraisal dimensions, 3 competing circuit predictions, somatic markers, "
                        "and a unified training engine for persuasion games.",
            version="1.0.0",
        )
        from core.limbic_cascade import LimbicCascade
        from core.ux_patterns import UXPatternLibrary
        from core.technique_to_appraisal import apply_technique_impacts, TECHNIQUE_IMPACTS
        from core.appraisal_extractor import AppraisalScores
        from training.scorer import ResponseScorer
        from training.techniques import TechniqueLibrary
        from training.engagement import RewardSequencer, DifficultyEngine, SpacedRepetition

        self.cascade = LimbicCascade()
        self.patterns = UXPatternLibrary()
        self.technique_impacts = TECHNIQUE_IMPACTS
        self.scorer = ResponseScorer()
        self.techniques = TechniqueLibrary()
        self.reward_seq = RewardSequencer()
        self.difficulty = DifficultyEngine()
        self.srs = SpacedRepetition()

    # ─── Analysis Tools ──────────────────────────────────────────────────

    @tool(
        name="analyze",
        description="Run a full 6-stage limbic decision cascade on any text stimulus. "
                    "Returns effectiveness score, predicted behavior (compliance/rejection/delay), "
                    "7 appraisal dimension scores, 3 circuit activations, and reframing suggestions.",
    )
    def analyze(self, text: str, context: str = None, multimodal_channels: int = 1) -> dict:
        result = self.cascade.analyze(
            text, context=context, multimodal_channels=multimodal_channels,
        )
        return result.to_dict()

    @tool(
        name="compare",
        description="A/B compare two text stimuli. Returns effectiveness scores, "
                    "behavioral predictions, appraisal dimension deltas, and a winner.",
    )
    def compare(self, text_a: str, text_b: str) -> dict:
        return self.cascade.compare(text_a, text_b)

    @tool(
        name="patterns",
        description="Search the UX pattern library. Find success/failure patterns "
                    "by category (error, pricing, cta, etc.), by weak dimension, "
                    "or by full-text search. Returns circuit-level mechanism explanations.",
    )
    def get_patterns(self, category: str = None, weak: str = None, search: str = None) -> list:
        if weak:
            results = self.patterns.for_weak_dimension(weak)
        elif category:
            results = self.patterns.by_category(category)
        elif search:
            results = self.patterns.search(search)
        else:
            return {"categories": self.patterns.categories(), "total": len(self.patterns.patterns)}
        return [
            {"category": p.category, "outcome": p.outcome, "product": p.product,
             "description": p.description, "circuit": p.circuit, "mechanism": p.mechanism}
            for p in results
        ]

    @tool(
        name="technique_bridge",
        description="Apply detected persuasion technique impacts to appraisal scores. "
                    "Takes a list of detected technique names and optional base appraisal, "
                    "returns adjusted appraisal scores and aggregate disgust risk.",
    )
    def technique_bridge(self, techniques_detected: list, base_appraisal: dict = None) -> dict:
        from core.appraisal_extractor import AppraisalScores
        from core.technique_to_appraisal import apply_technique_impacts
        base = base_appraisal or AppraisalScores().to_dict()
        adjusted, disgust = apply_technique_impacts(base, techniques_detected)
        return {"adjusted_appraisal": adjusted, "aggregate_disgust_risk": disgust}

    # ─── Training Tools ──────────────────────────────────────────────────

    @tool(
        name="score_response",
        description="Score a player response against NPC psychology. Returns skill scores "
                    "across 9 axes, detected tone, identified techniques, risk level, "
                    "and near-miss detection.",
    )
    def score_response(self, response_text: str, npc_id: str, difficulty: str = "standard") -> dict:
        return self.scorer.score(response_text, npc_id, difficulty)

    @tool(
        name="evaluate_combo",
        description="Evaluate a technique combo sequence (2-5 tags like "
                    "'warm', 'vulnerable', 'bold'). Returns synergy multiplier and analysis.",
    )
    def evaluate_combo(self, tags: list) -> dict:
        return self.scorer.evaluate_combo(tags)

    @tool(
        name="list_techniques",
        description="List all techniques from the master library. Optionally filter by category: "
                    "rapport, extraction, compliance, framing, emotional_escalation, "
                    "emotional_manipulation, behavioral_conditioning, cognitive_distortion.",
    )
    def list_techniques(self, category: str = None) -> list:
        return self.techniques.list(category=category)

    @tool(
        name="get_technique",
        description="Get detailed info about a specific technique by ID. Includes "
                    "psychological mechanism, neural basis, detection markers, "
                    "counter-strategy, combo partners, and appraisal dimension shifts.",
    )
    def get_technique(self, technique_id: str) -> dict:
        return self.techniques.get(technique_id)

    @tool(
        name="reward_sequence",
        description="Get timing parameters for the 7-second reward arc. "
                    "event_type: breakthrough, near_miss, skill_unlock, combo_hit, micro_reward. "
                    "intensity: low, normal, high. Returns phase-by-phase visual/audio/haptic params.",
    )
    def reward_sequence(self, event_type: str = "breakthrough", intensity: str = "normal") -> dict:
        return self.reward_seq.get_sequence(event_type, intensity)

    @tool(
        name="difficulty_level",
        description="Get difficulty modifiers for a training level. "
                    "level: guided, standard, authentic, intense.",
    )
    def difficulty_level(self, level: str = "standard") -> dict:
        return self.difficulty.get_level(level)

    @tool(
        name="srs_due",
        description="Get social skills due for spaced repetition review. "
                    "Returns skills sorted by urgency (lowest recall probability first).",
    )
    def srs_due(self) -> list:
        return self.srs.get_due_cards()

    @tool(
        name="srs_update",
        description="Update a spaced repetition card after practicing a skill. "
                    "quality: 1 (fail) to 5 (perfect). Adjusts stability and next review interval.",
    )
    def srs_update(self, skill_id: str, quality: int) -> dict:
        return self.srs.update_card(skill_id, quality)


# ─── Minimal MCP server library ─────────────────────────────────────────────
# This is a standalone implementation that doesn't require the mcp pip package.
# It speaks the MCP JSON-RPC protocol over stdin/stdout.

if __name__ == "__main__":
    server = PersuasionMaxMCP()
    server.run()
