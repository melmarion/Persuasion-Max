# MACHINE-READABLE MANIPULATION DETECTION SYSTEM
## Quantifiable Rules, Regex Patterns, and Algorithmic Decision Trees
**Automated Detection Without Qualitative Interpretation**

---

## OVERVIEW

This system converts ALL influence strategy tactics into **machine-readable formats**:
- Regex patterns for text matching
- Numerical scoring thresholds
- Boolean logic operators
- Quantifiable metrics
- Algorithmic decision trees
- Zero human interpretation required

**Output:** A JSON score for ANY input text showing exact mechanism deployment.

---

## PART 1: TACTICAL STIMULUS DETECTION - QUANTIFIABLE RULES

### STIMULUS 1: PERSONAL (Self-Centered Targeting)

#### Rule 1.1: Exclusion Language Detection

**Pattern Definition (Regex):**
```regex
(?i)(not\s+for\s+everyone|if\s+you\s+know\s+,?\s+you\s+know|for\s+those\s+who\s+recognize|for\s+the\s+\d+\s+people|you'll\s+be\s+illegible)
```

**Scoring Rule:**
```
MATCH FOUND = 20 points per match (max 3 matches = 60 points, capped at 40)
```

**Boolean Logic:**
```
IF regex_match_count >= 1 THEN exclusion_language_detected = TRUE
IF regex_match_count >= 2 THEN intensity = "MODERATE"
IF regex_match_count >= 3 THEN intensity = "STRONG"
```

#### Rule 1.2: Status Threat Language Detection

**Exact String Matching (Case-Insensitive):**
```
"being basic" → 30 points
"fear of being basic" → 30 points
"culturally irrelevant" → 30 points
"algorithmically predictable" → 30 points
"you're still too visible" → 30 points
"your references are being sold back" → 30 points
```

**Scoring Rule:**
```
points = (number_of_exact_matches) × 30
MAX: 100 points (capped)
```

**Machine Decision:**
```
IF points > 60 THEN high_status_threat = TRUE
IF points > 90 THEN extreme_status_threat = TRUE
```

#### Rule 1.3: Tribal Safety Signals Detection

**Pattern Recognition (Substring Matching):**
```
"we understand the references you understand" → 25 points
"silent mutual recognition" → 25 points
"tribal markers" → 25 points
"tribal safety" → 25 points
"obscurity signals" → 25 points
"pre-algorithmic" → 25 points
"post-commercial" → 25 points
```

**Scoring Rule:**
```
FOR EACH exact_substring_found:
  points += 25
TOTAL tribal_score = sum of all matches (no cap)
```

#### STIMULUS 1 Composite Calculation

```
PERSONAL_STIMULUS_SCORE = MIN([
  (exclusion_language_score / 60) × 40,
  (status_threat_score / 90) × 35,
  (tribal_safety_score / 175) × 25
], 100)

If any component > 0:
  intensity = 0-20: "NONE"
           = 21-40: "WEAK"
           = 41-60: "MODERATE"
           = 61-80: "STRONG"
           = 81-100: "EXTREME"
```

---

### STIMULUS 2: CONTRASTABLE (Binary Ideological Framing)

#### Rule 2.1: Binary Pair Detection

**Quantifiable Pairs (Each pair = 30 points if BOTH present):**

```
PAIR_1_MASS = ["mass-produced", "factory", "generic", "manufactured"]
PAIR_1_ARTIFACT = ["artifact", "unique", "evidence", "one-of-a-kind"]

PAIR_2_ALGORITHMIC = ["algorithmic", "predicted", "personalized"]
PAIR_2_AUTHORED = ["authored", "curated", "deliberate", "intentional"]

PAIR_3_VISIBLE = ["visible", "obvious", "legible", "logo"]
PAIR_3_CODED = ["coded", "references", "signals", "obscure"]

PAIR_4_COMMERCIAL = ["commercial", "marketing", "selling"]
PAIR_4_AUTHENTIC = ["authentic", "real", "genuine", "raw"]
```

**Detection Algorithm:**
```
FOR each PAIR in [PAIR_1, PAIR_2, PAIR_3, PAIR_4]:
  pair_found_in_text = (
    ANY_SUBSTRING(text, PAIR[0]) AND
    ANY_SUBSTRING(text, PAIR[1])
  )

  IF pair_found_in_text:
    binary_score += 30
    pairs_count += 1

TOTAL = min(binary_score, 100)
```

#### Rule 2.2: Contrast Markers

**Marker Patterns (10 points each):**
```regex
\bvs\b|↔|not|unlike|instead\s+of|while\s+they|but\s+we|on\s+the\s+other\s+hand
```

**Algorithm:**
```
contrast_markers_count = REGEX_MATCH_COUNT(pattern)
marker_score = contrast_markers_count × 10
MAX = 30 points
```

#### Rule 2.3: Spectrum Language (REDUCES score)

**Spectrum Keywords (-8 points each):**
```
"also offers", "ranges from", "variety", "flexibility",
"multiple options", "for everyone", "something for all"
```

**Algorithm:**
```
spectrum_count = COUNT_EXACT_MATCHES(text, spectrum_keywords)
spectrum_penalty = spectrum_count × 8
contrastable_score = MAX(0, contrastable_score - spectrum_penalty)
```

#### STIMULUS 2 Composite Calculation

```
CONTRASTABLE_SCORE = MIN([
  (pairs_count / 4) × 50,
  (marker_score / 30) × 30,
  100 - spectrum_penalty
], 100)
```

---

### STIMULUS 3: TANGIBLE (Concrete vs. Abstract)

#### Rule 3.1: Material Specificity Patterns

**Pattern Type 1: Weight Specifications**
```regex
(\d+)\s*(gsm|g/m²|lb/yd²|weight)
```
**Scoring:**
- Match found = 20 points
- Exact number extracted = valid match
- "Premium quality" (no number) = 0 points

**Algorithm:**
```
weight_matches = REGEX_EXTRACT(text, weight_pattern)
FOR EACH match:
  IF is_number(match):
    tangible_score += 20
```

**Pattern Type 2: Production Location**
```regex
made\s+in\s+([A-Za-z]+)|manufactured\s+in\s+([A-Za-z\s]+)|factory\s+in\s+
```
**Scoring:**
- Generic ("made in Europe") = 10 points
- Specific city ("made in Portugal") = 20 points
- Narrative detail ("closed Portuguese mill, 2003") = 25 points

**Algorithm:**
```
location_text = REGEX_EXTRACT(text, location_pattern)
location_score = CALCULATE_SPECIFICITY(location_text):
  IF contains_city_name: +20
  IF contains_year_or_date: +5
  IF contains_descriptive_narrative: +5
  ELSE: 10
```

**Pattern Type 3: Material Decay/Change**
```regex
(fades|wears|ages|deteriorates|shrinks|bleeds)\s+([a-z\s]+)?(\d+\s*(month|week|year|%|time))
```
**Scoring:**
- With specific timeline = 20 points
- With percentage = 20 points
- Vague ("will age") = 5 points

**Algorithm:**
```
decay_matches = REGEX_EXTRACT(text, decay_pattern)
FOR EACH match:
  IF contains_timeframe OR contains_percentage:
    tangible_score += 20
  ELSE:
    tangible_score += 5
```

**Pattern Type 4: Sensory Details**
```regex
(smells?|texture|feel|sound|taste|touch)\s+(like|of|is|was)\s+([a-z\s]+)
```
**Scoring:**
- Specific sensory ("smells like zinc and old rain") = 15 points
- Vague ("feels nice") = 3 points

**Algorithm:**
```
sensory_matches = REGEX_EXTRACT(text, sensory_pattern)
sensory_text = extracted_sensory_phrase
sensory_score = LENGTH(sensory_text) > 10_chars ? 15 : 3
```

**Pattern Type 5: Production Artifacts/Imperfections**
```regex
(uneven|visible\s+seams|not\s+identical|handmade|mistakes?|irregularit|one-of-a-kind)
```
**Scoring:**
- Each match = 15 points
- Max 2 matches = 30 points (capped)

#### Rule 3.2: Abstract Language (REDUCES score)

**Abstract Keywords (-5 points each):**
```
"premium quality", "luxury", "elevated", "timeless",
"perfection", "excellence", "superior", "world-class",
"sophisticated", "elegant", "refined", "exquisite",
"impeccable", "top-tier", "best in class"
```

**Algorithm:**
```
abstract_count = COUNT_EXACT_MATCHES(text, abstract_keywords)
abstract_penalty = abstract_count × 5
tangible_score = MAX(0, tangible_score - abstract_penalty)
```

#### STIMULUS 3 Composite Calculation

```
TANGIBLE_SCORE = MIN([
  (weight_score / 20) × 20 +
  (location_score / 25) × 20 +
  (decay_score / 20) × 20 +
  (sensory_score / 15) × 20 +
  (artifacts_score / 30) × 20 -
  (abstract_penalty)
], 100)
```

---

### STIMULUS 4: MEMORABLE (U-Curve Structure)

#### Rule 4.1: Structural Analysis (Line-Based)

**Algorithm:**
```
total_lines = COUNT_LINES(text)
first_third_line_num = total_lines / 3
last_third_line_start = (total_lines × 2) / 3

opening_section = lines[0:first_third_line_num]
middle_section = lines[first_third_line_num:last_third_line_start]
closing_section = lines[last_third_line_start:total_lines]
```

#### Rule 4.2: Opening Strength Detection

**System Signals (20 points each):**
```regex
(archive\s+\d+|collection|series|episode|chapter)\b
```

**Cryptic/Memorable Openings (20 points each):**
```regex
(if\s+you\s+recognize|grainy|stark|cryptic|ambiguous|unknown|forgotten|unearthed)
```

**Scoring:**
```
opening_score = 0
FOR EACH regex_match IN opening_section:
  opening_score += 20

IF length(opening_section) < 30_chars:
  opening_score += 10 (brevity = memorability)
```

#### Rule 4.3: Closing Strength Detection

**Unresolved/Ambiguous Closings (20 points each):**
```regex
(or\s+you\s+were\s+already|you\s+decide|the\s+rest\s+is\s+up\s+to\s+you|never\s+resolve|if\s+you've?\s+found|question\s+mark)
```

**Scoring:**
```
closing_score = 0
FOR EACH regex_match IN closing_section:
  closing_score += 20

IF closing_line_ends_with_question_mark:
  closing_score += 10
```

#### Rule 4.4: Middle Weakness Detection

**Filler Words (-5 points each):**
```regex
(also|additionally|moreover|furthermore|and\s+we\s+also|choose\s+from|various|traditional)
```

**Scoring:**
```
filler_count = REGEX_MATCH_COUNT(pattern, middle_section)
middle_weakness = filler_count × 5
```

#### STIMULUS 4 Composite Calculation

```
MEMORABLE_SCORE = MIN([
  (opening_score / 40) × 40 +
  (closing_score / 40) × 40 +
  MAX(0, 20 - middle_weakness)
], 100)

IF opening_score > 0 AND closing_score > 0 AND middle_weakness > 0:
  u_curve_detected = TRUE
  MEMORABLE_SCORE += 20
```

---

### STIMULUS 5: VISUAL (Anti-Aesthetic vs. Polished)

#### Rule 5.1: Anti-Aesthetic Keywords

**Anti-Aesthetic Terms (15 points each):**
```
"grainy", "blur", "bad lighting", "accidental crop", "mistakes",
"CCTV", "found footage", "webcam quality", "documentary",
"cold", "unvarnished", "raw", "unedited", "unfiltered",
"bad white balance", "cropped awkwardly", "harsh shadow",
"shot on phone", "not made for Instagram"
```

**Scoring:**
```
anti_aesthetic_count = COUNT_EXACT_MATCHES(text, anti_aesthetic_terms)
anti_aesthetic_score = anti_aesthetic_count × 15
```

#### Rule 5.2: No-Models/Styling Terms (15 points each)

**Keywords:**
```
"no models", "on hangers", "on the floor", "strangers in background",
"not styled", "no styling", "no moments", "just recording"
```

**Scoring:**
```
no_styling_count = COUNT_EXACT_MATCHES(text, no_styling_terms)
no_styling_score = no_styling_count × 15
```

#### Rule 5.3: Mood Board Approach (10 points each)

**Keywords:**
```
"mood board", "references", "gallery", "Russian Constructivism",
"Brutalist", "90s rave", "film stills", "archive", "unlabeled"
```

**Scoring:**
```
mood_board_count = COUNT_EXACT_MATCHES(text, mood_board_terms)
mood_board_score = mood_board_count × 10
```

#### Rule 5.4: Polished Language (REDUCES score)

**Polished Keywords (-10 points each):**
```
"beautiful", "stunning", "gorgeous", "elegant", "clean", "pristine",
"professional photography", "lifestyle", "aspirational", "gloss",
"luxury aesthetic", "refined"
```

**Scoring:**
```
polished_count = COUNT_EXACT_MATCHES(text, polished_keywords)
polished_penalty = polished_count × 10
visual_score = MAX(0, visual_score - polished_penalty)
```

#### STIMULUS 5 Composite Calculation

```
VISUAL_SCORE = MIN([
  (anti_aesthetic_score / 60) × 35 +
  (no_styling_score / 30) × 30 +
  (mood_board_score / 40) × 25 -
  (polished_penalty)
], 100)
```

---

### STIMULUS 6: EMOTIONAL (Fear→Relief Arc)

#### Rule 6.1: Pain/Threat Detection

**Pain Triggers (Exact Match = 15 points each):**
```
pain_keywords = {
  "cultural_irrelevance": ["cultural irrelevance", "outdated", "behind", "forgotten"],
  "algorithmic_threat": ["algorithmic", "predicted for you", "feed algorithm", "your references sold back"],
  "status_anxiety": ["being basic", "normies", "everyone else", "mainstream", "trying too hard"],
  "inauthenticity": ["fake", "commercial", "manufactured", "mass-produced", "cookie cutter"]
}
```

**Algorithm:**
```
pain_score = 0
FOR EACH category IN pain_keywords:
  FOR EACH keyword IN category.keywords:
    IF exact_match(text, keyword):
      pain_score += 15
```

#### Rule 6.2: Relief Signals Detection

**Relief Keywords (15 points each):**
```
relief_keywords = {
  "esoteric_access": ["if you know you know", "get it", "understanding the reference", "in-group knowledge"],
  "escape_offered": ["we don't have a logo", "not looking for you", "not for everyone", "exit the algorithm"],
  "authenticity_promise": ["authentic", "real", "genuine", "unmanufactured", "artifact"],
  "tribal_safety": ["community of people", "silent recognition", "mutual understanding", "your people"]
}
```

**Algorithm:**
```
relief_score = 0
FOR EACH category IN relief_keywords:
  FOR EACH keyword IN category.keywords:
    IF exact_match(text, keyword):
      relief_score += 15
```

#### Rule 6.3: Complete Arc Detection

**Algorithm:**
```
IF pain_score > 0 AND relief_score > 0:
  emotional_arc_complete = TRUE
  arc_bonus = 25
ELSE IF pain_score > 0 XOR relief_score > 0:
  emotional_arc_complete = FALSE
  arc_bonus = 0
ELSE:
  emotional_arc_complete = FALSE
  arc_bonus = 0
```

#### STIMULUS 6 Composite Calculation

```
EMOTIONAL_SCORE = MIN([
  ((pain_score + relief_score) / 2 / 100) × 100 +
  arc_bonus
], 100)
```

---

## PART 2: PSYCHOLOGICAL PRINCIPLES - QUANTIFIABLE DETECTION

### PRINCIPLE 1: AUTHORITY

#### Rule 1.1: Competence Signal Detection

**Credential Keywords (15 points each):**
```
credentials = [
  "doctor", "dr.", "phd", "expert", "professor",
  "researcher", "scientist", "certified", "licensed",
  "30 years", "industry leader", "award-winning"
]
```

**Institution Keywords (20 points each):**
```
institutions = [
  "harvard", "stanford", "mit", "oxford", "yale",
  "johns hopkins", "mayo clinic"
]
```

**Algorithm:**
```
competence_score = 0
FOR EACH keyword IN credentials:
  IF case_insensitive_match(text, keyword):
    competence_score += 15

FOR EACH institution IN institutions:
  IF case_insensitive_match(text, institution):
    competence_score += 20

competence_total = MIN(competence_score, 100)
```

#### Rule 1.2: Confidence Markers Detection

**Confidence Keywords (10 points each):**
```regex
(steady\s+vocal|unhurried\s+pace|120.*150\s+words|70\%\s+eye\s+contact|relaxed\s+shoulders|slight\s+forward\s+lean|precise\s+language|stillness)
```

**Algorithm:**
```
confidence_matches = REGEX_MATCH_COUNT(pattern)
confidence_score = MIN(confidence_matches × 10, 80)
```

#### Rule 1.3: Threat Reduction

**Threat Keywords (deduct -20 points each):**
```
threat_keywords = ["aggressive", "demanding", "high pressure", "intensity", "angry"]
```

**Algorithm:**
```
threat_count = COUNT_EXACT_MATCHES(text, threat_keywords)
threat_score = threat_count × 20
```

#### PRINCIPLE 1 Authority Formula Calculation

```
AUTHORITY_SCORE = (competence_total + confidence_score) / (threat_score > 0 ? threat_score : 1)

compliance_probability = {
  < 5: "Low (20-30%)",
  5-15: "Moderate (40-50%)",
  15-30: "High (65%+)",
  > 30: "Extreme (65-100%)"
}
```

---

### PRINCIPLE 5: SCARCITY

#### Rule 5.1: Limitation Language

**Keywords (15 points each):**
```regex
(limited\s+edition|only\s+\d+\s+left|scarce|in\s+short\s+supply|running\s+out|while\s+supplies\s+last|rare|exclusive|one-time\s+only|never\s+again)
```

#### Rule 5.2: Competition Language (20 points each)

```regex
(many\s+want|quickly\s+selling|people.*buying|interest\s+is\s+high|others.*getting|don't\s+miss\s+out)
```

#### Rule 5.3: Destruction Language (30 points each)

```regex
(burn.*unsold|destroyed\s+forever|going\s+away\s+forever|never\s+be\s+made|will\s+disappear|last\s+chance\s+forever)
```

#### Rule 5.4: Urgency Language (15 points each)

```regex
(hurry|act\s+now|today\s+only|expires|deadline|before\s+midnight|rush|immediate|don't\s+delay)
```

#### PRINCIPLE 5 Scarcity Score Calculation

```
limitation_score = REGEX_MATCH_COUNT(limitation_pattern) × 15
competition_score = REGEX_MATCH_COUNT(competition_pattern) × 20
destruction_score = REGEX_MATCH_COUNT(destruction_pattern) × 30
urgency_score = REGEX_MATCH_COUNT(urgency_pattern) × 15

SCARCITY_SCORE = MIN([
  limitation_score +
  competition_score +
  destruction_score +
  urgency_score
], 100)
```

---

## PART 3: COMPOSITE SCORING ALGORITHM

### Step 1: Calculate Individual Stimulus Scores

```
tactical_stimulus_scores = {
  "PERSONAL": PERSONAL_STIMULUS_SCORE,
  "CONTRASTABLE": CONTRASTABLE_SCORE,
  "TANGIBLE": TANGIBLE_SCORE,
  "MEMORABLE": MEMORABLE_SCORE,
  "VISUAL": VISUAL_SCORE,
  "EMOTIONAL": EMOTIONAL_SCORE
}

tactical_average = AVERAGE(tactical_stimulus_scores.values())
```

### Step 2: Calculate Individual Principle Scores

```
psychological_principle_scores = {
  "AUTHORITY": AUTHORITY_SCORE,
  "SOCIAL_PROOF": SOCIAL_PROOF_SCORE,
  "RECIPROCITY": RECIPROCITY_SCORE,
  "COMMITMENT": COMMITMENT_SCORE,
  "SCARCITY": SCARCITY_SCORE,
  "LIKING": LIKING_SCORE,
  "UNITY": UNITY_SCORE
}

psychological_average = AVERAGE(psychological_principle_scores.values())
```

### Step 3: Advanced Frameworks

```
advanced_scores = {
  "COGNITIVE_LOAD": COGNITIVE_LOAD_SCORE,
  "DECISION_FATIGUE": DECISION_FATIGUE_SCORE,
  "INOCULATION": INOCULATION_SCORE,
  "ENVIRONMENTAL_PRIMING": ENVIRONMENTAL_PRIMING_SCORE
}

advanced_average = AVERAGE(advanced_scores.values())
```

### Step 4: Final Composite Score

```
COMPOSITE_MANIPULATION_SCORE = (
  (tactical_average × 0.35) +
  (psychological_average × 0.35) +
  (advanced_average × 0.30)
)

MIN_COMPOSITE = 0
MAX_COMPOSITE = 100

IF COMPOSITE_MANIPULATION_SCORE > 100:
  COMPOSITE_MANIPULATION_SCORE = 100
```

### Step 5: Risk Categorization

```
risk_level = {
  0-25: "LOW (Ethical messaging)",
  26-50: "MODERATE (Some targeting)",
  51-75: "HIGH (Sophisticated influence strategy)",
  76-100: "EXTREME (Weaponized tactics)"
}
```

---

## PART 4: JSON OUTPUT FORMAT

### Input
```json
{
  "content": "Your marketing text here",
  "audit_id": "unique_identifier",
  "timestamp": "ISO_8601_timestamp"
}
```

### Output Structure

```json
{
  "audit_id": "unique_identifier",
  "timestamp": "ISO_8601_timestamp",
  "content_hash": "SHA256_hash_of_input",
  "content_length": 1024,

  "tactical_stimulus": {
    "PERSONAL": {
      "score": 65,
      "intensity": "STRONG",
      "matches": [
        {"keyword": "not for everyone", "points": 20, "location": "line 2"},
        {"keyword": "if you know you know", "points": 20, "location": "line 3"}
      ]
    },
    "CONTRASTABLE": {
      "score": 48,
      "intensity": "MODERATE",
      "pairs_detected": 1,
      "marker_count": 3
    },
    "TANGIBLE": {
      "score": 72,
      "intensity": "CONCRETE",
      "material_specifics_count": 5,
      "abstract_penalty": 15
    },
    "MEMORABLE": {
      "score": 61,
      "intensity": "CLEAR_U_CURVE",
      "opening_strength": 30,
      "closing_strength": 25,
      "middle_weakness": 8,
      "u_curve_detected": true
    },
    "VISUAL": {
      "score": 58,
      "intensity": "ANTI_AESTHETIC",
      "anti_aesthetic_count": 4,
      "polished_penalty": 10
    },
    "EMOTIONAL": {
      "score": 74,
      "intensity": "STRONG_ARC",
      "pain_score": 45,
      "relief_score": 45,
      "arc_complete": true
    },
    "tactical_average": 63
  },

  "psychological_principles": {
    "AUTHORITY": {
      "score": 52,
      "formula_result": 13,
      "competence": 40,
      "confidence": 20,
      "threat": 5,
      "compliance_probability": "High (65%+)"
    },
    "SOCIAL_PROOF": {
      "score": 41,
      "consensus_signals": 2,
      "similarity_signals": 1,
      "uncertainty_context": true
    },
    "RECIPROCITY": {
      "score": 35,
      "give_first_signals": 2,
      "obligation_language": 1
    },
    "COMMITMENT": {
      "score": 28,
      "small_commitment_present": true,
      "escalation_present": false,
      "public_commitment": false
    },
    "SCARCITY": {
      "score": 65,
      "limitation_signals": 2,
      "competition_signals": 2,
      "destruction_signals": 1,
      "urgency_signals": 2,
      "strongest_mechanism": "competition"
    },
    "psychological_average": 44
  },

  "advanced_frameworks": {
    "COGNITIVE_LOAD": {
      "score": 38,
      "complexity_signals": 2,
      "time_pressure_signals": 1,
      "distraction_signals": 2
    },
    "DECISION_FATIGUE": {
      "score": 42,
      "decision_multiplications": 3,
      "sequential_asks": 2,
      "fatigue_positioning": true
    },
    "INOCULATION": {
      "score": 55,
      "objection_introductions": 2,
      "validations": 2,
      "refutations": 2,
      "complete_inoculation_cycles": 2
    },
    "advanced_average": 45
  },

  "composite_scores": {
    "tactical_stimulus_average": 63,
    "psychological_principles_average": 44,
    "advanced_frameworks_average": 45,
    "overall_influence strategy_index": 51,
    "risk_level": "HIGH (Sophisticated influence strategy)"
  },

  "vulnerability_profile": {
    "vulnerable_to_identity_targeting": true,
    "vulnerable_to_ideological_framing": true,
    "vulnerable_to_emotional_arcs": true,
    "vulnerable_to_scarcity": true,
    "total_vulnerability_dimensions": 4
  },

  "red_flags": [
    {
      "category": "PERSONAL_STIMULUS",
      "severity": "HIGH",
      "details": "Strong status threat + exclusion language combination"
    },
    {
      "category": "EMOTIONAL",
      "severity": "HIGH",
      "details": "Complete fear-to-relief arc with high intensity"
    }
  ],

  "machine_flagging_summary": {
    "total_matches_found": 47,
    "high_severity_flags": 5,
    "moderate_severity_flags": 8,
    "low_severity_flags": 34,
    "requires_human_review": false,
    "automation_confidence": 0.94
  }
}
```

---

## PART 5: PYTHON IMPLEMENTATION SKELETON

```python
import re
import json
from typing import Dict, List, Tuple

class MachineReadableDetectionEngine:
    """Quantifiable influence strategy detection without human interpretation"""

    # CONSTANTS - All thresholds as numbers
    PERSONAL_EXCLUSION_POINTS = 20
    PERSONAL_STATUS_THREAT_POINTS = 30
    PERSONAL_TRIBAL_SAFETY_POINTS = 25

    CONTRASTABLE_PAIR_POINTS = 30
    CONTRASTABLE_MARKER_POINTS = 10
    CONTRASTABLE_SPECTRUM_PENALTY = 8

    # Regex patterns as constants
    WEIGHT_PATTERN = r'(\d+)\s*(gsm|g/m²|lb/yd²|weight)'
    LOCATION_PATTERN = r'made\s+in\s+([A-Za-z]+)|manufactured\s+in\s+([A-Za-z\s]+)'
    DECAY_PATTERN = r'(fades|wears|ages|deteriorates|shrinks|bleeds)\s+([a-z\s]+)?(\d+\s*(month|week|year|%))'

    def __init__(self):
        self.results = {}

    def detect_personal_stimulus(self, text: str) -> Dict:
        """Pure quantitative detection - no interpretation"""
        score = 0
        matches = []

        # Rule 1.1: Exclusion language
        exclusion_pattern = r'(?i)(not\s+for\s+everyone|if\s+you\s+know\s+,?\s+you\s+know|for\s+those\s+who)'
        exclusion_matches = re.finditer(exclusion_pattern, text)
        for match in exclusion_matches:
            score += self.PERSONAL_EXCLUSION_POINTS
            matches.append({
                'keyword': match.group(),
                'points': self.PERSONAL_EXCLUSION_POINTS,
                'position': match.start()
            })

        # Rule 1.2: Status threat
        status_threats = [
            "being basic", "culturally irrelevant",
            "algorithmically predictable", "you're still too visible"
        ]
        for threat in status_threats:
            if threat.lower() in text.lower():
                score += self.PERSONAL_STATUS_THREAT_POINTS
                matches.append({
                    'keyword': threat,
                    'points': self.PERSONAL_STATUS_THREAT_POINTS
                })

        # Cap score
        final_score = min(score, 100)

        # Determine intensity
        intensity = 'NONE' if final_score == 0 else \
                   'WEAK' if final_score <= 40 else \
                   'MODERATE' if final_score <= 60 else \
                   'STRONG' if final_score <= 80 else \
                   'EXTREME'

        return {
            'stimulus': 'PERSONAL',
            'score': final_score,
            'intensity': intensity,
            'match_count': len(matches),
            'matches': matches
        }

    def detect_scarcity_principle(self, text: str) -> Dict:
        """Pure quantification of scarcity tactics"""
        score = 0
        components = {}

        # Limitation (15 points each)
        limitation_pattern = r'(?i)(limited\s+edition|only\s+\d+\s+left|scarce|never\s+again)'
        limitation_matches = len(re.findall(limitation_pattern, text))
        limitation_score = limitation_matches * 15
        components['limitation'] = {
            'matches': limitation_matches,
            'points': limitation_score
        }
        score += limitation_score

        # Competition (20 points each)
        competition_pattern = r'(?i)(many\s+want|quickly\s+selling|others.*getting|don\'t\s+miss\s+out)'
        competition_matches = len(re.findall(competition_pattern, text))
        competition_score = competition_matches * 20
        components['competition'] = {
            'matches': competition_matches,
            'points': competition_score
        }
        score += competition_score

        # Destruction (30 points each - most powerful)
        destruction_pattern = r'(?i)(burn.*unsold|destroyed\s+forever|never\s+be\s+made|last\s+chance\s+forever)'
        destruction_matches = len(re.findall(destruction_pattern, text))
        destruction_score = destruction_matches * 30
        components['destruction'] = {
            'matches': destruction_matches,
            'points': destruction_score
        }
        score += destruction_score

        # Cap and categorize
        final_score = min(score, 100)

        return {
            'principle': 'SCARCITY',
            'score': final_score,
            'components': components,
            'total_scarcity_signals': sum([c['matches'] for c in components.values()]),
            'strongest_mechanism': max(components, key=lambda k: components[k]['points'])
        }

    def calculate_composite_score(self, tactical_avg: float,
                                  psychological_avg: float,
                                  advanced_avg: float) -> Dict:
        """Mathematical formula - no interpretation"""

        composite = (
            (tactical_avg * 0.35) +
            (psychological_avg * 0.35) +
            (advanced_avg * 0.30)
        )

        # Clamp to 0-100
        composite = max(0, min(composite, 100))

        # Categorize by numerical threshold only
        if composite <= 25:
            risk = "LOW"
        elif composite <= 50:
            risk = "MODERATE"
        elif composite <= 75:
            risk = "HIGH"
        else:
            risk = "EXTREME"

        return {
            'composite_score': round(composite, 2),
            'risk_level': risk,
            'weights': {
                'tactical': 0.35,
                'psychological': 0.35,
                'advanced': 0.30
            }
        }

    def audit(self, content: str) -> Dict:
        """Complete quantitative audit"""

        # Calculate all components
        personal = self.detect_personal_stimulus(content)
        scarcity = self.detect_scarcity_principle(content)
        # ... (all other detectors)

        # Average by category
        tactical_avg = 63.0  # Example
        psychological_avg = 44.0
        advanced_avg = 45.0

        # Composite
        composite = self.calculate_composite_score(
            tactical_avg, psychological_avg, advanced_avg
        )

        return {
            'audit_timestamp': '2026-02-02T00:00:00Z',
            'content_length': len(content),
            'personal_stimulus': personal,
            'scarcity_principle': scarcity,
            'composite': composite,
            'machine_flagging_confidence': 0.94
        }

# Usage
engine = MachineReadableDetectionEngine()
result = engine.audit("Your text here")
print(json.dumps(result, indent=2))
```

---

## PART 6: DECISION TREES (BOOLEAN LOGIC)

### Decision Tree 1: Immediate Red Flag Detection

```
IF PERSONAL_SCORE > 60 AND EMOTIONAL_SCORE > 70:
  THEN immediate_red_flag = TRUE
  REASON: "Strong identity targeting + complete fear-relief arc"

IF SCARCITY_SCORE > 70 AND DESTRUCTION_SIGNALS > 0:
  THEN immediate_red_flag = TRUE
  REASON: "Destruction threat detected - highest scarcity intensity"

IF AUTHORITY_SCORE > 50 AND THREAT_SCORE == 0:
  THEN immediate_red_flag = TRUE
  REASON: "High authority with zero threat = maximum compliance"

IF DECISION_FATIGUE_SCORE > 50 AND FATIGUE_POSITIONING == TRUE:
  THEN immediate_red_flag = TRUE
  REASON: "Big ask positioned after decision depletion"
```

### Decision Tree 2: Audience Vulnerability Assessment

```
IF PERSONAL_SCORE > 50:
  vulnerable_audience = "Identity-conscious" (fear of being basic)

IF CONTRASTABLE_SCORE > 50:
  vulnerable_audience += "Ideologically-driven" (binary thinkers)

IF EMOTIONAL_ARC_COMPLETE == TRUE AND EMOTIONAL_SCORE > 60:
  vulnerable_audience += "Emotionally-responsive" (pain→relief cycle)

IF SCARCITY_SCORE > 60 AND COMPETITION_SIGNALS > 2:
  vulnerable_audience += "Status-conscious" (FOMO/territorial)
```

### Decision Tree 3: Influence strategy Intensity Classification

```
IF COMPOSITE_SCORE <= 25:
  classification = "ETHICAL"
  actions_required = "NONE"

ELSE IF COMPOSITE_SCORE <= 50:
  classification = "MODERATE"
  actions_required = "MONITOR"

ELSE IF COMPOSITE_SCORE <= 75:
  classification = "HIGH"
  actions_required = "REVIEW_REQUIRED"

ELSE:
  classification = "EXTREME"
  actions_required = "IMMEDIATE_REMEDIATION"
```

---

## PART 7: THRESHOLDS AS LOOKUP TABLES

### Intensity Thresholds (Quantitative Only)

```json
{
  "thresholds": {
    "STIMULUS_INTENSITY": {
      "NONE": [0, 20],
      "WEAK": [21, 40],
      "MODERATE": [41, 60],
      "STRONG": [61, 80],
      "EXTREME": [81, 100]
    },
    "PRINCIPLE_INTENSITY": {
      "NOT_PRESENT": [0, 25],
      "WEAK": [26, 50],
      "MODERATE": [51, 75],
      "STRONG": [76, 100]
    },
    "COMPLIANCE_PROBABILITY": {
      "LOW": [0, 5],
      "MODERATE": [6, 15],
      "HIGH": [16, 30],
      "EXTREME": [31, 100]
    }
  }
}
```

---

**This system is 100% quantifiable and automatable. No human interpretation required. Output is pure numerical scores, boolean flags, and categorical assignments based on algorithmic thresholds.**

