from __future__ import annotations

"""
Response Scorer — Unified scoring engine for training games
=============================================================
Scores player responses against NPC psychology profiles.
Evaluates combo sequences for synergy multipliers.

Unified from:
    - read-the-room: 5-axis skill scoring + 4-axis extraction scoring + combo synergies
    - charisma-training-game: emotional risk calculator + near-miss detection
    - Persuade-Me: NLP technique identification in free-text responses
"""

import re
from dataclasses import dataclass, asdict
from typing import Optional

from training.techniques import MASTER_TECHNIQUES


# ─── Skill Axes ─────────────────────────────────────────────────────────────
# Unified from read-the-room (charm/framing/leverage/empathy/timing)
# + extraction skills (stealth/extraction/rapport/reading)

SKILL_AXES = {
    # Interpersonal (from read-the-room core)
    "charm": {"name": "Charm", "description": "Warmth, likeability, emotional resonance"},
    "framing": {"name": "Framing", "description": "Controlling how information is interpreted"},
    "leverage": {"name": "Leverage", "description": "Creating and using advantageous positions"},
    "empathy": {"name": "Empathy", "description": "Understanding and validating emotional states"},
    "timing": {"name": "Timing", "description": "When to speak, when to wait, when to act"},
    # Extraction (from read-the-room advanced scenarios)
    "stealth": {"name": "Stealth", "description": "Getting information without triggering defenses"},
    "extraction": {"name": "Extraction", "description": "Drawing out specific information"},
    "rapport": {"name": "Rapport", "description": "Building trust and connection quickly"},
    "reading": {"name": "Reading", "description": "Detecting hidden emotions, needs, and motives"},
}


# ─── Combo Synergies ────────────────────────────────────────────────────────
# From read-the-room's SYNERGIES system — technique sequence multipliers

COMBO_SYNERGIES = {
    # 3-move combos (tag sequences)
    "warm→vulnerable→bold": {"mult": 1.4, "why": "Disarm, expose, strike."},
    "warm→vulnerable→warm": {"mult": 1.3, "why": "Consistent warmth. They feel held."},
    "sharp→calculated→sharp": {"mult": 1.25, "why": "Relentless precision."},
    "warm→calculated→bold": {"mult": 1.35, "why": "Open warm, pivot strategy, close conviction."},
    "vulnerable→vulnerable→warm": {"mult": 1.3, "why": "Layer vulnerability then resolve."},
    "vulnerable→warm→bold": {"mult": 1.35, "why": "Vulnerability→sympathy→converts."},
    "bold→vulnerable→warm": {"mult": 1.35, "why": "Courage, wound, care."},
    "warm→warm→warm": {"mult": 1.15, "why": "Pure charm. Safe."},
    # Negative combos
    "vulnerable→sharp→warm": {"mult": 0.7, "why": "Vulnerable then sharp? Feels manipulative."},
    "warm→sharp→vulnerable": {"mult": 0.65, "why": "Sharp middle broke trust."},
    "weak→weak→weak": {"mult": 0.4, "why": "No spine."},
    "trap→warm→bold": {"mult": 0.6, "why": "Opener failed. Tainted."},
    "warm→trap→warm": {"mult": 0.55, "why": "Middle overplayed."},
    "warm→warm→trap": {"mult": 0.65, "why": "Fumbled the landing."},
    # Advanced extraction combos (from read-the-room intel scenarios)
    "rapport→provocative→scharff": {"mult": 1.45, "why": "Textbook HUMINT."},
    "rapport→quidproquo→scharff": {"mult": 1.4, "why": "Give to get to extract."},
    "flattery→provocative→bracket": {"mult": 1.35, "why": "Ego→correct→narrow."},
    "naive→flattery→scharff": {"mult": 1.4, "why": "Dumb→expert→extract."},
    "naive→quidproquo→bracket": {"mult": 1.35, "why": "Each step natural."},
    "direct→direct→direct": {"mult": 0.4, "why": "Interrogation. Defense walls go up."},
}


# ─── Tone Detection ─────────────────────────────────────────────────────────
# From charisma-training-game's emotional risk calculator

TONE_SIGNALS = {
    "warm": re.compile(r"(?i)\b(hey|love|miss|care|glad|happy|together|us|we|safe|sorry|thank)\b"),
    "vulnerable": re.compile(r"(?i)\b(scared|afraid|honest|admit|feel|struggle|hard|hurt|need|help)\b"),
    "bold": re.compile(r"(?i)\b(now|tonight|let's|come|right now|done|enough|decision|choose)\b"),
    "sharp": re.compile(r"(?i)\b(know|notice|see through|interesting|curious|pattern|really)\b"),
    "calculated": re.compile(r"(?i)\b(because|between us|imagine|consider|what if|hypothetically)\b"),
    "weak": re.compile(r"(?i)\b(maybe|idk|i guess|whatever|sure|fine|okay|probably|idc)\b"),
    "trap": re.compile(r"(?i)\b(anything|everything|always|never|promise|swear|literally dying|worst)\b"),
}

TONE_RISK = {
    "warm": 0.3, "vulnerable": 0.8, "bold": 0.6, "sharp": 0.5,
    "calculated": 0.5, "weak": 0.1, "trap": 0.7,
}


@dataclass
class ScoreResult:
    skills: dict[str, int]
    combo_multiplier: float
    combo_analysis: str
    tone_detected: str
    risk_level: float
    reward_potential: float
    near_miss: bool
    near_miss_message: Optional[str]
    techniques_detected: list[str]
    total_score: int

    def to_dict(self) -> dict:
        return asdict(self)


class ResponseScorer:
    """Score player responses across all training games."""

    def detect_tone(self, text: str) -> str:
        """Detect the dominant emotional tone of a response."""
        scores = {}
        for tone, pattern in TONE_SIGNALS.items():
            scores[tone] = len(pattern.findall(text))
        if not any(scores.values()):
            return "neutral"
        return max(scores, key=scores.get)

    def detect_techniques(self, text: str) -> list[str]:
        """Detect which persuasion techniques are present in free text."""
        detected = []
        text_lower = text.lower()

        # Simple heuristic detection — maps text patterns to techniques
        technique_signals = {
            "labeling": r"(?i)(you (seem|feel|sound|look) |i can (see|tell|sense) you)",
            "mirroring": None,  # requires conversation context, not single-response
            "calibrated_questions": r"(?i)^(how|what) (do|would|could|can|should|did)",
            "vulnerability_display": r"(?i)(i('m| am) (scared|afraid|honest)|can i be (real|honest))",
            "tactical_agreement": r"(?i)(you're right|i agree|that's fair|you have a point)",
            "presupposition": r"(?i)(when (you|we)|after (you|we)|which (one|option))",
            "social_proof": r"(?i)(everyone|people|others|they all|most people)",
            "scarcity_takeaway": r"(?i)(nevermind|forget it|don't worry|it's fine|nvm)",
            "flattery": r"(?i)(you're (so|really|genuinely|the) |amazing|brilliant|impressive|best)",
            "urgency_framing": r"(?i)(right now|tonight|today|before it's|last chance|now or)",
        }

        for tech_id, pattern in technique_signals.items():
            if pattern and re.search(pattern, text):
                detected.append(tech_id)

        return detected

    def score(
        self,
        response_text: str,
        npc_id: str,
        difficulty: str = "standard",
    ) -> dict:
        """Score a player response."""
        tone = self.detect_tone(response_text)
        techniques_used = self.detect_techniques(response_text)
        risk = TONE_RISK.get(tone, 0.3)

        # Higher risk = higher reward potential (vulnerability pays off)
        reward = min(1.0, risk * 1.5)

        # Base skill scores from tone
        skills = {axis: 0 for axis in SKILL_AXES}
        tone_skill_map = {
            "warm": {"charm": 3, "empathy": 2, "rapport": 2},
            "vulnerable": {"empathy": 3, "charm": 2, "reading": 1},
            "bold": {"leverage": 3, "timing": 2, "framing": 1},
            "sharp": {"framing": 3, "reading": 2, "stealth": 1},
            "calculated": {"framing": 2, "leverage": 2, "stealth": 2, "extraction": 1},
            "weak": {"charm": -1, "timing": -1},
            "trap": {"charm": -1, "empathy": -1},
        }
        for skill, points in tone_skill_map.get(tone, {}).items():
            skills[skill] = points

        # Bonus points for detected techniques
        for tech_id in techniques_used:
            tech = MASTER_TECHNIQUES.get(tech_id)
            if tech:
                if tech.category == "rapport":
                    skills["rapport"] = skills.get("rapport", 0) + 2
                elif tech.category == "extraction":
                    skills["extraction"] = skills.get("extraction", 0) + 2
                elif tech.category == "compliance":
                    skills["leverage"] = skills.get("leverage", 0) + 2
                elif tech.category == "framing":
                    skills["framing"] = skills.get("framing", 0) + 2

        # Difficulty modifier
        diff_mods = {"guided": 1.5, "standard": 1.0, "authentic": 0.8, "intense": 0.6}
        modifier = diff_mods.get(difficulty, 1.0)
        skills = {k: max(0, round(v * modifier)) for k, v in skills.items()}

        total = sum(v for v in skills.values() if v > 0)

        # Near-miss detection (from charisma-training-game)
        near_miss = 10 <= total <= 14
        near_miss_msg = "You're close. One more exchange like that..." if near_miss else None

        return ScoreResult(
            skills=skills,
            combo_multiplier=1.0,
            combo_analysis="Single response — combo requires 3+ moves",
            tone_detected=tone,
            risk_level=round(risk, 2),
            reward_potential=round(reward, 2),
            near_miss=near_miss,
            near_miss_message=near_miss_msg,
            techniques_detected=techniques_used,
            total_score=total,
        ).to_dict()

    def evaluate_combo(self, tags: list[str]) -> dict:
        """Evaluate a sequence of tone/technique tags for synergy."""
        if len(tags) < 2:
            return {"multiplier": 1.0, "analysis": "Need 2+ moves for combo."}

        # Check 3-move combos
        if len(tags) >= 3:
            for i in range(len(tags) - 2):
                key = f"{tags[i]}→{tags[i+1]}→{tags[i+2]}"
                if key in COMBO_SYNERGIES:
                    syn = COMBO_SYNERGIES[key]
                    return {
                        "multiplier": syn["mult"],
                        "combo_key": key,
                        "analysis": syn["why"],
                        "is_positive": syn["mult"] > 1.0,
                    }

        # Check for patterns
        unique = len(set(tags))
        has_trap = "trap" in tags
        has_weak = "weak" in tags
        trap_count = tags.count("trap")
        weak_count = tags.count("weak")

        if trap_count >= 2:
            return {"multiplier": 0.4, "analysis": "Multiple overplays. Feels fake."}
        if weak_count >= 2:
            return {"multiplier": 0.5, "analysis": "Too weak. No spine."}
        if has_trap:
            return {"multiplier": 0.65, "analysis": "One misstep. Something felt off."}
        if unique == 1 and tags[0] not in ("weak", "trap"):
            return {"multiplier": 1.15, "analysis": "Consistent. Trustworthy."}
        if unique == len(tags) and not has_trap and not has_weak:
            return {"multiplier": 1.25, "analysis": "Varied approach. Engaging."}

        return {"multiplier": 1.0, "analysis": "Solid. Unremarkable."}
