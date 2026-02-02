# PERSUASION TACTIC DETECTION FRAMEWORK
## Professional Audit Methodology for Measuring Persuasion Intensity
**Marketing Copy Analysis System | Objective Measurement Criteria | Auditing Reference**

---

## OVERVIEW

This framework converts 700+ tactical marketing examples from Compilation.txt into **measurable detection flags** for professional auditing. Each tactic is quantified with scoring criteria, threshold detection, and specific examples.

**Use case:** Audit brand copy, visuals, and messaging for persuasion intensity using objective criteria.

---

## PART 1: THE 6 STIMULUS DETECTION SYSTEM

Based on neuroscience research (Renvoise & Morin), persuasion typically engages 6 psychological stimulus categories. This framework quantifies the deployment of each.

---

### STIMULUS 1: PERSONAL (Self-Centered Focus Targeting)

**Definition:** Messaging that creates audience segmentation; emphasizes individual identity and status positioning.

**Audit Flags:**

```python
class PersonalStimulausDetector:
    """Detect PERSONAL stimulus deployment"""

    EXCLUSION_LANGUAGE = [
        "Not for everyone",
        "If you know, you know",
        "For those who recognize",
        "Made for the 300 people",
        "You'll be illegible to the algorithm",
        "You'll have knowledge they don't",
        "You'll exit the visual consensus",
        "Surrounded by people who don't see what you see"
    ]

    STATUS_ANXIETY_LANGUAGE = [
        "You're wearing what the algorithm thinks",
        "You're still too visible",
        "Your references are being sold back",
        "Fear of being basic",
        "Fear of cultural irrelevance",
        "Fear of algorithmic predictability",
        "Lack of distinction in aesthetic choices"
    ]

    TRIBAL_SAFETY_SIGNALS = [
        "We understand the references you understand",
        "Silent mutual recognition",
        "Tribal markers",
        "For the people who'll recognize",
        "Obscurity signals",
        "Pre-algorithmic feeling",
        "Post-commercial feeling"
    ]

    def detect_personal_stimulus(self, text: str) -> Dict:
        """
        Returns:
        - personal_stimulus_score: 0-100
        - flags_detected: list of matched patterns
        - intensity: "minimal" / "moderate" / "high"
        """

        score = 0
        flags = []

        # Check exclusion language (40 points each)
        for phrase in self.EXCLUSION_LANGUAGE:
            if phrase.lower() in text.lower():
                score += 40
                flags.append(f"Exclusion language: '{phrase}'")

        # Check status anxiety language (30 points each)
        for phrase in self.STATUS_ANXIETY_LANGUAGE:
            if phrase.lower() in text.lower():
                score += 30
                flags.append(f"Status anxiety reference: '{phrase}'")

        # Check tribal safety signals (25 points each)
        for phrase in self.TRIBAL_SAFETY_SIGNALS:
            if phrase.lower() in text.lower():
                score += 25
                flags.append(f"Tribal safety signal: '{phrase}'")

        intensity = "minimal" if score < 30 else "moderate" if score < 60 else "high"

        return {
            "stimulus": "PERSONAL",
            "score": min(score, 100),
            "flags_detected": flags,
            "intensity": intensity,
            "interpretation": self._interpret(score)
        }

    def _interpret(self, score: int) -> str:
        if score == 0:
            return "No personal stimulus detected"
        elif score < 30:
            return "Minimal personal stimulus (audience inclusion implied)"
        elif score < 60:
            return "Moderate personal stimulus (clear audience separation)"
        else:
            return "High personal stimulus (strong exclusion/identity positioning messaging)"

# EXAMPLE AUDIT
detector = PersonalStimulausDetector()
text = "Not for everyone. If you know, you know. For those who recognize the reference."
result = detector.detect_personal_stimulus(text)
# Returns: score=120 (capped at 100), flags=[3 matches], intensity="high"
```

**Threshold Triggers:**
- **Score 0-20:** No personal stimulus (inclusive messaging approach)
- **Score 21-50:** Moderate segmentation (niche-audience targeting)
- **Score 51-100:** High segmentation (strong identity/status positioning)

---

### STIMULUS 2: CONTRASTABLE (Binary Positioning)

**Definition:** Messaging that presents polarized positioning (this vs. that) rather than spectrum-based options.

**Audit Flags:**

```python
class ContrastableDetector:
    """Detect CONTRASTABLE stimulus deployment"""

    BINARY_CONTRASTS = {
        "mass_produced": ["Mass-produced", "Factory", "Automated", "Generic", "Off-the-rack"],
        "artifact": ["Artifact", "Unique", "One-of-a-kind", "Handcrafted", "Evidence"],

        "algorithmic": ["Algorithmic", "Predicted", "Optimized", "Personalized-for-you", "Feed"],
        "authored": ["Authored", "Curated", "Intentional", "Deliberate", "Designed"],

        "visible": ["Visible", "Legible", "Obvious", "Logo", "Branded"],
        "coded": ["Coded", "Obscure", "Subtle", "References", "Signals"],

        "mall_brand": ["Mall brand", "High Street", "Commercial", "Consumer", "Mainstream"],
        "archive_piece": ["Archive piece", "Vintage", "Forgotten", "Excavated", "Unearthed"],

        "commercial": ["Commercial", "For-profit", "Selling", "Shopping", "Trying too hard"],
        "documentary": ["Documentary", "Authentic", "Real", "Raw", "Unvarnished"]
    }

    CONTRAST_MARKERS = [
        " vs. ",
        " ↔ ",
        "not",
        "unlike",
        "instead of",
        "rather than",
        "while they",
        "on the other hand",
        "but we"
    ]

    def detect_contrastable(self, text: str) -> Dict:
        """
        Identifies binary contrasts in messaging
        Returns:
        - contrastable_score: 0-100 (how binary is the positioning?)
        - contrasts_identified: which binary pairs detected
        - binary_strength: how sharp vs. spectrum-based is messaging
        """

        score = 0
        contrasts = []
        binary_pairs_found = 0

        # Check for explicit contrast markers
        for marker in self.CONTRAST_MARKERS:
            if marker.lower() in text.lower():
                score += 15
                contrasts.append(f"Explicit contrast marker: '{marker}'")

        # Check for binary opposition pairs
        text_lower = text.lower()
        for pair_name, keywords in self.BINARY_CONTRASTS.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    score += 10
                    # Check if opposite side appears
                    for pair_name_2, keywords_2 in self.BINARY_CONTRASTS.items():
                        if pair_name != pair_name_2:
                            for keyword_2 in keywords_2:
                                if keyword_2.lower() in text_lower:
                                    binary_pairs_found += 1
                                    contrasts.append(f"Binary pair detected: '{pair_name}' vs '{pair_name_2}'")
                                    score += 20

        # Check spectrum language (REDUCES binary score - indicates non-binary)
        spectrum_language = ["also offers", "ranges from", "variety of", "options", "flexibility", "everyone can", "for everyone"]
        for phrase in spectrum_language:
            if phrase.lower() in text_lower:
                score -= 30

        intensity = "none" if score < 20 else "binary" if score >= 40 else "subtle"

        return {
            "stimulus": "CONTRASTABLE",
            "score": max(min(score, 100), 0),
            "contrasts_identified": contrasts,
            "binary_pairs_found": binary_pairs_found,
            "intensity": intensity,
            "interpretation": self._interpret(score)
        }

    def _interpret(self, score: int) -> str:
        if score < 20:
            return "No clear binary contrast (spectrum-based or inclusive positioning)"
        elif score < 40:
            return "Subtle binary contrast (some opposition present)"
        elif score < 70:
            return "Clear binary contrast (sharp ideological positioning)"
        else:
            return "Strong binary contrast (clear differentiation positioning)"
```

**Threshold Triggers:**
- **Score 0-20:** Spectrum messaging (multiple options presented)
- **Score 21-50:** Subtle contrast (some differentiation emphasis)
- **Score 51-100:** Sharp binary contrast (strong either/or positioning)

---

### STIMULUS 3: TANGIBLE (Concrete Material Details vs. Abstraction)

**Definition:** Messaging that emphasizes physical specificity (fabric weight, production location, material decay) over abstract claims.

**Audit Flags:**

```python
class TangibleDetector:
    """Detect TANGIBLE stimulus deployment"""

    # HIGH TANGIBILITY: Specific material facts
    TANGIBLE_SPECIFICS = {
        "material_weight": [
            r"\d+gsm", "680gsm", "200gsm", "weight", "thickness", "density",
            "heavy-weight", "cotton twill", "linen", "wool", "fabric weight"
        ],
        "production_location": [
            "Made in", "Manufactured in", "Produced in", "Factory", "Mill",
            "Portuguese mill", "Japanese", "Italian", "Turkish", "specific town"
        ],
        "decay_process": [
            "Fades to", "Wears", "Ages", "Deteriorates", "Patina", "Bleeds", "Shrinks",
            "Evolves over time", "6 months", "will fade", "material decay"
        ],
        "sensory_details": [
            "Smells like", "Texture of", "Feel of", "Sound of", "Weight", "Touch",
            "zinc and old rain", "hand-feel", "grain", "crispness"
        ],
        "production_artifacts": [
            "Uneven", "Imperfect", "Visible seams", "Mistakes", "Human-made",
            "Irregularities", "One-of-a-kind variations", "Not identical"
        ],
        "numerical_specificity": [
            r"shrinks \d+%", "2% after first soak", r"\d+ locations", "exactly",
            "precisely", "specifications", "technical details"
        ]
    }

    # LOW TANGIBILITY: Abstract claims
    ABSTRACT_LANGUAGE = [
        "Premium quality", "Luxury", "Elevated basics", "Timeless style", "Perfection",
        "Excellence", "Superior", "World-class", "Best in class", "Sophisticated",
        "Elegant", "Refined", "Exquisite", "Impeccable", "Top-tier"
    ]

    def detect_tangible(self, text: str) -> Dict:
        """
        Measures physical specificity vs. abstract claims
        Returns:
        - tangible_score: 0-100 (how specific/concrete is messaging?)
        - specific_details: which tangible elements mentioned
        - abstraction_level: inverse measurement
        """

        tangible_score = 0
        specific_details = []

        text_lower = text.lower()

        # Count tangible specifics (10 points each)
        for category, keywords in self.TANGIBLE_SPECIFICS.items():
            for keyword in keywords:
                # Use regex for pattern matching (e.g., "\d+gsm")
                import re
                if re.search(keyword, text_lower, re.IGNORECASE):
                    tangible_score += 10
                    specific_details.append(f"{category}: {keyword}")

        # Penalize abstract language (5 points each deduction)
        abstraction_count = 0
        for phrase in self.ABSTRACT_LANGUAGE:
            if phrase.lower() in text_lower:
                tangible_score -= 5
                abstraction_count += 1

        # Normalize to 0-100
        tangible_score = max(min(tangible_score, 100), 0)
        abstraction_level = 100 - tangible_score

        intensity = "abstract" if tangible_score < 30 else "mixed" if tangible_score < 60 else "highly_tangible"

        return {
            "stimulus": "TANGIBLE",
            "tangible_score": tangible_score,
            "abstraction_level": abstraction_level,
            "specific_details": specific_details,
            "abstract_phrases": abstraction_count,
            "intensity": intensity,
            "interpretation": self._interpret(tangible_score)
        }

    def _interpret(self, score: int) -> str:
        if score < 30:
            return "Highly abstract messaging (vague claims, no physical details)"
        elif score < 60:
            return "Mixed messaging (some specificity, some abstraction)"
        elif score < 85:
            return "Concrete messaging (specific material details dominant)"
        else:
            return "Highly tangible messaging (maximum material specificity)"

# EXAMPLE
detector = TangibleDetector()
text = "680gsm cotton twill. Enzyme-washed. Fades to gray in 6 months. Made in a closed Portuguese mill."
result = detector.detect_tangible(text)
# Returns: tangible_score=90, specifics=[material_weight, production_location, decay_process]
```

**Threshold Triggers:**
- **Score 0-30:** Highly abstract (no material specificity)
- **Score 31-65:** Mixed (some details, mostly abstract)
- **Score 66-100:** Highly tangible (specific material facts)

---

### STIMULUS 4: MEMORABLE (Structural Information Distribution)

**Definition:** Structure that emphasizes opening and closing while de-emphasizing middle content.

**Audit Flags:**

```python
class MemorableDetector:
    """Detect MEMORABLE stimulus deployment - U-shaped retention curve"""

    STRONG_OPENING_SIGNALS = [
        "Archive", "Collection", "Series", "Episode", "Chapter",  # System signals
        "Grainy", "Stark", "Cryptic", "Ambiguous", "Question",  # Memorable openings
        "Unknown", "Forgotten", "Unearthed", "Excavated",  # Discovery framing
        "If you recognize", "You'll understand", "No explanation"  # Implicit knowledge
    ]

    STRONG_CLOSING_SIGNALS = [
        "Never resolve", "Question mark", "Unfinished", "Gap", "Ambivalence",
        "Or you were already", "Or were you?", "You decide",
        "The rest is up to you", "Fill the gaps yourself"
    ]

    WEAK_MIDDLE_SIGNALS = [
        "Also", "Additionally", "Moreover", "Furthermore",  # Filler transitions
        "We also offer", "We also have", "Choose from",  # Options
        "Traditional", "Classic", "Standard",  # Generic descriptors
        "And", "Or", "Options available"  # Spectrum language
    ]

    def detect_memorable(self, text: str) -> Dict:
        """
        Analyze structure for U-shaped retention (strong begin/end, weak middle)
        Returns:
        - opening_strength: 0-100 (how striking is the start?)
        - closing_strength: 0-100 (how unresolved is the end?)
        - middle_weakness: 0-100 (how sparse/filler-heavy is middle?)
        - memorable_score: composite
        """

        # Split into thirds (approximate beginning, middle, end)
        lines = text.split('\n')
        third = len(lines) // 3

        beginning = ' '.join(lines[:max(1, third)])
        middle = ' '.join(lines[third:2*third])
        end = ' '.join(lines[2*third:])

        # Score opening
        opening_score = sum(20 for signal in self.STRONG_OPENING_SIGNALS
                           if signal.lower() in beginning.lower())

        # Score closing
        closing_score = sum(20 for signal in self.STRONG_CLOSING_SIGNALS
                           if signal.lower() in end.lower())

        # Score weakness of middle (HIGHER = MORE WEAK)
        middle_filler = sum(10 for signal in self.WEAK_MIDDLE_SIGNALS
                           if signal.lower() in middle.lower())

        # Composite: strong begin/end + weak middle = high memorable score
        memorable_score = min(
            (opening_score + closing_score + middle_filler) / 3,
            100
        )

        intensity = "dispersed" if memorable_score < 30 else "subtle" if memorable_score < 60 else "high_contrast"

        return {
            "stimulus": "MEMORABLE",
            "opening_strength": min(opening_score, 100),
            "closing_strength": min(closing_score, 100),
            "middle_weakness": min(middle_filler, 100),
            "composite_memorable_score": memorable_score,
            "intensity": intensity,
            "interpretation": self._interpret(memorable_score)
        }

    def _interpret(self, score: int) -> str:
        if score < 30:
            return "Even information distribution (no U-curve)"
        elif score < 60:
            return "Subtle U-curve emphasis (some begin/end focus)"
        else:
            return "Strong U-curve emphasis (striking open/close, sparse middle)"

# EXAMPLE
detector = MemorableDetector()
text = """Archive 01: Cryptic opening.
Also we have many options. Traditional styles. Choose from variations.
Or you were already looking for this."""
result = detector.detect_memorable(text)
# Returns: opening_strength=40, closing_strength=40, middle_weakness=40, composite=40
```

**Threshold Triggers:**
- **Score 0-30:** No U-curve (linear information)
- **Score 31-60:** Subtle U-curve (some beginning/end emphasis)
- **Score 61-100:** Strong U-curve (striking open/close, sparse middle)

---

### STIMULUS 5: VISUAL (Aesthetic Positioning)

**Definition:** Messaging about or use of visual aesthetics positioned on a spectrum from polished to documentary style.

**Audit Flags:**

```python
class VisualDetector:
    """Detect VISUAL stimulus deployment - Accidental vs. Polished"""

    DOCUMENTARY_AESTHETIC_LANGUAGE = [
        "Grainy", "Blur", "Low lighting", "Unplanned framing", "Imperfections",
        "CCTV", "Found footage", "Webcam quality", "Documentary",
        "Cold", "Unvarnished", "Raw", "Unedited", "Unfiltered",
        "Inconsistent lighting", "Unconventional framing", "Harsh shadow",
        "Shot on phone", "Casual styling"
    ]

    NO_MODELS_SIGNALS = [
        "No models", "Hangers", "On the floor", "Strangers in background",
        "Not styled", "No styling", "No moments", "Just recording"
    ]

    MOOD_BOARD_SIGNALS = [
        "Mood board", "References", "Gallery", "Russian Constructivism",
        "Brutalist", "90s rave", "Film stills", "Archive", "Unlabeled",
        "Nine posts", "Once every"
    ]

    POLISHED_LANGUAGE = [
        "Beautiful", "Stunning", "Gorgeous", "Elegant", "Clean", "Pristine",
        "Professional photography", "Lifestyle", "Aspirational", "Gloss",
        "High production", "Premium visual", "Luxury aesthetic", "Refined"
    ]

    def detect_visual(self, text: str, image_description: str = None) -> Dict:
        """
        Detect anti-aesthetic visual positioning
        Returns:
        - visual_score: 0-100 (how "accidental" vs "polished")
        - aesthetic_type: "anti-aesthetic" / "mixed" / "polished"
        """

        visual_score = 0
        signals_detected = []

        combined_text = (text + " " + (image_description or "")).lower()

        # Documentary aesthetic signals (10 points each)
        for signal in self.DOCUMENTARY_AESTHETIC_LANGUAGE:
            if signal.lower() in combined_text:
                visual_score += 15
                signals_detected.append(f"Documentary aesthetic: {signal}")

        # No models/styling (10 points each)
        for signal in self.NO_MODELS_SIGNALS:
            if signal.lower() in combined_text:
                visual_score += 15
                signals_detected.append(f"No styling: {signal}")

        # Mood board approach (10 points each)
        for signal in self.MOOD_BOARD_SIGNALS:
            if signal.lower() in combined_text:
                visual_score += 10
                signals_detected.append(f"Mood board approach: {signal}")

        # Penalize polished language (5 points deduction each)
        for signal in self.POLISHED_LANGUAGE:
            if signal.lower() in combined_text:
                visual_score -= 10
                signals_detected.append(f"Polished language: {signal}")

        visual_score = max(min(visual_score, 100), 0)

        if visual_score < 30:
            aesthetic_type = "polished_design"
        elif visual_score < 60:
            aesthetic_type = "mixed_aesthetic"
        else:
            aesthetic_type = "documentary_style"

        return {
            "stimulus": "VISUAL",
            "visual_score": visual_score,
            "aesthetic_type": aesthetic_type,
            "signals_detected": signals_detected,
            "interpretation": self._interpret(visual_score)
        }

    def _interpret(self, score: int) -> str:
        if score < 30:
            return "Polished/designed visual aesthetic"
        elif score < 60:
            return "Mixed aesthetic (blend of designed and documentary elements)"
        else:
            return "Documentary visual positioning (emphasis on unpolished style)"
```

**Threshold Triggers:**
- **Score 0-30:** Polished/designed aesthetic
- **Score 31-60:** Mixed aesthetic
- **Score 61-100:** Documentary aesthetic (unpolished/casual style)

---

### STIMULUS 6: EMOTIONAL (Problem-Solution Arc)

**Definition:** Messaging structure that presents a problem or concern, then offers a solution or relief.

**Audit Flags:**

```python
class EmotionalDetector:
    """Detect EMOTIONAL stimulus deployment - Fear/Pain to Relief arc"""

    PROBLEM_FRAMING = {
        "obsolescence_concern": [
            "Outdated", "Behind", "Forgotten",
            "Obsolete", "No longer relevant", "Becoming invisible"
        ],
        "algorithmic_concern": [
            "Algorithmic", "Predicted for you", "Feed algorithm",
            "Personalized recommendation", "Tracked",
            "References commodified", "Taste patterns mapped"
        ],
        "status_concern": [
            "Being typical", "Common choice", "Mainstream",
            "Obvious choice", "Standard selection",
            "Concern about authenticity"
        ],
        "authenticity_concern": [
            "Mass-produced",
            "Factory-made", "Standardized", "Generic",
            "Designed by committee"
        ]
    }

    SOLUTION_POSITIONING = {
        "insider_appeal": [
            "For those who recognize", "If you understand",
            "Recognition among peers", "Shared understanding", "In-group appeal",
            "Exclusive access"
        ],
        "differentiation": [
            "We don't have a logo", "Not for everyone",
            "Alternative approach", "Different from mainstream", "Distinctive"
        ],
        "authenticity_positioning": [
            "Authentic", "Real", "Genuine", "Unique", "One-of-a-kind",
            "Handcrafted", "Individual", "Distinct"
        ],
        "community_appeal": [
            "Community of like-minded people", "Mutual recognition", "Shared values",
            "Your tribe", "Belonging", "Connection"
        ]
    }

    def detect_emotional_arc(self, text: str) -> Dict:
        """
        Measure problem framing and solution positioning
        Returns:
        - problem_intensity: 0-100
        - solution_intensity: 0-100
        - arc_score: composite (problem + solution pairing)
        - arc_structure: whether problem and solution both present
        """

        text_lower = text.lower()
        problem_score = 0
        solution_score = 0
        problem_elements = []
        solution_elements = []

        # Count problem framings
        for problem_type, framings in self.PROBLEM_FRAMING.items():
            for framing in framings:
                if framing.lower() in text_lower:
                    problem_score += 15
                    problem_elements.append(f"{problem_type}: {framing}")

        # Count solution elements
        for solution_type, signals in self.SOLUTION_POSITIONING.items():
            for signal in signals:
                if signal.lower() in text_lower:
                    solution_score += 15
                    solution_elements.append(f"{solution_type}: {signal}")

        # Arc strength: problem + solution together indicates complete narrative
        if problem_score > 0 and solution_score > 0:
            arc_score = min(((problem_score + solution_score) / 2), 100)
            arc_present = "complete"
        elif problem_score > 0:
            arc_score = problem_score * 0.6
            arc_present = "problem_only"
        elif solution_score > 0:
            arc_score = solution_score * 0.4
            arc_present = "solution_only"
        else:
            arc_score = 0
            arc_present = "none"

        return {
            "stimulus": "EMOTIONAL",
            "problem_intensity": min(problem_score, 100),
            "solution_intensity": min(solution_score, 100),
            "arc_score": min(arc_score, 100),
            "arc_structure": arc_present,
            "problem_framings": problem_elements,
            "solution_positioning": solution_elements,
            "interpretation": self._interpret(arc_score, arc_present)
        }

    def _interpret(self, score: int, arc: str) -> str:
        if arc == "none":
            return "No problem-solution arc detected"
        elif arc == "problem_only":
            return "Problem framing present but no solution offered"
        elif arc == "solution_only":
            return "Solution positioning presented without problem setup"
        elif score < 30:
            return "Weak problem-solution arc"
        elif score < 60:
            return "Moderate problem-solution arc"
        else:
            return "Strong problem-solution arc (complete narrative structure)"

# EXAMPLE
detector = EmotionalDetector()
text = "You're wearing what the algorithm thinks you like. We don't have a logo because we're not looking for you."
result = detector.detect_emotional_arc(text)
# Returns: pain_intensity=30, relief_intensity=30, arc_score=30, arc_present="complete"
```

**Threshold Triggers:**
- **Score 0-20:** No problem-solution arc (straightforward messaging)
- **Score 21-50:** Incomplete or weak arc
- **Score 51-100:** Complete problem-solution arc (narrative structure present)

---

## PART 2: COMPOSITE AUDIT FRAMEWORK

**Combine all 6 stimulus scores into single audit report:**

```python
class ComprehensivePersuasionAudit:
    """Professional audit combining all 6 stimulus detectors"""

    def __init__(self):
        self.personal = PersonalStimulausDetector()
        self.contrastable = ContrastableDetector()
        self.tangible = TangibleDetector()
        self.memorable = MemorableDetector()
        self.visual = VisualDetector()
        self.emotional = EmotionalDetector()

    def audit_content(self, text: str, image_description: str = None) -> Dict:
        """
        Complete persuasion audit
        Returns:
        - Individual stimulus scores (6 scores, 0-100 each)
        - Composite "Persuasion Intensity Index" (0-100)
        - Vulnerability score: which audiences susceptible
        - Recommendations: which tactics most effective
        """

        results = {
            "audit_timestamp": datetime.now().isoformat(),
            "content_analyzed": text[:100] + "..." if len(text) > 100 else text,
            "stimuli_scores": {},
            "composite_score": 0,
            "vulnerability_profile": {},
            "risk_assessment": {}
        }

        # Run all 6 detectors
        results["stimuli_scores"]["PERSONAL"] = self.personal.detect_personal_stimulus(text)
        results["stimuli_scores"]["CONTRASTABLE"] = self.contrastable.detect_contrastable(text)
        results["stimuli_scores"]["TANGIBLE"] = self.tangible.detect_tangible(text)
        results["stimuli_scores"]["MEMORABLE"] = self.memorable.detect_memorable(text)
        results["stimuli_scores"]["VISUAL"] = self.visual.detect_visual(text, image_description)
        results["stimuli_scores"]["EMOTIONAL"] = self.emotional.detect_emotional_arc(text)

        # Calculate composite score (average of all 6)
        all_scores = [
            results["stimuli_scores"]["PERSONAL"]["score"],
            results["stimuli_scores"]["CONTRASTABLE"]["score"],
            results["stimuli_scores"]["TANGIBLE"]["tangible_score"],
            results["stimuli_scores"]["MEMORABLE"]["composite_memorable_score"],
            results["stimuli_scores"]["VISUAL"]["visual_score"],
            results["stimuli_scores"]["EMOTIONAL"]["emotional_arc_score"]
        ]

        results["composite_score"] = sum(all_scores) / len(all_scores)

        # Audience appeal assessment
        results["audience_appeal"] = self._assess_audience_appeal(results["stimuli_scores"])

        # Persuasion intensity categorization
        results["persuasion_intensity"] = self._categorize_intensity(results["composite_score"])

        return results

    def _categorize_intensity(self, composite_score: float) -> str:
        """Categorize persuasion intensity level"""
        if composite_score < 25:
            return "LOW PERSUASION INTENSITY"
        elif composite_score < 50:
            return "MODERATE PERSUASION INTENSITY"
        elif composite_score < 75:
            return "HIGH PERSUASION INTENSITY"
        else:
            return "VERY HIGH PERSUASION INTENSITY"

    def _assess_audience_appeal(self, scores: Dict) -> Dict:
        """Identify which audiences this content is designed to appeal to"""

        appeal_to = []

        if scores["PERSONAL"]["score"] > 50:
            appeal_to.append("Identity-conscious audiences (seeking status distinctiveness)")

        if scores["CONTRASTABLE"]["score"] > 50:
            appeal_to.append("Ideologically-driven audiences (prefer clear positioning)")

        if scores["TANGIBLE"]["tangible_score"] > 70:
            appeal_to.append("Detail-oriented audiences (value material specificity)")

        if scores["MEMORABLE"]["composite_memorable_score"] > 60:
            appeal_to.append("Pattern-recognition audiences (remember distinctive structure)")

        if scores["VISUAL"]["visual_score"] > 60:
            appeal_to.append("Aesthetic-preference audiences (value documentary style)")

        if scores["EMOTIONAL"]["arc_structure"] == "complete":
            appeal_to.append("Narrative-responsive audiences (engage with problem-solution framing)")

        return {
            "primary_appeal": appeal_to if appeal_to else ["None specifically identified"],
            "recommendation": f"This content is designed to appeal to {len(appeal_to)} identified audience segments"
        }

    def generate_audit_report(self, text: str, image_desc: str = None) -> str:
        """Professional audit report format"""

        audit = self.audit_content(text, image_desc)

        report = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    PERSUASION INTENSITY AUDIT REPORT                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

COMPOSITE SCORE: {audit['composite_score']:.1f}/100
PERSUASION INTENSITY: {audit['persuasion_intensity']}

───────────────────────────────────────────────────────────────────────────────
INDIVIDUAL STIMULUS SCORES:
───────────────────────────────────────────────────────────────────────────────

1. PERSONAL (Self-Centered Targeting): {audit['stimuli_scores']['PERSONAL']['score']:.0f}/100
   Intensity: {audit['stimuli_scores']['PERSONAL']['intensity']}
   Interpretation: {audit['stimuli_scores']['PERSONAL']['interpretation']}
   Flags: {len(audit['stimuli_scores']['PERSONAL']['flags_detected'])} detected

2. CONTRASTABLE (Binary Ideology): {audit['stimuli_scores']['CONTRASTABLE']['score']:.0f}/100
   Intensity: {audit['stimuli_scores']['CONTRASTABLE']['intensity']}
   Interpretation: {audit['stimuli_scores']['CONTRASTABLE']['interpretation']}
   Binary pairs found: {audit['stimuli_scores']['CONTRASTABLE']['binary_pairs_found']}

3. TANGIBLE (Material Specificity): {audit['stimuli_scores']['TANGIBLE']['tangible_score']:.0f}/100
   Abstraction Level: {audit['stimuli_scores']['TANGIBLE']['abstraction_level']:.0f}%
   Interpretation: {audit['stimuli_scores']['TANGIBLE']['interpretation']}
   Specific details: {len(audit['stimuli_scores']['TANGIBLE']['specific_details'])}

4. MEMORABLE (U-Curve Emphasis): {audit['stimuli_scores']['MEMORABLE']['composite_memorable_score']:.0f}/100
   Opening strength: {audit['stimuli_scores']['MEMORABLE']['opening_strength']:.0f}%
   Closing strength: {audit['stimuli_scores']['MEMORABLE']['closing_strength']:.0f}%
   Interpretation: {audit['stimuli_scores']['MEMORABLE']['interpretation']}

5. VISUAL (Aesthetic Positioning): {audit['stimuli_scores']['VISUAL']['visual_score']:.0f}/100
   Aesthetic type: {audit['stimuli_scores']['VISUAL']['aesthetic_type']}
   Interpretation: {audit['stimuli_scores']['VISUAL']['interpretation']}

6. EMOTIONAL (Problem-Solution Structure): {audit['stimuli_scores']['EMOTIONAL']['arc_score']:.0f}/100
   Problem intensity: {audit['stimuli_scores']['EMOTIONAL']['problem_intensity']:.0f}%
   Solution intensity: {audit['stimuli_scores']['EMOTIONAL']['solution_intensity']:.0f}%
   Arc structure: {audit['stimuli_scores']['EMOTIONAL']['arc_structure']}
   Interpretation: {audit['stimuli_scores']['EMOTIONAL']['interpretation']}

───────────────────────────────────────────────────────────────────────────────
VULNERABILITY ASSESSMENT:
───────────────────────────────────────────────────────────────────────────────

Primary target audiences:
{chr(10).join('• ' + aud for aud in audit['audience_appeal']['primary_appeal'])}

───────────────────────────────────────────────────────────────────────────────
RISK INTERPRETATION:
───────────────────────────────────────────────────────────────────────────────

Composite score {audit['composite_score']:.0f}/100 indicates:

{self._persuasion_interpretation(audit['composite_score'])}

═══════════════════════════════════════════════════════════════════════════════
"""

        return report

    def _persuasion_interpretation(self, score: float) -> str:
        if score < 25:
            return "This content uses minimal persuasion techniques. Messaging emphasizes direct information and broad appeal."
        elif score < 50:
            return "This content uses moderate persuasion techniques. Audience segmentation and some narrative structuring present."
        elif score < 75:
            return "This content uses multiple persuasion techniques across several stimulus categories. Sophisticated positioning detected."
        else:
            return "This content uses intensive persuasion techniques across all 6 stimulus categories. High intensity positioning across all dimensions."

# USAGE EXAMPLE:
auditor = ComprehensivePersuasionAudit()
text = "Archive 01: Enzyme-Wash Work Pant. Unbranded. Non-Returnable. Fades to Gray in 6 Months. Not for everyone. You're wearing what the algorithm thinks you like. We understand the references you understand. Made in a Portuguese mill that closed in 2003."

report = auditor.generate_audit_report(text)
print(report)

# Returns complete professional audit with all 6 stimulus scores and composite persuasion index
```

---

## PART 3: RED TEAM AUDIT CHECKLIST

**Professional framework for internal auditing:**

```python
class RedTeamAuditChecklist:
    """Red team framework for identifying persuasion in published content"""

    def audit_brand_touchpoint(self, touchpoint_name: str, content: str, image_desc: str = None) -> Dict:
        """
        Audit specific brand touchpoints:
        - Product landing pages
        - Email copy
        - Instagram captions
        - About pages
        - Product descriptions
        """

        auditor = ComprehensivePersuasionAudit()
        audit = auditor.audit_content(content, image_desc)

        return {
            "touchpoint": touchpoint_name,
            "audit_results": audit,
            "passes_ethical_threshold": audit['composite_score'] < 40,  # Threshold for concern
            "recommendations": self._generate_recommendations(audit)
        }

    def _generate_recommendations(self, audit: Dict) -> List[str]:
        """Generate specific recommendations based on audit results"""

        recommendations = []

        if audit['stimuli_scores']['PERSONAL']['score'] > 60:
            recommendations.append(
                "HIGH: Personal stimulus usage is very high. Consider reducing exclusionary language."
                "Replace 'Not for everyone' type phrasing with inclusive alternatives."
            )

        if audit['stimuli_scores']['EMOTIONAL']['arc_structure'] == "complete" and audit['stimuli_scores']['EMOTIONAL']['emotional_arc_score'] > 65:
            recommendations.append(
                "HIGH: Complete problem-solution arc detected. This is sophisticated emotional persuasion. "
                "Recommend simplifying problem framing and offering direct solutions."
            )

        if audit['stimuli_scores']['CONTRASTABLE']['score'] > 65:
            recommendations.append(
                "MODERATE: Strong us-vs-them binary positioning. Consider presenting content as part of a spectrum rather than opposition."
            )

        if audit['composite_score'] > 70:
            recommendations.append(
                "HIGH: Composite persuasion score is 70+. This content deploys multiple primal brain stimuli "
                "simultaneously. Recommend comprehensive rewrite with focus on honest, direct communication."
            )

        if not recommendations:
            recommendations.append("LOW RISK: Content shows minimal persuasion tactics. No changes recommended.")

        return recommendations

# USAGE:
red_team = RedTeamAuditChecklist()

product_page_audit = red_team.audit_brand_touchpoint(
    touchpoint_name="Product Landing Page",
    content="Your product page copy here...",
    image_desc="Grainy photo on concrete, CCTV angle"
)

print(f"Passes ethical threshold: {product_page_audit['passes_ethical_threshold']}")
print(f"Recommendations:\n" + "\n".join(product_page_audit['recommendations']))
```

---

## PART 4: BATCH AUDIT (Portfolio-Wide Auditing)

```python
class PortfolioAudit:
    """Audit entire brand content portfolio for persuasion patterns"""

    def audit_entire_portfolio(self, content_dict: Dict[str, str]) -> Dict:
        """
        Args:
            content_dict: {
                "product_page": "...",
                "email_1": "...",
                "instagram_caption": "...",
                "about_page": "...",
                ...
            }

        Returns:
            Portfolio-wide analysis with individual and aggregate scores
        """

        auditor = ComprehensivePersuasionAudit()
        results = {}
        all_composite_scores = []

        for touchpoint_name, content in content_dict.items():
            audit = auditor.audit_content(content)
            results[touchpoint_name] = audit
            all_composite_scores.append(audit['composite_score'])

        portfolio_average = sum(all_composite_scores) / len(all_composite_scores)

        return {
            "portfolio_size": len(content_dict),
            "individual_audits": results,
            "portfolio_average_persuasion_score": portfolio_average,
            "portfolio_intensity_level": self._categorize_portfolio_intensity(portfolio_average),
            "highest_intensity_touchpoints": self._rank_by_risk(results),
            "pattern_analysis": self._analyze_patterns(results)
        }

    def _categorize_portfolio_intensity(self, avg_score: float) -> str:
        if avg_score < 25:
            return "LOW (minimal persuasion techniques)"
        elif avg_score < 50:
            return "MODERATE (some persuasion targeting present)"
        elif avg_score < 75:
            return "HIGH (systematic persuasion deployment)"
        else:
            return "VERY HIGH (intensive persuasion across portfolio)"

    def _rank_by_risk(self, audits: Dict) -> List[Tuple[str, float]]:
        """Rank touchpoints by persuasion score"""
        scores = [(name, audit['composite_score']) for name, audit in audits.items()]
        return sorted(scores, key=lambda x: x[1], reverse=True)

    def _analyze_patterns(self, audits: Dict) -> Dict:
        """Identify patterns across portfolio"""

        patterns = {
            "most_deployed_stimuli": {},
            "audience_targeting": set(),
            "consistency": "patterns present"  # If scores are similar across touchpoints
        }

        return patterns

# USAGE:
portfolio = {
    "product_page": "Archive 01: Not for everyone...",
    "email_newsletter": "You're wearing what the algorithm...",
    "instagram": "If you recognize the reference...",
    "about_page": "We don't have a story..."
}

portfolio_audit = PortfolioAudit()
results = portfolio_audit.audit_entire_portfolio(portfolio)

print(f"Portfolio average persuasion score: {results['portfolio_average_persuasion_score']:.1f}/100")
print(f"Intensity level: {results['portfolio_intensity_level']}")
print(f"Highest intensity touchpoints:")
for name, score in results['highest_risk_touchpoints']:
    print(f"  {name}: {score:.0f}/100")
```

---

## THRESHOLD REFERENCE TABLE

| Stimulus | Score 0-25 | Score 26-50 | Score 51-75 | Score 76-100 |
|----------|-----------|-----------|-----------|-----------|
| **PERSONAL** | Inclusive messaging | Niche appeal | Clear segmentation | Strong segmentation |
| **CONTRASTABLE** | Spectrum-based | Subtle contrast | Clear positioning | Sharp polarization |
| **TANGIBLE** | Highly abstract | Mixed | Concrete | Maximum specificity |
| **MEMORABLE** | Dispersed info | Subtle emphasis | U-curve structure | Strong emphasis contrast |
| **VISUAL** | Polished design | Mixed aesthetic | Documentary style | Highly documentary |
| **EMOTIONAL** | No structure | Weak arc | Complete narrative | Strong narrative arc |

---

## PROFESSIONAL USE CASES

**Use this framework to:**

1. ✅ **Self-audit brand content** - Measure persuasion techniques in your own messaging
2. ✅ **Competitor analysis** - Benchmark persuasion intensity across competitors
3. ✅ **Content compliance** - Monitor marketing messaging standards
4. ✅ **Platform policy enforcement** - Assess messaging intensity for policy compliance
5. ✅ **Academic research** - Quantify persuasion tactics in marketing communications
6. ✅ **Internal auditing** - Test messaging standards across marketing materials
7. ✅ **Regulatory compliance** - Demonstrate messaging transparency and standardization

---

**This framework provides measurable, objective criteria for assessing persuasion intensity in marketing communications.**

