# HIGH-IMPACT DETECTION SYSTEMS
## Detection Code for the Most Effective Influence Patterns

**Document Version:** 1.0
**Created:** February 2025
**Purpose:** Specialized detectors for the highest-impact influence mechanisms identified through research

---

## TABLE OF CONTENTS

1. [Synergistic Stacking Detector](#1-synergistic-stacking-detector)
2. [Vulnerability Timing Detector](#2-vulnerability-timing-detector)
3. [Trust Leverage Sequence Detector](#3-trust-leverage-sequence-detector)
4. [Physiological Bypassing Detector](#4-physiological-bypassing-detector)
5. [AI Amplification Detector](#5-ai-amplification-detector)
6. [Economic Intensity Detector](#6-economic-intensity-detector)
7. [Vulnerable Population Targeting Detector](#7-vulnerable-population-targeting-detector)
8. [Information Ecosystem Optimization Detector](#8-information-ecosystem-optimization-detector)
9. [Master High-Impact Auditor](#9-master-high-impact-auditor)

---

## 1. SYNERGISTIC STACKING DETECTOR

**Research Finding:** Influencers stack 3-5 techniques with known synergy multipliers. Single techniques are rare in sophisticated influence applications.

```python
import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Set
from enum import Enum
from collections import defaultdict
import re
import time

class InfluenceTechnique(Enum):
    # Cialdini's Principles
    SCARCITY = "scarcity"
    SOCIAL_PROOF = "social_proof"
    AUTHORITY = "authority"
    RECIPROCITY = "reciprocity"
    COMMITMENT = "commitment"
    LIKING = "liking"
    UNITY = "unity"

    # Emotional Techniques
    FEAR = "fear"
    URGENCY = "urgency"
    FOMO = "fomo"
    GUILT = "guilt"
    EXCITEMENT = "excitement"

    # Cognitive Techniques
    ANCHORING = "anchoring"
    DECOY = "decoy"
    FRAMING = "framing"
    COGNITIVE_LOAD = "cognitive_overload"

    # Platform Techniques
    VARIABLE_REWARD = "variable_reward"
    STREAK = "streak"
    INFINITE_SCROLL = "infinite_scroll"
    PERSONALIZATION = "personalization"

    # Trust Techniques
    FAKE_REVIEWS = "fake_reviews"
    TESTIMONIALS = "testimonials"
    CREDENTIALS = "credentials"

@dataclass
class SynergyProfile:
    """Known synergistic combinations and their multipliers"""
    techniques: Tuple[InfluenceTechnique, ...]
    multiplier: float
    mechanism: str
    research_source: str

@dataclass
class StackingAnalysis:
    """Results of synergistic stacking analysis"""
    techniques_detected: List[InfluenceTechnique] = field(default_factory=list)
    technique_count: int = 0
    synergies_activated: List[SynergyProfile] = field(default_factory=list)
    total_multiplier: float = 1.0
    base_influence_score: float = 0.0
    amplified_score: float = 0.0
    sophistication_level: str = "low"  # low, medium, high, professional
    pattern_signature: str = ""

class SynergisticStackingDetector:
    """
    Detects when multiple influence techniques are stacked for amplified effect.

    Research basis:
    - Combination multipliers from persuasion research
    - Platform design analysis showing intentional stacking
    - Scarcity + Social Proof = 1.4x; Authority + Personalization = 1.3x
    """

    # Empirically validated synergy combinations
    KNOWN_SYNERGIES: List[SynergyProfile] = [
        SynergyProfile(
            techniques=(InfluenceTechnique.SCARCITY, InfluenceTechnique.SOCIAL_PROOF),
            multiplier=1.4,
            mechanism="Scarcity validates social proof ('others want it too')",
            research_source="Cialdini combination studies"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.AUTHORITY, InfluenceTechnique.PERSONALIZATION),
            multiplier=1.3,
            mechanism="Personalized authority feels more credible",
            research_source="LLM persuasion research 2024"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.URGENCY, InfluenceTechnique.SCARCITY),
            multiplier=1.35,
            mechanism="Time pressure + limited quantity = panic buying",
            research_source="E-commerce interface pattern analysis"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.FEAR, InfluenceTechnique.AUTHORITY),
            multiplier=1.45,
            mechanism="Authority amplifies fear credibility",
            research_source="Health misinformation studies"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.SOCIAL_PROOF, InfluenceTechnique.FOMO),
            multiplier=1.35,
            mechanism="Others acting + missing out = action compulsion",
            research_source="Social media engagement research"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.RECIPROCITY, InfluenceTechnique.COMMITMENT),
            multiplier=1.25,
            mechanism="Gift creates obligation, small commitment enables larger",
            research_source="Foot-in-door research"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.VARIABLE_REWARD, InfluenceTechnique.STREAK),
            multiplier=1.5,
            mechanism="Unpredictable rewards + loss aversion = compulsive engagement",
            research_source="Gamification engagement studies"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.INFINITE_SCROLL, InfluenceTechnique.PERSONALIZATION),
            multiplier=1.45,
            mechanism="Endless content + relevance = time distortion",
            research_source="CHI 2024 attention capture research"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.ANCHORING, InfluenceTechnique.DECOY),
            multiplier=1.4,
            mechanism="Reference price + inferior option = target selection",
            research_source="Behavioral economics pricing studies"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.COGNITIVE_LOAD, InfluenceTechnique.URGENCY),
            multiplier=1.5,
            mechanism="Overwhelmed + pressured = System 1 decision",
            research_source="Decision fatigue research"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.GUILT, InfluenceTechnique.COMMITMENT),
            multiplier=1.3,
            mechanism="Prior commitment + guilt = continued compliance",
            research_source="Sunk cost influence research"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.TESTIMONIALS, InfluenceTechnique.LIKING),
            multiplier=1.25,
            mechanism="Likeable testimonials feel more authentic",
            research_source="Influencer marketing research"
        ),
        # Triple combinations (higher sophistication)
        SynergyProfile(
            techniques=(InfluenceTechnique.SCARCITY, InfluenceTechnique.SOCIAL_PROOF, InfluenceTechnique.URGENCY),
            multiplier=1.7,
            mechanism="Triple threat: limited + popular + time-sensitive",
            research_source="Interface pattern combination analysis"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.AUTHORITY, InfluenceTechnique.FEAR, InfluenceTechnique.URGENCY),
            multiplier=1.8,
            mechanism="Expert warning + danger + act now = bypass critical thinking",
            research_source="Scam effectiveness research"
        ),
        SynergyProfile(
            techniques=(InfluenceTechnique.VARIABLE_REWARD, InfluenceTechnique.STREAK, InfluenceTechnique.SOCIAL_PROOF),
            multiplier=1.65,
            mechanism="Gambling mechanics + loss aversion + peer pressure",
            research_source="Mobile game monetization studies"
        ),
    ]

    # Detection patterns for each technique
    TECHNIQUE_PATTERNS = {
        InfluenceTechnique.SCARCITY: {
            'text_patterns': [
                r'only \d+ left', r'limited (stock|quantity|availability)',
                r'selling fast', r'almost (gone|sold out)', r'few remaining',
                r'while supplies last', r'exclusive', r'rare'
            ],
            'ui_patterns': ['low_stock_indicator', 'inventory_counter', 'sold_out_warning']
        },
        InfluenceTechnique.SOCIAL_PROOF: {
            'text_patterns': [
                r'\d+[,\d]* (people|customers|users)', r'best.?seller',
                r'most popular', r'trending', r'everyone', r'\d+\s*reviews',
                r'trusted by', r'join \d+', r'as seen'
            ],
            'ui_patterns': ['review_count', 'rating_stars', 'buyer_count', 'trending_badge']
        },
        InfluenceTechnique.AUTHORITY: {
            'text_patterns': [
                r'expert', r'doctor', r'scientist', r'study shows',
                r'research proves', r'certified', r'official', r'approved',
                r'recommended by', r'endorsed', r'award.?winning'
            ],
            'ui_patterns': ['certification_badge', 'expert_photo', 'credential_display']
        },
        InfluenceTechnique.URGENCY: {
            'text_patterns': [
                r'act now', r'limited time', r'expires', r'deadline',
                r'today only', r'last chance', r'don\'t wait', r'hurry',
                r'ends (in|soon)', r'\d+:\d+:\d+', r'countdown'
            ],
            'ui_patterns': ['countdown_timer', 'expiration_notice', 'urgency_banner']
        },
        InfluenceTechnique.FEAR: {
            'text_patterns': [
                r'risk', r'danger', r'threat', r'warning', r'protect',
                r'before it\'s too late', r'don\'t miss', r'lose',
                r'vulnerable', r'exposed', r'attack'
            ],
            'ui_patterns': ['warning_icon', 'alert_banner', 'danger_color']
        },
        InfluenceTechnique.FOMO: {
            'text_patterns': [
                r'missing out', r'don\'t miss', r'everyone (else|is)',
                r'left behind', r'others are', r'happening now',
                r'you\'re missing', r'while you wait'
            ],
            'ui_patterns': ['activity_feed', 'real_time_purchases', 'viewer_count']
        },
        InfluenceTechnique.GUILT: {
            'text_patterns': [
                r'disappoint', r'let down', r'after (all|everything)',
                r'we thought', r'sad to see', r'we\'ll miss',
                r'giving up', r'abandoning'
            ],
            'ui_patterns': ['sad_mascot', 'guilt_message', 'abandonment_warning']
        },
        InfluenceTechnique.RECIPROCITY: {
            'text_patterns': [
                r'free (gift|bonus|trial)', r'complimentary', r'on us',
                r'no obligation', r'as a thank you', r'exclusive (offer|access)',
                r'we\'ve given you', r'your free'
            ],
            'ui_patterns': ['gift_icon', 'bonus_indicator', 'free_trial_badge']
        },
        InfluenceTechnique.COMMITMENT: {
            'text_patterns': [
                r'you (already|previously)', r'continue', r'don\'t lose progress',
                r'you\'ve invested', r'come this far', r'almost there',
                r'just one more step', r'finish what you started'
            ],
            'ui_patterns': ['progress_bar', 'step_indicator', 'completion_percentage']
        },
        InfluenceTechnique.ANCHORING: {
            'text_patterns': [
                r'was \$[\d,]+', r'(originally|regular) \$[\d,]+',
                r'save \$[\d,]+', r'\d+% off', r'compare at',
                r'value of \$[\d,]+', r'worth \$[\d,]+'
            ],
            'ui_patterns': ['strikethrough_price', 'savings_badge', 'compare_price']
        },
        InfluenceTechnique.VARIABLE_REWARD: {
            'text_patterns': [
                r'spin (to|the) win', r'mystery', r'surprise', r'random',
                r'chance to', r'lucky', r'jackpot', r'bonus wheel'
            ],
            'ui_patterns': ['spin_wheel', 'loot_box', 'mystery_reward', 'gacha']
        },
        InfluenceTechnique.STREAK: {
            'text_patterns': [
                r'\d+ day streak', r'don\'t break', r'keep (it|your) going',
                r'consecutive', r'daily (bonus|reward)', r'maintain'
            ],
            'ui_patterns': ['streak_counter', 'flame_icon', 'chain_visual']
        },
        InfluenceTechnique.PERSONALIZATION: {
            'text_patterns': [
                r'(just |especially |picked )?for you', r'based on your',
                r'personalized', r'your (interests|preferences|history)',
                r'recommended for you', r'tailored'
            ],
            'ui_patterns': ['personalized_section', 'for_you_feed', 'recommendation_row']
        },
        InfluenceTechnique.COGNITIVE_LOAD: {
            'text_patterns': [
                r'(many|multiple|various) options', r'compare',
                r'features include', r'specifications'
            ],
            'ui_patterns': [
                'excessive_options', 'complex_comparison', 'information_overload',
                'multi_step_form', 'many_checkboxes'
            ]
        },
    }

    def __init__(self):
        self.detection_cache = {}

    def detect_techniques(self, content: Dict) -> List[InfluenceTechnique]:
        """
        Detect all influence techniques present in content.

        Expected content:
        {
            'text': str,
            'ui_elements': List[str],
            'metadata': Dict
        }
        """
        detected = []
        text = content.get('text', '').lower()
        ui_elements = [e.lower() for e in content.get('ui_elements', [])]

        for technique, patterns in self.TECHNIQUE_PATTERNS.items():
            # Check text patterns
            text_matches = sum(
                1 for pattern in patterns['text_patterns']
                if re.search(pattern, text, re.IGNORECASE)
            )

            # Check UI patterns
            ui_matches = sum(
                1 for pattern in patterns['ui_patterns']
                if any(pattern in elem for elem in ui_elements)
            )

            # Technique is detected if we have sufficient evidence
            if text_matches >= 1 or ui_matches >= 1:
                detected.append(technique)

        return detected

    def analyze_stacking(self, content: Dict) -> StackingAnalysis:
        """
        Analyze content for synergistic technique stacking.
        """
        analysis = StackingAnalysis()

        # Detect all techniques
        analysis.techniques_detected = self.detect_techniques(content)
        analysis.technique_count = len(analysis.techniques_detected)

        if analysis.technique_count == 0:
            return analysis

        # Calculate base score (diminishing returns for raw count)
        analysis.base_influence_score = min(1.0,
            0.15 * analysis.technique_count +
            0.05 * (analysis.technique_count ** 0.5)
        )

        # Find activated synergies
        detected_set = set(analysis.techniques_detected)

        for synergy in self.KNOWN_SYNERGIES:
            synergy_set = set(synergy.techniques)
            if synergy_set.issubset(detected_set):
                analysis.synergies_activated.append(synergy)

        # Calculate total multiplier (multiplicative but with diminishing returns)
        if analysis.synergies_activated:
            # Sort by multiplier descending
            sorted_synergies = sorted(
                analysis.synergies_activated,
                key=lambda x: x.multiplier,
                reverse=True
            )

            analysis.total_multiplier = 1.0
            for i, synergy in enumerate(sorted_synergies):
                # Each subsequent synergy has reduced additional effect
                diminishing_factor = 1 / (1 + i * 0.4)
                additional_multiplier = (synergy.multiplier - 1) * diminishing_factor
                analysis.total_multiplier += additional_multiplier

        # Calculate amplified score
        analysis.amplified_score = min(1.0,
            analysis.base_influence_score * analysis.total_multiplier
        )

        # Determine sophistication level
        if analysis.technique_count >= 5 and len(analysis.synergies_activated) >= 2:
            analysis.sophistication_level = "professional"
        elif analysis.technique_count >= 4 or len(analysis.synergies_activated) >= 2:
            analysis.sophistication_level = "high"
        elif analysis.technique_count >= 2 or len(analysis.synergies_activated) >= 1:
            analysis.sophistication_level = "medium"
        else:
            analysis.sophistication_level = "low"

        # Generate pattern signature
        technique_names = sorted([t.value for t in analysis.techniques_detected])
        analysis.pattern_signature = "+".join(technique_names[:5])  # Top 5

        return analysis

    def get_synergy_explanation(self, analysis: StackingAnalysis) -> List[str]:
        """Generate human-readable explanations of detected synergies"""
        explanations = []

        for synergy in analysis.synergies_activated:
            technique_names = [t.value for t in synergy.techniques]
            explanations.append(
                f"SYNERGY DETECTED: {' + '.join(technique_names)} "
                f"(×{synergy.multiplier:.2f})\n"
                f"  Mechanism: {synergy.mechanism}\n"
                f"  Source: {synergy.research_source}"
            )

        return explanations
```

---

## 2. VULNERABILITY TIMING DETECTOR

**Research Finding:** Influence is timed to vulnerability windows - circadian rhythm, emotional state, decision fatigue. TikTok detects emotional vulnerability with 94% accuracy.

```python
from datetime import datetime, timezone
from typing import Optional

class VulnerabilityWindow(Enum):
    CIRCADIAN_LOW = "circadian_cognitive_low"  # 2-4 AM
    DECISION_FATIGUE = "decision_fatigue_window"
    EMOTIONAL_DISTRESS = "emotional_vulnerability"
    POST_NOTIFICATION = "notification_arousal_window"
    WORK_STRESS = "end_of_workday"
    WEEKEND_RELAXED = "weekend_reduced_vigilance"
    PAYCHECK = "post_paycheck_spending"
    LATE_NIGHT = "late_night_impulse"
    MORNING_RUSH = "morning_decision_pressure"

@dataclass
class TimingIntensityAnalysis:
    """Analysis of vulnerability timing intensity"""
    vulnerability_windows_targeted: List[VulnerabilityWindow] = field(default_factory=list)
    timing_intensity_score: float = 0.0
    temporal_patterns: List[Dict] = field(default_factory=list)
    notification_timing_suspicious: bool = False
    circadian_intensity: bool = False
    decision_fatigue_intensity: bool = False
    emotional_state_intensity: bool = False
    recommendations: List[str] = field(default_factory=list)

class VulnerabilityTimingDetector:
    """
    Detects when content/notifications are timed to leverage vulnerability windows.

    Research basis:
    - 2-4 AM decisions show 40%+ reduced critical thinking
    - TikTok emotional state detection: 94% accuracy
    - Decision fatigue: After 10-15 choices, compliance +35%
    - Post-notification arousal window: 2-5 minutes elevated suggestibility
    """

    # Circadian vulnerability hours (local time)
    CIRCADIAN_VULNERABILITY = {
        'severe': [(2, 4)],      # 2-4 AM: worst cognitive function
        'moderate': [(0, 2), (4, 6), (14, 15)],  # Midnight-2AM, 4-6AM, post-lunch dip
        'mild': [(22, 24)]      # 10PM-midnight: fatigue accumulation
    }

    # Decision fatigue thresholds
    DECISION_FATIGUE_THRESHOLDS = {
        'onset': 7,           # Fatigue begins
        'moderate': 12,       # Significant impairment
        'severe': 20          # Compliance mode
    }

    # Notification-to-action optimal timing (for influencers)
    NOTIFICATION_INTENSITY_WINDOW = {
        'peak_arousal': (0, 30),      # 0-30 seconds: highest arousal
        'elevated': (30, 120),         # 30-120 seconds: still elevated
        'post_arousal': (120, 300)    # 2-5 minutes: residual effect
    }

    # Emotional state indicators that predict vulnerability
    EMOTIONAL_VULNERABILITY_SIGNALS = {
        'text_patterns': {
            'sadness': [r'sad', r'depressed', r'lonely', r'miss', r'crying', r'hurt'],
            'anxiety': [r'worried', r'anxious', r'scared', r'nervous', r'panic'],
            'anger': [r'angry', r'furious', r'hate', r'frustrated', r'annoyed'],
            'loneliness': [r'alone', r'no one', r'nobody', r'isolated', r'empty'],
            'boredom': [r'bored', r'nothing to do', r'tired of', r'same old'],
            'excitement': [r'excited', r'can\'t wait', r'amazing', r'best day']
        },
        'behavioral_patterns': {
            'late_night_browsing': 'loneliness_indicator',
            'rapid_scrolling': 'anxiety_or_boredom',
            'repeated_checking': 'anxiety_indicator',
            'long_sessions': 'escapism_indicator'
        }
    }

    def __init__(self):
        self.user_decision_count = defaultdict(int)
        self.user_notification_history = defaultdict(list)
        self.user_emotional_signals = defaultdict(list)

    def analyze_timing(
        self,
        timestamp: float,
        user_id: str,
        content: Dict,
        user_behavior: Dict = None
    ) -> TimingIntensityAnalysis:
        """
        Analyze whether content timing leverages vulnerability windows.

        Args:
            timestamp: Unix timestamp of content delivery
            user_id: User identifier for tracking patterns
            content: Content being delivered
            user_behavior: Optional behavioral signals
        """
        analysis = TimingIntensityAnalysis()

        # Convert timestamp to local time
        dt = datetime.fromtimestamp(timestamp)
        hour = dt.hour
        day_of_week = dt.weekday()  # 0=Monday, 6=Sunday

        # 1. Check circadian vulnerability
        circadian_risk = self._check_circadian_vulnerability(hour)
        if circadian_risk:
            analysis.circadian_intensity = True
            analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.CIRCADIAN_LOW)
            analysis.timing_intensity_score += circadian_risk
            analysis.temporal_patterns.append({
                'type': 'circadian',
                'hour': hour,
                'risk_level': circadian_risk
            })

        # 2. Check for late night targeting
        if 22 <= hour or hour < 6:
            analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.LATE_NIGHT)
            analysis.timing_intensity_score += 0.2

        # 3. Check decision fatigue
        if user_id:
            decision_count = self.user_decision_count.get(user_id, 0)
            fatigue_level = self._assess_decision_fatigue(decision_count)

            if fatigue_level:
                analysis.decision_fatigue_intensity = True
                analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.DECISION_FATIGUE)
                analysis.timing_intensity_score += fatigue_level
                analysis.temporal_patterns.append({
                    'type': 'decision_fatigue',
                    'decision_count': decision_count,
                    'fatigue_level': fatigue_level
                })

        # 4. Check notification timing patterns
        if user_id and self.user_notification_history.get(user_id):
            notification_analysis = self._analyze_notification_timing(user_id, timestamp)
            if notification_analysis['suspicious']:
                analysis.notification_timing_suspicious = True
                analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.POST_NOTIFICATION)
                analysis.timing_intensity_score += 0.3

        # 5. Check emotional state intensity
        if user_behavior:
            emotional_intensity = self._check_emotional_intensity(
                user_behavior,
                content
            )
            if emotional_intensity['targeted']:
                analysis.emotional_state_intensity = True
                analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.EMOTIONAL_DISTRESS)
                analysis.timing_intensity_score += emotional_intensity['score']

        # 6. Check work/weekend patterns
        if 17 <= hour <= 19 and day_of_week < 5:  # Weekday evening
            analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.WORK_STRESS)
            analysis.timing_intensity_score += 0.1

        if day_of_week >= 5 and 10 <= hour <= 14:  # Weekend midday
            analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.WEEKEND_RELAXED)
            analysis.timing_intensity_score += 0.1

        # 7. Check paycheck timing (if available)
        if dt.day in [1, 15, 28, 29, 30, 31]:  # Common paycheck days
            analysis.vulnerability_windows_targeted.append(VulnerabilityWindow.PAYCHECK)
            analysis.timing_intensity_score += 0.15

        # Normalize score
        analysis.timing_intensity_score = min(1.0, analysis.timing_intensity_score)

        # Generate recommendations
        analysis.recommendations = self._generate_recommendations(analysis)

        return analysis

    def _check_circadian_vulnerability(self, hour: int) -> float:
        """Check if hour falls in circadian vulnerability window"""
        for start, end in self.CIRCADIAN_VULNERABILITY['severe']:
            if start <= hour < end:
                return 0.5

        for start, end in self.CIRCADIAN_VULNERABILITY['moderate']:
            if start <= hour < end:
                return 0.3

        for start, end in self.CIRCADIAN_VULNERABILITY['mild']:
            if start <= hour < end:
                return 0.15

        return 0.0

    def _assess_decision_fatigue(self, decision_count: int) -> float:
        """Assess decision fatigue level"""
        if decision_count >= self.DECISION_FATIGUE_THRESHOLDS['severe']:
            return 0.5  # High intensity potential
        elif decision_count >= self.DECISION_FATIGUE_THRESHOLDS['moderate']:
            return 0.3
        elif decision_count >= self.DECISION_FATIGUE_THRESHOLDS['onset']:
            return 0.15
        return 0.0

    def _analyze_notification_timing(self, user_id: str, current_time: float) -> Dict:
        """Analyze if content follows shortly after notification (intensity window)"""
        history = self.user_notification_history.get(user_id, [])

        result = {
            'suspicious': False,
            'time_since_notification': None,
            'intensity_window': None
        }

        if not history:
            return result

        last_notification = history[-1]
        time_diff = current_time - last_notification['timestamp']

        result['time_since_notification'] = time_diff

        # Check if within intensity window
        for window_name, (start, end) in self.NOTIFICATION_INTENSITY_WINDOW.items():
            if start <= time_diff <= end:
                result['suspicious'] = True
                result['intensity_window'] = window_name
                break

        return result

    def _check_emotional_intensity(self, behavior: Dict, content: Dict) -> Dict:
        """Check if content targets detected emotional state"""
        result = {
            'targeted': False,
            'emotional_state': None,
            'content_targets_state': False,
            'score': 0.0
        }

        # Detect emotional state from behavior
        detected_emotions = []

        if behavior.get('recent_searches'):
            searches = ' '.join(behavior['recent_searches']).lower()
            for emotion, patterns in self.EMOTIONAL_VULNERABILITY_SIGNALS['text_patterns'].items():
                if any(re.search(p, searches) for p in patterns):
                    detected_emotions.append(emotion)

        if behavior.get('session_length_minutes', 0) > 60:
            detected_emotions.append('escapism')

        if behavior.get('time_hour') and (behavior['time_hour'] >= 23 or behavior['time_hour'] < 5):
            detected_emotions.append('loneliness')

        if not detected_emotions:
            return result

        result['emotional_state'] = detected_emotions

        # Check if content targets these emotions
        content_text = content.get('text', '').lower()

        # Emotional intensity patterns
        intensity_patterns = {
            'sadness': [r'feel better', r'cheer up', r'you deserve', r'treat yourself'],
            'loneliness': [r'connect', r'community', r'join', r'you\'re not alone', r'find (friends|love)'],
            'anxiety': [r'peace of mind', r'protection', r'security', r'don\'t worry', r'safe'],
            'boredom': [r'exciting', r'new', r'adventure', r'discover', r'experience'],
            'excitement': [r'now', r'act', r'limited', r'special']  # Leverage excitement for impulse
        }

        for emotion in detected_emotions:
            if emotion in intensity_patterns:
                patterns = intensity_patterns[emotion]
                if any(re.search(p, content_text) for p in patterns):
                    result['targeted'] = True
                    result['content_targets_state'] = True
                    result['score'] = 0.4
                    break

        return result

    def record_decision(self, user_id: str):
        """Record a decision to track decision fatigue"""
        self.user_decision_count[user_id] += 1

    def reset_decision_count(self, user_id: str):
        """Reset decision count (e.g., after break or new day)"""
        self.user_decision_count[user_id] = 0

    def record_notification(self, user_id: str, timestamp: float, notification_type: str):
        """Record notification for timing analysis"""
        self.user_notification_history[user_id].append({
            'timestamp': timestamp,
            'type': notification_type
        })
        # Keep only last 100 notifications
        if len(self.user_notification_history[user_id]) > 100:
            self.user_notification_history[user_id] = self.user_notification_history[user_id][-100:]

    def _generate_recommendations(self, analysis: TimingIntensityAnalysis) -> List[str]:
        """Generate protective recommendations"""
        recommendations = []

        if analysis.circadian_intensity:
            recommendations.append(
                "CIRCADIAN: Avoid major decisions between 2-4 AM. "
                "Cognitive function is at its lowest."
            )

        if analysis.decision_fatigue_intensity:
            recommendations.append(
                "DECISION FATIGUE: You've made many decisions recently. "
                "Take a break before any purchases or commitments."
            )

        if analysis.notification_timing_suspicious:
            recommendations.append(
                "NOTIFICATION TIMING: Content was served shortly after a notification. "
                "Wait 5+ minutes after alerts before acting."
            )

        if analysis.emotional_state_intensity:
            recommendations.append(
                "EMOTIONAL STATE: Content appears tailored to your current emotional state. "
                "Delay decisions when feeling strong emotions."
            )

        if VulnerabilityWindow.LATE_NIGHT in analysis.vulnerability_windows_targeted:
            recommendations.append(
                "LATE NIGHT: Late-night decisions are often regretted. "
                "Add items to cart but purchase tomorrow."
            )

        return recommendations
```

---

## 3. TRUST LEVERAGE SEQUENCE DETECTOR

**Research Finding:** Trust is systematically built for later intensity using predictable foot-in-the-door sequences. Small requests → Medium → Large intensity.

```python
class TrustStage(Enum):
    INITIAL_CONTACT = "initial_contact"
    RAPPORT_BUILDING = "rapport_building"
    SMALL_REQUEST = "small_request"
    COMPLIANCE_TEST = "compliance_test"
    MEDIUM_REQUEST = "medium_request"
    COMMITMENT_LOCK = "commitment_lock"
    LARGE_REQUEST = "large_request"
    INTENSITY = "intensity"

@dataclass
class TrustSequenceAnalysis:
    """Analysis of trust leverage sequence"""
    current_stage: TrustStage = TrustStage.INITIAL_CONTACT
    stage_progression: List[TrustStage] = field(default_factory=list)
    progression_velocity: float = 0.0  # How fast moving through stages
    escalation_detected: bool = False
    reciprocity_triggers: int = 0
    commitment_locks: int = 0
    intensity_risk_score: float = 0.0
    predicted_next_move: str = ""
    time_in_current_stage: float = 0.0
    red_flags: List[str] = field(default_factory=list)

class TrustLeverageSequenceDetector:
    """
    Detects systematic trust building and leverage sequences.

    Research basis:
    - Foot-in-the-door: Small → Medium → Large requests
    - Reciprocity: Unsolicited gifts create obligation
    - Commitment: Prior agreements enable larger asks
    - Grooming patterns transfer to commercial contexts
    """

    # Interaction patterns for each stage
    STAGE_PATTERNS = {
        TrustStage.INITIAL_CONTACT: {
            'patterns': [
                r'(hi|hello|hey)', r'how are you', r'nice to meet',
                r'introduction', r'first time', r'new here'
            ],
            'request_size': 0,
            'typical_duration_hours': (0, 24)
        },
        TrustStage.RAPPORT_BUILDING: {
            'patterns': [
                r'i understand', r'me too', r'same here', r'i agree',
                r'great (point|question)', r'you\'re (right|smart)',
                r'tell me more', r'interesting', r'i (like|love) that'
            ],
            'request_size': 0,
            'typical_duration_hours': (24, 168)  # 1-7 days
        },
        TrustStage.SMALL_REQUEST: {
            'patterns': [
                r'quick (question|favor)', r'small (ask|favor)',
                r'just (one|a) (minute|thing)', r'could you (just|simply)',
                r'easy', r'simple', r'no big deal'
            ],
            'request_size': 1,
            'typical_duration_hours': (0, 48)
        },
        TrustStage.COMPLIANCE_TEST: {
            'patterns': [
                r'did you', r'have you', r'you said you would',
                r'remember when', r'you (promised|agreed)',
                r'following up'
            ],
            'request_size': 1,
            'typical_duration_hours': (24, 72)
        },
        TrustStage.MEDIUM_REQUEST: {
            'patterns': [
                r'another (favor|thing)', r'(also|additionally)',
                r'while you\'re at it', r'one more thing',
                r'need (your help|you to)', r'important (to me|matter)'
            ],
            'request_size': 2,
            'typical_duration_hours': (48, 168)
        },
        TrustStage.COMMITMENT_LOCK: {
            'patterns': [
                r'you (already|already\'ve)', r'come this far',
                r'invested', r'committed', r'promised',
                r'can\'t (stop|quit) now', r'sunk'
            ],
            'request_size': 2,
            'typical_duration_hours': (0, 48)
        },
        TrustStage.LARGE_REQUEST: {
            'patterns': [
                r'(big|huge|major) (favor|ask)', r'(really|truly) need',
                r'(significant|substantial)', r'(money|loan|invest)',
                r'access', r'credentials', r'(personal|private)'
            ],
            'request_size': 3,
            'typical_duration_hours': (72, 336)
        },
        TrustStage.INTENSITY: {
            'patterns': [
                r'(wire|transfer|send)', r'(urgent|immediately|now)',
                r'(don\'t tell|keep.*secret)', r'(trust me|believe me)',
                r'(only you|you\'re the only)', r'(owe|obligation)'
            ],
            'request_size': 3,
            'typical_duration_hours': (0, 24)
        }
    }

    # Reciprocity trigger patterns
    RECIPROCITY_TRIGGERS = [
        r'free (gift|trial|bonus)', r'complimentary', r'on (me|us)',
        r'no (strings|obligation)', r'my treat', r'i\'ll (cover|pay)',
        r'special.*for you', r'exclusive (access|offer)'
    ]

    # Commitment lock patterns
    COMMITMENT_LOCKS = [
        r'you (said|agreed|promised)', r'we (agreed|discussed)',
        r'remember (when|our)', r'your (word|commitment)',
        r'don\'t go back on', r'after (all|everything)'
    ]

    # Red flag patterns (influence indicators)
    RED_FLAGS = {
        'rushed_progression': 'Moving through trust stages unusually fast',
        'premature_large_request': 'Large request before sufficient rapport',
        'guilt_influence': 'Using guilt to enforce compliance',
        'isolation_attempts': 'Trying to isolate from other relationships/advice',
        'secrecy_demands': 'Requesting secrecy about the relationship/transactions',
        'boundary_violations': 'Pushing past stated limits',
        'love_bombing': 'Excessive flattery and attention early on'
    }

    def __init__(self):
        self.interaction_history = defaultdict(list)
        self.stage_history = defaultdict(list)

    def analyze_interaction(
        self,
        interaction: Dict,
        user_id: str,
        counterpart_id: str
    ) -> TrustSequenceAnalysis:
        """
        Analyze interaction for trust leverage patterns.

        Expected interaction:
        {
            'content': str,
            'timestamp': float,
            'sender': str,  # Who sent this
            'contains_request': bool,
            'request_magnitude': int  # 0-3
        }
        """
        analysis = TrustSequenceAnalysis()

        # Store interaction
        relationship_key = f"{user_id}:{counterpart_id}"
        self.interaction_history[relationship_key].append(interaction)

        history = self.interaction_history[relationship_key]
        content = interaction.get('content', '').lower()

        # Detect current stage
        stage_scores = self._score_stages(history)
        analysis.current_stage = max(stage_scores, key=stage_scores.get)

        # Track stage progression
        if self.stage_history[relationship_key]:
            previous_stage = self.stage_history[relationship_key][-1]['stage']
            if analysis.current_stage != previous_stage:
                analysis.stage_progression = [
                    h['stage'] for h in self.stage_history[relationship_key]
                ] + [analysis.current_stage]

        self.stage_history[relationship_key].append({
            'stage': analysis.current_stage,
            'timestamp': interaction['timestamp']
        })

        # Calculate progression velocity
        analysis.progression_velocity = self._calculate_velocity(relationship_key)

        # Count reciprocity triggers
        for pattern in self.RECIPROCITY_TRIGGERS:
            if re.search(pattern, content):
                analysis.reciprocity_triggers += 1

        # Count commitment locks
        for pattern in self.COMMITMENT_LOCKS:
            if re.search(pattern, content):
                analysis.commitment_locks += 1

        # Detect escalation
        analysis.escalation_detected = self._detect_escalation(history)

        # Check for red flags
        analysis.red_flags = self._check_red_flags(history, analysis)

        # Calculate intensity risk
        analysis.intensity_risk_score = self._calculate_risk(analysis)

        # Predict next move
        analysis.predicted_next_move = self._predict_next_move(analysis)

        # Time in current stage
        analysis.time_in_current_stage = self._time_in_stage(relationship_key)

        return analysis

    def _score_stages(self, history: List[Dict]) -> Dict[TrustStage, float]:
        """Score how much each stage matches current interaction pattern"""
        scores = {stage: 0.0 for stage in TrustStage}

        # Consider recent interactions more heavily
        recent = history[-5:] if len(history) >= 5 else history

        for interaction in recent:
            content = interaction.get('content', '').lower()

            for stage, data in self.STAGE_PATTERNS.items():
                matches = sum(
                    1 for pattern in data['patterns']
                    if re.search(pattern, content)
                )
                scores[stage] += matches

        return scores

    def _calculate_velocity(self, relationship_key: str) -> float:
        """Calculate how fast the relationship is progressing through stages"""
        history = self.stage_history.get(relationship_key, [])

        if len(history) < 2:
            return 0.0

        # Count stage transitions
        transitions = 0
        for i in range(1, len(history)):
            if history[i]['stage'] != history[i-1]['stage']:
                transitions += 1

        # Time span
        time_span = history[-1]['timestamp'] - history[0]['timestamp']
        hours = time_span / 3600 if time_span > 0 else 1

        # Transitions per hour (normalized)
        velocity = transitions / hours

        # High velocity is suspicious (typical grooming is 0.01-0.05 transitions/hour)
        # Scams move faster (0.1-0.5 transitions/hour)
        return min(1.0, velocity * 5)

    def _detect_escalation(self, history: List[Dict]) -> bool:
        """Detect if requests are escalating in magnitude"""
        requests = [
            h.get('request_magnitude', 0)
            for h in history
            if h.get('contains_request')
        ]

        if len(requests) < 2:
            return False

        # Check if generally increasing
        increases = sum(1 for i in range(1, len(requests)) if requests[i] > requests[i-1])
        return increases >= len(requests) // 2

    def _check_red_flags(self, history: List[Dict], analysis: TrustSequenceAnalysis) -> List[str]:
        """Check for influence red flags"""
        flags = []

        # Rushed progression
        if analysis.progression_velocity > 0.3:
            flags.append(self.RED_FLAGS['rushed_progression'])

        # Premature large request
        stage_order = list(TrustStage)
        current_index = stage_order.index(analysis.current_stage)

        if analysis.current_stage in [TrustStage.LARGE_REQUEST, TrustStage.INTENSITY]:
            # Check if rapport stages were skipped
            rapport_interactions = sum(
                1 for h in history
                if any(re.search(p, h.get('content', '').lower())
                      for p in self.STAGE_PATTERNS[TrustStage.RAPPORT_BUILDING]['patterns'])
            )
            if rapport_interactions < 3:
                flags.append(self.RED_FLAGS['premature_large_request'])

        # Guilt influence
        guilt_patterns = [r'after (all|everything)', r'disappoint', r'let.*down', r'i thought']
        recent_content = ' '.join(h.get('content', '') for h in history[-3:]).lower()
        if any(re.search(p, recent_content) for p in guilt_patterns):
            flags.append(self.RED_FLAGS['guilt_influence'])

        # Secrecy demands
        secrecy_patterns = [r'don\'t tell', r'between us', r'secret', r'private']
        if any(re.search(p, recent_content) for p in secrecy_patterns):
            flags.append(self.RED_FLAGS['secrecy_demands'])

        # Love bombing (excessive early flattery)
        if len(history) <= 5:
            flattery_patterns = [r'amazing', r'incredible', r'perfect', r'best', r'love', r'special']
            flattery_count = sum(
                1 for h in history
                for p in flattery_patterns
                if re.search(p, h.get('content', '').lower())
            )
            if flattery_count > len(history) * 2:
                flags.append(self.RED_FLAGS['love_bombing'])

        return flags

    def _calculate_risk(self, analysis: TrustSequenceAnalysis) -> float:
        """Calculate overall intensity risk score"""
        risk = 0.0

        # Stage risk (later stages = higher risk)
        stage_risks = {
            TrustStage.INITIAL_CONTACT: 0.0,
            TrustStage.RAPPORT_BUILDING: 0.05,
            TrustStage.SMALL_REQUEST: 0.1,
            TrustStage.COMPLIANCE_TEST: 0.2,
            TrustStage.MEDIUM_REQUEST: 0.3,
            TrustStage.COMMITMENT_LOCK: 0.5,
            TrustStage.LARGE_REQUEST: 0.7,
            TrustStage.INTENSITY: 0.9
        }
        risk += stage_risks.get(analysis.current_stage, 0)

        # Velocity risk
        risk += analysis.progression_velocity * 0.3

        # Escalation risk
        if analysis.escalation_detected:
            risk += 0.2

        # Red flag risk
        risk += len(analysis.red_flags) * 0.1

        # Reciprocity/commitment influence
        risk += min(0.2, analysis.reciprocity_triggers * 0.05)
        risk += min(0.2, analysis.commitment_locks * 0.05)

        return min(1.0, risk)

    def _predict_next_move(self, analysis: TrustSequenceAnalysis) -> str:
        """Predict the influencer's likely next move"""
        predictions = {
            TrustStage.INITIAL_CONTACT: "Expect rapport-building: compliments, agreement, shared interests",
            TrustStage.RAPPORT_BUILDING: "Expect small request: 'quick favor', 'simple question'",
            TrustStage.SMALL_REQUEST: "If complied: expect compliance test or medium request soon",
            TrustStage.COMPLIANCE_TEST: "Expect reminder of prior compliance to set up medium request",
            TrustStage.MEDIUM_REQUEST: "Expect commitment lock: 'you already invested' framing",
            TrustStage.COMMITMENT_LOCK: "Expect large request: money, credentials, or major favor",
            TrustStage.LARGE_REQUEST: "Expect urgency tactics if resisted; intensity if complied",
            TrustStage.INTENSITY: "Active intensity in progress - recommend disengagement"
        }
        return predictions.get(analysis.current_stage, "Unknown pattern")

    def _time_in_stage(self, relationship_key: str) -> float:
        """Calculate time spent in current stage"""
        history = self.stage_history.get(relationship_key, [])

        if len(history) < 2:
            return 0.0

        current_stage = history[-1]['stage']

        # Find when we entered this stage
        for i in range(len(history) - 2, -1, -1):
            if history[i]['stage'] != current_stage:
                return history[-1]['timestamp'] - history[i + 1]['timestamp']

        return history[-1]['timestamp'] - history[0]['timestamp']
```

---

## 4. PHYSIOLOGICAL BYPASSING DETECTOR

**Research Finding:** Content is designed to bypass conscious processing - rapid cuts reduce analytical engagement, ASMR reduces skepticism, emotional arousal impairs critical thinking.

```python
class BypassMechanism(Enum):
    RAPID_CUTS = "attention_fragmentation"
    ASMR_RELAXATION = "critical_faculty_reduction"
    EMOTIONAL_AROUSAL = "amygdala_hijack"
    COGNITIVE_OVERLOAD = "system1_forcing"
    FOCUSED_RHYTHM = "trance_induction"
    PERIPHERAL_ROUTE = "low_elaboration"
    PRIMING = "subconscious_activation"

@dataclass
class PhysiologicalBypassAnalysis:
    """Analysis of physiological bypassing techniques"""
    bypass_mechanisms: List[BypassMechanism] = field(default_factory=list)
    conscious_processing_reduction: float = 0.0  # 0-1, how much critical thinking is impaired
    emotional_hijack_score: float = 0.0
    attention_fragmentation_score: float = 0.0
    relaxation_intensity_score: float = 0.0
    combined_bypass_effectiveness: float = 0.0
    target_brain_systems: List[str] = field(default_factory=list)
    countermeasures: List[str] = field(default_factory=list)

class PhysiologicalBypassDetector:
    """
    Detects content designed to bypass conscious cognitive processing.

    Research basis:
    - Rapid cuts (2.5 sec) reduce conscious processing via alpha rhythm disruption
    - ASMR triggers relaxation → reduced critical faculty
    - Emotional arousal (pupil dilation >15%) correlates with reduced critical thinking
    - Cognitive overload forces System 1 (automatic) over System 2 (analytical)
    """

    # Thresholds from research
    THRESHOLDS = {
        'rapid_cut_seconds': 2.5,  # Below this = attention fragmentation
        'cut_burst_count': 5,       # Consecutive rapid cuts
        'emotional_word_density': 0.15,  # 15% emotional words = high arousal
        'cognitive_load_elements': 7,  # Miller's 7 +/- 2
        'focused_regularity_cv': 0.15,  # Coefficient of variation
    }

    # ASMR and relaxation triggers
    ASMR_TRIGGERS = {
        'audio': [
            'whisper', 'soft spoken', 'gentle', 'soothing', 'calming',
            'tapping', 'scratching', 'crinkling', 'brushing', 'rain',
            'white noise', 'ambient', 'meditation', 'relaxation'
        ],
        'visual': [
            'slow motion', 'flowing', 'smooth', 'gentle movements',
            'close up hands', 'repetitive motion', 'satisfying'
        ]
    }

    # High-arousal emotional words (from psychological research)
    AROUSAL_WORDS = {
        'high_negative': [
            'danger', 'attack', 'threat', 'kill', 'destroy', 'terror',
            'panic', 'emergency', 'crisis', 'disaster', 'catastrophe',
            'horrifying', 'shocking', 'outrageous', 'disgusting'
        ],
        'high_positive': [
            'amazing', 'incredible', 'unbelievable', 'explosive',
            'revolutionary', 'breakthrough', 'miraculous', 'stunning',
            'thrilling', 'ecstatic', 'euphoric'
        ],
        'fear_specific': [
            'lose', 'miss', 'fail', 'risk', 'vulnerable', 'exposed',
            'unsafe', 'unprotected', 'deadline', 'expire', 'last chance'
        ],
        'anger_specific': [
            'unfair', 'cheated', 'lied', 'betrayed', 'corrupt',
            'scam', 'fraud', 'exploit', 'abuse', 'victim'
        ]
    }

    # Cognitive overload indicators
    OVERLOAD_INDICATORS = [
        'multiple_comparisons', 'excessive_features', 'complex_pricing',
        'many_options', 'dense_text', 'competing_visuals', 'rapid_information',
        'technical_jargon', 'fine_print', 'asterisks'
    ]

    def analyze_content(self, content: Dict) -> PhysiologicalBypassAnalysis:
        """
        Analyze content for physiological bypassing techniques.

        Expected content:
        {
            'text': str,
            'video_cuts': List[float],  # Timestamps of cuts
            'video_duration': float,
            'audio_features': Dict,
            'ui_elements': List[str],
            'visual_elements': List[str],
            'timing_pattern': List[float]  # Intervals between elements
        }
        """
        analysis = PhysiologicalBypassAnalysis()

        # 1. Analyze attention fragmentation (rapid cuts)
        if 'video_cuts' in content:
            fragmentation = self._analyze_attention_fragmentation(
                content['video_cuts'],
                content.get('video_duration', 0)
            )
            if fragmentation['detected']:
                analysis.bypass_mechanisms.append(BypassMechanism.RAPID_CUTS)
                analysis.attention_fragmentation_score = fragmentation['score']
                analysis.target_brain_systems.append('prefrontal_cortex_disruption')

        # 2. Analyze ASMR/relaxation intensity
        relaxation = self._analyze_relaxation_intensity(content)
        if relaxation['detected']:
            analysis.bypass_mechanisms.append(BypassMechanism.ASMR_RELAXATION)
            analysis.relaxation_intensity_score = relaxation['score']
            analysis.target_brain_systems.append('parasympathetic_activation')

        # 3. Analyze emotional arousal (amygdala hijack)
        emotional = self._analyze_emotional_arousal(content.get('text', ''))
        if emotional['hijack_potential'] > 0.3:
            analysis.bypass_mechanisms.append(BypassMechanism.EMOTIONAL_AROUSAL)
            analysis.emotional_hijack_score = emotional['hijack_potential']
            analysis.target_brain_systems.append('amygdala_activation')

        # 4. Analyze cognitive overload
        overload = self._analyze_cognitive_overload(content)
        if overload['detected']:
            analysis.bypass_mechanisms.append(BypassMechanism.COGNITIVE_OVERLOAD)
            analysis.target_brain_systems.append('working_memory_saturation')

        # 5. Analyze focused-engagement rhythm patterns
        if 'timing_pattern' in content:
            focused = self._analyze_focused_patterns(content['timing_pattern'])
            if focused['detected']:
                analysis.bypass_mechanisms.append(BypassMechanism.FOCUSED_RHYTHM)
                analysis.target_brain_systems.append('alpha_rhythm_entrainment')

        # 6. Calculate conscious processing reduction
        analysis.conscious_processing_reduction = self._calculate_processing_reduction(analysis)

        # 7. Calculate combined bypass effectiveness
        analysis.combined_bypass_effectiveness = self._calculate_combined_effectiveness(analysis)

        # 8. Generate countermeasures
        analysis.countermeasures = self._generate_countermeasures(analysis)

        return analysis

    def _analyze_attention_fragmentation(self, cuts: List[float], duration: float) -> Dict:
        """Analyze video cuts for attention fragmentation"""
        result = {
            'detected': False,
            'score': 0.0,
            'avg_shot_length': 0.0,
            'rapid_cut_sequences': 0
        }

        if len(cuts) < 2:
            return result

        intervals = np.diff(cuts)
        result['avg_shot_length'] = float(np.mean(intervals))

        # Count rapid cuts
        rapid_cuts = intervals < self.THRESHOLDS['rapid_cut_seconds']

        # Find burst sequences
        burst_count = 0
        current_burst = 0
        for is_rapid in rapid_cuts:
            if is_rapid:
                current_burst += 1
            else:
                if current_burst >= self.THRESHOLDS['cut_burst_count']:
                    burst_count += 1
                current_burst = 0

        if current_burst >= self.THRESHOLDS['cut_burst_count']:
            burst_count += 1

        result['rapid_cut_sequences'] = burst_count

        # Calculate score
        if result['avg_shot_length'] < self.THRESHOLDS['rapid_cut_seconds']:
            result['detected'] = True
            result['score'] = min(1.0,
                (self.THRESHOLDS['rapid_cut_seconds'] - result['avg_shot_length']) /
                self.THRESHOLDS['rapid_cut_seconds'] +
                burst_count * 0.2
            )

        return result

    def _analyze_relaxation_intensity(self, content: Dict) -> Dict:
        """Analyze for ASMR and relaxation influence"""
        result = {'detected': False, 'score': 0.0, 'triggers': []}

        text = content.get('text', '').lower()
        audio = content.get('audio_features', {})
        visual = content.get('visual_elements', [])

        # Check audio triggers
        for trigger in self.ASMR_TRIGGERS['audio']:
            if trigger in text or trigger in str(audio):
                result['triggers'].append(f"audio:{trigger}")

        # Check visual triggers
        visual_lower = [v.lower() for v in visual]
        for trigger in self.ASMR_TRIGGERS['visual']:
            if any(trigger in v for v in visual_lower):
                result['triggers'].append(f"visual:{trigger}")

        # Check audio properties
        if audio.get('whisper_segments', 0) > 0:
            result['triggers'].append('whisper_detected')

        if audio.get('tempo_bpm', 80) < 60:  # Very slow tempo
            result['triggers'].append('slow_tempo')

        if len(result['triggers']) >= 2:
            result['detected'] = True
            result['score'] = min(1.0, len(result['triggers']) * 0.2)

        return result

    def _analyze_emotional_arousal(self, text: str) -> Dict:
        """Analyze text for emotional arousal potential"""
        result = {
            'hijack_potential': 0.0,
            'dominant_emotion': None,
            'arousal_word_density': 0.0,
            'valence': 'neutral'
        }

        if not text:
            return result

        text_lower = text.lower()
        words = text_lower.split()
        total_words = len(words)

        if total_words == 0:
            return result

        emotion_counts = {
            'high_negative': 0,
            'high_positive': 0,
            'fear': 0,
            'anger': 0
        }

        for word in words:
            for category, patterns in self.AROUSAL_WORDS.items():
                if word in patterns or any(p in word for p in patterns):
                    if category == 'fear_specific':
                        emotion_counts['fear'] += 1
                    elif category == 'anger_specific':
                        emotion_counts['anger'] += 1
                    elif category == 'high_negative':
                        emotion_counts['high_negative'] += 1
                    else:
                        emotion_counts['high_positive'] += 1

        total_arousal_words = sum(emotion_counts.values())
        result['arousal_word_density'] = total_arousal_words / total_words

        # Determine dominant emotion
        if emotion_counts:
            result['dominant_emotion'] = max(emotion_counts, key=emotion_counts.get)

        # Calculate hijack potential
        # High density of arousal words = high hijack potential
        if result['arousal_word_density'] > self.THRESHOLDS['emotional_word_density']:
            result['hijack_potential'] = min(1.0, result['arousal_word_density'] * 4)

        # Fear and anger are most hijacking
        fear_anger_ratio = (emotion_counts['fear'] + emotion_counts['anger']) / max(1, total_arousal_words)
        result['hijack_potential'] = min(1.0, result['hijack_potential'] + fear_anger_ratio * 0.3)

        # Determine valence
        negative = emotion_counts['high_negative'] + emotion_counts['fear'] + emotion_counts['anger']
        positive = emotion_counts['high_positive']
        result['valence'] = 'negative' if negative > positive else ('positive' if positive > negative else 'neutral')

        return result

    def _analyze_cognitive_overload(self, content: Dict) -> Dict:
        """Analyze for cognitive overload influence"""
        result = {'detected': False, 'score': 0.0, 'overload_elements': []}

        ui_elements = content.get('ui_elements', [])
        text = content.get('text', '')

        # Count overload indicators
        for indicator in self.OVERLOAD_INDICATORS:
            if indicator in str(ui_elements).lower():
                result['overload_elements'].append(indicator)

        # Check for excessive options
        option_patterns = [r'\d+\s*(options|choices|plans|packages)', r'compare', r'vs\.?']
        for pattern in option_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                result['overload_elements'].append('excessive_comparison')

        # Check for dense information
        if text:
            # Word density proxy
            sentences = text.split('.')
            words = text.split()
            if sentences and len(words) / len(sentences) > 25:  # Very long sentences
                result['overload_elements'].append('dense_text')

            # Number density (prices, stats overwhelm)
            numbers = re.findall(r'\d+', text)
            if len(numbers) > 10:
                result['overload_elements'].append('number_overload')

        if len(result['overload_elements']) >= 3:
            result['detected'] = True
            result['score'] = min(1.0, len(result['overload_elements']) * 0.15)

        return result

    def _analyze_focused_patterns(self, timing_pattern: List[float]) -> Dict:
        """Analyze for focused-engagement regularity in content timing"""
        result = {'detected': False, 'score': 0.0, 'regularity': 0.0}

        if len(timing_pattern) < 5:
            return result

        # Calculate coefficient of variation
        mean_interval = np.mean(timing_pattern)
        std_interval = np.std(timing_pattern)

        if mean_interval > 0:
            cv = std_interval / mean_interval
            result['regularity'] = 1 - min(1, cv)

            if cv < self.THRESHOLDS['focused_regularity_cv']:
                result['detected'] = True
                result['score'] = result['regularity']

        return result

    def _calculate_processing_reduction(self, analysis: PhysiologicalBypassAnalysis) -> float:
        """Calculate overall reduction in conscious processing"""
        reduction = 0.0

        # Each bypass mechanism contributes
        mechanism_weights = {
            BypassMechanism.RAPID_CUTS: analysis.attention_fragmentation_score * 0.3,
            BypassMechanism.ASMR_RELAXATION: analysis.relaxation_intensity_score * 0.25,
            BypassMechanism.EMOTIONAL_AROUSAL: analysis.emotional_hijack_score * 0.35,
            BypassMechanism.COGNITIVE_OVERLOAD: 0.25,
            BypassMechanism.FOCUSED_RHYTHM: 0.2,
        }

        for mechanism in analysis.bypass_mechanisms:
            reduction += mechanism_weights.get(mechanism, 0.1)

        return min(1.0, reduction)

    def _calculate_combined_effectiveness(self, analysis: PhysiologicalBypassAnalysis) -> float:
        """Calculate combined bypass effectiveness with synergies"""
        base = analysis.conscious_processing_reduction

        # Synergies between bypass mechanisms
        mechanisms = set(analysis.bypass_mechanisms)

        # ASMR + emotional content = very effective
        if {BypassMechanism.ASMR_RELAXATION, BypassMechanism.EMOTIONAL_AROUSAL}.issubset(mechanisms):
            base *= 1.3

        # Rapid cuts + cognitive overload = overwhelming
        if {BypassMechanism.RAPID_CUTS, BypassMechanism.COGNITIVE_OVERLOAD}.issubset(mechanisms):
            base *= 1.25

        # Focused-engagement + relaxation = trance state
        if {BypassMechanism.FOCUSED_RHYTHM, BypassMechanism.ASMR_RELAXATION}.issubset(mechanisms):
            base *= 1.35

        return min(1.0, base)

    def _generate_countermeasures(self, analysis: PhysiologicalBypassAnalysis) -> List[str]:
        """Generate countermeasures for detected bypass attempts"""
        countermeasures = []

        if BypassMechanism.RAPID_CUTS in analysis.bypass_mechanisms:
            countermeasures.append(
                "ATTENTION FRAGMENTATION: Pause video. Read text instead. "
                "Rapid cuts are designed to prevent analytical thinking."
            )

        if BypassMechanism.ASMR_RELAXATION in analysis.bypass_mechanisms:
            countermeasures.append(
                "RELAXATION INTENSITY: Be aware you're in a reduced-vigilance state."
                "Delay any decisions until fully alert."
            )

        if BypassMechanism.EMOTIONAL_AROUSAL in analysis.bypass_mechanisms:
            countermeasures.append(
                "EMOTIONAL HIJACK: Strong emotions detected in content. "
                "Wait until emotional state normalizes before acting."
            )

        if BypassMechanism.COGNITIVE_OVERLOAD in analysis.bypass_mechanisms:
            countermeasures.append(
                "COGNITIVE OVERLOAD: Too much information at once. "
                "Focus on one factor at a time. Write down key points."
            )

        if BypassMechanism.FOCUSED_RHYTHM in analysis.bypass_mechanisms:
            countermeasures.append(
                "FOCUSED-ENGAGEMENT PATTERN: Highly regular rhythm detected. "
                "Look away periodically. Vary your attention deliberately."
            )

        return countermeasures
```

---

## 5. AI AMPLIFICATION DETECTOR

**Research Finding:** AI enables mass personalization with 81.7% higher persuasion. Increased AI persuasiveness correlates with DECREASED factual accuracy. Bot networks create false social proof with 76% detection failure.

```python
class AIAmplificationType(Enum):
    LLM_PERSONALIZATION = "personalized_persuasion"
    SYNTHETIC_SOCIAL_PROOF = "fake_engagement"
    BOT_COORDINATION = "coordinated_inauthentic"
    DEEPFAKE_AUTHORITY = "synthetic_credibility"
    ALGORITHMIC_TARGETING = "vulnerability_targeting"
    CONTENT_GENERATION = "ai_generated_content"
    SENTIMENT_INFLUENCE = "emotion_optimization"

@dataclass
class AIAmplificationAnalysis:
    """Analysis of AI-enabled influence amplification"""
    amplification_types: List[AIAmplificationType] = field(default_factory=list)
    personalization_level: float = 0.0  # 0-1, how personalized
    synthetic_engagement_probability: float = 0.0
    bot_coordination_score: float = 0.0
    ai_content_probability: float = 0.0
    targeting_precision: float = 0.0
    overall_amplification_factor: float = 1.0  # Multiplier on base influence
    factual_accuracy_concern: float = 0.0  # Higher = more concern about accuracy
    authenticity_score: float = 1.0  # 0-1, 1 = authentic

class AIAmplificationDetector:
    """
    Detects AI-enabled influence amplification.

    Research basis:
    - GPT-4 + personal info: 81.7% higher persuasion success
    - Increased AI persuasiveness correlates with decreased accuracy
    - Bot networks: 50%+ internet traffic, 76% detection failure
    - Deepfakes: Best detection only 75% accurate
    """

    # AI-generated text markers (from research)
    AI_TEXT_MARKERS = {
        'structural': [
            r'(firstly|secondly|thirdly|finally)',
            r'(in conclusion|to summarize|in summary)',
            r'(it\'s (important|worth) (to note|noting))',
            r'(furthermore|moreover|additionally|consequently)',
            r'(on the other hand|however|nevertheless)'
        ],
        'hedging': [
            r'(it (could|might|may) be (said|argued))',
            r'(some (people|experts|studies) (suggest|argue))',
            r'(there is (evidence|reason) to (believe|suggest))',
            r'(this (suggests|indicates|implies))'
        ],
        'formulaic': [
            r'(let me|allow me to) (explain|clarify)',
            r'(that being said|that said)',
            r'(it goes without saying)',
            r'(at the end of the day)'
        ]
    }

    # Bot behavior signatures
    BOT_SIGNATURES = {
        'timing': {
            'instant_response': 2,  # Seconds - faster than human
            'regular_intervals': 0.1,  # CV threshold for suspicious regularity
            '24_7_activity': 0.9  # Activity across all hours
        },
        'content': {
            'repetition_threshold': 0.7,  # Similarity between posts
            'template_patterns': [
                r'(wow|amazing|great|love) (this|it)',
                r'(check out|visit|click) (my|this)',
                r'(follow|subscribe|like) for more'
            ]
        },
        'network': {
            'follow_ratio_suspicious': 0.01,  # Very low followers/following
            'burst_activity': 10  # Posts per minute threshold
        }
    }

    # Personalization indicators
    PERSONALIZATION_MARKERS = [
        r'(based on|because of) your (interests|history|preferences|activity)',
        r'(just|especially|picked) for you',
        r'(you might|you\'ll) (like|love|enjoy)',
        r'(people like you|users in your area)',
        r'(your personalized|customized for you)'
    ]

    def analyze_content(self, content: Dict, engagement_data: Dict = None) -> AIAmplificationAnalysis:
        """
        Analyze content for AI amplification.

        Expected content:
        {
            'text': str,
            'source': str,
            'timestamp': float,
            'engagement': {'likes': int, 'comments': int, 'shares': int},
            'author_history': List[Dict],
            'related_posts': List[Dict]
        }
        """
        analysis = AIAmplificationAnalysis()

        text = content.get('text', '')

        # 1. Detect AI-generated content
        ai_content = self._detect_ai_generation(text)
        if ai_content['probability'] > 0.4:
            analysis.amplification_types.append(AIAmplificationType.CONTENT_GENERATION)
            analysis.ai_content_probability = ai_content['probability']

        # 2. Detect personalization level
        personalization = self._detect_personalization(content)
        if personalization['level'] > 0.3:
            analysis.amplification_types.append(AIAmplificationType.LLM_PERSONALIZATION)
            analysis.personalization_level = personalization['level']

        # 3. Detect synthetic engagement
        if engagement_data:
            synthetic = self._detect_synthetic_engagement(engagement_data)
            if synthetic['probability'] > 0.3:
                analysis.amplification_types.append(AIAmplificationType.SYNTHETIC_SOCIAL_PROOF)
                analysis.synthetic_engagement_probability = synthetic['probability']

        # 4. Detect bot coordination
        if content.get('related_posts'):
            coordination = self._detect_bot_coordination(content['related_posts'])
            if coordination['score'] > 0.4:
                analysis.amplification_types.append(AIAmplificationType.BOT_COORDINATION)
                analysis.bot_coordination_score = coordination['score']

        # 5. Detect algorithmic targeting
        if content.get('delivery_metadata'):
            targeting = self._detect_algorithmic_targeting(content['delivery_metadata'])
            if targeting['precision'] > 0.5:
                analysis.amplification_types.append(AIAmplificationType.ALGORITHMIC_TARGETING)
                analysis.targeting_precision = targeting['precision']

        # 6. Calculate overall amplification factor
        analysis.overall_amplification_factor = self._calculate_amplification(analysis)

        # 7. Assess factual accuracy concern
        # Research: AI persuasiveness inversely correlates with accuracy
        analysis.factual_accuracy_concern = self._assess_accuracy_concern(analysis)

        # 8. Calculate authenticity score
        analysis.authenticity_score = 1 - (
            analysis.ai_content_probability * 0.3 +
            analysis.synthetic_engagement_probability * 0.3 +
            analysis.bot_coordination_score * 0.2 +
            (1 - analysis.targeting_precision) * 0.2
        )

        return analysis

    def _detect_ai_generation(self, text: str) -> Dict:
        """Detect AI-generated text"""
        result = {'probability': 0.0, 'markers_found': []}

        if not text:
            return result

        text_lower = text.lower()
        marker_count = 0

        for category, patterns in self.AI_TEXT_MARKERS.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    marker_count += 1
                    result['markers_found'].append(f"{category}:{pattern}")

        # Normalize by text length
        word_count = len(text.split())
        if word_count > 0:
            marker_density = marker_count / (word_count / 100)
            result['probability'] = min(1.0, marker_density * 0.3)

        return result

    def _detect_personalization(self, content: Dict) -> Dict:
        """Detect content personalization level"""
        result = {'level': 0.0, 'indicators': []}

        text = content.get('text', '').lower()

        for pattern in self.PERSONALIZATION_MARKERS:
            if re.search(pattern, text):
                result['indicators'].append(pattern)

        # Check metadata for personalization signals
        metadata = content.get('metadata', {})
        if metadata.get('personalized'):
            result['indicators'].append('metadata_personalized_flag')

        if metadata.get('recommendation_engine'):
            result['indicators'].append('recommendation_engine')

        result['level'] = min(1.0, len(result['indicators']) * 0.25)

        return result

    def _detect_synthetic_engagement(self, engagement: Dict) -> Dict:
        """Detect fake/bot engagement"""
        result = {'probability': 0.0, 'anomalies': []}

        likes = engagement.get('likes', 0)
        comments = engagement.get('comments', 0)
        shares = engagement.get('shares', 0)
        views = engagement.get('views', 1)

        # Anomaly: High likes, low comments (bots don't write comments)
        if comments > 0:
            like_comment_ratio = likes / comments
            if like_comment_ratio > 100:  # Suspicious ratio
                result['anomalies'].append('high_like_comment_ratio')
                result['probability'] += 0.3

        # Anomaly: Engagement spike patterns
        engagement_history = engagement.get('history', [])
        if engagement_history:
            # Check for sudden spikes
            values = [e.get('count', 0) for e in engagement_history]
            if len(values) > 3:
                avg = np.mean(values[:-1])
                if values[-1] > avg * 5:  # 5x spike
                    result['anomalies'].append('engagement_spike')
                    result['probability'] += 0.3

        # Anomaly: Engagement timing (clustered = coordinated)
        comment_times = engagement.get('comment_timestamps', [])
        if len(comment_times) > 10:
            intervals = np.diff(sorted(comment_times))
            cv = np.std(intervals) / np.mean(intervals) if np.mean(intervals) > 0 else 1

            if cv < 0.3:  # Too regular
                result['anomalies'].append('regular_engagement_timing')
                result['probability'] += 0.25

        result['probability'] = min(1.0, result['probability'])
        return result

    def _detect_bot_coordination(self, posts: List[Dict]) -> Dict:
        """Detect coordinated bot activity"""
        result = {'score': 0.0, 'indicators': []}

        if len(posts) < 3:
            return result

        # Check content similarity
        contents = [p.get('text', '') for p in posts]
        similarity_scores = []

        for i in range(len(contents)):
            for j in range(i + 1, len(contents)):
                sim = self._text_similarity(contents[i], contents[j])
                similarity_scores.append(sim)

        if similarity_scores:
            avg_similarity = np.mean(similarity_scores)
            if avg_similarity > self.BOT_SIGNATURES['content']['repetition_threshold']:
                result['indicators'].append('high_content_similarity')
                result['score'] += 0.4

        # Check timing coordination
        timestamps = [p.get('timestamp', 0) for p in posts if p.get('timestamp')]
        if len(timestamps) > 3:
            sorted_times = sorted(timestamps)
            intervals = np.diff(sorted_times)

            if len(intervals) > 2:
                cv = np.std(intervals) / np.mean(intervals) if np.mean(intervals) > 0 else 1
                if cv < self.BOT_SIGNATURES['timing']['regular_intervals']:
                    result['indicators'].append('coordinated_timing')
                    result['score'] += 0.4

        # Check for template patterns
        all_text = ' '.join(contents).lower()
        for pattern in self.BOT_SIGNATURES['content']['template_patterns']:
            if re.search(pattern, all_text):
                result['indicators'].append(f'template_pattern:{pattern}')
                result['score'] += 0.15

        result['score'] = min(1.0, result['score'])
        return result

    def _detect_algorithmic_targeting(self, metadata: Dict) -> Dict:
        """Detect precision algorithmic targeting"""
        result = {'precision': 0.0, 'targeting_factors': []}

        targeting_signals = [
            'behavioral_targeting',
            'lookalike_audience',
            'interest_targeting',
            'demographic_targeting',
            'retargeting',
            'contextual_targeting',
            'predictive_targeting'
        ]

        for signal in targeting_signals:
            if metadata.get(signal):
                result['targeting_factors'].append(signal)

        # More targeting factors = higher precision
        result['precision'] = min(1.0, len(result['targeting_factors']) * 0.2)

        # Check for vulnerability targeting
        if any(t in str(metadata) for t in ['emotional_state', 'life_event', 'financial_distress']):
            result['targeting_factors'].append('vulnerability_targeting')
            result['precision'] = min(1.0, result['precision'] + 0.3)

        return result

    def _calculate_amplification(self, analysis: AIAmplificationAnalysis) -> float:
        """Calculate overall influence amplification factor"""
        base = 1.0

        # Personalization amplification (from research: 81.7% increase)
        if analysis.personalization_level > 0.5:
            base *= 1.0 + (0.817 * analysis.personalization_level)

        # Synthetic social proof amplification
        if analysis.synthetic_engagement_probability > 0.5:
            base *= 1.3

        # Bot coordination amplification
        if analysis.bot_coordination_score > 0.5:
            base *= 1.4

        # Algorithmic targeting amplification
        if analysis.targeting_precision > 0.5:
            base *= 1.25

        return base

    def _assess_accuracy_concern(self, analysis: AIAmplificationAnalysis) -> float:
        """Assess concern about factual accuracy (inverse correlation with persuasiveness)"""
        # Research shows more persuasive AI content is often less accurate
        concern = 0.0

        if analysis.ai_content_probability > 0.5:
            concern += 0.3

        if analysis.personalization_level > 0.7:
            concern += 0.25

        # High amplification = higher accuracy concern
        if analysis.overall_amplification_factor > 1.5:
            concern += 0.25

        return min(1.0, concern)

    def _text_similarity(self, text1: str, text2: str) -> float:
        """Simple word overlap similarity"""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())

        if not words1 or not words2:
            return 0.0

        intersection = len(words1 & words2)
        union = len(words1 | words2)

        return intersection / union if union > 0 else 0.0
```

---

## 6. RANKED INFLUENCE COMBINATION EFFECTIVENESS

**Research-Backed Ranking of Most Effective Technique Combinations**

```python
@dataclass
class CombinationEffectiveness:
    """Ranked effectiveness of influence combinations"""
    rank: int
    combination: Tuple[str, ...]
    effectiveness_multiplier: float
    mechanism: str
    target_vulnerability: str
    research_source: str
    detection_difficulty: float  # 0-1, higher = harder to detect
    typical_application: str

class RankedCombinationDetector:
    """
    Detects influence combinations ranked by proven effectiveness.

    Combinations ranked from most to least effective based on research.
    """

    # RANKED from most effective to least effective
    RANKED_COMBINATIONS: List[CombinationEffectiveness] = [
        # RANK 1-5: HIGHEST IMPACT COMBINATIONS
        CombinationEffectiveness(
            rank=1,
            combination=("emotional_arousal", "cognitive_overload", "urgency"),
            effectiveness_multiplier=2.1,
            mechanism="Emotional hijack + overwhelm + time pressure = complete bypass of analytical processing",
            target_vulnerability="Working memory saturation during stress response",
            research_source="Decision fatigue + amygdala hijack research",
            detection_difficulty=0.7,
            typical_application="High-pressure sales, crisis intensity, scam calls"
        ),
        CombinationEffectiveness(
            rank=2,
            combination=("authority", "fear", "urgency"),
            effectiveness_multiplier=1.95,
            mechanism="Credible threat + immediate action requirement = compliance without verification",
            target_vulnerability="Threat response overrides verification instinct",
            research_source="Phishing effectiveness studies, scam analysis",
            detection_difficulty=0.6,
            typical_application="Tech support scams, IRS scams, security alerts"
        ),
        CombinationEffectiveness(
            rank=3,
            combination=("variable_reward", "streak", "social_proof"),
            effectiveness_multiplier=1.85,
            mechanism="Gambling mechanics + loss aversion + peer validation = compulsive engagement",
            target_vulnerability="Dopamine reward pathway + social comparison",
            research_source="Gamification engagement research, mobile game studies",
            detection_difficulty=0.4,
            typical_application="Mobile games, social media, fitness apps"
        ),
        CombinationEffectiveness(
            rank=4,
            combination=("personalization", "scarcity", "social_proof"),
            effectiveness_multiplier=1.78,
            mechanism="Personal relevance + limited availability + others buying = FOMO + action",
            target_vulnerability="Identity + loss aversion + conformity",
            research_source="E-commerce conversion optimization studies",
            detection_difficulty=0.5,
            typical_application="E-commerce, flash sales, limited editions"
        ),
        CombinationEffectiveness(
            rank=5,
            combination=("trust_building", "reciprocity", "commitment_escalation"),
            effectiveness_multiplier=1.72,
            mechanism="Established relationship + gift obligation + prior compliance = large request acceptance",
            target_vulnerability="Reciprocity norm + consistency drive",
            research_source="Foot-in-the-door research, romance scam analysis",
            detection_difficulty=0.8,
            typical_application="Romance scams, business fraud, cult recruitment"
        ),

        # RANK 6-10: HIGH IMPACT COMBINATIONS
        CombinationEffectiveness(
            rank=6,
            combination=("infinite_scroll", "personalization", "variable_reward"),
            effectiveness_multiplier=1.65,
            mechanism="Endless content + relevance + unpredictable rewards = time distortion",
            target_vulnerability="Dopamine seeking + completion drive absence",
            research_source="Social media engagement research, CHI 2024",
            detection_difficulty=0.3,
            typical_application="Social media feeds, content platforms"
        ),
        CombinationEffectiveness(
            rank=7,
            combination=("anchoring", "decoy", "urgency"),
            effectiveness_multiplier=1.58,
            mechanism="Price reference + inferior comparison + time limit = target option selection",
            target_vulnerability="Reference point bias + comparison heuristic",
            research_source="Behavioral economics pricing studies",
            detection_difficulty=0.4,
            typical_application="Subscription pricing, SaaS plans, retail"
        ),
        CombinationEffectiveness(
            rank=8,
            combination=("authority", "social_proof", "personalization"),
            effectiveness_multiplier=1.52,
            mechanism="Expert endorsement + crowd validation + personal relevance = trust",
            target_vulnerability="Authority deference + conformity + relevance filter",
            research_source="Influencer marketing studies",
            detection_difficulty=0.5,
            typical_application="Health products, financial services, courses"
        ),
        CombinationEffectiveness(
            rank=9,
            combination=("fear", "scarcity", "loss_framing"),
            effectiveness_multiplier=1.48,
            mechanism="Threat awareness + limited opportunity + loss emphasis = action to avoid negative",
            target_vulnerability="Loss aversion (2x pain of loss vs gain)",
            research_source="Prospect theory applications",
            detection_difficulty=0.4,
            typical_application="Insurance, security products, limited offers"
        ),
        CombinationEffectiveness(
            rank=10,
            combination=("asmr_relaxation", "authority", "suggestion"),
            effectiveness_multiplier=1.45,
            mechanism="Reduced critical faculty + trusted source + direct suggestion = acceptance",
            target_vulnerability="Lowered analytical resistance in relaxed state",
            research_source="Focused engagement suggestion research, ASMR studies",
            detection_difficulty=0.7,
            typical_application="Guided meditations with product placement, wellness marketing"
        ),

        # RANK 11-15: MODERATE IMPACT COMBINATIONS
        CombinationEffectiveness(
            rank=11,
            combination=("guilt", "commitment", "reciprocity"),
            effectiveness_multiplier=1.42,
            mechanism="Emotional pressure + prior agreement + debt feeling = compliance",
            target_vulnerability="Guilt avoidance + consistency need",
            research_source="Donation and subscription retention studies",
            detection_difficulty=0.5,
            typical_application="Charity solicitation, subscription cancellation"
        ),
        CombinationEffectiveness(
            rank=12,
            combination=("scarcity", "social_proof"),
            effectiveness_multiplier=1.40,
            mechanism="Limited availability validated by crowd demand",
            target_vulnerability="FOMO + conformity",
            research_source="Cialdini combination studies",
            detection_difficulty=0.3,
            typical_application="Basic e-commerce, event tickets"
        ),
        CombinationEffectiveness(
            rank=13,
            combination=("liking", "reciprocity"),
            effectiveness_multiplier=1.35,
            mechanism="Positive relationship + gift = obligation from friend",
            target_vulnerability="Social bond + reciprocity norm",
            research_source="Influencer marketing, MLM research",
            detection_difficulty=0.6,
            typical_application="MLM, friend referrals, influencer affiliate"
        ),
        CombinationEffectiveness(
            rank=14,
            combination=("authority", "social_proof"),
            effectiveness_multiplier=1.32,
            mechanism="Expert endorsement + crowd validation",
            target_vulnerability="Dual verification heuristic",
            research_source="Advertising effectiveness studies",
            detection_difficulty=0.3,
            typical_application="Traditional advertising, product reviews"
        ),
        CombinationEffectiveness(
            rank=15,
            combination=("urgency", "scarcity"),
            effectiveness_multiplier=1.28,
            mechanism="Time + quantity limits",
            target_vulnerability="Fear of missing out",
            research_source="Basic FOMO research",
            detection_difficulty=0.2,
            typical_application="Flash sales, countdown timers"
        ),
    ]

    def detect_combinations(self, content: Dict) -> Dict:
        """
        Detect influence combinations and return ranked findings.
        """
        # First detect all individual techniques
        stacking_detector = SynergisticStackingDetector()
        techniques = stacking_detector.detect_techniques(content)
        technique_set = set(t.value for t in techniques)

        findings = {
            'combinations_detected': [],
            'highest_rank_detected': None,
            'total_effectiveness_multiplier': 1.0,
            'risk_assessment': 'low'
        }

        for combo in self.RANKED_COMBINATIONS:
            combo_set = set(combo.combination)

            # Check if combination is present
            if combo_set.issubset(technique_set):
                findings['combinations_detected'].append({
                    'rank': combo.rank,
                    'combination': combo.combination,
                    'multiplier': combo.effectiveness_multiplier,
                    'mechanism': combo.mechanism,
                    'typical_use': combo.typical_application,
                    'detection_difficulty': combo.detection_difficulty
                })

        # Sort by rank (most effective first)
        findings['combinations_detected'].sort(key=lambda x: x['rank'])

        if findings['combinations_detected']:
            findings['highest_rank_detected'] = findings['combinations_detected'][0]['rank']

            # Calculate combined multiplier (with diminishing returns)
            multipliers = [c['multiplier'] for c in findings['combinations_detected']]
            total = 1.0
            for i, m in enumerate(multipliers):
                total *= 1 + (m - 1) / (1 + i * 0.5)  # Diminishing returns

            findings['total_effectiveness_multiplier'] = total

            # Risk assessment
            if findings['highest_rank_detected'] <= 3:
                findings['risk_assessment'] = 'critical'
            elif findings['highest_rank_detected'] <= 7:
                findings['risk_assessment'] = 'high'
            elif findings['highest_rank_detected'] <= 12:
                findings['risk_assessment'] = 'medium'
            else:
                findings['risk_assessment'] = 'moderate'

        return findings

    def get_combination_by_rank(self, rank: int) -> Optional[CombinationEffectiveness]:
        """Get combination details by rank"""
        for combo in self.RANKED_COMBINATIONS:
            if combo.rank == rank:
                return combo
        return None

    def get_defenses_for_combination(self, rank: int) -> List[str]:
        """Get specific defenses for a ranked combination"""
        combo = self.get_combination_by_rank(rank)
        if not combo:
            return []

        defenses = {
            1: [
                "PAUSE: When feeling overwhelmed AND emotional AND pressured, this is the most dangerous combination",
                "BREAK PATTERN: Leave the situation physically or close the browser",
                "TIME BUFFER: Institute mandatory 24-hour delay for any decision",
                "COGNITIVE RESET: Do something requiring focus (math, reading) before deciding"
            ],
            2: [
                "VERIFY INDEPENDENTLY: Look up the organization's real contact number yourself",
                "AUTHORITY CHECK: Real authorities never demand immediate action",
                "CALLBACK: Hang up and call the official number you find independently",
                "TIME TEST: Legitimate issues can wait 24 hours for verification"
            ],
            3: [
                "STREAK IMMUNITY: Remember streaks are designed to leverage loss aversion",
                "SESSION LIMITS: Set hard time limits before opening apps",
                "SOCIAL COMPARISON OFF: Hide leaderboards and comparison features",
                "REWARD AWARENESS: Recognize variable rewards as slot machine psychology"
            ],
            4: [
                "PERSONALIZATION AWARENESS: 'For you' = targeted vulnerability",
                "ARTIFICIAL SCARCITY: Most 'limited' items restock",
                "SOCIAL PROOF CHECK: Reviews and numbers can be faked",
                "WISHLIST TEST: Add to wishlist, check if still 'limited' in a week"
            ],
            5: [
                "RELATIONSHIP PACING: Be suspicious of rapid intimacy building",
                "GIFT STRINGS: 'Free' gifts create obligations - decline or recognize",
                "ESCALATION AWARENESS: Notice when requests are growing",
                "OUTSIDE COUNSEL: Discuss major requests with uninvolved friends/family"
            ],
        }

        return defenses.get(rank, [
            "PAUSE before acting",
            "VERIFY claims independently",
            "DELAY decisions by 24 hours",
            "CONSULT someone not exposed to the same content"
        ])
```

---

## 7. TEMPORAL INTENSITY DETECTOR

**Research Finding:** Content is delivered at precise times when cognitive defenses are lowest. Circadian rhythm, decision fatigue, and emotional state all affect vulnerability.

```python
from datetime import datetime, timedelta
from typing import NamedTuple

class TemporalWindow(NamedTuple):
    """A vulnerability window with severity"""
    name: str
    hours: Tuple[int, int]  # Start, end hour
    severity: float  # 0-1
    mechanism: str
    research_basis: str

class TemporalIntensityDetector:
    """
    Detects temporal/timing-based influence intensity.

    Research basis:
    - 2-4 AM: Prefrontal cortex activity lowest, decisions 40%+ worse
    - Decision fatigue: After 10-15 decisions, compliance increases 35%
    - Post-notification: 0-5 minute elevated arousal window
    - Circadian rhythm affects risk tolerance, emotional regulation
    - Paycheck timing: Spending peaks immediately after payment
    """

    # Vulnerability windows ranked by severity
    VULNERABILITY_WINDOWS: List[TemporalWindow] = [
        TemporalWindow(
            name="deep_night_cognitive_low",
            hours=(2, 4),
            severity=0.9,
            mechanism="Prefrontal cortex activity at daily minimum. Analytical capacity severely impaired. Impulse control weakest.",
            research_basis="Circadian neuroscience: PFC activity nadir at 2-4 AM"
        ),
        TemporalWindow(
            name="late_night_fatigue",
            hours=(0, 2),
            severity=0.7,
            mechanism="Accumulated sleep pressure impairs executive function. Risk tolerance increases, self-control decreases.",
            research_basis="Sleep deprivation decision-making studies"
        ),
        TemporalWindow(
            name="early_morning_transition",
            hours=(4, 6),
            severity=0.6,
            mechanism="Cortisol awakening response. Emotional reactivity heightened. Analytical systems not yet fully online.",
            research_basis="Cortisol awakening response research"
        ),
        TemporalWindow(
            name="post_lunch_dip",
            hours=(14, 16),
            severity=0.4,
            mechanism="Postprandial glucose regulation affects cognition. Natural circadian alertness dip.",
            research_basis="Postprandial cognitive studies"
        ),
        TemporalWindow(
            name="end_of_workday",
            hours=(17, 19),
            severity=0.5,
            mechanism="Decision fatigue accumulated throughout day. Mental resources depleted.",
            research_basis="Judicial decision fatigue research"
        ),
        TemporalWindow(
            name="late_evening_impulsivity",
            hours=(22, 24),
            severity=0.55,
            mechanism="Self-regulation depletes over waking hours. Emotional purchases more likely.",
            research_basis="Ego depletion research, evening impulse buying studies"
        ),
    ]

    # Days with heightened vulnerability
    VULNERABLE_DAYS = {
        'payday_adjacent': {
            'days': [1, 14, 15, 28, 29, 30, 31],  # Common paycheck days
            'severity': 0.3,
            'mechanism': "Post-income spending impulse. Mental accounting of 'new money'."
        },
        'weekend': {
            'days_of_week': [5, 6],  # Saturday, Sunday
            'severity': 0.2,
            'mechanism': "Relaxed state, reduced vigilance. Leisure mindset more susceptible."
        },
        'monday': {
            'days_of_week': [0],
            'severity': 0.25,
            'mechanism': "Transition stress. Cognitive load from week planning."
        }
    }

    # Decision fatigue accumulation rates
    DECISION_FATIGUE_MODEL = {
        'decisions_per_minute_browsing': 2,  # Estimated micro-decisions during browsing
        'decisions_per_purchase_flow': 15,   # Typical checkout decisions
        'fatigue_onset_threshold': 7,        # Miller's 7 +/- 2
        'severe_fatigue_threshold': 20,
        'compliance_increase_at_fatigue': 0.35,  # 35% from research
    }

    # Notification timing intensity
    NOTIFICATION_WINDOWS = {
        'peak_arousal': (0, 30),      # Seconds post-notification
        'elevated_arousal': (30, 120),
        'residual_effect': (120, 300),
    }

    def __init__(self):
        self.user_decision_log = defaultdict(list)
        self.user_notification_log = defaultdict(list)
        self.user_session_start = {}

    def analyze_delivery_timing(
        self,
        timestamp: float,
        user_id: str = None,
        content_type: str = "general"
    ) -> Dict:
        """
        Analyze whether content delivery time leverages vulnerability windows.
        """
        analysis = {
            'timestamp': timestamp,
            'datetime': datetime.fromtimestamp(timestamp).isoformat(),
            'vulnerability_windows_active': [],
            'circadian_vulnerability': 0.0,
            'day_vulnerability': 0.0,
            'decision_fatigue_level': 0.0,
            'notification_intensity': False,
            'combined_temporal_risk': 0.0,
            'optimal_decision_time': False,
            'recommendations': []
        }

        dt = datetime.fromtimestamp(timestamp)
        hour = dt.hour
        day = dt.day
        weekday = dt.weekday()

        # 1. Check circadian vulnerability windows
        for window in self.VULNERABILITY_WINDOWS:
            start, end = window.hours
            if start <= hour < end:
                analysis['vulnerability_windows_active'].append({
                    'window': window.name,
                    'severity': window.severity,
                    'mechanism': window.mechanism
                })
                analysis['circadian_vulnerability'] = max(
                    analysis['circadian_vulnerability'],
                    window.severity
                )

        # 2. Check day-based vulnerability
        for vuln_type, config in self.VULNERABLE_DAYS.items():
            if 'days' in config and day in config['days']:
                analysis['day_vulnerability'] += config['severity']
                analysis['vulnerability_windows_active'].append({
                    'window': vuln_type,
                    'severity': config['severity'],
                    'mechanism': config['mechanism']
                })

            if 'days_of_week' in config and weekday in config['days_of_week']:
                analysis['day_vulnerability'] += config['severity']
                analysis['vulnerability_windows_active'].append({
                    'window': vuln_type,
                    'severity': config['severity'],
                    'mechanism': config['mechanism']
                })

        # 3. Check decision fatigue (if tracking user)
        if user_id:
            fatigue = self._calculate_decision_fatigue(user_id, timestamp)
            analysis['decision_fatigue_level'] = fatigue['level']

            if fatigue['level'] > 0.5:
                analysis['vulnerability_windows_active'].append({
                    'window': 'decision_fatigue',
                    'severity': fatigue['level'],
                    'mechanism': f"User has made approximately {fatigue['estimated_decisions']} decisions. Compliance increases {int(fatigue['compliance_boost']*100)}%."
                })

        # 4. Check notification timing intensity
        if user_id:
            notif_analysis = self._check_notification_timing(user_id, timestamp)
            if notif_analysis['within_window']:
                analysis['notification_intensity'] = True
                analysis['vulnerability_windows_active'].append({
                    'window': f"post_notification_{notif_analysis['window_type']}",
                    'severity': notif_analysis['severity'],
                    'mechanism': f"Content delivered {notif_analysis['seconds_since_notification']:.0f} seconds after notification during arousal window."
                })

        # 5. Calculate combined risk
        analysis['combined_temporal_risk'] = min(1.0,
            analysis['circadian_vulnerability'] * 0.4 +
            analysis['day_vulnerability'] * 0.2 +
            analysis['decision_fatigue_level'] * 0.25 +
            (0.15 if analysis['notification_intensity'] else 0)
        )

        # 6. Determine if this is optimal decision time
        if (analysis['circadian_vulnerability'] < 0.2 and
            analysis['decision_fatigue_level'] < 0.3 and
            9 <= hour <= 11):  # Mid-morning typically best
            analysis['optimal_decision_time'] = True

        # 7. Generate recommendations
        analysis['recommendations'] = self._generate_temporal_recommendations(analysis)

        return analysis

    def _calculate_decision_fatigue(self, user_id: str, current_time: float) -> Dict:
        """Calculate user's decision fatigue level"""
        result = {
            'level': 0.0,
            'estimated_decisions': 0,
            'compliance_boost': 0.0
        }

        # Get session start
        session_start = self.user_session_start.get(user_id)
        if not session_start:
            return result

        # Estimate decisions based on session duration
        session_minutes = (current_time - session_start) / 60

        # Add tracked decisions
        tracked = len([
            d for d in self.user_decision_log.get(user_id, [])
            if d > session_start
        ])

        # Estimate total (browsing generates many micro-decisions)
        estimated = tracked + int(session_minutes * self.DECISION_FATIGUE_MODEL['decisions_per_minute_browsing'])
        result['estimated_decisions'] = estimated

        # Calculate fatigue level
        if estimated > self.DECISION_FATIGUE_MODEL['severe_fatigue_threshold']:
            result['level'] = 0.8
        elif estimated > self.DECISION_FATIGUE_MODEL['fatigue_onset_threshold']:
            result['level'] = 0.3 + (estimated - 7) * 0.04
        else:
            result['level'] = estimated * 0.03

        result['level'] = min(1.0, result['level'])

        # Calculate compliance boost
        if result['level'] > 0.3:
            result['compliance_boost'] = result['level'] * self.DECISION_FATIGUE_MODEL['compliance_increase_at_fatigue']

        return result

    def _check_notification_timing(self, user_id: str, current_time: float) -> Dict:
        """Check if content follows notification (intensity window)"""
        result = {
            'within_window': False,
            'window_type': None,
            'seconds_since_notification': None,
            'severity': 0.0
        }

        notifications = self.user_notification_log.get(user_id, [])
        if not notifications:
            return result

        # Find most recent notification
        recent = max(notifications)
        diff = current_time - recent

        result['seconds_since_notification'] = diff

        # Check windows
        for window_name, (start, end) in self.NOTIFICATION_WINDOWS.items():
            if start <= diff <= end:
                result['within_window'] = True
                result['window_type'] = window_name

                # Severity based on window
                if window_name == 'peak_arousal':
                    result['severity'] = 0.6
                elif window_name == 'elevated_arousal':
                    result['severity'] = 0.4
                else:
                    result['severity'] = 0.2

                break

        return result

    def record_user_decision(self, user_id: str, timestamp: float):
        """Record a user decision point"""
        self.user_decision_log[user_id].append(timestamp)

    def record_notification(self, user_id: str, timestamp: float):
        """Record notification sent to user"""
        self.user_notification_log[user_id].append(timestamp)
        # Keep only recent
        if len(self.user_notification_log[user_id]) > 50:
            self.user_notification_log[user_id] = self.user_notification_log[user_id][-50:]

    def start_session(self, user_id: str, timestamp: float):
        """Mark session start for fatigue tracking"""
        self.user_session_start[user_id] = timestamp

    def get_optimal_decision_windows(self) -> List[Dict]:
        """Return optimal windows for important decisions"""
        return [
            {
                'window': '9-11 AM',
                'reason': 'Peak cortisol for alertness, pre-lunch optimal glucose, minimal decision fatigue',
                'best_for': 'Complex analytical decisions, major purchases, contract reviews'
            },
            {
                'window': '10 AM (mid-morning)',
                'reason': 'Generally considered peak cognitive performance time',
                'best_for': 'Any important decision'
            },
            {
                'window': 'After rest break (15+ minutes)',
                'reason': 'Cognitive resources restored, decision fatigue reduced',
                'best_for': 'Decisions that follow prolonged activity'
            }
        ]

    def _generate_temporal_recommendations(self, analysis: Dict) -> List[str]:
        """Generate timing-specific recommendations"""
        recommendations = []

        if analysis['circadian_vulnerability'] > 0.6:
            recommendations.append(
                "HIGH RISK TIME: Your cognitive function is significantly impaired at this hour. "
                "Delay any important decisions until morning (9-11 AM optimal)."
            )

        if analysis['decision_fatigue_level'] > 0.5:
            recommendations.append(
                f"DECISION FATIGUE: You've made many decisions in this session. "
                f"Take a 15+ minute break before any commitments. "
                f"Compliance tendency increased approximately {int(analysis['decision_fatigue_level'] * 35)}%."
            )

        if analysis['notification_intensity']:
            recommendations.append(
                "POST-NOTIFICATION: Content was delivered during your arousal window after a notification. "
                "Wait 5+ minutes for your state to normalize before engaging."
            )

        if analysis['day_vulnerability'] > 0.2:
            recommendations.append(
                "TIMING CONSIDERATION: This day carries additional vulnerability factors. "
                "Be extra cautious with financial decisions."
            )

        if not recommendations:
            if analysis['optimal_decision_time']:
                recommendations.append(
                    "GOOD TIMING: This is generally a good time for decision-making. "
                    "Cognitive function and vigilance are near optimal."
                )
            else:
                recommendations.append(
                    "NEUTRAL TIMING: No major temporal vulnerabilities detected, "
                    "but always take time to verify before major decisions."
                )

        return recommendations
```

---

## 8. PRECISE BEHAVIORAL INDICATOR DETECTION FOR AT-RISK POPULATIONS

**Clinical Approach Note:** This section uses precise, clinical terminology focused on behavioral indicators and cognitive patterns rather than stigmatizing labels. The goal is accurate identification of heightened susceptibility states to enable protective intervention.

```python
class CognitiveProcessingPattern(Enum):
    """Clinically-defined cognitive processing patterns indicating heightened susceptibility"""
    REDUCED_EXECUTIVE_FUNCTION = "reduced_executive_function"
    PROCESSING_SPEED_VARIATION = "processing_speed_variation"
    WORKING_MEMORY_LOAD = "working_memory_load"
    ATTENTION_REGULATION_DIFFERENCE = "attention_regulation_difference"
    SOCIAL_CUE_PROCESSING_DIFFERENCE = "social_cue_processing_difference"
    IMPULSE_REGULATION_STATE = "impulse_regulation_state"
    EMOTIONAL_REGULATION_STATE = "emotional_regulation_state"

class SusceptibilityFactor(Enum):
    """Research-identified factors associated with heightened influence susceptibility"""
    DEVELOPMENTAL_STAGE_EARLY = "early_developmental_cognitive_stage"
    DEVELOPMENTAL_STAGE_ADOLESCENT = "adolescent_developmental_stage"
    COGNITIVE_RESOURCE_DEPLETION = "cognitive_resource_depletion"
    SOCIAL_CONNECTION_DEFICIT = "social_connection_deficit"
    DIGITAL_INTERFACE_UNFAMILIARITY = "digital_interface_unfamiliarity"
    TRUST_CALIBRATION_DIFFERENCE = "trust_calibration_difference"
    INFORMATION_PROCESSING_DIFFERENCE = "information_processing_difference"
    EMOTIONAL_STATE_VULNERABILITY = "emotional_state_vulnerability"

@dataclass
class BehavioralIndicator:
    """A specific behavioral indicator with clinical precision"""
    indicator_name: str
    observable_behaviors: List[str]
    cognitive_mechanism: str
    susceptibility_increase: float
    protective_intervention: str

@dataclass
class PreciseSusceptibilityProfile:
    """Detailed susceptibility profile using clinical indicators"""
    active_factors: List[SusceptibilityFactor] = field(default_factory=list)
    behavioral_indicators: List[BehavioralIndicator] = field(default_factory=list)
    cognitive_patterns: List[CognitiveProcessingPattern] = field(default_factory=list)
    estimated_susceptibility_increase: float = 0.0
    high_risk_influence_types: List[str] = field(default_factory=list)
    recommended_protections: List[str] = field(default_factory=list)

class PreciseBehavioralIndicatorDetector:
    """
    Detects behavioral indicators of heightened influence susceptibility
    using clinical precision rather than demographic stereotyping.

    Research basis:
    - Developmental neuroscience: PFC maturation timeline
    - Cognitive psychology: Working memory, attention, executive function
    - Clinical research: Cognitive load, fatigue, emotional state effects
    """

    BEHAVIORAL_INDICATORS = {
        'developmental_persuasion_comprehension': BehavioralIndicator(
            indicator_name="Developing persuasive intent recognition",
            observable_behaviors=[
                "Difficulty distinguishing advertising from content",
                "Accepting claims at face value without verification instinct",
                "Responding to authority appeals without source evaluation"
            ],
            cognitive_mechanism="Persuasion knowledge develops gradually; metacognitive awareness requires mature theory of mind and executive function",
            susceptibility_increase=2.5,
            protective_intervention="Adult co-viewing and explicit discussion of persuasive intent. Content gatekeeping."
        ),
        'developing_impulse_regulation': BehavioralIndicator(
            indicator_name="Developing impulse regulation system",
            observable_behaviors=[
                "Faster decision-making under social pressure",
                "Heightened response to social reward cues",
                "Greater sensitivity to peer comparison metrics"
            ],
            cognitive_mechanism="Prefrontal cortex development continues through mid-20s. Limbic system (emotion, reward) matures earlier, creating developmental imbalance.",
            susceptibility_increase=1.8,
            protective_intervention="Structured decision delays. Explicit teaching of influence tactics."
        ),
        'cognitive_depletion_state': BehavioralIndicator(
            indicator_name="Cognitive resource depletion",
            observable_behaviors=[
                "Increased decision avoidance or deferral",
                "Preference for simpler options regardless of value",
                "Reduced information seeking before decisions",
                "Quicker acceptance of default options"
            ],
            cognitive_mechanism="Executive function requires glucose and rest. Depletion shifts processing toward System 1 (automatic) from System 2 (analytical).",
            susceptibility_increase=1.5,
            protective_intervention="Rest before important decisions. Reduce decision count. Use checklists to externalize analysis."
        ),
        'limited_verification_network': BehavioralIndicator(
            indicator_name="Limited social verification network",
            observable_behaviors=[
                "Making significant decisions without consulting others",
                "Extended online interaction sessions",
                "High engagement with parasocial relationships (influencers)",
                "Rapid trust development with new contacts"
            ],
            cognitive_mechanism="Social verification is key defense against influence. Isolation removes this check and increases reliance on influencer as sole information source.",
            susceptibility_increase=2.0,
            protective_intervention="Mandatory consultation with trusted others before major decisions. Structured social connection."
        ),
        'different_social_signal_processing': BehavioralIndicator(
            indicator_name="Different social signal processing",
            observable_behaviors=[
                "Literal interpretation of figurative influence language",
                "Difficulty detecting incongruence between words and intent",
                "Different weighting of verbal vs. nonverbal cues",
                "Pattern-following that can be leveraged"
            ],
            cognitive_mechanism="Neurodivergent processing often involves different social cue weighting. Influence tactics leverage neurotypical defaults, which may be processed differently.",
            susceptibility_increase=1.8,
            protective_intervention="Explicit verbal explanation of influence tactics. Written/visual guides. Trusted advisor consultation."
        ),
        'heightened_emotional_state': BehavioralIndicator(
            indicator_name="Heightened emotional processing state",
            observable_behaviors=[
                "Decisions driven by immediate emotional relief",
                "Reduced future-oriented thinking",
                "Seeking solutions to emotional pain",
                "Increased responsiveness to empathy appeals"
            ],
            cognitive_mechanism="Strong emotional states (grief, loneliness, fear, excitement) activate limbic processing and reduce prefrontal engagement. Creates 'hot' cognition.",
            susceptibility_increase=1.9,
            protective_intervention="Mandatory cooling-off periods during emotional states. Pre-commitment to decision delays."
        ),
    }

    FACTOR_VULNERABILITY_MAPPING = {
        SusceptibilityFactor.DEVELOPMENTAL_STAGE_EARLY: [
            "In-app purchase prompts", "Advertising disguised as content",
            "Gambling-adjacent mechanics (loot boxes)"
        ],
        SusceptibilityFactor.SOCIAL_CONNECTION_DEFICIT: [
            "Romance scams", "Companionship influence",
            "Parasocial relationship intensity"
        ],
        SusceptibilityFactor.DIGITAL_INTERFACE_UNFAMILIARITY: [
            "Phishing", "Tech support scams", "Interface spoofing"
        ],
        SusceptibilityFactor.INFORMATION_PROCESSING_DIFFERENCE: [
            "Social pressure intensity", "Gaslighting tactics",
            "Rule-based influence", "Boundary erosion"
        ],
        SusceptibilityFactor.EMOTIONAL_STATE_VULNERABILITY: [
            "Emotional relief promises", "Connection offers",
            "Fear intensity", "Hope influence"
        ],
    }

    def assess_from_behavioral_signals(self, behavioral_data: Dict) -> PreciseSusceptibilityProfile:
        """Assess susceptibility from observable behavioral signals."""
        profile = PreciseSusceptibilityProfile()

        session = behavioral_data.get('session_patterns', {})
        if session.get('late_night_activity_ratio', 0) > 0.3:
            profile.active_factors.append(SusceptibilityFactor.COGNITIVE_RESOURCE_DEPLETION)
            profile.behavioral_indicators.append(self.BEHAVIORAL_INDICATORS['cognitive_depletion_state'])

        if session.get('very_long_sessions', False):
            profile.active_factors.append(SusceptibilityFactor.SOCIAL_CONNECTION_DEFICIT)
            profile.behavioral_indicators.append(self.BEHAVIORAL_INDICATORS['limited_verification_network'])

        decisions = behavioral_data.get('decision_patterns', {})
        if decisions.get('accepts_defaults_frequently', False):
            profile.cognitive_patterns.append(CognitiveProcessingPattern.WORKING_MEMORY_LOAD)

        interactions = behavioral_data.get('interaction_patterns', {})
        if interactions.get('quick_trust_formation', False):
            profile.active_factors.append(SusceptibilityFactor.TRUST_CALIBRATION_DIFFERENCE)

        self_reported = behavioral_data.get('self_reported', {})
        if self_reported.get('emotional_state') in ['grief', 'loneliness', 'anxiety', 'excitement']:
            profile.active_factors.append(SusceptibilityFactor.EMOTIONAL_STATE_VULNERABILITY)
            profile.behavioral_indicators.append(self.BEHAVIORAL_INDICATORS['heightened_emotional_state'])

        if self_reported.get('processing_style') == 'neurodivergent':
            profile.active_factors.append(SusceptibilityFactor.INFORMATION_PROCESSING_DIFFERENCE)
            profile.behavioral_indicators.append(self.BEHAVIORAL_INDICATORS['different_social_signal_processing'])

        # Calculate susceptibility increase
        if profile.behavioral_indicators:
            increases = [ind.susceptibility_increase for ind in profile.behavioral_indicators]
            total = 1.0
            for i, inc in enumerate(sorted(increases, reverse=True)):
                total *= 1 + (inc - 1) / (1 + i * 0.5)
            profile.estimated_susceptibility_increase = total

        # Map vulnerabilities
        for factor in profile.active_factors:
            if factor in self.FACTOR_VULNERABILITY_MAPPING:
                profile.high_risk_influence_types.extend(self.FACTOR_VULNERABILITY_MAPPING[factor])

        # Generate protections
        for indicator in profile.behavioral_indicators:
            profile.recommended_protections.append(indicator.protective_intervention)

        return profile
```

---

## 9. INFORMATION ECOSYSTEM OPTIMIZATION DETECTOR

**Research Finding:** The information environment itself is optimized - echo chambers form algorithmically, emotional contagion spreads 4.34% faster for negative content.

```python
class EcosystemOptimizationType(Enum):
    ECHO_CHAMBER_FORMATION = "algorithmic_echo_chamber"
    FILTER_BUBBLE = "personalization_bubble"
    EMOTIONAL_CONTAGION = "emotion_spread_amplification"
    MISINFORMATION_CASCADE = "false_info_cascade"
    TRUST_EROSION = "impostor_bias_creation"
    POLARIZATION_AMPLIFICATION = "division_amplification"

@dataclass
class EcosystemAnalysis:
    """Analysis of information ecosystem influence"""
    optimization_types: List[EcosystemOptimizationType] = field(default_factory=list)
    echo_chamber_score: float = 0.0
    emotional_contagion_risk: float = 0.0
    trust_environment_score: float = 1.0
    ecosystem_health_rating: str = "unknown"

class InformationEcosystemDetector:
    """
    Detects optimization of the information ecosystem.

    Research basis:
    - Echo chambers form algorithmically, not organically
    - Emotional contagion spreads 4.34% faster for negative content
    - "Impostor Bias": People doubt even authentic content
    """

    CONTAGION_PATTERNS = {
        'negative_amplification': 1.0434,
        'anger_persistence': 1.2,
        'fear_spread_rate': 1.15,
    }

    def analyze_user_ecosystem(self, feed_data: List[Dict]) -> EcosystemAnalysis:
        """Analyze a user's information ecosystem for influence."""
        analysis = EcosystemAnalysis()

        if not feed_data:
            return analysis

        # Echo chamber detection
        stances = [f.get('stance') for f in feed_data if f.get('stance')]
        if stances:
            unique = len(set(stances))
            analysis.echo_chamber_score = 1 - (unique / len(stances))
            if analysis.echo_chamber_score > 0.6:
                analysis.optimization_types.append(EcosystemOptimizationType.ECHO_CHAMBER_FORMATION)

        # Emotional contagion
        valences = [f.get('emotional_valence', 'neutral') for f in feed_data]
        negative = sum(1 for v in valences if v in ['negative', 'anger', 'fear'])
        total = len(valences)
        if total > 0:
            negativity_ratio = negative / total
            analysis.emotional_contagion_risk = negativity_ratio * self.CONTAGION_PATTERNS['negative_amplification']
            if analysis.emotional_contagion_risk > 0.4:
                analysis.optimization_types.append(EcosystemOptimizationType.EMOTIONAL_CONTAGION)

        # Trust erosion
        erosion_patterns = ['can\'t trust', 'fake', 'hoax', 'propaganda', 'lie']
        content_text = ' '.join(f.get('content', '') for f in feed_data).lower()
        erosion_count = sum(1 for p in erosion_patterns if p in content_text)
        analysis.trust_environment_score = max(0, 1 - erosion_count / len(feed_data) * 3)
        if analysis.trust_environment_score < 0.5:
            analysis.optimization_types.append(EcosystemOptimizationType.TRUST_EROSION)

        # Health rating
        score = (
            (1 - analysis.echo_chamber_score) * 0.35 +
            (1 - analysis.emotional_contagion_risk) * 0.35 +
            analysis.trust_environment_score * 0.3
        )
        if score > 0.7:
            analysis.ecosystem_health_rating = "healthy"
        elif score > 0.5:
            analysis.ecosystem_health_rating = "moderate_concern"
        else:
            analysis.ecosystem_health_rating = "degraded"

        return analysis
```

---

## 10. MASTER HIGH-IMPACT AUDITOR

```python
class MasterHighImpactAuditor:
    """Master integration class for all high-impact detection systems."""

    def __init__(self):
        self.stacking_detector = SynergisticStackingDetector()
        self.temporal_detector = TemporalIntensityDetector()
        self.bypass_detector = PhysiologicalBypassDetector()
        self.combination_detector = RankedCombinationDetector()
        self.behavioral_detector = PreciseBehavioralIndicatorDetector()
        self.ecosystem_detector = InformationEcosystemDetector()

    def comprehensive_audit(self, content: Dict, user_data: Dict = None) -> Dict:
        """Perform comprehensive high-impact influence audit."""
        report = {
            'audit_timestamp': time.time(),
            'overall_threat_level': 'unknown',
            'overall_risk_score': 0.0,
            'ranked_findings': [],
            'immediate_actions': [],
            'protective_measures': []
        }

        risk_scores = []

        # 1. Technique stacking
        stacking = self.stacking_detector.analyze_stacking(content)
        report['technique_stacking'] = {
            'techniques': [t.value for t in stacking.techniques_detected],
            'synergies': len(stacking.synergies_activated),
            'amplified_score': stacking.amplified_score,
            'sophistication': stacking.sophistication_level
        }
        risk_scores.append(stacking.amplified_score)

        # 2. Ranked combinations
        combinations = self.combination_detector.detect_combinations(content)
        report['ranked_combinations'] = combinations
        if combinations['highest_rank_detected']:
            risk_scores.append(1 - (combinations['highest_rank_detected'] - 1) / 15)

        # 3. Temporal intensity
        if content.get('timestamp'):
            temporal = self.temporal_detector.analyze_delivery_timing(
                content['timestamp'],
                user_data.get('user_id') if user_data else None
            )
            report['temporal_intensity'] = {
                'windows_active': [w['window'] for w in temporal['vulnerability_windows_active']],
                'combined_risk': temporal['combined_temporal_risk']
            }
            risk_scores.append(temporal['combined_temporal_risk'])

        # 4. Physiological bypass
        bypass = self.bypass_detector.analyze_content(content)
        report['physiological_bypass'] = {
            'mechanisms': [m.value for m in bypass.bypass_mechanisms],
            'effectiveness': bypass.combined_bypass_effectiveness,
            'countermeasures': bypass.countermeasures
        }
        risk_scores.append(bypass.combined_bypass_effectiveness)

        # 5. User susceptibility
        if user_data:
            susceptibility = self.behavioral_detector.assess_from_behavioral_signals(user_data)
            report['user_susceptibility'] = {
                'factors': [f.value for f in susceptibility.active_factors],
                'increase': susceptibility.estimated_susceptibility_increase,
                'protections': susceptibility.recommended_protections
            }
            if susceptibility.estimated_susceptibility_increase > 1.5:
                risk_scores = [r * min(2.0, susceptibility.estimated_susceptibility_increase) for r in risk_scores]

        # Calculate overall risk
        if risk_scores:
            report['overall_risk_score'] = min(1.0, np.mean(risk_scores) * 0.6 + max(risk_scores) * 0.4)

        # Determine threat level
        if report['overall_risk_score'] > 0.8:
            report['overall_threat_level'] = 'CRITICAL'
        elif report['overall_risk_score'] > 0.6:
            report['overall_threat_level'] = 'HIGH'
        elif report['overall_risk_score'] > 0.4:
            report['overall_threat_level'] = 'MODERATE'
        else:
            report['overall_threat_level'] = 'LOW'

        # Generate actions for critical threats
        if report['overall_threat_level'] == 'CRITICAL':
            report['immediate_actions'] = [
                "STOP: Do not act on this content until fully analyzed",
                "DELAY: Mandatory 24-hour delay before any decision",
                "VERIFY: Consult trusted person not exposed to this content"
            ]

        return report
```

---

## APPENDIX: COMBINATION EFFECTIVENESS RANKING

Rankings based on empirical research:
1. **Effect size** (40%) - Cohen's d from controlled studies
2. **Mechanism synergy** (25%) - How techniques amplify each other
3. **Vulnerability depth** (20%) - How fundamental the intensity
4. **Field success** (15%) - Documented real-world effectiveness

### Top 5 Most Effective Combinations (Ranked)

| Rank | Combination | Multiplier | Primary Use |
|------|-------------|------------|-------------|
| 1 | Emotional arousal + Cognitive overload + Urgency | 2.1x | High-pressure scams |
| 2 | Authority + Fear + Urgency | 1.95x | IRS/tech support scams |
| 3 | Variable reward + Streak + Social proof | 1.85x | Mobile game engagement |
| 4 | Personalization + Scarcity + Social proof | 1.78x | E-commerce conversion |
| 5 | Trust building + Reciprocity + Commitment escalation | 1.72x | Romance/business fraud |

### Combinations 6-15 (Decreasing Effectiveness)

| Rank | Combination | Multiplier |
|------|-------------|------------|
| 6 | Infinite scroll + Personalization + Variable reward | 1.65x |
| 7 | Anchoring + Decoy + Urgency | 1.58x |
| 8 | Authority + Social proof + Personalization | 1.52x |
| 9 | Fear + Scarcity + Loss framing | 1.48x |
| 10 | ASMR relaxation + Authority + Suggestion | 1.45x |
| 11 | Guilt + Commitment + Reciprocity | 1.42x |
| 12 | Scarcity + Social proof | 1.40x |
| 13 | Liking + Reciprocity | 1.35x |
| 14 | Authority + Social proof | 1.32x |
| 15 | Urgency + Scarcity | 1.28x |

---

**Document compiled from 2024-2025 research. See APPENDIX_RESEARCH_SOURCES.md for citations.**