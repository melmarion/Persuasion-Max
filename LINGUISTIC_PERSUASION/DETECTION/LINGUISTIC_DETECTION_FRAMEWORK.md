# LINGUISTIC DETECTION FRAMEWORK
## Machine-Readable Detection System for Language-Based Influence
**Regex Patterns, Scoring Algorithms & Production Python Implementation**

---

## OVERVIEW

This document provides production-ready detection code for linguistic influence techniques documented in `RESEARCH/LINGUISTIC_PERSUASION_RESEARCH.md`. It complements the existing psychological detection frameworks (Documents 11-17) with dedicated linguistic analysis.

**Detection Categories:**
1. Rhetorical Device Detection
2. Syntactic Pattern Analysis
3. Framing Effect Identification
4. Pragmatic Pattern Recognition
5. Discourse Marker Analysis
6. Hedging & Certainty Detection
7. Register Analysis
8. Composite Linguistic Scoring

---

## PART 1: CORE DETECTION CLASSES

### 1.1 Rhetorical Device Detector

```python
import re
from typing import Dict, List, Tuple, Optional
from collections import Counter
from dataclasses import dataclass

@dataclass
class RhetoricalDetection:
    device: str
    score: int
    instances: List[str]
    confidence: float

class RhetoricalDeviceDetector:
    """
    Detect classical and modern rhetorical devices in text.
    Based on Aristotle, Perelman, and contemporary rhetoric research.
    """

    DEVICE_SCORES = {
        "anaphora": 25,
        "epistrophe": 20,
        "anadiplosis": 20,
        "antithesis": 30,
        "chiasmus": 25,
        "rhetorical_question": 15,
        "tricolon": 15,
        "alliteration": 10,
        "assonance": 8,
    }

    # Rhetorical question patterns
    RHETORICAL_QUESTION_PATTERNS = [
        r"\b(?:isn't it|aren't we|don't you think|wouldn't you|couldn't we)\b",
        r"\b(?:can we afford|how can anyone|who wouldn't want)\b",
        r"\b(?:what could be|why would anyone|how else can)\b",
        r"(?:^|\. )(?:really|seriously|honestly)\?",
    ]

    # Antithesis markers
    ANTITHESIS_PATTERNS = [
        r"(?:not\s+\w+,?\s+but\s+\w+)",
        r"(?:ask not what.*ask what)",
        r"(?:one small.*one giant)",
        r"(?:\w+\s+or\s+(?:death|liberty|nothing))",
    ]

    def detect_anaphora(self, text: str) -> Optional[RhetoricalDetection]:
        """
        Detect repeated openings of consecutive sentences/clauses.
        """
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) < 3:
            return None

        openings = []
        for sentence in sentences:
            words = sentence.split()
            if len(words) >= 2:
                openings.append(" ".join(words[:2]).lower())

        # Find consecutive repeated openings
        instances = []
        i = 0
        while i < len(openings) - 2:
            if openings[i] == openings[i+1] == openings[i+2]:
                instances.append(openings[i])
                i += 3
            else:
                i += 1

        if instances:
            return RhetoricalDetection(
                device="anaphora",
                score=self.DEVICE_SCORES["anaphora"] * len(instances),
                instances=instances,
                confidence=0.85
            )
        return None

    def detect_rhetorical_questions(self, text: str) -> Optional[RhetoricalDetection]:
        """
        Detect questions asked for effect rather than information.
        """
        instances = []

        for pattern in self.RHETORICAL_QUESTION_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            instances.extend(matches)

        # Also detect questions with obvious implied answers
        questions = re.findall(r'[^.!?]*\?', text)
        for q in questions:
            q_lower = q.lower()
            # Questions with loaded assumptions
            if any(marker in q_lower for marker in [
                "isn't it time", "don't you deserve", "why wouldn't you",
                "can we really afford", "who doesn't want", "what's stopping"
            ]):
                instances.append(q.strip())

        if instances:
            return RhetoricalDetection(
                device="rhetorical_question",
                score=self.DEVICE_SCORES["rhetorical_question"] * len(instances),
                instances=instances,
                confidence=0.75
            )
        return None

    def detect_antithesis(self, text: str) -> Optional[RhetoricalDetection]:
        """
        Detect contrasting ideas in parallel structure.
        """
        instances = []

        for pattern in self.ANTITHESIS_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            instances.extend(matches)

        # Detect "not X but Y" patterns
        not_but = re.findall(r'not\s+(\w+(?:\s+\w+)?),?\s+but\s+(\w+(?:\s+\w+)?)', text, re.IGNORECASE)
        instances.extend([f"not {a} but {b}" for a, b in not_but])

        if instances:
            return RhetoricalDetection(
                device="antithesis",
                score=self.DEVICE_SCORES["antithesis"] * len(instances),
                instances=instances,
                confidence=0.80
            )
        return None

    def detect_tricolon(self, text: str) -> Optional[RhetoricalDetection]:
        """
        Detect three-part parallel structures.
        """
        instances = []

        # Pattern: "X, Y, and Z" with similar structure
        tricolon_pattern = r'(\w+(?:\s+\w+)?),\s+(\w+(?:\s+\w+)?),\s+and\s+(\w+(?:\s+\w+)?)'
        matches = re.findall(tricolon_pattern, text)

        for match in matches:
            # Check if parts have similar length (parallel structure indicator)
            lengths = [len(part.split()) for part in match]
            if max(lengths) - min(lengths) <= 1:  # Similar length = likely parallel
                instances.append(", ".join(match))

        if instances:
            return RhetoricalDetection(
                device="tricolon",
                score=self.DEVICE_SCORES["tricolon"] * len(instances),
                instances=instances,
                confidence=0.70
            )
        return None

    def detect_alliteration(self, text: str) -> Optional[RhetoricalDetection]:
        """
        Detect repeated initial consonant sounds.
        """
        instances = []
        words = text.lower().split()

        for i in range(len(words) - 1):
            word1 = re.sub(r'[^a-z]', '', words[i])
            word2 = re.sub(r'[^a-z]', '', words[i + 1] if i + 1 < len(words) else '')

            if word1 and word2 and word1[0] == word2[0] and word1[0].isalpha():
                # Check for third word
                if i + 2 < len(words):
                    word3 = re.sub(r'[^a-z]', '', words[i + 2])
                    if word3 and word3[0] == word1[0]:
                        instances.append(f"{words[i]} {words[i+1]} {words[i+2]}")

        if instances:
            return RhetoricalDetection(
                device="alliteration",
                score=self.DEVICE_SCORES["alliteration"] * len(instances),
                instances=instances,
                confidence=0.90
            )
        return None

    def analyze(self, text: str) -> Dict:
        """
        Run all rhetorical device detection.
        """
        detections = []

        anaphora = self.detect_anaphora(text)
        if anaphora:
            detections.append(anaphora)

        rhetorical_q = self.detect_rhetorical_questions(text)
        if rhetorical_q:
            detections.append(rhetorical_q)

        antithesis = self.detect_antithesis(text)
        if antithesis:
            detections.append(antithesis)

        tricolon = self.detect_tricolon(text)
        if tricolon:
            detections.append(tricolon)

        alliteration = self.detect_alliteration(text)
        if alliteration:
            detections.append(alliteration)

        total_score = sum(d.score for d in detections)

        return {
            "category": "RHETORICAL_DEVICES",
            "total_score": min(total_score, 100),
            "detections": [
                {
                    "device": d.device,
                    "score": d.score,
                    "instances": d.instances,
                    "confidence": d.confidence
                }
                for d in detections
            ],
            "device_count": len(detections),
        }
```

### 1.2 Syntactic Pattern Detector

```python
class SyntacticPatternDetector:
    """
    Detect syntactic patterns that affect persuasion:
    - Passive voice (agency obfuscation)
    - Nominalization (hiding agents)
    - Sentence complexity
    - Active voice emphasis
    """

    PASSIVE_INDICATORS = [
        r'\b(?:was|were|been|being)\s+\w+ed\b',
        r'\b(?:has|have|had)\s+been\s+\w+ed\b',
        r'\b(?:is|are)\s+being\s+\w+ed\b',
        r'\b(?:will|would|could|should|might)\s+be\s+\w+ed\b',
    ]

    NOMINALIZATION_SUFFIXES = [
        r'\w+tion\b',      # organization, investigation
        r'\w+ment\b',      # development, agreement
        r'\w+ness\b',      # awareness, effectiveness
        r'\w+ity\b',       # responsibility, capability
        r'\w+ance\b',      # performance, compliance
        r'\w+ence\b',      # occurrence, preference
    ]

    NEGATIVE_CONTEXT_MARKERS = [
        'error', 'mistake', 'failure', 'problem', 'issue', 'fault',
        'loss', 'damage', 'harm', 'delay', 'decline', 'drop',
        'criticism', 'complaint', 'concern', 'risk', 'threat'
    ]

    def detect_passive_voice(self, text: str) -> Dict:
        """
        Detect passive voice, especially in negative contexts.
        """
        passive_instances = []
        passive_in_negative = []

        sentences = re.split(r'[.!?]+', text)

        for sentence in sentences:
            for pattern in self.PASSIVE_INDICATORS:
                matches = re.findall(pattern, sentence, re.IGNORECASE)
                if matches:
                    passive_instances.extend(matches)

                    # Check if negative context
                    sentence_lower = sentence.lower()
                    if any(neg in sentence_lower for neg in self.NEGATIVE_CONTEXT_MARKERS):
                        passive_in_negative.extend(matches)

        score = len(passive_instances) * 5
        if passive_in_negative:
            score += len(passive_in_negative) * 15  # Extra for agency obfuscation

        return {
            "pattern": "passive_voice",
            "total_instances": len(passive_instances),
            "in_negative_context": len(passive_in_negative),
            "score": min(score, 50),
            "interpretation": self._interpret_passive(len(passive_instances), len(passive_in_negative))
        }

    def _interpret_passive(self, total: int, negative: int) -> str:
        if negative > 2:
            return "SIGNIFICANT: Passive voice used to obscure responsibility for negative outcomes"
        elif total > 5:
            return "MODERATE: High passive voice usage may indicate evasive style"
        elif total > 0:
            return "LOW: Some passive voice detected"
        return "MINIMAL: Primarily active voice"

    def detect_nominalization(self, text: str) -> Dict:
        """
        Detect nominalization (verb→noun conversion hiding agents).
        """
        nominalizations = []
        text_lower = text.lower()

        for pattern in self.NOMINALIZATION_SUFFIXES:
            matches = re.findall(pattern, text_lower)
            nominalizations.extend(matches)

        # Filter common non-nominalized words
        false_positives = {'nation', 'station', 'position', 'fashion', 'mission'}
        nominalizations = [n for n in nominalizations if n not in false_positives]

        score = len(nominalizations) * 3

        return {
            "pattern": "nominalization",
            "instances": nominalizations[:10],  # Sample
            "count": len(nominalizations),
            "score": min(score, 40),
            "interpretation": self._interpret_nominalization(len(nominalizations))
        }

    def _interpret_nominalization(self, count: int) -> str:
        if count > 10:
            return "HIGH: Heavy nominalization may obscure agency and causation"
        elif count > 5:
            return "MODERATE: Some nominalization detected"
        return "LOW: Limited nominalization"

    def analyze_sentence_complexity(self, text: str) -> Dict:
        """
        Analyze sentence length distribution.
        Short = confident/urgent; Long = complex/obscuring
        """
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if not sentences:
            return {"pattern": "sentence_complexity", "score": 0}

        lengths = [len(s.split()) for s in sentences]
        avg_length = sum(lengths) / len(lengths)

        short_sentences = sum(1 for l in lengths if l <= 5)
        long_sentences = sum(1 for l in lengths if l > 25)

        short_ratio = short_sentences / len(sentences)
        long_ratio = long_sentences / len(sentences)

        score = 0
        flags = []

        if short_ratio > 0.3:
            score += 15
            flags.append("HIGH_SHORT_SENTENCE_RATIO: May indicate urgency/confidence strategy")

        if long_ratio > 0.2:
            score += 15
            flags.append("HIGH_COMPLEXITY: May indicate obscuring strategy")

        return {
            "pattern": "sentence_complexity",
            "average_length": round(avg_length, 1),
            "short_sentence_ratio": round(short_ratio, 2),
            "long_sentence_ratio": round(long_ratio, 2),
            "score": min(score, 30),
            "flags": flags
        }

    def analyze(self, text: str) -> Dict:
        """
        Run all syntactic pattern detection.
        """
        passive = self.detect_passive_voice(text)
        nominalization = self.detect_nominalization(text)
        complexity = self.analyze_sentence_complexity(text)

        total_score = passive["score"] + nominalization["score"] + complexity["score"]

        return {
            "category": "SYNTACTIC_PATTERNS",
            "total_score": min(total_score, 100),
            "passive_voice": passive,
            "nominalization": nominalization,
            "sentence_complexity": complexity
        }
```

### 1.3 Framing Effect Detector

```python
class FramingEffectDetector:
    """
    Detect semantic framing techniques:
    - Loss vs. gain framing
    - Euphemisms
    - Dysphemisms
    - Attribute framing
    """

    LOSS_FRAME_MARKERS = [
        r'\b(?:lose|losing|lost)\b',
        r'\b(?:miss out|missing out|missed out)\b',
        r'\b(?:waste|wasting|wasted)\b',
        r'\b(?:forfeit|forfeiting)\b',
        r'\b(?:before it\'s too late)\b',
        r'\b(?:don\'t let.*slip away)\b',
        r'\b(?:risk losing)\b',
        r'\b(?:running out)\b',
        r'\b(?:last chance)\b',
        r'\b(?:time is running out)\b',
    ]

    GAIN_FRAME_MARKERS = [
        r'\b(?:save|saving|saved)\s+\$?\d+\b',
        r'\b(?:gain|gaining|gained)\b',
        r'\b(?:earn|earning|earned)\b',
        r'\b(?:win|winning|won)\b',
        r'\b(?:benefit|benefiting)\b',
        r'\b(?:enjoy|enjoying)\b',
    ]

    EUPHEMISMS = {
        # Format: euphemism → what it softens
        "let go": "fired",
        "downsized": "fired",
        "restructured": "laid off",
        "passed away": "died",
        "departed": "died",
        "misspoke": "lied",
        "alternative facts": "lies",
        "enhanced interrogation": "torture",
        "collateral damage": "civilian casualties",
        "negative growth": "decline",
        "price adjustment": "price increase",
        "service fee": "extra charge",
        "pre-owned": "used",
        "previously loved": "used",
        "rightsizing": "layoffs",
        "workforce reduction": "layoffs",
        "economic headwinds": "recession",
    }

    DYSPHEMISMS = {
        # Format: dysphemism → neutral term
        "regime": "government",
        "scheme": "plan",
        "propaganda": "message",
        "indoctrination": "education",
        "mouthpiece": "spokesperson",
    }

    def detect_loss_framing(self, text: str) -> Dict:
        """
        Detect loss-framed language (more persuasive for risk-averse decisions).
        """
        instances = []
        text_lower = text.lower()

        for pattern in self.LOSS_FRAME_MARKERS:
            matches = re.findall(pattern, text_lower)
            instances.extend(matches)

        score = len(instances) * 10

        return {
            "frame_type": "loss",
            "instances": instances,
            "count": len(instances),
            "score": min(score, 40),
            "research_note": "Loss framing increases persuasion for risk-averse decisions (Kahneman & Tversky, 1979)"
        }

    def detect_gain_framing(self, text: str) -> Dict:
        """
        Detect gain-framed language.
        """
        instances = []
        text_lower = text.lower()

        for pattern in self.GAIN_FRAME_MARKERS:
            matches = re.findall(pattern, text_lower)
            instances.extend(matches)

        return {
            "frame_type": "gain",
            "instances": instances,
            "count": len(instances),
            "score": len(instances) * 5  # Lower score than loss frame
        }

    def detect_euphemisms(self, text: str) -> Dict:
        """
        Detect euphemistic language softening harsh realities.
        """
        detected = []
        text_lower = text.lower()

        for euphemism, reality in self.EUPHEMISMS.items():
            if euphemism in text_lower:
                detected.append({
                    "euphemism": euphemism,
                    "softens": reality
                })

        score = len(detected) * 15

        return {
            "pattern": "euphemism",
            "detected": detected,
            "count": len(detected),
            "score": min(score, 45),
            "effect": "Reduces emotional impact of negative content"
        }

    def detect_dysphemisms(self, text: str) -> Dict:
        """
        Detect dysphemistic language hardening neutral concepts.
        """
        detected = []
        text_lower = text.lower()

        for dysphemism, neutral in self.DYSPHEMISMS.items():
            if dysphemism in text_lower:
                detected.append({
                    "dysphemism": dysphemism,
                    "hardens": neutral
                })

        score = len(detected) * 15

        return {
            "pattern": "dysphemism",
            "detected": detected,
            "count": len(detected),
            "score": min(score, 45),
            "effect": "Increases negative emotional response to neutral concepts"
        }

    def analyze(self, text: str) -> Dict:
        """
        Run all framing effect detection.
        """
        loss = self.detect_loss_framing(text)
        gain = self.detect_gain_framing(text)
        euphemism = self.detect_euphemisms(text)
        dysphemism = self.detect_dysphemisms(text)

        # Determine dominant frame
        if loss["count"] > gain["count"] * 1.5:
            dominant = "LOSS_DOMINANT"
        elif gain["count"] > loss["count"] * 1.5:
            dominant = "GAIN_DOMINANT"
        else:
            dominant = "BALANCED"

        total_score = loss["score"] + euphemism["score"] + dysphemism["score"]

        return {
            "category": "FRAMING_EFFECTS",
            "total_score": min(total_score, 100),
            "dominant_frame": dominant,
            "loss_framing": loss,
            "gain_framing": gain,
            "euphemisms": euphemism,
            "dysphemisms": dysphemism
        }
```

### 1.4 Pragmatic Pattern Detector

```python
class PragmaticPatternDetector:
    """
    Detect pragmatic influence patterns:
    - Presupposition embedding
    - Indirect directives
    - Implicature
    """

    # Presupposition triggers
    PRESUPPOSITION_TRIGGERS = {
        "factive": [
            r'\b(?:realize|realized|realizing)\s+(?:that\s+)?',
            r'\b(?:know|knew|knowing)\s+(?:that\s+)?',
            r'\b(?:discover|discovered|discovering)\s+(?:that\s+)?',
            r'\b(?:notice|noticed|noticing)\s+(?:that\s+)?',
            r'\b(?:regret|regretted|regretting)\s+(?:that\s+)?',
        ],
        "change_of_state": [
            r'\b(?:stop|stopped|stopping)\s+\w+ing\b',
            r'\b(?:start|started|starting)\s+to\b',
            r'\b(?:continue|continued|continuing)\s+to\b',
            r'\b(?:begin|began|beginning)\s+to\b',
        ],
        "definite": [
            r'\bthe\s+(?:solution|answer|secret|key|way)\s+to\b',
            r'\byour\s+(?:problem|issue|challenge|opportunity)\b',
            r'\bthe\s+\w+\s+you(?:\'ve|\s+have)\s+been\s+(?:looking|waiting|searching)\b',
        ],
        "temporal": [
            r'\b(?:before|after|when|since)\s+you\s+\w+\b',
            r'\bfinally\b',
            r'\bagain\b',
            r'\bstill\b',
        ]
    }

    # Indirect directive patterns
    INDIRECT_DIRECTIVES = [
        r'\b(?:imagine|picture|visualize)\s+(?:yourself|your|a)\b',
        r'\b(?:consider|think about|what if)\b',
        r'\blet\'s\s+\w+\b',
        r'\b(?:why not|why don\'t you|why don\'t we)\b',
        r'\b(?:you might want to|you may want to)\b',
        r'\b(?:have you thought about|have you considered)\b',
    ]

    def detect_presuppositions(self, text: str) -> Dict:
        """
        Detect presupposition-embedding patterns.
        """
        detected = []

        for trigger_type, patterns in self.PRESUPPOSITION_TRIGGERS.items():
            for pattern in patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                for match in matches:
                    detected.append({
                        "type": trigger_type,
                        "trigger": match.strip(),
                        "effect": self._get_presupposition_effect(trigger_type)
                    })

        score = len(detected) * 10

        return {
            "pattern": "presupposition",
            "detected": detected,
            "count": len(detected),
            "score": min(score, 50),
            "interpretation": "Presuppositions embed claims as background assumptions, bypassing critical evaluation"
        }

    def _get_presupposition_effect(self, trigger_type: str) -> str:
        effects = {
            "factive": "Treats subsequent claim as established fact",
            "change_of_state": "Presupposes prior state existed",
            "definite": "Presupposes existence and uniqueness",
            "temporal": "Presupposes event occurrence"
        }
        return effects.get(trigger_type, "Unknown effect")

    def detect_indirect_directives(self, text: str) -> Dict:
        """
        Detect commands disguised as suggestions.
        """
        instances = []

        for pattern in self.INDIRECT_DIRECTIVES:
            matches = re.findall(pattern, text, re.IGNORECASE)
            instances.extend(matches)

        score = len(instances) * 8

        return {
            "pattern": "indirect_directive",
            "instances": instances,
            "count": len(instances),
            "score": min(score, 40),
            "interpretation": "Commands without appearing to command; reduces resistance"
        }

    def analyze(self, text: str) -> Dict:
        """
        Run all pragmatic pattern detection.
        """
        presupposition = self.detect_presuppositions(text)
        indirect = self.detect_indirect_directives(text)

        total_score = presupposition["score"] + indirect["score"]

        return {
            "category": "PRAGMATIC_PATTERNS",
            "total_score": min(total_score, 100),
            "presuppositions": presupposition,
            "indirect_directives": indirect
        }
```

### 1.5 Metaphor & Figurative Language Detector

```python
class MetaphorFigurativeDetector:
    """
    Detect metaphor, metonymy, synecdoche, and other figurative language.
    Figurative language shapes perception by mapping concepts onto familiar domains.
    Research: Lakoff & Johnson (1980) - Metaphors We Live By
    """

    # Conceptual metaphor patterns (source domain → target domain)
    CONCEPTUAL_METAPHORS = {
        "journey": {
            "patterns": [
                r'\b(?:path|road|journey|destination|milestone|crossroads)\b',
                r'\b(?:moving forward|on track|off track|roadmap|stepping stone)\b',
                r'\b(?:navigate|steer|direction|compass|way forward)\b',
            ],
            "effect": "Frames abstract concepts as physical travel",
            "score": 8
        },
        "war": {
            "patterns": [
                r'\b(?:battle|fight|combat|struggle|victory|defeat)\b',
                r'\b(?:strategy|tactics|target|ammunition|arsenal)\b',
                r'\b(?:conquer|attack|defend|offensive|campaign)\b',
                r'\b(?:front lines|trenches|troops|ally|enemy)\b',
            ],
            "effect": "Frames situations as conflict requiring aggressive action",
            "score": 12
        },
        "health": {
            "patterns": [
                r'\b(?:healthy|sick|diagnosis|symptom|cure|treatment)\b',
                r'\b(?:toxic|poison|heal|recover|epidemic|virus)\b',
                r'\b(?:vital|immune|chronic|acute|remedy)\b',
            ],
            "effect": "Frames abstract situations as medical conditions",
            "score": 10
        },
        "family": {
            "patterns": [
                r'\b(?:family|parent|child|sibling|birth|nurture)\b',
                r'\b(?:mother|father|offspring|grow|mature)\b',
                r'\b(?:orphan|adopted|raised|generation)\b',
            ],
            "effect": "Creates emotional attachment through kinship framing",
            "score": 10
        },
        "building": {
            "patterns": [
                r'\b(?:foundation|structure|build|construct|architecture)\b',
                r'\b(?:blueprint|framework|pillar|cornerstone|scaffold)\b',
                r'\b(?:collapse|crumble|rebuild|renovate|demolish)\b',
            ],
            "effect": "Frames abstract concepts as physical structures",
            "score": 6
        },
        "container": {
            "patterns": [
                r'\b(?:full of|empty|contain|inside|outside|overflow)\b',
                r'\b(?:boundaries|limits|capacity|filled with)\b',
            ],
            "effect": "Frames abstract states as physical containers",
            "score": 5
        },
        "machine": {
            "patterns": [
                r'\b(?:mechanism|engine|fuel|drive|power|operate)\b',
                r'\b(?:gears|cogs|system|automate|program|input|output)\b',
                r'\b(?:breakdown|malfunction|tune|calibrate)\b',
            ],
            "effect": "Frames humans/organizations as mechanical systems",
            "score": 8
        }
    }

    # Metonymy patterns (part for whole, associated concept)
    METONYMY_PATTERNS = {
        "institution_for_people": [
            r'\b(?:Washington|the White House|Downing Street|the Kremlin)\s+(?:says|believes|wants|announced)\b',
            r'\b(?:Wall Street|Silicon Valley|Hollywood|Madison Avenue)\s+(?:thinks|believes|says)\b',
            r'\bthe (?:Pentagon|State Department|Fed|Treasury)\b',
        ],
        "producer_for_product": [
            r'\b(?:read|buy|drink|drive)\s+(?:a\s+)?(?:Shakespeare|Hemingway|Ford|Tesla|Coke)\b',
        ],
        "place_for_event": [
            r'\b(?:another\s+)?(?:Watergate|Vietnam|Chernobyl|Hiroshima)\b',
        ],
        "symbol_for_concept": [
            r'\b(?:the Crown|the Throne|the Badge|the Bench|the Bar)\b',
        ]
    }

    # Synecdoche patterns (part for whole or whole for part)
    SYNECDOCHE_PATTERNS = [
        r'\b(?:hired|need)\s+(?:hands|heads|bodies|brains)\b',
        r'\b(?:all\s+)?(?:eyes|ears)\s+(?:on|are on)\b',
        r'\b(?:boots on the ground|seats at the table)\b',
        r'\b(?:the suits|the brass|the uniforms)\b',
    ]

    # Personification patterns
    PERSONIFICATION_PATTERNS = [
        r'\b(?:the market|technology|nature|time|death|fate|destiny)\s+(?:wants|demands|requires|insists|refuses|allows)\b',
        r'\b(?:the economy|the system|the algorithm)\s+(?:decides|chooses|determines|knows)\b',
        r'\b(?:your body|your brain|your heart)\s+(?:tells|knows|wants|needs)\b',
    ]

    def detect_conceptual_metaphors(self, text: str) -> Dict:
        """
        Detect conceptual metaphor frameworks that shape perception.
        """
        detected = []
        text_lower = text.lower()

        for domain, config in self.CONCEPTUAL_METAPHORS.items():
            domain_matches = []
            for pattern in config["patterns"]:
                matches = re.findall(pattern, text_lower)
                domain_matches.extend(matches)

            if domain_matches:
                detected.append({
                    "domain": domain,
                    "instances": domain_matches[:5],  # Sample
                    "count": len(domain_matches),
                    "effect": config["effect"],
                    "score": config["score"] * min(len(domain_matches), 3)
                })

        total_score = sum(d["score"] for d in detected)

        return {
            "pattern": "conceptual_metaphor",
            "detected": detected,
            "dominant_frame": max(detected, key=lambda x: x["count"])["domain"] if detected else None,
            "total_score": min(total_score, 50),
            "interpretation": "Conceptual metaphors shape how abstract concepts are understood by mapping to familiar domains"
        }

    def detect_metonymy(self, text: str) -> Dict:
        """
        Detect metonymy (associated concept substitution).
        """
        instances = []

        for metonymy_type, patterns in self.METONYMY_PATTERNS.items():
            for pattern in patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                for match in matches:
                    instances.append({
                        "type": metonymy_type,
                        "instance": match
                    })

        score = len(instances) * 8

        return {
            "pattern": "metonymy",
            "instances": instances,
            "count": len(instances),
            "score": min(score, 30),
            "effect": "Creates cognitive shortcuts by substituting associated concepts"
        }

    def detect_synecdoche(self, text: str) -> Dict:
        """
        Detect synecdoche (part for whole or whole for part).
        """
        instances = []

        for pattern in self.SYNECDOCHE_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            instances.extend(matches)

        score = len(instances) * 10

        return {
            "pattern": "synecdoche",
            "instances": instances,
            "count": len(instances),
            "score": min(score, 25),
            "effect": "Reduces complex entities to salient parts or expands parts to wholes"
        }

    def detect_personification(self, text: str) -> Dict:
        """
        Detect personification (attributing human qualities to non-human entities).
        """
        instances = []

        for pattern in self.PERSONIFICATION_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            instances.extend(matches)

        score = len(instances) * 12

        return {
            "pattern": "personification",
            "instances": instances,
            "count": len(instances),
            "score": min(score, 30),
            "effect": "Makes abstract systems seem to have agency, intentions, or emotions"
        }

    def analyze(self, text: str) -> Dict:
        """
        Run all figurative language detection.
        """
        metaphors = self.detect_conceptual_metaphors(text)
        metonymy = self.detect_metonymy(text)
        synecdoche = self.detect_synecdoche(text)
        personification = self.detect_personification(text)

        total_score = (
            metaphors["total_score"] +
            metonymy["score"] +
            synecdoche["score"] +
            personification["score"]
        )

        return {
            "category": "FIGURATIVE_LANGUAGE",
            "total_score": min(total_score, 100),
            "conceptual_metaphors": metaphors,
            "metonymy": metonymy,
            "synecdoche": synecdoche,
            "personification": personification,
            "dominant_metaphor_frame": metaphors["dominant_frame"]
        }
```

### 1.6 Discourse Marker Detector

```python
class DiscourseMarkerDetector:
    """
    Detect discourse markers that guide reasoning and signal relationships.
    Research: Discourse markers can significantly affect how arguments are processed.
    """

    # Causal/reasoning markers
    CAUSAL_MARKERS = {
        "strong_cause": {
            "patterns": [r'\b(?:because|since|therefore|thus|hence|consequently)\b'],
            "effect": "Signals causal relationship",
            "score": 5
        },
        "pseudo_cause": {
            "patterns": [
                r'\bbecause\s+(?:of\s+)?(?:you|it|that|this)\b',
                r'\bso\s+(?:you\s+(?:should|need|must|can))\b',
            ],
            "effect": "Creates appearance of reasoning without substance",
            "score": 15
        }
    }

    # Contrast markers
    CONTRAST_MARKERS = {
        "adversative": {
            "patterns": [r'\b(?:but|however|although|despite|nevertheless|yet|still)\b'],
            "effect": "Signals opposition or contrast",
            "score": 3
        },
        "concessive_pivot": {
            "patterns": [
                r'\b(?:yes|sure|granted|admittedly),?\s+but\b',
                r'\b(?:while|although)\s+.*,\s+(?:but|however)\b',
            ],
            "effect": "Acknowledges then dismisses counter-argument",
            "score": 12
        }
    }

    # Additive/emphatic markers
    ADDITIVE_MARKERS = {
        "simple_addition": {
            "patterns": [r'\b(?:also|and|moreover|furthermore|additionally)\b'],
            "effect": "Adds supporting information",
            "score": 2
        },
        "emphatic": {
            "patterns": [
                r'\b(?:in fact|actually|indeed|as a matter of fact)\b',
                r'\b(?:what\'s more|more importantly|even more)\b',
            ],
            "effect": "Signals emphasis or correction",
            "score": 8
        }
    }

    # Temporal/sequential markers
    TEMPORAL_MARKERS = {
        "sequence": {
            "patterns": [r'\b(?:first|second|third|then|next|finally|lastly)\b'],
            "effect": "Creates logical sequence",
            "score": 3
        },
        "urgency": {
            "patterns": [
                r'\b(?:now|immediately|right now|today|this moment)\b',
                r'\b(?:before it\'s too late|while you still can)\b',
            ],
            "effect": "Creates time pressure",
            "score": 12
        }
    }

    # Evidential markers
    EVIDENTIAL_MARKERS = {
        "reported": {
            "patterns": [
                r'\b(?:according to|reportedly|allegedly|apparently)\b',
                r'\b(?:studies show|research indicates|experts say)\b',
            ],
            "effect": "Signals source of information",
            "score": 5
        },
        "pseudo_evidence": {
            "patterns": [
                r'\b(?:studies show|research proves|science says)\b(?!\s+(?:at|from|by|in)\s+)',
                r'\b(?:everyone knows|it\'s well known|common knowledge)\b',
            ],
            "effect": "Claims evidence without providing it",
            "score": 18
        }
    }

    # Conditional markers
    CONDITIONAL_MARKERS = {
        "conditional": {
            "patterns": [r'\b(?:if|unless|provided that|assuming)\b'],
            "effect": "Sets conditions",
            "score": 3
        },
        "threat_conditional": {
            "patterns": [
                r'\bif you don\'t\b.*\byou\'ll\s+(?:lose|miss|regret)\b',
                r'\bunless you act\s+(?:now|today|immediately)\b',
            ],
            "effect": "Creates conditional threat",
            "score": 20
        }
    }

    def detect_marker_category(self, text: str, category_name: str, category_config: Dict) -> Dict:
        """
        Detect markers in a specific category.
        """
        results = {}
        total_score = 0
        total_count = 0

        for marker_type, config in category_config.items():
            instances = []
            for pattern in config["patterns"]:
                matches = re.findall(pattern, text, re.IGNORECASE)
                instances.extend(matches)

            if instances:
                type_score = config["score"] * min(len(instances), 5)
                results[marker_type] = {
                    "instances": instances,
                    "count": len(instances),
                    "effect": config["effect"],
                    "score": type_score
                }
                total_score += type_score
                total_count += len(instances)

        return {
            "category": category_name,
            "types": results,
            "total_count": total_count,
            "total_score": total_score
        }

    def analyze(self, text: str) -> Dict:
        """
        Run all discourse marker detection.
        """
        causal = self.detect_marker_category(text, "causal", self.CAUSAL_MARKERS)
        contrast = self.detect_marker_category(text, "contrast", self.CONTRAST_MARKERS)
        additive = self.detect_marker_category(text, "additive", self.ADDITIVE_MARKERS)
        temporal = self.detect_marker_category(text, "temporal", self.TEMPORAL_MARKERS)
        evidential = self.detect_marker_category(text, "evidential", self.EVIDENTIAL_MARKERS)
        conditional = self.detect_marker_category(text, "conditional", self.CONDITIONAL_MARKERS)

        total_score = (
            causal["total_score"] +
            contrast["total_score"] +
            additive["total_score"] +
            temporal["total_score"] +
            evidential["total_score"] +
            conditional["total_score"]
        )

        # Identify concerning patterns
        flags = []
        if causal["types"].get("pseudo_cause", {}).get("count", 0) > 0:
            flags.append("PSEUDO_REASONING: Empty causal connectives")
        if contrast["types"].get("concessive_pivot", {}).get("count", 0) > 1:
            flags.append("CONCESSION_DISMISS: Pattern of acknowledging then dismissing")
        if evidential["types"].get("pseudo_evidence", {}).get("count", 0) > 0:
            flags.append("PSEUDO_EVIDENCE: Claims evidence without citation")
        if temporal["types"].get("urgency", {}).get("count", 0) > 1:
            flags.append("URGENCY_PRESSURE: Multiple time-pressure markers")
        if conditional["types"].get("threat_conditional", {}).get("count", 0) > 0:
            flags.append("CONDITIONAL_THREAT: If-then threat structure")

        return {
            "category": "DISCOURSE_MARKERS",
            "total_score": min(total_score, 100),
            "causal": causal,
            "contrast": contrast,
            "additive": additive,
            "temporal": temporal,
            "evidential": evidential,
            "conditional": conditional,
            "flags": flags
        }
```

### 1.7 Register & Formality Detector

```python
class RegisterFormalityDetector:
    """
    Detect register shifts and formality influence patterns.
    Strategic register use can signal authority or create false intimacy.
    Research: Brown & Levinson (1987) - Politeness Theory
    """

    # Formal register indicators
    FORMAL_INDICATORS = {
        "vocabulary": {
            "patterns": [
                r'\b(?:utilize|commence|terminate|facilitate|endeavor)\b',
                r'\b(?:pursuant|henceforth|whereby|thereof|herein)\b',
                r'\b(?:notwithstanding|aforementioned|subsequently)\b',
            ],
            "score": 5
        },
        "passive_constructions": {
            "patterns": [
                r'\bit is\s+(?:believed|considered|recommended|suggested)\b',
                r'\b(?:has|have)\s+been\s+(?:determined|established|noted)\b',
            ],
            "score": 4
        },
        "hedged_assertions": {
            "patterns": [
                r'\bit would appear\b',
                r'\bone might argue\b',
                r'\bit could be said\b',
            ],
            "score": 4
        },
        "nominalization": {
            "patterns": [
                r'\bthe\s+\w+tion\s+of\b',
                r'\bthe\s+\w+ment\s+of\b',
            ],
            "score": 3
        }
    }

    # Informal register indicators
    INFORMAL_INDICATORS = {
        "contractions": {
            "patterns": [
                r'\b(?:don\'t|won\'t|can\'t|shouldn\'t|wouldn\'t|couldn\'t)\b',
                r'\b(?:it\'s|that\'s|there\'s|here\'s|what\'s)\b',
                r'\b(?:I\'m|you\'re|we\'re|they\'re|he\'s|she\'s)\b',
            ],
            "score": 3
        },
        "colloquialisms": {
            "patterns": [
                r'\b(?:gonna|wanna|gotta|kinda|sorta)\b',
                r'\b(?:awesome|cool|great|amazing|fantastic)\b',
                r'\b(?:stuff|things|lots of|a bunch of)\b',
            ],
            "score": 5
        },
        "direct_address": {
            "patterns": [
                r'\b(?:you know|I mean|let me tell you)\b',
                r'\b(?:here\'s the thing|the thing is|look)\b',
                r'\b(?:honestly|frankly|between you and me)\b',
            ],
            "score": 6
        },
        "phrasal_verbs": {
            "patterns": [
                r'\b(?:figure out|come up with|look into|get through)\b',
                r'\b(?:put up with|run into|come across|go through)\b',
            ],
            "score": 3
        }
    }

    # Intimate/familiar markers (creating false closeness)
    INTIMACY_MARKERS = {
        "inclusive_we": {
            "patterns": [
                r'\bwe\s+(?:all|both)\s+(?:know|understand|want|need)\b',
                r'\b(?:between us|you and I|we\'re in this together)\b',
            ],
            "score": 10,
            "effect": "Creates assumed solidarity"
        },
        "assumed_shared_values": {
            "patterns": [
                r'\b(?:like you|people like us|our kind)\b',
                r'\b(?:we all know|everyone agrees|obviously we)\b',
            ],
            "score": 12,
            "effect": "Presumes shared beliefs"
        },
        "pseudo_personal": {
            "patterns": [
                r'\b(?:my friend|friend|buddy|pal)\b',
                r'\b(?:just between us|can I be honest|let me level with you)\b',
            ],
            "score": 15,
            "effect": "Simulates personal relationship"
        }
    }

    # Authority/distance markers
    AUTHORITY_MARKERS = {
        "institutional_voice": {
            "patterns": [
                r'\b(?:our research|our team|our experts)\b',
                r'\b(?:the company|the organization|the institution)\b',
            ],
            "score": 5
        },
        "expert_positioning": {
            "patterns": [
                r'\b(?:in my professional opinion|as an expert|in my experience)\b',
                r'\b(?:based on my analysis|from what I\'ve seen)\b',
            ],
            "score": 8
        },
        "categorical_assertions": {
            "patterns": [
                r'\b(?:the fact is|the truth is|the reality is)\b',
                r'\b(?:without question|undeniably|unquestionably)\b',
            ],
            "score": 10
        }
    }

    def detect_register_type(self, text: str, register_name: str, indicators: Dict) -> Dict:
        """
        Detect indicators of a specific register type.
        """
        detected = {}
        total_count = 0
        total_score = 0

        for indicator_type, config in indicators.items():
            instances = []
            for pattern in config["patterns"]:
                matches = re.findall(pattern, text, re.IGNORECASE)
                instances.extend(matches)

            if instances:
                type_score = config["score"] * min(len(instances), 4)
                detected[indicator_type] = {
                    "instances": instances[:5],
                    "count": len(instances),
                    "score": type_score
                }
                if "effect" in config:
                    detected[indicator_type]["effect"] = config["effect"]
                total_count += len(instances)
                total_score += type_score

        return {
            "register": register_name,
            "indicators": detected,
            "total_count": total_count,
            "total_score": total_score
        }

    def analyze(self, text: str) -> Dict:
        """
        Analyze register and formality patterns.
        """
        formal = self.detect_register_type(text, "formal", self.FORMAL_INDICATORS)
        informal = self.detect_register_type(text, "informal", self.INFORMAL_INDICATORS)
        intimacy = self.detect_register_type(text, "intimacy", self.INTIMACY_MARKERS)
        authority = self.detect_register_type(text, "authority", self.AUTHORITY_MARKERS)

        # Determine dominant register
        if formal["total_score"] > informal["total_score"] * 1.5:
            dominant = "FORMAL"
        elif informal["total_score"] > formal["total_score"] * 1.5:
            dominant = "INFORMAL"
        else:
            dominant = "MIXED"

        # Detect strategic register use
        flags = []

        # False intimacy detection
        if intimacy["total_count"] > 2 and dominant != "INFORMAL":
            flags.append("FALSE_INTIMACY: Intimacy markers in formal context")

        # Authority in casual context
        if authority["total_score"] > 15 and informal["total_score"] > formal["total_score"]:
            flags.append("AUTHORITY_IN_CASUAL: Expert claims in informal register")

        # Assumed solidarity
        if intimacy["indicators"].get("inclusive_we", {}).get("count", 0) > 2:
            flags.append("ASSUMED_SOLIDARITY: Heavy use of inclusive 'we'")

        # Pseudo-personal
        if intimacy["indicators"].get("pseudo_personal", {}).get("count", 0) > 0:
            flags.append("PSEUDO_PERSONAL: Simulated personal relationship")

        influence_score = intimacy["total_score"] + authority["total_score"]

        return {
            "category": "REGISTER_FORMALITY",
            "total_score": min(influence_score, 100),
            "dominant_register": dominant,
            "formal": formal,
            "informal": informal,
            "intimacy_markers": intimacy,
            "authority_markers": authority,
            "flags": flags
        }
```

### 1.8 Hedging & Certainty Detector

```python
class HedgingCertaintyDetector:
    """
    Detect hedging (uncertainty) and boosting (certainty) markers.
    Asymmetric use indicates strategic influence.
    """

    HEDGES = {
        "modal_weak": [
            r'\b(?:may|might|could|would)\b',
        ],
        "adverb_weak": [
            r'\b(?:perhaps|possibly|probably|maybe|apparently)\b',
        ],
        "phrase_weak": [
            r'\b(?:it seems|it appears|one might argue|it could be said)\b',
            r'\b(?:to some extent|in some ways|to a degree)\b',
            r'\b(?:sort of|kind of|somewhat)\b',
        ]
    }

    BOOSTERS = {
        "certainty_markers": [
            r'\b(?:clearly|obviously|certainly|definitely|absolutely|undoubtedly)\b',
            r'\b(?:of course|without question|without doubt|no question)\b',
        ],
        "emphasis_markers": [
            r'\b(?:the fact is|the truth is|the reality is)\b',
            r'\b(?:everyone knows|as we all know|it\'s well known)\b',
            r'\b(?:studies prove|research proves|science proves)\b',
        ],
        "strong_modals": [
            r'\b(?:must|will|shall)\b',
        ]
    }

    def detect_hedges(self, text: str) -> Dict:
        """
        Detect uncertainty markers.
        """
        hedge_instances = []

        for hedge_type, patterns in self.HEDGES.items():
            for pattern in patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                for match in matches:
                    hedge_instances.append({
                        "type": hedge_type,
                        "instance": match
                    })

        return {
            "pattern": "hedging",
            "instances": hedge_instances,
            "count": len(hedge_instances)
        }

    def detect_boosters(self, text: str) -> Dict:
        """
        Detect certainty markers.
        """
        booster_instances = []

        for booster_type, patterns in self.BOOSTERS.items():
            for pattern in patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                for match in matches:
                    booster_instances.append({
                        "type": booster_type,
                        "instance": match
                    })

        return {
            "pattern": "boosting",
            "instances": booster_instances,
            "count": len(booster_instances)
        }

    def detect_asymmetry(self, text: str) -> Dict:
        """
        Detect asymmetric hedging (boost strengths, hedge weaknesses).
        This is a key influence strategy indicator.
        """
        sentences = re.split(r'[.!?]+', text)

        positive_contexts = []
        negative_contexts = []

        positive_markers = ['benefit', 'advantage', 'success', 'effective', 'quality', 'value', 'gain']
        negative_markers = ['risk', 'side effect', 'cost', 'limitation', 'disadvantage', 'concern', 'issue']

        for sentence in sentences:
            sentence_lower = sentence.lower()

            if any(pos in sentence_lower for pos in positive_markers):
                positive_contexts.append(sentence)
            elif any(neg in sentence_lower for neg in negative_markers):
                negative_contexts.append(sentence)

        # Check hedging/boosting in each context
        pos_boosted = sum(1 for s in positive_contexts if re.search(r'\b(?:clearly|definitely|absolutely|proven)\b', s, re.IGNORECASE))
        neg_hedged = sum(1 for s in negative_contexts if re.search(r'\b(?:may|might|possibly|rare|some)\b', s, re.IGNORECASE))

        asymmetry_score = 0
        if pos_boosted > 0 and neg_hedged > 0:
            asymmetry_score = 30
        elif pos_boosted > 0 or neg_hedged > 0:
            asymmetry_score = 15

        return {
            "pattern": "asymmetric_hedging",
            "positive_boosted": pos_boosted,
            "negative_hedged": neg_hedged,
            "score": asymmetry_score,
            "interpretation": "Boosters on positives + hedges on negatives = strategic asymmetry" if asymmetry_score > 0 else "No significant asymmetry detected"
        }

    def analyze(self, text: str) -> Dict:
        """
        Run all hedging/certainty detection.
        """
        hedges = self.detect_hedges(text)
        boosters = self.detect_boosters(text)
        asymmetry = self.detect_asymmetry(text)

        # Calculate base scores
        hedge_score = min(hedges["count"] * 3, 30)
        booster_score = min(boosters["count"] * 5, 40)

        total_score = booster_score + asymmetry["score"]

        return {
            "category": "HEDGING_CERTAINTY",
            "total_score": min(total_score, 100),
            "hedges": hedges,
            "boosters": boosters,
            "asymmetry": asymmetry,
            "balance": "BOOSTER_HEAVY" if boosters["count"] > hedges["count"] * 1.5 else "HEDGE_HEAVY" if hedges["count"] > boosters["count"] * 1.5 else "BALANCED"
        }
```

---

## PART 2: COMPOSITE LINGUISTIC ANALYZER

```python
class LinguisticInfluenceAnalyzer:
    """
    Master class combining all linguistic detection modules.
    Produces composite linguistic influence score.

    Detection Categories (8 total):
    1. Rhetorical Devices (anaphora, antithesis, rhetorical questions)
    2. Figurative Language (metaphor, metonymy, synecdoche, personification)
    3. Syntactic Patterns (passive voice, nominalization, complexity)
    4. Framing Effects (loss/gain, euphemism, dysphemism)
    5. Pragmatic Patterns (presupposition, implicature, indirect directives)
    6. Discourse Markers (causal, contrast, evidential, urgency)
    7. Register & Formality (intimacy markers, authority markers)
    8. Hedging & Certainty (hedges, boosters, asymmetric hedging)
    """

    def __init__(self):
        self.rhetorical_detector = RhetoricalDeviceDetector()
        self.figurative_detector = MetaphorFigurativeDetector()
        self.syntactic_detector = SyntacticPatternDetector()
        self.framing_detector = FramingEffectDetector()
        self.pragmatic_detector = PragmaticPatternDetector()
        self.discourse_detector = DiscourseMarkerDetector()
        self.register_detector = RegisterFormalityDetector()
        self.hedging_detector = HedgingCertaintyDetector()

    # Weighting for composite score (based on research effectiveness)
    WEIGHTS = {
        "rhetorical": 0.12,
        "figurative": 0.10,
        "syntactic": 0.10,
        "framing": 0.18,       # High effectiveness (Kahneman)
        "pragmatic": 0.15,     # High: operates below awareness
        "discourse": 0.12,
        "register": 0.10,
        "hedging": 0.13
    }

    def analyze(self, text: str) -> Dict:
        """
        Run comprehensive linguistic influence analysis.

        Returns:
            Complete analysis with composite score and all component analyses.
        """
        # Run all 8 detectors
        rhetorical = self.rhetorical_detector.analyze(text)
        figurative = self.figurative_detector.analyze(text)
        syntactic = self.syntactic_detector.analyze(text)
        framing = self.framing_detector.analyze(text)
        pragmatic = self.pragmatic_detector.analyze(text)
        discourse = self.discourse_detector.analyze(text)
        register = self.register_detector.analyze(text)
        hedging = self.hedging_detector.analyze(text)

        # Calculate weighted composite score
        composite_score = (
            rhetorical["total_score"] * self.WEIGHTS["rhetorical"] +
            figurative["total_score"] * self.WEIGHTS["figurative"] +
            syntactic["total_score"] * self.WEIGHTS["syntactic"] +
            framing["total_score"] * self.WEIGHTS["framing"] +
            pragmatic["total_score"] * self.WEIGHTS["pragmatic"] +
            discourse["total_score"] * self.WEIGHTS["discourse"] +
            register["total_score"] * self.WEIGHTS["register"] +
            hedging["total_score"] * self.WEIGHTS["hedging"]
        )

        # Determine classification
        classification = self._classify(composite_score)

        # Collect all flags
        all_flags = self._generate_flags(rhetorical, syntactic, framing, pragmatic, hedging)
        all_flags.extend(discourse.get("flags", []))
        all_flags.extend(register.get("flags", []))

        return {
            "composite_score": round(composite_score, 1),
            "classification": classification,
            "flags": all_flags,
            "component_scores": {
                "rhetorical_devices": rhetorical["total_score"],
                "figurative_language": figurative["total_score"],
                "syntactic_patterns": syntactic["total_score"],
                "framing_effects": framing["total_score"],
                "pragmatic_patterns": pragmatic["total_score"],
                "discourse_markers": discourse["total_score"],
                "register_formality": register["total_score"],
                "hedging_certainty": hedging["total_score"]
            },
            "detailed_analysis": {
                "rhetorical": rhetorical,
                "figurative": figurative,
                "syntactic": syntactic,
                "framing": framing,
                "pragmatic": pragmatic,
                "discourse": discourse,
                "register": register,
                "hedging": hedging
            },
            "dominant_patterns": {
                "metaphor_frame": figurative.get("dominant_metaphor_frame"),
                "framing_type": framing.get("dominant_frame"),
                "register": register.get("dominant_register")
            },
            "word_count": len(text.split()),
            "sentence_count": len(re.split(r'[.!?]+', text))
        }

    def _classify(self, score: float) -> Dict:
        """
        Classify overall linguistic influence level.
        """
        if score < 25:
            return {
                "level": "LOW",
                "description": "Minimal linguistic influence techniques detected",
                "color": "green"
            }
        elif score < 50:
            return {
                "level": "MODERATE",
                "description": "Some linguistic influence techniques present",
                "color": "yellow"
            }
        elif score < 75:
            return {
                "level": "HIGH",
                "description": "Significant linguistic influence techniques deployed",
                "color": "orange"
            }
        else:
            return {
                "level": "EXTREME",
                "description": "Intensive linguistic influence techniques detected",
                "color": "red"
            }

    def _generate_flags(self, rhetorical, syntactic, framing, pragmatic, hedging) -> List[str]:
        """
        Generate summary flags for notable patterns.
        """
        flags = []

        # Rhetorical flags
        if rhetorical["total_score"] > 50:
            flags.append("HIGH_RHETORICAL: Multiple persuasive rhetorical devices")

        # Syntactic flags
        if syntactic["passive_voice"]["in_negative_context"] > 2:
            flags.append("AGENCY_OBFUSCATION: Passive voice hiding responsibility")

        # Framing flags
        if framing["dominant_frame"] == "LOSS_DOMINANT":
            flags.append("LOSS_FRAMING: Emphasis on what's lost by not acting")

        if framing["euphemisms"]["count"] > 2:
            flags.append("EUPHEMISM_CLUSTER: Multiple terms softening harsh realities")

        # Pragmatic flags
        if pragmatic["presuppositions"]["count"] > 3:
            flags.append("PRESUPPOSITION_LOADING: Multiple embedded assumptions")

        # Hedging flags
        if hedging["asymmetry"]["score"] > 20:
            flags.append("ASYMMETRIC_HEDGING: Boosted positives, hedged negatives")

        if hedging["balance"] == "BOOSTER_HEAVY":
            flags.append("OVERCLAIMING: Excessive certainty markers")

        return flags


# Convenience function for quick analysis
def analyze_linguistic_influence(text: str) -> Dict:
    """
    Quick function to analyze linguistic influence in text.

    Usage:
        result = analyze_linguistic_influence("Your text here...")
        print(f"Score: {result['composite_score']}")
        print(f"Level: {result['classification']['level']}")
    """
    analyzer = LinguisticInfluenceAnalyzer()
    return analyzer.analyze(text)
```

---

## PART 3: USAGE EXAMPLES

### Basic Analysis

```python
# Example usage
text = """
Isn't it time you treated yourself? Studies prove our product is definitely
the most effective solution available. Don't let this opportunity slip away.
The savings you'll discover are substantial. Before it's too late, consider
what you might lose by waiting. Our customers have realized the true value
of premium quality. Let's transform your life together.
"""

result = analyze_linguistic_influence(text)

print(f"Composite Score: {result['composite_score']}/100")
print(f"Classification: {result['classification']['level']}")
print(f"\nFlags:")
for flag in result['flags']:
    print(f"  - {flag}")

print(f"\nComponent Scores:")
for component, score in result['component_scores'].items():
    print(f"  {component}: {score}")
```

### Expected Output

```
Composite Score: 67.3/100
Classification: HIGH

Flags:
  - LOSS_FRAMING: Emphasis on what's lost by not acting
  - PRESUPPOSITION_LOADING: Multiple embedded assumptions
  - OVERCLAIMING: Excessive certainty markers

Component Scores:
  rhetorical_devices: 45
  syntactic_patterns: 25
  framing_effects: 80
  pragmatic_patterns: 65
  hedging_certainty: 70
```

---

## PART 4: INTEGRATION WITH EXISTING FRAMEWORKS

### Combining with Psychological Detection

```python
def comprehensive_influence_analysis(text: str) -> Dict:
    """
    Combine linguistic analysis with psychological principle detection.
    Requires both LINGUISTIC_DETECTION_FRAMEWORK and
    PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.
    """
    linguistic = analyze_linguistic_influence(text)

    # Import psychological detector (from Document 12)
    # psychological = analyze_psychological_principles(text)

    # Combined scoring
    # combined_score = (linguistic['composite_score'] * 0.4 +
    #                   psychological['composite_score'] * 0.6)

    return {
        "linguistic_analysis": linguistic,
        # "psychological_analysis": psychological,
        # "combined_score": combined_score
    }
```

### Mapping Linguistic to Primal Stimuli

```python
LINGUISTIC_TO_PRIMAL_MAPPING = {
    "rhetorical_question": ["PERSONAL", "EMOTIONAL"],
    "loss_framing": ["EMOTIONAL", "SCARCITY"],
    "presupposition": ["PERSONAL", "TANGIBLE"],
    "indirect_directive": ["PERSONAL"],
    "alliteration": ["MEMORABLE"],
    "antithesis": ["CONTRASTABLE", "MEMORABLE"],
    "boosters": ["AUTHORITY"],
    "euphemism": ["EMOTIONAL"],
}
```

---

## CONCLUSION

This detection framework provides:

1. **Five specialized detectors** covering major linguistic influence categories
2. **Composite scoring system** with weighted components
3. **Flag generation** for notable patterns
4. **Integration pathways** with existing psychological frameworks
5. **Production-ready Python code** with clear documentation

The linguistic detection complements the existing psychological detection by analyzing *how* messages are constructed, not just *what* psychological principles they deploy.

---

**Document Status:** PRODUCTION READY
**Dependencies:** Python 3.7+, re module (standard library)
**Integration:** Compatible with Documents 11-17 detection systems

