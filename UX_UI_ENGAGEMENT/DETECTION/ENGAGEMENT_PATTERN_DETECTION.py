"""
ENGAGEMENT PATTERN DETECTION SYSTEM
====================================
Comprehensive detection framework for 12 UX/UI engagement patterns (P1-P12).

Detects behavioral influence techniques in digital interfaces including:
- Variable Reward Scheduling (P1)
- Progress Momentum (P2)
- Encouraging Feedback (P3)
- Progress Protection (P4)
- Investment Recognition (P5)
- Timely Opportunities (P6)
- Contextual Offers (P7)
- Immersive Experience (P8)
- Personalized Experience Tiers (P9)
- Community Activity Display (P10)
- Community Connection (P11)
- Identity & Achievement (P12)

Usage:
    auditor = EngagementPatternAuditor()
    result = auditor.audit(ui_config, text_content)
    print(result)

Author: Persuasion Max Project
Version: 1.0.0
"""

import re
import json
import hashlib
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, asdict, field
from datetime import datetime
from enum import Enum


# =============================================================================
# SECTION 1: CONSTANTS AND ENUMERATIONS
# =============================================================================

class IntensityLevel(Enum):
    """Standard intensity classification levels."""
    NONE = "NONE"
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    EXTREME = "EXTREME"


class PatternCategory(Enum):
    """The 12 engagement pattern categories."""
    P1_VARIABLE_REWARD = "VARIABLE_REWARD_SCHEDULING"
    P2_PROGRESS_MOMENTUM = "PROGRESS_MOMENTUM"
    P3_ENCOURAGING_FEEDBACK = "ENCOURAGING_FEEDBACK"
    P4_PROGRESS_PROTECTION = "PROGRESS_PROTECTION"
    P5_INVESTMENT_RECOGNITION = "INVESTMENT_RECOGNITION"
    P6_TIMELY_OPPORTUNITIES = "TIMELY_OPPORTUNITIES"
    P7_CONTEXTUAL_OFFERS = "CONTEXTUAL_OFFERS"
    P8_IMMERSIVE_EXPERIENCE = "IMMERSIVE_EXPERIENCE"
    P9_PERSONALIZED_TIERS = "PERSONALIZED_EXPERIENCE_TIERS"
    P10_COMMUNITY_ACTIVITY = "COMMUNITY_ACTIVITY_DISPLAY"
    P11_COMMUNITY_CONNECTION = "COMMUNITY_CONNECTION"
    P12_IDENTITY_ACHIEVEMENT = "IDENTITY_ACHIEVEMENT"


# =============================================================================
# SECTION 2: KEYWORD AND PHRASE DETECTION LISTS
# =============================================================================

class EngagementPatterns:
    """All keyword lists and regex patterns for engagement pattern detection."""

    # -------------------------------------------------------------------------
    # P1: Variable Reward Scheduling
    # -------------------------------------------------------------------------
    SURPRISE_MESSAGING = [
        "surprise", "mystery", "discover", "reveal", "unlock", "unbox",
        "what will you get", "find out", "see what's inside", "random",
        "chance", "lucky", "fortune", "fate", "destiny"
    ]

    ODDS_TRANSPARENCY = [
        "odds", "probability", "chance", "likelihood", "rate", "percentage",
        "drop rate", "pull rate", "pity rate", "guaranteed"
    ]

    RARITY_LANGUAGE = [
        "legendary", "epic", "rare", "uncommon", "common", "mythic",
        "ultra rare", "super rare", "SSR", "SR", "UR", "limited edition",
        "exclusive", "premium", "elite", "godly", "divine"
    ]

    # -------------------------------------------------------------------------
    # P2: Progress Momentum (Near-Miss)
    # -------------------------------------------------------------------------
    NEAR_MISS_MESSAGING = [
        "almost", "so close", "nearly", "just missed", "one away",
        "almost there", "close call", "narrow miss", "just short",
        "inches away", "hair's breadth", "on the verge", "nearly won"
    ]

    PROGRESS_ENCOURAGEMENT = [
        "keep going", "don't give up", "you're getting closer",
        "progress saved", "momentum building", "on a roll",
        "hot streak", "winning streak", "keep the streak"
    ]

    # -------------------------------------------------------------------------
    # P3: Encouraging Feedback (Sub-Wager Celebration)
    # -------------------------------------------------------------------------
    CELEBRATION_TRIGGERS = [
        "congratulations", "winner", "you won", "victory", "success",
        "amazing", "incredible", "fantastic", "awesome", "great job",
        "well done", "nice", "bonus", "reward", "prize"
    ]

    PARTIAL_WIN_FRAMING = [
        "you got", "earned", "collected", "received", "claimed",
        "added to", "credited", "bonus points", "free spin"
    ]

    # -------------------------------------------------------------------------
    # P4: Progress Protection (Loss Aversion)
    # -------------------------------------------------------------------------
    LOSS_FOCUSED_LANGUAGE = [
        "lose", "losing", "will lose", "about to lose", "risk losing",
        "forfeit", "expire", "gone forever", "miss out", "slip away",
        "vanish", "disappear", "reset", "start over"
    ]

    PROTECTION_OFFERS = [
        "protect", "save", "preserve", "keep", "maintain", "secure",
        "safeguard", "insurance", "shield", "guard", "freeze",
        "pause", "extend", "continue"
    ]

    STREAK_LANGUAGE = [
        "streak", "consecutive", "in a row", "daily", "chain",
        "combo", "multiplier", "bonus streak", "perfect attendance"
    ]

    URGENCY_PROTECTION = [
        "expires", "limited time", "don't miss", "hurry", "act now",
        "before it's too late", "last chance", "running out",
        "time sensitive", "urgent"
    ]

    # -------------------------------------------------------------------------
    # P5: Investment Recognition (Sunk Cost)
    # -------------------------------------------------------------------------
    INVESTMENT_SUMMARY = [
        "you've invested", "your progress", "your journey", "time spent",
        "hours played", "days active", "achievements earned",
        "milestones reached", "your collection", "your history"
    ]

    BENEFIT_ENUMERATION = [
        "you'll lose access to", "benefits include", "you currently have",
        "your membership includes", "features you use", "saved preferences",
        "personalized", "your data", "your content"
    ]

    SAVINGS_LANGUAGE = [
        "you've saved", "total savings", "lifetime value", "earned rewards",
        "accumulated", "banked", "stored value", "credit balance"
    ]

    # -------------------------------------------------------------------------
    # P6: Timely Opportunities (Scarcity)
    # -------------------------------------------------------------------------
    SCARCITY_CLAIMS = [
        "only", "left", "remaining", "limited", "few left", "selling fast",
        "almost gone", "low stock", "high demand", "popular item",
        "trending", "hot", "going fast"
    ]

    ACTIVITY_INDICATORS = [
        "people looking", "people viewing", "in carts", "watching",
        "interested", "bought today", "sold today", "booked today",
        "reserved", "claimed"
    ]

    PRICE_URGENCY = [
        "price increase", "prices rising", "will increase", "going up",
        "was", "now", "sale ends", "offer expires", "deal ends"
    ]

    # -------------------------------------------------------------------------
    # P7: Contextual Offers (Emotional Timing)
    # -------------------------------------------------------------------------
    FAILURE_RECOVERY = [
        "try again", "one more chance", "don't give up", "keep trying",
        "special offer", "bonus attempt", "extra life", "continue",
        "resurrection", "revive", "second chance"
    ]

    EMOTIONAL_STATE_MESSAGING = [
        "frustrated", "stuck", "struggling", "having trouble",
        "need help", "boost", "power up", "advantage", "edge"
    ]

    NEAR_MISS_PURCHASE = [
        "so close", "almost had it", "just need", "one more",
        "unlock now", "get it now", "instant access"
    ]

    # -------------------------------------------------------------------------
    # P8: Immersive Experience (Flow State)
    # -------------------------------------------------------------------------
    AUTOPLAY_LANGUAGE = [
        "autoplay", "auto-play", "next episode", "up next", "playing next",
        "continue watching", "keep watching", "binge", "marathon"
    ]

    INFINITE_SCROLL_INDICATORS = [
        "endless", "infinite", "never-ending", "more content",
        "load more", "keep scrolling", "discover more"
    ]

    TIME_OBSCURING = [
        "one more", "just one more", "quick", "brief", "short",
        "won't take long", "few minutes", "moment"
    ]

    # -------------------------------------------------------------------------
    # P9: Personalized Experience Tiers (Whale Targeting)
    # -------------------------------------------------------------------------
    PERSONALIZATION_LANGUAGE = [
        "just for you", "personalized", "special offer", "exclusive",
        "selected for you", "recommended for you", "based on your",
        "tailored", "customized", "your preferences"
    ]

    VIP_STATUS_LANGUAGE = [
        "VIP", "elite", "premium", "gold", "platinum", "diamond",
        "exclusive member", "top tier", "high roller", "whale",
        "valued customer", "loyal member", "special status"
    ]

    SPENDING_TIER_INDICATORS = [
        "unlock at", "spend to unlock", "purchase to access",
        "upgrade available", "premium features", "pro version",
        "starter pack", "bundle", "value pack"
    ]

    # -------------------------------------------------------------------------
    # P10: Community Activity Display (Social Proof)
    # -------------------------------------------------------------------------
    ACTIVITY_CLAIMS = [
        "people", "users", "customers", "members", "players",
        "viewers", "visitors", "shoppers", "buyers"
    ]

    ACTIVITY_VERBS = [
        "viewing", "watching", "looking at", "bought", "purchased",
        "booked", "reserved", "joined", "signed up", "playing"
    ]

    RECENCY_INDICATORS = [
        "right now", "currently", "at this moment", "live",
        "in real-time", "just now", "recently", "today"
    ]

    # -------------------------------------------------------------------------
    # P11: Community Connection (Social Obligation)
    # -------------------------------------------------------------------------
    SOCIAL_OBLIGATION = [
        "your team needs you", "friends are waiting", "don't let down",
        "counting on you", "they need your help", "join your friends",
        "your clan", "your guild", "your alliance"
    ]

    INACTIVITY_MESSAGING = [
        "we miss you", "come back", "your friends miss you",
        "you've been away", "return bonus", "welcome back",
        "inactive", "haven't seen you"
    ]

    RECIPROCITY_TRIGGERS = [
        "sent you", "gifted you", "shared with you", "invited you",
        "wants to help", "helped you", "gave you", "return the favor"
    ]

    GROUP_VISIBILITY = [
        "leaderboard", "ranking", "contribution", "activity score",
        "participation", "team stats", "group progress"
    ]

    # -------------------------------------------------------------------------
    # P12: Identity & Achievement (Identity Lock-In)
    # -------------------------------------------------------------------------
    IDENTITY_LABELS = [
        "you are a", "you're a", "as a", "being a", "true",
        "real", "dedicated", "devoted", "loyal", "committed"
    ]

    PROGRESSION_TITLES = [
        "beginner", "novice", "apprentice", "journeyman", "expert",
        "master", "grandmaster", "legend", "champion", "elite",
        "curious", "practitioner", "dedicated", "devoted"
    ]

    ACHIEVEMENT_LANGUAGE = [
        "achievement", "badge", "trophy", "medal", "award",
        "milestone", "level up", "rank up", "unlocked", "earned",
        "completed", "mastered", "conquered"
    ]

    PUBLIC_PROFILE = [
        "share", "show off", "display", "profile", "public",
        "visible to", "others can see", "showcase", "flaunt"
    ]

    MAINTENANCE_REQUIREMENTS = [
        "maintain", "keep active", "stay engaged", "continue to",
        "requires", "daily login", "weekly", "monthly", "decay",
        "expires if", "lose if inactive"
    ]


# =============================================================================
# SECTION 3: DATA CLASSES
# =============================================================================

@dataclass
class PatternDetectionResult:
    """Result from a single pattern detector."""
    pattern_id: str
    pattern_name: str
    score: float  # 0.0 to 1.0
    intensity: str
    text_indicators: List[str]
    ui_indicators: List[str]
    details: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format."""
        return asdict(self)


@dataclass
class UIConfigAnalysis:
    """Analysis of UI configuration elements."""
    element_type: str
    detected_patterns: List[str]
    values: Dict[str, Any]
    flags: List[str]


@dataclass
class EngagementAuditReport:
    """Complete engagement pattern audit report."""
    audit_id: str
    timestamp: str
    content_hash: str
    patterns: Dict[str, PatternDetectionResult]
    composite_score: float
    intensity_classification: str
    high_intensity_patterns: List[str]
    recommendations: List[str]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format."""
        result = asdict(self)
        result["patterns"] = {k: v.to_dict() if hasattr(v, 'to_dict') else v
                             for k, v in self.patterns.items()}
        return result

    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), indent=2)


# =============================================================================
# SECTION 4: BASE DETECTOR CLASS
# =============================================================================

class BasePatternDetector:
    """Base class for all engagement pattern detectors."""

    PATTERN_ID: str = "P0"
    PATTERN_NAME: str = "Base Pattern"

    # Intensity thresholds (score ranges for classification)
    # Thresholds based on behavioral science research indicating:
    # - Below 0.2: Minimal/incidental pattern presence
    # - 0.2-0.4: Noticeable but not dominant
    # - 0.4-0.7: Significant presence affecting user behavior
    # - Above 0.7: Dominant pattern likely to strongly influence behavior
    INTENSITY_THRESHOLDS = {
        "NONE": 0.0,
        "LOW": 0.2,
        "MODERATE": 0.4,
        "HIGH": 0.7,
        "EXTREME": 0.85
    }

    def __init__(self):
        """Initialize the detector."""
        self.keywords: List[str] = []
        self.ui_checks: List[str] = []

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """
        Main detection method to be implemented by subclasses.

        Args:
            text_content: Text content to analyze for linguistic indicators
            ui_config: UI configuration dictionary for structural analysis

        Returns:
            PatternDetectionResult with score and details
        """
        raise NotImplementedError("Subclasses must implement detect()")

    def _classify_intensity(self, score: float) -> str:
        """
        Classify score into intensity level.

        Args:
            score: Detection score from 0.0 to 1.0

        Returns:
            Intensity level string
        """
        if score >= self.INTENSITY_THRESHOLDS["EXTREME"]:
            return "EXTREME"
        elif score >= self.INTENSITY_THRESHOLDS["HIGH"]:
            return "HIGH"
        elif score >= self.INTENSITY_THRESHOLDS["MODERATE"]:
            return "MODERATE"
        elif score >= self.INTENSITY_THRESHOLDS["LOW"]:
            return "LOW"
        return "NONE"

    def _count_keyword_matches(
        self,
        text: str,
        keywords: List[str]
    ) -> Tuple[int, List[str]]:
        """
        Count keyword matches in text.

        Args:
            text: Text to search
            keywords: List of keywords to find

        Returns:
            Tuple of (count, list of matched keywords)
        """
        text_lower = text.lower()
        matches = []
        for keyword in keywords:
            if keyword.lower() in text_lower:
                matches.append(keyword)
        return len(matches), matches

    def _check_ui_condition(
        self,
        ui_config: Dict[str, Any],
        path: str,
        condition: str,
        value: Any
    ) -> bool:
        """
        Check a UI configuration condition.

        Args:
            ui_config: UI configuration dictionary
            path: Dot-separated path to config value (e.g., "odds_disclosure.exists")
            condition: Comparison operator ("=", ">", "<", ">=", "<=", "!=")
            value: Value to compare against

        Returns:
            Boolean result of condition check
        """
        # Navigate to the value
        current = ui_config
        for key in path.split("."):
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return False

        # Perform comparison
        try:
            if condition == "=":
                return current == value
            elif condition == "!=":
                return current != value
            elif condition == ">":
                return float(current) > float(value)
            elif condition == "<":
                return float(current) < float(value)
            elif condition == ">=":
                return float(current) >= float(value)
            elif condition == "<=":
                return float(current) <= float(value)
        except (ValueError, TypeError):
            return False

        return False


# =============================================================================
# SECTION 5: PATTERN DETECTORS (P1-P12)
# =============================================================================

class P1VariableRewardDetector(BasePatternDetector):
    """
    P1: Variable Reward Scheduling Detection

    Detects patterns associated with variable ratio reinforcement schedules
    commonly used in gacha mechanics, loot boxes, and gambling-style interfaces.

    Key indicators:
    - Hidden or buried odds disclosure
    - Rarity tier systems with visual distinction
    - Extended anticipation animations
    - Surprise/mystery framing instead of probability language
    """

    PATTERN_ID = "P1"
    PATTERN_NAME = "Variable Reward Scheduling"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect variable reward scheduling patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Check for surprise/mystery framing (positive indicator)
        surprise_count, surprise_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.SURPRISE_MESSAGING
        )
        if surprise_matches:
            text_indicators.extend(surprise_matches)
            details["surprise_framing"] = surprise_matches
            # Score: 0.15 per match, max 0.3
            # Rationale: Surprise framing is moderate indicator; 2+ matches suggests intentional pattern
            score_components.append(min(surprise_count * 0.15, 0.3))

        # Check for odds transparency (negative indicator - reduces score)
        odds_count, odds_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.ODDS_TRANSPARENCY
        )
        if odds_matches:
            details["odds_transparency"] = odds_matches
            # Reduce score for transparency
            # Rationale: Transparent odds disclosure is ethical practice, reduces pattern intensity
            score_components.append(-min(odds_count * 0.1, 0.2))

        # Check for rarity language
        rarity_count, rarity_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.RARITY_LANGUAGE
        )
        if rarity_matches:
            text_indicators.extend(rarity_matches)
            details["rarity_tiers"] = rarity_matches
            # Score: 0.1 per match, max 0.25
            # Rationale: Rarity tiers alone are common; multiple tiers increase intensity
            score_components.append(min(rarity_count * 0.1, 0.25))

        # --- UI Configuration Analysis ---

        # Odds disclosure hidden or buried
        if self._check_ui_condition(ui_config, "odds_disclosure.exists", "=", False):
            ui_indicators.append("odds_disclosure_missing")
            score_components.append(0.25)
        elif self._check_ui_condition(ui_config, "odds_disclosure.location", "=", "settings"):
            ui_indicators.append("odds_disclosure_buried_in_settings")
            score_components.append(0.15)

        # Rarity tier count (3+ tiers is notable)
        if self._check_ui_condition(ui_config, "rarity_tier.count", ">=", 3):
            ui_indicators.append("multiple_rarity_tiers")
            tier_count = ui_config.get("rarity_tier", {}).get("count", 0)
            details["tier_count"] = tier_count
            # Score scales with tier count: 0.05 per tier above 2, max 0.2
            score_components.append(min((tier_count - 2) * 0.05, 0.2))

        # Animation duration > 3000ms (anticipation extension)
        if self._check_ui_condition(ui_config, "animation_duration", ">", 3000):
            ui_indicators.append("extended_anticipation_animation")
            duration = ui_config.get("animation_duration", 0)
            details["animation_duration_ms"] = duration
            score_components.append(0.15)

        # Skip button de-emphasized
        if self._check_ui_condition(ui_config, "skip_button.opacity", "<", 0.5):
            ui_indicators.append("skip_button_de_emphasized")
            score_components.append(0.1)

        # Audio intensity scaling with rarity
        if self._check_ui_condition(ui_config, "audio_amplitude_ratio", ">", 1.8):
            ui_indicators.append("audio_scales_with_rarity")
            score_components.append(0.1)

        # Haptic response correlation
        if self._check_ui_condition(ui_config, "haptic_correlation", ">", 0.73):
            ui_indicators.append("haptic_scales_with_outcome")
            score_components.append(0.1)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        details["score_breakdown"] = {
            "components": score_components,
            "raw_total": raw_score
        }

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P2ProgressMomentumDetector(BasePatternDetector):
    """
    P2: Progress Momentum Detection (Near-Miss Patterns)

    Detects patterns that create perceived closeness to success,
    encouraging continued engagement through near-miss experiences.

    Key indicators:
    - Near-miss messaging ("Almost!", "So close!")
    - Target symbol visibility on losses
    - Progress bar advancement on unsuccessful attempts
    - Audio similarity between wins and losses
    """

    PATTERN_ID = "P2"
    PATTERN_NAME = "Progress Momentum"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect progress momentum patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Near-miss messaging
        nearmiss_count, nearmiss_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.NEAR_MISS_MESSAGING
        )
        if nearmiss_matches:
            text_indicators.extend(nearmiss_matches)
            details["near_miss_language"] = nearmiss_matches
            # Score: 0.2 per match, max 0.4 (near-miss is strong indicator)
            score_components.append(min(nearmiss_count * 0.2, 0.4))

        # Progress encouragement
        progress_count, progress_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.PROGRESS_ENCOURAGEMENT
        )
        if progress_matches:
            text_indicators.extend(progress_matches)
            details["progress_encouragement"] = progress_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(progress_count * 0.1, 0.2))

        # --- UI Configuration Analysis ---

        # Target symbol visible on loss
        if self._check_ui_condition(ui_config, "target_symbol.visible_on_loss", "=", True):
            ui_indicators.append("target_visible_on_loss")
            score_components.append(0.15)

        # Progress bar fills forward on loss
        if self._check_ui_condition(ui_config, "progress_bar.fill_on_loss", "=", True):
            ui_indicators.append("progress_fills_on_loss")
            score_components.append(0.15)

        # Reel deceleration > 200ms
        if self._check_ui_condition(ui_config, "reel_deceleration_ms", ">", 200):
            ui_indicators.append("extended_reel_deceleration")
            score_components.append(0.1)

        # Audio similarity between win/loss > 0.85
        if self._check_ui_condition(ui_config, "win_loss_audio_similarity", ">", 0.85):
            ui_indicators.append("similar_win_loss_audio")
            score_components.append(0.15)

        # Near-success frequency above random expectation
        if self._check_ui_condition(ui_config, "near_success_frequency_deviation", ">", 0.05):
            ui_indicators.append("elevated_near_miss_frequency")
            deviation = ui_config.get("near_success_frequency_deviation", 0)
            details["near_miss_frequency_above_random"] = deviation
            score_components.append(0.2)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P3EncouragingFeedbackDetector(BasePatternDetector):
    """
    P3: Encouraging Feedback Detection (Sub-Wager Celebration)

    Detects patterns where positive feedback is given for outcomes
    that are actually net losses, creating perception of winning.

    Key indicators:
    - Celebration triggers for partial returns
    - Amount display without wager context
    - Normalized sensory intensity across outcome values
    - Celebration timing before outcome display
    """

    PATTERN_ID = "P3"
    PATTERN_NAME = "Encouraging Feedback"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect encouraging feedback patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Celebration language
        celebration_count, celebration_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.CELEBRATION_TRIGGERS
        )
        if celebration_matches:
            text_indicators.extend(celebration_matches)
            details["celebration_language"] = celebration_matches
            # Score: 0.1 per match, max 0.25
            score_components.append(min(celebration_count * 0.1, 0.25))

        # Partial win framing
        partial_count, partial_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.PARTIAL_WIN_FRAMING
        )
        if partial_matches:
            text_indicators.extend(partial_matches)
            details["partial_win_framing"] = partial_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(partial_count * 0.1, 0.2))

        # Check for "+$X" pattern without context
        amount_pattern = re.compile(r'\+\s*\$?\d+(?:\.\d{2})?')
        amount_matches = amount_pattern.findall(text_content)
        context_pattern = re.compile(r'(wager|bet|total|net|spent)', re.IGNORECASE)
        has_context = bool(context_pattern.search(text_content))

        if amount_matches and not has_context:
            text_indicators.append("amount_without_context")
            details["isolated_amounts"] = amount_matches
            score_components.append(0.2)

        # --- UI Configuration Analysis ---

        # Celebration triggered for sub-wager outcomes
        if self._check_ui_condition(ui_config, "celebration.triggers_below_wager", "=", True):
            ui_indicators.append("celebrates_partial_returns")
            score_components.append(0.25)

        # Net outcome display hidden or delayed
        if self._check_ui_condition(ui_config, "net_outcome_display.visible", "=", False):
            ui_indicators.append("net_outcome_hidden")
            score_components.append(0.15)

        # Sensory intensity normalized (small wins = large wins)
        if self._check_ui_condition(ui_config, "audio_intensity_normalized", "=", True):
            ui_indicators.append("audio_intensity_normalized")
            score_components.append(0.1)

        # Celebration starts before outcome display
        if self._check_ui_condition(ui_config, "celebration_before_outcome", "=", True):
            ui_indicators.append("premature_celebration")
            score_components.append(0.15)

        # High celebration frequency (> 60% of outcomes)
        if self._check_ui_condition(ui_config, "celebration_frequency", ">", 0.6):
            ui_indicators.append("high_celebration_frequency")
            freq = ui_config.get("celebration_frequency", 0)
            details["celebration_frequency"] = freq
            score_components.append(0.15)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P4ProgressProtectionDetector(BasePatternDetector):
    """
    P4: Progress Protection Detection (Loss Aversion)

    Detects patterns leveraging loss aversion to encourage purchases
    that protect accumulated progress or streaks.

    Key indicators:
    - Prominent streak counters
    - Loss-focused messaging (losing > keeping)
    - Urgency language around protection offers
    - Price scaling with streak length
    """

    PATTERN_ID = "P4"
    PATTERN_NAME = "Progress Protection"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect progress protection patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Loss-focused language
        loss_count, loss_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.LOSS_FOCUSED_LANGUAGE
        )

        # Protection offer language
        protect_count, protect_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.PROTECTION_OFFERS
        )

        # Calculate loss/gain ratio
        if loss_matches:
            text_indicators.extend(loss_matches)
            details["loss_language"] = loss_matches
        if protect_matches:
            text_indicators.extend(protect_matches)
            details["protection_language"] = protect_matches

        # Loss framing ratio (loss terms / protection terms)
        if protect_count > 0:
            loss_ratio = loss_count / max(protect_count, 1)
            details["loss_to_protection_ratio"] = round(loss_ratio, 2)
            if loss_ratio > 2:
                # Score: 0.25 for strong loss framing
                score_components.append(0.25)
            elif loss_ratio > 1:
                score_components.append(0.15)

        # Streak language
        streak_count, streak_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.STREAK_LANGUAGE
        )
        if streak_matches:
            text_indicators.extend(streak_matches)
            details["streak_language"] = streak_matches
            # Score: 0.15 per match, max 0.25
            score_components.append(min(streak_count * 0.15, 0.25))

        # Urgency language
        urgency_count, urgency_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.URGENCY_PROTECTION
        )
        if urgency_matches:
            text_indicators.extend(urgency_matches)
            details["urgency_language"] = urgency_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(urgency_count * 0.1, 0.2))

        # --- UI Configuration Analysis ---

        # Streak counter prominence
        if self._check_ui_condition(ui_config, "streak_display.opacity", ">", 0.9):
            ui_indicators.append("prominent_streak_display")
            score_components.append(0.1)

        if self._check_ui_condition(ui_config, "streak_display.font_size_ratio", ">", 1.0):
            ui_indicators.append("large_streak_font")
            score_components.append(0.1)

        # Protection price scales with streak
        if self._check_ui_condition(ui_config, "protection_price.streak_correlation", ">", 0.85):
            ui_indicators.append("price_scales_with_streak")
            score_components.append(0.2)

        # Multi-step cancellation (friction)
        if self._check_ui_condition(ui_config, "cancellation_flow.step_count", ">", 2):
            ui_indicators.append("multi_step_cancellation")
            steps = ui_config.get("cancellation_flow", {}).get("step_count", 0)
            details["cancellation_steps"] = steps
            score_components.append(0.15)

        # Non-dismissible countdown
        if self._check_ui_condition(ui_config, "countdown.dismissible", "=", False):
            ui_indicators.append("non_dismissible_countdown")
            score_components.append(0.1)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P5InvestmentRecognitionDetector(BasePatternDetector):
    """
    P5: Investment Recognition Detection (Sunk Cost)

    Detects patterns that highlight user's accumulated investment
    to increase switching costs and reduce churn.

    Key indicators:
    - Multi-step cancellation flows
    - Investment summary displays during exit
    - Benefit enumeration in cancellation context
    - Progress decay mechanics
    """

    PATTERN_ID = "P5"
    PATTERN_NAME = "Investment Recognition"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect investment recognition patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Investment summary language
        investment_count, investment_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.INVESTMENT_SUMMARY
        )
        if investment_matches:
            text_indicators.extend(investment_matches)
            details["investment_language"] = investment_matches
            # Score: 0.15 per match, max 0.3
            score_components.append(min(investment_count * 0.15, 0.3))

        # Benefit enumeration
        benefit_count, benefit_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.BENEFIT_ENUMERATION
        )
        if benefit_matches:
            text_indicators.extend(benefit_matches)
            details["benefit_enumeration"] = benefit_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(benefit_count * 0.1, 0.2))

        # Savings/value language
        savings_count, savings_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.SAVINGS_LANGUAGE
        )
        if savings_matches:
            text_indicators.extend(savings_matches)
            details["savings_language"] = savings_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(savings_count * 0.1, 0.2))

        # --- UI Configuration Analysis ---

        # Multi-step cancellation
        if self._check_ui_condition(ui_config, "cancellation_flow.step_count", ">", 2):
            ui_indicators.append("multi_step_cancellation")
            steps = ui_config.get("cancellation_flow", {}).get("step_count", 0)
            details["cancellation_steps"] = steps
            # More steps = higher score (max at 5+ steps)
            # Rationale: Each additional step adds friction; 5+ steps is excessive
            score_components.append(min((steps - 2) * 0.1, 0.3))

        # Investment summary shown at cancellation
        if self._check_ui_condition(ui_config, "investment_summary.shown_at_cancellation", "=", True):
            ui_indicators.append("investment_summary_at_cancellation")
            score_components.append(0.2)

        # Benefit count >= 3 in exit flow
        if self._check_ui_condition(ui_config, "exit_flow.benefit_count", ">=", 3):
            ui_indicators.append("extensive_benefit_list")
            count = ui_config.get("exit_flow", {}).get("benefit_count", 0)
            details["benefits_shown"] = count
            score_components.append(0.15)

        # Pause option before cancel (softer alternative)
        if self._check_ui_condition(ui_config, "pause_before_cancel", "=", True):
            ui_indicators.append("pause_option_prominent")
            score_components.append(0.1)

        # Progress decay mechanic
        if self._check_ui_condition(ui_config, "progress_decay.rate_per_day", ">=", 0.005):
            ui_indicators.append("progress_decay_active")
            rate = ui_config.get("progress_decay", {}).get("rate_per_day", 0)
            details["decay_rate_per_day"] = rate
            score_components.append(0.15)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P6TimelyOpportunitiesDetector(BasePatternDetector):
    """
    P6: Timely Opportunities Detection (Scarcity Claims)

    Detects patterns using unverifiable scarcity and urgency
    to accelerate purchase decisions.

    Key indicators:
    - Unverifiable inventory claims
    - Specific (non-round) activity numbers
    - Activity counts without timeframes
    - Countdown resets after expiry
    """

    PATTERN_ID = "P6"
    PATTERN_NAME = "Timely Opportunities"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect timely opportunities patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Scarcity claims
        scarcity_count, scarcity_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.SCARCITY_CLAIMS
        )
        if scarcity_matches:
            text_indicators.extend(scarcity_matches)
            details["scarcity_language"] = scarcity_matches
            # Score: 0.15 per match, max 0.3
            score_components.append(min(scarcity_count * 0.15, 0.3))

        # Activity indicators
        activity_count, activity_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.ACTIVITY_INDICATORS
        )
        if activity_matches:
            text_indicators.extend(activity_matches)
            details["activity_claims"] = activity_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(activity_count * 0.1, 0.2))

        # Price urgency
        price_count, price_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.PRICE_URGENCY
        )
        if price_matches:
            text_indicators.extend(price_matches)
            details["price_urgency"] = price_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(price_count * 0.1, 0.2))

        # Check for specific (non-round) numbers
        number_pattern = re.compile(r'\b(\d{2,})\s*(?:people|users|left|remaining|viewing)')
        number_matches = number_pattern.findall(text_content)
        non_round_numbers = []
        for num_str in number_matches:
            num = int(num_str)
            # Non-round: not divisible by 10 or 50
            if num % 10 != 0 and num % 50 != 0:
                non_round_numbers.append(num)

        if non_round_numbers:
            text_indicators.append("specific_non_round_numbers")
            details["specific_numbers"] = non_round_numbers
            # Score: 0.15 for using specific numbers (appears more credible but often fabricated)
            score_components.append(0.15)

        # Check for activity without timeframe
        timeframe_pattern = re.compile(
            r'(today|this hour|last hour|in the past|recently|this week|per day)',
            re.IGNORECASE
        )
        has_timeframe = bool(timeframe_pattern.search(text_content))
        if activity_matches and not has_timeframe:
            text_indicators.append("activity_without_timeframe")
            score_components.append(0.15)

        # --- UI Configuration Analysis ---

        # Scarcity without verification
        if self._check_ui_condition(ui_config, "scarcity.verification_available", "=", False):
            ui_indicators.append("unverifiable_scarcity")
            score_components.append(0.2)

        # Countdown resets
        if self._check_ui_condition(ui_config, "countdown.resets_after_expiry", "=", True):
            ui_indicators.append("countdown_resets")
            score_components.append(0.2)

        # Notification escalation near deadline
        if self._check_ui_condition(ui_config, "notification.escalates_near_deadline", "=", True):
            ui_indicators.append("notification_escalation")
            score_components.append(0.1)

        # Activity updates only on page load (batch, not real-time)
        if self._check_ui_condition(ui_config, "activity_update.batch_only", "=", True):
            ui_indicators.append("batch_activity_updates")
            score_components.append(0.1)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P7ContextualOffersDetector(BasePatternDetector):
    """
    P7: Contextual Offers Detection (Emotional Timing)

    Detects patterns that time offers based on user's emotional
    state, particularly after failures or near-misses.

    Key indicators:
    - Offer timing after failure events
    - Emotional state-based message variation
    - Near-miss combined with purchase option
    - Time-limited offers with countdowns
    """

    PATTERN_ID = "P7"
    PATTERN_NAME = "Contextual Offers"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect contextual offers patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Failure recovery language
        failure_count, failure_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.FAILURE_RECOVERY
        )
        if failure_matches:
            text_indicators.extend(failure_matches)
            details["failure_recovery_language"] = failure_matches
            # Score: 0.15 per match, max 0.3
            score_components.append(min(failure_count * 0.15, 0.3))

        # Emotional state messaging
        emotional_count, emotional_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.EMOTIONAL_STATE_MESSAGING
        )
        if emotional_matches:
            text_indicators.extend(emotional_matches)
            details["emotional_targeting"] = emotional_matches
            # Score: 0.15 per match, max 0.25
            score_components.append(min(emotional_count * 0.15, 0.25))

        # Near-miss with purchase
        nearmiss_count, nearmiss_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.NEAR_MISS_PURCHASE
        )
        if nearmiss_matches:
            text_indicators.extend(nearmiss_matches)
            details["near_miss_purchase"] = nearmiss_matches
            # Score: 0.2 per match, max 0.3 (strong indicator)
            score_components.append(min(nearmiss_count * 0.2, 0.3))

        # --- UI Configuration Analysis ---

        # Offer timing after failure < 1000ms
        if self._check_ui_condition(ui_config, "offer.delay_after_failure_ms", "<", 1000):
            ui_indicators.append("immediate_offer_after_failure")
            delay = ui_config.get("offer", {}).get("delay_after_failure_ms", 0)
            details["offer_delay_ms"] = delay
            score_components.append(0.2)

        # Message varies by emotional state
        if self._check_ui_condition(ui_config, "messaging.varies_by_emotional_state", "=", True):
            ui_indicators.append("emotional_state_messaging")
            score_components.append(0.2)

        # Limited free attempts before paid option
        if self._check_ui_condition(ui_config, "free_attempts.limit_exists", "=", True):
            ui_indicators.append("limited_free_attempts")
            limit = ui_config.get("free_attempts", {}).get("count", 0)
            details["free_attempt_limit"] = limit
            score_components.append(0.15)

        # Countdown on offer (60-180 seconds)
        offer_countdown = ui_config.get("offer", {}).get("countdown_ms", 0)
        if 60000 <= offer_countdown <= 180000:
            ui_indicators.append("offer_countdown_active")
            details["offer_countdown_ms"] = offer_countdown
            score_components.append(0.15)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P8ImmersiveExperienceDetector(BasePatternDetector):
    """
    P8: Immersive Experience Detection (Flow State)

    Detects patterns designed to induce and maintain flow states,
    reducing user awareness of time and external factors.

    Key indicators:
    - Hidden time displays
    - Infinite scroll without breaks
    - Autoplay enabled by default
    - Infrequent pause checks
    """

    PATTERN_ID = "P8"
    PATTERN_NAME = "Immersive Experience"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect immersive experience patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Autoplay language
        autoplay_count, autoplay_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.AUTOPLAY_LANGUAGE
        )
        if autoplay_matches:
            text_indicators.extend(autoplay_matches)
            details["autoplay_language"] = autoplay_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(autoplay_count * 0.1, 0.2))

        # Infinite scroll language
        infinite_count, infinite_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.INFINITE_SCROLL_INDICATORS
        )
        if infinite_matches:
            text_indicators.extend(infinite_matches)
            details["infinite_scroll_language"] = infinite_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(infinite_count * 0.1, 0.2))

        # Time-obscuring language
        time_count, time_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.TIME_OBSCURING
        )
        if time_matches:
            text_indicators.extend(time_matches)
            details["time_obscuring_language"] = time_matches
            # Score: 0.1 per match, max 0.15
            score_components.append(min(time_count * 0.1, 0.15))

        # --- UI Configuration Analysis ---

        # Time display hidden or low opacity
        if self._check_ui_condition(ui_config, "time_display.visible", "=", False):
            ui_indicators.append("time_display_hidden")
            score_components.append(0.2)
        elif self._check_ui_condition(ui_config, "time_display.opacity", "<", 0.3):
            ui_indicators.append("time_display_obscured")
            score_components.append(0.15)

        # Infinite scroll (no stopping points)
        if self._check_ui_condition(ui_config, "scroll.stopping_points", "=", 0):
            ui_indicators.append("infinite_scroll_no_breaks")
            score_components.append(0.2)

        # Autoplay default enabled with short countdown
        if self._check_ui_condition(ui_config, "autoplay.default_enabled", "=", True):
            ui_indicators.append("autoplay_default_on")
            score_components.append(0.15)

            if self._check_ui_condition(ui_config, "autoplay.countdown_ms", "<", 5000):
                ui_indicators.append("short_autoplay_countdown")
                score_components.append(0.1)

        # Infrequent pause checks (> 3 minutes)
        if self._check_ui_condition(ui_config, "pause_check.interval_ms", ">", 180000):
            ui_indicators.append("infrequent_pause_checks")
            interval = ui_config.get("pause_check", {}).get("interval_ms", 0)
            details["pause_check_interval_ms"] = interval
            score_components.append(0.15)

        # Session duration hidden
        if self._check_ui_condition(ui_config, "session_duration.visible", "=", False):
            ui_indicators.append("session_duration_hidden")
            score_components.append(0.15)

        # Content pre-buffered seamlessly
        if self._check_ui_condition(ui_config, "content.preload_enabled", "=", True):
            ui_indicators.append("seamless_content_preload")
            score_components.append(0.1)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P9PersonalizedTiersDetector(BasePatternDetector):
    """
    P9: Personalized Experience Tiers Detection (Whale Targeting)

    Detects patterns that segment users by spending and provide
    differentiated pricing/experiences to high-value users.

    Key indicators:
    - Personalized offer messaging
    - Price variance by user cohort
    - VIP/status labels tied to spending
    - Offer value scaling with spending history
    """

    PATTERN_ID = "P9"
    PATTERN_NAME = "Personalized Experience Tiers"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect personalized tier patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Personalization language
        personal_count, personal_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.PERSONALIZATION_LANGUAGE
        )
        if personal_matches:
            text_indicators.extend(personal_matches)
            details["personalization_language"] = personal_matches
            # Score: 0.1 per match, max 0.25
            score_components.append(min(personal_count * 0.1, 0.25))

        # VIP/status language
        vip_count, vip_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.VIP_STATUS_LANGUAGE
        )
        if vip_matches:
            text_indicators.extend(vip_matches)
            details["vip_language"] = vip_matches
            # Score: 0.15 per match, max 0.3
            score_components.append(min(vip_count * 0.15, 0.3))

        # Spending tier indicators
        tier_count, tier_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.SPENDING_TIER_INDICATORS
        )
        if tier_matches:
            text_indicators.extend(tier_matches)
            details["tier_indicators"] = tier_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(tier_count * 0.1, 0.2))

        # --- UI Configuration Analysis ---

        # Price variance by cohort > 15%
        if self._check_ui_condition(ui_config, "pricing.cohort_variance", ">", 0.15):
            ui_indicators.append("price_varies_by_cohort")
            variance = ui_config.get("pricing", {}).get("cohort_variance", 0)
            details["price_variance"] = variance
            score_components.append(0.25)

        # VIP labels tied to spending threshold
        if self._check_ui_condition(ui_config, "vip_label.spending_threshold_trigger", "=", True):
            ui_indicators.append("vip_tied_to_spending")
            score_components.append(0.2)

        # Offer value correlates with lifetime spending
        if self._check_ui_condition(ui_config, "offer.spending_correlation", ">", 0.8):
            ui_indicators.append("offers_scale_with_spending")
            correlation = ui_config.get("offer", {}).get("spending_correlation", 0)
            details["spending_correlation"] = correlation
            score_components.append(0.2)

        # High-value bundles available to select cohort
        if self._check_ui_condition(ui_config, "bundles.high_value_restricted", "=", True):
            ui_indicators.append("exclusive_high_value_bundles")
            score_components.append(0.15)

        # Spending tier system active
        tier_count_config = ui_config.get("spending_tiers", {}).get("count", 0)
        if tier_count_config >= 3:
            ui_indicators.append("multi_tier_spending_system")
            details["spending_tier_count"] = tier_count_config
            score_components.append(0.15)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P10CommunityActivityDetector(BasePatternDetector):
    """
    P10: Community Activity Display Detection (Social Proof)

    Detects patterns displaying community activity metrics
    that may be unverifiable or presented without context.

    Key indicators:
    - Monotonic (never decreasing) activity counters
    - Activity without timeframe disclosure
    - Specific non-round numbers
    - Batch updates (not real-time)
    """

    PATTERN_ID = "P10"
    PATTERN_NAME = "Community Activity Display"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect community activity display patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Activity claims
        activity_count, activity_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.ACTIVITY_CLAIMS
        )

        # Activity verbs
        verb_count, verb_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.ACTIVITY_VERBS
        )

        # Combined activity messaging
        if activity_matches and verb_matches:
            text_indicators.extend(activity_matches)
            text_indicators.extend(verb_matches)
            details["activity_messaging"] = {
                "subjects": activity_matches,
                "verbs": verb_matches
            }
            # Score: 0.15 for combined activity claims
            score_components.append(0.15)

        # Recency indicators
        recency_count, recency_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.RECENCY_INDICATORS
        )
        if recency_matches:
            text_indicators.extend(recency_matches)
            details["recency_claims"] = recency_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(recency_count * 0.1, 0.2))

        # Check for specific numbers without timeframe
        number_pattern = re.compile(r'(\d+)\s*(?:people|users|customers|viewing|watching)')
        number_matches = number_pattern.findall(text_content)

        timeframe_pattern = re.compile(
            r'(today|this hour|per hour|this week|right now|currently)',
            re.IGNORECASE
        )
        has_timeframe = bool(timeframe_pattern.search(text_content))

        if number_matches:
            # Check for non-round numbers
            non_round = [int(n) for n in number_matches if int(n) % 10 != 0]
            if non_round:
                text_indicators.append("specific_activity_numbers")
                details["specific_numbers"] = non_round
                score_components.append(0.15)

            if not has_timeframe:
                text_indicators.append("activity_no_timeframe")
                score_components.append(0.15)

        # --- UI Configuration Analysis ---

        # Monotonic counter (never decreases)
        if self._check_ui_condition(ui_config, "activity_counter.monotonic", "=", True):
            ui_indicators.append("monotonic_counter")
            score_components.append(0.2)

        # Updates only on page load
        if self._check_ui_condition(ui_config, "activity_update.on_page_load_only", "=", True):
            ui_indicators.append("batch_updates_only")
            score_components.append(0.15)

        # No verification link
        if self._check_ui_condition(ui_config, "activity_claims.verification_available", "=", False):
            ui_indicators.append("no_verification_available")
            score_components.append(0.15)

        # Social proof on conversion page only
        if self._check_ui_condition(ui_config, "social_proof.conversion_page_only", "=", True):
            ui_indicators.append("social_proof_conversion_focused")
            score_components.append(0.1)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P11CommunityConnectionDetector(BasePatternDetector):
    """
    P11: Community Connection Detection (Social Obligation)

    Detects patterns that create social obligations and
    leverage peer relationships to drive engagement.

    Key indicators:
    - Group outcome dependency
    - Inactivity notifications with social context
    - Non-participation visibility
    - Reciprocity mechanics
    """

    PATTERN_ID = "P11"
    PATTERN_NAME = "Community Connection"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect community connection patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Social obligation language
        obligation_count, obligation_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.SOCIAL_OBLIGATION
        )
        if obligation_matches:
            text_indicators.extend(obligation_matches)
            details["social_obligation"] = obligation_matches
            # Score: 0.2 per match, max 0.4 (strong indicator)
            score_components.append(min(obligation_count * 0.2, 0.4))

        # Inactivity messaging
        inactivity_count, inactivity_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.INACTIVITY_MESSAGING
        )
        if inactivity_matches:
            text_indicators.extend(inactivity_matches)
            details["inactivity_messaging"] = inactivity_matches
            # Score: 0.15 per match, max 0.3
            score_components.append(min(inactivity_count * 0.15, 0.3))

        # Reciprocity triggers
        reciprocity_count, reciprocity_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.RECIPROCITY_TRIGGERS
        )
        if reciprocity_matches:
            text_indicators.extend(reciprocity_matches)
            details["reciprocity_triggers"] = reciprocity_matches
            # Score: 0.15 per match, max 0.25
            score_components.append(min(reciprocity_count * 0.15, 0.25))

        # Group visibility language
        visibility_count, visibility_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.GROUP_VISIBILITY
        )
        if visibility_matches:
            text_indicators.extend(visibility_matches)
            details["group_visibility"] = visibility_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(visibility_count * 0.1, 0.2))

        # --- UI Configuration Analysis ---

        # User actions affect group outcome
        if self._check_ui_condition(ui_config, "group_mechanics.user_affects_group", "=", True):
            ui_indicators.append("actions_affect_group")
            score_components.append(0.2)

        # Non-participation publicly visible
        if self._check_ui_condition(ui_config, "visibility.non_participation_public", "=", True):
            ui_indicators.append("non_participation_visible")
            score_components.append(0.2)

        # Inactivity notifications with social context
        if self._check_ui_condition(ui_config, "notifications.inactivity_social_context", "=", True):
            ui_indicators.append("social_inactivity_notifications")
            score_components.append(0.15)

        # Gift requires reciprocal action
        if self._check_ui_condition(ui_config, "gifts.requires_reciprocation", "=", True):
            ui_indicators.append("reciprocal_gift_requirement")
            score_components.append(0.15)

        # Leaderboard shows non-contributors
        if self._check_ui_condition(ui_config, "leaderboard.shows_non_contributors", "=", True):
            ui_indicators.append("non_contributor_leaderboard")
            score_components.append(0.15)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


class P12IdentityAchievementDetector(BasePatternDetector):
    """
    P12: Identity & Achievement Detection (Identity Lock-In)

    Detects patterns that tie user identity to platform engagement,
    creating psychological switching costs through identity investment.

    Key indicators:
    - Progression-based identity labels
    - Public profile investment display
    - Badge maintenance requirements
    - Achievement-tied merchandise/sharing
    """

    PATTERN_ID = "P12"
    PATTERN_NAME = "Identity & Achievement"

    def detect(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> PatternDetectionResult:
        """Detect identity and achievement patterns."""
        text_indicators = []
        ui_indicators = []
        details = {}
        score_components = []

        ui_config = ui_config or {}

        # --- Text Analysis ---

        # Identity labels
        identity_count, identity_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.IDENTITY_LABELS
        )
        if identity_matches:
            text_indicators.extend(identity_matches)
            details["identity_labels"] = identity_matches
            # Score: 0.15 per match, max 0.3
            score_components.append(min(identity_count * 0.15, 0.3))

        # Progression titles
        title_count, title_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.PROGRESSION_TITLES
        )
        if title_matches:
            text_indicators.extend(title_matches)
            details["progression_titles"] = title_matches
            # Score: 0.1 per match, max 0.25
            score_components.append(min(title_count * 0.1, 0.25))

        # Achievement language
        achievement_count, achievement_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.ACHIEVEMENT_LANGUAGE
        )
        if achievement_matches:
            text_indicators.extend(achievement_matches)
            details["achievement_language"] = achievement_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(achievement_count * 0.1, 0.2))

        # Public profile language
        profile_count, profile_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.PUBLIC_PROFILE
        )
        if profile_matches:
            text_indicators.extend(profile_matches)
            details["public_profile_language"] = profile_matches
            # Score: 0.1 per match, max 0.2
            score_components.append(min(profile_count * 0.1, 0.2))

        # Maintenance requirements
        maintenance_count, maintenance_matches = self._count_keyword_matches(
            text_content, EngagementPatterns.MAINTENANCE_REQUIREMENTS
        )
        if maintenance_matches:
            text_indicators.extend(maintenance_matches)
            details["maintenance_requirements"] = maintenance_matches
            # Score: 0.15 per match, max 0.25
            score_components.append(min(maintenance_count * 0.15, 0.25))

        # --- UI Configuration Analysis ---

        # Progression-based identity system
        if self._check_ui_condition(ui_config, "identity.progression_based", "=", True):
            ui_indicators.append("progression_identity_system")
            score_components.append(0.15)

        # Achievements visible on public profile
        if self._check_ui_condition(ui_config, "profile.achievements_public", "=", True):
            ui_indicators.append("public_achievement_display")
            score_components.append(0.15)

        # Badges require ongoing engagement
        if self._check_ui_condition(ui_config, "badges.requires_ongoing_engagement", "=", True):
            ui_indicators.append("badge_maintenance_required")
            score_components.append(0.2)

        # Badges decay without activity
        if self._check_ui_condition(ui_config, "badges.decay_without_activity", "=", True):
            ui_indicators.append("badge_decay_mechanic")
            score_components.append(0.2)

        # Merchandise tied to achievements
        if self._check_ui_condition(ui_config, "merchandise.achievement_triggered", "=", True):
            ui_indicators.append("achievement_merchandise")
            score_components.append(0.1)

        # Social sharing prompts at milestones
        if self._check_ui_condition(ui_config, "sharing.milestone_triggered", "=", True):
            ui_indicators.append("milestone_share_prompts")
            score_components.append(0.1)

        # Calculate final score
        raw_score = sum(score_components)
        final_score = max(0.0, min(1.0, raw_score))

        return PatternDetectionResult(
            pattern_id=self.PATTERN_ID,
            pattern_name=self.PATTERN_NAME,
            score=round(final_score, 3),
            intensity=self._classify_intensity(final_score),
            text_indicators=text_indicators,
            ui_indicators=ui_indicators,
            details=details
        )


# =============================================================================
# SECTION 6: COMBINED AUDITOR CLASS
# =============================================================================

class EngagementPatternAuditor:
    """
    Combined auditor for all 12 engagement patterns.

    Analyzes both text content and UI configuration to detect
    behavioral influence patterns and produce a comprehensive report.

    Usage:
        auditor = EngagementPatternAuditor()
        report = auditor.audit(
            text_content="Your UI text here",
            ui_config={"odds_disclosure": {"exists": False}}
        )
        print(report.to_json())
    """

    def __init__(self):
        """Initialize the auditor with all pattern detectors."""
        self.detectors: Dict[str, BasePatternDetector] = {
            "P1": P1VariableRewardDetector(),
            "P2": P2ProgressMomentumDetector(),
            "P3": P3EncouragingFeedbackDetector(),
            "P4": P4ProgressProtectionDetector(),
            "P5": P5InvestmentRecognitionDetector(),
            "P6": P6TimelyOpportunitiesDetector(),
            "P7": P7ContextualOffersDetector(),
            "P8": P8ImmersiveExperienceDetector(),
            "P9": P9PersonalizedTiersDetector(),
            "P10": P10CommunityActivityDetector(),
            "P11": P11CommunityConnectionDetector(),
            "P12": P12IdentityAchievementDetector(),
        }

        # Pattern weights for composite scoring
        # Weights based on behavioral impact research:
        # - Variable rewards (P1) and loss aversion (P4) have highest demonstrated impact
        # - Social patterns (P11) show strong retention effects
        # - Other patterns contribute moderately
        self.pattern_weights = {
            "P1": 1.2,   # Variable rewards - high impact on spending
            "P2": 1.0,   # Near-miss - moderate impact
            "P3": 0.9,   # Encouraging feedback - moderate impact
            "P4": 1.1,   # Loss aversion - high psychological impact
            "P5": 1.0,   # Sunk cost - moderate impact
            "P6": 1.0,   # Scarcity - moderate impact
            "P7": 1.0,   # Emotional timing - moderate impact
            "P8": 0.9,   # Flow state - moderate impact
            "P9": 1.1,   # Whale targeting - high revenue impact
            "P10": 0.8,  # Social proof - lower individual impact
            "P11": 1.1,  # Social obligation - high retention impact
            "P12": 1.0,  # Identity - moderate impact
        }

    def audit(
        self,
        text_content: str = "",
        ui_config: Optional[Dict[str, Any]] = None
    ) -> EngagementAuditReport:
        """
        Run full audit across all pattern detectors.

        Args:
            text_content: Text content from UI to analyze
            ui_config: UI configuration dictionary with structural elements

        Returns:
            Complete EngagementAuditReport
        """
        ui_config = ui_config or {}

        # Generate audit metadata
        audit_id = self._generate_audit_id(text_content, ui_config)
        timestamp = datetime.utcnow().isoformat() + "Z"
        content_hash = hashlib.sha256(
            (text_content + json.dumps(ui_config, sort_keys=True)).encode()
        ).hexdigest()[:16]

        # Run all detectors
        patterns: Dict[str, PatternDetectionResult] = {}
        for pattern_id, detector in self.detectors.items():
            result = detector.detect(text_content, ui_config)
            patterns[pattern_id] = result

        # Calculate composite score
        composite_score = self._calculate_composite_score(patterns)

        # Classify overall intensity
        intensity_classification = self._classify_overall_intensity(composite_score)

        # Identify high-intensity patterns
        high_intensity_patterns = [
            f"{pid}: {result.pattern_name}"
            for pid, result in patterns.items()
            if result.intensity in ["HIGH", "EXTREME"]
        ]

        # Generate recommendations
        recommendations = self._generate_recommendations(patterns)

        return EngagementAuditReport(
            audit_id=audit_id,
            timestamp=timestamp,
            content_hash=content_hash,
            patterns=patterns,
            composite_score=round(composite_score, 3),
            intensity_classification=intensity_classification,
            high_intensity_patterns=high_intensity_patterns,
            recommendations=recommendations
        )

    def audit_text_only(self, text_content: str) -> EngagementAuditReport:
        """
        Run audit on text content only (no UI configuration).

        Args:
            text_content: Text content to analyze

        Returns:
            EngagementAuditReport
        """
        return self.audit(text_content=text_content, ui_config=None)

    def audit_ui_only(self, ui_config: Dict[str, Any]) -> EngagementAuditReport:
        """
        Run audit on UI configuration only (no text).

        Args:
            ui_config: UI configuration dictionary

        Returns:
            EngagementAuditReport
        """
        return self.audit(text_content="", ui_config=ui_config)

    def _generate_audit_id(
        self,
        text_content: str,
        ui_config: Dict[str, Any]
    ) -> str:
        """Generate unique audit ID."""
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        content_hash = hashlib.md5(
            (text_content + str(ui_config)).encode()
        ).hexdigest()[:8]
        return f"ENG-{timestamp}-{content_hash}"

    def _calculate_composite_score(
        self,
        patterns: Dict[str, PatternDetectionResult]
    ) -> float:
        """
        Calculate weighted composite score from all patterns.

        Uses weighted average with pattern-specific weights based on
        behavioral impact research.
        """
        weighted_sum = 0.0
        weight_sum = 0.0

        for pattern_id, result in patterns.items():
            weight = self.pattern_weights.get(pattern_id, 1.0)
            weighted_sum += result.score * weight
            weight_sum += weight

        if weight_sum == 0:
            return 0.0

        return weighted_sum / weight_sum

    def _classify_overall_intensity(self, composite_score: float) -> str:
        """Classify overall intensity based on composite score."""
        if composite_score >= 0.7:
            return "HIGH_INTENSITY"
        elif composite_score >= 0.4:
            return "MODERATE_INTENSITY"
        elif composite_score >= 0.2:
            return "LOW_INTENSITY"
        return "MINIMAL"

    def _generate_recommendations(
        self,
        patterns: Dict[str, PatternDetectionResult]
    ) -> List[str]:
        """Generate actionable recommendations based on detected patterns."""
        recommendations = []

        # Pattern-specific recommendations
        pattern_recommendations = {
            "P1": "Consider displaying odds/probability information prominently",
            "P2": "Review near-miss frequency to ensure it matches random expectation",
            "P3": "Ensure outcome displays include full context (wager amount, net result)",
            "P4": "Review loss-focused messaging ratio and protection pricing",
            "P5": "Simplify cancellation flow and reduce investment summary emphasis",
            "P6": "Add verification mechanisms for scarcity claims",
            "P7": "Review offer timing relative to user emotional states",
            "P8": "Add periodic break prompts and visible session duration",
            "P9": "Review price consistency across user cohorts",
            "P10": "Add timeframe context to activity displays",
            "P11": "Review social obligation mechanics and notification frequency",
            "P12": "Review badge maintenance requirements and decay mechanics",
        }

        for pattern_id, result in patterns.items():
            if result.intensity in ["HIGH", "EXTREME"]:
                if pattern_id in pattern_recommendations:
                    recommendations.append(
                        f"[{pattern_id}] {pattern_recommendations[pattern_id]}"
                    )

        if not recommendations:
            recommendations.append("No high-intensity patterns detected")

        return recommendations

    def get_pattern_summary(
        self,
        patterns: Dict[str, PatternDetectionResult]
    ) -> Dict[str, Any]:
        """
        Get summary statistics for detected patterns.

        Args:
            patterns: Dictionary of pattern detection results

        Returns:
            Summary dictionary with statistics
        """
        scores = [r.score for r in patterns.values()]
        intensities = [r.intensity for r in patterns.values()]

        return {
            "total_patterns": len(patterns),
            "average_score": round(sum(scores) / len(scores), 3) if scores else 0,
            "max_score": round(max(scores), 3) if scores else 0,
            "min_score": round(min(scores), 3) if scores else 0,
            "high_intensity_count": sum(1 for i in intensities if i in ["HIGH", "EXTREME"]),
            "moderate_intensity_count": sum(1 for i in intensities if i == "MODERATE"),
            "low_intensity_count": sum(1 for i in intensities if i == "LOW"),
            "none_count": sum(1 for i in intensities if i == "NONE"),
        }


# =============================================================================
# SECTION 7: UTILITY FUNCTIONS
# =============================================================================

def quick_audit(text: str) -> Dict[str, Any]:
    """
    Quick audit function for simple text analysis.

    Args:
        text: Text content to analyze

    Returns:
        Dictionary with audit results
    """
    auditor = EngagementPatternAuditor()
    report = auditor.audit_text_only(text)
    return report.to_dict()


def audit_ui_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Audit UI configuration dictionary.

    Args:
        config: UI configuration dictionary

    Returns:
        Dictionary with audit results
    """
    auditor = EngagementPatternAuditor()
    report = auditor.audit_ui_only(config)
    return report.to_dict()


def get_pattern_descriptions() -> Dict[str, str]:
    """
    Get descriptions for all 12 engagement patterns.

    Returns:
        Dictionary mapping pattern IDs to descriptions
    """
    return {
        "P1": "Variable Reward Scheduling - Randomized reward mechanisms with hidden odds",
        "P2": "Progress Momentum - Near-miss experiences encouraging continuation",
        "P3": "Encouraging Feedback - Positive reinforcement for net-negative outcomes",
        "P4": "Progress Protection - Loss aversion leveraged for streak protection",
        "P5": "Investment Recognition - Sunk cost highlighted during exit flows",
        "P6": "Timely Opportunities - Unverifiable scarcity and urgency claims",
        "P7": "Contextual Offers - Emotionally-timed purchase opportunities",
        "P8": "Immersive Experience - Flow state induction reducing time awareness",
        "P9": "Personalized Experience Tiers - Spending-based user segmentation",
        "P10": "Community Activity Display - Social proof with limited verification",
        "P11": "Community Connection - Social obligation and peer pressure mechanics",
        "P12": "Identity & Achievement - Platform-tied identity and status systems",
    }


# =============================================================================
# SECTION 8: MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Example usage demonstration

    # Sample text content
    sample_text = """
    Congratulations! You almost won the jackpot! Just one more spin could be your lucky break.

    Your 47-day streak is at risk! Protect it now before it expires in 2 hours.
    Only 3 left in stock - 847 people are viewing this right now!

    As a Dedicated Player, you've earned exclusive VIP access. Your friends are waiting
    for you to join the raid. Don't let your team down!

    Special offer just for you: Get 50% more coins. This personalized deal expires soon!
    """

    # Sample UI configuration
    sample_ui_config = {
        "odds_disclosure": {"exists": False},
        "rarity_tier": {"count": 5},
        "animation_duration": 4500,
        "streak_display": {"opacity": 0.95, "font_size_ratio": 1.2},
        "cancellation_flow": {"step_count": 4},
        "autoplay": {"default_enabled": True, "countdown_ms": 3000},
        "time_display": {"visible": False},
        "activity_counter": {"monotonic": True},
        "badges": {"requires_ongoing_engagement": True}
    }

    # Run audit
    auditor = EngagementPatternAuditor()
    report = auditor.audit(sample_text, sample_ui_config)

    # Print results
    print("=" * 70)
    print("ENGAGEMENT PATTERN AUDIT REPORT")
    print("=" * 70)
    print(f"Audit ID: {report.audit_id}")
    print(f"Timestamp: {report.timestamp}")
    print(f"Composite Score: {report.composite_score}")
    print(f"Classification: {report.intensity_classification}")
    print()
    print("Pattern Scores:")
    print("-" * 40)
    for pid, result in report.patterns.items():
        print(f"  {pid} ({result.pattern_name}): {result.score:.3f} [{result.intensity}]")
    print()
    print("High Intensity Patterns:")
    for pattern in report.high_intensity_patterns:
        print(f"  - {pattern}")
    print()
    print("Recommendations:")
    for rec in report.recommendations:
        print(f"  - {rec}")
    print()
    print("Full JSON Report:")
    print(report.to_json())
