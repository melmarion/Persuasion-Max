from __future__ import annotations

"""
Engagement Engine — Shared behavioral mechanics for training games
===================================================================
Extracted from charisma-training-game's 27-system engagement architecture.
Provides timing, difficulty, and spaced repetition as reusable modules.

Any training game (React, Swift, or otherwise) can call these via the API
to get consistent engagement parameters.
"""

import math
import time
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════════
# 7-SECOND REWARD SEQUENCE
# Based on casino anticipation arcs, repurposed for emotional breakthroughs.
# ═══════════════════════════════════════════════════════════════════════════════

SEQUENCE_PHASES = [
    {
        "id": "hook",
        "name": "The Hook",
        "start_ms": 0,
        "end_ms": 2000,
        "visual": {"glow_intensity": 0.2, "pulse_rate_hz": 0.5, "color_shift": 0.1, "blur": 0},
        "audio": {"volume": 0.3, "pitch": 1.0, "layers": 1},
        "haptic": {"intensity": 0.2, "pattern": "pulse", "interval_ms": 500},
        "psychology": "Something shifts. Player notices. Attention captured.",
    },
    {
        "id": "build",
        "name": "The Build",
        "start_ms": 2000,
        "end_ms": 5000,
        "visual": {"glow_intensity": 0.5, "pulse_rate_hz": 1.0, "color_shift": 0.4, "blur": 2},
        "audio": {"volume": 0.5, "pitch": 1.1, "layers": 2},
        "haptic": {"intensity": 0.4, "pattern": "heartbeat", "interval_ms": 400},
        "psychology": "Anticipation rises. 'Is this it?' Dopamine climbing.",
    },
    {
        "id": "peak",
        "name": "The Peak",
        "start_ms": 5000,
        "end_ms": 6500,
        "visual": {"glow_intensity": 0.8, "pulse_rate_hz": 2.0, "color_shift": 0.7, "blur": 4},
        "audio": {"volume": 0.7, "pitch": 1.2, "layers": 3},
        "haptic": {"intensity": 0.7, "pattern": "crescendo", "interval_ms": 200},
        "psychology": "Maximum tension. Breath held. This is the slot-machine pull moment.",
    },
    {
        "id": "release",
        "name": "The Release",
        "start_ms": 6500,
        "end_ms": 7000,
        "visual": {"glow_intensity": 1.0, "pulse_rate_hz": 0, "color_shift": 1.0, "blur": 0},
        "audio": {"volume": 1.0, "pitch": 1.3, "layers": 5},
        "haptic": {"intensity": 1.0, "pattern": "burst", "interval_ms": 0},
        "psychology": "Payoff. The moment lands. Maximum dopamine release.",
    },
    {
        "id": "afterglow",
        "name": "The Afterglow",
        "start_ms": 7000,
        "end_ms": 10000,
        "visual": {"glow_intensity": 0.4, "pulse_rate_hz": 0.3, "color_shift": 0.3, "blur": 1},
        "audio": {"volume": 0.3, "pitch": 0.95, "layers": 1},
        "haptic": {"intensity": 0.1, "pattern": "none", "interval_ms": 0},
        "psychology": "Let it sink in. Don't rush. This is where memory encoding happens.",
    },
]

REWARD_EVENTS = {
    "breakthrough": {
        "description": "NPC opens up or shifts behavior — the emotional jackpot",
        "intensity_scale": 1.0,
        "phases": SEQUENCE_PHASES,
    },
    "near_miss": {
        "description": "Almost had the breakthrough — keeps player trying",
        "intensity_scale": 0.6,
        "phases": SEQUENCE_PHASES,  # same phases, lower intensity
    },
    "skill_unlock": {
        "description": "New technique or skill recognized",
        "intensity_scale": 0.7,
        "phases": SEQUENCE_PHASES,
    },
    "combo_hit": {
        "description": "Player landed a named combo sequence",
        "intensity_scale": 0.8,
        "phases": SEQUENCE_PHASES,
    },
    "micro_reward": {
        "description": "Small positive NPC reaction — maintains engagement baseline",
        "intensity_scale": 0.3,
        "phases": SEQUENCE_PHASES[:2],  # hook + build only, no full arc
    },
}


class RewardSequencer:
    """Generate timing parameters for the 7-second reward arc."""

    def get_sequence(self, event_type: str = "breakthrough", intensity: str = "normal") -> dict:
        event = REWARD_EVENTS.get(event_type, REWARD_EVENTS["micro_reward"])
        intensity_mult = {"low": 0.6, "normal": 1.0, "high": 1.3}.get(intensity, 1.0)
        scale = event["intensity_scale"] * intensity_mult

        phases = []
        for phase in event["phases"]:
            scaled = dict(phase)
            scaled["visual"] = {k: round(v * scale, 2) if isinstance(v, float) else v
                                for k, v in phase["visual"].items()}
            scaled["audio"] = {k: round(v * scale, 2) if isinstance(v, float) else v
                               for k, v in phase["audio"].items()}
            scaled["haptic"] = {k: round(v * scale, 2) if isinstance(v, float) else v
                                for k, v in phase["haptic"].items()}
            phases.append(scaled)

        return {
            "event_type": event_type,
            "description": event["description"],
            "total_duration_ms": phases[-1]["end_ms"],
            "phases": phases,
        }


# ═══════════════════════════════════════════════════════════════════════════════
# DIFFICULTY ENGINE
# From charisma-training-game's 4-level system.
# ═══════════════════════════════════════════════════════════════════════════════

DIFFICULTY_LEVELS = {
    "guided": {
        "name": "Guided",
        "description": "Learn the foundations with helpful guidance",
        "metrics_visible": True,
        "metric_changes_visible": True,
        "tone_indicators_visible": True,
        "consequence_preview": True,
        "hints_enabled": True,
        "pressure_multiplier": 0.5,
        "ending_threshold_modifier": -10,
        "undo_available": True,
        "undo_count": 2,
        "scoring_multiplier": 0.7,
    },
    "standard": {
        "name": "Standard",
        "description": "Balanced challenge with fair feedback",
        "metrics_visible": True,
        "metric_changes_visible": False,
        "tone_indicators_visible": True,
        "consequence_preview": False,
        "hints_enabled": False,
        "pressure_multiplier": 1.0,
        "ending_threshold_modifier": 0,
        "undo_available": False,
        "undo_count": 0,
        "scoring_multiplier": 1.0,
    },
    "authentic": {
        "name": "Authentic",
        "description": "Minimal HUD. Conversations feel real.",
        "metrics_visible": False,
        "metric_changes_visible": False,
        "tone_indicators_visible": False,
        "consequence_preview": False,
        "hints_enabled": False,
        "pressure_multiplier": 1.3,
        "ending_threshold_modifier": 5,
        "undo_available": False,
        "undo_count": 0,
        "scoring_multiplier": 1.3,
    },
    "intense": {
        "name": "Intense",
        "description": "No hints. No metrics. Unforgiving relationships.",
        "metrics_visible": False,
        "metric_changes_visible": False,
        "tone_indicators_visible": False,
        "consequence_preview": False,
        "hints_enabled": False,
        "pressure_multiplier": 1.8,
        "ending_threshold_modifier": 15,
        "undo_available": False,
        "undo_count": 0,
        "scoring_multiplier": 1.6,
    },
}


class DifficultyEngine:
    """Provide difficulty modifiers for any training game."""

    def get_level(self, level: str) -> dict:
        return DIFFICULTY_LEVELS.get(level, DIFFICULTY_LEVELS["standard"])

    def list_levels(self) -> list[dict]:
        return [{"id": k, **v} for k, v in DIFFICULTY_LEVELS.items()]


# ═══════════════════════════════════════════════════════════════════════════════
# SPACED REPETITION (FSRS-inspired)
# From charisma-training-game's spacedRepetition.js
# Determines WHEN to re-surface specific skills/scenarios.
# ═══════════════════════════════════════════════════════════════════════════════

SKILL_CATEGORIES = {
    "active_listening": {
        "name": "Active Listening",
        "description": "Reflecting back, asking follow-ups, showing you heard",
    },
    "vulnerability": {
        "name": "Vulnerability",
        "description": "Sharing honestly, admitting uncertainty, being real",
    },
    "boundary_setting": {
        "name": "Boundary Setting",
        "description": "Saying no, holding limits, self-respect without aggression",
    },
    "empathic_response": {
        "name": "Empathic Response",
        "description": "Validating emotions, meeting people where they are",
    },
    "de_escalation": {
        "name": "De-escalation",
        "description": "Reducing tension without surrendering position",
    },
    "framing": {
        "name": "Framing & Reframing",
        "description": "Controlling interpretation of events and information",
    },
    "extraction": {
        "name": "Information Extraction",
        "description": "Getting information without triggering defenses",
    },
    "influence": {
        "name": "Influence & Compliance",
        "description": "Getting someone to agree through psychological technique",
    },
}


@dataclass
class SRSCard:
    skill_id: str
    stability: float = 1.0      # days until 90% recall probability
    difficulty: float = 0.5     # 0-1, how hard this skill is for this player
    last_review: float = 0.0    # unix timestamp
    review_count: int = 0
    quality_history: list = None

    def __post_init__(self):
        self.quality_history = self.quality_history or []

    @property
    def days_since_review(self) -> float:
        if self.last_review == 0:
            return 999
        return (time.time() - self.last_review) / 86400

    @property
    def recall_probability(self) -> float:
        """Estimated probability of recall right now."""
        if self.last_review == 0:
            return 0.0
        t = self.days_since_review
        return round(math.exp(-t / max(self.stability, 0.1)), 3)

    @property
    def is_due(self) -> bool:
        return self.recall_probability < 0.9

    def to_dict(self) -> dict:
        return {
            "skill_id": self.skill_id,
            "skill_name": SKILL_CATEGORIES.get(self.skill_id, {}).get("name", self.skill_id),
            "stability_days": round(self.stability, 1),
            "difficulty": round(self.difficulty, 2),
            "recall_probability": self.recall_probability,
            "is_due": self.is_due,
            "days_since_review": round(self.days_since_review, 1),
            "review_count": self.review_count,
        }


class SpacedRepetition:
    """FSRS-inspired spaced repetition for social skills."""

    def __init__(self, store_path: Optional[str] = None):
        self.path = Path(store_path) if store_path else Path.home() / ".persuasion-max" / "srs_cards.json"
        self.cards: dict[str, SRSCard] = {}
        self._load()

    def _load(self):
        if self.path.exists():
            raw = json.loads(self.path.read_text())
            for k, v in raw.items():
                self.cards[k] = SRSCard(**v)

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        raw = {}
        for k, card in self.cards.items():
            raw[k] = {
                "skill_id": card.skill_id,
                "stability": card.stability,
                "difficulty": card.difficulty,
                "last_review": card.last_review,
                "review_count": card.review_count,
                "quality_history": card.quality_history[-20:],  # keep last 20
            }
        self.path.write_text(json.dumps(raw, indent=2))

    def update_card(self, skill_id: str, quality: int) -> dict:
        """Update a skill card after practice.

        quality: 1 (fail) to 5 (perfect)
        """
        quality = max(1, min(5, quality))

        if skill_id not in self.cards:
            self.cards[skill_id] = SRSCard(skill_id=skill_id)

        card = self.cards[skill_id]
        card.review_count += 1
        card.last_review = time.time()
        card.quality_history.append(quality)

        # FSRS-inspired update
        if quality >= 4:
            # Good review — increase stability
            card.stability *= 1.5 + 0.5 * (quality - 3)
            card.difficulty = max(0.1, card.difficulty - 0.05)
        elif quality == 3:
            # Okay — small stability increase
            card.stability *= 1.2
        elif quality == 2:
            # Poor — reduce stability
            card.stability *= 0.7
            card.difficulty = min(1.0, card.difficulty + 0.1)
        else:
            # Fail — reset stability
            card.stability = max(0.5, card.stability * 0.3)
            card.difficulty = min(1.0, card.difficulty + 0.2)

        card.stability = round(min(365, card.stability), 2)  # cap at 1 year
        self._save()
        return card.to_dict()

    def get_due_cards(self) -> list[dict]:
        """Get all skills due for review, sorted by urgency."""
        # Include skills never reviewed
        all_skills = set(SKILL_CATEGORIES.keys())
        for skill_id in all_skills:
            if skill_id not in self.cards:
                self.cards[skill_id] = SRSCard(skill_id=skill_id)

        due = [card for card in self.cards.values() if card.is_due]
        due.sort(key=lambda c: c.recall_probability)
        return [c.to_dict() for c in due]

    def get_all_cards(self) -> list[dict]:
        """Get all skill cards with their current state."""
        return [c.to_dict() for c in self.cards.values()]
