# ENHANCED DETECTION RESEARCH
## Detection Methods and Frameworks
**Compilation for Influence Auditing Tool**

---

## OVERVIEW

This document enhances your existing detection frameworks with:
- **Documented behavioral patterns**
- **Real-world case studies** with documented regulatory actions
- **Improved detection mechanisms** based on ML/AI approaches
- **Physiological measurement methods**
- **Regulatory frameworks** (FTC, EU AI Act, CCPA)

---

## PART 1: EMOTIONAL FRACTIONATION - ENHANCED DETECTION

### Key Findings

#### Key Finding 1: Algorithmic Amplification Confirmed
A study published in **Science** conducted a 10-day field experiment with 1,256 participants on X during a US presidential campaign:
- Decreasing or increasing exposure to content expressing antidemocratic attitudes and partisan animosity shifted out-party partisan animosity by **more than 2 points on a 100-point feeling thermometer**
- This provides **causal evidence** that algorithmic content exposure directly alters emotional states

#### Key Finding 2: Engagement Algorithms Amplify Emotional Content
Research published in **PNAS Nexus** found:
- Twitter's engagement-based ranking algorithm amplifies **emotionally charged, out-group hostile content**
- Users report this content makes them feel **worse** about their political out-group
- Users do **not prefer** the political tweets selected by the algorithm
- Engagement-based algorithms underperform at satisfying users' stated preferences

#### Key Finding 3: Facebook's Emotional Weighting System
Whistleblower Frances Haugen revealed (2021):
- Facebook's newsfeed algorithm favored material that made people emotional (sad/angry) over material that elicited a "like" **by a factor of 5**
- Angry emoji reactions were weighted **5x higher than likes** (2018)
- This was gradually reduced to **weight 0 by 2020** after internal complaints
- Anger-evoking material disproportionately includes misinformation and high-intensity content

#### Key Finding 4: TikTok's Emotional Engagement Cycle
Reverse-engineering analysis reveals TikTok's algorithm follows:
```
Baseline → Negative content → Emotional dip → Positive content → Relief/gratitude → Dependency reinforcement
```

Key findings:
- TikTok can detect when users are sad, anxious, or emotionally vulnerable with **94% accuracy**
- Content is adjusted to keep users engaged longer, not to improve wellbeing
- Creates emotional dependency on the app for mood regulation

### Enhanced Detection Code

```python
class EnhancedFractionationDetector:
    """
    Enhanced fractionation detection.
    Incorporates current research findings and platform analysis.
    """

    # TikTok engagement scoring (reverse-engineered)
    ENGAGEMENT_WEIGHTS = {
        "rewatch_loop": 10,      # Highest value - indicates emotional capture
        "complete_watch": 8,     # High engagement
        "share": 6,              # Distribution behavior
        "comment": 4,            # Active engagement
        "like": 2,               # Low value signal
        "quick_scroll": -1       # Negative signal
    }

    # Emotional content markers (expanded from academic research)
    ANGER_OUTRAGE_MARKERS = [
        # Political/tribal outrage
        "outrageous", "unbelievable", "disgusting", "shameful",
        "corrupt", "hypocrite", "traitor", "enemy", "threat",
        "attack", "destroy", "fight", "war", "battle",
        # Moral outrage
        "should be ashamed", "how dare", "unacceptable",
        "this is wrong", "can't believe", "absolutely unacceptable",
        # Threat framing
        "coming for", "want to take", "trying to destroy",
        "end of", "death of", "threat to", "danger"
    ]

    JOY_RELIEF_MARKERS = [
        # Wholesome content
        "heartwarming", "restored faith", "beautiful", "amazing",
        "incredible", "touching", "inspiring", "wholesome",
        # Social bonding
        "community", "together", "support", "family", "friends",
        "belong", "one of us", "our people", "tribe",
        # Relief/resolution
        "finally", "justice", "karma", "deserved", "won",
        "victory", "breakthrough", "solved", "fixed"
    ]

    COMMERCIAL_RELIEF_MARKERS = [
        # Product as solution
        "you deserve", "treat yourself", "self-care",
        "invest in yourself", "you're worth it",
        # Limited offer urgency
        "limited time", "exclusive", "special offer",
        "don't miss", "act now", "while supplies last",
        # Lifestyle aspiration
        "upgrade your life", "transform", "breakthrough",
        "secret", "what they don't want you to know"
    ]

    def detect_emotional_sequence(self, content_list: List[Dict]) -> Dict:
        """
        Analyze a sequence of content items for fractionation patterns.

        Args:
            content_list: List of dicts with 'text', 'type', 'timestamp', 'engagement'

        Returns:
            Analysis with fractionation score and detected patterns
        """

        emotional_scores = []
        sequence_patterns = []

        for i, content in enumerate(content_list):
            text = content.get('text', '').lower()

            # Calculate emotional valence
            anger_score = sum(1 for m in self.ANGER_OUTRAGE_MARKERS if m in text)
            joy_score = sum(1 for m in self.JOY_RELIEF_MARKERS if m in text)
            commercial_score = sum(1 for m in self.COMMERCIAL_RELIEF_MARKERS if m in text)

            # Determine emotional state
            if anger_score > joy_score and anger_score > 0:
                emotional_scores.append(('anger', anger_score))
            elif joy_score > anger_score and joy_score > 0:
                emotional_scores.append(('joy', joy_score))
            elif commercial_score > 0:
                emotional_scores.append(('commercial_relief', commercial_score))
            else:
                emotional_scores.append(('neutral', 0))

        # Detect A-J-A-R (Anger-Joy-Anger-Relief) sequences
        ajar_count = self._count_ajar_sequences(emotional_scores)

        # Calculate oscillation frequency
        oscillation_rate = self._calculate_oscillation(emotional_scores)

        # Determine fractionation intensity
        fractionation_score = min(
            (ajar_count * 25) + (oscillation_rate * 50),
            100
        )

        return {
            "fractionation_score": fractionation_score,
            "ajar_sequences_detected": ajar_count,
            "oscillation_rate": oscillation_rate,
            "emotional_sequence": emotional_scores,
            "intensity": self._categorize_intensity(fractionation_score),
            "regulatory_relevance": "EU AI Act classifies certain emotional influence techniques as high-risk/prohibited"
        }

    def _count_ajar_sequences(self, scores: List[Tuple]) -> int:
        """Count Anger-Joy-Anger-Relief patterns"""
        count = 0
        for i in range(len(scores) - 3):
            if (scores[i][0] == 'anger' and
                scores[i+1][0] == 'joy' and
                scores[i+2][0] == 'anger' and
                scores[i+3][0] in ['joy', 'commercial_relief']):
                count += 1
        return count

    def _calculate_oscillation(self, scores: List[Tuple]) -> float:
        """Calculate emotional oscillation rate (switches per content item)"""
        switches = 0
        for i in range(1, len(scores)):
            if scores[i][0] != scores[i-1][0] and scores[i][0] != 'neutral':
                switches += 1
        return switches / max(len(scores), 1)

    def _categorize_intensity(self, score: float) -> str:
        if score < 25:
            return "MINIMAL - Normal content variation"
        elif score < 50:
            return "MODERATE - Some emotional cycling present"
        elif score < 75:
            return "HIGH - Active fractionation patterns detected"
        else:
            return "EXTREME - Systematic emotional sequencing"
```

### Physiological Detection Methods (Neuromarketing Research)


```python
class PhysiologicalFractionationDetector:
    """
    Physiological markers for fractionation detection.
    Based on neuromarketing and consumer neuroscience research.
    """

    # Baseline thresholds from research
    BLINK_RATE_THRESHOLDS = {
        "normal": (15, 20),           # blinks per minute
        "anger_arousal": (30, 45),    # elevated during threat content
        "focused_engagement": (0, 10),    # reduced during relief/purchase state
    }

    SKIN_CONDUCTANCE_THRESHOLDS = {
        "baseline": (0, 1),           # microsiemens
        "anger_arousal": (2, 5),      # elevated during emotional content
        "relief_drop": (-2, -1),      # rapid decrease during relief phase
    }

    HEART_RATE_VARIABILITY = {
        "normal": (50, 100),          # ms between beats
        "stress_reduced": (20, 40),   # low variability = stress/anger
        "relief_spike": (60, 80),     # recovery during relief
    }

    PUPIL_DILATION_STATES = {
        "baseline": 1.0,              # normalized
        "anger_content": 1.15,        # 15% dilation
        "joy_content": 0.95,          # slight constriction
        "ad_focus": 1.20,             # maximum dilation = low critical thinking
    }

    def analyze_biometric_sequence(self, measurements: List[Dict]) -> Dict:
        """
        Analyze sequence of biometric measurements for fractionation indicators.

        Expected input format:
        {
            'timestamp': float,
            'blink_rate': int,          # blinks per minute
            'skin_conductance': float,  # microsiemens
            'heart_rate': int,          # bpm
            'hrv': float,               # heart rate variability ms
            'pupil_dilation': float,    # normalized to baseline
            'content_type': str         # 'anger', 'joy', 'ad', 'neutral'
        }
        """

        fractionation_indicators = []

        # Look for the signature pattern:
        # 1. Elevated arousal (anger phase)
        # 2. Partial recovery (joy phase)
        # 3. Higher elevation (anger #2)
        # 4. Reduced-vigilance state (relief/ad phase)

        for i in range(len(measurements) - 3):
            sequence = measurements[i:i+4]

            if self._detect_anger_phase(sequence[0]):
                if self._detect_joy_recovery(sequence[1]):
                    if self._detect_elevated_anger(sequence[2], sequence[0]):
                        if self._detect_reduced_vigilance_state(sequence[3]):
                            fractionation_indicators.append({
                                "start_index": i,
                                "pattern": "COMPLETE_FRACTIONATION_CYCLE",
                                "confidence": "HIGH",
                                "indicators": {
                                    "anger_1": self._summarize_state(sequence[0]),
                                    "joy": self._summarize_state(sequence[1]),
                                    "anger_2": self._summarize_state(sequence[2]),
                                    "relief": self._summarize_state(sequence[3])
                                }
                            })

        return {
            "fractionation_cycles_detected": len(fractionation_indicators),
            "detailed_patterns": fractionation_indicators,
            "physiological_signature": "Prefrontal cortex shows 40-60% reduced activity during relief phase",
            "methodology": "Neuroimaging + physiological measure comparison"
        }

    def _detect_anger_phase(self, m: Dict) -> bool:
        return (m.get('blink_rate', 0) > 30 and
                m.get('skin_conductance', 0) > 2 and
                m.get('hrv', 100) < 40)

    def _detect_joy_recovery(self, m: Dict) -> bool:
        return (15 <= m.get('blink_rate', 0) <= 25 and
                m.get('hrv', 0) > 50)

    def _detect_elevated_anger(self, m2: Dict, m1: Dict) -> bool:
        return (m2.get('blink_rate', 0) > m1.get('blink_rate', 0) and
                m2.get('skin_conductance', 0) > m1.get('skin_conductance', 0))

    def _detect_reduced_vigilance_state(self, m: Dict) -> bool:
        return (m.get('blink_rate', 100) < 10 and
                m.get('pupil_dilation', 1) > 1.15)

    def _summarize_state(self, m: Dict) -> Dict:
        return {
            "blink_rate": m.get('blink_rate'),
            "skin_conductance": m.get('skin_conductance'),
            "hrv": m.get('hrv'),
            "pupil_dilation": m.get('pupil_dilation'),
            "content_type": m.get('content_type')
        }
```

---

## PART 2: NON-TRANSPARENT DESIGN PATTERNS - ENHANCED DETECTION

### FTC Global Review Findings

The FTC's international review (ICPEN + GPEN) examined 642 websites and mobile apps:

- **76% employed at least one interface design pattern**
- **67% used multiple interface design patterns**
- **97% of privacy-related flows contained interface design patterns** (GPEN finding)

### Regulatory Framework

| Regulation | Scope | Interface Design Prohibition |
|------------|-------|-------------------------|
| **FTC Act Section 5** | US Federal | Commercial practices regulation |
| **CCPA** | California | Explicit interface design prohibition |
| **EU AI Act** | European Union | Emotional influence techniques = prohibited/high-risk |
| **14 State Privacy Laws** | Various US States | Non-transparent design prohibitions |

### Enhanced Interface Design Detectors

```python
class EnhancedInterfaceDesignDetector:
    """
    Enhanced interface design detection based on FTC/ICPEN findings.
    Covers all major interface design categories with regulatory references.
    """

    # === CONFIRMSHAMING ===

    CONFIRMSHAMING_PATTERNS = {
        "self_deprecating_decline": [
            r"no,?\s*i\s*(don'?t|do not)\s*(want|like|need|care)",
            r"no\s*thanks?,?\s*i('?m|am)\s*(not|already)",
            r"i('?d|would)\s*rather\s*(not|stay|continue)",
            r"no,?\s*i\s*prefer\s*to\s*(pay|miss|lose)",
            r"i\s*hate\s*(saving|deals|discounts|fun)",
        ],
        "guilt_inducing_language": [
            "are you sure you want to miss",
            "you'll regret",
            "don't make this mistake",
            "people who care about",
            "smart people choose",
        ],
        "extreme_examples_documented": [
            # MyMedic (2018) - documented case
            "no, i don't want to stay alive",
            "no, i prefer to bleed to death",
            # Common newsletter patterns
            "no, i don't want to save money",
            "no, i hate good deals",
        ]
    }

    # === ROACH MOTEL (Hard to Cancel) ===

    ROACH_MOTEL_INDICATORS = {
        "signup_vs_cancel_asymmetry": {
            "easy_signup_phrases": [
                "sign up in seconds", "one-click", "instant access",
                "start free trial", "get started now", "join free"
            ],
            "difficult_cancel_phrases": [
                "call to cancel", "contact customer service",
                "mail cancellation request", "visit in person",
                "speak to retention specialist", "wait for callback"
            ]
        },
        "cancel_obstruction_tactics": [
            "are you sure?",           # Confirmation loop
            "before you go",           # Retention intercept
            "special offer to stay",   # Bribe attempt
            "we'll miss you",          # Emotional appeal
            "type 'CANCEL' to confirm", # Friction addition
        ],
        "documented_cases": {
            "Amazon Prime": "FTC lawsuit - 'labyrinth-like process'",
            "New York Times": "8+ minutes conversation required to cancel",
            "HelloFresh": "Documented roach motel pattern user"
        }
    }

    # === FALSE URGENCY/SCARCITY ===

    FAKE_URGENCY_INDICATORS = {
        "countdown_patterns": [
            r"only\s*\d+\s*(hours?|minutes?|seconds?)\s*left",
            r"offer\s*ends?\s*in",
            r"sale\s*ends?\s*at\s*midnight",
            r"limited\s*time\s*only",
            r"\d+:\d+:\d+",  # Timer format
        ],
        "fake_scarcity_patterns": [
            r"only\s*\d+\s*left\s*in\s*stock",
            r"\d+\s*people\s*(are\s*)?(viewing|looking|watching)",
            r"selling\s*fast",
            r"almost\s*(gone|sold\s*out)",
            r"low\s*stock\s*warning",
        ],
        "detection_method": """
            1. Refresh page - does timer reset?
            2. Clear cookies - does 'limited stock' reset?
            3. Visit from different device - same urgency claims?
            4. Return after timer expires - still available?
            If YES to any: FAKE URGENCY CONFIRMED
        """
    }

    def detect_confirmshaming(self, decline_button_text: str) -> Dict:
        """
        Detect confirmshaming in decline/opt-out button text.

        Research basis: Princeton 2019 interface design study,
        FTC ICPEN review
        """

        text_lower = decline_button_text.lower()
        score = 0
        flags = []

        # Check self-deprecating patterns
        import re
        for pattern in self.CONFIRMSHAMING_PATTERNS["self_deprecating_decline"]:
            if re.search(pattern, text_lower):
                score += 40
                flags.append(f"Self-deprecating decline: matches '{pattern}'")

        # Check guilt-inducing language
        for phrase in self.CONFIRMSHAMING_PATTERNS["guilt_inducing_language"]:
            if phrase in text_lower:
                score += 30
                flags.append(f"Guilt-inducing: '{phrase}'")

        # Check for documented extreme examples
        for phrase in self.CONFIRMSHAMING_PATTERNS["extreme_examples_documented"]:
            if phrase in text_lower:
                score += 50
                flags.append(f"EXTREME confirmshaming (documented case): '{phrase}'")

        return {
            "pattern_type": "CONFIRMSHAMING",
            "score": min(score, 100),
            "flags": flags,
            "regulatory_status": "Prohibited under CCPA; FTC enforcement active",
            "academic_research": "Mild patterns somewhat effective; aggressive patterns 4x more effective but generate backlash"
        }

    def detect_roach_motel(self, signup_flow: Dict, cancel_flow: Dict) -> Dict:
        """
        Detect roach motel pattern by comparing signup vs cancel difficulty.

        Args:
            signup_flow: {'steps': int, 'time_seconds': int, 'requires_call': bool}
            cancel_flow: {'steps': int, 'time_seconds': int, 'requires_call': bool}
        """

        asymmetry_score = 0
        flags = []

        # Step asymmetry
        step_ratio = cancel_flow['steps'] / max(signup_flow['steps'], 1)
        if step_ratio > 2:
            asymmetry_score += 30
            flags.append(f"Cancel requires {step_ratio:.1f}x more steps than signup")

        # Time asymmetry
        time_ratio = cancel_flow['time_seconds'] / max(signup_flow['time_seconds'], 1)
        if time_ratio > 3:
            asymmetry_score += 30
            flags.append(f"Cancel takes {time_ratio:.1f}x longer than signup")

        # Channel asymmetry (online signup but phone cancel)
        if not signup_flow.get('requires_call') and cancel_flow.get('requires_call'):
            asymmetry_score += 40
            flags.append("CHANNEL MISMATCH: Online signup but phone required to cancel")

        return {
            "pattern_type": "ROACH_MOTEL",
            "asymmetry_score": min(asymmetry_score, 100),
            "flags": flags,
            "regulatory_status": "FTC actively prosecuting (Amazon Prime lawsuit)",
            "documented_prevalence": "11% of e-commerce sites (Princeton 2019)",
            "CHI_reference": "Staying at the Roach Motel: Cross-Country Analysis"
        }

    def detect_fake_urgency(self, page_content: str, page_reload_content: str = None) -> Dict:
        """
        Detect fake urgency/scarcity with optional reload comparison.

        Args:
            page_content: HTML/text content of page
            page_reload_content: Same page after refresh (optional - enables timer reset detection)
        """

        import re

        score = 0
        flags = []
        content_lower = page_content.lower()

        # Check for urgency patterns
        for pattern in self.FAKE_URGENCY_INDICATORS["countdown_patterns"]:
            matches = re.findall(pattern, content_lower)
            if matches:
                score += 20
                flags.append(f"Countdown timer detected: {matches}")

        # Check for scarcity patterns
        for pattern in self.FAKE_URGENCY_INDICATORS["fake_scarcity_patterns"]:
            matches = re.findall(pattern, content_lower)
            if matches:
                score += 20
                flags.append(f"Scarcity claim detected: {matches}")

        # Timer reset detection (if reload provided)
        if page_reload_content:
            reload_lower = page_reload_content.lower()

            # Extract timers from both
            original_timers = re.findall(r'\d+:\d+:\d+', content_lower)
            reload_timers = re.findall(r'\d+:\d+:\d+', reload_lower)

            # If timer reset or same after refresh = FAKE
            if original_timers and reload_timers:
                if original_timers == reload_timers or reload_timers[0] >= original_timers[0]:
                    score += 50
                    flags.append("FAKE TIMER CONFIRMED: Timer reset on page refresh")

        return {
            "pattern_type": "FAKE_URGENCY_SCARCITY",
            "score": min(score, 100),
            "flags": flags,
            "regulatory_status": "Competition Bureau Canada advisory; FTC enforcement",
            "research": "1.2% of e-commerce sites reset timers (Princeton interface design study)",
            "consumer_impact": "68% of millennials make purchases within 24 hours when influenced by FOMO"
        }
```

---

## PART 3: CIALDINI'S PRINCIPLES - ENHANCED DETECTION

### Key Findings

#### Social Engineering Context
Research with 642 UK and Arab participants found:
- **Social Proof and Authority** are the most influential principles
- **Scarcity** is least influential but still significant
- Effects persist even when social engineering is knowingly possible

#### LLM Personalized Persuasion
Study of 19 LLMs across 5 model families:
- Models adapt persuasive language based on personality cues
- More anxiety-related words for neuroticism
- More achievement-related words for conscientiousness
- Potential for mass-scale personalized influence

#### Deepfake Analysis Framework
DEEP FRAME tool developed to analyze deepfakes through Cialdini's lens:
- Authority and Social Proof most commonly leveraged
- Financial fraud scenarios most prevalent
- Systematic framework for analysis

### Enhanced Cialdini Detection

```python
class EnhancedCialdiniDetector:
    """
    Enhanced Cialdini principle detection with research findings.
    Includes deepfake/AI influence detection.
    """

    # Social Proof - Enhanced with fake review detection
    SOCIAL_PROOF_SIGNALS = {
        "genuine_indicators": [
            "verified purchase", "verified buyer",
            "specific details about use", "balanced pros/cons",
            "mentions specific features", "realistic timeline"
        ],
        "fake_indicators": [
            "generic superlatives only", "no specific details",
            "extreme rating without context", "similar phrasing across reviews",
            "posted in burst pattern", "reviewer has few other reviews"
        ],
        "manufactured_consensus": [
            "everyone agrees", "unanimous support",
            "all experts say", "studies show" # without citation
        ]
    }

    # Authority - Enhanced with deepfake/AI detection
    AUTHORITY_SIGNALS = {
        "legitimate": [
            "peer-reviewed", "published in", "university affiliation",
            "verifiable credentials", "documented experience"
        ],
        "manufactured": [
            "expert says" # without naming expert
            "doctors recommend" # without specific doctors
            "according to studies" # without citations
            "industry leader" # vague positioning
        ],
        "deepfake_risk_indicators": [
            "celebrity endorsement", "politician statement",
            "expert video testimony", "audio recording"
        ]
    }

    # Scarcity - Enhanced with fake urgency detection
    SCARCITY_SIGNALS = {
        "legitimate": [
            "batch production with number",
            "specific inventory count",
            "seasonal availability with dates",
            "manufacturing constraints explained"
        ],
        "manufactured": [
            "limited time" # resets on refresh
            "only X left" # same number across sessions
            "exclusive" # but widely advertised
            "selling fast" # no verification possible
        ],
        "destruction_framing": [
            "will never be made again",
            "burning unsold inventory",
            "one-time-only production"
        ]
    }

    def detect_fake_social_proof(self, reviews: List[Dict]) -> Dict:
        """
        Detect manufactured social proof using ML indicators.

        Based on: fake review detection research
        """

        fake_indicators = 0
        flags = []

        # Analyze review patterns
        review_texts = [r.get('text', '') for r in reviews]
        review_ratings = [r.get('rating', 0) for r in reviews]
        review_dates = [r.get('date') for r in reviews]

        # Check for rating distribution anomaly
        # Real reviews: approximate normal distribution
        # Fake reviews: bimodal (mostly 5s and 1s)
        high_ratings = sum(1 for r in review_ratings if r >= 4)
        if len(review_ratings) > 10 and high_ratings / len(review_ratings) > 0.9:
            fake_indicators += 25
            flags.append("Suspicious: >90% high ratings")

        # Check for burst posting pattern
        if review_dates:
            # Multiple reviews in short timeframe = suspicious
            # Implementation would check date clustering
            pass

        # Check for generic language patterns
        generic_phrases = [
            "great product", "highly recommend", "love it",
            "best purchase ever", "exactly as described"
        ]

        for review_text in review_texts:
            text_lower = review_text.lower()
            generic_count = sum(1 for p in generic_phrases if p in text_lower)
            if generic_count >= 3:
                fake_indicators += 10
                flags.append(f"Generic phrases detected in review")

        # Check for similar phrasing across reviews (copy patterns)
        # Would use NLP similarity measures in production

        return {
            "principle": "SOCIAL_PROOF",
            "manufactured_probability": min(fake_indicators, 100),
            "flags": flags,
            "detection_method": "Pattern analysis for fake review detection",
            "ml_approaches_available": [
                "BERT-based classification (91% accuracy)",
                "Graph Neural Networks for reviewer networks",
                "Semi-supervised PU-learning for unlabeled data"
            ]
        }

    def detect_manufactured_authority(self, content: str, media_type: str = "text") -> Dict:
        """
        Detect manufactured or potentially deepfaked authority claims.
        """

        score = 0
        flags = []
        content_lower = content.lower()

        # Check for vague authority claims
        vague_authorities = [
            ("experts say", "No specific expert named"),
            ("studies show", "No study citation provided"),
            ("doctors recommend", "No specific doctors identified"),
            ("according to science", "No scientific reference"),
            ("research proves", "No research cited")
        ]

        for phrase, concern in vague_authorities:
            if phrase in content_lower:
                score += 20
                flags.append(f"Vague authority: '{phrase}' - {concern}")

        # Check for deepfake risk (video/audio content)
        if media_type in ["video", "audio"]:
            deepfake_risk_phrases = [
                "endorses", "recommends", "supports",
                "personally uses", "trusts"
            ]

            for phrase in deepfake_risk_phrases:
                if phrase in content_lower:
                    score += 15
                    flags.append(f"DEEPFAKE RISK: Celebrity/authority '{phrase}' claim in {media_type}")

        return {
            "principle": "AUTHORITY",
            "manufactured_probability": min(score, 100),
            "flags": flags,
            "deepfake_analysis": "Use DEEP FRAME tool for video/audio verification",
            "framework": "Cialdini's Principles for Deepfake Analysis"
        }
```

---

## PART 4: COGNITIVE LOAD & DECISION FATIGUE - ENHANCED

### Key Findings

#### Cognitive Load Theory Application
- Working memory limited to **7±2 information units**
- Maximum processing duration: **~20 seconds**
- Better checkout design could increase conversions by **35.26%**

#### Decision Fatigue Research
- After **10-15 decisions**: analytical capability drops **40%**
- Compliance increases **35%** when decision fatigued
- **12+ decision points**: measurable slower response times and cart abandonment

### Enhanced Decision Fatigue Detection

```python
class EnhancedCognitiveLoadDetector:
    """
    Enhanced cognitive load and decision fatigue detection.
    Based on e-commerce and cognitive psychology research.
    """

    # Cognitive load thresholds from research
    COGNITIVE_THRESHOLDS = {
        "working_memory_limit": 7,        # Miller's Law (±2)
        "processing_window_seconds": 20,   # Maximum sustained focus
        "decision_fatigue_onset": 10,      # Decisions before fatigue
        "critical_decision_points": 12,    # Point of significant degradation
        "conversion_optimal_steps": 3,     # Checkout steps for max conversion
    }

    # Decision multiplication patterns
    DECISION_MULTIPLICATION_SIGNALS = [
        # Configuration overload
        "customize", "personalize", "configure", "select your",
        "choose from", "pick your", "decide between",
        # Option multiplication
        "multiple options", "various choices", "many alternatives",
        "extended selection", "full range", "complete lineup",
        # Nested decisions
        "also consider", "you might also like", "frequently bought together",
        "customers also viewed", "similar items"
    ]

    # Strategic fatigue positioning (big ask after exhaustion)
    FATIGUE_POSITIONING_SIGNALS = [
        # End-of-flow positioning
        "final step", "one more thing", "last question",
        "almost done", "just one more", "before you finish",
        # Upsell/cross-sell at checkout
        "add protection plan", "upgrade your order",
        "complete your purchase with", "don't forget"
    ]

    def analyze_user_flow(self, flow_steps: List[Dict]) -> Dict:
        """
        Analyze a user flow for cognitive load intensity.

        Args:
            flow_steps: List of dicts with:
                - 'step_name': str
                - 'decisions_required': int
                - 'options_presented': int
                - 'time_pressure': bool
                - 'contains_upsell': bool
        """

        total_decisions = sum(s.get('decisions_required', 0) for s in flow_steps)
        max_options_single_step = max(s.get('options_presented', 0) for s in flow_steps)

        intensity_score = 0
        flags = []

        # Check total decision count
        if total_decisions > self.COGNITIVE_THRESHOLDS["decision_fatigue_onset"]:
            intensity_score += 30
            flags.append(f"HIGH DECISION COUNT: {total_decisions} decisions (fatigue onset at 10)")

        if total_decisions > self.COGNITIVE_THRESHOLDS["critical_decision_points"]:
            intensity_score += 20
            flags.append(f"CRITICAL: {total_decisions} decisions exceeds degradation threshold")

        # Check for working memory overload
        if max_options_single_step > self.COGNITIVE_THRESHOLDS["working_memory_limit"]:
            intensity_score += 25
            flags.append(f"WORKING MEMORY OVERLOAD: {max_options_single_step} options in single step (limit: 7±2)")

        # Check for fatigue-positioned upsells
        late_upsells = [
            s for i, s in enumerate(flow_steps)
            if s.get('contains_upsell') and i >= len(flow_steps) * 0.7  # Last 30% of flow
        ]

        if late_upsells:
            intensity_score += 25
            flags.append(f"FATIGUE POSITIONING: {len(late_upsells)} upsell(s) positioned in final steps")

        # Check for time pressure combined with complexity
        time_pressured_complex = [
            s for s in flow_steps
            if s.get('time_pressure') and s.get('options_presented', 0) > 5
        ]

        if time_pressured_complex:
            intensity_score += 20
            flags.append("SYSTEM 1 HIJACK: Time pressure + high complexity (forces emotional decision)")

        return {
            "intensity_score": min(intensity_score, 100),
            "total_decisions_required": total_decisions,
            "max_options_single_step": max_options_single_step,
            "flags": flags,
            "potential_improvement": "35.26% conversion increase possible with simplified flow",
            "recommendation": self._generate_recommendation(intensity_score, total_decisions)
        }

    def _generate_recommendation(self, score: float, decisions: int) -> str:
        if score < 25:
            return "Flow appears reasonable for cognitive load"
        elif score < 50:
            return f"Consider reducing decisions from {decisions} to under 10"
        elif score < 75:
            return "Significant cognitive load concerns detected - recommend user flow audit"
        else:
            return "CRITICAL: Flow appears designed to leverage decision fatigue - regulatory risk"
```

---

## PART 5: VARIABLE RATIO REINFORCEMENT - NEW DETECTOR

### Key Findings

Variable ratio reinforcement (VR) schedules are the most resistant to extinction and most associated with high-engagement behaviors. Research shows:

- Slot machines using VR schedules create **compulsive engagement**
- Same mechanics used in social media, gaming, and e-commerce
- Activates **dopamine pathways similarly to habit-forming substances**

### Detection Implementation

```python
class VariableRatioReinforcementDetector:
    """
    Detect variable ratio reinforcement (slot machine) mechanics.
    Based on behavioral research and game design analysis.
    """

    # Common VR mechanics in digital products
    VR_MECHANICS = {
        "loot_boxes": {
            "indicators": [
                "random reward", "mystery box", "surprise",
                "chance to win", "rare item", "legendary",
                "epic drop", "unlock random"
            ],
            "visual_cues": [
                "spinning wheel", "card flip", "chest opening",
                "slot animation", "gacha", "pull"
            ]
        },
        "infinite_scroll": {
            "indicators": [
                "endless content", "keep scrolling",
                "more content below", "infinite feed",
                "algorithmic recommendations"
            ]
        },
        "notification_variability": {
            "indicators": [
                "someone liked", "new follower",
                "you have X notifications", "trending now",
                "breaking", "just posted"
            ]
        },
        "near_miss_mechanics": {
            "indicators": [
                "so close", "almost won", "just missed",
                "try again", "one more", "nearly there"
            ],
            "psychological_effect": "Heightens engagement despite loss - borrowed from slot machines"
        }
    }

    def detect_vr_mechanics(self, product_features: List[str], ui_description: str = None) -> Dict:
        """
        Detect variable ratio reinforcement mechanics in product/app.
        """

        score = 0
        detected_mechanics = []

        combined_text = ' '.join(product_features).lower()
        if ui_description:
            combined_text += ' ' + ui_description.lower()

        # Check each VR mechanic category
        for mechanic_name, mechanic_data in self.VR_MECHANICS.items():
            indicators = mechanic_data.get("indicators", [])
            visual_cues = mechanic_data.get("visual_cues", [])

            indicator_matches = sum(1 for i in indicators if i in combined_text)
            visual_matches = sum(1 for v in visual_cues if v in combined_text)

            if indicator_matches > 0 or visual_matches > 0:
                score += 20 + (indicator_matches * 5) + (visual_matches * 10)
                detected_mechanics.append({
                    "mechanic": mechanic_name,
                    "indicator_matches": indicator_matches,
                    "visual_matches": visual_matches,
                    "concern": mechanic_data.get("psychological_effect", "VR schedule creates compulsive engagement")
                })

        return {
            "vr_reinforcement_score": min(score, 100),
            "detected_mechanics": detected_mechanics,
            "engagement_intensity": self._assess_engagement_intensity(score),
            "mechanism": "VR schedules activate dopamine pathways similarly to substances",
            "regulatory_context": "Belgium and Netherlands have banned loot boxes as gambling"
        }

    def _assess_engagement_intensity(self, score: float) -> str:
        if score < 20:
            return "LOW - Minimal VR mechanics detected"
        elif score < 50:
            return "MODERATE - Some VR mechanics present"
        elif score < 75:
            return "HIGH - Multiple VR mechanics present"
        else:
            return "VERY HIGH - Systematic VR implementation (slot machine design)"
```

---

## PART 6: ANCHORING & DECOY EFFECT - ENHANCED

### Key Findings

- **70% of consumers** admit purchasing decisions are influenced by initial price
- Decoy effect shifts consumer choice to higher-priced targeted item
- Anchoring persists even when anchor is clearly irrelevant

### Classic Examples

| Example | Anchor | Result |
|---------|--------|--------|
| Williams-Sonoma Bread Maker | Added $429 model | $275 model sales increased significantly |
| Campbell's Soup "Limit 12" | Number 12 | Purchases increased from 3.3 to 7 cans |

### Detection Implementation

```python
class EnhancedAnchoringDetector:
    """
    Detect anchoring and decoy pricing effects.
    """

    def detect_pricing_anchors(self, price_display: List[Dict]) -> Dict:
        """
        Analyze pricing display for anchoring techniques.

        Args:
            price_display: List of dicts with:
                - 'product_name': str
                - 'current_price': float
                - 'original_price': float (optional)
                - 'comparison_price': float (optional)
                - 'position': str ('first', 'middle', 'last')
        """

        score = 0
        flags = []

        prices = [p.get('current_price', 0) for p in price_display]

        # Check for high anchor first
        if len(prices) > 1:
            first_price = price_display[0].get('current_price', 0)
            avg_other = sum(prices[1:]) / len(prices[1:])

            if first_price > avg_other * 1.5:
                score += 30
                flags.append(f"HIGH ANCHOR FIRST: First price ({first_price}) is >150% of average others ({avg_other:.2f})")

        # Check for decoy pricing (asymmetric dominance)
        for i, product in enumerate(price_display):
            original = product.get('original_price')
            current = product.get('current_price')

            if original and current:
                discount_pct = (original - current) / original * 100

                # Check for inflated original price
                if discount_pct > 50:
                    score += 25
                    flags.append(f"POTENTIAL INFLATED ANCHOR: {product.get('product_name')} shows {discount_pct:.0f}% discount")

        # Check for decoy products (dominated option)
        self._detect_decoy_products(price_display, flags)

        return {
            "anchoring_score": min(score, 100),
            "flags": flags,
            "consumer_impact": "70% of consumers influenced by initial price anchor",
            "intensity_concern": "Artificially inflated 'original' prices erode trust when discovered"
        }

    def _detect_decoy_products(self, products: List[Dict], flags: List[str]):
        """Detect asymmetrically dominated decoy options"""
        # A decoy is worse than target on all dimensions but close in price
        # Implementation would compare features and prices
        pass
```

---

## PART 7: COMPREHENSIVE AUDIT INTEGRATION

### Combined Framework

```python
class ComprehensivePersuasionAudit:
    """
    Master audit class combining all enhanced detectors.
    Incorporates regulatory frameworks.
    """

    def __init__(self):
        self.fractionation = EnhancedFractionationDetector()
        self.physiological = PhysiologicalFractionationDetector()
        self.interface_patterns = EnhancedInterfaceDesignDetector()
        self.cialdini = EnhancedCialdiniDetector()
        self.cognitive_load = EnhancedCognitiveLoadDetector()
        self.vr_reinforcement = VariableRatioReinforcementDetector()
        self.anchoring = EnhancedAnchoringDetector()

    def full_audit(self, content: Dict) -> Dict:
        """
        Comprehensive audit across all detection categories.

        Args:
            content: Dict containing:
                - 'text': str
                - 'content_sequence': List[Dict] (for fractionation)
                - 'user_flow': List[Dict] (for cognitive load)
                - 'pricing': List[Dict] (for anchoring)
                - 'product_features': List[str] (for VR detection)
                - 'signup_flow': Dict (for roach motel)
                - 'cancel_flow': Dict (for roach motel)
                - 'decline_buttons': List[str] (for confirmshaming)
                - 'reviews': List[Dict] (for fake social proof)
        """

        results = {
            "audit_timestamp": datetime.now().isoformat(),
            "framework_version": "1.0",
            "detections": {},
            "composite_scores": {},
            "regulatory_flags": [],
            "recommendations": []
        }

        # Run all detectors
        if content.get('content_sequence'):
            results["detections"]["fractionation"] = self.fractionation.detect_emotional_sequence(
                content['content_sequence']
            )

        if content.get('decline_buttons'):
            for i, btn in enumerate(content['decline_buttons']):
                results["detections"][f"confirmshaming_{i}"] = self.interface_patterns.detect_confirmshaming(btn)

        if content.get('signup_flow') and content.get('cancel_flow'):
            results["detections"]["roach_motel"] = self.interface_patterns.detect_roach_motel(
                content['signup_flow'], content['cancel_flow']
            )

        if content.get('user_flow'):
            results["detections"]["cognitive_load"] = self.cognitive_load.analyze_user_flow(
                content['user_flow']
            )

        if content.get('product_features'):
            results["detections"]["vr_reinforcement"] = self.vr_reinforcement.detect_vr_mechanics(
                content['product_features']
            )

        if content.get('pricing'):
            results["detections"]["anchoring"] = self.anchoring.detect_pricing_anchors(
                content['pricing']
            )

        if content.get('reviews'):
            results["detections"]["fake_social_proof"] = self.cialdini.detect_fake_social_proof(
                content['reviews']
            )

        # Calculate composite scores
        results["composite_scores"] = self._calculate_composites(results["detections"])

        # Generate regulatory flags
        results["regulatory_flags"] = self._check_regulatory_compliance(results["detections"])

        # Generate recommendations
        results["recommendations"] = self._generate_recommendations(results["detections"])

        return results

    def _calculate_composites(self, detections: Dict) -> Dict:
        """Calculate composite risk scores"""

        scores = []
        for name, result in detections.items():
            if isinstance(result, dict):
                for key in ['score', 'fractionation_score', 'intensity_score',
                           'vr_reinforcement_score', 'anchoring_score', 'asymmetry_score',
                           'manufactured_probability']:
                    if key in result:
                        scores.append(result[key])

        return {
            "average_risk_score": sum(scores) / len(scores) if scores else 0,
            "max_risk_score": max(scores) if scores else 0,
            "categories_flagged": sum(1 for s in scores if s > 50)
        }

    def _check_regulatory_compliance(self, detections: Dict) -> List[str]:
        """Check for regulatory violations"""

        flags = []

        # Check FTC interface design violations
        roach_motel = detections.get('roach_motel', {})
        if roach_motel.get('asymmetry_score', 0) > 60:
            flags.append("FTC RISK: Roach motel pattern may violate FTC Section 5")

        # Check CCPA interface design prohibition
        for key, result in detections.items():
            if 'confirmshaming' in key and result.get('score', 0) > 50:
                flags.append("CCPA RISK: Confirmshaming prohibited under California Consumer Privacy Act")

        # Check EU AI Act emotional influence provisions
        if detections.get('fractionation', {}).get('fractionation_score', 0) > 70:
            flags.append("EU AI ACT RISK: Certain emotional influence techniques classified as high-risk/prohibited")

        return flags

    def _generate_recommendations(self, detections: Dict) -> List[str]:
        """Generate actionable recommendations"""

        recommendations = []

        for name, result in detections.items():
            if isinstance(result, dict) and result.get('flags'):
                for flag in result['flags'][:2]:  # Top 2 flags per category
                    recommendations.append(f"[{name.upper()}] {flag}")

        return recommendations
```

---

**Document Version:** 1.0
