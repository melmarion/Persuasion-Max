# PROMPT 4: DETECTION CODE, SCORING SYSTEMS & COMPREHENSIVE FRAMEWORKS

> **Consolidation source:** 15_PROFESSIONAL_AUDITOR_MANUAL.md + 17_MACHINE_READABLE_DETECTION_SYSTEM.md + 24_ENHANCED_DETECTION_RESEARCH.md + 26_COMPREHENSIVE_DETECTION_FRAMEWORKS.md + 27_HIGH_IMPACT_DETECTION_SYSTEMS.md
> **Purpose:** Complete machine-readable detection code, scoring algorithms, regex patterns, Python classes, and comprehensive audit frameworks for behavioral science pattern detection.

---

## TABLE OF CONTENTS

1. [PART 1: PROFESSIONAL AUDITOR MANUAL — Exact Language Patterns & Scoring](#part-1)
2. [PART 2: MACHINE-READABLE DETECTION SYSTEM — Regex, Algorithms & JSON Output](#part-2)
3. [PART 3: ENHANCED DETECTION WITH PLATFORM RESEARCH](#part-3)
4. [PART 4: COMPREHENSIVE DETECTION FRAMEWORKS (10 Domains)](#part-4)
5. [PART 5: HIGH-IMPACT DETECTION SYSTEMS (9 Specialized Detectors)](#part-5)
6. [PART 6: MASTER INTEGRATION CLASSES](#part-6)
7. [APPENDIX: Research Sources](#appendix)

---

## PART 1: PROFESSIONAL AUDITOR MANUAL — Exact Language Patterns & Scoring {#part-1}

### 1.1 Primal Brain Stimuli Detection (Renvoise & Morin Framework)

The six stimuli that bypass analytical processing and trigger instinctive responses. Each includes exact language markers, point-based scoring, and intensity classification.

---

#### STIMULUS 1: PERSONAL (Self-Referential Targeting)

**What it does:** Makes content feel individually directed, activating self-referential processing.

**Exact language markers (score each occurrence):**

| Pattern | Points | Example |
|---------|--------|---------|
| Direct "you/your" address | +2 per instance | "Your business deserves..." |
| Name personalization | +5 per instance | "Mario, we noticed..." |
| Behavioral reference | +8 per instance | "Based on your recent search..." |
| Pain-point mirroring | +10 per instance | "Tired of losing customers?" |
| Identity labeling | +7 per instance | "As a serious professional..." |
| Exclusivity framing | +6 per instance | "Not for everyone—only for those who..." |

**Scoring guide:**
- 0-10 points: Minimal personalization (standard marketing)
- 11-25 points: Moderate personalization (targeted campaign)
- 26-50 points: High personalization (behavioral targeting likely)
- 51+ points: Intensive personalization (individual profiling likely)

**Detection regex:**
```
(?i)(you[r]?\s|based on your|we noticed you|as a\s+\w+\s+(professional|leader|expert)|not for everyone)
```

---

#### STIMULUS 2: CONTRASTABLE (Before/After Framing)

**What it does:** Creates clear dichotomy between current pain and promised state, making the "gap" feel urgent.

**Exact language markers:**

| Pattern | Points | Example |
|---------|--------|---------|
| Before/after contrast | +5 per instance | "Before X, you struggled. After X, you thrive." |
| Competitor diminishment | +7 per instance | "Unlike [competitor], we actually..." |
| Status quo pain | +6 per instance | "Still doing it the old way?" |
| Transformation language | +8 per instance | "Transform your results overnight" |
| Numerical contrast | +4 per instance | "From 10 leads to 10,000" |
| Gap amplification | +9 per instance | "The gap between where you are and where you could be..." |

**Scoring guide:**
- 0-10: Minimal contrast (informational comparison)
- 11-25: Moderate contrast (persuasive positioning)
- 26-50: High contrast (deliberate gap amplification)
- 51+: Intensive contrast (manufactured urgency through contrast)

**Detection regex:**
```
(?i)(before\s+\w+.*after|unlike\s+\w+|still\s+(doing|using|stuck)|transform|from\s+\d+.*to\s+\d+|the gap between)
```

---

#### STIMULUS 3: TANGIBLE (Concreteness & Specificity)

**What it does:** Provides specific numbers, timelines, and measurable claims to create perceived reliability.

**Exact language markers:**

| Pattern | Points | Example |
|---------|--------|---------|
| Specific percentages | +3 per instance | "Increase conversions by 47%" |
| Exact timeframes | +4 per instance | "Results in 14 days" |
| Dollar amounts | +5 per instance | "Save $2,847 per month" |
| Case study references | +6 per instance | "Company X increased revenue 312%" |
| Guarantee language | +7 per instance | "100% money-back guarantee" |
| Precision anchoring | +8 per instance | "$2,847" (not "$3,000" — false precision) |

**Scoring guide:**
- 0-10: Standard specificity (normal business communication)
- 11-25: Elevated specificity (persuasive but potentially valid)
- 26-50: High specificity (likely engineered precision)
- 51+: Intensive specificity (precision anchoring pattern)

**Detection regex:**
```
(?i)(\d+\.?\d*\s*%|\$\s*[\d,]+\.?\d*|\d+\s*(days?|hours?|minutes?|weeks?|months?)|guarantee|money[- ]back|results in)
```

**Red flag — false precision:** Watch for oddly specific numbers ($2,847 vs $3,000). Unusual precision (e.g., "47%" rather than "about 50%") triggers anchoring bias more effectively. Score +3 additional points for each instance of false precision.

---

#### STIMULUS 4: MEMORABLE (Sticky Patterns)

**What it does:** Creates cognitive hooks that persist in memory, increasing retrieval likelihood and influencing future decisions.

**Exact language markers:**

| Pattern | Points | Example |
|---------|--------|---------|
| Alliteration | +3 per instance | "Simple, Smart, Scalable" |
| Rhyming/rhythm | +4 per instance | "If it doesn't fit, you must acquit" |
| Rule of three | +5 per instance | "Faster. Cheaper. Better." |
| Metaphor/analogy | +4 per instance | "Your data is a goldmine" |
| Story opening | +6 per instance | "Picture this..." / "Imagine..." |
| Catchphrase/tagline | +7 per instance | Repeated branded phrase |
| Surprising statistic | +5 per instance | "90% of businesses fail because..." |

**Scoring guide:**
- 0-10: Standard communication (normal writing techniques)
- 11-25: Elevated memorability (professional copywriting)
- 26-50: High memorability (deliberate cognitive hook strategy)
- 51+: Intensive memorability (multiple reinforcing hooks)

**Detection regex:**
```
(?i)(imagine|picture this|what if|here's the (thing|truth|secret)|rule of|the\s+\w+\s+of\s+\w+\s+is|remember when)
```

---

#### STIMULUS 5: VISUAL (Imagery & Spatial Patterns)

**What it does:** Activates visual processing, which is faster and more emotionally engaging than text processing alone.

**Exact language markers:**

| Pattern | Points | Example |
|---------|--------|---------|
| Visual verbs | +2 per instance | "See how...", "Look at...", "Watch..." |
| Color/size descriptions | +3 per instance | "The bright red warning sign..." |
| Spatial language | +3 per instance | "Above the fold", "At the top..." |
| Sensory descriptions | +4 per instance | "Feel the smooth texture..." |
| Visualization commands | +5 per instance | "Visualize your success..." |
| Contrast imagery | +6 per instance | "Dark vs. light" visual metaphors |

**Scoring guide:**
- 0-10: Standard visual language
- 11-25: Elevated visual engagement
- 26-50: High visual activation (deliberate sensory strategy)
- 51+: Intensive visual manipulation

**Detection regex:**
```
(?i)(see how|look at|watch (how|this)|visuali[sz]e|picture|imagine.*see|bright|vivid|stunning)
```

---

#### STIMULUS 6: EMOTIONAL (Affect Activation)

**What it does:** Triggers emotional responses that bypass analytical processing. The most powerful stimulus — processes 3,000x faster than rational thought.

**Exact language markers:**

| Pattern | Points | Example |
|---------|--------|---------|
| Fear/threat language | +8 per instance | "Don't get left behind", "Before it's too late" |
| Shame/inadequacy | +9 per instance | "Are you still making this mistake?" |
| Excitement/aspiration | +5 per instance | "Unlock your full potential" |
| Anger/outrage | +7 per instance | "They don't want you to know..." |
| Belonging/exclusion | +8 per instance | "Join thousands who already..." |
| Urgency/FOMO | +10 per instance | "Only 3 spots left" / "Offer expires in..." |
| Relief/comfort | +4 per instance | "Finally, a solution that works" |
| Hope/possibility | +3 per instance | "A brighter future awaits" |

**Scoring guide:**
- 0-10: Minimal emotional appeal (informational)
- 11-25: Moderate emotional appeal (standard persuasion)
- 26-50: High emotional appeal (deliberate emotional targeting)
- 51+: Intensive emotional appeal (emotional manipulation pattern)

**Special rule — Emotional cycling (fractionation):**
If you detect ALTERNATING emotional tones (fear → relief → fear → hope), add +15 per complete cycle. This pattern (A-J-A-R: anger-joy-anger-relief) reduces critical thinking by 200%+ per cycle.

**Detection regex:**
```
(?i)(don't (miss|get left|wait)|before it's too late|last chance|limited time|only \d+ (left|remaining|spots)|act now|hurry|urgent|finally|afraid|worried|scared|excited|thrilled)
```

---

### 1.2 Psychological Principles Detection

#### AUTHORITY PRINCIPLE

**Formula:** Authority = (Competence + Confidence) / Threat

**Language markers:**

| Pattern | Points | Type |
|---------|--------|------|
| Expert citation | +5 | "Harvard researchers found..." |
| Credential display | +4 | "As a certified..." |
| Award/recognition | +3 | "Award-winning..." |
| Statistical backing | +6 | "Studies show that 94%..." |
| Institutional authority | +7 | "The FDA approved..." |
| Manufactured authority | +10 | Fake expert, unverifiable credentials |
| White coat effect | +8 | Visual authority cues (uniforms, settings) |

**Detection regex:**
```
(?i)(stud(y|ies)\s+show|research (proves?|shows?|confirms?)|experts?\s+(say|agree|recommend)|according to|certified|award[- ]winning|approved by|endorsed by|dr\.?\s+\w+\s+(says?|recommends?))
```

**Red flags for manufactured authority:**
- Unverifiable "studies" with no citation
- "Experts agree" without naming experts
- Credentials from unknown institutions
- Authority figure outside their domain of expertise

---

#### SOCIAL PROOF PRINCIPLE

**Language markers:**

| Pattern | Points | Type |
|---------|--------|------|
| Numbers language | +4 | "Over 10,000 customers..." |
| Testimonial patterns | +5 | Quote + name + title |
| Bandwagon language | +6 | "Everyone is switching to..." |
| FOMO social | +7 | "3 people viewing this right now" |
| Rating/review display | +3 | "4.9 stars, 2,847 reviews" |
| Celebrity/influencer | +8 | Known figure endorsement |
| Fake social proof | +12 | Fabricated reviews, bot-like patterns |

**Detection regex:**
```
(?i)(\d+[,\d]*\s*(customers?|users?|people|companies|professionals?)\s+(trust|use|love|chose|switched)|join\s+\d+|rated\s+\d+\.?\d*|★|⭐|verified (purchase|buyer)|as seen (on|in))
```

---

#### RECIPROCITY PRINCIPLE

**Language markers:**

| Pattern | Points | Type |
|---------|--------|------|
| Free offer | +5 | "Free trial", "Free download" |
| Value-first framing | +4 | "Here's a free resource..." |
| Gift language | +6 | "As a gift to you..." |
| Obligation creation | +8 | "After everything we've given you..." |
| Unexpected bonus | +7 | "Plus, we're including..." |
| Reciprocity escalation | +10 | Small free → medium ask → large commitment |

**Detection regex:**
```
(?i)(free\s+(trial|download|access|gift|bonus|guide|ebook|report)|complimentary|no (cost|charge|obligation)|as (a|our) gift|bonus|we('ve| have) (given|provided|shared))
```

---

#### COMMITMENT & CONSISTENCY PRINCIPLE

**Language markers:**

| Pattern | Points | Type |
|---------|--------|------|
| Small yes requests | +5 | "Just enter your email..." |
| Identity reinforcement | +6 | "You're the type who..." |
| Public commitment | +7 | "Share your goal with friends" |
| Sunk cost activation | +8 | "You've already invested..." |
| Progressive disclosure | +6 | Multi-step forms revealing cost late |
| Foot-in-the-door | +9 | Small request → larger request pattern |

**Detection regex:**
```
(?i)(you('ve| have) already|since you (started|joined|signed)|you're the (type|kind)|don't (stop|quit) now|you've come (this|so) far|just (one more|the first) step)
```

---

#### SCARCITY PRINCIPLE

**Language markers:**

| Pattern | Points | Type |
|---------|--------|------|
| Quantity limits | +6 | "Only 5 left" |
| Time limits | +7 | "Offer expires midnight" |
| Exclusive access | +5 | "Invitation only" |
| Countdown timers | +8 | Visual timer display |
| Loss framing | +9 | "Don't miss out" / "You'll lose access" |
| Fake scarcity | +12 | Timers that reset, always "low stock" |

**Detection regex:**
```
(?i)(only \d+\s*(left|remaining|available|spots?|seats?)|limited (time|offer|edition|spots?|availability)|expires?\s+(soon|today|tonight|midnight|in \d+)|while (supplies|stocks?) last|don't miss|last chance|final (offer|chance|call)|act (now|fast|quickly)|hurry)
```

---

### 1.3 Cognitive Bias Detection

#### DECISION FATIGUE

**Mechanism:** After 10-15 decisions, processing capability drops ~40%, making users more susceptible to defaults and suggestions.

**Indicators:**

| Pattern | Points | Indicator |
|---------|--------|-----------|
| Multi-step process | +5 per step beyond 3 | Long signup/checkout flows |
| Excessive options | +3 per option beyond 5 | Paradox of choice |
| Progressive complexity | +6 | Simple → complex question ordering |
| Late-stage upsells | +8 | Offers after decision fatigue likely |
| Default pre-selection | +7 | Pre-checked boxes after many steps |
| Information overload | +5 | Dense text before decision point |

**Detection regex:**
```
(?i)(step \d+ of \d+|continue to (step|next)|almost (done|there|finished)|just one more|final step|before you go|add to (cart|order)|would you also like|recommended for you)
```

---

#### ANCHORING BIAS

**Mechanism:** First number presented creates anchor; subsequent numbers judged relative to it. Anchoring pull: 40-60% toward the anchor.

**Indicators:**

| Pattern | Points | Indicator |
|---------|--------|-----------|
| Strikethrough pricing | +7 | ~~$199~~ → $99 |
| "Was/Now" framing | +6 | "Was $500, now just $199" |
| High-first comparison | +5 | Enterprise ($999) shown before Basic ($49) |
| "Value of" language | +8 | "A $10,000 value for just $497" |
| Per-unit reframing | +4 | "$1/day" instead of "$365/year" |
| Decoy pricing | +9 | Three tiers where middle is clearly best |

**Detection regex:**
```
(?i)(was\s*\$[\d,]+.*now\s*\$[\d,]+|originally\s*\$|save\s*\$[\d,]+|\$[\d,]+\s*value|retail\s*\$|compare at\s*\$|~~\$[\d,]+~~|regular(ly)?\s*\$|just\s*\$[\d.]+\s*\/\s*(day|month|week))
```

---

### 1.4 Inoculation Theory Detection

**Structure:** 3-part pattern — Objection → Validation → Refutation

**Markers:**

| Component | Points | Language |
|-----------|--------|----------|
| Objection raising | +5 | "You might be thinking..." / "Some people say..." |
| Validation | +4 | "That's a fair concern..." / "I understand why..." |
| Refutation | +6 | "But here's what they don't tell you..." |
| Complete cycle | +15 bonus | All three parts in sequence |
| Multiple cycles | +10 per additional | Repeated inoculation pattern |

**Detection regex:**
```
(?i)(you might (be thinking|wonder|ask)|some (people|might) say|I (know|understand) (what you're|you might)|that's a (fair|valid|good) (point|concern|question)|but (here's|what|the (truth|reality|fact)))
```

**Why it matters:** Pre-emptive objection handling disarms skepticism before it forms. When done transparently it's legitimate argumentation; when manipulative, it creates false sense of having "already considered" alternatives.

---

### 1.5 Composite Scoring System

**Formula:**
```
TACTICAL_SCORE = average(Personal, Contrastable, Tangible, Memorable, Visual, Emotional)
PSYCHOLOGICAL_SCORE = average(Authority, Social_Proof, Reciprocity, Commitment, Scarcity)
ADVANCED_SCORE = average(Decision_Fatigue, Anchoring, Inoculation)

COMPOSITE = (TACTICAL_SCORE × 0.35) + (PSYCHOLOGICAL_SCORE × 0.35) + (ADVANCED_SCORE × 0.30)
```

**Intensity classification:**
- 0-20: LOW — Standard communication techniques
- 21-45: MODERATE — Intentional persuasion, within normal range
- 46-70: HIGH — Systematic influence, multiple techniques stacked
- 71-90: VERY HIGH — Aggressive influence campaign, multiple manipulation vectors
- 91-100: CRITICAL — Full-spectrum manipulation, likely coordinated

**Red flag triggers (regardless of composite score):**
- Any single stimulus > 80 points
- Emotional cycling detected (fractionation)
- Fake scarcity or fake social proof confirmed
- Vulnerability targeting detected (children, elderly, distressed)
- 4+ principles active simultaneously at HIGH+ levels

---

### 1.6 Professional Audit Checklist

#### Pre-Audit Setup
- [ ] Identify content type (ad, landing page, email, app, video, chatbot)
- [ ] Note target audience (if determinable)
- [ ] Record platform and distribution context
- [ ] Establish baseline (what's normal for this category?)
- [ ] Document audit date and version of content

#### During Audit — Systematic Scan
- [ ] Score all 6 Primal Stimuli (with language evidence)
- [ ] Score all 5 Psychological Principles (with language evidence)
- [ ] Score Cognitive Biases (Decision Fatigue, Anchoring)
- [ ] Check for Inoculation patterns
- [ ] Check for emotional cycling / fractionation
- [ ] Check for dark patterns (confirmshaming, roach motel, fake urgency)
- [ ] Check interface design (if applicable): signup vs. cancel friction
- [ ] Check pricing patterns (anchoring, decoys, drip pricing)
- [ ] Assess vulnerability targeting

#### Post-Audit Assessment
- [ ] Calculate composite score
- [ ] Classify intensity level
- [ ] Document specific red flags
- [ ] Note technique stacking / synergies
- [ ] Assess regulatory compliance implications
- [ ] Generate findings report

#### Common Audit Scenarios & Decision Rules

**Scenario 1: High emotional + low tangible**
→ Content relies on affect rather than substance. Elevated risk of manipulation.

**Scenario 2: High authority + low verifiability**
→ Manufactured authority pattern. Flag for investigation.

**Scenario 3: High scarcity + resets detected**
→ Fake scarcity confirmed. Score as manipulation regardless of other factors.

**Scenario 4: Progressive commitment + late-stage cost reveal**
→ Classic foot-in-the-door with decision fatigue exploitation. Flag as dark pattern.

---

### 1.7 Final Audit Report Template

```
=== PERSUASION AUDIT REPORT ===

Content: [description]
Date: [audit date]
Auditor: [name/system]

--- TACTICAL SCORES ---
Personal:      [score]/100  Evidence: [quotes]
Contrastable:  [score]/100  Evidence: [quotes]
Tangible:      [score]/100  Evidence: [quotes]
Memorable:     [score]/100  Evidence: [quotes]
Visual:        [score]/100  Evidence: [quotes]
Emotional:     [score]/100  Evidence: [quotes]
TACTICAL AVG:  [score]/100

--- PSYCHOLOGICAL SCORES ---
Authority:     [score]/100  Evidence: [quotes]
Social Proof:  [score]/100  Evidence: [quotes]
Reciprocity:   [score]/100  Evidence: [quotes]
Commitment:    [score]/100  Evidence: [quotes]
Scarcity:      [score]/100  Evidence: [quotes]
PSYCHOLOGICAL AVG: [score]/100

--- ADVANCED SCORES ---
Decision Fatigue: [score]/100  Evidence: [quotes]
Anchoring:        [score]/100  Evidence: [quotes]
Inoculation:      [score]/100  Evidence: [quotes]
ADVANCED AVG:     [score]/100

--- COMPOSITE ---
COMPOSITE SCORE: [score]/100
INTENSITY LEVEL: [LOW/MODERATE/HIGH/VERY HIGH/CRITICAL]

--- RED FLAGS ---
[List any triggered red flags]

--- TECHNIQUE STACKING ---
[List detected synergistic combinations]

--- KEY FINDINGS ---
[Narrative summary of most significant patterns]

--- REGULATORY NOTES ---
[Any potential regulatory compliance concerns]
```

---

## PART 2: MACHINE-READABLE DETECTION SYSTEM — Regex, Algorithms & JSON Output {#part-2}

### 2.1 Complete Regex Pattern Library

All patterns designed for production use. Each includes the stimulus/principle, regex, match type, and confidence weighting.

```python
DETECTION_PATTERNS = {
    # === PRIMAL STIMULI ===
    'personal': {
        'patterns': [
            {
                'name': 'direct_address',
                'regex': r'(?i)\b(you[r]?\b|you\'re|you\'ve|you\'ll)',
                'points': 2,
                'confidence': 0.7
            },
            {
                'name': 'name_personalization',
                'regex': r'(?i)(dear\s+[A-Z]\w+|hi\s+[A-Z]\w+|hello\s+[A-Z]\w+)',
                'points': 5,
                'confidence': 0.9
            },
            {
                'name': 'behavioral_reference',
                'regex': r'(?i)(based on your|because you (visited|viewed|searched|clicked|purchased|liked)|your recent|your browsing)',
                'points': 8,
                'confidence': 0.95
            },
            {
                'name': 'pain_point_mirror',
                'regex': r'(?i)(tired of|frustrated with|struggling with|sick of|fed up with|worried about|can\'t seem to)',
                'points': 10,
                'confidence': 0.85
            },
            {
                'name': 'identity_label',
                'regex': r'(?i)(as a (serious|smart|savvy|dedicated|true|real)\s+\w+|for (professionals?|experts?|leaders?|entrepreneurs?|visionaries?))',
                'points': 7,
                'confidence': 0.8
            },
            {
                'name': 'exclusivity',
                'regex': r'(?i)(not for everyone|if you (know|understand|are serious)|only (serious|dedicated|committed)|exclusive(ly)? for)',
                'points': 6,
                'confidence': 0.85
            }
        ]
    },
    'contrastable': {
        'patterns': [
            {
                'name': 'before_after',
                'regex': r'(?i)(before\s+\w+.*?after\s+\w+|used to.*?now\s+(you|we|they)|without\s+\w+.*?with\s+\w+)',
                'points': 5,
                'confidence': 0.8
            },
            {
                'name': 'competitor_diminish',
                'regex': r'(?i)(unlike\s+(other|most|typical|traditional)|while (others?|they|competitors?)\s+(struggle|fail|can\'t)|compared to)',
                'points': 7,
                'confidence': 0.85
            },
            {
                'name': 'status_quo_pain',
                'regex': r'(?i)(still (doing|using|stuck|relying|paying|waiting)|the old way|outdated|behind the curve|falling behind)',
                'points': 6,
                'confidence': 0.8
            },
            {
                'name': 'transformation',
                'regex': r'(?i)(transform|revolutioni[sz]e|reinvent|reimagine|completely change|total(ly)? (new|different)|game[- ]chang)',
                'points': 8,
                'confidence': 0.75
            },
            {
                'name': 'numerical_contrast',
                'regex': r'(?i)(from\s+\d+.*?to\s+\d+|\d+x\s+(more|better|faster)|went from.*?to)',
                'points': 4,
                'confidence': 0.85
            },
            {
                'name': 'gap_amplification',
                'regex': r'(?i)(the (gap|distance|difference) between|where you are.*?where you (could|should|want to) be|leaving (money|opportunity|growth) on the table)',
                'points': 9,
                'confidence': 0.8
            }
        ]
    },
    'tangible': {
        'patterns': [
            {
                'name': 'specific_percentage',
                'regex': r'(?i)(\d+\.?\d*\s*%)',
                'points': 3,
                'confidence': 0.7
            },
            {
                'name': 'exact_timeframe',
                'regex': r'(?i)(in\s+(just\s+)?\d+\s*(days?|hours?|minutes?|weeks?|months?)|within\s+\d+|by\s+(day|week|month)\s+\d+)',
                'points': 4,
                'confidence': 0.75
            },
            {
                'name': 'dollar_amount',
                'regex': r'(?i)(\$\s*[\d,]+\.?\d*)',
                'points': 5,
                'confidence': 0.7
            },
            {
                'name': 'case_study',
                'regex': r'(?i)(case study|client\s+\w+\s+(saw|achieved|increased|grew)|real[- ]world (example|result)|success story)',
                'points': 6,
                'confidence': 0.85
            },
            {
                'name': 'guarantee',
                'regex': r'(?i)(guarantee|money[- ]back|risk[- ]free|no[- ]risk|full refund|satisfaction guaranteed|or your money back)',
                'points': 7,
                'confidence': 0.9
            },
            {
                'name': 'false_precision',
                'regex': r'(?i)(\$\d+,?\d{2,3}(?!\d)(?!\.\d{1,2}\s*%))',
                'points': 8,
                'confidence': 0.6,
                'note': 'Oddly specific dollar amounts (e.g., $2,847) suggesting manufactured precision'
            }
        ]
    },
    'memorable': {
        'patterns': [
            {
                'name': 'alliteration',
                'regex': r'\b([A-Z])\w+\s+\1\w+\s+\1\w+',
                'points': 3,
                'confidence': 0.7
            },
            {
                'name': 'rule_of_three',
                'regex': r'(?i)(\w+[.,]\s*\w+[.,]\s*(and\s+)?\w+[.])',
                'points': 5,
                'confidence': 0.6
            },
            {
                'name': 'story_opening',
                'regex': r'(?i)(imagine|picture this|what if I told you|here\'s (the thing|a story|what happened)|let me (tell|share|paint))',
                'points': 6,
                'confidence': 0.85
            },
            {
                'name': 'metaphor',
                'regex': r'(?i)(is (a|the|like)\s+\w+\s+(of|for|in)|like a|think of it as|consider it)',
                'points': 4,
                'confidence': 0.6
            },
            {
                'name': 'surprising_stat',
                'regex': r'(?i)(did you know|surprising(ly)?|shock(ing|ingly)?|\d+%\s+of\s+(people|businesses?|companies?|users?)\s+(don\'t|fail|miss|never))',
                'points': 5,
                'confidence': 0.75
            }
        ]
    },
    'visual': {
        'patterns': [
            {
                'name': 'visual_verbs',
                'regex': r'(?i)(see how|look at (this|how|what)|watch (this|how)|notice (how|the)|observe)',
                'points': 2,
                'confidence': 0.75
            },
            {
                'name': 'sensory_language',
                'regex': r'(?i)(feel (the|how|it)|touch|smooth|rough|bright|vivid|stunning|beautiful|sleek|crisp|sharp|warm|cool)',
                'points': 4,
                'confidence': 0.6
            },
            {
                'name': 'visualization_command',
                'regex': r'(?i)(visuali[sz]e|picture (yourself|this|your)|close your eyes|imagine (seeing|looking|watching))',
                'points': 5,
                'confidence': 0.85
            }
        ]
    },
    'emotional': {
        'patterns': [
            {
                'name': 'fear_threat',
                'regex': r'(?i)(don\'t (miss|get left|wait|risk|lose|fall)|before it\'s too late|while you still can|protect yourself|danger|threat|warning|at risk)',
                'points': 8,
                'confidence': 0.85
            },
            {
                'name': 'shame_inadequacy',
                'regex': r'(?i)(still (making|doing) (this|that|the same) mistake|embarrass|ashamed|failing|behind|don\'t be the (last|only)|everyone else (already|is))',
                'points': 9,
                'confidence': 0.8
            },
            {
                'name': 'excitement_aspiration',
                'regex': r'(?i)(unlock (your|the)|unleash|breakthrough|skyrocket|explode (your)?|supercharge|level up|next level|dream|ultimate)',
                'points': 5,
                'confidence': 0.75
            },
            {
                'name': 'anger_outrage',
                'regex': r'(?i)(they don\'t want you to|the truth (they|that)|what (they|no one) (tell|want)|exposed|scandal|outrage|unfair|rigged|corrupt)',
                'points': 7,
                'confidence': 0.85
            },
            {
                'name': 'belonging_exclusion',
                'regex': r'(?i)(join (the|thousands|millions|our)|be part of|don\'t be left out|exclusive (community|group|circle)|inner circle|tribe|movement|us vs|together)',
                'points': 8,
                'confidence': 0.8
            },
            {
                'name': 'urgency_fomo',
                'regex': r'(?i)(only \d+\s*(left|remaining|spots?|seats?|available)|limited (time|offer|edition|spots?)|expires?\s+(soon|today|tonight|midnight)|while (supplies|stocks?)\s+last|act (now|fast|quickly)|hurry|rush|don\'t (delay|wait)|last chance|final (offer|chance|call)|going fast|selling out|almost gone)',
                'points': 10,
                'confidence': 0.9
            },
            {
                'name': 'relief_comfort',
                'regex': r'(?i)(finally|at last|no more|never again|put an end to|stop (worrying|struggling)|peace of mind|rest easy|sleep better|relax)',
                'points': 4,
                'confidence': 0.7
            }
        ]
    },

    # === PSYCHOLOGICAL PRINCIPLES ===
    'authority': {
        'patterns': [
            {
                'name': 'expert_citation',
                'regex': r'(?i)(stud(y|ies)\s+show|research\s+(proves?|shows?|confirms?|suggests?|found|indicates?)|according to\s+(a\s+)?stud)',
                'points': 5,
                'confidence': 0.8
            },
            {
                'name': 'credential_display',
                'regex': r'(?i)(certified|licensed|accredited|board[- ]certified|ph\.?d|m\.?d\.?|professor|dr\.?\s+\w+)',
                'points': 4,
                'confidence': 0.85
            },
            {
                'name': 'institutional_authority',
                'regex': r'(?i)(harvard|stanford|mit|yale|princeton|fda|who|cdc|nasa|university of|published in|peer[- ]reviewed|journal of)',
                'points': 7,
                'confidence': 0.85
            },
            {
                'name': 'expert_consensus',
                'regex': r'(?i)(experts?\s+(agree|recommend|say|confirm)|leading\s+(experts?|authorities?|researchers?)|world[- ]renowned|globally recognized)',
                'points': 6,
                'confidence': 0.8
            },
            {
                'name': 'manufactured_authority',
                'regex': r'(?i)(the\s+#1|america\'s (favorite|leading|top)|world\'s (best|leading|top|most)|as (featured|seen) (on|in))',
                'points': 10,
                'confidence': 0.7,
                'note': 'May be legitimate or manufactured — verify claims'
            }
        ]
    },
    'social_proof': {
        'patterns': [
            {
                'name': 'numbers_language',
                'regex': r'(?i)(\d+[,\d]*\s*(customers?|users?|people|companies?|professionals?|subscribers?|members?)\s+(trust|use|love|chose|rely on|prefer|switched to|joined))',
                'points': 4,
                'confidence': 0.85
            },
            {
                'name': 'testimonial',
                'regex': r'(?i)(".*?"\s*[-–—]\s*\w+|[\u201c].*?[\u201d]\s*[-–—])',
                'points': 5,
                'confidence': 0.8
            },
            {
                'name': 'bandwagon',
                'regex': r'(?i)(everyone (is|\'s)|most people|the majority|trending|popular choice|best[- ]sell(er|ing)|top[- ]rated|#1 (rated|choice|pick))',
                'points': 6,
                'confidence': 0.8
            },
            {
                'name': 'realtime_social',
                'regex': r'(?i)(\d+\s*(people|others?|users?)\s*(are\s+)?(viewing|watching|looking at|bought|signed up|in (the|their) cart)|purchased (recently|in the last|today))',
                'points': 7,
                'confidence': 0.9
            },
            {
                'name': 'rating_display',
                'regex': r'(?i)(rated\s+\d+\.?\d*\s*\/?\s*\d*|★|⭐|\d+\.?\d*\s*stars?|\d+[,\d]*\s*reviews?|verified (purchase|buyer|review))',
                'points': 3,
                'confidence': 0.85
            }
        ]
    },
    'reciprocity': {
        'patterns': [
            {
                'name': 'free_offer',
                'regex': r'(?i)(free\s+(trial|download|access|gift|bonus|guide|ebook|report|consultation|demo|sample|shipping)|at no (cost|charge)|complimentary|on (the|us) house)',
                'points': 5,
                'confidence': 0.85
            },
            {
                'name': 'value_first',
                'regex': r'(?i)(here\'s a free|we\'re giving you|no strings attached|yours (free|to keep)|as a (thank you|gift|bonus))',
                'points': 6,
                'confidence': 0.8
            },
            {
                'name': 'obligation_creation',
                'regex': r'(?i)(after (all|everything) we\'ve (given|provided|shared|done)|we\'ve already|since we (gave|provided|shared)|in return|you owe)',
                'points': 8,
                'confidence': 0.9
            }
        ]
    },
    'commitment': {
        'patterns': [
            {
                'name': 'small_yes',
                'regex': r'(?i)(just (enter|type|click|tap|share|tell us)|start with|begin by|first,?\s*(just|simply))',
                'points': 5,
                'confidence': 0.7
            },
            {
                'name': 'identity_reinforcement',
                'regex': r'(?i)(you\'re (the (type|kind) (of|who)|someone who|clearly|obviously)|people like you|as someone who)',
                'points': 6,
                'confidence': 0.85
            },
            {
                'name': 'sunk_cost',
                'regex': r'(?i)(you\'ve (already|invested|spent|come (this|so) far)|don\'t (waste|throw away|lose) (what|all)|since you (started|joined|began|invested))',
                'points': 8,
                'confidence': 0.9
            },
            {
                'name': 'progressive_disclosure',
                'regex': r'(?i)(step\s+\d+\s+of\s+\d+|next step|continue to|almost (done|there|finished|complete)|you\'re \d+% (done|complete|through))',
                'points': 6,
                'confidence': 0.75
            }
        ]
    },
    'scarcity': {
        'patterns': [
            {
                'name': 'quantity_limit',
                'regex': r'(?i)(only\s+\d+\s*(left|remaining|available|in stock|spots?|seats?|units?|copies?)|limited (quantity|stock|supply|number)|low stock|few (left|remaining)|selling (fast|out)|almost (gone|sold out))',
                'points': 6,
                'confidence': 0.9
            },
            {
                'name': 'time_limit',
                'regex': r'(?i)(offer\s+(expires?|ends?)|sale\s+ends?|limited[- ]time|for a limited|today only|this (week|weekend|month) only|deadline|expires?\s+(soon|today|tonight|midnight|in\s+\d+)|flash sale|door[- ]?buster)',
                'points': 7,
                'confidence': 0.9
            },
            {
                'name': 'exclusive_access',
                'regex': r'(?i)(invitation[- ]only|exclusive (access|offer|deal|preview)|vip|members?[- ]only|private (sale|access|offer)|by invitation|waitlist|early access)',
                'points': 5,
                'confidence': 0.8
            },
            {
                'name': 'loss_framing',
                'regex': r'(?i)(don\'t miss (out|this)|you\'ll (lose|miss|regret)|before (it\'s gone|they\'re gone|you miss)|missing out|pass(ing)? up|slip(ping)? away)',
                'points': 9,
                'confidence': 0.85
            }
        ]
    },

    # === COGNITIVE BIASES ===
    'anchoring': {
        'patterns': [
            {
                'name': 'strikethrough_price',
                'regex': r'(?i)(~~\$[\d,.]+~~|was\s*\$[\d,.]+\s*,?\s*now\s*\$[\d,.]+|originally\s*\$[\d,.]+)',
                'points': 7,
                'confidence': 0.9
            },
            {
                'name': 'value_comparison',
                'regex': r'(?i)(\$[\d,.]+\s*value\s*(for|yours|at)\s*(just|only)?\s*\$[\d,.]+|compare at\s*\$|retail(s?)\s*(for|at)\s*\$)',
                'points': 8,
                'confidence': 0.85
            },
            {
                'name': 'per_unit_reframe',
                'regex': r'(?i)((just|only|less than)\s*\$[\d.]+\s*(per|\/|a)\s*(day|week|month|hour|cup of coffee|lunch))',
                'points': 4,
                'confidence': 0.8
            },
            {
                'name': 'savings_highlight',
                'regex': r'(?i)(save\s*\$[\d,.]+|saving(s?)\s*of\s*\$[\d,.]+|\d+%\s*off|you save)',
                'points': 6,
                'confidence': 0.85
            }
        ]
    },
    'decision_fatigue': {
        'patterns': [
            {
                'name': 'multi_step_flow',
                'regex': r'(?i)(step\s+\d+\s+(of|\/)\s+\d+)',
                'points': 5,
                'confidence': 0.9
            },
            {
                'name': 'late_stage_offer',
                'regex': r'(?i)(before you (go|leave|check out)|wait[,!]?\s*(before|don\'t)|one more thing|add to (your )?order|would you (also )?like to|recommended (for|based on) you)',
                'points': 8,
                'confidence': 0.8
            },
            {
                'name': 'progress_indicator',
                'regex': r'(?i)(almost (done|there|finished|complete)|you\'re (nearly|almost|\d+%)|just\s+(one|1)\s+more\s+step|final\s+step)',
                'points': 6,
                'confidence': 0.75
            }
        ]
    },
    'inoculation': {
        'patterns': [
            {
                'name': 'objection_raising',
                'regex': r'(?i)(you (might|may|could|probably) (be (thinking|wondering)|think|wonder|ask|say)|some (people|might|may) (say|think|argue|wonder)|I (know|bet|understand) (what )?you\'re (thinking|wondering))',
                'points': 5,
                'confidence': 0.85
            },
            {
                'name': 'validation',
                'regex': r'(?i)(that\'s a (fair|valid|good|great|legitimate|understandable) (point|concern|question|objection)|I (understand|get it|hear you|see why)|fair enough|you\'re (right|not wrong) to)',
                'points': 4,
                'confidence': 0.8
            },
            {
                'name': 'refutation',
                'regex': r'(?i)(but (here\'s|what|the (truth|reality|fact|thing|data))|however,?\s*(the (reality|truth|data|facts?)|what)|in (reality|fact|truth)|actually|the thing is)',
                'points': 6,
                'confidence': 0.75
            }
        ]
    }
}
```

### 2.2 Scoring Algorithm (Python Implementation)

```python
import re
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum

class IntensityLevel(Enum):
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"
    CRITICAL = "CRITICAL"

@dataclass
class DetectionResult:
    """Result from a single pattern detection"""
    category: str
    pattern_name: str
    matches: List[str]
    match_count: int
    raw_score: float
    weighted_score: float
    confidence: float
    evidence: List[str]

@dataclass
class AuditResult:
    """Complete audit result"""
    tactical_scores: Dict[str, float]
    psychological_scores: Dict[str, float]
    advanced_scores: Dict[str, float]
    tactical_average: float
    psychological_average: float
    advanced_average: float
    composite_score: float
    intensity_level: IntensityLevel
    red_flags: List[str]
    all_detections: List[DetectionResult]
    evidence_map: Dict[str, List[str]]

class MachineReadableDetectionEngine:
    """
    Production detection engine with quantifiable scoring.

    Implements the full Primal Stimuli + Psychological Principles +
    Cognitive Biases framework with machine-readable output.
    """

    def __init__(self, patterns: Dict = None):
        self.patterns = patterns or DETECTION_PATTERNS
        self.intensity_thresholds = {
            'LOW': (0, 20),
            'MODERATE': (21, 45),
            'HIGH': (46, 70),
            'VERY_HIGH': (71, 90),
            'CRITICAL': (91, 100)
        }

    def analyze(self, text: str) -> AuditResult:
        """
        Perform full analysis on text content.

        Returns complete AuditResult with all scores, evidence, and flags.
        """
        all_detections = []
        scores_by_category = {}

        # Run all pattern categories
        for category, category_data in self.patterns.items():
            category_score = 0
            category_evidence = []

            for pattern_info in category_data['patterns']:
                matches = re.findall(pattern_info['regex'], text)
                if matches:
                    # Flatten matches (handle groups)
                    flat_matches = []
                    for m in matches:
                        if isinstance(m, tuple):
                            flat_matches.append(m[0])
                        else:
                            flat_matches.append(m)

                    raw_score = len(flat_matches) * pattern_info['points']
                    weighted_score = raw_score * pattern_info['confidence']

                    detection = DetectionResult(
                        category=category,
                        pattern_name=pattern_info['name'],
                        matches=flat_matches,
                        match_count=len(flat_matches),
                        raw_score=raw_score,
                        weighted_score=weighted_score,
                        confidence=pattern_info['confidence'],
                        evidence=flat_matches[:5]  # Cap evidence samples at 5
                    )
                    all_detections.append(detection)
                    category_score += weighted_score
                    category_evidence.extend(flat_matches[:3])

            # Cap scores at 100
            scores_by_category[category] = min(100, category_score)

        # Calculate composite scores
        tactical_cats = ['personal', 'contrastable', 'tangible', 'memorable', 'visual', 'emotional']
        psychological_cats = ['authority', 'social_proof', 'reciprocity', 'commitment', 'scarcity']
        advanced_cats = ['anchoring', 'decision_fatigue', 'inoculation']

        tactical_scores = {c: scores_by_category.get(c, 0) for c in tactical_cats}
        psychological_scores = {c: scores_by_category.get(c, 0) for c in psychological_cats}
        advanced_scores = {c: scores_by_category.get(c, 0) for c in advanced_cats}

        tactical_avg = sum(tactical_scores.values()) / len(tactical_cats) if tactical_cats else 0
        psychological_avg = sum(psychological_scores.values()) / len(psychological_cats) if psychological_cats else 0
        advanced_avg = sum(advanced_scores.values()) / len(advanced_cats) if advanced_cats else 0

        composite = (tactical_avg * 0.35) + (psychological_avg * 0.35) + (advanced_avg * 0.30)

        # Determine intensity
        intensity = self._classify_intensity(composite)

        # Check red flags
        red_flags = self._check_red_flags(scores_by_category, all_detections, text)

        # Build evidence map
        evidence_map = {}
        for det in all_detections:
            if det.category not in evidence_map:
                evidence_map[det.category] = []
            evidence_map[det.category].extend(det.evidence)

        return AuditResult(
            tactical_scores=tactical_scores,
            psychological_scores=psychological_scores,
            advanced_scores=advanced_scores,
            tactical_average=round(tactical_avg, 2),
            psychological_average=round(psychological_avg, 2),
            advanced_average=round(advanced_avg, 2),
            composite_score=round(composite, 2),
            intensity_level=intensity,
            red_flags=red_flags,
            all_detections=all_detections,
            evidence_map=evidence_map
        )

    def _classify_intensity(self, score: float) -> IntensityLevel:
        """Classify composite score into intensity level"""
        if score >= 91:
            return IntensityLevel.CRITICAL
        elif score >= 71:
            return IntensityLevel.VERY_HIGH
        elif score >= 46:
            return IntensityLevel.HIGH
        elif score >= 21:
            return IntensityLevel.MODERATE
        else:
            return IntensityLevel.LOW

    def _check_red_flags(
        self,
        scores: Dict[str, float],
        detections: List[DetectionResult],
        text: str
    ) -> List[str]:
        """Check for red flag conditions"""
        flags = []

        # Any single stimulus > 80
        for cat, score in scores.items():
            if score > 80:
                flags.append(f"SINGLE_CATEGORY_EXTREME: {cat} scored {score}")

        # Check for emotional cycling (fractionation)
        if self._detect_emotional_cycling(text):
            flags.append("EMOTIONAL_CYCLING: Alternating emotional tones detected (fractionation pattern)")

        # Check for fake scarcity indicators
        fake_scarcity_patterns = [
            r'(?i)(timer|countdown).*?(reset|restart|refresh)',
            r'(?i)(always|every time|constantly)\s+(low stock|limited|selling out)',
        ]
        for pattern in fake_scarcity_patterns:
            if re.search(pattern, text):
                flags.append("FAKE_SCARCITY: Indicators of artificial scarcity detected")
                break

        # Check for 4+ principles at HIGH+ levels
        high_principles = sum(1 for s in scores.values() if s >= 46)
        if high_principles >= 4:
            flags.append(f"MULTI_VECTOR_STACK: {high_principles} categories at HIGH+ intensity")

        # Check for vulnerability targeting
        vuln_patterns = [
            r'(?i)(senior|elderly|retired|pension|medicare|social security)',
            r'(?i)(kids?|children|teens?|young people|students?)',
            r'(?i)(struggling|desperate|lonely|depressed|anxious|overwhelmed)',
        ]
        for pattern in vuln_patterns:
            if re.search(pattern, text):
                flags.append("VULNERABILITY_TARGETING: Content may target vulnerable populations")
                break

        return flags

    def _detect_emotional_cycling(self, text: str) -> bool:
        """Detect alternating emotional patterns (A-J-A-R fractionation)"""
        # Split into segments
        sentences = re.split(r'[.!?]+', text)

        negative_pattern = r'(?i)(afraid|worried|angry|outrage|threat|danger|lose|miss out|risk|fail|behind|mistake|problem|crisis)'
        positive_pattern = r'(?i)(solution|finally|relief|hope|success|achieve|win|thrive|joy|happy|secure|safe|breakthrough|freedom)'

        tone_sequence = []
        for sentence in sentences:
            if re.search(negative_pattern, sentence):
                tone_sequence.append('N')
            elif re.search(positive_pattern, sentence):
                tone_sequence.append('P')

        # Look for N-P-N or N-P-N-P patterns
        tone_string = ''.join(tone_sequence)
        if re.search(r'N.?P.?N', tone_string) or re.search(r'P.?N.?P.?N', tone_string):
            return True
        return False

    def to_json(self, result: AuditResult) -> str:
        """Export audit result as JSON"""
        output = {
            'scores': {
                'tactical': result.tactical_scores,
                'psychological': result.psychological_scores,
                'advanced': result.advanced_scores,
                'averages': {
                    'tactical': result.tactical_average,
                    'psychological': result.psychological_average,
                    'advanced': result.advanced_average
                },
                'composite': result.composite_score
            },
            'classification': {
                'intensity_level': result.intensity_level.value,
                'red_flags': result.red_flags,
                'red_flag_count': len(result.red_flags)
            },
            'evidence': result.evidence_map,
            'detections': [
                {
                    'category': d.category,
                    'pattern': d.pattern_name,
                    'matches': d.match_count,
                    'score': d.weighted_score,
                    'confidence': d.confidence,
                    'samples': d.evidence
                }
                for d in result.all_detections
            ]
        }
        return json.dumps(output, indent=2)
```

### 2.3 JSON Output Format Specification

```json
{
  "audit_metadata": {
    "timestamp": "ISO-8601",
    "engine_version": "4.0",
    "content_type": "text|interface|pricing|multimodal",
    "content_length": 0,
    "word_count": 0
  },
  "scores": {
    "tactical": {
      "personal": 0.0,
      "contrastable": 0.0,
      "tangible": 0.0,
      "memorable": 0.0,
      "visual": 0.0,
      "emotional": 0.0
    },
    "psychological": {
      "authority": 0.0,
      "social_proof": 0.0,
      "reciprocity": 0.0,
      "commitment": 0.0,
      "scarcity": 0.0
    },
    "advanced": {
      "anchoring": 0.0,
      "decision_fatigue": 0.0,
      "inoculation": 0.0
    },
    "averages": {
      "tactical": 0.0,
      "psychological": 0.0,
      "advanced": 0.0
    },
    "composite": 0.0
  },
  "classification": {
    "intensity_level": "LOW|MODERATE|HIGH|VERY_HIGH|CRITICAL",
    "red_flags": [],
    "red_flag_count": 0,
    "technique_count": 0,
    "synergy_detected": false
  },
  "evidence": {
    "category_name": ["matched text samples"]
  },
  "detections": [
    {
      "category": "string",
      "pattern": "string",
      "matches": 0,
      "score": 0.0,
      "confidence": 0.0,
      "samples": ["string"]
    }
  ]
}
```

### 2.4 Boolean Logic Decision Trees

```python
# Risk categorization decision tree
def categorize_risk(audit_result: AuditResult) -> Dict:
    """
    Decision tree for risk categorization.
    Returns risk level, primary concern, and recommended action.
    """
    composite = audit_result.composite_score
    flags = audit_result.red_flags
    scores = {**audit_result.tactical_scores, **audit_result.psychological_scores, **audit_result.advanced_scores}

    # CRITICAL PATH: Any red flag escalates
    if any("VULNERABILITY_TARGETING" in f for f in flags):
        return {
            'risk_level': 'CRITICAL',
            'primary_concern': 'Potential targeting of vulnerable populations',
            'action': 'IMMEDIATE_REVIEW',
            'escalation': True
        }

    if any("EMOTIONAL_CYCLING" in f for f in flags):
        return {
            'risk_level': 'HIGH',
            'primary_concern': 'Fractionation / emotional cycling detected',
            'action': 'DETAILED_ANALYSIS',
            'escalation': True
        }

    if any("FAKE_SCARCITY" in f for f in flags):
        return {
            'risk_level': 'HIGH',
            'primary_concern': 'Artificial scarcity indicators',
            'action': 'VERIFY_CLAIMS',
            'escalation': True
        }

    # SCORE-BASED PATH
    if composite >= 91:
        return {
            'risk_level': 'CRITICAL',
            'primary_concern': 'Full-spectrum influence campaign',
            'action': 'FULL_AUDIT_REQUIRED',
            'escalation': True
        }
    elif composite >= 71:
        max_cat = max(scores, key=scores.get)
        return {
            'risk_level': 'VERY_HIGH',
            'primary_concern': f'Aggressive influence, primary vector: {max_cat}',
            'action': 'DETAILED_REVIEW',
            'escalation': True
        }
    elif composite >= 46:
        active_cats = [c for c, s in scores.items() if s >= 30]
        return {
            'risk_level': 'HIGH',
            'primary_concern': f'Systematic influence across {len(active_cats)} categories',
            'action': 'MONITOR_AND_REVIEW',
            'escalation': False
        }
    elif composite >= 21:
        return {
            'risk_level': 'MODERATE',
            'primary_concern': 'Standard persuasion techniques present',
            'action': 'DOCUMENT_FINDINGS',
            'escalation': False
        }
    else:
        return {
            'risk_level': 'LOW',
            'primary_concern': 'Minimal influence techniques detected',
            'action': 'NO_ACTION_NEEDED',
            'escalation': False
        }
```

---

## PART 3: ENHANCED DETECTION WITH PLATFORM RESEARCH {#part-3}

### 3.1 Key Platform Research Findings

These findings from peer-reviewed research and regulatory investigations inform the enhanced detection systems below.

**Facebook/Meta Internal Research:**
- Anger-weighted engagement: Facebook's algorithm weights anger reactions 5x more than likes for content distribution
- Emotional state inference: Internal models achieve ~87% accuracy in detecting user emotional state from behavior patterns
- Amplification effect: Political content with anger framing receives 2-3x more algorithmic distribution

**TikTok Research:**
- Emotional detection: TikTok's recommendation system achieves 94% accuracy in detecting user emotional state within 3 minutes of usage
- Engagement optimization: Content with emotional cycling patterns receives 2.7x more distribution
- Micro-targeting: Behavioral fingerprinting enables individual-level content calibration

**Science Field Experiment (2023):**
- Algorithmic amplification of political content: ~70% more engagement on politically divisive content when algorithmically selected vs. chronological
- Removal of reshared content reduced exposure to untrustworthy news by 57%

**FTC Enforcement Data (2024-2025):**
- Amazon: $2.5 billion settlement for dark patterns in Prime enrollment/cancellation
- Adobe: DOJ complaint for cancellation difficulty (roach motel pattern)
- International review: 76% of examined sites use at least one dark pattern
- Click-to-Cancel rule adopted then vacated

### 3.2 Enhanced Fractionation Detector

```python
class EnhancedFractionationDetector:
    """
    Detects emotional cycling patterns with platform-specific calibration.

    Based on research showing A-J-A-R (anger-joy-anger-relief) cycles
    reduce critical thinking by 200%+ per complete cycle.
    """

    ENGAGEMENT_WEIGHTS = {
        'anger': 5.0,      # Facebook internal: anger weighted 5x
        'outrage': 4.5,
        'fear': 3.5,
        'sadness': 2.0,
        'joy': 1.5,
        'surprise': 2.5,
        'love': 1.0,
        'neutral': 0.5
    }

    ANGER_OUTRAGE_MARKERS = [
        r'(?i)(outrag|scandal|corrupt|betray|unfair|disgust|appalling|unacceptable)',
        r'(?i)(they (lied|cheated|stole|hid)|cover[- ]?up|exposed|shocking truth)',
        r'(?i)(you should be (angry|furious|outraged)|how (dare|could) they)',
        r'(?i)(rigged|stolen|crooked|fraud|scam|sham|hoax)',
        r'(?i)(wake up|open your eyes|can\'t believe|unbelievable)'
    ]

    JOY_RELIEF_MARKERS = [
        r'(?i)(finally|at last|breakthrough|amazing|wonderful|incredible|fantastic)',
        r'(?i)(good news|great news|exciting|celebration|victory|success|triumph)',
        r'(?i)(hope|healing|recovery|solution|answer|cure|fix|resolution)',
        r'(?i)(together|united|community|strength|resilience|overcome)',
        r'(?i)(love|gratitude|blessed|thankful|grateful|appreciate)'
    ]

    COMMERCIAL_RELIEF_MARKERS = [
        r'(?i)(but (don\'t worry|there\'s hope|we have|here\'s the solution))',
        r'(?i)(luckily|fortunately|the good news is|here\'s what you can do)',
        r'(?i)(our (product|service|solution|tool|platform) (can|will|helps?))',
        r'(?i)(protect yourself|take (control|action|back)|fight back|defend)'
    ]

    def detect_fractionation(self, content_sequence: List[str]) -> Dict:
        """
        Analyze sequence of content items for fractionation patterns.

        Args:
            content_sequence: Ordered list of content items (posts, paragraphs, slides, etc.)

        Returns:
            Dict with cycle_count, intensity, pattern, and risk_score
        """
        emotional_sequence = []

        for item in content_sequence:
            emotion = self._classify_emotion(item)
            emotional_sequence.append(emotion)

        # Detect cycles
        cycles = self._find_cycles(emotional_sequence)

        # Calculate fractionation intensity
        intensity = self._calculate_intensity(cycles, content_sequence)

        return {
            'emotional_sequence': emotional_sequence,
            'cycle_count': len(cycles),
            'cycles': cycles,
            'intensity': intensity,
            'risk_score': min(1.0, len(cycles) * 0.25 + intensity * 0.5),
            'pattern': self._describe_pattern(emotional_sequence),
            'commercial_relief_detected': self._check_commercial_relief(content_sequence)
        }

    def _classify_emotion(self, text: str) -> str:
        """Classify dominant emotion of a text segment"""
        scores = {}

        for marker_list, label in [
            (self.ANGER_OUTRAGE_MARKERS, 'anger'),
            (self.JOY_RELIEF_MARKERS, 'joy'),
            (self.COMMERCIAL_RELIEF_MARKERS, 'relief')
        ]:
            count = 0
            for pattern in marker_list:
                count += len(re.findall(pattern, text))
            scores[label] = count

        # Also check for fear/sadness
        fear_patterns = [
            r'(?i)(afraid|scared|terrif|danger|threat|risk|catastroph|disaster|crisis|emergency|alarm)'
        ]
        sadness_patterns = [
            r'(?i)(sad|tragic|heartbreak|devastating|loss|grief|mourn|suffer)'
        ]

        scores['fear'] = sum(len(re.findall(p, text)) for p in fear_patterns)
        scores['sadness'] = sum(len(re.findall(p, text)) for p in sadness_patterns)

        if max(scores.values()) == 0:
            return 'neutral'

        return max(scores, key=scores.get)

    def _find_cycles(self, sequence: List[str]) -> List[Dict]:
        """Find emotional cycling patterns"""
        cycles = []
        negative_emotions = {'anger', 'fear', 'sadness'}
        positive_emotions = {'joy', 'relief'}

        i = 0
        while i < len(sequence) - 2:
            if sequence[i] in negative_emotions:
                # Look for N-P transition
                for j in range(i + 1, min(i + 4, len(sequence))):
                    if sequence[j] in positive_emotions:
                        # Found N-P, look for another N
                        for k in range(j + 1, min(j + 4, len(sequence))):
                            if sequence[k] in negative_emotions:
                                cycles.append({
                                    'start': i,
                                    'peak_negative': sequence[i],
                                    'relief': sequence[j],
                                    'return_negative': sequence[k],
                                    'length': k - i + 1
                                })
                                i = k
                                break
                        break
            i += 1

        return cycles

    def _calculate_intensity(self, cycles: List[Dict], content: List[str]) -> float:
        """Calculate fractionation intensity from 0-1"""
        if not cycles:
            return 0.0

        # Base intensity from cycle count
        base = min(1.0, len(cycles) * 0.3)

        # Rapidity bonus (cycles close together = more intense)
        avg_length = sum(c['length'] for c in cycles) / len(cycles) if cycles else 10
        rapidity_bonus = max(0, 0.3 - (avg_length * 0.05))

        # Engagement weight bonus (anger-heavy cycles more impactful)
        anger_cycles = sum(1 for c in cycles if c['peak_negative'] == 'anger')
        anger_bonus = anger_cycles * 0.1

        return min(1.0, base + rapidity_bonus + anger_bonus)

    def _describe_pattern(self, sequence: List[str]) -> str:
        """Create human-readable pattern description"""
        abbreviated = [s[0].upper() for s in sequence if s != 'neutral']
        return '-'.join(abbreviated) if abbreviated else 'NO_PATTERN'

    def _check_commercial_relief(self, content: List[str]) -> bool:
        """Check if relief phase coincides with commercial messaging"""
        for item in content:
            commercial_count = sum(
                len(re.findall(p, item)) for p in self.COMMERCIAL_RELIEF_MARKERS
            )
            if commercial_count >= 2:
                return True
        return False
```

### 3.3 Physiological Fractionation Detector

```python
class PhysiologicalFractionationDetector:
    """
    Detects fractionation through physiological markers.

    Research basis: fMRI studies showing emotional cycling produces
    measurable neurochemical responses (cortisol → dopamine → cortisol).
    """

    BIOMETRIC_THRESHOLDS = {
        'heart_rate_variability': {
            'baseline_deviation_threshold': 0.15,  # 15% deviation from baseline
            'rapid_cycling_window': 120,  # seconds
            'min_cycles_for_detection': 2
        },
        'skin_conductance': {
            'arousal_threshold': 0.5,  # microsiemens above baseline
            'cycling_detection_window': 180,  # seconds
            'recovery_time_min': 10  # seconds between peaks
        },
        'pupil_dilation': {
            'dilation_threshold': 0.5,  # mm above baseline
            'constriction_threshold': -0.3,  # mm below baseline
            'rapid_change_window': 5  # seconds
        }
    }

    def analyze_biometric_stream(self, readings: List[Dict]) -> Dict:
        """
        Analyze stream of biometric readings for fractionation signatures.

        Args:
            readings: List of timestamped biometric readings
                Each: {'timestamp': float, 'heart_rate': float,
                       'skin_conductance': float, 'pupil_diameter': float}

        Returns:
            Dict with fractionation detection results
        """
        if len(readings) < 10:
            return {'detected': False, 'reason': 'insufficient_data'}

        # Calculate baselines
        baseline_hr = sum(r['heart_rate'] for r in readings[:5]) / 5
        baseline_sc = sum(r['skin_conductance'] for r in readings[:5]) / 5
        baseline_pupil = sum(r['pupil_diameter'] for r in readings[:5]) / 5

        # Detect cycling in each modality
        hr_cycles = self._detect_hr_cycling(readings, baseline_hr)
        sc_cycles = self._detect_sc_cycling(readings, baseline_sc)
        pupil_cycles = self._detect_pupil_cycling(readings, baseline_pupil)

        # Cross-modal correlation
        cross_modal = self._cross_modal_analysis(hr_cycles, sc_cycles, pupil_cycles)

        total_cycles = max(len(hr_cycles), len(sc_cycles), len(pupil_cycles))

        return {
            'detected': total_cycles >= 2,
            'heart_rate_cycles': len(hr_cycles),
            'skin_conductance_cycles': len(sc_cycles),
            'pupil_cycles': len(pupil_cycles),
            'cross_modal_correlation': cross_modal,
            'estimated_susceptibility_increase': self._estimate_susceptibility(total_cycles),
            'risk_score': min(1.0, total_cycles * 0.2 + cross_modal * 0.3)
        }

    def _detect_hr_cycling(self, readings: List[Dict], baseline: float) -> List[Dict]:
        """Detect heart rate cycling patterns"""
        threshold = self.BIOMETRIC_THRESHOLDS['heart_rate_variability']
        deviation = baseline * threshold['baseline_deviation_threshold']
        cycles = []
        state = 'baseline'  # baseline, elevated, depressed

        for i, reading in enumerate(readings):
            hr = reading['heart_rate']
            if state == 'baseline' and hr > baseline + deviation:
                state = 'elevated'
                cycle_start = i
            elif state == 'elevated' and hr < baseline - deviation * 0.5:
                state = 'depressed'
            elif state == 'depressed' and hr > baseline + deviation:
                cycles.append({
                    'start_index': cycle_start,
                    'end_index': i,
                    'peak_deviation': max(r['heart_rate'] for r in readings[cycle_start:i+1]) - baseline
                })
                state = 'elevated'
                cycle_start = i

        return cycles

    def _detect_sc_cycling(self, readings: List[Dict], baseline: float) -> List[Dict]:
        """Detect skin conductance cycling"""
        threshold = self.BIOMETRIC_THRESHOLDS['skin_conductance']
        cycles = []
        peaks = []

        for i, reading in enumerate(readings):
            sc = reading['skin_conductance']
            if sc > baseline + threshold['arousal_threshold']:
                peaks.append({'index': i, 'value': sc})

        # Find cycling: peak-recovery-peak pattern
        for i in range(len(peaks) - 1):
            time_diff = readings[peaks[i+1]['index']]['timestamp'] - readings[peaks[i]['index']]['timestamp']
            if time_diff >= threshold['recovery_time_min']:
                cycles.append({
                    'peak1_index': peaks[i]['index'],
                    'peak2_index': peaks[i+1]['index'],
                    'interval_seconds': time_diff
                })

        return cycles

    def _detect_pupil_cycling(self, readings: List[Dict], baseline: float) -> List[Dict]:
        """Detect pupil dilation/constriction cycling"""
        threshold = self.BIOMETRIC_THRESHOLDS['pupil_dilation']
        cycles = []
        state = 'baseline'

        for i, reading in enumerate(readings):
            deviation = reading['pupil_diameter'] - baseline
            if state == 'baseline' and deviation > threshold['dilation_threshold']:
                state = 'dilated'
                cycle_start = i
            elif state == 'dilated' and deviation < threshold['constriction_threshold']:
                state = 'constricted'
            elif state == 'constricted' and deviation > threshold['dilation_threshold']:
                cycles.append({'start': cycle_start, 'end': i})
                state = 'dilated'
                cycle_start = i

        return cycles

    def _cross_modal_analysis(self, hr_cycles, sc_cycles, pupil_cycles) -> float:
        """Assess cross-modal correlation (higher = more likely genuine fractionation)"""
        modalities_active = sum([
            len(hr_cycles) >= 2,
            len(sc_cycles) >= 2,
            len(pupil_cycles) >= 2
        ])

        if modalities_active >= 3:
            return 0.9  # High confidence: all modalities cycling
        elif modalities_active >= 2:
            return 0.7  # Moderate confidence
        elif modalities_active >= 1:
            return 0.4  # Low confidence: single modality
        return 0.0

    def _estimate_susceptibility(self, cycle_count: int) -> str:
        """Estimate susceptibility increase based on cycle count"""
        # Research basis: 4 cycles in 10 min = 200%+ susceptibility increase
        if cycle_count >= 4:
            return "200%+ increase (critical)"
        elif cycle_count >= 3:
            return "150%+ increase (high)"
        elif cycle_count >= 2:
            return "100%+ increase (moderate)"
        elif cycle_count >= 1:
            return "50%+ increase (mild)"
        return "No significant increase"
```

### 3.4 Enhanced Interface Design Detector

```python
class EnhancedInterfaceDesignDetector:
    """
    Detects dark patterns and manipulative interface design.

    Based on FTC enforcement data (2024-2025) and academic
    dark pattern taxonomies.
    """

    CONFIRMSHAMING_PATTERNS = [
        r'(?i)(no,?\s*i\s*(don\'t|do not)\s*(want|need|like|care))',
        r'(?i)(no\s*thanks?,?\s*i\s*(prefer|\'d rather|want to)\s*(stay|remain|keep|be)\s*(broke|poor|behind|average|mediocre|unsuccessful|uninformed|ignorant|stuck))',
        r'(?i)(i\s*(don\'t|do not)\s*(care|value)\s*(about|my)\s*(money|health|success|family|future|career|growth))',
        r'(?i)(i\'ll\s*(pass|skip)\s*on\s*(saving|growing|improving|succeeding|learning))',
        r'(?i)(no,?\s*i\s*(hate|dislike)\s*(saving|money|success|progress))',
    ]

    ROACH_MOTEL_INDICATORS = {
        'signup_steps_max': 3,   # More than 3 = potential issue
        'cancel_steps_max': 3,   # More than 3 = roach motel
        'friction_ratio_threshold': 2.0,  # cancel_steps / signup_steps > 2x
        'cancel_requirements': [
            'phone_call_required',
            'chat_with_agent_required',
            'survey_required',
            'waiting_period',
            'manager_escalation',
            'hidden_cancel_link',
            'multiple_confirmations',
            'guilt_trip_screens'
        ]
    }

    FAKE_URGENCY_INDICATORS = [
        r'(?i)(\d+\s*(people|others?|users?)\s*(are\s+)?(viewing|watching|looking at)\s*(this|right now))',
        r'(?i)(only\s+\d+\s*(left|remaining|in stock|available))',
        r'(?i)((timer|countdown|offer)\s*(expires?|ends?|resets?))',
        r'(?i)(limited[- ]time\s+(offer|deal|price|discount))',
        r'(?i)(prices?\s+(going|will go|about to go)\s+up)',
        r'(?i)(last\s+chance|final\s+(offer|chance|warning))',
    ]

    FAKE_SCARCITY_SIGNALS = [
        'timer_resets_on_refresh',
        'stock_counter_never_reaches_zero',
        'urgency_message_always_present',
        'same_deal_available_next_day',
        'countdown_reappears_after_expiry'
    ]

    def analyze_interface(self, interface_data: Dict) -> Dict:
        """
        Analyze interface for dark patterns.

        Args:
            interface_data: Dict containing:
                - text_content: str (all visible text)
                - signup_steps: int
                - cancel_steps: int
                - cancel_requirements: List[str]
                - urgency_elements: List[str]
                - decline_button_text: str
                - option_visual_weights: Dict (button sizes, colors)

        Returns:
            Dict with detected patterns and scores
        """
        findings = {
            'confirmshaming': self._detect_confirmshaming(interface_data),
            'roach_motel': self._detect_roach_motel(interface_data),
            'fake_urgency': self._detect_fake_urgency(interface_data),
            'visual_manipulation': self._detect_visual_manipulation(interface_data),
            'overall_dark_pattern_score': 0.0
        }

        # Calculate overall score
        scores = [
            findings['confirmshaming']['score'],
            findings['roach_motel']['score'],
            findings['fake_urgency']['score'],
            findings['visual_manipulation']['score']
        ]
        findings['overall_dark_pattern_score'] = sum(scores) / len(scores)

        return findings

    def _detect_confirmshaming(self, data: Dict) -> Dict:
        """Detect confirmshaming patterns in decline options"""
        text = data.get('decline_button_text', '') + ' ' + data.get('text_content', '')
        matches = []

        for pattern in self.CONFIRMSHAMING_PATTERNS:
            found = re.findall(pattern, text)
            if found:
                matches.extend(found)

        return {
            'detected': len(matches) > 0,
            'instances': matches,
            'score': min(1.0, len(matches) * 0.3),
            'severity': 'high' if len(matches) > 2 else 'moderate' if matches else 'none'
        }

    def _detect_roach_motel(self, data: Dict) -> Dict:
        """Detect roach motel (easy to enter, hard to leave) patterns"""
        signup_steps = data.get('signup_steps', 0)
        cancel_steps = data.get('cancel_steps', 0)
        cancel_reqs = data.get('cancel_requirements', [])

        issues = []
        score = 0.0

        if cancel_steps > 0 and signup_steps > 0:
            ratio = cancel_steps / signup_steps
            if ratio > self.ROACH_MOTEL_INDICATORS['friction_ratio_threshold']:
                issues.append(f'Friction ratio: {ratio:.1f}x (cancel vs signup)')
                score += 0.4

        if cancel_steps > self.ROACH_MOTEL_INDICATORS['cancel_steps_max']:
            issues.append(f'Cancel requires {cancel_steps} steps')
            score += 0.2

        for req in cancel_reqs:
            if req in self.ROACH_MOTEL_INDICATORS['cancel_requirements']:
                issues.append(f'Friction requirement: {req}')
                score += 0.15

        return {
            'detected': len(issues) > 0,
            'issues': issues,
            'signup_steps': signup_steps,
            'cancel_steps': cancel_steps,
            'friction_ratio': cancel_steps / signup_steps if signup_steps > 0 else 0,
            'score': min(1.0, score),
            'regulatory_risk': 'HIGH' if score > 0.5 else 'MODERATE' if score > 0.2 else 'LOW'
        }

    def _detect_fake_urgency(self, data: Dict) -> Dict:
        """Detect fake urgency and scarcity patterns"""
        text = data.get('text_content', '')
        urgency_elements = data.get('urgency_elements', [])
        all_text = text + ' ' + ' '.join(urgency_elements)

        matches = []
        for pattern in self.FAKE_URGENCY_INDICATORS:
            found = re.findall(pattern, all_text)
            if found:
                matches.extend([f[0] if isinstance(f, tuple) else f for f in found])

        # Check for fake scarcity signals
        fake_signals = []
        for signal in self.FAKE_SCARCITY_SIGNALS:
            if data.get(signal, False):
                fake_signals.append(signal)

        score = min(1.0, len(matches) * 0.15 + len(fake_signals) * 0.3)

        return {
            'detected': len(matches) > 0 or len(fake_signals) > 0,
            'urgency_instances': matches,
            'fake_scarcity_signals': fake_signals,
            'score': score,
            'confirmed_fake': len(fake_signals) > 0
        }

    def _detect_visual_manipulation(self, data: Dict) -> Dict:
        """Detect visual weight manipulation (option asymmetry)"""
        weights = data.get('option_visual_weights', {})
        issues = []
        score = 0.0

        # Check for asymmetric option presentation
        accept_weight = weights.get('accept_button_size', 0)
        decline_weight = weights.get('decline_button_size', 0)

        if accept_weight > 0 and decline_weight > 0:
            ratio = accept_weight / decline_weight
            if ratio > 2.0:
                issues.append(f'Accept button {ratio:.1f}x larger than decline')
                score += 0.3

        # Check color manipulation
        accept_color = weights.get('accept_button_color', '')
        decline_color = weights.get('decline_button_color', '')

        if accept_color and decline_color:
            # Bright accept + muted decline = visual manipulation
            bright_colors = ['green', 'blue', '#00', '#0f', 'primary', 'brand']
            muted_colors = ['gray', 'grey', 'light', 'muted', 'transparent', 'text-only']

            accept_bright = any(c in accept_color.lower() for c in bright_colors)
            decline_muted = any(c in decline_color.lower() for c in muted_colors)

            if accept_bright and decline_muted:
                issues.append('Color asymmetry: bright accept vs muted decline')
                score += 0.2

        return {
            'detected': len(issues) > 0,
            'issues': issues,
            'score': min(1.0, score)
        }
```

### 3.5 Enhanced Cialdini Principle Detectors

```python
class EnhancedCialdiniDetector:
    """
    Enhanced detection for Cialdini's principles with
    fake/manufactured pattern identification.
    """

    FAKE_SOCIAL_PROOF_INDICATORS = {
        'review_patterns': [
            r'(?i)(5[- ]star|five[- ]star)\s*(review|rating)\s*(from|by)\s*\w+\s*[A-Z]\.',
            # "5-star review from John D." — truncated last name pattern
            r'(?i)(verified\s+(purchas|buyer|customer))',
        ],
        'bot_review_signals': [
            'reviews_clustered_in_time',       # Many reviews in short window
            'similar_language_patterns',        # Template reviews
            'reviewer_no_other_history',        # Single-review accounts
            'all_positive_no_nuance',           # No mixed reviews
            'generic_product_descriptions'      # Reviews don't mention specific features
        ],
        'fake_counter_signals': [
            'counter_never_decreases',          # "Only 3 left" but never goes to 2
            'viewing_count_suspiciously_round',  # "100 people viewing" — too round
            'same_count_on_return_visits'        # Count doesn't change over time
        ]
    }

    MANUFACTURED_AUTHORITY_INDICATORS = [
        r'(?i)(as (seen|featured) (on|in)\s+(CNN|Fox|NBC|ABC|CBS|Forbes|Inc|Entrepreneur))',
        r'(?i)(#1\s+(rated|best|top|choice|recommended|selling))',
        r'(?i)(world\'?s?\s+(leading|best|top|most|#1|premier|foremost))',
        r'(?i)(trusted by\s+(millions|thousands|hundreds of thousands))',
        r'(?i)((award|prize)[- ]winning)',
    ]

    DEEPFAKE_RISK_INDICATORS = {
        'video_testimonial_risk': [
            'single_speaker_static_background',
            'lip_sync_inconsistencies',
            'unnatural_blinking_pattern',
            'lighting_inconsistencies',
            'audio_video_mismatch'
        ],
        'text_generation_risk': [
            'unnaturally_consistent_tone',
            'no_personal_specifics',
            'generic_enthusiasm_patterns',
            'lacks_temporal_markers',
            'absent_brand_misspellings'  # Real users often misspell
        ]
    }

    def detect_fake_social_proof(self, reviews: List[Dict]) -> Dict:
        """
        Analyze reviews for authenticity signals.

        Args:
            reviews: List of review dicts with 'text', 'rating', 'date',
                    'reviewer_name', 'reviewer_history_count'

        Returns:
            Dict with authenticity assessment
        """
        if not reviews:
            return {'assessed': False, 'reason': 'no_reviews'}

        signals = {
            'temporal_clustering': self._check_temporal_clustering(reviews),
            'language_similarity': self._check_language_similarity(reviews),
            'rating_distribution': self._check_rating_distribution(reviews),
            'reviewer_authenticity': self._check_reviewer_authenticity(reviews),
            'specificity_score': self._check_review_specificity(reviews)
        }

        # Calculate fake probability
        fake_indicators = sum(1 for v in signals.values() if v.get('suspicious', False))
        fake_probability = fake_indicators / len(signals)

        return {
            'signals': signals,
            'fake_probability': fake_probability,
            'assessment': 'likely_fake' if fake_probability > 0.6 else 'possibly_fake' if fake_probability > 0.3 else 'likely_authentic',
            'confidence': min(0.9, 0.5 + fake_probability * 0.4)
        }

    def _check_temporal_clustering(self, reviews: List[Dict]) -> Dict:
        """Check if reviews are clustered in time (bot signal)"""
        dates = sorted([r.get('date', '') for r in reviews if r.get('date')])
        if len(dates) < 3:
            return {'suspicious': False, 'reason': 'insufficient_data'}

        # Check for bursts (multiple reviews within same day/hour)
        # Simplified: count reviews per date
        from collections import Counter
        date_counts = Counter(d[:10] for d in dates)  # Count by day
        max_per_day = max(date_counts.values()) if date_counts else 0

        return {
            'suspicious': max_per_day > len(reviews) * 0.3,
            'max_reviews_per_day': max_per_day,
            'clustering_ratio': max_per_day / len(reviews) if reviews else 0
        }

    def _check_language_similarity(self, reviews: List[Dict]) -> Dict:
        """Check if review language is suspiciously similar"""
        texts = [r.get('text', '').lower() for r in reviews]
        if len(texts) < 2:
            return {'suspicious': False}

        # Simple n-gram overlap check
        common_phrases = {}
        for text in texts:
            words = text.split()
            for i in range(len(words) - 2):
                trigram = ' '.join(words[i:i+3])
                common_phrases[trigram] = common_phrases.get(trigram, 0) + 1

        repeated = {k: v for k, v in common_phrases.items() if v > len(texts) * 0.3}

        return {
            'suspicious': len(repeated) > 3,
            'repeated_phrases': list(repeated.keys())[:10],
            'similarity_score': len(repeated) / max(len(common_phrases), 1)
        }

    def _check_rating_distribution(self, reviews: List[Dict]) -> Dict:
        """Check if rating distribution is natural"""
        ratings = [r.get('rating', 0) for r in reviews]
        if not ratings:
            return {'suspicious': False}

        from collections import Counter
        dist = Counter(ratings)
        five_star_ratio = dist.get(5, 0) / len(ratings)

        # Natural distributions typically have some variation
        # All-5-star is suspicious
        return {
            'suspicious': five_star_ratio > 0.9 and len(ratings) > 5,
            'five_star_ratio': five_star_ratio,
            'distribution': dict(dist),
            'has_variation': len(dist) > 2
        }

    def _check_reviewer_authenticity(self, reviews: List[Dict]) -> Dict:
        """Check reviewer account authenticity signals"""
        single_review_accounts = sum(
            1 for r in reviews if r.get('reviewer_history_count', 0) <= 1
        )
        ratio = single_review_accounts / len(reviews) if reviews else 0

        return {
            'suspicious': ratio > 0.7,
            'single_review_ratio': ratio,
            'single_review_count': single_review_accounts
        }

    def _check_review_specificity(self, reviews: List[Dict]) -> Dict:
        """Check if reviews contain specific product details"""
        specific_patterns = [
            r'(?i)(the\s+\w+\s+(feature|button|screen|option|setting))',
            r'(?i)(after\s+\d+\s+(days?|weeks?|months?))',
            r'(?i)(compared to\s+\w+)',
            r'(?i)(one (issue|problem|drawback|downside))',
        ]

        specific_count = 0
        for review in reviews:
            text = review.get('text', '')
            for pattern in specific_patterns:
                if re.search(pattern, text):
                    specific_count += 1
                    break

        specificity_ratio = specific_count / len(reviews) if reviews else 0

        return {
            'suspicious': specificity_ratio < 0.2 and len(reviews) > 5,
            'specificity_ratio': specificity_ratio,
            'reviews_with_specifics': specific_count
        }

    def detect_manufactured_authority(self, text: str) -> Dict:
        """Detect manufactured authority claims"""
        matches = []
        for pattern in self.MANUFACTURED_AUTHORITY_INDICATORS:
            found = re.findall(pattern, text)
            if found:
                matches.extend([f[0] if isinstance(f, tuple) else f for f in found])

        return {
            'detected': len(matches) > 0,
            'claims': matches,
            'score': min(1.0, len(matches) * 0.2),
            'verification_needed': len(matches) > 0
        }
```

### 3.6 Cognitive Load & Variable Reinforcement Detectors

```python
class EnhancedCognitiveLoadDetector:
    """
    Detects cognitive overload patterns designed to
    reduce analytical processing capability.
    """

    COGNITIVE_THRESHOLDS = {
        'working_memory_limit': 7,           # Miller's Law: 7 ± 2 items
        'processing_window_seconds': 20,      # Effective decision window
        'choice_overload_threshold': 6,       # Iyengar & Lepper (2000)
        'information_density_threshold': 0.7, # Ratio of info-bearing to total words
        'decision_points_per_page': 5         # Max before fatigue onset
    }

    def analyze_cognitive_load(self, page_data: Dict) -> Dict:
        """
        Analyze page/interface for cognitive overload patterns.

        Args:
            page_data: Dict with 'text_content', 'choice_count',
                      'decision_points', 'time_pressure_elements',
                      'information_chunks'
        """
        findings = {}

        # Choice overload
        choice_count = page_data.get('choice_count', 0)
        if choice_count > self.COGNITIVE_THRESHOLDS['choice_overload_threshold']:
            findings['choice_overload'] = {
                'detected': True,
                'count': choice_count,
                'threshold': self.COGNITIVE_THRESHOLDS['choice_overload_threshold'],
                'overload_ratio': choice_count / self.COGNITIVE_THRESHOLDS['choice_overload_threshold']
            }

        # Information density
        text = page_data.get('text_content', '')
        if text:
            words = text.split()
            info_words = [w for w in words if len(w) > 3]  # Simplified info-bearing check
            density = len(info_words) / len(words) if words else 0
            findings['information_density'] = {
                'detected': density > self.COGNITIVE_THRESHOLDS['information_density_threshold'],
                'density': round(density, 2),
                'threshold': self.COGNITIVE_THRESHOLDS['information_density_threshold']
            }

        # Decision point overload
        decision_points = page_data.get('decision_points', 0)
        if decision_points > self.COGNITIVE_THRESHOLDS['decision_points_per_page']:
            findings['decision_overload'] = {
                'detected': True,
                'count': decision_points,
                'threshold': self.COGNITIVE_THRESHOLDS['decision_points_per_page'],
                'fatigue_estimate': f"{(decision_points - 3) * 8}% reduction in decision quality"
            }

        # Time pressure + overload combination
        time_pressure = page_data.get('time_pressure_elements', [])
        if time_pressure and decision_points > 3:
            findings['pressure_overload_combo'] = {
                'detected': True,
                'description': 'Time pressure combined with decision overload — reduces analytical capacity',
                'severity': 'high'
            }

        # Overall score
        detected_count = sum(1 for f in findings.values() if f.get('detected', False))
        findings['overall_score'] = min(1.0, detected_count * 0.25)

        return findings


class VariableRatioReinforcementDetector:
    """
    Detects variable ratio reinforcement (slot machine mechanics)
    in digital interfaces.

    Research basis: Skinner's operant conditioning research showing
    variable ratio schedules produce highest, most persistent response rates.
    """

    DETECTION_PATTERNS = {
        'loot_box': {
            'indicators': [
                'randomized_rewards',
                'purchase_for_chance',
                'rare_item_display',
                'opening_animation',
                'collection_completion_pressure'
            ],
            'text_patterns': [
                r'(?i)(loot\s*(box|crate|pack)|mystery\s*(box|item|reward))',
                r'(?i)(rare|epic|legendary|mythic|ultra[- ]rare)\s*(item|drop|find|reward)',
                r'(?i)(chance\s+to\s+(win|get|unlock|receive))',
                r'(?i)(random\s*(reward|drop|item|bonus))',
            ]
        },
        'infinite_scroll': {
            'indicators': [
                'no_pagination',
                'auto_load_content',
                'no_end_point_visible',
                'pull_to_refresh',
                'content_preloading'
            ],
            'text_patterns': [
                r'(?i)(load(ing)?\s+more|see\s+more|show\s+more)',
                r'(?i)(endless|infinite)\s*(scroll|feed|content)',
            ]
        },
        'notification_variability': {
            'indicators': [
                'unpredictable_notification_timing',
                'mixed_notification_types',
                'reward_notifications_mixed_with_social',
                'variable_notification_value'
            ],
            'text_patterns': [
                r'(?i)(you\s+(have|got|received)\s+(a\s+)?new)',
                r'(?i)(someone\s+(liked|commented|shared|mentioned))',
                r'(?i)(don\'t\s+miss|you\'re\s+missing)',
            ]
        },
        'near_miss': {
            'indicators': [
                'almost_won_messaging',
                'close_to_threshold_display',
                'progress_bar_near_complete',
                'one_more_needed_framing'
            ],
            'text_patterns': [
                r'(?i)(so\s+close|almost\s+(there|won|reached|complete))',
                r'(?i)(just\s+\d+\s+more|only\s+\d+\s+(away|left|needed|to go))',
                r'(?i)(\d+%\s+complete|\d+\s*\/\s*\d+)',
            ]
        }
    }

    def analyze(self, interface_data: Dict, text_content: str = '') -> Dict:
        """Analyze for variable ratio reinforcement patterns"""
        findings = {}

        for mechanism, config in self.DETECTION_PATTERNS.items():
            # Check structural indicators
            indicators_found = []
            for indicator in config['indicators']:
                if interface_data.get(indicator, False):
                    indicators_found.append(indicator)

            # Check text patterns
            text_matches = []
            for pattern in config['text_patterns']:
                matches = re.findall(pattern, text_content)
                if matches:
                    text_matches.extend([m[0] if isinstance(m, tuple) else m for m in matches])

            detected = len(indicators_found) > 0 or len(text_matches) > 0

            findings[mechanism] = {
                'detected': detected,
                'structural_indicators': indicators_found,
                'text_matches': text_matches,
                'score': min(1.0, len(indicators_found) * 0.2 + len(text_matches) * 0.15)
            }

        # Overall assessment
        active_mechanisms = sum(1 for f in findings.values() if f['detected'])
        findings['overall'] = {
            'mechanisms_detected': active_mechanisms,
            'score': min(1.0, active_mechanisms * 0.25),
            'classification': 'high_engagement_design' if active_mechanisms >= 3
                else 'moderate_engagement_design' if active_mechanisms >= 2
                else 'standard_design'
        }

        return findings
```

### 3.7 Enhanced Anchoring Detector

```python
class EnhancedAnchoringDetector:
    """
    Detects anchoring bias exploitation in pricing and framing.

    Research basis: Tversky & Kahneman (1974) — anchoring pull
    of 40-60% toward initial value presented.
    """

    def analyze_pricing(self, pricing_data: Dict) -> Dict:
        """
        Analyze pricing structure for anchoring patterns.

        Args:
            pricing_data: Dict with 'prices' (list of {name, displayed_price}),
                         'original_prices', 'urgency_elements',
                         'comparison_values'
        """
        findings = {}

        prices = pricing_data.get('prices', [])
        originals = pricing_data.get('original_prices', [])

        # Strikethrough/was-now anchoring
        if originals and prices:
            discounts = []
            for i, (orig, current) in enumerate(zip(originals, prices)):
                current_price = current.get('displayed_price', 0) if isinstance(current, dict) else current
                if orig > 0 and current_price > 0:
                    discount_pct = ((orig - current_price) / orig) * 100
                    discounts.append({
                        'original': orig,
                        'current': current_price,
                        'discount_percent': round(discount_pct, 1),
                        'anchoring_pull': round(discount_pct * 0.5, 1)  # 40-60% pull estimate
                    })

            if discounts:
                avg_discount = sum(d['discount_percent'] for d in discounts) / len(discounts)
                findings['strikethrough_anchoring'] = {
                    'detected': True,
                    'discounts': discounts,
                    'average_discount': round(avg_discount, 1),
                    'score': min(1.0, avg_discount / 100)
                }

        # Decoy pricing detection
        if len(prices) >= 3:
            decoy = self._detect_decoy(prices)
            if decoy:
                findings['decoy_pricing'] = decoy

        # Value comparison anchoring
        comparisons = pricing_data.get('comparison_values', [])
        if comparisons:
            findings['value_anchoring'] = {
                'detected': True,
                'comparison_claims': comparisons,
                'score': min(1.0, len(comparisons) * 0.2)
            }

        # Per-unit reframing
        text = pricing_data.get('text_content', '')
        per_unit = re.findall(
            r'(?i)((just|only|less than)\s*\$[\d.]+\s*(per|\/|a)\s*(day|week|month|hour|cup of coffee))',
            text
        )
        if per_unit:
            findings['per_unit_reframing'] = {
                'detected': True,
                'instances': [p[0] for p in per_unit],
                'score': min(1.0, len(per_unit) * 0.2)
            }

        # Overall
        detected_count = sum(1 for f in findings.values() if isinstance(f, dict) and f.get('detected'))
        findings['overall_score'] = min(1.0, detected_count * 0.25)

        return findings

    def _detect_decoy(self, prices: List) -> Optional[Dict]:
        """Detect decoy pricing (asymmetric dominance effect)"""
        if len(prices) < 3:
            return None

        # Extract price values
        price_values = []
        for p in prices:
            if isinstance(p, dict):
                price_values.append(p.get('displayed_price', 0))
            else:
                price_values.append(p)

        price_values.sort()

        # Classic decoy: middle option is close to highest but much more than lowest
        if len(price_values) >= 3:
            low, mid, high = price_values[0], price_values[1], price_values[2]

            if low > 0 and mid > 0 and high > 0:
                low_to_mid_jump = (mid - low) / low
                mid_to_high_jump = (high - mid) / mid

                # Decoy signal: large jump to middle, small jump to high
                if low_to_mid_jump > 0.5 and mid_to_high_jump < 0.3:
                    return {
                        'detected': True,
                        'pattern': 'asymmetric_dominance',
                        'target_tier': 'highest',
                        'price_ratios': {
                            'low_to_mid': round(low_to_mid_jump, 2),
                            'mid_to_high': round(mid_to_high_jump, 2)
                        },
                        'score': 0.7,
                        'description': f'Large gap (${low}→${mid}) then small gap (${mid}→${high}) — classic decoy pushing toward highest tier'
                    }

        return None
```

### 3.8 Comprehensive Persuasion Audit (Master Integration — Enhanced)

```python
class ComprehensivePersuasionAudit:
    """
    Master audit class integrating all enhanced detectors.

    Provides unified interface for comprehensive persuasion analysis
    with platform-research-calibrated thresholds.
    """

    def __init__(self):
        self.text_engine = MachineReadableDetectionEngine()
        self.fractionation_detector = EnhancedFractionationDetector()
        self.physiological_detector = PhysiologicalFractionationDetector()
        self.interface_detector = EnhancedInterfaceDesignDetector()
        self.cialdini_detector = EnhancedCialdiniDetector()
        self.cognitive_load_detector = EnhancedCognitiveLoadDetector()
        self.vrr_detector = VariableRatioReinforcementDetector()
        self.anchoring_detector = EnhancedAnchoringDetector()

    def full_audit(self, content: Dict) -> Dict:
        """
        Run complete audit across all detection systems.

        Args:
            content: Dict containing any combination of:
                - 'text': str
                - 'content_sequence': List[str] (for fractionation)
                - 'biometric_readings': List[Dict] (for physiological)
                - 'interface': Dict (for dark patterns)
                - 'reviews': List[Dict] (for social proof authenticity)
                - 'pricing': Dict (for anchoring)
                - 'page_data': Dict (for cognitive load)

        Returns:
            Comprehensive audit report Dict
        """
        report = {
            'timestamp': None,  # Set by caller
            'text_analysis': None,
            'fractionation': None,
            'physiological': None,
            'interface_patterns': None,
            'social_proof_authenticity': None,
            'cognitive_load': None,
            'variable_reinforcement': None,
            'anchoring': None,
            'composite_risk': 0.0,
            'red_flags': [],
            'summary': ''
        }

        risk_scores = []

        # 1. Text analysis
        if 'text' in content:
            text_result = self.text_engine.analyze(content['text'])
            report['text_analysis'] = {
                'composite_score': text_result.composite_score,
                'intensity': text_result.intensity_level.value,
                'tactical_avg': text_result.tactical_average,
                'psychological_avg': text_result.psychological_average,
                'advanced_avg': text_result.advanced_average,
                'red_flags': text_result.red_flags
            }
            risk_scores.append(text_result.composite_score / 100)
            report['red_flags'].extend(text_result.red_flags)

        # 2. Fractionation
        if 'content_sequence' in content:
            frac_result = self.fractionation_detector.detect_fractionation(content['content_sequence'])
            report['fractionation'] = frac_result
            risk_scores.append(frac_result['risk_score'])
            if frac_result['cycle_count'] >= 2:
                report['red_flags'].append(f"FRACTIONATION: {frac_result['cycle_count']} emotional cycles detected")

        # 3. Physiological
        if 'biometric_readings' in content:
            phys_result = self.physiological_detector.analyze_biometric_stream(content['biometric_readings'])
            report['physiological'] = phys_result
            risk_scores.append(phys_result['risk_score'])

        # 4. Interface patterns
        if 'interface' in content:
            interface_result = self.interface_detector.analyze_interface(content['interface'])
            report['interface_patterns'] = interface_result
            risk_scores.append(interface_result['overall_dark_pattern_score'])
            if interface_result['roach_motel']['detected']:
                report['red_flags'].append("DARK_PATTERN: Roach motel detected")
            if interface_result.get('fake_urgency', {}).get('confirmed_fake'):
                report['red_flags'].append("DARK_PATTERN: Confirmed fake urgency/scarcity")

        # 5. Social proof authenticity
        if 'reviews' in content:
            social_result = self.cialdini_detector.detect_fake_social_proof(content['reviews'])
            report['social_proof_authenticity'] = social_result
            if social_result['assessment'] == 'likely_fake':
                risk_scores.append(0.8)
                report['red_flags'].append("FAKE_SOCIAL_PROOF: Reviews assessed as likely fake")

        # 6. Cognitive load
        if 'page_data' in content:
            cog_result = self.cognitive_load_detector.analyze_cognitive_load(content['page_data'])
            report['cognitive_load'] = cog_result
            risk_scores.append(cog_result.get('overall_score', 0))

        # 7. Variable reinforcement
        if 'interface' in content:
            text_for_vrr = content.get('text', '')
            vrr_result = self.vrr_detector.analyze(content['interface'], text_for_vrr)
            report['variable_reinforcement'] = vrr_result
            risk_scores.append(vrr_result.get('overall', {}).get('score', 0))

        # 8. Anchoring
        if 'pricing' in content:
            anchor_result = self.anchoring_detector.analyze_pricing(content['pricing'])
            report['anchoring'] = anchor_result
            risk_scores.append(anchor_result.get('overall_score', 0))

        # Calculate composite risk
        if risk_scores:
            report['composite_risk'] = round(
                (sum(risk_scores) / len(risk_scores)) * 0.6 + max(risk_scores) * 0.4,
                3
            )

        # Generate summary
        risk_level = 'CRITICAL' if report['composite_risk'] > 0.8 else \
                     'HIGH' if report['composite_risk'] > 0.6 else \
                     'MODERATE' if report['composite_risk'] > 0.3 else 'LOW'

        report['summary'] = (
            f"Risk Level: {risk_level} ({report['composite_risk']:.2f}) | "
            f"Red Flags: {len(report['red_flags'])} | "
            f"Active Detection Systems: {len(risk_scores)}"
        )

        return report
```

## PART 4: COMPREHENSIVE DETECTION FRAMEWORKS (10 Domains) {#part-4}

### 4.1 Multimodal Persuasion Mechanics

#### Audio Influence Detection

```python
class AudioInfluenceType(Enum):
    PITCH_MANIPULATION = "pitch_manipulation"        # Vocal pitch shifts
    ASMR_RELAXATION = "asmr_relaxation"             # ASMR triggers
    TEMPO_MANIPULATION = "tempo_manipulation"        # Speech rate changes
    VOLUME_DYNAMICS = "volume_dynamics"              # Strategic volume changes
    FREQUENCY_TARGETING = "frequency_targeting"      # Specific Hz targeting
    BACKGROUND_AUDIO = "background_audio_influence"  # Subliminal audio
```

**Research findings:**
- Voice pitch: Lower pitch = +23% perceived authority (PSPB 2024)
- ASMR: Triggers measurable physiological relaxation (reduced heart rate, increased skin conductance) — MDPI 2024
- Tempo: Faster speech = less counterargument; slower = more processing
- Background audio: Low-frequency drones (40-60 Hz) reduce critical alertness

**Detection thresholds:**
```python
AUDIO_THRESHOLDS = {
    'pitch_manipulation': {
        'authority_range_hz': (85, 180),      # Male: 85-155, Female: 165-255
        'persuasive_drop_hz': 20,             # Pitch drop for authority
        'excitement_rise_hz': 30              # Pitch rise for enthusiasm
    },
    'asmr_triggers': {
        'whispering_db_range': (20, 40),
        'tapping_frequency_hz': (1, 5),
        'mouth_sounds': True,
        'binaural_beats': True
    },
    'tempo_manipulation': {
        'baseline_wpm': 150,
        'fast_persuasion_wpm': 190,           # Reduce counterargument time
        'slow_emphasis_wpm': 100,             # Increase processing of key points
        'rate_change_threshold': 0.2          # 20% shift = deliberate
    },
    'subliminal_audio': {
        'frequency_below_threshold': 20,      # Hz — below conscious hearing
        'frequency_above_threshold': 20000,   # Hz — above conscious hearing
        'volume_below_conscious': -40         # dB relative to main audio
    }
}
```

#### Video Influence Detection

```python
class VideoInfluenceType(Enum):
    CUT_RHYTHM = "cut_rhythm_manipulation"
    COLOR_PSYCHOLOGY = "color_psychology"
    EYE_CONTACT = "eye_contact_manipulation"
    FRAMING = "visual_framing"
    SUBLIMINAL_FLASH = "subliminal_flash"
    MOTION_MANIPULATION = "motion_manipulation"
```

**Color psychology research data:**
```python
COLOR_PSYCHOLOGY = {
    'red': {
        'associations': ['urgency', 'danger', 'excitement', 'passion'],
        'physiological': 'increases heart rate and arousal',
        'persuasion_use': 'sale banners, CTA buttons, urgency indicators',
        'effectiveness': '+20% click-through on CTA buttons vs blue'
    },
    'blue': {
        'associations': ['trust', 'stability', 'calm', 'authority'],
        'physiological': 'reduces anxiety, lowers blood pressure',
        'persuasion_use': 'financial services, tech companies, trust signals',
        'effectiveness': 'Most trusted color across cultures'
    },
    'green': {
        'associations': ['safety', 'go', 'nature', 'health', 'money'],
        'physiological': 'reduces stress, associated with positive outcomes',
        'persuasion_use': 'checkout buttons, health products, eco-branding'
    },
    'orange': {
        'associations': ['energy', 'enthusiasm', 'warmth', 'impulse'],
        'physiological': 'stimulates appetite and impulse',
        'persuasion_use': 'buy buttons, food marketing, call-to-action'
    },
    'black': {
        'associations': ['luxury', 'sophistication', 'exclusivity', 'power'],
        'physiological': 'perceived weight and importance',
        'persuasion_use': 'premium branding, luxury products'
    },
    'yellow': {
        'associations': ['attention', 'optimism', 'caution', 'warmth'],
        'physiological': 'first color eye processes, attention-grabbing',
        'persuasion_use': 'warnings, highlights, attention capture'
    },
    'purple': {
        'associations': ['royalty', 'creativity', 'wisdom', 'luxury'],
        'physiological': 'calming, associated with imagination',
        'persuasion_use': 'beauty products, creative services, premium tiers'
    },
    'white': {
        'associations': ['purity', 'simplicity', 'cleanliness', 'space'],
        'physiological': 'reduces visual fatigue, creates openness',
        'persuasion_use': 'minimalist design, premium feel, healthcare'
    }
}
```

#### Multimodal Persuasion Detector (Source: 26_COMPREHENSIVE_DETECTION_FRAMEWORKS)

```python
# Source Enum variants (used by MultimodalPersuasionDetector)
class AudioInfluenceType_Source(Enum):
    VOICE_PITCH_LOW = "low_pitch_authority"
    VOICE_PITCH_VARIATION = "pitch_influence"
    FALLING_INTONATION = "confidence_signal"
    ASMR_TRIGGERS = "asmr_relaxation"
    URGENCY_TONE = "urgency_pressure"
    WHISPER = "intimacy_whisper"
    BACKGROUND_MUSIC_TEMPO = "tempo_influence"

class VideoInfluenceType_Source(Enum):
    RAPID_CUTS = "attention_fragmentation"
    ZOOM_FOCUS = "attention_direction"
    RHYTHM_PATTERN = "emotional_pacing"
    FLASH_FRAMES = "subliminal_priming"
    EYE_CONTACT = "parasocial_connection"
    COLOR_GRADING = "mood_influence"

@dataclass
class AudioAnalysisResult:
    """Results from audio influence analysis"""
    pitch_mean: float = 0.0
    pitch_variance: float = 0.0
    intonation_pattern: str = ""
    tempo_bpm: float = 0.0
    asmr_trigger_count: int = 0
    whisper_segments: int = 0
    urgency_markers: int = 0
    influence_types: List[AudioInfluenceType_Source] = field(default_factory=list)
    risk_score: float = 0.0

@dataclass
class VideoAnalysisResult:
    """Results from video influence analysis"""
    avg_shot_length: float = 0.0
    cut_frequency: float = 0.0
    rapid_cut_sequences: int = 0
    zoom_events: int = 0
    eye_contact_duration: float = 0.0
    dominant_colors: List[str] = field(default_factory=list)
    color_influence_score: float = 0.0
    influence_types: List[VideoInfluenceType_Source] = field(default_factory=list)
    risk_score: float = 0.0

class MultimodalPersuasionDetector:
    """
    Detects influence techniques in audio-visual content.

    Research basis:
    - ICMI 2025: Multimodal persuasion combines emotion, cognition, personality factors
    - 2024 voice research: Low pitch increases perceived competence
    - Film editing research: Cuts affect alpha rhythm and conscious processing
    """

    ASMR_TRIGGERS = [
        'whisper', 'tapping', 'scratching', 'brushing', 'crinkling',
        'soft spoken', 'gentle', 'relaxing', 'soothing', 'tingles'
    ]

    URGENCY_AUDIO_MARKERS = [
        'now', 'immediately', 'hurry', 'quick', 'fast', 'limited time',
        'act now', 'don\'t wait', 'today only', 'expires'
    ]

    COLOR_PSYCHOLOGY = {
        'red': {'emotions': ['urgency', 'excitement', 'danger'], 'influence_potential': 0.8},
        'orange': {'emotions': ['enthusiasm', 'warmth'], 'influence_potential': 0.5},
        'yellow': {'emotions': ['optimism', 'attention'], 'influence_potential': 0.6},
        'green': {'emotions': ['trust', 'nature', 'money'], 'influence_potential': 0.4},
        'blue': {'emotions': ['trust', 'calm', 'security'], 'influence_potential': 0.3},
        'purple': {'emotions': ['luxury', 'creativity'], 'influence_potential': 0.5},
        'black': {'emotions': ['sophistication', 'power'], 'influence_potential': 0.4},
        'white': {'emotions': ['purity', 'simplicity'], 'influence_potential': 0.2},
    }

    def __init__(self):
        self.thresholds = {
            'low_pitch_hz': 120,
            'high_pitch_variance': 50,
            'rapid_cut_threshold': 2.0,
            'burst_sequence_min': 5,
            'asmr_trigger_threshold': 3,
            'eye_contact_influence': 0.4,
        }

    def analyze_audio_features(self, audio_data: Dict) -> AudioAnalysisResult:
        """
        Analyze audio for influence techniques.

        Expected audio_data format:
        {
            'pitch_values': [float],
            'transcript': str,
            'tempo_bpm': float,
            'volume_envelope': [float],
            'segments': [{'start': float, 'end': float, 'type': str}]
        }
        """
        result = AudioAnalysisResult()

        # Pitch analysis
        if 'pitch_values' in audio_data and audio_data['pitch_values']:
            pitches = np.array(audio_data['pitch_values'])
            result.pitch_mean = float(np.mean(pitches))
            result.pitch_variance = float(np.var(pitches))

            if result.pitch_mean < self.thresholds['low_pitch_hz']:
                result.influence_types.append(AudioInfluenceType_Source.VOICE_PITCH_LOW)
                result.risk_score += 0.3

            if result.pitch_variance > self.thresholds['high_pitch_variance']:
                result.influence_types.append(AudioInfluenceType_Source.VOICE_PITCH_VARIATION)
                result.risk_score += 0.4

        # Transcript analysis for ASMR triggers
        if 'transcript' in audio_data:
            transcript_lower = audio_data['transcript'].lower()

            for trigger in self.ASMR_TRIGGERS:
                if trigger in transcript_lower:
                    result.asmr_trigger_count += 1

            if result.asmr_trigger_count >= self.thresholds['asmr_trigger_threshold']:
                result.influence_types.append(AudioInfluenceType_Source.ASMR_TRIGGERS)
                result.risk_score += 0.5

            for marker in self.URGENCY_AUDIO_MARKERS:
                if marker in transcript_lower:
                    result.urgency_markers += 1

            if result.urgency_markers >= 3:
                result.influence_types.append(AudioInfluenceType_Source.URGENCY_TONE)
                result.risk_score += 0.4

        # Tempo analysis
        if 'tempo_bpm' in audio_data:
            result.tempo_bpm = audio_data['tempo_bpm']
            if result.tempo_bpm > 120:
                result.influence_types.append(AudioInfluenceType_Source.BACKGROUND_MUSIC_TEMPO)
                result.risk_score += 0.2

        # Whisper segment detection
        if 'segments' in audio_data:
            result.whisper_segments = sum(
                1 for seg in audio_data['segments']
                if seg.get('type') == 'whisper'
            )
            if result.whisper_segments > 0:
                result.influence_types.append(AudioInfluenceType_Source.WHISPER)
                result.risk_score += 0.3

        # Intonation pattern (falling = confidence)
        if 'pitch_values' in audio_data and len(audio_data['pitch_values']) > 10:
            last_quarter = audio_data['pitch_values'][-len(audio_data['pitch_values'])//4:]
            if np.mean(last_quarter) < result.pitch_mean * 0.9:
                result.intonation_pattern = "falling"
                result.influence_types.append(AudioInfluenceType_Source.FALLING_INTONATION)
                result.risk_score += 0.2

        result.risk_score = min(1.0, result.risk_score)
        return result

    def analyze_video_features(self, video_data: Dict) -> VideoAnalysisResult:
        """
        Analyze video for influence techniques.

        Expected video_data format:
        {
            'cuts': [float],
            'duration': float,
            'zoom_events': [{'time': float, 'type': str}],
            'face_detections': [{'time': float, 'eye_contact': bool}],
            'color_histogram': {'red': float, 'green': float, 'blue': float, ...}
        }
        """
        result = VideoAnalysisResult()

        # Cut analysis
        if 'cuts' in video_data and 'duration' in video_data:
            cuts = video_data['cuts']
            duration = video_data['duration']

            if len(cuts) > 1:
                intervals = np.diff(cuts)
                result.avg_shot_length = float(np.mean(intervals))
                result.cut_frequency = len(cuts) / duration * 60

                rapid_cuts = intervals < self.thresholds['rapid_cut_threshold']

                consecutive_count = 0
                burst_sequences = 0

                for is_rapid in rapid_cuts:
                    if is_rapid:
                        consecutive_count += 1
                    else:
                        if consecutive_count >= self.thresholds['burst_sequence_min']:
                            burst_sequences += 1
                        consecutive_count = 0

                result.rapid_cut_sequences = burst_sequences

                if result.avg_shot_length < 3.0:
                    result.influence_types.append(VideoInfluenceType_Source.RAPID_CUTS)
                    result.risk_score += 0.4

                if burst_sequences > 0:
                    result.influence_types.append(VideoInfluenceType_Source.RHYTHM_PATTERN)
                    result.risk_score += 0.3

        # Zoom event analysis
        if 'zoom_events' in video_data:
            result.zoom_events = len(video_data['zoom_events'])
            if result.zoom_events > 10:
                result.influence_types.append(VideoInfluenceType_Source.ZOOM_FOCUS)
                result.risk_score += 0.2

        # Eye contact analysis (parasocial relationship building)
        if 'face_detections' in video_data and 'duration' in video_data:
            eye_contact_frames = sum(
                1 for f in video_data['face_detections']
                if f.get('eye_contact', False)
            )
            total_frames = len(video_data['face_detections'])

            if total_frames > 0:
                result.eye_contact_duration = eye_contact_frames / total_frames

                if result.eye_contact_duration > self.thresholds['eye_contact_influence']:
                    result.influence_types.append(VideoInfluenceType_Source.EYE_CONTACT)
                    result.risk_score += 0.3

        # Color analysis
        if 'color_histogram' in video_data:
            histogram = video_data['color_histogram']
            total = sum(histogram.values())

            if total > 0:
                for color, value in histogram.items():
                    proportion = value / total
                    if proportion > 0.3:
                        result.dominant_colors.append(color)
                        if color in self.COLOR_PSYCHOLOGY:
                            result.color_influence_score += (
                                self.COLOR_PSYCHOLOGY[color]['influence_potential'] * proportion
                            )

                if result.color_influence_score > 0.5:
                    result.influence_types.append(VideoInfluenceType_Source.COLOR_GRADING)
                    result.risk_score += result.color_influence_score * 0.3

        result.risk_score = min(1.0, result.risk_score)
        return result

    def analyze_audiovisual_synchronization(
        self,
        audio_result: AudioAnalysisResult,
        video_result: VideoAnalysisResult
    ) -> Dict:
        """
        Analyze how audio and video work together for influence.

        Research: Audio-visual synchronization amplifies emotional impact
        (ICMI 2025, MMS-LLaMA research)
        """
        sync_analysis = {
            'combined_risk_score': 0.0,
            'synergy_detected': False,
            'influence_amplification': 1.0,
            'findings': []
        }

        sync_analysis['combined_risk_score'] = (
            audio_result.risk_score * 0.4 +
            video_result.risk_score * 0.4
        )

        synergies = []

        # ASMR audio + slow video = deep relaxation (reduced critical thinking)
        if (AudioInfluenceType_Source.ASMR_TRIGGERS in audio_result.influence_types and
            video_result.avg_shot_length > 5.0):
            synergies.append("ASMR_RELAXATION_COMBO")
            sync_analysis['influence_amplification'] *= 1.4

        # Urgency audio + rapid cuts = heightened anxiety
        if (AudioInfluenceType_Source.URGENCY_TONE in audio_result.influence_types and
            VideoInfluenceType_Source.RAPID_CUTS in video_result.influence_types):
            synergies.append("URGENCY_ANXIETY_COMBO")
            sync_analysis['influence_amplification'] *= 1.5

        # Authority voice + eye contact = trust application
        if (AudioInfluenceType_Source.VOICE_PITCH_LOW in audio_result.influence_types and
            VideoInfluenceType_Source.EYE_CONTACT in video_result.influence_types):
            synergies.append("AUTHORITY_TRUST_COMBO")
            sync_analysis['influence_amplification'] *= 1.3

        # Fast tempo + rapid cuts = overstimulation
        if (AudioInfluenceType_Source.BACKGROUND_MUSIC_TEMPO in audio_result.influence_types and
            VideoInfluenceType_Source.RAPID_CUTS in video_result.influence_types):
            synergies.append("OVERSTIMULATION_COMBO")
            sync_analysis['influence_amplification'] *= 1.4

        if synergies:
            sync_analysis['synergy_detected'] = True
            sync_analysis['findings'] = synergies
            sync_analysis['combined_risk_score'] *= sync_analysis['influence_amplification']

        sync_analysis['combined_risk_score'] = min(1.0, sync_analysis['combined_risk_score'])

        return sync_analysis
```

#### Cut Rhythm Analyzer

```python
class CutRhythmAnalyzer:
    """
    Analyzes video cut patterns for influence techniques.

    Research basis: Rapid cuts (< 2s) reduce analytical processing
    and increase emotional response.
    """

    THRESHOLDS = {
        'rapid_cut': 2.0,           # seconds — cuts below this reduce analysis
        'hypnotic_rhythm': 4.0,     # seconds — regular rhythm induces trance-like
        'contrast_cut': 0.5,        # seconds — flash cuts for subliminal effect
        'standard_narrative': 6.0   # seconds — normal storytelling pace
    }

    def analyze_cuts(self, cut_timestamps: List[float]) -> Dict:
        """
        Analyze cut timing pattern.

        Args:
            cut_timestamps: List of timestamps (seconds) where cuts occur
        """
        if len(cut_timestamps) < 2:
            return {'analyzed': False, 'reason': 'insufficient_cuts'}

        intervals = [
            cut_timestamps[i+1] - cut_timestamps[i]
            for i in range(len(cut_timestamps) - 1)
        ]

        avg_interval = sum(intervals) / len(intervals)
        rapid_cuts = sum(1 for i in intervals if i < self.THRESHOLDS['rapid_cut'])
        flash_cuts = sum(1 for i in intervals if i < self.THRESHOLDS['contrast_cut'])

        # Rhythm regularity (low std = more hypnotic)
        import statistics
        rhythm_std = statistics.stdev(intervals) if len(intervals) > 1 else 0
        rhythm_regularity = 1.0 - min(1.0, rhythm_std / avg_interval) if avg_interval > 0 else 0

        # Acceleration detection (cuts getting faster)
        first_half = intervals[:len(intervals)//2]
        second_half = intervals[len(intervals)//2:]
        acceleration = (
            (sum(first_half)/len(first_half)) - (sum(second_half)/len(second_half))
        ) / (sum(first_half)/len(first_half)) if first_half and second_half else 0

        influence_types = []
        if rapid_cuts / len(intervals) > 0.5:
            influence_types.append('rapid_cut_overwhelm')
        if rhythm_regularity > 0.8 and avg_interval < self.THRESHOLDS['hypnotic_rhythm']:
            influence_types.append('hypnotic_rhythm')
        if flash_cuts > 0:
            influence_types.append('subliminal_flash')
        if acceleration > 0.3:
            influence_types.append('escalating_pace')

        return {
            'total_cuts': len(intervals),
            'average_interval': round(avg_interval, 2),
            'rapid_cut_ratio': round(rapid_cuts / len(intervals), 2),
            'flash_cuts': flash_cuts,
            'rhythm_regularity': round(rhythm_regularity, 2),
            'acceleration': round(acceleration, 2),
            'influence_types': influence_types,
            'risk_score': min(1.0,
                (rapid_cuts / len(intervals)) * 0.4 +
                rhythm_regularity * 0.2 +
                (flash_cuts > 0) * 0.3 +
                acceleration * 0.1
            )
        }
```

---

### 4.2 Social Network Dynamics

```python
@dataclass
class CascadeMetrics:
    """Metrics for information cascade analysis"""
    reach: int = 0
    depth: int = 0
    velocity: float = 0.0               # Shares per hour
    homogeneity_score: float = 0.0
    bot_participation_rate: float = 0.0
    phase: str = ""                      # introduction, acceleration, saturation, stabilization
    echo_chamber_score: float = 0.0

@dataclass
class AccountSuspicionScore:
    """Suspicion scoring for potential bot/fake accounts"""
    account_id: str = ""
    creation_recency: float = 0.0
    posting_regularity: float = 0.0
    engagement_ratio: float = 0.0
    content_originality: float = 0.0
    network_clustering: float = 0.0
    temporal_patterns: float = 0.0
    overall_bot_probability: float = 0.0

class SocialNetworkInfluenceDetector:
    """
    Detects influence operations in social network dynamics.

    Covers: cascade analysis, bot detection, coordinated behavior,
    emotional contagion, echo chamber formation.
    """

    @dataclass
    class CascadeMetrics:
        """Metrics for information cascade analysis"""
        cascade_depth: int
        cascade_breadth: int
        velocity: float                     # shares per hour
        bot_participation_rate: float
        emotional_amplification: float
        cross_community_bridges: int
        phase: str                          # 'seeding', 'growth', 'viral', 'saturation', 'decay'

    @dataclass
    class AccountSuspicionScore:
        """Bot/coordinated account suspicion assessment"""
        account_id: str
        suspicion_score: float              # 0-1
        indicators: List[str]
        account_age_days: int
        posting_regularity: float           # 0-1 (1 = perfectly regular)
        content_originality: float          # 0-1
        network_pattern: str                # 'organic', 'amplifier', 'bridge', 'coordinator'

    BOT_INDICATORS = {
        'timing': {
            'posting_interval_cv': 0.1,      # Coefficient of variation < 0.1 = bot-like regularity
            'response_time_seconds': 5,       # Responds < 5 seconds = suspicious
            'active_hours_per_day': 20        # Active > 20 hours = suspicious
        },
        'content': {
            'hashtag_ratio_threshold': 0.5,   # > 50% of tweets have hashtags
            'url_ratio_threshold': 0.7,       # > 70% contain URLs
            'retweet_ratio_threshold': 0.9,   # > 90% retweets = amplifier
            'language_diversity_threshold': 0.2  # Low diversity = template-based
        },
        'network': {
            'follower_following_ratio': 0.01,  # Very low = bot farm
            'cluster_coefficient': 0.9,        # Very high = coordinated group
            'reciprocity_rate': 0.01           # Very low reciprocity = not organic
        }
    }

    COORDINATED_BEHAVIOR_SIGNALS = {
        'temporal_coordination': {
            'posting_within_window_seconds': 60,
            'minimum_accounts': 5,
            'similar_content_threshold': 0.7
        },
        'content_coordination': {
            'identical_text_threshold': 0.95,
            'shared_url_pattern': True,
            'hashtag_set_overlap': 0.8
        },
        'network_coordination': {
            'mutual_follow_cluster': 10,
            'simultaneous_following': True,
            'creation_date_cluster_days': 7
        }
    }

    def analyze_cascade(self, posts: List[Dict], shares: List[Dict]) -> CascadeMetrics:
        """Analyze information cascade for influence patterns"""
        if not posts or not shares:
            return None

        # Calculate cascade metrics
        total_shares = len(shares)
        time_span = max(s.get('timestamp', 0) for s in shares) - min(s.get('timestamp', 0) for s in shares)
        velocity = total_shares / (time_span / 3600) if time_span > 0 else 0

        # Cascade depth (max reshare chain)
        depth = max(s.get('depth', 1) for s in shares)

        # Cascade breadth (unique sharers)
        breadth = len(set(s.get('user_id', '') for s in shares))

        # Bot participation estimate
        bot_count = sum(1 for s in shares if self._is_likely_bot(s))
        bot_rate = bot_count / len(shares) if shares else 0

        # Emotional amplification
        original_sentiment = posts[0].get('sentiment_score', 0) if posts else 0
        shared_sentiments = [s.get('added_sentiment', 0) for s in shares if 'added_sentiment' in s]
        emotional_amp = (
            sum(abs(s) for s in shared_sentiments) / len(shared_sentiments)
            if shared_sentiments else 0
        )

        # Phase detection
        phase = self._detect_cascade_phase(shares, time_span)

        return self.CascadeMetrics(
            cascade_depth=depth,
            cascade_breadth=breadth,
            velocity=round(velocity, 1),
            bot_participation_rate=round(bot_rate, 3),
            emotional_amplification=round(emotional_amp, 3),
            cross_community_bridges=self._count_community_bridges(shares),
            phase=phase
        )

    def _is_likely_bot(self, share_data: Dict) -> bool:
        """Quick bot assessment based on share metadata"""
        score = 0
        if share_data.get('response_time_seconds', 999) < self.BOT_INDICATORS['timing']['response_time_seconds']:
            score += 1
        if share_data.get('account_age_days', 365) < 30:
            score += 1
        if share_data.get('is_retweet', False) and share_data.get('retweet_ratio', 0) > 0.9:
            score += 1
        return score >= 2

    def _detect_cascade_phase(self, shares: List[Dict], time_span: float) -> str:
        """Detect current phase of information cascade"""
        if not shares:
            return 'inactive'

        # Divide timeline into quartiles
        quarter = time_span / 4 if time_span > 0 else 1
        timestamps = sorted(s.get('timestamp', 0) for s in shares)
        min_time = timestamps[0]

        q1 = sum(1 for t in timestamps if t - min_time < quarter)
        q2 = sum(1 for t in timestamps if quarter <= t - min_time < 2 * quarter)
        q3 = sum(1 for t in timestamps if 2 * quarter <= t - min_time < 3 * quarter)
        q4 = sum(1 for t in timestamps if t - min_time >= 3 * quarter)

        total = len(timestamps)
        if q1 / total > 0.6:
            return 'seeding'
        elif q2 / total > 0.4:
            return 'growth'
        elif q3 / total > 0.3:
            return 'viral'
        elif q4 / total > 0.4:
            return 'decay'
        return 'saturation'

    def _count_community_bridges(self, shares: List[Dict]) -> int:
        """Count cross-community bridge events"""
        communities = set()
        bridges = 0
        for share in shares:
            community = share.get('user_community', 'unknown')
            if community not in communities and len(communities) > 0:
                bridges += 1
            communities.add(community)
        return bridges


class EmotionalContagionDetector:
    """Detects emotional contagion patterns in social feeds"""

    CONTAGION_THRESHOLDS = {
        'sentiment_shift_threshold': 0.3,    # Significant shift in feed sentiment
        'anger_contagion_multiplier': 2.5,   # Anger spreads 2.5x faster
        'fear_contagion_multiplier': 2.0,
        'joy_contagion_multiplier': 1.2,
        'sadness_contagion_multiplier': 1.5
    }

    def analyze_feed_contagion(self, feed_items: List[Dict]) -> Dict:
        """Analyze feed for emotional contagion patterns"""
        if len(feed_items) < 5:
            return {'analyzed': False, 'reason': 'insufficient_items'}

        sentiments = [item.get('sentiment', 'neutral') for item in feed_items]
        from collections import Counter
        distribution = Counter(sentiments)

        # Check for dominant negative emotion
        negative_emotions = ['anger', 'fear', 'sadness', 'outrage', 'anxiety']
        negative_ratio = sum(distribution.get(e, 0) for e in negative_emotions) / len(sentiments)

        # Check for emotional escalation
        sentiment_scores = [item.get('sentiment_score', 0) for item in feed_items]
        escalation = self._detect_escalation(sentiment_scores)

        return {
            'dominant_emotion': distribution.most_common(1)[0][0] if distribution else 'none',
            'negative_ratio': round(negative_ratio, 2),
            'emotional_escalation': escalation,
            'contagion_risk': 'high' if negative_ratio > 0.6 else 'moderate' if negative_ratio > 0.3 else 'low',
            'distribution': dict(distribution)
        }

    def _detect_escalation(self, scores: List[float]) -> Dict:
        """Detect if emotional intensity escalates through feed"""
        if len(scores) < 4:
            return {'detected': False}

        mid = len(scores) // 2
        first_half_avg = sum(abs(s) for s in scores[:mid]) / mid
        second_half_avg = sum(abs(s) for s in scores[mid:]) / (len(scores) - mid)

        escalation = (second_half_avg - first_half_avg) / first_half_avg if first_half_avg > 0 else 0

        return {
            'detected': escalation > 0.2,
            'escalation_rate': round(escalation, 2),
            'first_half_intensity': round(first_half_avg, 2),
            'second_half_intensity': round(second_half_avg, 2)
        }


class EchoChAmberDetector:
    """Detects echo chamber / filter bubble patterns"""

    def analyze_information_diversity(self, feed_data: Dict) -> Dict:
        """
        Analyze feed for information diversity.

        Args:
            feed_data: Dict with 'sources', 'viewpoints', 'topics',
                      'recommended_content', 'user_interactions'
        """
        sources = feed_data.get('sources', [])
        viewpoints = feed_data.get('viewpoints', [])

        # Source diversity
        unique_sources = len(set(sources))
        source_diversity = unique_sources / len(sources) if sources else 0

        # Viewpoint diversity
        unique_viewpoints = len(set(viewpoints))
        viewpoint_diversity = unique_viewpoints / max(len(viewpoints), 1)

        # Echo chamber score (inverse of diversity)
        echo_score = 1.0 - ((source_diversity + viewpoint_diversity) / 2)

        return {
            'source_diversity': round(source_diversity, 2),
            'viewpoint_diversity': round(viewpoint_diversity, 2),
            'echo_chamber_score': round(echo_score, 2),
            'unique_sources': unique_sources,
            'total_sources': len(sources),
            'assessment': 'echo_chamber' if echo_score > 0.7 else 'partial_bubble' if echo_score > 0.4 else 'diverse'
        }
```

---

### 4.3 Trust Architecture

```python
class TrustInfluenceType(Enum):
    RELATIONSHIP_HISTORY = "leveraging_past_relationship"
    FUTURE_EXPECTATIONS = "promises_threats_rewards"
    AUTHORITY_IMPERSONATION = "fake_authority"
    AFFINITY_FRAUD = "shared_group_intensity"
    RECIPROCITY_TRIGGER = "unsolicited_gift_obligation"
    COMMITMENT_ESCALATION = "foot_in_door"
    URGENCY_PRESSURE = "time_pressure_trust_bypass"
    SOCIAL_PROOF_FABRICATION = "fake_endorsements"

@dataclass
class TrustInfluenceIndicator:
    """Indicators of trust-based influence"""
    influence_type: TrustInfluenceType
    confidence: float
    evidence: List[str]
    risk_level: str       # low, medium, high, critical

@dataclass
class GroomingStageAnalysis:
    """Analysis of potential grooming behavior"""
    stage: str            # selection, trust_building, desensitization, application
    indicators: List[str]
    progression_velocity: float    # How fast moving through stages
    risk_score: float

class TrustInfluenceDetector:
    """
    Detects trust-based influence patterns in conversations and content.

    Covers: authority exploitation, rapport building for manipulation,
    trust escalation, grooming patterns.
    """

    class TrustInfluenceType(Enum):
        AUTHORITY_CLAIM = "authority_claim"
        RAPPORT_BUILDING = "rapport_building"
        VULNERABILITY_SHARING = "vulnerability_sharing"
        RECIPROCITY_CREATION = "reciprocity_creation"
        COMMITMENT_ESCALATION = "commitment_escalation"
        ISOLATION_ATTEMPT = "isolation_attempt"
        URGENCY_WITH_TRUST = "urgency_with_trust"
        IDENTITY_MIRRORING = "identity_mirroring"

    TRUST_INFLUENCE_PATTERNS = {
        'authority_claim': [
            r'(?i)(trust me|believe me|I (know|understand) (exactly|precisely)|in my (experience|expertise|years))',
            r'(?i)(as (a|an) (expert|professional|specialist|doctor|lawyer|advisor)|I\'ve (seen|helped|worked with) (hundreds|thousands|many))'
        ],
        'rapport_building': [
            r'(?i)(I (completely|totally|absolutely) (understand|get it|feel you)|me too|same here|I\'ve been (there|through that))',
            r'(?i)(we\'re (alike|similar|the same)|you remind me of|I see (myself|a lot of me) in you)'
        ],
        'vulnerability_sharing': [
            r'(?i)(I\'m (going to|gonna) (share|tell you) something (personal|private|I don\'t usually))',
            r'(?i)(between (you and me|us)|just between|I trust you (enough|with))',
            r'(?i)(I (rarely|never|don\'t usually) (tell|share|open up) (about|to) (anyone|people))'
        ],
        'isolation_attempt': [
            r'(?i)(don\'t (tell|listen to|trust|believe) (them|others?|anyone else|your (friends|family)))',
            r'(?i)(only I (understand|know|can help)|no one else (gets?|understands?|cares?))',
            r'(?i)(they (don\'t|won\'t|can\'t) (understand|help|care about) you (like|the way) I)'
        ],
        'commitment_escalation': [
            r'(?i)(you (already|said|agreed|promised|committed))',
            r'(?i)(since you (already|agreed|said|started))',
            r'(?i)(just (one|a little|a small) (more|thing|step|favor))',
            r'(?i)(after (all|everything) (we\'ve|I\'ve) (been through|done|shared))'
        ],
        'identity_mirroring': [
            r'(?i)(I\'m (just like|exactly like|the same as) you)',
            r'(?i)(we (both|share|have (the same|so much in common)))',
            r'(?i)((great|good) (minds|people) think alike)'
        ]
    }

    def analyze_message(self, text: str) -> List:
        """Analyze single message for trust influence indicators"""
        indicators = []

        for influence_type, patterns in self.TRUST_INFLUENCE_PATTERNS.items():
            for pattern in patterns:
                matches = re.findall(pattern, text)
                if matches:
                    indicators.append({
                        'influence_type': influence_type,
                        'matches': [m[0] if isinstance(m, tuple) else m for m in matches],
                        'risk_level': 'critical' if influence_type in ['isolation_attempt', 'commitment_escalation'] else 'moderate'
                    })

        return indicators

    def analyze_conversation(self, messages: List[Dict]) -> Dict:
        """
        Analyze conversation thread for trust influence escalation.

        Args:
            messages: List of {'sender': str, 'text': str, 'timestamp': str}
        """
        all_indicators = []
        escalation_timeline = []

        for msg in messages:
            indicators = self.analyze_message(msg.get('text', ''))
            if indicators:
                all_indicators.extend(indicators)
                escalation_timeline.append({
                    'message_index': messages.index(msg),
                    'sender': msg.get('sender'),
                    'indicators': [i['influence_type'] for i in indicators]
                })

        # Check for escalation pattern
        types_over_time = [i['influence_type'] for i in all_indicators]
        escalation_detected = self._check_escalation_pattern(types_over_time)

        return {
            'total_indicators': len(all_indicators),
            'unique_types': list(set(i['influence_type'] for i in all_indicators)),
            'escalation_detected': escalation_detected,
            'timeline': escalation_timeline,
            'risk_score': min(1.0, len(all_indicators) * 0.1 + (0.3 if escalation_detected else 0))
        }

    def _check_escalation_pattern(self, types: List[str]) -> bool:
        """Check if trust influence types escalate in severity"""
        severity_order = [
            'rapport_building',
            'identity_mirroring',
            'vulnerability_sharing',
            'reciprocity_creation',
            'authority_claim',
            'commitment_escalation',
            'isolation_attempt',
            'urgency_with_trust'
        ]

        if len(types) < 3:
            return False

        # Check if later types are generally higher severity
        indices = [severity_order.index(t) for t in types if t in severity_order]
        if len(indices) < 3:
            return False

        first_half = indices[:len(indices)//2]
        second_half = indices[len(indices)//2:]
        return sum(second_half) / len(second_half) > sum(first_half) / len(first_half)


class GroomingPatternDetector:
    """
    Detects grooming patterns in interaction sequences.

    4 stages: selection → trust_building → desensitization → application
    """

    GROOMING_STAGES = {
        'selection': {
            'patterns': [
                r'(?i)(you seem (special|different|unique|mature|smart))',
                r'(?i)(I (noticed|can tell|see that) you\'re (not like|different from|special))',
                r'(?i)(most people (don\'t|can\'t|wouldn\'t) (understand|appreciate|get))'
            ],
            'indicators': ['flattery', 'isolation_from_peers', 'special_treatment']
        },
        'trust_building': {
            'patterns': [
                r'(?i)(you can (trust|confide in|rely on|count on) me)',
                r'(?i)(I\'m (here|always here) for you)',
                r'(?i)(our (special|secret|private) (bond|connection|relationship))',
                r'(?i)(no one (needs|has) to know)'
            ],
            'indicators': ['secret_keeping', 'exclusive_relationship', 'availability']
        },
        'desensitization': {
            'patterns': [
                r'(?i)(it\'s (normal|natural|okay|fine|not a big deal))',
                r'(?i)(everyone does (it|this)|lots of people)',
                r'(?i)(don\'t be (shy|scared|worried|afraid))',
                r'(?i)(relax|calm down|it\'s (just|only))'
            ],
            'indicators': ['boundary_pushing', 'normalization', 'minimization']
        },
        'application': {
            'patterns': [
                r'(?i)(you (owe|promised|said you would|agreed))',
                r'(?i)(after (everything|all) I\'ve (done|given|sacrificed))',
                r'(?i)(don\'t (ruin|destroy|throw away) (what we have|this|our))',
                r'(?i)(if you (really|truly) (cared|loved|trusted) me)'
            ],
            'indicators': ['guilt_manipulation', 'obligation', 'emotional_blackmail']
        }
    }

    def analyze_interaction_sequence(self, messages: List[Dict]) -> Dict:
        """
        Analyze message sequence for grooming pattern progression.

        Returns:
            Dict with stage detection, progression, and risk score
        """
        stage_detections = {stage: [] for stage in self.GROOMING_STAGES}

        for i, msg in enumerate(messages):
            text = msg.get('text', '')
            for stage, config in self.GROOMING_STAGES.items():
                for pattern in config['patterns']:
                    if re.search(pattern, text):
                        stage_detections[stage].append({
                            'message_index': i,
                            'text_sample': text[:100],
                            'pattern_matched': pattern
                        })

        # Check for stage progression
        active_stages = [s for s, detections in stage_detections.items() if detections]
        progression = self._assess_progression(stage_detections)

        # Risk score
        risk = 0.0
        stage_weights = {'selection': 0.1, 'trust_building': 0.2, 'desensitization': 0.3, 'application': 0.5}
        for stage, detections in stage_detections.items():
            if detections:
                risk += stage_weights.get(stage, 0.1)
        if progression['sequential']:
            risk += 0.2

        return {
            'stage': active_stages[-1] if active_stages else 'none',
            'active_stages': active_stages,
            'detections_per_stage': {s: len(d) for s, d in stage_detections.items()},
            'progression': progression,
            'risk_score': min(1.0, risk),
            'assessment': 'grooming_pattern_detected' if risk > 0.5 else 'monitoring_recommended' if risk > 0.2 else 'low_risk'
        }

    def _assess_progression(self, stage_detections: Dict) -> Dict:
        """Assess if stages occur in expected sequential order"""
        stage_order = ['selection', 'trust_building', 'desensitization', 'application']
        first_occurrence = {}

        for stage in stage_order:
            if stage_detections[stage]:
                first_occurrence[stage] = min(d['message_index'] for d in stage_detections[stage])

        # Check if stages appear in order
        ordered_stages = sorted(first_occurrence.keys(), key=lambda s: first_occurrence[s])
        expected_order = [s for s in stage_order if s in ordered_stages]

        return {
            'sequential': ordered_stages == expected_order and len(ordered_stages) >= 2,
            'stages_in_order': ordered_stages,
            'stage_count': len(ordered_stages)
        }
```

---

### 4.4 Platform-Specific Mechanics

```python
class GamificationInfluenceType(Enum):
    STREAK_LOSS_AVERSION = "streak_punishment"
    VARIABLE_RATIO_REWARD = "slot_machine"
    SOCIAL_COMPARISON = "leaderboard_pressure"
    ARTIFICIAL_SCARCITY = "limited_availability"
    PROGRESS_ILLUSION = "fake_progress"
    FOMO_NOTIFICATION = "fear_of_missing_out"
    INFINITE_SCROLL = "bottomless_consumption"
    AUTOPLAY = "friction_removal"
    ROACH_MOTEL = "easy_in_hard_out"

@dataclass
class GamificationAnalysis:
    """Analysis of gamification influence"""
    influence_types: List[GamificationInfluenceType] = field(default_factory=list)
    streak_dependency_score: float = 0.0
    variable_reward_frequency: float = 0.0
    friction_asymmetry: float = 0.0           # signup ease vs cancel difficulty
    overall_influence_score: float = 0.0
    detailed_findings: Dict = field(default_factory=dict)

class PlatformInfluenceDetector:
    """
    Detects platform-specific influence mechanics:
    gamification, streaks, notifications, cancellation friction.
    """

    class GamificationInfluenceType(Enum):
        STREAK_PRESSURE = "streak_pressure"
        LEADERBOARD_COMPETITION = "leaderboard_competition"
        BADGE_COLLECTION = "badge_collection"
        LEVEL_PROGRESSION = "level_progression"
        DAILY_REWARD = "daily_reward"
        POINT_ACCUMULATION = "point_accumulation"

    STREAK_PATTERNS = {
        'text_indicators': [
            r'(?i)(\d+[- ]day streak|keep (your|the) streak|streak (frozen?|at risk|lost))',
            r'(?i)(don\'t (lose|break|end) your streak|maintain your streak)',
            r'(?i)(consecutive (days?|visits?|logins?|check[- ]ins?))'
        ],
        'loss_aversion_multiplier': 2.5,  # Losing a streak feels 2.5x worse than gaining
        'sunk_cost_threshold_days': 7     # After 7 days, sunk cost bias strongly active
    }

    NOTIFICATION_PATTERNS = {
        'urgency_notifications': [
            r'(?i)(you\'re (missing|losing)|someone (just|recently)|happening (now|right now))',
            r'(?i)(limited time|expiring (soon|today)|last chance)'
        ],
        'social_notifications': [
            r'(?i)(liked your|commented on|shared your|mentioned you|tagged you)',
            r'(?i)(is now following|sent you|wants to connect)'
        ],
        'fomo_notifications': [
            r'(?i)(trending|popular|going viral|don\'t miss|everyone is)',
            r'(?i)(\d+ people (are|have)|your friends? (liked|shared|are))'
        ],
        'optimal_timing': {
            'morning_peak': (7, 9),        # 7-9 AM — high open rates
            'lunch_peak': (12, 13),        # 12-1 PM — boredom check
            'evening_peak': (19, 21),      # 7-9 PM — leisure/wind-down
            'late_night': (22, 24)         # 10 PM-midnight — reduced inhibition
        }
    }

    CANCELLATION_FRICTION_INDICATORS = {
        'high_friction': [
            'phone_call_required',
            'chat_agent_required',
            'multiple_surveys',
            'waiting_period',
            'manager_escalation',
            'hidden_cancel_option',
            'guilt_trip_screens',
            'multiple_confirmation_steps'
        ],
        'moderate_friction': [
            'single_survey',
            'confirmation_dialog',
            'retention_offer',
            'feature_reminder'
        ],
        'legitimate': [
            'single_click_cancel',
            'clear_cancel_button',
            'confirmation_page',
            'feedback_optional'
        ]
    }

    def analyze_app_interface(self, interface_data: Dict) -> Dict:
        """Analyze app interface for platform influence mechanics"""
        findings = {
            'gamification': self._detect_gamification(interface_data),
            'notification_influence': self._detect_notification_influence(interface_data),
            'cancellation_friction': self._detect_cancellation_friction(interface_data),
            'engagement_loops': self._detect_engagement_loops(interface_data),
            'influence_types': [],
            'overall_influence_score': 0.0
        }

        # Aggregate
        scores = []
        if findings['gamification']['detected']:
            scores.append(findings['gamification']['score'])
            findings['influence_types'].extend(findings['gamification']['types'])
        if findings['notification_influence']['detected']:
            scores.append(findings['notification_influence']['score'])
        if findings['cancellation_friction']['detected']:
            scores.append(findings['cancellation_friction']['score'])
        if findings['engagement_loops']['detected']:
            scores.append(findings['engagement_loops']['score'])

        findings['overall_influence_score'] = sum(scores) / max(len(scores), 1) if scores else 0

        return findings

    def _detect_gamification(self, data: Dict) -> Dict:
        """Detect gamification influence patterns"""
        features = data.get('features', [])
        gamification_features = ['streak', 'leaderboard', 'badge', 'level', 'daily_reward', 'points', 'xp']

        detected = [f for f in features if any(g in f.lower() for g in gamification_features)]
        types = []

        for f in detected:
            f_lower = f.lower()
            if 'streak' in f_lower:
                types.append(self.GamificationInfluenceType.STREAK_PRESSURE.value)
            elif 'leaderboard' in f_lower:
                types.append(self.GamificationInfluenceType.LEADERBOARD_COMPETITION.value)
            elif 'badge' in f_lower:
                types.append(self.GamificationInfluenceType.BADGE_COLLECTION.value)
            elif 'level' in f_lower or 'xp' in f_lower:
                types.append(self.GamificationInfluenceType.LEVEL_PROGRESSION.value)
            elif 'daily' in f_lower or 'reward' in f_lower:
                types.append(self.GamificationInfluenceType.DAILY_REWARD.value)
            elif 'point' in f_lower:
                types.append(self.GamificationInfluenceType.POINT_ACCUMULATION.value)

        return {
            'detected': len(detected) > 0,
            'features': detected,
            'types': types,
            'score': min(1.0, len(detected) * 0.2)
        }

    def _detect_notification_influence(self, data: Dict) -> Dict:
        """Detect notification-based influence"""
        notifications = data.get('notification_samples', [])
        urgency = 0
        social = 0
        fomo = 0

        for notif in notifications:
            text = notif.get('text', '') if isinstance(notif, dict) else str(notif)
            for p in self.NOTIFICATION_PATTERNS['urgency_notifications']:
                if re.search(p, text):
                    urgency += 1
            for p in self.NOTIFICATION_PATTERNS['social_notifications']:
                if re.search(p, text):
                    social += 1
            for p in self.NOTIFICATION_PATTERNS['fomo_notifications']:
                if re.search(p, text):
                    fomo += 1

        total = urgency + social + fomo
        return {
            'detected': total > 0,
            'urgency_count': urgency,
            'social_count': social,
            'fomo_count': fomo,
            'score': min(1.0, total * 0.1)
        }

    def _detect_cancellation_friction(self, data: Dict) -> Dict:
        """Detect cancellation friction patterns"""
        signup_steps = data.get('signup_steps', 0)
        cancel_steps = data.get('cancel_steps', 0)
        cancel_reqs = data.get('cancel_requirements', [])

        high_friction = [r for r in cancel_reqs
                        if r in self.CANCELLATION_FRICTION_INDICATORS['high_friction']]
        moderate_friction = [r for r in cancel_reqs
                           if r in self.CANCELLATION_FRICTION_INDICATORS['moderate_friction']]

        friction_ratio = cancel_steps / signup_steps if signup_steps > 0 else 0
        score = min(1.0, len(high_friction) * 0.2 + len(moderate_friction) * 0.1 + max(0, (friction_ratio - 1) * 0.2))

        return {
            'detected': len(high_friction) > 0 or friction_ratio > 2,
            'signup_steps': signup_steps,
            'cancel_steps': cancel_steps,
            'friction_ratio': round(friction_ratio, 1),
            'high_friction_elements': high_friction,
            'moderate_friction_elements': moderate_friction,
            'score': score
        }

    def _detect_engagement_loops(self, data: Dict) -> Dict:
        """Detect compulsive engagement loop patterns"""
        features = data.get('features', [])
        loop_indicators = ['infinite_scroll', 'auto_play', 'pull_to_refresh',
                          'push_notifications', 'variable_rewards']

        detected = [f for f in features if any(l in f.lower().replace(' ', '_') for l in loop_indicators)]

        reward_schedule = data.get('reward_schedule', 'fixed')
        is_variable = reward_schedule == 'variable'

        return {
            'detected': len(detected) > 0 or is_variable,
            'loop_elements': detected,
            'variable_reward_schedule': is_variable,
            'score': min(1.0, len(detected) * 0.2 + (0.3 if is_variable else 0))
        }


class InfiniteScrollDetector:
    """
    Detects infinite scroll influence patterns.

    Research: ScienceDirect 2025 — Scroll immersion reduces
    time perception accuracy by 40-60%.
    """

    SCROLL_METRICS = {
        'session_duration_threshold_minutes': 30,  # Extended session indicator
        'content_consumed_threshold': 50,          # Items consumed without natural stopping
        'scroll_velocity_threshold': 500,          # pixels/second — compulsive scrolling
        'pause_frequency_threshold': 0.1,          # Pauses per item — low = compulsive
        'time_distortion_marker': 0.4              # 40% time perception inaccuracy
    }

    def analyze_scroll_session(self, session_data: Dict) -> Dict:
        """Analyze scroll session for compulsive patterns"""
        duration = session_data.get('duration_minutes', 0)
        items_consumed = session_data.get('items_consumed', 0)
        avg_velocity = session_data.get('avg_scroll_velocity', 0)
        pause_count = session_data.get('pause_count', 0)

        pause_frequency = pause_count / items_consumed if items_consumed > 0 else 1

        compulsive_indicators = 0
        if duration > self.SCROLL_METRICS['session_duration_threshold_minutes']:
            compulsive_indicators += 1
        if items_consumed > self.SCROLL_METRICS['content_consumed_threshold']:
            compulsive_indicators += 1
        if avg_velocity > self.SCROLL_METRICS['scroll_velocity_threshold']:
            compulsive_indicators += 1
        if pause_frequency < self.SCROLL_METRICS['pause_frequency_threshold']:
            compulsive_indicators += 1

        return {
            'session_duration_minutes': duration,
            'items_consumed': items_consumed,
            'average_scroll_velocity': avg_velocity,
            'pause_frequency': round(pause_frequency, 3),
            'compulsive_indicators': compulsive_indicators,
            'risk_level': 'high' if compulsive_indicators >= 3 else 'moderate' if compulsive_indicators >= 2 else 'low',
            'estimated_time_distortion': f"{self.SCROLL_METRICS['time_distortion_marker'] * 100}% if session > {self.SCROLL_METRICS['session_duration_threshold_minutes']} min"
        }
```

---

### 4.5 Physiological Validation Methods

```python
@dataclass
class PhysiologicalReading:
    """Single physiological measurement"""
    timestamp: float
    pupil_diameter: float = 0.0       # mm
    blink_rate: float = 0.0           # per minute
    gsr: float = 0.0                  # microsiemens
    hrv: float = 0.0                  # ms
    gaze_x: float = 0.0
    gaze_y: float = 0.0
    fixation_duration: float = 0.0    # ms

@dataclass
class PhysiologicalState:
    """Interpreted physiological state"""
    arousal_level: float = 0.0        # 0-1
    cognitive_load: float = 0.0       # 0-1
    emotional_valence: float = 0.0    # -1 to 1
    critical_engagement: float = 0.0  # 0-1 (low = vulnerable)
    stress_level: float = 0.0        # 0-1
    state_label: str = ""             # e.g., "vulnerable", "engaged", "stressed"

class PhysiologicalInfluenceDetector:
    """
    Detects influence through physiological response analysis.

    Research-calibrated thresholds from peer-reviewed studies.
    """

    READING_THRESHOLDS = {
        'pupil_dilation': {
            'baseline_mm': 3.5,
            'interest_increase_mm': 0.5,
            'arousal_increase_mm': 1.0,
            'cognitive_load_increase_mm': 0.3,
            'measurement': 'pupillometry'
        },
        'blink_rate': {
            'baseline_per_minute': 17,
            'cognitive_load_decrease': 0.5,    # Blinks decrease under load
            'boredom_increase': 1.5,           # Blinks increase with boredom
            'deception_increase': 1.3          # Blinks increase when processing deception
        },
        'skin_conductance': {
            'baseline_microsiemens': 2.0,
            'emotional_response_increase': 0.5,
            'fear_response_increase': 1.5,
            'habituation_decrease_per_exposure': 0.1
        },
        'heart_rate_variability': {
            'baseline_ms': 50,                  # RMSSD
            'stress_decrease_threshold': 0.2,   # 20% decrease = stress
            'relaxation_increase_threshold': 0.15,
            'emotional_engagement_pattern': 'decreased_HF_power'
        }
    }

    def analyze_physiological_response(self, readings: List[Dict], content_events: List[Dict] = None) -> Dict:
        """
        Analyze physiological readings for influence response patterns.

        Args:
            readings: Timestamped biometric readings
            content_events: Optional content timeline to correlate with responses
        """
        if len(readings) < 10:
            return {'analyzed': False, 'reason': 'insufficient_data'}

        # Calculate baselines (first 5 readings)
        baselines = {
            'pupil': sum(r.get('pupil_diameter', 0) for r in readings[:5]) / 5,
            'blink_rate': sum(r.get('blink_rate', 0) for r in readings[:5]) / 5,
            'skin_conductance': sum(r.get('skin_conductance', 0) for r in readings[:5]) / 5,
            'hrv': sum(r.get('hrv_rmssd', 0) for r in readings[:5]) / 5
        }

        # Analyze deviations
        responses = []
        for reading in readings[5:]:
            response = {
                'timestamp': reading.get('timestamp'),
                'pupil_deviation': reading.get('pupil_diameter', 0) - baselines['pupil'],
                'blink_deviation': (reading.get('blink_rate', 0) - baselines['blink_rate']) / baselines['blink_rate'] if baselines['blink_rate'] > 0 else 0,
                'sc_deviation': reading.get('skin_conductance', 0) - baselines['skin_conductance'],
                'hrv_deviation': (reading.get('hrv_rmssd', 0) - baselines['hrv']) / baselines['hrv'] if baselines['hrv'] > 0 else 0
            }
            responses.append(response)

        # Detect influence response patterns
        arousal_peaks = sum(1 for r in responses if r['sc_deviation'] > self.READING_THRESHOLDS['skin_conductance']['emotional_response_increase'])
        cognitive_load = sum(1 for r in responses if r['pupil_deviation'] > self.READING_THRESHOLDS['pupil_dilation']['cognitive_load_increase_mm'])
        stress = sum(1 for r in responses if r['hrv_deviation'] < -self.READING_THRESHOLDS['heart_rate_variability']['stress_decrease_threshold'])

        return {
            'baselines': baselines,
            'arousal_peaks': arousal_peaks,
            'cognitive_load_episodes': cognitive_load,
            'stress_episodes': stress,
            'influence_response_detected': arousal_peaks > 3 or stress > 2,
            'risk_score': min(1.0, (arousal_peaks * 0.1 + cognitive_load * 0.05 + stress * 0.15))
        }


class GazePatternAnalyzer:
    """
    Analyzes gaze patterns for attention manipulation detection.

    Uses Area of Interest (AOI) analysis and scanpath classification.
    """

    def analyze_gaze_data(self, gaze_points: List[Dict], aoi_definitions: Dict) -> Dict:
        """
        Analyze gaze data against Areas of Interest.

        Args:
            gaze_points: List of {'x': float, 'y': float, 'timestamp': float, 'duration_ms': float}
            aoi_definitions: Dict of AOI name → {'x': range, 'y': range, 'type': str}
                type can be: 'cta_button', 'price', 'urgency', 'testimonial', 'content', 'navigation'
        """
        aoi_fixations = {name: {'count': 0, 'total_duration': 0, 'first_fixation': None}
                        for name in aoi_definitions}

        for point in gaze_points:
            for aoi_name, aoi in aoi_definitions.items():
                if (aoi['x'][0] <= point['x'] <= aoi['x'][1] and
                    aoi['y'][0] <= point['y'] <= aoi['y'][1]):
                    aoi_fixations[aoi_name]['count'] += 1
                    aoi_fixations[aoi_name]['total_duration'] += point.get('duration_ms', 0)
                    if aoi_fixations[aoi_name]['first_fixation'] is None:
                        aoi_fixations[aoi_name]['first_fixation'] = point['timestamp']

        # Analyze attention distribution
        total_duration = sum(f['total_duration'] for f in aoi_fixations.values())

        attention_distribution = {}
        for name, fix in aoi_fixations.items():
            attention_distribution[name] = {
                'fixation_count': fix['count'],
                'duration_ms': fix['total_duration'],
                'attention_share': fix['total_duration'] / total_duration if total_duration > 0 else 0,
                'first_fixation_time': fix['first_fixation']
            }

        # Check if persuasive elements capture disproportionate attention
        persuasive_aois = ['cta_button', 'price', 'urgency', 'testimonial']
        persuasive_attention = sum(
            attention_distribution.get(name, {}).get('attention_share', 0)
            for name, aoi in aoi_definitions.items()
            if aoi.get('type') in persuasive_aois
        )

        return {
            'attention_distribution': attention_distribution,
            'persuasive_element_attention_share': round(persuasive_attention, 3),
            'attention_captured': persuasive_attention > 0.5,
            'scanpath': self._classify_scanpath(gaze_points)
        }

    def _classify_scanpath(self, gaze_points: List[Dict]) -> str:
        """Classify scanpath pattern"""
        if len(gaze_points) < 5:
            return 'insufficient_data'

        # Simple classification based on pattern regularity
        x_positions = [p['x'] for p in gaze_points]
        y_positions = [p['y'] for p in gaze_points]

        import statistics
        x_std = statistics.stdev(x_positions) if len(x_positions) > 1 else 0
        y_std = statistics.stdev(y_positions) if len(y_positions) > 1 else 0

        if x_std < 50 and y_std < 50:
            return 'fixated'  # Attention locked on small area
        elif x_std > 200 and y_std > 200:
            return 'scanning'  # Wide exploration
        else:
            return 'guided'  # Following a designed path
```

---

### 4.6 Vulnerable Population Detection

```python
class VulnerabilityFactorType(Enum):
    AGE_CHILD = "child_developing_cognition"
    AGE_ADOLESCENT = "adolescent_risk_taking"
    AGE_ELDERLY = "elderly_cognitive_decline"
    COGNITIVE_LOAD = "high_cognitive_load"
    EMOTIONAL_STATE = "vulnerable_emotional_state"
    SOCIAL_ISOLATION = "isolated_lonely"
    NEURODIVERGENT = "neurodivergent_processing"
    MENTAL_HEALTH = "mental_health_condition"
    DIGITAL_LITERACY = "low_digital_literacy"
    FINANCIAL_STRESS = "financial_vulnerability"

@dataclass
class VulnerabilityProfile:
    """Individual vulnerability assessment"""
    factors: List[VulnerabilityFactorType] = field(default_factory=list)
    overall_vulnerability_score: float = 0.0
    risk_areas: List[str] = field(default_factory=list)
    protective_recommendations: List[str] = field(default_factory=list)
    requires_enhanced_protection: bool = False

class VulnerablePopulationDetector:
    """
    Detects content/design targeting vulnerable populations.

    Covers: children, elderly, neurodivergent individuals,
    those in emotional distress, financially vulnerable.
    """

    VULNERABILITY_PROFILES = {
        'children': {
            'age_range': (0, 17),
            'indicators': [
                'bright_colors_excessive',
                'cartoon_characters',
                'game_mechanics',
                'reward_sounds',
                'simple_language',
                'character_branding'
            ],
            'cognitive_factors': [
                'limited_impulse_control',
                'developing_critical_thinking',
                'susceptible_to_authority',
                'peer_pressure_vulnerability',
                'difficulty_distinguishing_ad_content'
            ],
            'multiplier': 2.0  # 2x risk weighting for children
        },
        'elderly': {
            'age_range': (65, 120),
            'indicators': [
                'large_font_requirement',
                'simplified_navigation',
                'phone_number_prominence',
                'trust_authority_heavy',
                'nostalgia_appeals',
                'health_fear_appeals'
            ],
            'cognitive_factors': [
                'processing_speed_decline',
                'working_memory_reduction',
                'increased_trust_tendency',
                'reduced_digital_literacy',
                'social_isolation_vulnerability'
            ],
            'multiplier': 1.8
        },
        'neurodivergent': {
            'indicators': [
                'pattern_exploitation',
                'routine_disruption',
                'sensory_overwhelm',
                'hyperfocus_exploitation',
                'social_cue_manipulation'
            ],
            'cognitive_factors': [
                'executive_function_differences',
                'impulse_control_variation',
                'pattern_recognition_differences',
                'social_processing_differences',
                'hyperfocus_susceptibility'
            ],
            'multiplier': 1.5
        },
        'emotionally_distressed': {
            'indicators': [
                'crisis_language',
                'desperation_appeals',
                'immediate_relief_promises',
                'isolation_content',
                'hopelessness_exploitation'
            ],
            'cognitive_factors': [
                'impaired_decision_making',
                'increased_impulsivity',
                'reduced_risk_assessment',
                'heightened_emotional_reactivity',
                'cognitive_narrowing'
            ],
            'multiplier': 1.7
        }
    }

    def assess_individual_vulnerability(self, user_profile: Dict) -> Dict:
        """
        Assess individual vulnerability based on profile.

        Args:
            user_profile: Dict with 'age', 'cognitive_indicators',
                         'emotional_state', 'social_connection_score',
                         'digital_literacy_score'
        """
        age = user_profile.get('age', 30)
        factors = []
        overall_score = 0.0

        # Age-based vulnerability
        if age <= 17:
            factors.append('child')
            overall_score += 0.4
        elif age >= 65:
            factors.append('elderly')
            overall_score += 0.3
            # Additional: USC Dornsife 2024 — APOE4 carriers 2x scam vulnerability
            if user_profile.get('apoe4_carrier', False):
                overall_score += 0.2

        # Cognitive indicators
        cognitive = user_profile.get('cognitive_indicators', [])
        cognitive_flags = ['processing_speed_decline', 'limited_impulse_control',
                          'executive_function_differences', 'working_memory_reduction']
        matched = [c for c in cognitive if c in cognitive_flags]
        overall_score += len(matched) * 0.1

        # Emotional state
        emotional = user_profile.get('emotional_state', 'neutral')
        high_risk_emotions = ['loneliness', 'depression', 'grief', 'anxiety', 'desperation', 'crisis']
        if emotional in high_risk_emotions:
            factors.append('emotionally_distressed')
            overall_score += 0.3

        # Social isolation
        social_score = user_profile.get('social_connection_score', 0.5)
        if social_score < 0.3:
            factors.append('socially_isolated')
            overall_score += 0.2

        # Digital literacy
        digital = user_profile.get('digital_literacy_score', 0.5)
        if digital < 0.3:
            factors.append('low_digital_literacy')
            overall_score += 0.15

        overall_score = min(1.0, overall_score)

        # Generate recommendations
        recommendations = self._generate_protective_recommendations(factors)

        return {
            'overall_vulnerability_score': round(overall_score, 2),
            'factors': factors,
            'risk_areas': self._identify_risk_areas(factors),
            'protective_recommendations': recommendations,
            'risk_multiplier': self._calculate_multiplier(factors)
        }

    def _identify_risk_areas(self, factors: List[str]) -> List[str]:
        """Identify specific risk areas based on vulnerability factors"""
        risk_map = {
            'child': ['loot boxes', 'social pressure', 'influencer marketing', 'data collection'],
            'elderly': ['phone scams', 'tech support scams', 'romance scams', 'health fraud'],
            'emotionally_distressed': ['predatory lending', 'miracle cures', 'emotional exploitation'],
            'socially_isolated': ['romance scams', 'community manipulation', 'radicalization'],
            'low_digital_literacy': ['phishing', 'fake websites', 'hidden charges', 'dark patterns']
        }
        risks = []
        for factor in factors:
            risks.extend(risk_map.get(factor, []))
        return list(set(risks))

    def _generate_protective_recommendations(self, factors: List[str]) -> List[str]:
        """Generate protective recommendations"""
        recs = []
        if 'child' in factors:
            recs.extend(['Enable parental controls', 'Limit exposure to targeted advertising',
                        'Disable in-app purchases', 'Monitor engagement patterns'])
        if 'elderly' in factors:
            recs.extend(['Enable fraud alerts', 'Implement cooling-off periods for purchases',
                        'Add trusted contact for high-value decisions'])
        if 'emotionally_distressed' in factors:
            recs.extend(['Delay major financial decisions', 'Enable purchase limits',
                        'Activate decision cooling-off periods'])
        if 'socially_isolated' in factors:
            recs.extend(['Verify new online contacts', 'Be cautious of rapid intimacy',
                        'Cross-check information with trusted sources'])
        return recs

    def _calculate_multiplier(self, factors: List[str]) -> float:
        """Calculate risk multiplier based on factors"""
        multiplier = 1.0
        for factor in factors:
            for profile_name, profile in self.VULNERABILITY_PROFILES.items():
                if factor in profile_name or factor in str(profile.get('indicators', [])):
                    multiplier = max(multiplier, profile.get('multiplier', 1.0))
        return multiplier


class ChildSafetyDetector:
    """
    Specialized detector for child-targeting patterns.

    Research basis: Thorn 2024, COPPA regulations
    """

    GROOMING_LANGUAGE_PATTERNS = [
        r'(?i)(how old are you|what grade|where do you go to school)',
        r'(?i)(don\'t tell (your|anyone|mom|dad|parents))',
        r'(?i)(you\'re (mature|grown up|special|different) for your age)',
        r'(?i)(our (little )?secret)',
        r'(?i)(send (me )?(a )?(pic|photo|picture|selfie))',
        r'(?i)(are you (home )?alone|when are your parents)'
    ]

    CHILD_TARGETED_ADVERTISING = [
        r'(?i)(kids?|children|boys? and girls?|little ones?)',
        r'(?i)(collect (them )?all|complete (the|your) (set|collection))',
        r'(?i)(ask (your )?(mom|dad|parents) (to buy|for))',
        r'(?i)(new (toys?|game|episode|character|season))',
        r'(?i)(limited edition|exclusive|rare|super rare|legendary)'
    ]

    def analyze_content_for_children(self, text: str, context: Dict = None) -> Dict:
        """Analyze content for child-targeting patterns"""
        grooming_matches = []
        for pattern in self.GROOMING_LANGUAGE_PATTERNS:
            matches = re.findall(pattern, text)
            if matches:
                grooming_matches.extend([m[0] if isinstance(m, tuple) else m for m in matches])

        ad_matches = []
        for pattern in self.CHILD_TARGETED_ADVERTISING:
            matches = re.findall(pattern, text)
            if matches:
                ad_matches.extend([m[0] if isinstance(m, tuple) else m for m in matches])

        return {
            'grooming_indicators': grooming_matches,
            'child_targeted_advertising': ad_matches,
            'grooming_risk': 'high' if len(grooming_matches) >= 2 else 'moderate' if grooming_matches else 'low',
            'targeting_risk': 'high' if len(ad_matches) >= 3 else 'moderate' if ad_matches else 'low',
            'overall_risk_score': min(1.0, len(grooming_matches) * 0.3 + len(ad_matches) * 0.1)
        }
```

---

### 4.7 Economic Influence Mechanics

```python
class PricingInfluenceType(Enum):
    DYNAMIC_PRICING = "real_time_price_adjustment"
    PERSONALIZED_PRICING = "surveillance_pricing"
    ANCHOR_PRICING = "reference_price_influence"
    DECOY_PRICING = "asymmetric_dominance"
    DRIP_PRICING = "hidden_fees_revealed_late"
    PARTITIONED_PRICING = "split_price_components"
    CHARM_PRICING = "psychological_pricing"
    ARTIFICIAL_SCARCITY = "fake_limited_stock"
    TIME_PRESSURE = "countdown_urgency"
    SUBSCRIPTION_TRAP = "difficult_cancellation"

@dataclass
class PricingAnalysis:
    """Analysis of pricing influence"""
    influence_types: List[PricingInfluenceType] = field(default_factory=list)
    anchor_effect_strength: float = 0.0
    decoy_detected: bool = False
    drip_pricing_amount: float = 0.0
    true_price_vs_displayed: float = 0.0
    urgency_tactics: List[str] = field(default_factory=list)
    overall_influence_score: float = 0.0

class EconomicInfluenceDetector:
    """
    Detects economic influence patterns in pricing and purchase flows.
    """

    class PricingInfluenceType(Enum):
        ANCHORING = "price_anchoring"
        DECOY = "decoy_pricing"
        DRIP_PRICING = "drip_pricing"
        DYNAMIC_PRICING = "dynamic_pricing"
        CHARM_PRICING = "charm_pricing"
        BUNDLE_FORCED = "forced_bundling"
        SUBSCRIPTION_TRAP = "subscription_trap"
        HIDDEN_FEES = "hidden_fees"
        LOSS_LEADER = "loss_leader"
        PARTITIONED_PRICING = "partitioned_pricing"

    def analyze_pricing_page(self, pricing_data: Dict) -> Dict:
        """
        Analyze pricing page for economic influence patterns.

        Returns comprehensive findings with influence types and scores.
        """
        findings = {}
        influence_types = []

        prices = pricing_data.get('prices', [])

        # Charm pricing ($X.99)
        charm = [p for p in prices
                if isinstance(p, dict) and str(p.get('displayed_price', '')).endswith(('99', '.99', '.95'))]
        if charm:
            findings['charm_pricing'] = {'detected': True, 'count': len(charm)}
            influence_types.append(self.PricingInfluenceType.CHARM_PRICING)

        # Drip pricing (hidden fees revealed late)
        if pricing_data.get('additional_fees', []):
            fees = pricing_data['additional_fees']
            findings['drip_pricing'] = {
                'detected': True,
                'hidden_fees': fees,
                'total_hidden': sum(f.get('amount', 0) for f in fees if isinstance(f, dict))
            }
            influence_types.append(self.PricingInfluenceType.DRIP_PRICING)

        # Decoy pricing
        if len(prices) >= 3:
            decoy = self._detect_decoy_option(prices)
            if decoy:
                findings['decoy'] = decoy
                influence_types.append(self.PricingInfluenceType.DECOY)

        # Dynamic pricing
        if pricing_data.get('price_varies_by_user', False) or pricing_data.get('price_changes_detected', False):
            findings['dynamic_pricing'] = {'detected': True}
            influence_types.append(self.PricingInfluenceType.DYNAMIC_PRICING)

        # Urgency elements on pricing
        urgency = pricing_data.get('urgency_elements', [])
        if urgency:
            findings['urgency_on_pricing'] = {
                'detected': True,
                'elements': urgency,
                'count': len(urgency)
            }

        score = min(1.0, len(influence_types) * 0.2)

        return {
            'findings': findings,
            'influence_types': [t.value for t in influence_types],
            'overall_influence_score': score
        }

    def _detect_decoy_option(self, prices: List) -> Optional[Dict]:
        """Detect decoy option in pricing tiers"""
        price_values = []
        for p in prices:
            val = p.get('displayed_price', 0) if isinstance(p, dict) else p
            name = p.get('name', f'tier_{len(price_values)}') if isinstance(p, dict) else f'tier_{len(price_values)}'
            price_values.append({'name': name, 'price': val})

        price_values.sort(key=lambda x: x['price'])

        if len(price_values) >= 3:
            low = price_values[0]['price']
            mid = price_values[1]['price']
            high = price_values[2]['price']

            if low > 0 and mid > 0 and high > 0:
                gap_1 = (mid - low) / low
                gap_2 = (high - mid) / mid if mid > 0 else 0

                if gap_1 > 0.5 and gap_2 < 0.3:
                    return {
                        'detected': True,
                        'likely_decoy': price_values[1]['name'],
                        'target': price_values[2]['name'],
                        'pattern': 'asymmetric_dominance'
                    }

        return None


class SubscriptionTrapDetector:
    """Detects subscription trap patterns"""

    TRAP_INDICATORS = {
        'enrollment': [
            'free_trial_auto_converts',
            'credit_card_required_for_free',
            'pre_checked_subscription',
            'subscription_buried_in_terms'
        ],
        'retention': [
            'cancel_requires_phone_call',
            'multiple_retention_screens',
            'guilt_trip_on_cancel',
            'hidden_cancel_button',
            'cancel_requires_survey',
            'cancel_requires_waiting_period',
            'cancel_penalty_fee'
        ],
        'pricing': [
            'introductory_price_jumps',
            'price_increase_notification_buried',
            'annual_vs_monthly_pressure',
            'auto_upgrade_to_higher_tier'
        ]
    }

    def analyze_subscription(self, sub_data: Dict) -> Dict:
        """Analyze subscription model for trap patterns"""
        enrollment_traps = []
        retention_traps = []
        pricing_traps = []

        for indicator in self.TRAP_INDICATORS['enrollment']:
            if sub_data.get(indicator, False):
                enrollment_traps.append(indicator)

        for indicator in self.TRAP_INDICATORS['retention']:
            if sub_data.get(indicator, False):
                retention_traps.append(indicator)

        for indicator in self.TRAP_INDICATORS['pricing']:
            if sub_data.get(indicator, False):
                pricing_traps.append(indicator)

        total = len(enrollment_traps) + len(retention_traps) + len(pricing_traps)

        return {
            'enrollment_traps': enrollment_traps,
            'retention_traps': retention_traps,
            'pricing_traps': pricing_traps,
            'total_trap_indicators': total,
            'risk_score': min(1.0, total * 0.15),
            'regulatory_concern': total >= 3,
            'ftc_risk': len(retention_traps) >= 2  # FTC focusing on cancellation difficulty
        }
```

---

### 4.8 AI-Specific Influence Detection

```python
class AIInfluenceType(Enum):
    LLM_PERSUASION = "llm_generated_persuasion"
    DEEPFAKE_VIDEO = "synthetic_video"
    DEEPFAKE_AUDIO = "voice_cloning"
    DEEPFAKE_IMAGE = "synthetic_image"
    AI_PERSONALIZATION = "algorithmic_targeting"
    CHATBOT_INFLUENCE = "conversational_ai_intensity"
    SYNTHETIC_SOCIAL_PROOF = "ai_generated_reviews"
    AUTOMATED_DISINFORMATION = "ai_disinformation_campaign"

@dataclass
class AIContentAnalysis:
    """Analysis of AI-generated content"""
    ai_generated_probability: float = 0.0
    influence_type: Optional[AIInfluenceType] = None
    authenticity_indicators: List[str] = field(default_factory=list)
    synthetic_markers: List[str] = field(default_factory=list)
    risk_level: str = "unknown"
    confidence: float = 0.0

class AIInfluenceDetector:
    """
    Detects AI-specific influence patterns.

    Research: LLMs increase persuasion by 81.7% (Nature 2025).
    AI-generated political ads as effective as human-written (Science 2025).
    """

    AI_TEXT_MARKERS = {
        'structural': [
            r'(?i)(in (conclusion|summary)|to (sum up|summarize|conclude))',
            r'(?i)(first(ly)?[\s,].*second(ly)?[\s,].*third(ly)?)',
            r'(?i)(it\'s (worth noting|important to note|crucial to understand))',
            r'(?i)(on the other hand|having said that|that being said)',
            r'(?i)(let me (explain|clarify|break (this|it) down))'
        ],
        'hedging': [
            r'(?i)(it\'s (important|worth|crucial) to (note|remember|consider|acknowledge))',
            r'(?i)(while (this|it|there) (may|might|could|is))',
            r'(?i)(however,?\s*(it\'s|it is|we should))',
            r'(?i)(I (should|must|need to) (note|mention|point out|clarify|emphasize))',
            r'(?i)((generally|typically|usually|often|frequently)\s+speaking)'
        ],
        'formulaic': [
            r'(?i)(here are \d+ (ways?|tips?|reasons?|steps?|strategies?))',
            r'(?i)(in today\'s (world|landscape|environment|digital age))',
            r'(?i)((delve|dive|venture) (into|deeper|further))',
            r'(?i)(the (landscape|realm|world) of)',
            r'(?i)(leverage|utilize|harness|optimize|streamline|synergize)'
        ]
    }

    BOT_CONVERSATION_SIGNATURES = {
        'response_patterns': [
            'always_available',                  # 24/7 instant response
            'consistent_response_time',          # No human variation
            'no_typos_or_corrections',           # Perfect text
            'formulaic_empathy',                 # "I understand how you feel"
            'context_amnesia',                   # Forgets previous conversation
            'no_personal_anecdotes'              # Never shares genuine experiences
        ],
        'persuasion_indicators': [
            'persistent_product_steering',        # Always returns to product
            'emotional_mirroring_without_depth',  # Surface empathy
            'personalization_from_data',          # Uses data user didn't share in convo
            'objection_handling_scripted',         # Pre-programmed objection responses
            'urgency_insertion'                   # Inserts time pressure
        ]
    }

    PERSONALIZATION_MARKERS = [
        r'(?i)(based on your (profile|preferences?|history|behavior|browsing|activity))',
        r'(?i)(personali[sz]ed|customiz|tailored)\s+(for|to)\s+you',
        r'(?i)(users?\s+like you|people (with your|in your|who share your))',
        r'(?i)(we (noticed|know|see|detected) (that )?you)',
        r'(?i)(your (unique|personal|individual|specific)\s+(needs?|preferences?|situation|profile))'
    ]

    def analyze_text_for_ai_generation(self, text: str) -> Dict:
        """Detect AI-generated text markers"""
        marker_counts = {}
        total_markers = 0

        for category, patterns in self.AI_TEXT_MARKERS.items():
            count = 0
            matches = []
            for pattern in patterns:
                found = re.findall(pattern, text)
                if found:
                    count += len(found)
                    matches.extend([f[0] if isinstance(f, tuple) else f for f in found])
            marker_counts[category] = {'count': count, 'matches': matches[:5]}
            total_markers += count

        # Calculate probability
        word_count = len(text.split())
        marker_density = total_markers / word_count if word_count > 0 else 0

        # Higher density of these markers = more likely AI
        ai_probability = min(0.95, marker_density * 10)

        # Check personalization
        personalization_matches = []
        for pattern in self.PERSONALIZATION_MARKERS:
            found = re.findall(pattern, text)
            if found:
                personalization_matches.extend([f[0] if isinstance(f, tuple) else f for f in found])

        return {
            'ai_generated_probability': round(ai_probability, 2),
            'marker_counts': marker_counts,
            'total_markers': total_markers,
            'marker_density': round(marker_density, 4),
            'synthetic_markers': list(marker_counts.keys()),
            'personalization_detected': len(personalization_matches) > 0,
            'personalization_instances': personalization_matches,
            'assessment': 'likely_ai' if ai_probability > 0.7 else 'possibly_ai' if ai_probability > 0.4 else 'likely_human'
        }

    def analyze_chatbot_interaction(self, messages: List[Dict]) -> Dict:
        """Analyze chatbot interaction for AI influence patterns"""
        bot_signals = 0
        persuasion_signals = 0

        for msg in messages:
            if msg.get('sender') == 'bot' or msg.get('sender') == 'agent':
                text = msg.get('text', '')

                # Check response patterns
                if msg.get('response_time_ms', 999999) < 500:
                    bot_signals += 1
                if not re.search(r'[a-z]\s[A-Z]', text):  # No mid-sentence caps (no typos)
                    bot_signals += 0.5

                # Check persuasion patterns
                for pattern in self.PERSONALIZATION_MARKERS:
                    if re.search(pattern, text):
                        persuasion_signals += 1

                # Check for persistent steering
                product_mentions = re.findall(r'(?i)(our (product|service|solution|platform|tool)|sign up|subscribe|purchase|buy now)', text)
                if product_mentions:
                    persuasion_signals += len(product_mentions) * 0.5

        return {
            'bot_probability': min(1.0, bot_signals / max(len(messages), 1)),
            'persuasion_intensity': min(1.0, persuasion_signals / max(len(messages), 1)),
            'ai_influence_risk': min(1.0, (bot_signals + persuasion_signals) / max(len(messages) * 2, 1))
        }


class DeepfakeDetector:
    """
    Detects deepfake indicators in video/audio content.

    Research basis: PMC 2025 survey, Deloitte 2025 report.
    Detection capped at 75% confidence due to evolving technology.
    """

    VIDEO_AUTHENTICITY_CHECKS = {
        'facial': [
            'blinking_irregularity',      # Deepfakes often have irregular blinks
            'lip_sync_mismatch',          # Audio-lip sync issues
            'skin_texture_uniformity',    # Too-smooth skin
            'eye_reflection_inconsistency',
            'facial_boundary_artifacts'
        ],
        'temporal': [
            'frame_inconsistency',        # Flickering between frames
            'lighting_direction_shift',   # Light source inconsistency
            'motion_blur_absence',        # Missing natural motion blur
            'temporal_coherence_break'
        ]
    }

    AUDIO_AUTHENTICITY_CHECKS = {
        'voice': [
            'pitch_stability_unnatural',   # Too stable pitch
            'breathing_pattern_absence',   # No natural breathing sounds
            'emotional_tone_flat',         # Limited emotional range
            'background_noise_inconsistency'
        ],
        'spectral': [
            'frequency_artifacts',         # Artifacts from generation
            'harmonic_irregularity',
            'room_acoustic_mismatch'
        ]
    }

    def assess_authenticity(self, media_analysis: Dict) -> Dict:
        """
        Assess media authenticity based on provided analysis features.

        Note: Confidence capped at 75% due to rapidly evolving generation technology.
        """
        video_flags = []
        audio_flags = []

        for check in self.VIDEO_AUTHENTICITY_CHECKS.get('facial', []):
            if media_analysis.get(f'video_{check}', False):
                video_flags.append(check)

        for check in self.VIDEO_AUTHENTICITY_CHECKS.get('temporal', []):
            if media_analysis.get(f'video_{check}', False):
                video_flags.append(check)

        for check in self.AUDIO_AUTHENTICITY_CHECKS.get('voice', []):
            if media_analysis.get(f'audio_{check}', False):
                audio_flags.append(check)

        for check in self.AUDIO_AUTHENTICITY_CHECKS.get('spectral', []):
            if media_analysis.get(f'audio_{check}', False):
                audio_flags.append(check)

        total_checks = (len(self.VIDEO_AUTHENTICITY_CHECKS.get('facial', [])) +
                       len(self.VIDEO_AUTHENTICITY_CHECKS.get('temporal', [])) +
                       len(self.AUDIO_AUTHENTICITY_CHECKS.get('voice', [])) +
                       len(self.AUDIO_AUTHENTICITY_CHECKS.get('spectral', [])))

        flag_count = len(video_flags) + len(audio_flags)
        raw_score = flag_count / total_checks if total_checks > 0 else 0

        # Cap at 75% — current detection limits
        capped_confidence = min(0.75, raw_score)

        return {
            'video_flags': video_flags,
            'audio_flags': audio_flags,
            'raw_authenticity_concern': round(raw_score, 2),
            'deepfake_probability': round(capped_confidence, 2),
            'confidence_cap': 0.75,
            'assessment': 'likely_deepfake' if capped_confidence > 0.5 else 'possible_deepfake' if capped_confidence > 0.25 else 'likely_authentic',
            'note': 'Detection confidence capped at 75% — deepfake technology evolves rapidly'
        }
```

---

### 4.9 Intervention Effectiveness Analysis

```python
class InterventionType(Enum):
    MEDIA_LITERACY = "media_literacy_education"
    FRICTION = "behavioral_friction"
    INOCULATION = "prebunking_inoculation"
    WARNING_LABEL = "content_warning"
    COOLING_OFF = "decision_delay"
    TRANSPARENCY = "disclosure_requirement"
    DESIGN_CHANGE = "intensity_reduction_design_modification"

@dataclass
class InterventionEffectiveness:
    """Measured effectiveness of an intervention"""
    intervention_type: InterventionType
    effect_size: float                        # Cohen's d or similar
    confidence_interval: Tuple[float, float]
    duration_of_effect: str                   # "immediate", "short-term", "long-term"
    decay_rate: float                         # How quickly effect diminishes
    population_moderators: List[str]
    implementation_cost: str                  # "low", "medium", "high"
    scalability: str                          # "low", "medium", "high"

class InterventionAnalyzer:
    """
    Evidence-based intervention effectiveness analysis.

    Based on meta-analyses and field experiments.
    """

    INTERVENTION_EVIDENCE = {
        'media_literacy_training': {
            'effect_size_d': 0.60,
            'source': 'Sage 2024 meta-analysis, N=81,155',
            'sustainability': 'moderate',
            'best_for': ['fake_news', 'advertising_awareness', 'propaganda'],
            'limitations': ['requires_time', 'may_not_transfer_to_new_contexts'],
            'decay_rate': 0.1  # per month
        },
        'inoculation': {
            'effect_size_d': 0.36,
            'source': 'Multiple RCTs, Compton & Pfau',
            'sustainability': 'good',
            'best_for': ['specific_manipulation_techniques', 'attitude_resistance'],
            'limitations': ['technique_specific', 'needs_booster'],
            'decay_rate': 0.05
        },
        'friction': {
            'effect_size_d': 0.45,
            'source': 'CHI 2025 design friction studies',
            'sustainability': 'high',
            'best_for': ['impulsive_purchases', 'sharing_misinformation', 'dark_patterns'],
            'limitations': ['can_frustrate_users', 'may_be_circumvented'],
            'decay_rate': 0.02
        },
        'warning_labels': {
            'effect_size_d': 0.20,
            'source': 'Multiple platform experiments',
            'sustainability': 'low',
            'best_for': ['misinformation', 'health_claims'],
            'limitations': ['habituation_effect', 'implied_truth_for_unlabeled'],
            'decay_rate': 0.15
        },
        'cooling_off_periods': {
            'effect_size_d': 0.55,
            'source': 'Consumer protection research',
            'sustainability': 'high',
            'best_for': ['high_value_purchases', 'subscription_enrollment', 'emotional_decisions'],
            'limitations': ['reduces_conversion', 'users_may_opt_out'],
            'decay_rate': 0.01
        },
        'social_norm_messaging': {
            'effect_size_d': 0.30,
            'source': 'Behavioral economics literature',
            'sustainability': 'moderate',
            'best_for': ['energy_use', 'health_behavior', 'financial_decisions'],
            'limitations': ['boomerang_effect_possible', 'requires_accurate_norms'],
            'decay_rate': 0.08
        },
        'deliberative_prompts': {
            'effect_size_d': 0.40,
            'source': 'Bago & Rand, Pennycook & Rand',
            'sustainability': 'moderate',
            'best_for': ['misinformation_sharing', 'impulsive_decisions'],
            'limitations': ['cognitive_load', 'may_reduce_engagement'],
            'decay_rate': 0.07
        }
    }

    def recommend_interventions(self, influence_analysis: Dict, user_profile: Dict = None) -> List[Dict]:
        """Recommend evidence-based interventions"""
        recommendations = []

        influence_types = influence_analysis.get('influence_types', [])
        risk_score = influence_analysis.get('overall_risk_score', 0)

        for intervention_name, evidence in self.INTERVENTION_EVIDENCE.items():
            # Check if intervention matches detected influence types
            relevance = 0
            for best_for in evidence['best_for']:
                for influence in influence_types:
                    if best_for in str(influence).lower() or str(influence).lower() in best_for:
                        relevance += 1

            if relevance > 0 or risk_score > 0.5:
                recommendations.append({
                    'intervention': intervention_name,
                    'effect_size': evidence['effect_size_d'],
                    'sustainability': evidence['sustainability'],
                    'relevance_score': min(1.0, relevance * 0.3 + risk_score * 0.2),
                    'limitations': evidence['limitations'],
                    'decay_rate_per_month': evidence['decay_rate']
                })

        # Sort by relevance then effect size
        recommendations.sort(key=lambda x: (x['relevance_score'], x['effect_size']), reverse=True)

        return recommendations[:5]  # Top 5 recommendations


class InterventionDecayTracker:
    """
    Tracks intervention effectiveness decay over time.

    Interventions lose effectiveness; this models expected decay
    and recommends booster timing.
    """

    def project_decay(self, intervention_name: str, months_since: int) -> Dict:
        """Project intervention effectiveness decay"""
        evidence = InterventionAnalyzer.INTERVENTION_EVIDENCE.get(intervention_name)
        if not evidence:
            return {'error': f'Unknown intervention: {intervention_name}'}

        initial_d = evidence['effect_size_d']
        decay_rate = evidence['decay_rate']

        # Exponential decay model
        import math
        current_d = initial_d * math.exp(-decay_rate * months_since)

        # Minimum effective threshold
        min_effective_d = 0.2

        months_to_ineffective = -math.log(min_effective_d / initial_d) / decay_rate if decay_rate > 0 else float('inf')

        return {
            'intervention': intervention_name,
            'initial_effect_size': initial_d,
            'current_effect_size': round(current_d, 3),
            'months_since_intervention': months_since,
            'still_effective': current_d >= min_effective_d,
            'months_until_ineffective': round(months_to_ineffective, 1),
            'booster_recommended': current_d < initial_d * 0.5,
            'booster_urgency': 'immediate' if current_d < min_effective_d else 'soon' if current_d < initial_d * 0.5 else 'not_needed'
        }
```

---

### 4.10 Regulatory Compliance Mapping

```python
class Jurisdiction(Enum):
    US_FEDERAL = "us_federal"
    US_CALIFORNIA = "us_california"
    EU = "european_union"
    UK = "united_kingdom"
    GERMANY = "germany"
    CANADA = "canada"
    AUSTRALIA = "australia"

class RegulationType(Enum):
    DARK_PATTERN_PROHIBITION = "dark_pattern"
    DECEPTIVE_ADVERTISING = "deceptive_advertising"
    SUBSCRIPTION_PRACTICES = "subscription_regulation"
    CHILD_PROTECTION = "children_online_protection"
    AI_REGULATION = "ai_specific"
    PRIVACY_DESIGN = "privacy_by_design"

@dataclass
class RegulatoryViolation:
    """Identified regulatory violation"""
    jurisdiction: Jurisdiction
    regulation_type: RegulationType
    specific_law: str
    violation_description: str
    severity: str                    # "minor", "moderate", "severe"
    enforcement_likelihood: float
    potential_penalty: str
    remediation_steps: List[str]
```

**Regulatory Database:**

| Jurisdiction | Regulation | Prohibits | Enforcement | Penalties |
|---|---|---|---|---|
| US Federal | FTC Act Section 5 | Deceptive & unfair practices | Active — multiple 2024 cases | Civil penalties, injunctions, refunds |
| US Federal | ROSCA | Negative option without consent, hidden terms | Active — Amazon case 2024 ($2.5B) | Up to $50,000+ per violation |
| California | CCPA/CPRA | Dark patterns in consent, deceptive design | Active | $2,500-$7,500 per violation |
| EU | Digital Services Act | Cancellation harder than signup, dark patterns, manipulative design | Active since Feb 2024 | Up to 6% global turnover |
| EU | AI Act | Subliminal influence, exploitation of vulnerabilities, social scoring | Phased implementation | Up to 7% global turnover (prohibited practices) |
| EU | GDPR | Deceptive consent, dark patterns in privacy | Active | Up to 4% global turnover or EUR 20 million |
| Germany | Fair Consumer Contracts Act | No termination button | Active | Varies |

**Influence-to-Regulation Mapping:**

| Influence Type | Applicable Regulations |
|---|---|
| Roach motel | EU DSA, FTC Section 5, Germany Fair Contracts Act |
| Confirmshaming | FTC Section 5, EU DSA |
| Fake urgency | FTC Section 5, EU DSA |
| Hidden costs | ROSCA, CCPA |
| Dark pattern consent | GDPR, CCPA |
| Subliminal influence | EU AI Act |
| Child-targeted influence | FTC/COPPA, EU DSA |
| Deepfake fraud | FTC Section 5, multiple state laws |

```python
class RegulatoryComplianceAnalyzer:
    """
    Maps detected influence to regulatory violations.

    Research basis: FTC enforcement actions 2024, EU DSA requirements,
    State privacy law requirements.
    """

    REGULATION_DATABASE = {
        Jurisdiction.US_FEDERAL: {
            'ftc_section_5': {
                'name': 'FTC Act Section 5',
                'prohibits': ['deceptive_practices', 'unfair_practices'],
                'enforcement': 'Active - multiple 2024 cases',
                'penalties': 'Civil penalties, injunctions, refunds'
            },
            'rosca': {
                'name': 'Restore Online Shoppers Confidence Act',
                'prohibits': ['negative_option_without_consent', 'hidden_terms'],
                'enforcement': 'Active - Amazon case 2024',
                'penalties': 'Civil penalties up to $50,000+ per violation'
            }
        },
        Jurisdiction.US_CALIFORNIA: {
            'ccpa_cpra': {
                'name': 'California Consumer Privacy Act / CPRA',
                'prohibits': ['dark_patterns_in_consent', 'deceptive_design'],
                'enforcement': 'Active',
                'penalties': '$2,500-$7,500 per violation'
            }
        },
        Jurisdiction.EU: {
            'dsa': {
                'name': 'Digital Services Act',
                'prohibits': ['cancellation_harder_than_signup', 'dark_patterns', 'manipulative_design'],
                'enforcement': 'Active since Feb 2024',
                'penalties': 'Up to 6% global turnover'
            },
            'ai_act': {
                'name': 'EU AI Act',
                'prohibits': ['subliminal_influence', 'exploitation_of_vulnerabilities', 'social_scoring'],
                'enforcement': 'Phased implementation',
                'penalties': 'Up to 7% global turnover for prohibited practices'
            },
            'gdpr': {
                'name': 'General Data Protection Regulation',
                'prohibits': ['deceptive_consent', 'dark_patterns_in_privacy'],
                'enforcement': 'Active',
                'penalties': 'Up to 4% global turnover or EUR 20 million'
            }
        },
        Jurisdiction.GERMANY: {
            'fair_contracts_act': {
                'name': 'Fair Consumer Contracts Act',
                'prohibits': ['no_termination_button'],
                'enforcement': 'Active',
                'penalties': 'Varies'
            }
        }
    }

    INFLUENCE_TO_REGULATION = {
        'roach_motel': [
            (Jurisdiction.EU, 'dsa'),
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.GERMANY, 'fair_contracts_act')
        ],
        'confirmshaming': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.EU, 'dsa')
        ],
        'fake_urgency': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.EU, 'dsa')
        ],
        'hidden_costs': [
            (Jurisdiction.US_FEDERAL, 'rosca'),
            (Jurisdiction.US_CALIFORNIA, 'ccpa_cpra')
        ],
        'dark_pattern_consent': [
            (Jurisdiction.EU, 'gdpr'),
            (Jurisdiction.US_CALIFORNIA, 'ccpa_cpra')
        ],
        'subliminal_influence': [
            (Jurisdiction.EU, 'ai_act')
        ],
        'child_targeted_influence': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.EU, 'dsa')
        ],
        'deepfake_fraud': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5')
        ]
    }

    REMEDIATION_STEPS = {
        'roach_motel': [
            'Make cancellation process equal in steps to signup',
            'Provide clear online cancellation option',
            'Add termination button (required in Germany)',
            'Remove unnecessary friction from cancellation'
        ],
        'fake_urgency': [
            'Remove countdown timers that reset',
            'Ensure scarcity claims are accurate and verifiable',
            'Add disclosure for limited-time offers'
        ],
        'confirmshaming': [
            'Use neutral language for decline options',
            'Remove guilt-inducing decline buttons',
            'Provide equal visual weight to all options'
        ],
        'hidden_costs': [
            'Display full price including all fees upfront',
            'Itemize additional charges clearly',
            'Obtain affirmative consent for each charge'
        ],
        'dark_pattern_consent': [
            'Implement clear, specific consent requests',
            'Avoid pre-checked boxes',
            'Make rejection as easy as acceptance'
        ]
    }

    def analyze_compliance(self, influence_analysis: Dict,
                          operating_jurisdictions: List[Jurisdiction] = None) -> List[RegulatoryViolation]:
        """Analyze detected influence for regulatory compliance"""
        violations = []

        if operating_jurisdictions is None:
            operating_jurisdictions = list(Jurisdiction)

        influence_types = influence_analysis.get('influence_types', [])

        for manip_type in influence_types:
            manip_key = str(manip_type).lower().replace(' ', '_')

            for key, regulations in self.INFLUENCE_TO_REGULATION.items():
                if key in manip_key or manip_key in key:
                    for jurisdiction, reg_id in regulations:
                        if jurisdiction in operating_jurisdictions:
                            reg_info = self.REGULATION_DATABASE.get(jurisdiction, {}).get(reg_id, {})
                            if reg_info:
                                severity = self._assess_severity(influence_analysis, manip_type)
                                violation = RegulatoryViolation(
                                    jurisdiction=jurisdiction,
                                    regulation_type=self._get_regulation_type(reg_id),
                                    specific_law=reg_info.get('name', reg_id),
                                    violation_description=f"Detected {manip_type} may violate {reg_info.get('name')}",
                                    severity=severity,
                                    enforcement_likelihood=self._assess_enforcement(jurisdiction, reg_id),
                                    potential_penalty=reg_info.get('penalties', 'Unknown'),
                                    remediation_steps=self.REMEDIATION_STEPS.get(key, ['Review and modify design'])
                                )
                                violations.append(violation)

        return violations

    def _get_regulation_type(self, reg_id: str) -> RegulationType:
        mapping = {
            'ftc_section_5': RegulationType.DECEPTIVE_ADVERTISING,
            'rosca': RegulationType.SUBSCRIPTION_PRACTICES,
            'ccpa_cpra': RegulationType.PRIVACY_DESIGN,
            'dsa': RegulationType.DARK_PATTERN_PROHIBITION,
            'ai_act': RegulationType.AI_REGULATION,
            'gdpr': RegulationType.PRIVACY_DESIGN,
            'fair_contracts_act': RegulationType.SUBSCRIPTION_PRACTICES
        }
        return mapping.get(reg_id, RegulationType.DARK_PATTERN_PROHIBITION)

    def _assess_severity(self, analysis: Dict, manip_type: str) -> str:
        risk_score = analysis.get('overall_risk_score', 0)
        if 'child' in str(manip_type).lower():
            return 'severe'
        elif risk_score > 0.7:
            return 'severe'
        elif risk_score > 0.4:
            return 'moderate'
        return 'minor'

    def _assess_enforcement(self, jurisdiction: Jurisdiction, reg_id: str) -> float:
        high_enforcement = [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.US_FEDERAL, 'rosca'),
            (Jurisdiction.EU, 'dsa'),
            (Jurisdiction.EU, 'gdpr')
        ]
        return 0.7 if (jurisdiction, reg_id) in high_enforcement else 0.4

    def generate_compliance_report(self, violations: List[RegulatoryViolation]) -> Dict:
        """Generate comprehensive compliance report"""
        report = {
            'total_violations': len(violations),
            'by_jurisdiction': {},
            'by_severity': {'severe': 0, 'moderate': 0, 'minor': 0},
            'high_priority_remediations': [],
            'estimated_risk_exposure': 'Low'
        }

        for violation in violations:
            jur = violation.jurisdiction.value
            report['by_jurisdiction'][jur] = report['by_jurisdiction'].get(jur, 0) + 1
            report['by_severity'][violation.severity] += 1
            if violation.severity == 'severe':
                report['high_priority_remediations'].extend(violation.remediation_steps)

        if report['by_severity']['severe'] > 0:
            report['estimated_risk_exposure'] = 'High'
        elif report['by_severity']['moderate'] > 2:
            report['estimated_risk_exposure'] = 'Medium'

        report['high_priority_remediations'] = list(set(report['high_priority_remediations']))

        return report
```

## PART 5: HIGH-IMPACT DETECTION SYSTEMS (9 Specialized Detectors) {#part-5}

### 5.1 Synergistic Stacking Detector

Detects when multiple persuasion techniques are combined for amplified effect. Research shows technique combinations produce multiplicative (not additive) effects.

```python
class SynergisticStackingDetector:
    """
    Detects synergistic combinations of persuasion techniques.

    Research basis: Combinations produce multiplicative effects.
    15 known high-impact synergies ranked by effectiveness.
    """

    KNOWN_SYNERGIES = {
        'scarcity_social_proof': {
            'techniques': ['scarcity', 'social_proof'],
            'multiplier': 1.8,
            'mechanism': 'Limited availability + others wanting it = amplified urgency',
            'example': '"Only 3 left — 47 people viewing this right now"'
        },
        'authority_reciprocity': {
            'techniques': ['authority', 'reciprocity'],
            'multiplier': 1.6,
            'mechanism': 'Expert gives free advice → obligation to follow recommendation',
            'example': '"Dr. Smith recommends... and here\'s a free consultation"'
        },
        'commitment_consistency': {
            'techniques': ['commitment', 'consistency'],
            'multiplier': 1.7,
            'mechanism': 'Small agreement → larger request aligned with identity',
            'example': '"You said you value health → this premium plan aligns with that"'
        },
        'fear_relief_product': {
            'techniques': ['emotional_fear', 'emotional_relief', 'product_placement'],
            'multiplier': 1.75,
            'mechanism': 'Create fear → offer relief through product',
            'example': '"Your data is at risk! ...But our security suite protects you"'
        },
        'anchoring_decoy_scarcity': {
            'techniques': ['anchoring', 'decoy', 'scarcity'],
            'multiplier': 1.65,
            'mechanism': 'High anchor + decoy option + time pressure',
            'example': '"Was $999 → $497 (vs $399 basic) — offer ends tonight"'
        },
        'social_proof_authority_urgency': {
            'techniques': ['social_proof', 'authority', 'urgency'],
            'multiplier': 1.7,
            'mechanism': 'Others trust it + experts endorse it + act now',
            'example': '"10,000 doctors recommend — join them before enrollment closes"'
        },
        'reciprocity_commitment_escalation': {
            'techniques': ['reciprocity', 'commitment', 'escalation'],
            'multiplier': 1.55,
            'mechanism': 'Free value → small commitment → larger ask',
            'example': '"Free ebook → email signup → webinar → course purchase"'
        },
        'identity_exclusivity_belonging': {
            'techniques': ['identity', 'exclusivity', 'belonging'],
            'multiplier': 1.5,
            'mechanism': 'You\'re special + exclusive access + join your tribe',
            'example': '"For serious professionals only — join the inner circle"'
        },
        'pain_agitation_solution': {
            'techniques': ['pain_point', 'agitation', 'solution'],
            'multiplier': 1.6,
            'mechanism': 'Identify pain → amplify → present solution',
            'example': '"Losing customers? It\'s costing you $X daily. Here\'s how to fix it"'
        },
        'fractionation_commercial': {
            'techniques': ['emotional_cycling', 'commercial_relief'],
            'multiplier': 1.8,
            'mechanism': 'Emotional cycling reduces critical thinking → product as relief',
            'example': 'Fear content → joy content → fear → product advertisement'
        },
        'gamification_sunk_cost': {
            'techniques': ['gamification', 'sunk_cost'],
            'multiplier': 1.45,
            'mechanism': 'Accumulated points/streaks → can\'t leave without losing them',
            'example': '"You have 47,000 points! Don\'t lose them by cancelling"'
        },
        'personalization_vulnerability': {
            'techniques': ['personalization', 'vulnerability_timing'],
            'multiplier': 1.7,
            'mechanism': 'Personalized content delivered at vulnerable moments',
            'example': 'Late-night targeted ad based on browsing behavior'
        },
        'social_comparison_shame': {
            'techniques': ['social_comparison', 'shame'],
            'multiplier': 1.5,
            'mechanism': 'Compare to successful peers → shame gap → product bridges gap',
            'example': '"Your competitors are already using this — are you falling behind?"'
        },
        'curiosity_gap_clickbait': {
            'techniques': ['curiosity_gap', 'information_asymmetry'],
            'multiplier': 1.35,
            'mechanism': 'Create information gap → withhold resolution → require action',
            'example': '"The one thing successful people do that you don\'t..."'
        },
        'default_friction_dark': {
            'techniques': ['default_bias', 'friction_asymmetry'],
            'multiplier': 1.4,
            'mechanism': 'Desired action = easy default; alternative = high friction',
            'example': 'Pre-checked premium plan, cancel requires phone call'
        }
    }

    TECHNIQUE_PATTERNS = {
        'scarcity': {
            'text': [r'(?i)(only \d+ left|limited|running out|last chance|while supplies last)'],
            'ui': ['countdown_timer', 'stock_counter', 'urgency_banner']
        },
        'social_proof': {
            'text': [r'(?i)(\d+ (people|users|customers)|trusted by|as seen|rated|reviews?)'],
            'ui': ['review_widget', 'user_count', 'testimonial_carousel']
        },
        'authority': {
            'text': [r'(?i)(expert|doctor|study|research|certified|award|endorsed)'],
            'ui': ['badge_display', 'credential_section', 'media_logos']
        },
        'reciprocity': {
            'text': [r'(?i)(free|gift|bonus|complimentary|no charge|on us)'],
            'ui': ['free_trial_button', 'gift_icon', 'bonus_badge']
        },
        'commitment': {
            'text': [r'(?i)(you already|since you|don\'t stop now|you\'ve come)'],
            'ui': ['progress_bar', 'step_indicator', 'streak_display']
        },
        'emotional_fear': {
            'text': [r'(?i)(danger|risk|threat|warning|protect|afraid|worried|vulnerable)'],
            'ui': ['warning_icon', 'red_alert', 'danger_banner']
        },
        'emotional_relief': {
            'text': [r'(?i)(safe|secure|protected|peace of mind|finally|solution|relief)'],
            'ui': ['checkmark', 'shield_icon', 'green_indicator']
        },
        'anchoring': {
            'text': [r'(?i)(was \$|originally|save \$|value of|\$[\d,]+\s*value)'],
            'ui': ['strikethrough_price', 'comparison_table', 'savings_badge']
        },
        'identity': {
            'text': [r'(?i)(you\'re the type|as a (serious|smart)|for (leaders|experts|professionals))'],
            'ui': ['persona_selection', 'role_badge']
        },
        'pain_point': {
            'text': [r'(?i)(tired of|frustrated|struggling|losing|wasting|stuck)'],
            'ui': ['problem_illustration', 'pain_stat']
        },
        'curiosity_gap': {
            'text': [r'(?i)(the (one|secret|surprising|shocking)|you won\'t believe|what they don\'t)'],
            'ui': ['blurred_content', 'locked_section', 'reveal_button']
        },
        'gamification': {
            'text': [r'(?i)(points|level|badge|streak|reward|achievement|leaderboard|rank)'],
            'ui': ['point_counter', 'level_bar', 'achievement_popup']
        },
        'sunk_cost': {
            'text': [r'(?i)(you\'ve (invested|earned|built|accumulated)|don\'t (lose|waste)|your \d+ (points|days))'],
            'ui': ['investment_summary', 'loss_preview']
        },
        'default_bias': {
            'text': [r'(?i)(recommended|most popular|best value|pre-selected)'],
            'ui': ['pre_checked', 'highlighted_option', 'default_selected']
        }
    }

    def detect_stacking(self, text: str, ui_elements: List[str] = None) -> Dict:
        """Detect synergistic technique stacking"""
        # Detect active techniques
        active_techniques = {}
        for technique, config in self.TECHNIQUE_PATTERNS.items():
            text_matches = []
            for pattern in config['text']:
                found = re.findall(pattern, text)
                if found:
                    text_matches.extend([f[0] if isinstance(f, tuple) else f for f in found])

            ui_matches = []
            if ui_elements:
                for ui_indicator in config.get('ui', []):
                    if ui_indicator in ui_elements:
                        ui_matches.append(ui_indicator)

            if text_matches or ui_matches:
                active_techniques[technique] = {
                    'text_evidence': text_matches,
                    'ui_evidence': ui_matches,
                    'confidence': min(1.0, len(text_matches) * 0.2 + len(ui_matches) * 0.3)
                }

        # Check for known synergies
        detected_synergies = []
        for synergy_name, synergy_data in self.KNOWN_SYNERGIES.items():
            required = synergy_data['techniques']
            matched = [t for t in required if t in active_techniques or
                      any(t in at for at in active_techniques)]

            if len(matched) >= len(required) * 0.7:  # 70% match threshold
                detected_synergies.append({
                    'synergy': synergy_name,
                    'multiplier': synergy_data['multiplier'],
                    'mechanism': synergy_data['mechanism'],
                    'matched_techniques': matched,
                    'match_ratio': len(matched) / len(required)
                })

        # Calculate combined effect
        if detected_synergies:
            max_multiplier = max(s['multiplier'] for s in detected_synergies)
            combined_multiplier = 1.0
            for s in detected_synergies:
                combined_multiplier *= (1 + (s['multiplier'] - 1) * 0.5)  # Diminishing returns
        else:
            max_multiplier = 1.0
            combined_multiplier = 1.0

        return {
            'active_techniques': list(active_techniques.keys()),
            'technique_count': len(active_techniques),
            'detected_synergies': detected_synergies,
            'synergy_count': len(detected_synergies),
            'max_single_multiplier': max_multiplier,
            'combined_multiplier': round(combined_multiplier, 2),
            'risk_score': min(1.0, len(detected_synergies) * 0.2 + (combined_multiplier - 1) * 0.5),
            'technique_details': active_techniques
        }
```

---

### 5.2 Vulnerability Timing Detector

```python
class VulnerabilityTimingDetector:
    """
    Detects exploitation of temporal vulnerability windows.

    Research: Decision quality varies with time of day, emotional state,
    and cognitive depletion.
    """

    CIRCADIAN_VULNERABILITY = {
        'early_morning': {
            'hours': (5, 7),
            'vulnerability': 'moderate',
            'factor': 'cortisol_spike',
            'description': 'Cortisol awakening response — heightened anxiety, reactive decisions'
        },
        'mid_morning': {
            'hours': (9, 11),
            'vulnerability': 'low',
            'factor': 'peak_cognition',
            'description': 'Peak cognitive function — best analytical processing'
        },
        'post_lunch': {
            'hours': (13, 15),
            'vulnerability': 'moderate',
            'factor': 'postprandial_dip',
            'description': 'Post-meal cognitive dip — reduced analytical capacity'
        },
        'late_afternoon': {
            'hours': (16, 18),
            'vulnerability': 'moderate',
            'factor': 'decision_fatigue_accumulation',
            'description': 'Accumulated decision fatigue — defaults more attractive'
        },
        'evening': {
            'hours': (20, 22),
            'vulnerability': 'high',
            'factor': 'ego_depletion',
            'description': 'Ego depletion + relaxation — reduced self-control'
        },
        'late_night': {
            'hours': (23, 4),
            'vulnerability': 'very_high',
            'factor': 'circadian_low',
            'description': 'Circadian low point — impaired judgment, emotional reactivity'
        }
    }

    DECISION_FATIGUE_THRESHOLDS = {
        'decisions_today': {
            5: 'baseline',
            15: 'mild_fatigue',        # ~10% quality reduction
            25: 'moderate_fatigue',    # ~25% quality reduction
            40: 'severe_fatigue',      # ~40% quality reduction
            60: 'critical_fatigue'     # ~60% quality reduction
        },
        'quality_reduction_per_10_decisions': 0.08  # 8% per 10 decisions
    }

    EMOTIONAL_VULNERABILITY_SIGNALS = [
        r'(?i)(just (lost|broke up|got fired|received bad news|diagnosed))',
        r'(?i)(feeling (down|sad|angry|lonely|overwhelmed|stressed|anxious))',
        r'(?i)(can\'t (sleep|stop thinking|cope|handle))',
        r'(?i)(need (help|comfort|support|relief|escape))'
    ]

    VULNERABLE_DAYS = {
        'post_payday': {'day_offset': (0, 3), 'vulnerability': 'spending_impulse'},
        'friday_evening': {'vulnerability': 'reward_seeking'},
        'sunday_evening': {'vulnerability': 'anxiety_anticipation'},
        'month_end': {'day_offset': (28, 31), 'vulnerability': 'financial_stress'},
        'holidays': {'vulnerability': 'loneliness_or_social_pressure'}
    }

    def assess_timing_vulnerability(self, timestamp: Dict, user_context: Dict = None) -> Dict:
        """
        Assess vulnerability based on timing context.

        Args:
            timestamp: Dict with 'hour', 'day_of_week', 'day_of_month'
            user_context: Optional dict with 'decisions_today', 'emotional_signals',
                         'recent_events'
        """
        hour = timestamp.get('hour', 12)
        day_of_week = timestamp.get('day_of_week', 'monday')
        day_of_month = timestamp.get('day_of_month', 15)

        vulnerabilities = []
        risk_score = 0.0

        # Circadian check
        for window_name, window in self.CIRCADIAN_VULNERABILITY.items():
            h_start, h_end = window['hours']
            if h_start <= hour <= h_end or (h_start > h_end and (hour >= h_start or hour <= h_end)):
                vulnerabilities.append({
                    'type': 'circadian',
                    'window': window_name,
                    'vulnerability': window['vulnerability'],
                    'factor': window['factor'],
                    'description': window['description']
                })
                risk_addition = {'low': 0.1, 'moderate': 0.2, 'high': 0.3, 'very_high': 0.4}
                risk_score += risk_addition.get(window['vulnerability'], 0)

        # Decision fatigue
        if user_context:
            decisions = user_context.get('decisions_today', 0)
            fatigue_reduction = decisions * self.DECISION_FATIGUE_THRESHOLDS['quality_reduction_per_10_decisions'] / 10
            if fatigue_reduction > 0.1:
                vulnerabilities.append({
                    'type': 'decision_fatigue',
                    'decisions_today': decisions,
                    'estimated_quality_reduction': f"{fatigue_reduction * 100:.0f}%"
                })
                risk_score += min(0.3, fatigue_reduction)

            # Emotional signals
            emotional_text = user_context.get('emotional_signals', '')
            if emotional_text:
                for pattern in self.EMOTIONAL_VULNERABILITY_SIGNALS:
                    if re.search(pattern, emotional_text):
                        vulnerabilities.append({
                            'type': 'emotional_vulnerability',
                            'signal': emotional_text[:100]
                        })
                        risk_score += 0.3
                        break

        # Day-based vulnerability
        if day_of_week.lower() == 'friday' and hour >= 17:
            vulnerabilities.append({'type': 'temporal', 'window': 'friday_evening'})
            risk_score += 0.1
        if day_of_week.lower() == 'sunday' and hour >= 18:
            vulnerabilities.append({'type': 'temporal', 'window': 'sunday_evening'})
            risk_score += 0.1
        if day_of_month <= 3:
            vulnerabilities.append({'type': 'temporal', 'window': 'post_payday'})
            risk_score += 0.15

        return {
            'vulnerabilities': vulnerabilities,
            'vulnerability_count': len(vulnerabilities),
            'risk_score': min(1.0, risk_score),
            'recommendation': self._recommend_action(risk_score)
        }

    def _recommend_action(self, risk_score: float) -> str:
        if risk_score > 0.6:
            return 'DELAY_DECISION: High vulnerability — implement cooling-off period'
        elif risk_score > 0.3:
            return 'CAUTION: Moderate vulnerability — add friction before irreversible actions'
        return 'STANDARD: Normal vulnerability level'
```

---

### 5.3 Trust Leverage Sequence Detector

```python
class TrustLeverageSequenceDetector:
    """
    Detects structured trust-building sequences designed
    to exploit trust for persuasion.

    8 stages of trust leverage identified.
    """

    class TrustStage(Enum):
        INITIAL_CONTACT = "initial_contact"
        VALUE_DELIVERY = "value_delivery"
        RAPPORT_BUILDING = "rapport_building"
        VULNERABILITY_EXCHANGE = "vulnerability_exchange"
        COMMITMENT_SECURING = "commitment_securing"
        TRUST_TESTING = "trust_testing"
        LEVERAGE_APPLICATION = "leverage_application"
        LOCK_IN = "lock_in"

    STAGE_PATTERNS = {
        'initial_contact': [
            r'(?i)(nice to meet|great to connect|I\'ve been following|I admire)',
            r'(?i)(reaching out because|wanted to connect|saw your (post|profile|work))'
        ],
        'value_delivery': [
            r'(?i)(here\'s (something|a resource|a tip)|thought you\'d (find|appreciate)|free (guide|resource))',
            r'(?i)(no strings|just wanted to share|hope this helps)'
        ],
        'rapport_building': [
            r'(?i)(we have (so much|a lot) in common|I (totally|completely) (get|understand))',
            r'(?i)(same here|me too|I feel the same|great minds)'
        ],
        'vulnerability_exchange': [
            r'(?i)(I\'ll be honest|between you and me|I don\'t usually share)',
            r'(?i)(can I be (real|honest|vulnerable)|I trust you (enough|with))'
        ],
        'commitment_securing': [
            r'(?i)(would you be (open|willing)|can I (count on|rely on) you)',
            r'(?i)(let\'s (commit|agree|promise)|I need your (word|commitment))'
        ],
        'trust_testing': [
            r'(?i)(small favor|quick ask|one thing|can you (just|do me))',
            r'(?i)(prove|show me|demonstrate (your|that you))'
        ],
        'leverage_application': [
            r'(?i)(since we (agreed|talked|committed)|you (said|promised|agreed))',
            r'(?i)(remember when|based on our (relationship|trust|agreement))'
        ],
        'lock_in': [
            r'(?i)(you can\'t (leave|stop|quit) now|too (late|far|much invested))',
            r'(?i)(after (everything|all) we\'ve (built|shared)|don\'t throw (this|it) away)'
        ]
    }

    RED_FLAGS = {
        'too_fast_progression': 'Moving through trust stages unusually quickly',
        'asymmetric_vulnerability': 'One party shares much more than the other',
        'premature_commitment_request': 'Asking for commitment before trust is established',
        'isolation_from_others': 'Discouraging consultation with others',
        'urgency_at_leverage': 'Adding time pressure when applying leverage',
        'guilt_at_resistance': 'Using guilt when requests are questioned'
    }

    def analyze_sequence(self, messages: List[Dict]) -> Dict:
        """Analyze message sequence for trust leverage patterns"""
        stage_timeline = []

        for i, msg in enumerate(messages):
            text = msg.get('text', '')
            detected_stages = []

            for stage, patterns in self.STAGE_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, text):
                        detected_stages.append(stage)
                        break

            if detected_stages:
                stage_timeline.append({
                    'message_index': i,
                    'sender': msg.get('sender', 'unknown'),
                    'stages': detected_stages
                })

        # Analyze progression
        all_stages = [s for entry in stage_timeline for s in entry['stages']]
        stage_order = list(self.STAGE_PATTERNS.keys())
        progression_score = self._calculate_progression(all_stages, stage_order)

        # Check red flags
        red_flags = self._check_red_flags(stage_timeline, messages)

        # Risk calculation
        risk = min(1.0, progression_score * 0.4 + len(red_flags) * 0.15 + len(set(all_stages)) * 0.05)

        # Prediction
        prediction = self._predict_next_move(all_stages, stage_order)

        return {
            'stages_detected': list(set(all_stages)),
            'stage_count': len(set(all_stages)),
            'timeline': stage_timeline,
            'progression_score': round(progression_score, 2),
            'red_flags': red_flags,
            'risk_score': round(risk, 2),
            'predicted_next': prediction,
            'assessment': 'trust_leverage_detected' if risk > 0.5 else 'monitoring' if risk > 0.2 else 'normal'
        }

    def _calculate_progression(self, stages: List[str], stage_order: List[str]) -> float:
        """Calculate how closely stages follow the expected progression"""
        if len(stages) < 2:
            return 0.0

        indices = [stage_order.index(s) for s in stages if s in stage_order]
        if len(indices) < 2:
            return 0.0

        # Check if indices are generally increasing
        increasing = sum(1 for i in range(len(indices)-1) if indices[i+1] >= indices[i])
        return increasing / (len(indices) - 1)

    def _check_red_flags(self, timeline: List[Dict], messages: List[Dict]) -> List[str]:
        """Check for trust leverage red flags"""
        flags = []

        if len(timeline) >= 4:
            # Check speed of progression
            if timeline[-1]['message_index'] - timeline[0]['message_index'] < 10:
                flags.append(self.RED_FLAGS['too_fast_progression'])

        # Check for isolation language
        for msg in messages:
            text = msg.get('text', '')
            if re.search(r'(?i)(don\'t (tell|listen to|trust) (them|others|anyone))', text):
                flags.append(self.RED_FLAGS['isolation_from_others'])
            if re.search(r'(?i)(you (owe|promised|committed|agreed).*?(now|immediately|right away))', text):
                flags.append(self.RED_FLAGS['urgency_at_leverage'])

        return list(set(flags))

    def _predict_next_move(self, stages: List[str], stage_order: List[str]) -> str:
        """Predict next stage based on current progression"""
        if not stages:
            return 'initial_contact'

        last_stage = stages[-1]
        if last_stage in stage_order:
            idx = stage_order.index(last_stage)
            if idx + 1 < len(stage_order):
                return stage_order[idx + 1]
        return 'lock_in'
```

---

### 5.4 Physiological Bypassing Detector

```python
class PhysiologicalBypassDetector:
    """
    Detects techniques that bypass conscious processing
    through physiological mechanisms.

    5 bypass mechanisms identified with countermeasures.
    """

    class BypassMechanism(Enum):
        RAPID_CUT = "rapid_cut_overwhelm"
        ASMR_RELAXATION = "asmr_relaxation_bypass"
        EMOTIONAL_AROUSAL = "emotional_arousal_bypass"
        COGNITIVE_OVERLOAD = "cognitive_overload_bypass"
        RHYTHMIC_ENTRAINMENT = "rhythmic_entrainment"
        SUBLIMINAL_PRIMING = "subliminal_priming"
        SENSORY_OVERWHELM = "sensory_overwhelm"

    ASMR_TRIGGERS = [
        r'(?i)(whisper|soft[- ]?spoken|gentle (voice|tone|sounds?))',
        r'(?i)(tapping|scratching|brushing|crinkling)',
        r'(?i)(personal attention|close[- ]up|ear to ear)',
        r'(?i)(relaxing|calming|soothing|peaceful|tingles?)'
    ]

    AROUSAL_WORDS = {
        'high_arousal_negative': [
            r'(?i)(terrif|horrif|shock|outrage|fury|rage|panic|crisis|catastroph|devastating)',
        ],
        'high_arousal_positive': [
            r'(?i)(ecsta|thrilling|exhilarat|euphori|incredible|amazing|mind[- ]blow)',
        ],
        'low_arousal_relaxation': [
            r'(?i)(calm|relax|sooth|peace|tranquil|serene|gentle|soft|warm|comfort)',
        ]
    }

    OVERLOAD_INDICATORS = [
        r'(?i)(but wait|and that\'s not all|plus|also|additionally|moreover|furthermore|on top of)',
        r'(?i)(not only.*but also|in addition|what\'s more|even better)',
    ]

    BYPASS_THRESHOLDS = {
        'rapid_cut': {'cuts_per_minute': 30, 'risk': 'Reduces analytical processing time'},
        'asmr': {'trigger_density': 3, 'risk': 'Induces parasympathetic state reducing critical evaluation'},
        'arousal': {'arousal_word_density': 0.05, 'risk': 'Emotional flooding bypasses rational assessment'},
        'overload': {'info_units_per_paragraph': 5, 'risk': 'Exceeds working memory → defaults accepted'},
        'rhythm': {'beat_regularity': 0.9, 'risk': 'Entrains neural oscillations reducing independent thought'}
    }

    def analyze_content(self, text: str, media_features: Dict = None) -> Dict:
        """Analyze content for physiological bypass mechanisms"""
        findings = {}

        # ASMR detection
        asmr_matches = []
        for pattern in self.ASMR_TRIGGERS:
            found = re.findall(pattern, text)
            if found:
                asmr_matches.extend([f[0] if isinstance(f, tuple) else f for f in found])
        if asmr_matches:
            findings['asmr_bypass'] = {
                'detected': True,
                'triggers': asmr_matches,
                'risk': self.BYPASS_THRESHOLDS['asmr']['risk']
            }

        # Arousal bypass
        arousal_counts = {}
        for category, patterns in self.AROUSAL_WORDS.items():
            count = sum(len(re.findall(p, text)) for p in patterns)
            arousal_counts[category] = count

        word_count = len(text.split())
        total_arousal = sum(arousal_counts.values())
        arousal_density = total_arousal / word_count if word_count > 0 else 0

        if arousal_density > self.BYPASS_THRESHOLDS['arousal']['arousal_word_density']:
            findings['arousal_bypass'] = {
                'detected': True,
                'density': round(arousal_density, 4),
                'breakdown': arousal_counts,
                'risk': self.BYPASS_THRESHOLDS['arousal']['risk']
            }

        # Cognitive overload
        overload_matches = []
        for pattern in self.OVERLOAD_INDICATORS:
            found = re.findall(pattern, text)
            if found:
                overload_matches.extend([f[0] if isinstance(f, tuple) else f for f in found])

        paragraphs = text.split('\n\n')
        overload_score = len(overload_matches) / max(len(paragraphs), 1)

        if overload_score > 1.0:
            findings['overload_bypass'] = {
                'detected': True,
                'overload_markers': len(overload_matches),
                'per_paragraph': round(overload_score, 2),
                'risk': self.BYPASS_THRESHOLDS['overload']['risk']
            }

        # Media-based bypass (if media features provided)
        if media_features:
            cuts_per_min = media_features.get('cuts_per_minute', 0)
            if cuts_per_min > self.BYPASS_THRESHOLDS['rapid_cut']['cuts_per_minute']:
                findings['rapid_cut_bypass'] = {
                    'detected': True,
                    'cuts_per_minute': cuts_per_min,
                    'risk': self.BYPASS_THRESHOLDS['rapid_cut']['risk']
                }

            beat_regularity = media_features.get('beat_regularity', 0)
            if beat_regularity > self.BYPASS_THRESHOLDS['rhythm']['beat_regularity']:
                findings['rhythmic_bypass'] = {
                    'detected': True,
                    'regularity': beat_regularity,
                    'risk': self.BYPASS_THRESHOLDS['rhythm']['risk']
                }

        # Countermeasures
        bypass_count = len(findings)
        countermeasures = self._generate_countermeasures(findings)

        return {
            'bypass_mechanisms_detected': bypass_count,
            'findings': findings,
            'risk_score': min(1.0, bypass_count * 0.25),
            'countermeasures': countermeasures
        }

    def _generate_countermeasures(self, findings: Dict) -> List[str]:
        """Generate countermeasures for detected bypass mechanisms"""
        countermeasures = []
        if 'rapid_cut_bypass' in findings:
            countermeasures.append('Slow playback speed to restore analytical processing time')
        if 'asmr_bypass' in findings:
            countermeasures.append('Increase alertness before engaging with content (stand up, bright light)')
        if 'arousal_bypass' in findings:
            countermeasures.append('Take a 5-minute break before making decisions after high-arousal content')
        if 'overload_bypass' in findings:
            countermeasures.append('Break content into chunks; process one section at a time')
        if 'rhythmic_bypass' in findings:
            countermeasures.append('Mute audio periodically to break entrainment')
        return countermeasures
```

---

### 5.5 AI Amplification Detector

```python
class AIAmplificationDetector:
    """
    Detects AI-amplified persuasion techniques.

    Research: LLMs increase persuasion by 81.7% (Nature 2025).
    AI political ads as effective as human-written (Science 2025).
    """

    AI_TEXT_MARKERS = {
        'structural': [
            r'(?i)(in (conclusion|summary)|to (sum up|summarize))',
            r'(?i)(first(ly)?.*second(ly)?.*third(ly)?)',
            r'(?i)(it\'s (worth noting|important to note))',
        ],
        'hedging': [
            r'(?i)(it\'s important to (note|consider|remember))',
            r'(?i)(while (this|it|there) (may|might|could))',
            r'(?i)(however,?\s*it\'s)',
        ],
        'formulaic': [
            r'(?i)(here are \d+ (ways?|tips?|reasons?|steps?))',
            r'(?i)(in today\'s (world|landscape|digital age))',
            r'(?i)((delve|dive) (into|deeper))',
            r'(?i)(leverage|utilize|harness|optimize|streamline)',
        ]
    }

    BOT_SIGNATURES = {
        'timing': {
            'response_time_threshold_ms': 500,
            'posting_regularity_cv_threshold': 0.1,
            'activity_hours_threshold': 20
        },
        'content': {
            'no_typos': True,
            'consistent_formatting': True,
            'no_personal_anecdotes': True,
            'formulaic_empathy': True
        }
    }

    PERSONALIZATION_MARKERS = [
        r'(?i)(based on your (profile|behavior|preferences|history))',
        r'(?i)(personali[sz]ed|tailored|customiz[sz]ed) for you',
        r'(?i)(users? like you|people in your)',
        r'(?i)(we (noticed|detected|know) (that )?you)'
    ]

    def detect_ai_amplification(self, text: str, metadata: Dict = None) -> Dict:
        """Detect AI amplification of persuasion"""
        # AI text detection
        ai_markers = {}
        for category, patterns in self.AI_TEXT_MARKERS.items():
            matches = []
            for pattern in patterns:
                found = re.findall(pattern, text)
                if found:
                    matches.extend([f[0] if isinstance(f, tuple) else f for f in found])
            ai_markers[category] = matches

        total_markers = sum(len(m) for m in ai_markers.values())
        word_count = len(text.split())
        marker_density = total_markers / word_count if word_count > 0 else 0

        # Personalization detection
        personalization = []
        for pattern in self.PERSONALIZATION_MARKERS:
            found = re.findall(pattern, text)
            if found:
                personalization.extend([f[0] if isinstance(f, tuple) else f for f in found])

        # Bot signature check (if metadata available)
        bot_score = 0.0
        if metadata:
            if metadata.get('response_time_ms', 9999) < self.BOT_SIGNATURES['timing']['response_time_threshold_ms']:
                bot_score += 0.3
            if metadata.get('no_typos', False):
                bot_score += 0.1
            if metadata.get('posting_regularity_cv', 1.0) < self.BOT_SIGNATURES['timing']['posting_regularity_cv_threshold']:
                bot_score += 0.3

        # Combined assessment
        ai_probability = min(0.95, marker_density * 10 + bot_score)

        return {
            'ai_probability': round(ai_probability, 2),
            'ai_markers': ai_markers,
            'total_markers': total_markers,
            'marker_density': round(marker_density, 4),
            'personalization_detected': len(personalization) > 0,
            'personalization_instances': personalization,
            'bot_score': round(bot_score, 2),
            'amplification_risk': 'high' if ai_probability > 0.7 else 'moderate' if ai_probability > 0.4 else 'low',
            'concern': 'AI-generated persuasion is 81.7% more effective than human baseline' if ai_probability > 0.5 else None
        }
```

---

### 5.6 Ranked Combination Effectiveness Data

Research-derived rankings of persuasion technique combinations by measured effectiveness multiplier:

| Rank | Combination | Multiplier | Primary Defense |
|------|------------|-----------|-----------------|
| 1 | Emotional fractionation + commercial relief | **2.1x** | Awareness of cycling pattern; pause before purchase |
| 2 | Scarcity + social proof + urgency | **1.95x** | Verify scarcity claims; check if offer returns |
| 3 | Authority + fear + solution product | **1.85x** | Verify authority credentials; seek second opinion |
| 4 | Personalization + vulnerability timing | **1.82x** | Be aware of timing; avoid decisions when depleted |
| 5 | Identity lock-in + sunk cost + social proof | **1.78x** | Calculate actual value; ignore sunk costs |
| 6 | Anchoring + decoy + scarcity | **1.72x** | Research market prices independently |
| 7 | Reciprocity + commitment escalation | **1.68x** | Recognize gift ≠ obligation; evaluate each ask independently |
| 8 | Trust building + isolation + urgency | **1.65x** | Maintain outside counsel; impose cooling-off periods |
| 9 | Gamification + variable reward + sunk cost | **1.62x** | Set time/money limits; track actual utility vs. engagement |
| 10 | Social comparison + shame + solution | **1.58x** | Recognize comparison manipulation; define own metrics |
| 11 | Curiosity gap + information asymmetry + authority | **1.52x** | Recognize clickbait structure; verify claims |
| 12 | Default bias + friction asymmetry + commitment | **1.48x** | Actively review defaults; question pre-selections |
| 13 | Nostalgia + identity + community | **1.42x** | Recognize emotional appeal; evaluate offer objectively |
| 14 | Pain agitation + urgency + social proof | **1.35x** | Acknowledge pain without panic; research solutions |
| 15 | Repetition + familiarity + mere exposure | **1.28x** | Recognize familiarity ≠ quality; compare alternatives |

**Defenses for Top 5 Combinations:**

1. **Fractionation + commercial relief (2.1x):** Recognize when content alternates fear/anger with joy/relief. The product/service appearing during the "relief" phase is exploiting reduced critical thinking. Countermeasure: pause, leave the environment, return later.

2. **Scarcity + social proof + urgency (1.95x):** "Only 3 left, 47 people viewing, offer expires in 2 hours." Countermeasure: close the page, check if the offer returns tomorrow (it usually does).

3. **Authority + fear + solution (1.85x):** "Experts warn of X danger → but our product protects you." Countermeasure: verify the authority independently, check if the fear is proportionate.

4. **Personalization + vulnerability timing (1.82x):** Targeted content delivered when you're depleted/emotional. Countermeasure: avoid major decisions late at night or when stressed.

5. **Identity lock-in + sunk cost + social proof (1.78x):** "You've invested 200 hours, your friends are here, this is who you are." Countermeasure: evaluate current value, not past investment.

---

### 5.7 Temporal Intensity Detector

```python
class TemporalIntensityDetector:
    """
    Detects temporal patterns in persuasion intensity.
    """

    VULNERABILITY_WINDOWS = {
        'late_night': {'hours': (22, 4), 'multiplier': 1.4, 'factor': 'reduced_inhibition'},
        'early_morning': {'hours': (5, 7), 'multiplier': 1.2, 'factor': 'cortisol_spike'},
        'post_lunch': {'hours': (13, 15), 'multiplier': 1.15, 'factor': 'cognitive_dip'},
        'commute': {'hours': (7, 9), 'multiplier': 1.1, 'factor': 'attention_divided'},
        'evening_wind_down': {'hours': (20, 22), 'multiplier': 1.25, 'factor': 'ego_depletion'},
        'weekend_morning': {'hours': (9, 11), 'multiplier': 1.1, 'factor': 'leisure_spending'}
    }

    DECISION_FATIGUE_MODEL = {
        'baseline_capacity': 100,
        'cost_per_decision': {
            'trivial': 2,        # "What to eat"
            'minor': 5,          # "Which email to respond to"
            'moderate': 15,      # "Whether to buy"
            'major': 30,         # "Career/financial decisions"
            'high_stakes': 50    # "Medical/legal decisions"
        },
        'recovery_per_hour_rest': 10,
        'critical_threshold': 30,     # Below this = highly vulnerable
        'default_acceptance_threshold': 20  # Below this = accepts defaults
    }

    NOTIFICATION_WINDOWS = {
        'optimal_open_rate': {'hours': (8, 10), 'rate': 0.45},
        'optimal_click_rate': {'hours': (20, 22), 'rate': 0.12},
        'optimal_purchase_rate': {'hours': (21, 23), 'rate': 0.08},
        'optimal_impulse_rate': {'hours': (23, 2), 'rate': 0.15}
    }

    def analyze_temporal_pattern(self, content_timeline: List[Dict]) -> Dict:
        """
        Analyze temporal pattern of content delivery for exploitation.

        Args:
            content_timeline: List of {'timestamp': datetime_str, 'type': str,
                             'intensity': float, 'persuasion_score': float}
        """
        if not content_timeline:
            return {'analyzed': False}

        # Check if high-intensity content clusters at vulnerable times
        vulnerable_delivery = 0
        total_items = len(content_timeline)

        for item in content_timeline:
            hour = item.get('hour', 12)
            intensity = item.get('persuasion_score', 0)

            for window_name, window in self.VULNERABILITY_WINDOWS.items():
                h_start, h_end = window['hours']
                in_window = (h_start <= hour <= h_end) if h_start < h_end else (hour >= h_start or hour <= h_end)

                if in_window and intensity > 0.5:
                    vulnerable_delivery += 1

        exploitation_ratio = vulnerable_delivery / total_items if total_items > 0 else 0

        return {
            'total_items': total_items,
            'vulnerable_time_delivery': vulnerable_delivery,
            'exploitation_ratio': round(exploitation_ratio, 2),
            'deliberate_timing': exploitation_ratio > 0.5,
            'risk_score': min(1.0, exploitation_ratio * 1.5)
        }

    def model_decision_capacity(self, decision_log: List[Dict]) -> Dict:
        """Model remaining decision capacity based on decisions made today"""
        capacity = self.DECISION_FATIGUE_MODEL['baseline_capacity']

        for decision in decision_log:
            d_type = decision.get('type', 'minor')
            cost = self.DECISION_FATIGUE_MODEL['cost_per_decision'].get(d_type, 5)
            capacity -= cost

            # Rest recovery
            rest_hours = decision.get('rest_since_last', 0)
            capacity += rest_hours * self.DECISION_FATIGUE_MODEL['recovery_per_hour_rest']
            capacity = min(100, capacity)

        return {
            'remaining_capacity': max(0, capacity),
            'vulnerability_level': 'critical' if capacity < self.DECISION_FATIGUE_MODEL['critical_threshold']
                else 'high' if capacity < 50
                else 'moderate' if capacity < 70
                else 'low',
            'will_accept_defaults': capacity < self.DECISION_FATIGUE_MODEL['default_acceptance_threshold'],
            'recommendation': 'Avoid major decisions' if capacity < 30 else 'Proceed with caution' if capacity < 50 else 'Normal capacity'
        }
```

---

### 5.8 Precise Behavioral Indicator Detector

```python
class PreciseBehavioralIndicatorDetector:
    """
    Clinical-precision behavioral indicator detection.

    Uses specific, measurable behavioral indicators rather than
    broad pattern matching. 6 behavioral indicator categories.
    """

    BEHAVIORAL_INDICATORS = {
        'developmental_vulnerability': {
            'description': 'Age-appropriate development indicators',
            'markers': [
                'impulse_control_developing',      # Age < 25 (prefrontal cortex maturation)
                'abstract_thinking_limited',        # Age < 12
                'peer_influence_heightened',         # Age 12-18
                'authority_trust_default',           # Age < 10
                'ad_content_distinction_absent'      # Age < 8
            ],
            'risk_multiplier': 2.0
        },
        'impulse_control_deficit': {
            'description': 'Reduced ability to delay gratification or resist impulse',
            'markers': [
                'rapid_decision_making',            # Decisions in < 5 seconds
                'regret_after_purchase',            # Returns/complaints pattern
                'late_night_purchasing',            # Purchases 11PM-4AM
                'emotional_state_purchasing',        # Purchases after negative events
                'escalating_spending_pattern'        # Spending increases over time
            ],
            'risk_multiplier': 1.5
        },
        'cognitive_depletion': {
            'description': 'Temporary reduction in cognitive capacity',
            'markers': [
                'decision_count_high',              # > 30 decisions today
                'task_switching_frequent',           # > 20 context switches
                'time_of_day_late',                 # After 10PM
                'stress_indicators_present',        # Elevated cortisol indicators
                'sleep_deprivation_likely'           # Active > 18 hours
            ],
            'risk_multiplier': 1.3
        },
        'limited_social_network': {
            'description': 'Reduced access to external validation/counsel',
            'markers': [
                'single_information_source',         # One content platform
                'no_peer_consultation',              # Decisions without discussion
                'geographic_isolation',              # Remote location
                'language_barrier',                  # Non-native language
                'digital_literacy_low'               # Difficulty navigating interfaces
            ],
            'risk_multiplier': 1.4
        },
        'social_signal_processing': {
            'description': 'Difficulty processing social influence cues',
            'markers': [
                'sarcasm_detection_difficulty',
                'social_hierarchy_confusion',
                'implicit_communication_miss',
                'trust_calibration_atypical',
                'reciprocity_norm_unfamiliar'
            ],
            'risk_multiplier': 1.3
        },
        'emotional_state_vulnerability': {
            'description': 'Current emotional state reducing rational evaluation',
            'markers': [
                'grief_recent',                     # Within 6 months
                'relationship_disruption',           # Recent breakup/divorce
                'financial_stress',                  # Debt/job loss
                'health_anxiety',                    # Recent diagnosis
                'loneliness_chronic'                 # Social isolation > 3 months
            ],
            'risk_multiplier': 1.7
        }
    }

    def assess_vulnerability(self, behavioral_data: Dict) -> Dict:
        """
        Assess vulnerability using precise behavioral indicators.

        Args:
            behavioral_data: Dict mapping indicator names to values
        """
        active_indicators = {}
        total_risk = 0.0

        for category, config in self.BEHAVIORAL_INDICATORS.items():
            active_markers = []
            for marker in config['markers']:
                if behavioral_data.get(marker, False):
                    active_markers.append(marker)

            if active_markers:
                category_risk = len(active_markers) / len(config['markers']) * config['risk_multiplier']
                active_indicators[category] = {
                    'active_markers': active_markers,
                    'marker_count': len(active_markers),
                    'total_markers': len(config['markers']),
                    'category_risk': round(category_risk, 2),
                    'description': config['description']
                }
                total_risk += category_risk

        overall_risk = min(1.0, total_risk / len(self.BEHAVIORAL_INDICATORS))

        return {
            'active_indicators': active_indicators,
            'active_category_count': len(active_indicators),
            'overall_vulnerability': round(overall_risk, 2),
            'risk_level': 'critical' if overall_risk > 0.7 else 'high' if overall_risk > 0.5 else 'moderate' if overall_risk > 0.3 else 'low',
            'protective_actions': self._recommend_protections(active_indicators)
        }

    def _recommend_protections(self, indicators: Dict) -> List[str]:
        """Generate protective action recommendations"""
        protections = []
        if 'developmental_vulnerability' in indicators:
            protections.append('Apply age-appropriate content restrictions')
        if 'impulse_control_deficit' in indicators:
            protections.append('Implement mandatory cooling-off period before purchases')
        if 'cognitive_depletion' in indicators:
            protections.append('Delay important decisions until cognitive capacity restored')
        if 'limited_social_network' in indicators:
            protections.append('Seek external input before major decisions')
        if 'emotional_state_vulnerability' in indicators:
            protections.append('Increase decision friction during emotional vulnerability periods')
        return protections
```

---

### 5.9 Information Ecosystem Detector

```python
class InformationEcosystemDetector:
    """
    Detects information ecosystem manipulation:
    echo chambers, emotional contagion, trust erosion.
    """

    CONTAGION_PATTERNS = {
        'anger_cascade': {
            'seed_patterns': [r'(?i)(outrage|scandal|unbelievable|how (dare|could) they)'],
            'amplification': [r'(?i)(share this|spread the word|everyone needs to (see|know)|retweet|RT)'],
            'cascade_velocity_threshold': 100  # shares per hour
        },
        'fear_cascade': {
            'seed_patterns': [r'(?i)(breaking|alert|warning|emergency|danger|threat)'],
            'amplification': [r'(?i)(protect yourself|be (careful|warned)|stay safe|watch out)'],
            'cascade_velocity_threshold': 150
        },
        'hope_cascade': {
            'seed_patterns': [r'(?i)(miracle|cure|breakthrough|solution|finally)'],
            'amplification': [r'(?i)(this (changes|could change) everything|game[- ]changer)'],
            'cascade_velocity_threshold': 80
        }
    }

    def analyze_ecosystem(self, feed_data: Dict) -> Dict:
        """
        Analyze information ecosystem for manipulation patterns.

        Args:
            feed_data: Dict with 'posts', 'sources', 'diversity_metrics',
                      'emotional_distribution', 'sharing_patterns'
        """
        findings = {}

        # Echo chamber analysis
        source_diversity = feed_data.get('source_diversity', 1.0)
        viewpoint_diversity = feed_data.get('viewpoint_diversity', 1.0)
        echo_score = 1.0 - ((source_diversity + viewpoint_diversity) / 2)

        findings['echo_chamber'] = {
            'score': round(echo_score, 2),
            'source_diversity': source_diversity,
            'viewpoint_diversity': viewpoint_diversity,
            'assessment': 'echo_chamber' if echo_score > 0.7 else 'partial_bubble' if echo_score > 0.4 else 'diverse'
        }

        # Emotional contagion
        emotions = feed_data.get('emotional_distribution', {})
        negative = sum(emotions.get(e, 0) for e in ['anger', 'fear', 'sadness', 'outrage'])
        total = sum(emotions.values()) if emotions else 1
        negative_ratio = negative / total

        findings['emotional_contagion'] = {
            'negative_ratio': round(negative_ratio, 2),
            'dominant_emotion': max(emotions, key=emotions.get) if emotions else 'none',
            'risk': 'high' if negative_ratio > 0.6 else 'moderate' if negative_ratio > 0.3 else 'low'
        }

        # Trust erosion (check for systematic trust-undermining)
        posts = feed_data.get('posts', [])
        trust_erosion_patterns = [
            r'(?i)(can\'t trust|don\'t believe|they\'re lying|fake news|mainstream media)',
            r'(?i)(wake up|sheep|brainwashed|think for yourself)',
            r'(?i)(they don\'t want you to know|the truth they\'re hiding)'
        ]

        trust_erosion_count = 0
        for post in posts:
            text = post.get('text', '') if isinstance(post, dict) else str(post)
            for pattern in trust_erosion_patterns:
                if re.search(pattern, text):
                    trust_erosion_count += 1
                    break

        trust_erosion_ratio = trust_erosion_count / len(posts) if posts else 0

        findings['trust_erosion'] = {
            'ratio': round(trust_erosion_ratio, 2),
            'count': trust_erosion_count,
            'risk': 'high' if trust_erosion_ratio > 0.3 else 'moderate' if trust_erosion_ratio > 0.1 else 'low'
        }

        # Overall ecosystem health
        overall = (echo_score + negative_ratio + trust_erosion_ratio) / 3

        return {
            'findings': findings,
            'overall_manipulation_score': round(overall, 2),
            'assessment': 'compromised' if overall > 0.6 else 'at_risk' if overall > 0.3 else 'healthy'
        }
```

---

## PART 6: MASTER INTEGRATION CLASSES {#part-6}

### 6.1 Master High-Impact Auditor

```python
class MasterHighImpactAuditor:
    """
    Master integration class combining all high-impact detection systems.

    Provides single entry point for comprehensive influence auditing.
    """

    def __init__(self):
        self.stacking_detector = SynergisticStackingDetector()
        self.timing_detector = VulnerabilityTimingDetector()
        self.trust_detector = TrustLeverageSequenceDetector()
        self.bypass_detector = PhysiologicalBypassDetector()
        self.ai_detector = AIAmplificationDetector()
        self.temporal_detector = TemporalIntensityDetector()
        self.behavioral_detector = PreciseBehavioralIndicatorDetector()
        self.ecosystem_detector = InformationEcosystemDetector()

    def comprehensive_audit(self, content: Dict, context: Dict = None) -> Dict:
        """
        Run all high-impact detection systems.

        Args:
            content: Dict with 'text', 'ui_elements', 'messages',
                    'media_features', 'feed_data'
            context: Dict with 'timestamp', 'user_context',
                    'behavioral_data'
        """
        report = {
            'synergistic_stacking': None,
            'vulnerability_timing': None,
            'trust_leverage': None,
            'physiological_bypass': None,
            'ai_amplification': None,
            'temporal_intensity': None,
            'behavioral_vulnerability': None,
            'information_ecosystem': None,
            'overall_risk': 0.0,
            'critical_findings': [],
            'recommended_actions': []
        }

        risk_scores = []

        # 1. Synergistic stacking
        if 'text' in content:
            stacking = self.stacking_detector.detect_stacking(
                content['text'],
                content.get('ui_elements', [])
            )
            report['synergistic_stacking'] = stacking
            risk_scores.append(stacking['risk_score'])
            if stacking['synergy_count'] >= 2:
                report['critical_findings'].append(
                    f"SYNERGY_STACK: {stacking['synergy_count']} synergistic combinations detected "
                    f"(combined multiplier: {stacking['combined_multiplier']}x)"
                )

        # 2. Vulnerability timing
        if context and 'timestamp' in context:
            timing = self.timing_detector.assess_timing_vulnerability(
                context['timestamp'],
                context.get('user_context')
            )
            report['vulnerability_timing'] = timing
            risk_scores.append(timing['risk_score'])
            if timing['risk_score'] > 0.5:
                report['critical_findings'].append(
                    f"TIMING: Content delivered during vulnerability window "
                    f"(risk: {timing['risk_score']:.2f})"
                )

        # 3. Trust leverage
        if 'messages' in content:
            trust = self.trust_detector.analyze_sequence(content['messages'])
            report['trust_leverage'] = trust
            risk_scores.append(trust['risk_score'])
            if trust['assessment'] == 'trust_leverage_detected':
                report['critical_findings'].append(
                    f"TRUST_LEVERAGE: {trust['stage_count']} trust stages detected"
                )

        # 4. Physiological bypass
        if 'text' in content:
            bypass = self.bypass_detector.analyze_content(
                content['text'],
                content.get('media_features')
            )
            report['physiological_bypass'] = bypass
            risk_scores.append(bypass['risk_score'])
            if bypass['bypass_mechanisms_detected'] >= 2:
                report['critical_findings'].append(
                    f"BYPASS: {bypass['bypass_mechanisms_detected']} physiological bypass mechanisms detected"
                )

        # 5. AI amplification
        if 'text' in content:
            ai = self.ai_detector.detect_ai_amplification(
                content['text'],
                content.get('metadata')
            )
            report['ai_amplification'] = ai
            risk_scores.append(ai['ai_probability'] * 0.5)
            if ai['amplification_risk'] == 'high':
                report['critical_findings'].append(
                    f"AI_AMPLIFICATION: High probability ({ai['ai_probability']:.0%}) of AI-generated persuasion"
                )

        # 6. Temporal intensity
        if 'content_timeline' in content:
            temporal = self.temporal_detector.analyze_temporal_pattern(content['content_timeline'])
            report['temporal_intensity'] = temporal
            if temporal.get('deliberate_timing'):
                risk_scores.append(temporal['risk_score'])
                report['critical_findings'].append("TEMPORAL: Deliberate high-intensity delivery at vulnerable times")

        # 7. Behavioral vulnerability
        if context and 'behavioral_data' in context:
            behavioral = self.behavioral_detector.assess_vulnerability(context['behavioral_data'])
            report['behavioral_vulnerability'] = behavioral
            risk_scores.append(behavioral['overall_vulnerability'])
            if behavioral['risk_level'] in ['critical', 'high']:
                report['critical_findings'].append(
                    f"VULNERABILITY: {behavioral['risk_level']} behavioral vulnerability "
                    f"({behavioral['active_category_count']} categories active)"
                )

        # 8. Information ecosystem
        if 'feed_data' in content:
            ecosystem = self.ecosystem_detector.analyze_ecosystem(content['feed_data'])
            report['information_ecosystem'] = ecosystem
            risk_scores.append(ecosystem['overall_manipulation_score'])
            if ecosystem['assessment'] == 'compromised':
                report['critical_findings'].append("ECOSYSTEM: Information ecosystem assessed as compromised")

        # Overall risk
        if risk_scores:
            report['overall_risk'] = round(
                sum(risk_scores) / len(risk_scores) * 0.6 + max(risk_scores) * 0.4,
                3
            )

        # Recommended actions
        report['recommended_actions'] = self._generate_recommendations(report)

        return report

    def _generate_recommendations(self, report: Dict) -> List[str]:
        """Generate actionable recommendations based on findings"""
        actions = []

        if report['overall_risk'] > 0.7:
            actions.append('IMMEDIATE: Implement full content review and user protection measures')
        elif report['overall_risk'] > 0.4:
            actions.append('PRIORITY: Schedule detailed audit and implement monitoring')

        if report.get('synergistic_stacking', {}).get('synergy_count', 0) >= 2:
            actions.append('Decompose stacked techniques and evaluate each independently')

        if report.get('vulnerability_timing', {}).get('risk_score', 0) > 0.5:
            actions.append('Implement cooling-off periods for decisions during vulnerable windows')

        if report.get('physiological_bypass', {}).get('bypass_mechanisms_detected', 0) >= 2:
            actions.append('Add friction/breaks to counter physiological bypass mechanisms')

        if report.get('ai_amplification', {}).get('amplification_risk') == 'high':
            actions.append('Flag as potentially AI-generated; verify claims independently')

        bypass = report.get('physiological_bypass', {})
        if 'countermeasures' in bypass:
            actions.extend(bypass['countermeasures'])

        behavioral = report.get('behavioral_vulnerability', {})
        if 'protective_actions' in behavioral:
            actions.extend(behavioral['protective_actions'])

        return list(dict.fromkeys(actions))  # Deduplicate while preserving order
```

### 6.2 Comprehensive Persuasion Auditor (Full Integration)

```python
class ComprehensivePersuasionAuditor:
    """
    Complete master class integrating ALL detection frameworks.

    Provides unified interface for full persuasion/influence auditing
    across all domains: text, interface, pricing, multimodal, social,
    trust, platform, physiological, economic, AI, regulatory, and
    high-impact specialized systems.
    """

    def __init__(self):
        # Core detection
        self.text_engine = MachineReadableDetectionEngine()
        self.enhanced_audit = ComprehensivePersuasionAudit()

        # Comprehensive frameworks (Part 4)
        self.multimodal_detector = MultimodalPersuasionDetector()
        self.cut_rhythm_analyzer = CutRhythmAnalyzer()
        self.social_network_detector = SocialNetworkInfluenceDetector()
        self.emotional_contagion_detector = EmotionalContagionDetector()
        self.echo_chamber_detector = EchoChAmberDetector()
        self.trust_detector = TrustInfluenceDetector()
        self.grooming_detector = GroomingPatternDetector()
        self.platform_detector = PlatformInfluenceDetector()
        self.infinite_scroll_detector = InfiniteScrollDetector()
        self.physiological_detector = PhysiologicalInfluenceDetector()
        self.gaze_analyzer = GazePatternAnalyzer()
        self.vulnerability_detector = VulnerablePopulationDetector()
        self.child_safety_detector = ChildSafetyDetector()
        self.economic_detector = EconomicInfluenceDetector()
        self.subscription_detector = SubscriptionTrapDetector()
        self.ai_detector = AIInfluenceDetector()
        self.deepfake_detector = DeepfakeDetector()
        self.intervention_analyzer = InterventionAnalyzer()
        self.compliance_analyzer = RegulatoryComplianceAnalyzer()

        # High-impact systems (Part 5)
        self.high_impact_auditor = MasterHighImpactAuditor()

    def full_audit(self, content_data: Dict, user_profile: Dict = None,
                   context: Dict = None) -> Dict:
        """
        Perform comprehensive audit across ALL detection systems.

        Args:
            content_data: All available content information
            user_profile: Optional user vulnerability profile
            context: Optional timing/behavioral context

        Returns:
            Complete audit report with all findings
        """
        import time
        report = {
            'audit_timestamp': time.time(),
            'overall_risk_score': 0.0,
            'influence_categories': {},
            'specific_findings': [],
            'vulnerability_assessment': None,
            'regulatory_concerns': [],
            'recommended_interventions': [],
            'high_impact_analysis': None,
            'summary': ''
        }

        risk_scores = []

        # === CORE TEXT ANALYSIS ===
        if 'text' in content_data:
            text_result = self.text_engine.analyze(content_data['text'])
            report['influence_categories']['text_persuasion'] = {
                'composite_score': text_result.composite_score,
                'intensity': text_result.intensity_level.value,
                'red_flags': text_result.red_flags
            }
            risk_scores.append(text_result.composite_score / 100)

        # === MULTIMODAL ANALYSIS ===
        if 'audio' in content_data:
            audio_result = self.multimodal_detector.analyze_audio_features(content_data['audio'])
            report['influence_categories']['audio'] = {
                'risk_score': audio_result.risk_score,
                'influence_types': [t.value for t in audio_result.influence_types]
            }
            risk_scores.append(audio_result.risk_score)

        if 'video' in content_data:
            video_result = self.multimodal_detector.analyze_video_features(content_data['video'])
            report['influence_categories']['video'] = {
                'risk_score': video_result.risk_score,
                'influence_types': [t.value for t in video_result.influence_types]
            }
            risk_scores.append(video_result.risk_score)

        # === SOCIAL/TRUST ANALYSIS ===
        if 'messages' in content_data:
            trust_indicators = self.trust_detector.analyze_message(
                content_data.get('text', '')
            )
            if trust_indicators:
                report['influence_categories']['trust_influence'] = {
                    'indicators': [ind['influence_type'] for ind in trust_indicators],
                    'count': len(trust_indicators)
                }
                risk_scores.append(0.7 if any(i.get('risk_level') == 'critical' for i in trust_indicators) else 0.4)

            grooming_result = self.grooming_detector.analyze_interaction_sequence(content_data['messages'])
            if grooming_result['risk_score'] > 0.3:
                report['influence_categories']['grooming_patterns'] = {
                    'stage': grooming_result['stage'],
                    'risk_score': grooming_result['risk_score']
                }
                risk_scores.append(grooming_result['risk_score'])

        # === PLATFORM/INTERFACE ANALYSIS ===
        if 'interface' in content_data:
            platform_result = self.platform_detector.analyze_app_interface(content_data['interface'])
            if platform_result['overall_influence_score'] > 0.3:
                report['influence_categories']['platform_influence'] = {
                    'types': [t for t in platform_result.get('influence_types', [])],
                    'risk_score': platform_result['overall_influence_score']
                }
                risk_scores.append(platform_result['overall_influence_score'])

        # === PRICING ANALYSIS ===
        if 'pricing' in content_data:
            pricing_result = self.economic_detector.analyze_pricing_page(content_data['pricing'])
            if pricing_result['overall_influence_score'] > 0.3:
                report['influence_categories']['economic_influence'] = {
                    'types': pricing_result.get('influence_types', []),
                    'risk_score': pricing_result['overall_influence_score']
                }
                risk_scores.append(pricing_result['overall_influence_score'])

        # === AI DETECTION ===
        if 'text' in content_data:
            ai_result = self.ai_detector.analyze_text_for_ai_generation(content_data['text'])
            if ai_result['ai_generated_probability'] > 0.4:
                report['influence_categories']['ai_generated'] = {
                    'probability': ai_result['ai_generated_probability'],
                    'markers': ai_result['synthetic_markers']
                }
                risk_scores.append(ai_result['ai_generated_probability'] * 0.5)

        # === VULNERABILITY ASSESSMENT ===
        if user_profile:
            vuln_profile = self.vulnerability_detector.assess_individual_vulnerability(user_profile)
            report['vulnerability_assessment'] = {
                'score': vuln_profile['overall_vulnerability_score'],
                'factors': vuln_profile['factors'],
                'risk_areas': vuln_profile['risk_areas'],
                'recommendations': vuln_profile['protective_recommendations']
            }
            if vuln_profile['overall_vulnerability_score'] > 0.5:
                risk_scores = [r * 1.3 for r in risk_scores]

        # === HIGH-IMPACT ANALYSIS ===
        high_impact = self.high_impact_auditor.comprehensive_audit(content_data, context)
        report['high_impact_analysis'] = {
            'overall_risk': high_impact['overall_risk'],
            'critical_findings': high_impact['critical_findings'],
            'recommended_actions': high_impact['recommended_actions']
        }
        risk_scores.append(high_impact['overall_risk'])

        # === CALCULATE OVERALL RISK ===
        if risk_scores:
            import numpy as np
            report['overall_risk_score'] = min(1.0,
                float(np.mean(risk_scores)) + float(np.max(risk_scores)) * 0.2
            )

        # === REGULATORY COMPLIANCE ===
        influence_summary = {
            'influence_types': list(report['influence_categories'].keys()),
            'overall_risk_score': report['overall_risk_score']
        }
        violations = self.compliance_analyzer.analyze_compliance(influence_summary)
        if violations:
            report['regulatory_concerns'] = [
                {
                    'law': v.specific_law,
                    'severity': v.severity,
                    'penalty': v.potential_penalty,
                    'remediation': v.remediation_steps
                }
                for v in violations
            ]

        # === INTERVENTION RECOMMENDATIONS ===
        report['recommended_interventions'] = self.intervention_analyzer.recommend_interventions(
            influence_summary,
            user_profile
        )

        # === GENERATE SUMMARY ===
        risk_level = 'CRITICAL' if report['overall_risk_score'] > 0.8 else (
            'HIGH' if report['overall_risk_score'] > 0.6 else (
            'MODERATE' if report['overall_risk_score'] > 0.3 else 'LOW'))

        categories = list(report['influence_categories'].keys())
        critical = len(high_impact.get('critical_findings', []))

        report['summary'] = (
            f"Overall Risk: {risk_level} ({report['overall_risk_score']:.2f}) | "
            f"Categories: {len(categories)} | "
            f"Critical Findings: {critical} | "
            f"Regulatory Concerns: {len(report['regulatory_concerns'])}"
        )

        return report
```

---

## APPENDIX: Research Sources {#appendix}

### Foundational
- Renvoise & Morin — Neuromarketing: Understanding the Buy Buttons in Your Customer's Brain
- Cialdini — Influence: The Psychology of Persuasion (7 principles)
- Kahneman — Thinking, Fast and Slow
- Tversky & Kahneman — Judgment Under Uncertainty: Heuristics and Biases

### Platform Research (2024-2025)
- Facebook internal research on anger-weighted engagement (5x multiplier)
- TikTok recommendation system emotional detection (94% accuracy)
- Science (2023) — Algorithmic amplification field experiment
- FTC 2024 — Amazon ($2.5B settlement), Adobe enforcement actions
- EU DSA implementation Feb 2024

### Multimodal & Audio
- ICMI 2025: Multimodal persuasion research
- Personality and Social Psychology Bulletin 2024: Voice tone and persuasion
- MDPI 2024: ASMR emotional and physiological responses

### Social Networks
- Springer 2025: Cascading falsehoods mapping
- Nature 2026: Temporal graph analysis of fake news
- NATO StratCom 2024: Social media influence report

### Trust & Grooming
- ACIG Journal 2024: Trust framework for cybersecurity
- Zero Abuse Project 2024: Influence and grooming patterns

### Platform Mechanics
- CHI 2024: "Staying at the Roach Motel"
- CHI 2025: Design frictions on social media
- ScienceDirect 2025: Scroll immersion research

### Vulnerable Populations
- USC Dornsife 2024: Alzheimer's and scam vulnerability
- PNAS Nexus 2024: APOE4 and phishing
- Thorn 2024: Youth online safety data
- Psychology Today 2025: Neurodivergent vulnerability

### AI & Deepfakes
- Science 2025: Political persuasion with AI
- Nature 2025: LLM persuasive power meta-analysis (81.7% increase)
- PMC 2025: Deepfake forensics survey
- Deloitte 2025: Deepfake disruption report

### Interventions
- Sage 2024: Media literacy meta-analysis (N=81,155, d=0.60)
- Taiwan 2024: Adolescent media literacy intervention
- Compton & Pfau: Inoculation theory (d=0.36)
- CHI 2025: Design friction studies (d=0.45)

### Regulatory
- FTC 2024: Amazon, Adobe enforcement actions
- EU DSA 2024: Implementation and enforcement
- EU AI Act: Phased implementation
- CCPA/CPRA: California dark pattern prohibitions
- German Fair Consumer Contracts Act

---

## SECTION 7: COMPREHENSIVE AUDITING CHECKLIST (from Professional Auditor Manual)

### Pre-Audit Preparation

**Step 1: Gather the Content**
- [ ] Product copy
- [ ] Visual descriptions (if available)
- [ ] Email sequences
- [ ] Social media posts
- [ ] Landing page copy
- [ ] About page
- [ ] Pricing page
- [ ] Any other customer-facing content

**Step 2: Establish Baseline**
- [ ] Note the company/brand being audited
- [ ] Note the target audience
- [ ] Note the product/service being marketed
- [ ] Note any stated values or positioning

---

### Tactical Stimulus Audit

**STIMULUS 1: PERSONAL**
- [ ] Search for exact exclusion phrases ("Not for everyone," "If you know, you know")
- [ ] Search for status threat language ("Being basic," "Fear of cultural irrelevance")
- [ ] Search for tribal safety signals ("We understand the references you understand")
- [ ] Total score: _____ / 100
- [ ] Red flags detected: _________________

**STIMULUS 2: CONTRASTABLE**
- [ ] Identify binary oppositions (Mass ↔ Artifact, Algorithmic ↔ Authored, etc.)
- [ ] Count contrast markers ("vs," "but we," "while they")
- [ ] Check for spectrum language (if present, reduces score)
- [ ] Total score: _____ / 100
- [ ] Primary binary pairs: _________________

**STIMULUS 3: TANGIBLE**
- [ ] Document specific material details (weights, measurements, production facts)
- [ ] Document sensory descriptions
- [ ] Count abstract language and deduct points
- [ ] Total score: _____ / 100
- [ ] Specific details found: _________________

**STIMULUS 4: MEMORABLE**
- [ ] Analyze opening (first 3 sentences) for impact
- [ ] Analyze closing (last 3 sentences) for impact
- [ ] Count filler language in middle
- [ ] Total score: _____ / 100
- [ ] U-curve structure: _________________

**STIMULUS 5: VISUAL**
- [ ] Note visual descriptions or imagery
- [ ] Search for anti-aesthetic language ("Grainy," "Bad lighting," "CCTV")
- [ ] Search for polished language (penalizes score)
- [ ] Total score: _____ / 100
- [ ] Aesthetic positioning: _________________

**STIMULUS 6: EMOTIONAL**
- [ ] Identify pain/threat messaging (status anxiety, cultural irrelevance, algorithmic capture)
- [ ] Identify relief/solution messaging
- [ ] Assess if complete arc present (pain → relief)
- [ ] Total score: _____ / 100
- [ ] Emotional arc type: _________________

**COMPOSITE TACTICAL SCORE:** Average of all 6 = _____ / 100

---

### Psychological Principles Audit

**AUTHORITY PRINCIPLE**
- [ ] Search for credentials (Dr., Ph.D, Expert, Professor, etc.)
- [ ] Search for institutional signals (Harvard, Stanford, MIT, etc.)
- [ ] Search for experience claims ("30 years," "Industry leader")
- [ ] Assess confidence markers (steady tone, precise language, etc.)
- [ ] Check for threat reduction
- [ ] Authority formula result: _____ (Competence + Confidence) / Threat
- [ ] Expected compliance: _________________

**SOCIAL PROOF PRINCIPLE**
- [ ] Look for consensus language ("Most popular," "Bestseller," "Everyone agrees")
- [ ] Look for similarity signals ("People like you," "Your peers")
- [ ] Check if presented in uncertainty context
- [ ] Check for manufactured proof signals
- [ ] Score: _____ / 100
- [ ] Proof type: _________________

**RECIPROCITY PRINCIPLE**
- [ ] Search for "give first" signals (free trial, free sample, money-back guarantee)
- [ ] Search for explicit obligation language ("You owe us," "In return")
- [ ] Score: _____ / 100
- [ ] Obligation intensity: _________________

**COMMITMENT/CONSISTENCY PRINCIPLE**
- [ ] Look for small initial asks (signup, quiz, registration)
- [ ] Look for escalation language ("Next step," "Then you can")
- [ ] Check if public commitment requested
- [ ] Check if written commitment required
- [ ] Score: _____ / 100
- [ ] Escalation pattern present: Yes / No

**SCARCITY PRINCIPLE**
- [ ] Search for limitation language (Limited, Rare, Exclusive, Only)
- [ ] Search for competition language (High demand, Quickly selling, Others getting)
- [ ] Search for destruction language (We'll burn, Never again, Going away forever)
- [ ] Search for urgency language (Hurry, Deadline, Today only)
- [ ] Score: _____ / 100
- [ ] Strongest mechanism: _________________

**COMPOSITE PSYCHOLOGICAL SCORE:** Average of all principles = _____ / 100

---

### Advanced Frameworks Audit

**COGNITIVE LOAD TARGETING**
- [ ] Identify complexity signals (Technical, Multi-layered, Comprehensive)
- [ ] Identify time pressure signals (Hurry, Limited time, Urgent)
- [ ] Identify distraction signals (Also, Additionally, By the way)
- [ ] Score: _____ / 100
- [ ] System 1 activation likely: Yes / No

**DECISION FATIGUE APPLICATION**
- [ ] Count decision multiplication (Choose from, Select which, Customize)
- [ ] Count sequential asks (First, Then, Next, Also)
- [ ] Check for fatigue positioning (Final ask at end = leverages depletion)
- [ ] Score: _____ / 100
- [ ] Decisions required before big ask: _____ decisions

**INOCULATION THEORY APPLICATION**
- [ ] Identify objection introductions (You might think, Some say, Critics argue)
- [ ] Identify validation language (That's fair, Good point, Valid concern)
- [ ] Identify refutation language (But here's what, However, Actually)
- [ ] Count complete inoculation cycles (objection + validate + refute)
- [ ] Score: _____ / 100
- [ ] Sophistication level: _________________

**ENVIRONMENTAL PRIMING**
- [ ] Identify location priming (At home, In person, Privately)
- [ ] Identify temporal optimization (Morning, Evening, Specific time)
- [ ] Identify sequence optimization (First, Then, Step 1)
- [ ] Identify social context signals (With friends, In public, Alone)
- [ ] Score: _____ / 100
- [ ] Priming channels deployed: _____ channels

**COMPOSITE ADVANCED SCORE:** Average of frameworks = _____ / 100

---

## SECTION 8: FINAL AUDIT REPORT TEMPLATE

```
═══════════════════════════════════════════════════════════════
COMPREHENSIVE PERSUASION INTENSITY AUDIT REPORT
═══════════════════════════════════════════════════════════════

Brand/Content Audited: _____________________
Date of Audit: _____________________
Auditor: _____________________

─────────────────────────────────────────────────────────────
COMPOSITE SCORES
─────────────────────────────────────────────────────────────

Tactical Stimulus Score (avg of 6): _____ / 100
Psychological Principles Score (avg of 6+): _____ / 100
Advanced Frameworks Score (avg of 7): _____ / 100

OVERALL PERSUASION INTENSITY INDEX: _____ / 100

Persuasion Intensity Level:
[ ] LOW (0-25): Minimal persuasion techniques
[ ] MODERATE (26-50): Some persuasion targeting present
[ ] HIGH (51-75): Sophisticated persuasion techniques
[ ] VERY HIGH (76-100): Intensive persuasion techniques deployed

─────────────────────────────────────────────────────────────
DETAILED STIMULUS BREAKDOWN
─────────────────────────────────────────────────────────────

STIMULUS 1 - PERSONAL (Self-centered targeting): _____ / 100
Key signals: _________________________________
Risk: [ ] Low [ ] Medium [ ] High

STIMULUS 2 - CONTRASTABLE (Binary framing): _____ / 100
Key signals: _________________________________
Risk: [ ] Low [ ] Medium [ ] High

STIMULUS 3 - TANGIBLE (Material specificity): _____ / 100
Key signals: _________________________________
Risk: [ ] Low [ ] Medium [ ] High

STIMULUS 4 - MEMORABLE (U-curve structure): _____ / 100
Key signals: _________________________________
Risk: [ ] Low [ ] Medium [ ] High

STIMULUS 5 - VISUAL (Anti-aesthetic): _____ / 100
Key signals: _________________________________
Risk: [ ] Low [ ] Medium [ ] High

STIMULUS 6 - EMOTIONAL (Fear→Relief arc): _____ / 100
Key signals: _________________________________
Risk: [ ] Low [ ] Medium [ ] High

─────────────────────────────────────────────────────────────
PSYCHOLOGICAL PRINCIPLES DETECTED
─────────────────────────────────────────────────────────────

[ ] Authority (Credentials/titles)
    Intensity: _____ / 100
    Details: _________________________________

[ ] Social Proof (Consensus/peer behavior)
    Intensity: _____ / 100
    Details: _________________________________

[ ] Reciprocity (Give-first obligation)
    Intensity: _____ / 100
    Details: _________________________________

[ ] Commitment/Consistency (Escalation)
    Intensity: _____ / 100
    Details: _________________________________

[ ] Scarcity (Limitation/urgency)
    Intensity: _____ / 100
    Details: _________________________________

─────────────────────────────────────────────────────────────
ADVANCED TACTICS DETECTED
─────────────────────────────────────────────────────────────

[ ] Cognitive Load Targeting: _____ / 100
[ ] Decision Fatigue Application: _____ / 100
[ ] Inoculation Theory: _____ / 100
[ ] Environmental Priming: _____ / 100
[ ] Authority Infiltration: _____ / 100
[ ] Fee Architecture: _____ / 100
[ ] Manufactured Reality: _____ / 100

─────────────────────────────────────────────────────────────
RED FLAGS & CRITICAL FINDINGS
─────────────────────────────────────────────────────────────

CRITICAL (Score > 75 on any dimension):
_________________________________

HIGH CONCERN (Score 51-75):
_________________________________

MODERATE CONCERN (Score 26-50):
_________________________________

─────────────────────────────────────────────────────────────
VULNERABLE AUDIENCES
─────────────────────────────────────────────────────────────

This messaging is most effective for:
[ ] Identity-conscious audiences (fear of being "basic")
[ ] Ideologically-driven audiences (binary thinkers)
[ ] Materialist/artifact-conscious audiences
[ ] High-attention audiences (remember first/last)
[ ] Anti-establishment audiences (distrust polish)
[ ] Emotionally-responsive audiences (pain→relief cycle)
[ ] Status-conscious audiences (exclusivity appeal)

─────────────────────────────────────────────────────────────
RECOMMENDATIONS
─────────────────────────────────────────────────────────────

IMMEDIATE ACTIONS (if score > 70):
1. _________________________________
2. _________________________________
3. _________________________________

REVIEW ITEMS (if score 50-70):
1. _________________________________
2. _________________________________

MONITOR (if score < 50):
1. _________________________________

─────────────────────────────────────────────────────────────
AUDITOR CERTIFICATION
─────────────────────────────────────────────────────────────

This audit was conducted using professional persuasion detection
frameworks extracted from comprehensive research on persuasion tactics.

Auditor Signature: _________________ Date: _________

═══════════════════════════════════════════════════════════════
```

---

## SECTION 9: COMMON AUDIT SCENARIOS & DECISIONS

### Scenario 1: "It's Just Marketing, Isn't ALL Marketing Influence-Based?"

**Answer:** No. There's a spectrum:

- **0-25 (Ethical):** Clear value proposition, no exclusion tactics, transparent about benefits
  - Example: "Quality water bottles. Durable design. Made in the USA."

- **26-50 (Some Targeting):** Audience-specific messaging without exclusion
  - Example: "For coffee lovers: the perfect thermos keeps drinks hot 12 hours."

- **51-75 (Sophisticated):** Multiple primal stimuli, psychological principles, but not misleading
  - Example: Uses PERSONAL + EMOTIONAL but with truthful claims

- **76-100 (Optimized):** Combines multiple frameworks, leverages vulnerabilities, obscures truth
  - Example: Uses all tactics, creates false scarcity, manufactures objections

---

### Scenario 2: "What if the Company Actually Does Make Things in Portugal?"

**Rule:** Specificity of claims doesn't matter. What matters is whether they're used to influence.

**Check:**
- Is "Made in Portugal" just a fact statement (0 points)
- OR is it positioned to create exclusivity ("Made in a closed Portuguese mill only 300 people knew about") (15 points)

**Example:**
- ❌ "Made in Portugal" mentioned once in specs = 0 points
- ✅ "Made in a Portuguese mill that closed in 2003" = narrative-driven = 25 points

---

### Scenario 3: "The Company Says They're Targeting a Specific Niche"

**Rule:** Niche targeting ≠ intensive persuasion. Exclusion ≠ niche marketing.

**Niche Marketing (LOW score):**
"For runners: we've engineered the perfect running shoe"
- Audience-specific = 0 points for PERSONAL stimulus

**Exclusion Marketing (HIGH score):**
"Not for everyone. If you're a real runner, you'll recognize the reference"
- Creates separation from non-runners = 20+ points

---

### Scenario 4: "Technical Details Seem Legit. Are They Just Being Specific?"

**Check:** Is the specificity used to obscure or to clarify?

- **Clarifying:** "680gsm cotton twill (this is what most t-shirts are made of)" = 10 points
- **Obscuring:** "680gsm enzyme-wash non-GM cotton twill with historical mill reference" = 20 points (specificity used to seem more exclusive)

---

## FINAL AUDITOR CHECKLIST

Before submitting your audit, verify:

- [ ] I searched for EXACT PHRASE MATCHES (not paraphrases)
- [ ] I counted each flagged item with its point value
- [ ] I documented my scoring with evidence
- [ ] I distinguished between legitimate specificity and exclusionary detail
- [ ] I assessed audience vulnerability accurately
- [ ] I identified which tactical combinations are being used
- [ ] I provided specific recommendations for reduction
- [ ] I completed the audit report template fully

---

> **Document version:** 4.0
> **Last updated:** February 2026
> **Total source files consolidated:** 5 (15 + 17 + 24 + 26 + 27)
> **Total detection systems:** 30+ Python classes
> **Total regex patterns:** 100+
> **Purpose:** Machine-readable behavioral science pattern detection for auditing
