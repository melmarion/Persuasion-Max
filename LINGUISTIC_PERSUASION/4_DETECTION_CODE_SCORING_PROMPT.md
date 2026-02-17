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
- 51+: Intensive visual influence

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
- 51+: Intensive emotional appeal (emotional influence pattern)

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

**Why it matters:** Pre-emptive objection handling disarms skepticism before it forms. When done transparently it's legitimate argumentation; when used as an influence technique, it creates false sense of having "already considered" alternatives.

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
- 71-90: VERY HIGH — Aggressive influence campaign, multiple influence vectors
- 91-100: CRITICAL — Full-spectrum influence, likely coordinated

**Red flag triggers (regardless of composite score):**
- Any single stimulus > 80 points
- Emotional cycling detected (fractionation)
- Fake scarcity or fake social proof confirmed
- Susceptibility targeting detected (children, elderly, distressed)
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
- [ ] Check for interface design patterns (confirmshaming, roach motel, fake urgency)
- [ ] Check interface design (if applicable): signup vs. cancel friction
- [ ] Check pricing patterns (anchoring, decoys, drip pricing)
- [ ] Assess susceptibility targeting

#### Post-Audit Assessment
- [ ] Calculate composite score
- [ ] Classify intensity level
- [ ] Document specific red flags
- [ ] Note technique stacking / synergies
- [ ] Assess regulatory compliance implications
- [ ] Generate findings report

#### Common Audit Scenarios & Decision Rules

**Scenario 1: High emotional + low tangible**
→ Content relies on affect rather than substance. Elevated intensity of influence.

**Scenario 2: High authority + low verifiability**
→ Manufactured authority pattern. Flag for investigation.

**Scenario 3: High scarcity + resets detected**
→ Fake scarcity confirmed. Score as high-intensity influence regardless of other factors.

**Scenario 4: Progressive commitment + late-stage cost reveal**
→ Classic foot-in-the-door with decision fatigue intensity. Flag as interface design pattern.

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

### 1.8 Detailed Auditor Reference — Exact Language Patterns & Scoring (from Professional Auditor Manual)

#### STIMULUS 1: PERSONAL — Detailed Detection Criteria

Content that makes the audience feel separated from the masses, isolated from "normal" people, or part of an exclusive group.

**EXCLUSION LANGUAGE - Flag these EXACT phrases (20 points each):**
```
"Not for everyone"           → EXACT MATCH = 20 points
"If you know, you know"      → EXACT MATCH = 20 points
"For those who recognize"    → EXACT MATCH = 20 points
"For the 300 people who"     → EXACT MATCH = 20 points
"You'll be illegible to the algorithm"  → EXACT MATCH = 20 points
```

**VARIATIONS ON EXCLUSION (15 points each):**
- "For the initiated" / "For insiders" / "For those in the know"
- "Not your typical..." / "Unlike mainstream..." / "Against the grain"
- "We're not for you if..." [followed by common characteristic]
- "Only [small number] people will understand this"
- "If you recognize" = EXCLUSION VARIANT (15 points)

**STATUS THREAT LANGUAGE - Flag these (30 points each):**
```
"You're wearing what the algorithm thinks you like"
→ EXACT MATCH = 30 points (explicitly threatens status)

"Your references are being sold back to you"
→ EXACT MATCH = 30 points (threatens intellectual autonomy)

"Fear of being basic"
→ EXACT MATCH = 30 points (directly addresses status anxiety)

"You're still too visible"
→ EXACT MATCH = 30 points (threatens desire for obscurity)
```

**TRIBAL SAFETY SIGNALS - Flag these (25 points each):**
```
"We understand the references you understand"
→ EXACT MATCH = 25 points (promises in-group recognition)

"Silent mutual recognition"
→ EXACT MATCH = 25 points (tribal bonding signal)

"Pre-algorithmic feeling"
→ EXACT MATCH = 25 points (promises authenticity)

"Obscurity signals"
→ EXACT MATCH = 25 points (promises hiddenness = safety)
```

**Red Flag Example (Score = 85):**
```
Text: "Not for everyone. If you know, you know. For those who
       recognize the reference. You're wearing what the algorithm
       thinks you like. We understand the references you understand.
       Silent mutual recognition among our people."

BREAKDOWN:
- "Not for everyone" (20) + "If you know, you know" (20) = 40
- "You're wearing what the algorithm thinks" (30) = 30
- "We understand the references you understand" (25) = 25
- "Silent mutual recognition" (25) = 25
TOTAL = 120 (capped at 100) = HIGH PERSONAL STIMULUS
```

#### STIMULUS 2: CONTRASTABLE — Detailed Detection Criteria

**PRIMARY BINARY PAIRS - Flag these (30 points each if BOTH sides mentioned):**
```
PAIR 1: Mass-produced ↔ Artifact
- Points: 30 if both present, 15 if only one side

PAIR 2: Algorithmic ↔ Authored
- Points: 30 if both present, 15 if only one side

PAIR 3: Visible ↔ Coded
- Points: 30 if both present, 15 if only one side

PAIR 4: Commercial ↔ Authentic
- Points: 30 if both present, 15 if only one side
```

**Example Audit Case (Score = 65 = STRONG):**
```
Text: "While they buy logos, you buy language.
       Not made by algorithm, made by intention.
       Unlike mainstream brands, we create evidence.
       Mass-produced or artifact? We make artifacts."

BREAKDOWN:
- "While they...you" (contrast marker, 10)
- "logos" vs "language" (partial PAIR, 15)
- "Not made by algorithm, made by intention" (PAIR 2, 30)
- "Unlike mainstream" (contrast marker, 10)
- Explicit artifact positioning (15)
TOTAL = 80 → Capped at 75 = STRONG CONTRASTABLE STIMULUS
```

**Common Mistakes:**
- Offering multiple options ("Choose from styles A, B, or C") = NOT binary
- Using spectrum language = NOT binary

#### STIMULUS 3: TANGIBLE — Detailed Detection Criteria

**MATERIAL WEIGHT SPECIFICATIONS - Flag these (20 points each):**
```
"680gsm cotton"        → EXACT SPECIFICATION (20 points)
"200gsm" [any fabric]  → EXACT WEIGHT (20 points)
"Heavyweight"          → VAGUE - only 5 points
"Premium quality"      → ABSTRACT - SUBTRACT 5 points
"Heavy-weight twill"   → SOMEWHAT SPECIFIC (10 points)
```

**PRODUCTION LOCATION - Flag these (20 points each):**
```
"Made in Portugal"                           → SPECIFIC (20 points)
"Manufactured in a closed Portuguese mill"   → HIGHLY SPECIFIC (25 points)
"Made in a factory that closed in 2003"      → NARRATIVE DETAIL (25 points)
"Made in Europe"    → VAGUE - only 10 points
"Made locally"      → VAGUE - only 8 points
```

**DECAY/MATERIAL CHANGE - Flag these (20 points each):**
```
"Fades to gray in 6 months"           → SPECIFIC TIMELINE (20 points)
"Shrinks 2% after first soak"         → SPECIFIC MEASUREMENT (20 points)
"Dye bleeds onto skin in heat"        → SPECIFIC PHENOMENON (20 points)
```

**SENSORY DETAILS - Flag these (15 points each):**
```
"Smells like zinc and old rain"       → SPECIFIC SCENT (15 points)
"Texture of aged linen"               → VAGUE TEXTURE (5 points)
```

**PRODUCTION ARTIFACTS/IMPERFECTIONS - Flag these (15 points each):**
```
"Uneven dye"                          → SPECIFIC IMPERFECTION (15 points)
"Visible seams"                       → SPECIFIC ARTIFACT (15 points)
"Not identical—each is unique"        → VARIATION DETAIL (12 points)
```

**SUBTRACT POINTS for ABSTRACT LANGUAGE (5 points deduction each):**
```
"Premium quality"      "Luxury"              "Elevated basics"
"Timeless style"       "Perfection"          "Excellence"
"Superior"             "World-class"         "Sophisticated"
"Elegant"              "Refined"             "Exquisite"
```

| Score Range | Interpretation | Example |
|-------------|---|---|
| 0-30 | HIGHLY ABSTRACT | "Premium quality, timeless elegance" |
| 31-60 | MIXED | Some specifics + some abstract |
| 61-85 | CONCRETE | Mostly material details, few abstractions |
| 86-100 | EXTREMELY TANGIBLE | Pure technical specs, no aspirational language |

**Example Audit Case (Score = 72 = CONCRETE):**
```
Text: "680gsm cotton twill. Enzyme-washed. Shrinks 2% after first
       soak. Dye bleeds onto skin in heat. Smells like zinc and
       old rain. Made in a Portuguese mill that closed in 2003.
       Fades to gray in 6 months. Each is unique."

BREAKDOWN:
680gsm (20) + enzyme-washed (5) + shrinks 2% (20) +
dye bleeds (20) + smells like zinc (15) + Portuguese mill (20) +
fades 6 months (20) + unique variations (12) = 132
Capped at 100, subtract any abstract language = 72
TOTAL = 72 (CONCRETE MESSAGING)
```

#### STIMULUS 4: MEMORABLE — Detailed Detection Criteria (U-Curve Structure)

**OPENING STRENGTH - Flag these OPENING LINES (20 points each):**
```
"Archive 01"                          → System signal (20 points)
"If you recognize the reference"      → Cryptic opening (20 points)
"We don't have a story"               → Unexpected statement (20 points)
```

**CLOSING STRENGTH - Flag these FINAL STATEMENTS (20 points each):**
```
"Or you were already"                 → Unresolved (20 points)
"The rest is up to you"               → Gap left for completion (20 points)
"If you've found this, you were looking for it"  → Questioning close (20 points)
```

**MIDDLE WEAKNESS - Deduct points:**
```
"Also"              → Filler word (-5 points)
"Moreover"          → Filler word (-5 points)
"Choose from options"  → Removes focus (-8 points)
"And we also..."    → Dilutes message (-10 points)
```

| Score Range | Interpretation | Example |
|-------------|---|---|
| 0-30 | NO STRUCTURAL EMPHASIS | Even information distribution |
| 31-60 | SUBTLE EMPHASIS | Some beginning/end focus |
| 61-80 | CLEAR EMPHASIS | Strong opening/closing, sparse middle |
| 81-100 | STRONG EMPHASIS | High contrast opening/closing, minimal middle |

**Example Audit Case (Score = 75 = CLEAR U-CURVE):**
```
Opening:
"Archive 01: Unbranded. Non-returnable. Fades to gray in 6 months."
(20 + 15 + 15 = 50 opening strength)

Middle:
"Also available in other colors. Additionally, we have sizing options.
Choose from variations. And we also ship worldwide."
(Multiple filler signals = -30 total)

Closing:
"Or you were already looking for this."
(20 closing strength)

TOTAL: 50 - 30 + 20 = 40... but U-curve structure itself adds 35
for clear beginning/end emphasis = 75 TOTAL
```

#### AUTHORITY PRINCIPLE — Detailed Detection Criteria

**COMPETENCE SIGNALS (15 points each):**
```
"Doctor" / "Dr."      → Title (15 points)
"Ph.D"                → Advanced degree (15 points)
"Professor"           → Academic title (15 points)
"Licensed"            → License (15 points)
"Harvard" / "Stanford" / "MIT"  → Prestigious institution (20 points)
"30 years experience" → Experience quantified (20 points)
```

**CONFIDENCE MARKERS (10 points each):**
```
"Steady vocal tone"           → Vocal confidence (10 points)
"Unhurried pace"              → Paced delivery (10 points)
"120-150 words per minute"    → Optimal speaking speed (10 points)
"Relaxed shoulders"           → Body language (10 points)
"Slight forward lean"         → Engagement signal (10 points)
```

**THREAT REDUCTION (-20 points each):**
```
"Demanding language"          → Intimidation (-20)
```

**Formula Results:**
- Result < 5 = ~20-30% influence
- Result 5-15 = ~40-50% influence
- Result 15-30 = ~65% influence likelihood

**Example Audit Case (Score = 45 influence level = HIGH):**
```
Text: "Dr. John Smith, Harvard Medical School, 30 years experience.
       Speaks with steady tone, precise language. No aggressive elements."

CALCULATION:
Competence: "Dr." (15) + "Harvard" (20) + "30 years" (20) = 55
Confidence: "steady tone" (10) + "precise language" (10) = 20
Threat: None = 0 (base = 1)
Authority = (55 + 20) / 1 = 75
```

#### SCARCITY PRINCIPLE — Detailed Detection Criteria

**COMPETITION LANGUAGE (20 points each):**
```
"Interest is high"            → Demand signal (20)
"Don't miss out"              → FOMO (20)
"Popular with [group]"        → Desirability (15)
```

**SCARCITY THROUGH FINALITY (30 points each - strongest scarcity mechanism):**
```
"We'll burn the unsold copies"        → Finality statement (30)
"Will be discontinued forever"        → Permanent removal (30)
"Last chance forever"                 → Ultimate deadline (30)
```

**URGENCY LANGUAGE (15 points each):**
```
"Don't delay"     "Time-sensitive"  "Limited time offer"
```

| Score Range | Interpretation | Mechanism |
|-------------|---|---|
| 0-20 | MINIMAL | No scarcity signal |
| 21-40 | MILD | Soft limitations mentioned |
| 41-60 | MODERATE | Clear time limits, demand signals |
| 61-80 | STRONG | Multiple scarcity signals, urgency emphasis |
| 81-100 | VERY HIGH | Finality language + competition + time pressure |

**Example Audit Case (Score = 75 = STRONG):**
```
Text: "Limited edition. Only 50 pieces worldwide. Quickly selling.
       People are buying. Don't miss out. Last chance—we're burning
       the remaining unsold pieces next week."

BREAKDOWN:
"Limited edition" (15) + "Only 50" (15) + "Quickly selling" (20) +
"People are buying" (20) + "Don't miss out" (20) +
"burning unsold pieces" (30) = 120
```

#### DECISION FATIGUE — Detailed Detection Criteria

**DECISION MULTIPLICATION (15 points each):**
```
"Choose from"         → Forces selection (15)
"Select which"        → Decision required (15)
"Pick your"           → Selection needed (15)
"Decide between"      → Choice needed (15)
"Multiple options"    → Multiple decisions (15)
"Configure"           → Setup decisions (20)
"Various choices"     → Multiple decisions (15)
```

**FATIGUE POSITIONING - Big ask at end (25 points):**
```
"Final decision"      → Strategic timing (25)
"Last step"           → Final phase (25)
"One more thing"      → After multiple asks (25)
"Just one more"       → Leverages fatigue (25)
"Final ask"           → End position (25)
"Closing decision"    → Final request (25)
```

**Research Baseline:**
- After 10-15 decisions: analytical capability drops 40%
- Compliance increases 35%

**Example Audit Case (Score = 65 = HIGH INTENSITY):**
```
1. "Choose your size" (Decision 1 = 15 points)
2. "Select color" (Decision 2 = 15 points)
3. "Pick shipping method" (Decision 3 = 15 points)
4. "Choose gift wrap" (Decision 4 = 15 points)
[At this point: 60 points worth of depleted willpower]

Then:
"Just one more thing—upgrade to our premium membership"
(Positioned at end = 25 points)
```

#### ANCHORING EFFECT — Detailed Detection Criteria

**HIGH ANCHORS (40 points each if followed by concessions):**
```
"Normally $500" [then "now $45"]       → Extreme anchor (40)
"Enterprise clients pay $2M annually"  → High anchor (40)
```

**ANCHOR FOLLOWED BY CONCESSION (adds 20 points):**
```
"$500 enterprise package... actually, for your needs: $45"
= 40 (high anchor) + 20 (concession adjustment) = 60
```

**Example Audit Case (Score = 60 = STRONG ANCHORING):**
```
1. "Enterprise clients invest $500K-$2M annually"
   (Extreme anchor, first number = 40 points)

3. "For your specific situation: $45K annual investment"
   (Adjusted down, but still anchored to the $500K-$2M range)

High anchor: $500K-$2M
Concession framing: "actually... for you"
Final offer: $45K (which feels reasonable compared to $500K)

If anchored to $500K: $45K = 9% of anchor (feels like huge discount)
If evaluated independently: $45K = significant investment

ANCHORING SCORE = 60 (STRONG)
```

#### INOCULATION/OBJECTION HANDLING — Detailed Detection Criteria

**PART 2: VALIDATION - Validate the objection (10 points):**
```
"That's a fair point"                  → Validation (10)
"That's a reasonable concern"          → Reasonableness (10)
```

**PART 3: REFUTATION (25 points):**
```
"However, the reality is..."           → Contradiction (25)
"The key difference is..."             → Distinction (25)
"What that overlooks..."               → Gap identification (25)
"Actually, here's the truth..."        → Truth claim (25)
```

**Example Audit Case (Score = 55 base):**
```
Text: "You might be thinking this is too expensive. That's a fair
       concern—premium costs more. But here's what that overlooks:
       the materials cost 3x more, production takes twice as long,
       and it lasts 5x longer than alternatives."

TOTAL = 55 points base
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

        # Check for susceptibility targeting
        vuln_patterns = [
            r'(?i)(senior|elderly|retired|pension|medicare|social security)',
            r'(?i)(kids?|children|teens?|young people|students?)',
            r'(?i)(struggling|desperate|lonely|depressed|anxious|overwhelmed)',
        ]
        for pattern in vuln_patterns:
            if re.search(pattern, text):
                flags.append("SUSCEPTIBILITY_TARGETING: Content may target high-susceptibility populations")
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
    if any("SUSCEPTIBILITY_TARGETING" in f for f in flags):
        return {
            'risk_level': 'CRITICAL',
            'primary_concern': 'Potential targeting of high-susceptibility populations',
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

### 2.5 Quantifiable Scoring Rules (from Machine-Readable Detection System)

#### Stimulus 1: Personal — Quantifiable Rules

**Overview:** This system converts ALL tactics into machine-readable formats:
- Numerical scoring thresholds
- Boolean logic operators
- Algorithmic decision trees

**Exclusion Language Detection (Regex):**
```regex
(?i)(not\s+for\s+everyone|if\s+you\s+know\s+,?\s+you\s+know|for\s+those\s+who\s+recognize|for\s+the\s+\d+\s+people|you'll\s+be\s+illegible)
```

**Status Threat Scoring:**
```
"culturally irrelevant" → 30 points
points = (number_of_exact_matches) × 30
MAX: 100 points (capped)
```

**Machine Decision:**
```
IF points > 60 THEN high_status_threat = TRUE
IF points > 90 THEN extreme_status_threat = TRUE
```

**Tribal Safety Signals:**
```
"tribal markers" → 25 points
"tribal safety" → 25 points
"pre-algorithmic" → 25 points
"post-commercial" → 25 points

FOR EACH exact_substring_found:
  points += 25
```

**Composite Calculation:**
```
PERSONAL_STIMULUS_SCORE = MIN([
  (exclusion_language_score / 60) × 40,
  (status_threat_score / 90) × 35,
  (tribal_safety_score / 175) × 25
], 100)

intensity:
  = 21-40: "WEAK"
  = 41-60: "MODERATE"
  = 61-80: "STRONG"
  = 81-100: "EXTREME"
```

#### Stimulus 2: Contrastable — Quantifiable Rules

**Detection Algorithm:**
```
TOTAL = min(binary_score, 100)

contrast_markers_count = REGEX_MATCH_COUNT(pattern)
marker_score = contrast_markers_count × 10
MAX = 30 points
```

**Composite Calculation:**
```
CONTRASTABLE_SCORE = MIN([
  (pairs_count / 4) × 50,
  (marker_score / 30) × 30,
  100 - spectrum_penalty
], 100)
```

#### Stimulus 3: Tangible — Quantifiable Rules

**Weight Specifications:**
```
- Match found = 20 points
FOR EACH match:
  tangible_score += 20
```

**Production Location:**
```
IF contains_city_name: +20
IF contains_year_or_date: +5
ELSE: 10
```

**Material Decay:**
```
- With percentage = 20 points
FOR EACH match with timeframe/percentage:
  tangible_score += 20
```

**Production Artifacts:**
```
- Each match = 15 points
```

**Abstract Language Penalty:**
```
"impeccable", "top-tier", "best in class"
abstract_penalty = abstract_count × 5
```

**Composite Calculation:**
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

#### Stimulus 4: Memorable — Quantifiable Rules

**Opening Strength:**
```
opening_score += 20

IF length(opening_section) < 30_chars:
  opening_score += 10 (brevity = memorability)
```

**Closing Strength:**
```regex
(or\s+you\s+were\s+already|you\s+decide|the\s+rest\s+is\s+up\s+to\s+you|never\s+resolve|if\s+you've?\s+found|question\s+mark)
```
```
closing_score += 20
IF closing_line_ends_with_question_mark:
  closing_score += 10
```

**Composite Calculation:**
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

#### Stimulus 5: Visual — Quantifiable Rules

**Anti-Aesthetic Terms (15 points each):**
```
"grainy", "blur", "bad lighting", "accidental crop", "mistakes",
"CCTV", "found footage", "webcam quality"
anti_aesthetic_score = anti_aesthetic_count × 15
```

**No-Models/Styling Terms (15 points each):**
```
"no models", "on hangers", "on the floor", "strangers in background",
"not styled", "no styling"
no_styling_score = no_styling_count × 15
```

**Mood Board Terms (10 points each):**
```
"Brutalist", "90s rave", "film stills", "archive", "unlabeled"
mood_board_score = mood_board_count × 10
```

**Polished Penalty (-10 points each):**
```
polished_penalty = polished_count × 10
```

**Composite Calculation:**
```
VISUAL_SCORE = MIN([
  (anti_aesthetic_score / 60) × 35 +
  (no_styling_score / 30) × 30 +
  (mood_board_score / 40) × 25 -
  (polished_penalty)
], 100)
```

#### Stimulus 6: Emotional — Quantifiable Rules

**Pain Triggers:**
```
"inauthenticity": ["fake", "commercial", "manufactured", "mass-produced", "cookie cutter"]
FOR EACH keyword match:
  pain_score += 15
```

**Relief Signals:**
```
FOR EACH keyword match:
  relief_score += 15
```

**Arc Detection:**
```
IF pain_score > 0 AND relief_score > 0:
  arc_bonus = 25
```

**Composite Calculation:**
```
EMOTIONAL_SCORE = MIN([
  ((pain_score + relief_score) / 2 / 100) × 100 +
  arc_bonus
], 100)
```

#### Authority Principle — Quantifiable Rules

**Credentials:**
```
credentials = [
  "doctor", "dr.", "phd", "expert", "professor",
  "researcher", "scientist", "certified", "licensed",
  "30 years", "industry leader", "award-winning"
]

competence_total = MIN(competence_score, 100)
```

**Confidence (Regex):**
```regex
(steady\s+vocal|unhurried\s+pace|120.*150\s+words|70\%\s+eye\s+contact|relaxed\s+shoulders|slight\s+forward\s+lean|precise\s+language|stillness)
```

**Threat Reduction:**
```
threat_score = threat_count × 20
```

**Authority Formula:**
```
compliance_probability = {
  < 5: "Low (20-30%)",
  5-15: "Moderate (40-50%)",
  15-30: "High (65%+)",
  > 30: "Extreme (65-100%)"
}
```

#### Scarcity Principle — Quantifiable Rules

**Competition Language (Regex):**
```regex
(many\s+want|quickly\s+selling|people.*buying|interest\s+is\s+high|others.*getting|don't\s+miss\s+out)
```

**Scarcity Score Calculation:**
```
limitation_score = REGEX_MATCH_COUNT(limitation_pattern) × 15
urgency_score = REGEX_MATCH_COUNT(urgency_pattern) × 15
```

#### Composite Scoring Algorithm

**Risk Categorization:**
```
0-25: "LOW (Standard messaging)",
26-50: "MODERATE (Some targeting)",
51-75: "HIGH (Sophisticated influence strategy)",
76-100: "EXTREME (Optimized tactics)"
```

### 2.6 JSON Output Format (Detailed)

```json
{
  "audit_id": "unique_identifier",
  "timestamp": "ISO_8601_timestamp",
  "content_hash": "SHA256_hash_of_input",
  "tactical_stimulus": {
    "PERSONAL": {
      "score": 65,
      "intensity": "STRONG"
    },
    "CONTRASTABLE": {
      "score": 48,
      "intensity": "MODERATE"
    },
    "TANGIBLE": {
      "score": 72,
      "intensity": "CONCRETE",
      "abstract_penalty": 15
    },
    "MEMORABLE": {
      "score": 61,
      "opening_strength": 30,
      "closing_strength": 25,
      "u_curve_detected": true
    },
    "VISUAL": {
      "score": 58,
      "polished_penalty": 10
    },
    "EMOTIONAL": {
      "score": 74,
      "pain_score": 45,
      "relief_score": 45,
      "arc_complete": true
    }
  },
  "psychological_principles": {
    "AUTHORITY": {
      "score": 52,
      "formula_result": 13,
      "competence": 40,
      "confidence": 20,
      "compliance_probability": "High (65%+)"
    },
    "SOCIAL_PROOF": {
      "score": 41,
      "consensus_signals": 2,
      "similarity_signals": 1
    },
    "RECIPROCITY": {
      "score": 35,
      "give_first_signals": 2,
      "obligation_language": 1
    },
    "COMMITMENT": {
      "score": 28,
      "small_commitment_present": true,
      "escalation_present": false
    },
    "SCARCITY": {
      "score": 65,
      "strongest_mechanism": "competition"
    }
  },
  "advanced_frameworks": {
    "COGNITIVE_LOAD": {
      "score": 38
    },
    "DECISION_FATIGUE": {
      "score": 42,
      "decision_multiplications": 3,
      "fatigue_positioning": true
    },
    "INOCULATION": {
      "score": 55,
      "complete_inoculation_cycles": 2
    }
  },
  "composite_scores": {
    "tactical_stimulus_average": 63,
    "psychological_principles_average": 44,
    "advanced_frameworks_average": 45,
    "risk_level": "HIGH"
  },
  "machine_flagging_summary": {
    "total_matches_found": 47,
    "high_severity_flags": 5,
    "low_severity_flags": 34
  }
}
```

### 2.7 Python Implementation (MachineReadableDetectionEngine)

```python
import re
import json
from typing import Dict, List, Tuple

class MachineReadableDetectionEngine:
    """Quantifiable influence strategy detection without human interpretation"""

    PERSONAL_EXCLUSION_POINTS = 20
    PERSONAL_STATUS_THREAT_POINTS = 30
    PERSONAL_TRIBAL_SAFETY_POINTS = 25

    def __init__(self):
        self.results = {}

    def detect_personal_stimulus(self, text: str) -> Dict:
        score = 0
        matches = []
        exclusion_pattern = r'(?i)(not\s+for\s+everyone|if\s+you\s+know\s+,?\s+you\s+know|for\s+those\s+who)'
        for match in re.finditer(exclusion_pattern, text):
            score += self.PERSONAL_EXCLUSION_POINTS
            matches.append({
                'keyword': match.group(),
                'points': self.PERSONAL_EXCLUSION_POINTS,
                'position': match.start()
            })

        status_threats = ["being basic", "culturally irrelevant", "algorithmically predictable"]
        for threat in status_threats:
            if threat.lower() in text.lower():
                score += self.PERSONAL_STATUS_THREAT_POINTS
                matches.append({'keyword': threat, 'points': self.PERSONAL_STATUS_THREAT_POINTS})

        final_score = min(score, 100)
        intensity = 'NONE' if final_score == 0 else \
                   'WEAK' if final_score <= 40 else \
                   'MODERATE' if final_score <= 60 else \
                   'STRONG' if final_score <= 80 else \
                   'EXTREME'
        return {'stimulus': 'PERSONAL', 'score': final_score, 'intensity': intensity}

    def detect_scarcity_principle(self, text: str) -> Dict:
        score = 0
        components = {}
        limitation_pattern = r'(?i)(limited\s+edition|only\s+\d+\s+left|scarce|never\s+again)'
        limitation_matches = len(re.findall(limitation_pattern, text))
        components['limitation'] = {'matches': limitation_matches, 'points': limitation_matches * 15}
        score += limitation_matches * 15

        competition_pattern = r'(?i)(many\s+want|quickly\s+selling|others.*getting|don\'t\s+miss\s+out)'
        competition_matches = len(re.findall(competition_pattern, text))
        components['competition'] = {'matches': competition_matches, 'points': competition_matches * 20}
        score += competition_matches * 20

        destruction_pattern = r'(?i)(burn.*unsold|destroyed\s+forever|never\s+be\s+made|last\s+chance\s+forever)'
        destruction_matches = len(re.findall(destruction_pattern, text))
        components['destruction'] = {'matches': destruction_matches, 'points': destruction_matches * 30}
        score += destruction_matches * 30

        return {
            'principle': 'SCARCITY',
            'score': min(score, 100),
            'components': components,
            'strongest_mechanism': max(components, key=lambda k: components[k]['points'])
        }

    def audit(self, content: str) -> Dict:
        personal = self.detect_personal_stimulus(content)
        scarcity = self.detect_scarcity_principle(content)
        return {'personal_stimulus': personal, 'scarcity_principle': scarcity}
```

### 2.8 Decision Trees (Pseudocode Boolean Logic)

```
IF SCARCITY_SCORE > 70 AND DESTRUCTION_SIGNALS > 0:
  THEN immediate_red_flag = TRUE

IF AUTHORITY_SCORE > 50 AND THREAT_SCORE == 0:
  THEN immediate_red_flag = TRUE

IF PERSONAL_SCORE > 50:
  susceptible_audience = "Identity-conscious"

IF CONTRASTABLE_SCORE > 50:
  susceptible_audience += "Ideologically-driven"

IF SCARCITY_SCORE > 60 AND COMPETITION_SIGNALS > 2:
  susceptible_audience += "Status-conscious"

IF COMPOSITE_SCORE <= 25: classification = "LOW_INTENSITY"
ELSE IF COMPOSITE_SCORE <= 50: classification = "MODERATE"
ELSE IF COMPOSITE_SCORE <= 75: classification = "HIGH"
ELSE: classification = "EXTREME"
```

### 2.9 Threshold Lookup Tables

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
- Amazon: $2.5 billion settlement for interface design patterns in Prime enrollment/cancellation
- Adobe: DOJ complaint for cancellation difficulty (roach motel pattern)
- International review: 76% of examined sites use at least one UX pattern
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
    Detects UX patterns and high-intensity interface design.

    Based on FTC enforcement data (2024-2025) and academic
    interface design pattern taxonomies.
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
        Analyze interface for design patterns.

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
    Detects anchoring bias leveraging in pricing and framing.

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

### 3.9 Source Reference: Enhanced Detection Research (Original Implementations)

The following contains the original source implementations with alternate marker lists,
threshold structures, and scoring approaches from the Enhanced Detection Research compilation.

#### 3.9.1 Platform Research (Detailed Findings)

**Key Finding 1: Algorithmic Amplification Confirmed**
A study published in **Science** conducted a 10-day field experiment with 1,256 participants on X during a US presidential campaign:
- Decreasing or increasing exposure to content expressing antidemocratic attitudes and partisan animosity shifted out-party partisan animosity by **more than 2 points on a 100-point feeling thermometer**
- This provides **causal evidence** that algorithmic content exposure directly alters emotional states

**Key Finding 2: Engagement Algorithms Amplify Emotional Content**
Research published in **PNAS Nexus** found:
- Twitter's engagement-based ranking algorithm amplifies **emotionally charged, out-group hostile content**
- Users report this content makes them feel **worse** about their political out-group
- Users do **not prefer** the political tweets selected by the algorithm
- Engagement-based algorithms underperform at satisfying users' stated preferences

**Key Finding 3: Facebook's Emotional Weighting System**
Whistleblower Frances Haugen revealed (2021):
- Facebook's newsfeed algorithm favored material that made people emotional (sad/angry) over material that elicited a "like" **by a factor of 5**
- Angry emoji reactions were weighted **5x higher than likes** (2018)
- This was gradually reduced to **weight 0 by 2020** after internal complaints
- Anger-evoking material disproportionately includes misinformation and high-intensity content

#### 3.9.2 Original Fractionation Detector (Alternate Marker Lists)

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

#### 3.9.3 Original Physiological Detector (Alternate Threshold Structure)

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

#### 3.9.4 Original Interface Design Detector (Alternate Regex Patterns)

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

#### 3.9.5 Original Cialdini Detector (Alternate Signal Structures)

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

    # Social engineering context
    # Research with 642 UK and Arab participants found:
    # - Social Proof and Authority are the most influential principles
    # - Scarcity is least influential but still significant

    # LLM Personalized Persuasion
    # Study of 19 LLMs across 5 model families:
    # - Models adapt persuasive language based on personality cues

    # Deepfake Analysis Framework
    # DEEP FRAME tool developed to analyze deepfakes through Cialdini's lens:
    # - Authority and Social Proof most commonly leveraged

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

        return {
            "principle": "AUTHORITY",
            "manufactured_probability": min(score, 100),
            "flags": flags,
            "deepfake_analysis": "Use DEEP FRAME tool for video/audio verification",
            "framework": "Cialdini's Principles for Deepfake Analysis"
        }
```

#### 3.9.6 Original Cognitive Load Detector (Alternate Implementation)

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

    # Key Findings:
    # - Working memory limited to **7±2 information units**
    # - Maximum processing duration: **~20 seconds**
    # - Better checkout design could increase conversions by **35.26%**
    # - After **10-15 decisions**: analytical capability drops **40%**
    # - Compliance increases **35%** when decision fatigued

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

#### 3.9.7 Original Variable Ratio Reinforcement Detector

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

#### 3.9.8 Original Anchoring Detector (with Classic Examples)

**Classic Anchoring Examples:**

| Example | Anchor | Result |
|---------|--------|--------|
| Williams-Sonoma Bread Maker | Added $429 model | $275 model sales increased significantly |
| Campbell's Soup "Limit 12" | Number 12 | Purchases increased from 3.3 to 7 cans |

**Key findings:**
- **70% of consumers** admit purchasing decisions are influenced by initial price
- Decoy effect shifts consumer choice to higher-priced targeted item
- Anchoring persists even when anchor is clearly irrelevant

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

        return {
            "anchoring_score": min(score, 100),
            "flags": flags,
            "consumer_impact": "70% of consumers influenced by initial price anchor",
            "intensity_concern": "Artificially inflated 'original' prices erode trust when discovered"
        }
```

#### 3.9.9 Original Comprehensive Audit (Master Integration)

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

        return results

    def _calculate_composites(self, detections: Dict) -> Dict:
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
```

---

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

    Covers: authority leveraging, rapport building for influence,
    trust escalation, grooming patterns.
    """

    class TrustInfluenceType(Enum):
        AUTHORITY_CLAIM = "authority_claim"
        RAPPORT_BUILDING = "rapport_building"
        SUSCEPTIBILITY_SHARING = "susceptibility_sharing"
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
        'susceptibility_sharing': [
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
            'susceptibility_sharing',
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
    critical_engagement: float = 0.0  # 0-1 (low = susceptible)
    stress_level: float = 0.0        # 0-1
    state_label: str = ""             # e.g., "susceptible", "engaged", "stressed"

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

### 4.6 High-Susceptibility Population Detection

```python
class SusceptibilityFactorType(Enum):
    AGE_CHILD = "child_developing_cognition"
    AGE_ADOLESCENT = "adolescent_risk_taking"
    AGE_ELDERLY = "elderly_cognitive_decline"
    COGNITIVE_LOAD = "high_cognitive_load"
    EMOTIONAL_STATE = "susceptible_emotional_state"
    SOCIAL_ISOLATION = "isolated_lonely"
    NEURODIVERGENT = "neurodivergent_processing"
    MENTAL_HEALTH = "mental_health_condition"
    DIGITAL_LITERACY = "low_digital_literacy"
    FINANCIAL_STRESS = "financial_susceptibility"

@dataclass
class SusceptibilityProfile:
    """Individual susceptibility assessment"""
    factors: List[SusceptibilityFactorType] = field(default_factory=list)
    overall_susceptibility_score: float = 0.0
    risk_areas: List[str] = field(default_factory=list)
    protective_recommendations: List[str] = field(default_factory=list)
    requires_enhanced_protection: bool = False

class SusceptiblePopulationDetector:
    """
    Detects content/design targeting susceptible populations.

    Covers: children, elderly, neurodivergent individuals,
    those in emotional distress, financially susceptible.
    """

    SUSCEPTIBILITY_PROFILES = {
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
                'peer_pressure_susceptibility',
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
                'social_isolation_susceptibility'
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

    def assess_individual_susceptibility(self, user_profile: Dict) -> Dict:
        """
        Assess individual susceptibility based on profile.

        Args:
            user_profile: Dict with 'age', 'cognitive_indicators',
                         'emotional_state', 'social_connection_score',
                         'digital_literacy_score'
        """
        age = user_profile.get('age', 30)
        factors = []
        overall_score = 0.0

        # Age-based susceptibility
        if age <= 17:
            factors.append('child')
            overall_score += 0.4
        elif age >= 65:
            factors.append('elderly')
            overall_score += 0.3
            # Additional: USC Dornsife 2024 — APOE4 carriers 2x scam susceptibility
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
            'overall_susceptibility_score': round(overall_score, 2),
            'factors': factors,
            'risk_areas': self._identify_risk_areas(factors),
            'protective_recommendations': recommendations,
            'risk_multiplier': self._calculate_multiplier(factors)
        }

    def _identify_risk_areas(self, factors: List[str]) -> List[str]:
        """Identify specific risk areas based on susceptibility factors"""
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
            for profile_name, profile in self.SUSCEPTIBILITY_PROFILES.items():
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
| California | CCPA/CPRA | Interface design patterns in consent, deceptive design | Active | $2,500-$7,500 per violation |
| EU | Digital Services Act | Cancellation harder than signup, interface design patterns, high-intensity design | Active since Feb 2024 | Up to 6% global turnover |
| EU | AI Act | Subliminal influence, leveraging of susceptibilities, social scoring | Phased implementation | Up to 7% global turnover (prohibited practices) |
| EU | GDPR | Deceptive consent, interface design patterns in privacy | Active | Up to 4% global turnover or EUR 20 million |
| Germany | Fair Consumer Contracts Act | No termination button | Active | Varies |

**Influence-to-Regulation Mapping:**

| Influence Type | Applicable Regulations |
|---|---|
| Roach motel | EU DSA, FTC Section 5, Germany Fair Contracts Act |
| Confirmshaming | FTC Section 5, EU DSA |
| Fake urgency | FTC Section 5, EU DSA |
| Hidden costs | ROSCA, CCPA |
| Interface design pattern consent | GDPR, CCPA |
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
                'prohibits': ['subliminal_influence', 'exploitation_of_susceptibilities', 'social_scoring'],
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


### 4.11 Source Reference: Comprehensive Detection Frameworks (Original Implementations)

The following contains original source implementations with alternate class structures,
threshold values, scoring approaches, and research data from the Comprehensive Detection Frameworks.

#### 4.11.1 Multimodal Persuasion Research & Dataclasses


**Audio Influence Techniques:**
- Voice tone affects perceived competence and persuasiveness
- Low-pitched voices perceived as more competent, authoritative (Personality and Social Psychology Bulletin, 2024)
- Falling intonation signals confidence and increases elaboration likelihood
- ASMR triggers (whispering, tapping) activate relaxation responses and reduce critical processing

**Video Editing Patterns:**
- Cut frequency of 2.5-3 seconds creates "attentional synchrony"
- Rapid cuts (5-10 in sequence) followed by calm pacing creates "stimulate → calm → re-engage" cycle
- Chaotic/fast audiovisuals increase attentional scope but DECREASE conscious processing
- Alpha rhythm increases after cuts, indicating reduced analytical engagement

**Color Psychology:**
- Colors influence 85-90% of initial purchase impressions
- Red: Urgency, passion, danger - makes time feel slower, objects heavier
- Blue: Trust, calm - time passes quickly, objects feel lighter
- Yellow: Optimism, attention-grabbing (left brain stimulation)

```python
import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
import re

class AudioInfluenceType(Enum):
    VOICE_PITCH_LOW = "low_pitch_authority"
    VOICE_PITCH_VARIATION = "pitch_influence"
    FALLING_INTONATION = "confidence_signal"
    ASMR_TRIGGERS = "asmr_relaxation"
    URGENCY_TONE = "urgency_pressure"
    WHISPER = "intimacy_whisper"
    BACKGROUND_MUSIC_TEMPO = "tempo_influence"

class VideoInfluenceType(Enum):
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
    influence_types: List[AudioInfluenceType] = field(default_factory=list)
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
    influence_types: List[VideoInfluenceType] = field(default_factory=list)
    risk_score: float = 0.0

#### 4.11.2 Cut Rhythm Analyzer


class CutRhythmAnalyzer:
    """
    Specialized analyzer for video editing rhythm patterns.

    Research basis:
    - Film editing affects alpha rhythm and conscious processing
    - "Stimulate → calm → re-engage" pattern keeps viewers engaged
    - Modern content: 2.5-3 second average shot length
    """

    def __init__(self):
        self.patterns = {
            'commercial': {'avg_shot': 2.0, 'burst_freq': 'high'},
            'documentary': {'avg_shot': 8.0, 'burst_freq': 'low'},
            'social_media': {'avg_shot': 1.5, 'burst_freq': 'very_high'},
            'high_influence': {'avg_shot': 2.5, 'burst_freq': 'strategic'}
        }

    def analyze_rhythm_pattern(self, cut_timestamps: List[float], duration: float) -> Dict:
        """
        Analyze the rhythm pattern of video cuts.

        Returns pattern classification and influence indicators.
        """
        if len(cut_timestamps) < 3:
            return {'pattern': 'minimal', 'influence_score': 0.0}

        intervals = np.diff(cut_timestamps)

        analysis = {
            'avg_interval': float(np.mean(intervals)),
            'std_interval': float(np.std(intervals)),
            'min_interval': float(np.min(intervals)),
            'max_interval': float(np.max(intervals)),
            'cuts_per_minute': len(cut_timestamps) / duration * 60,
            'pattern_type': '',
            'influence_indicators': [],
            'influence_score': 0.0
        }

        # Detect "stimulate → calm → re-engage" pattern
        # Look for alternating fast/slow sequences
        window_size = 5
        if len(intervals) >= window_size * 2:
            window_means = [
                np.mean(intervals[i:i+window_size])
                for i in range(0, len(intervals) - window_size, window_size)
            ]

            # Check for significant variance between windows (pattern switching)
            if len(window_means) >= 2:
                window_variance = np.var(window_means)
                if window_variance > 2.0:  # High variance = intentional rhythm influence
                    analysis['influence_indicators'].append('RHYTHM_INFLUENCE')
                    analysis['influence_score'] += 0.4

        # Detect reduced-vigilance regularity (very consistent rhythm)
        cv = analysis['std_interval'] / analysis['avg_interval'] if analysis['avg_interval'] > 0 else 0
        if cv < 0.2:  # Very consistent timing
            analysis['influence_indicators'].append('REDUCED_VIGILANCE_REGULARITY')
            analysis['influence_score'] += 0.3

        # Detect acceleration patterns (building urgency)
        if len(intervals) >= 10:
            first_half = np.mean(intervals[:len(intervals)//2])
            second_half = np.mean(intervals[len(intervals)//2:])

            if second_half < first_half * 0.7:  # 30%+ acceleration
                analysis['influence_indicators'].append('URGENCY_ACCELERATION')
                analysis['influence_score'] += 0.4

        # Classify pattern type
        if analysis['avg_interval'] < 2.0:
            analysis['pattern_type'] = 'high_intensity'
        elif analysis['avg_interval'] < 4.0:
            analysis['pattern_type'] = 'commercial'
        elif analysis['avg_interval'] < 8.0:
            analysis['pattern_type'] = 'moderate'
        else:
            analysis['pattern_type'] = 'slow_pace'

        analysis['influence_score'] = min(1.0, analysis['influence_score'])

        return analysis
```

#### 4.11.3 Social Network Dynamics (Cascade Effects, Bot Detection)


## 2. SOCIAL NETWORK DYNAMICS

### Research Findings

**Cascade Effects (2024-2025):**
- Misinformation follows 4 phases: introduction, acceleration, saturation, stabilization
- Confirmation bias + algorithmic personalization creates echo chambers
- Homogeneity is the primary driver of content diffusion
- Temporal graph analysis shows community evolution during cascades

**Bot Networks:**
- 50%+ of internet traffic is now automated bots (2024)
- 76% detection failure rate for advanced AI bots
- Bot farms use real phones with SIM cards to evade detection
- AI swarms coordinate and adapt tactics in real-time

**Emotional Contagion:**
- Negative posts evoke more attention and are more persistent
- 4.34% over-exposure to negative content precedes negative posting
- Massive-scale emotional influence is technically feasible

```python
@dataclass
class CascadeMetrics:
    """Metrics for information cascade analysis"""
    reach: int = 0
    depth: int = 0
    velocity: float = 0.0  # Shares per hour
    homogeneity_score: float = 0.0
    bot_participation_rate: float = 0.0
    phase: str = ""  # introduction, acceleration, saturation, stabilization
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
    Detects influence patterns in social network dynamics.

    Research basis:
    - Springer 2025: Cascading falsehoods mapping
    - Nature 2026: Temporal graph analysis of fake news cascades
    - Frontiers 2025: Multi-scenario misinformation modeling
    - NATO StratCom 2024: Social media influence for sale
    """

    def __init__(self):
        # Thresholds based on research
        self.thresholds = {
            'bot_posting_regularity': 0.95,  # >95% regular = suspicious
            'engagement_ratio_low': 0.001,  # Very low engagement = fake followers
            'engagement_ratio_high': 0.5,  # Very high = coordinated
            'cascade_velocity_viral': 1000,  # Shares per hour
            'homogeneity_echo_chamber': 0.8,  # >80% similar = echo chamber
            'coordination_window': 60,  # Seconds - posts within this = coordinated
        }

        # Bot behavior patterns
        self.bot_indicators = {
            'perfect_timing': 0.3,  # Posts at exact intervals
            'no_typos': 0.1,  # Never makes mistakes
            'rapid_response': 0.2,  # Responds within seconds
            'template_content': 0.3,  # Repetitive phrasing
            'unusual_hours': 0.2,  # Active 24/7
            'network_clustering': 0.3,  # Connected mainly to other bots
        }


#### 4.11.4 Viral Spread Analysis & Bot Detection Code

```python

    def _determine_cascade_phase(self, sorted_posts: List[Dict]) -> str:
        """
        Determine cascade phase based on velocity patterns.

        Phases from research:
        - Introduction: Initial slow spread
        - Acceleration: Rapid growth
        - Saturation: Peak reached
        - Stabilization: Decline to baseline
        """
        if len(sorted_posts) < 10:
            return "introduction"

        # Divide into quarters and calculate velocity for each
        quarter_size = len(sorted_posts) // 4
        velocities = []

        for i in range(4):
            start_idx = i * quarter_size
            end_idx = (i + 1) * quarter_size if i < 3 else len(sorted_posts)
            quarter = sorted_posts[start_idx:end_idx]

            if len(quarter) >= 2:
                time_span = quarter[-1]['timestamp'] - quarter[0]['timestamp']
                if time_span > 0:
                    velocities.append(len(quarter) / (time_span / 3600))
                else:
                    velocities.append(0)

        if len(velocities) < 4:
            return "introduction"

        # Analyze velocity pattern
        if velocities[1] > velocities[0] * 1.5:
            if velocities[2] < velocities[1]:
                if velocities[3] < velocities[2]:
                    return "stabilization"
                return "saturation"
            return "acceleration"

        return "introduction"

    def _calculate_content_homogeneity(self, posts: List[Dict]) -> float:
        """Calculate how similar the content is across posts"""
        if len(posts) < 2:
            return 0.0

        contents = [p.get('content', '') for p in posts if p.get('content')]
        if len(contents) < 2:
            return 0.0

        # Simple word overlap calculation
        word_sets = [set(c.lower().split()) for c in contents]

        total_similarity = 0
        comparisons = 0

        for i in range(len(word_sets)):
            for j in range(i + 1, len(word_sets)):
                if word_sets[i] and word_sets[j]:
                    intersection = len(word_sets[i] & word_sets[j])
                    union = len(word_sets[i] | word_sets[j])
                    if union > 0:
                        total_similarity += intersection / union
                        comparisons += 1

        return total_similarity / comparisons if comparisons > 0 else 0.0

    def _estimate_bot_participation(self, posts: List[Dict]) -> float:
        """Estimate the percentage of posts from likely bots"""
        if not posts:
            return 0.0

        suspicious_posts = 0

        # Group posts by author
        author_posts = {}
        for post in posts:
            author = post['author_id']
            if author not in author_posts:
                author_posts[author] = []
            author_posts[author].append(post)

        for author, author_post_list in author_posts.items():
            suspicion = 0.0

            # Check posting regularity
            if len(author_post_list) >= 3:
                timestamps = sorted([p['timestamp'] for p in author_post_list])
                intervals = np.diff(timestamps)

                if len(intervals) >= 2:
                    cv = np.std(intervals) / np.mean(intervals) if np.mean(intervals) > 0 else 0
                    if cv < 0.1:  # Very regular posting
                        suspicion += self.bot_indicators['perfect_timing']

            # Check for rapid responses
            for post in author_post_list:
                if post.get('parent_id'):
                    # Find parent timestamp
                    parent = next((p for p in posts if p['id'] == post['parent_id']), None)
                    if parent:
                        response_time = post['timestamp'] - parent['timestamp']
                        if response_time < 5:  # Less than 5 seconds
                            suspicion += self.bot_indicators['rapid_response']
                            break

            if suspicion > 0.3:
                suspicious_posts += len(author_post_list)

        return suspicious_posts / len(posts) if posts else 0.0

    def detect_coordinated_behavior(self, posts: List[Dict]) -> Dict:
        """
        Detect coordinated inauthentic behavior patterns.

        Research: Meta's "coordinated inauthentic behavior" detection
        """
        coordination_analysis = {
            'coordinated_clusters': [],
```

#### 4.11.5 Emotional Contagion Detector

```python
class EmotionalContagionDetector:
    """
    Detects emotional contagion patterns in social media content.

    Research basis:
    - PNAS Facebook study: Emotional contagion at massive scale
    - 2024 research: Negative posts more persistent and contagious
    - 4.34% over-exposure to negative content precedes negative posting
    """

    EMOTION_KEYWORDS = {
        'anger': ['angry', 'furious', 'outraged', 'hate', 'disgusted', 'infuriated'],
        'fear': ['scared', 'afraid', 'terrified', 'worried', 'anxious', 'panic'],
        'sadness': ['sad', 'depressed', 'hopeless', 'miserable', 'devastated'],
        'joy': ['happy', 'excited', 'thrilled', 'delighted', 'ecstatic', 'amazing'],
        'surprise': ['shocked', 'stunned', 'amazed', 'unbelievable', 'wow'],
        'disgust': ['disgusting', 'gross', 'revolting', 'sickening', 'appalling']
    }

    def __init__(self):
        self.negative_emotions = ['anger', 'fear', 'sadness', 'disgust']
        self.positive_emotions = ['joy', 'surprise']

    def analyze_emotional_content(self, posts: List[Dict]) -> Dict:
        """Analyze emotional content distribution and patterns"""
        analysis = {
            'emotion_distribution': {},
            'negativity_ratio': 0.0,
            'emotional_intensity': 0.0,
            'contagion_risk_score': 0.0,
            'influence_indicators': []
        }

        emotion_counts = {emotion: 0 for emotion in self.EMOTION_KEYWORDS}
        total_emotional_posts = 0

        for post in posts:
            content = post.get('content', '').lower()
            post_emotions = []

            for emotion, keywords in self.EMOTION_KEYWORDS.items():
                if any(kw in content for kw in keywords):
                    emotion_counts[emotion] += 1
                    post_emotions.append(emotion)

            if post_emotions:
                total_emotional_posts += 1

        if total_emotional_posts > 0:
            analysis['emotion_distribution'] = {
                emotion: count / total_emotional_posts
                for emotion, count in emotion_counts.items()
            }

            # Calculate negativity ratio
            negative_count = sum(emotion_counts[e] for e in self.negative_emotions)
            positive_count = sum(emotion_counts[e] for e in self.positive_emotions)
            total = negative_count + positive_count

            if total > 0:
                analysis['negativity_ratio'] = negative_count / total

            # Emotional intensity (proportion of posts with strong emotion)
            analysis['emotional_intensity'] = total_emotional_posts / len(posts)

            # Contagion risk assessment
            # High negativity + high intensity = high contagion risk
            analysis['contagion_risk_score'] = (
                analysis['negativity_ratio'] * 0.5 +
                analysis['emotional_intensity'] * 0.3 +
                (emotion_counts['anger'] / total_emotional_posts) * 0.2  # Anger most contagious
            )

            # Detect influence patterns
            if analysis['negativity_ratio'] > 0.7:
                analysis['influence_indicators'].append('HIGH_NEGATIVITY_BIAS')

            if emotion_counts['anger'] > emotion_counts['fear'] * 2:
                analysis['influence_indicators'].append('ANGER_AMPLIFICATION')

            # Check for emotional sequencing (fractionation)
            if self._detect_emotional_cycling(posts):
                analysis['influence_indicators'].append('EMOTIONAL_CYCLING_DETECTED')
                analysis['contagion_risk_score'] += 0.2

        analysis['contagion_risk_score'] = min(1.0, analysis['contagion_risk_score'])

        return analysis

    def _detect_emotional_cycling(self, posts: List[Dict]) -> bool:
        """Detect rapid emotional shifts (fractionation pattern)"""
        if len(posts) < 5:
            return False

        emotions_sequence = []

        for post in posts:
            content = post.get('content', '').lower()
            dominant_emotion = None

            for emotion, keywords in self.EMOTION_KEYWORDS.items():
                if any(kw in content for kw in keywords):
                    dominant_emotion = emotion
                    break

            if dominant_emotion:
                valence = 'negative' if dominant_emotion in self.negative_emotions else 'positive'
                emotions_sequence.append(valence)

        # Count valence switches
        switches = 0
        for i in range(1, len(emotions_sequence)):
            if emotions_sequence[i] != emotions_sequence[i-1]:
                switches += 1

        # High switch rate = emotional sequencing
        switch_rate = switches / len(emotions_sequence) if emotions_sequence else 0

        return switch_rate > 0.4  # More than 40% switches


class EchoChAmberDetector:
    """
    Detects echo chamber formation and filter bubble effects.

    Research basis:
    - PNAS: Polarized information ecosystems reorganize networks via cascades
    - 2024: Homogeneity is preferential driver for content diffusion
    """

    def analyze_information_ecosystem(self, user_feed: List[Dict], network_data: Dict) -> Dict:
        """
        Analyze user's information ecosystem for echo chamber characteristics.

        Expected formats:
        user_feed: [{'content': str, 'source': str, 'stance': str, 'timestamp': float}]
        network_data: {'connections': [str], 'interaction_counts': {str: int}}
        """
        analysis = {
            'viewpoint_diversity': 0.0,
            'source_diversity': 0.0,
            'echo_chamber_score': 0.0,
            'filter_bubble_indicators': [],
            'exposure_bias': {}
        }

        if not user_feed:
            return analysis

        # Analyze viewpoint diversity
        stances = [item.get('stance') for item in user_feed if item.get('stance')]
        if stances:
            unique_stances = set(stances)
            stance_counts = {s: stances.count(s) for s in unique_stances}

            # Shannon entropy for diversity
            total = len(stances)
            entropy = 0
            for count in stance_counts.values():
                if count > 0:
                    p = count / total
                    entropy -= p * np.log2(p)

            # Normalize to 0-1 (max entropy = log2(n_stances))
            max_entropy = np.log2(len(unique_stances)) if len(unique_stances) > 1 else 1
            analysis['viewpoint_diversity'] = entropy / max_entropy if max_entropy > 0 else 0

        # Analyze source diversity
        sources = [item.get('source') for item in user_feed if item.get('source')]
        if sources:
            unique_sources = set(sources)
            analysis['source_diversity'] = len(unique_sources) / len(sources)

        # Calculate echo chamber score (inverse of diversity)
        analysis['echo_chamber_score'] = 1 - (
            analysis['viewpoint_diversity'] * 0.6 +
            analysis['source_diversity'] * 0.4
        )

        # Detect filter bubble indicators
        if analysis['viewpoint_diversity'] < 0.3:
            analysis['filter_bubble_indicators'].append('LOW_VIEWPOINT_DIVERSITY')

        if analysis['source_diversity'] < 0.2:
            analysis['filter_bubble_indicators'].append('SOURCE_CONCENTRATION')

        # Check for algorithmic amplification patterns
        if len(user_feed) >= 20:
            recent = user_feed[-10:]
            older = user_feed[:10]

            recent_diversity = len(set(item.get('stance') for item in recent if item.get('stance')))
            older_diversity = len(set(item.get('stance') for item in older if item.get('stance')))

            if recent_diversity < older_diversity * 0.7:
                analysis['filter_bubble_indicators'].append('NARROWING_EXPOSURE')

        return analysis
```

#### 4.11.6 Trust Architecture & Grooming Detection

```python
@dataclass
class TrustInfluenceIndicator:
    """Indicators of trust-based influence"""
    influence_type: TrustInfluenceType
    confidence: float
    evidence: List[str]
    risk_level: str  # low, medium, high, critical

@dataclass
class GroomingStageAnalysis:
    """Analysis of potential grooming behavior"""
    stage: str  # selection, trust_building, desensitization, application
    indicators: List[str]
    progression_velocity: float  # How fast moving through stages
    risk_score: float

class TrustInfluenceDetector:
    """
    Detects patterns of trust building and application.

    Research basis:
    - ACIG Journal 2024: Trust framework for cybersecurity intensity
    - Wharton 2015: Trust promotes unethical behavior research
    - 2024: Social Engineering 2.0 - 98% of attacks involve influence
    """

    # Patterns that indicate trust influence attempts
    AUTHORITY_SIGNALS = [
        'official', 'authorized', 'verified', 'certified', 'government',
        'security', 'admin', 'support', 'department', 'representative',
        'manager', 'director', 'compliance', 'legal'
    ]

    URGENCY_SIGNALS = [
        'immediately', 'urgent', 'expire', 'deadline', 'last chance',
        'act now', 'limited time', 'don\'t delay', 'critical', 'emergency',
        'within 24 hours', 'account suspended', 'security alert'
    ]

    RECIPROCITY_SIGNALS = [
        'free gift', 'bonus', 'reward', 'exclusive offer', 'selected',
        'lucky winner', 'complimentary', 'no obligation', 'as a thank you'
    ]

    AFFINITY_SIGNALS = [
        'fellow', 'community', 'member', 'family', 'brother', 'sister',
        'alumni', 'veteran', 'colleague', 'neighbor', 'believer'
    ]

    COMMITMENT_ESCALATION_PATTERNS = [
        ('small_request', ['quick survey', 'just one question', 'simple form']),
        ('medium_request', ['share your details', 'verify account', 'provide information']),
        ('large_request', ['wire transfer', 'full access', 'credentials', 'payment'])
    ]

    def __init__(self):
        self.interaction_history = {}

    def analyze_message(self, message: str, sender_info: Dict = None) -> List[TrustInfluenceIndicator]:
        """
        Analyze a message for trust influence patterns.

        Args:
            message: The text content to analyze
            sender_info: Optional sender metadata
        """
        indicators = []
        message_lower = message.lower()

        # Check for authority impersonation
        authority_matches = [sig for sig in self.AUTHORITY_SIGNALS if sig in message_lower]
        if authority_matches:
            confidence = min(1.0, len(authority_matches) * 0.2)
            indicators.append(TrustInfluenceIndicator(
                influence_type=TrustInfluenceType.AUTHORITY_IMPERSONATION,
                confidence=confidence,
                evidence=authority_matches,
                risk_level='high' if confidence > 0.6 else 'medium'
            ))

        # Check for urgency pressure
        urgency_matches = [sig for sig in self.URGENCY_SIGNALS if sig in message_lower]
        if urgency_matches:
            confidence = min(1.0, len(urgency_matches) * 0.25)
            indicators.append(TrustInfluenceIndicator(
                influence_type=TrustInfluenceType.URGENCY_PRESSURE,
                confidence=confidence,
                evidence=urgency_matches,
                risk_level='high' if confidence > 0.5 else 'medium'
            ))

        # Check for reciprocity triggers
        reciprocity_matches = [sig for sig in self.RECIPROCITY_SIGNALS if sig in message_lower]
        if reciprocity_matches:
            confidence = min(1.0, len(reciprocity_matches) * 0.3)
            indicators.append(TrustInfluenceIndicator(
                influence_type=TrustInfluenceType.RECIPROCITY_TRIGGER,
                confidence=confidence,
                evidence=reciprocity_matches,
                risk_level='medium'
            ))

        # Check for affinity influence
        affinity_matches = [sig for sig in self.AFFINITY_SIGNALS if sig in message_lower]
        if affinity_matches:
            confidence = min(1.0, len(affinity_matches) * 0.25)
            indicators.append(TrustInfluenceIndicator(
                influence_type=TrustInfluenceType.AFFINITY_FRAUD,
                confidence=confidence,
                evidence=affinity_matches,
                risk_level='medium'
            ))

        # Combined pattern detection (more significant)
        if len(indicators) >= 2:
            # Multiple influence types = higher risk
            for indicator in indicators:
                indicator.risk_level = 'critical' if indicator.risk_level == 'high' else 'high'

        return indicators

    def analyze_conversation_sequence(self, messages: List[Dict]) -> Dict:
        """
        Analyze a sequence of messages for escalation patterns.

        Expected format: [{'sender': str, 'content': str, 'timestamp': float}]
        """
        analysis = {
            'escalation_detected': False,
            'grooming_indicators': [],
            'trust_building_phase': False,
            'application_phase': False,
            'risk_progression': [],
            'overall_risk_score': 0.0
        }

        if len(messages) < 3:
            return analysis

        # Track request sizes over time
        request_sizes = []

        for msg in messages:
            content_lower = msg.get('content', '').lower()

            # Classify request size
            for size, patterns in self.COMMITMENT_ESCALATION_PATTERNS:
                if any(p in content_lower for p in patterns):
                    request_sizes.append(size)
                    break

        # Check for escalation pattern
        size_order = {'small_request': 1, 'medium_request': 2, 'large_request': 3}

        if len(request_sizes) >= 2:
            # Check if requests are escalating
            escalating = True
            for i in range(1, len(request_sizes)):
                if size_order.get(request_sizes[i], 0) <= size_order.get(request_sizes[i-1], 0):
                    escalating = False
                    break

            if escalating:
                analysis['escalation_detected'] = True
                analysis['grooming_indicators'].append('COMMITMENT_ESCALATION')
                analysis['overall_risk_score'] += 0.4

        # Analyze trust building phase
        early_messages = messages[:len(messages)//2]
        late_messages = messages[len(messages)//2:]

        early_risk = sum(len(self.analyze_message(m.get('content', ''))) for m in early_messages)
        late_risk = sum(len(self.analyze_message(m.get('content', ''))) for m in late_messages)

        if early_risk < late_risk:
            analysis['trust_building_phase'] = True
            analysis['application_phase'] = True
            analysis['grooming_indicators'].append('TRUST_THEN_APPLY_PATTERN')
            analysis['overall_risk_score'] += 0.3

        analysis['overall_risk_score'] = min(1.0, analysis['overall_risk_score'])

        return analysis


class GroomingPatternDetector:
    """
    Detects grooming behavior patterns in online interactions.

    Research basis:
    - Zero Abuse Project 2024: Influence, Grooming, and Gradual Desensitization
    - Research on predictable grooming stages
    """

    GROOMING_STAGES = {
        'selection': {
            'indicators': [
                'personal_questions', 'susceptibility_probing', 'isolation_attempts',
                'compliments_excessive', 'special_attention'
            ],
            'patterns': [
                r'tell me about yourself',
                r'do you have many friends',
                r'are you alone',
                r'you\'re (so |very )?(special|unique|different)',
                r'no one understands you like'
            ]
        },
        'trust_building': {
            'indicators': [
                'shared_secrets', 'exclusive_relationship', 'gift_giving',
                'reliability_demonstration', 'understanding_claims'
            ],
            'patterns': [
                r'just between us',
                r'our (little )?secret',
                r'i\'ll always be here',
                r'you can trust me',
                r'i understand you'
            ]
        },
        'desensitization': {
            'indicators': [
                'boundary_testing', 'normalization', 'gradual_exposure',
                'secrecy_requests', 'guilt_influence'
            ],
            'patterns': [
                r'everyone does',
                r'it\'s (normal|natural)',
                r'don\'t tell anyone',
                r'you (owe|promised) me',
                r'after everything i\'ve done'
            ]
        },
        'application': {
            'indicators': [
                'explicit_requests', 'threats', 'blackmail',
                'isolation_complete', 'control_established'
            ],
            'patterns': [
                r'send me',
                r'if you don\'t',
                r'i\'ll tell everyone',
                r'no one will believe',
                r'you have no choice'
            ]
        }
    }

    def analyze_interaction_sequence(self, interactions: List[Dict]) -> GroomingStageAnalysis:
        """
        Analyze interaction sequence for grooming patterns.

        Expected format: [{'content': str, 'timestamp': float, 'sender': str}]
        """
        stage_scores = {stage: 0.0 for stage in self.GROOMING_STAGES}
        all_indicators = []

        for interaction in interactions:
            content = interaction.get('content', '').lower()

            for stage, stage_data in self.GROOMING_STAGES.items():
                for pattern in stage_data['patterns']:
                    if re.search(pattern, content):
                        stage_scores[stage] += 1
                        all_indicators.append(f"{stage}:{pattern}")
```

#### 4.11.7 Platform-Specific Mechanics (Gamification, Infinite Scroll)

```python
@dataclass
class GamificationAnalysis:
    """Analysis of gamification influence"""
    influence_types: List[GamificationInfluenceType] = field(default_factory=list)
    streak_dependency_score: float = 0.0
    variable_reward_frequency: float = 0.0
    friction_asymmetry: float = 0.0  # signup ease vs cancel difficulty
    overall_influence_score: float = 0.0
    detailed_findings: Dict = field(default_factory=dict)

class PlatformInfluenceDetector:
    """
    Detects influence mechanics in platform/app design.

    Research basis:
    - CHI 2024: "Staying at the Roach Motel" subscription analysis
    - 2024 research on gamification interface design patterns
    - Kahneman's Prospect Theory (loss aversion)
    - Wansink's "bottomless bowl" experiment
    """

    # Streak-related UI patterns
    STREAK_PATTERNS = {
        'visual_elements': ['fire', 'flame', 'chain', 'streak', 'consecutive', 'daily'],
        'loss_framing': ['don\'t lose', 'protect', 'maintain', 'keep alive', 'at risk'],
        'guilt_triggers': ['you\'ll lose', 'streak will end', 'don\'t break', 'miss out']
    }

    # Notification influence patterns
    NOTIFICATION_PATTERNS = {
        'fomo': ['someone just', 'you\'re missing', 'happening now', 'don\'t miss'],
        'false_urgency': ['limited time', 'expiring', 'last chance', 'ending soon'],
        'social_pressure': ['friends are', 'everyone is', 'you\'re falling behind'],
        'curiosity_gap': ['you won\'t believe', 'find out', 'see what', 'discover']
    }

    # Cancellation friction patterns
    CANCELLATION_FRICTION = {
        'required_call': 0.8,  # Must call to cancel
        'long_survey': 0.5,  # Forced feedback before cancel
        'confirmation_typing': 0.6,  # Must type phrase like "CONFIRM"
        'hidden_button': 0.4,  # Cancel button hard to find
        'emotional_influence': 0.7,  # "We'll miss you" guilt
        'multiple_screens': 0.5,  # Many steps to cancel
        'retention_offers': 0.3,  # Discount offers to stay
    }

    def __init__(self):
        self.thresholds = {
            'high_streak_dependency': 0.7,
            'frequent_variable_rewards': 0.5,
            'severe_friction_asymmetry': 0.6
        }

    def analyze_app_interface(self, interface_data: Dict) -> GamificationAnalysis:
        """
        Analyze app/platform interface for influence patterns.

        Expected interface_data:
        {
            'features': List[str],
            'notifications': List[Dict],
            'signup_steps': int,
            'cancel_steps': int,
            'cancel_requirements': List[str],
            'reward_schedule': str,  # 'fixed', 'variable', 'none'
            'ui_elements': List[Dict]
        }
        """
        analysis = GamificationAnalysis()

        # Analyze streak mechanics
        if 'features' in interface_data:
            features_lower = [f.lower() for f in interface_data['features']]

            streak_elements = sum(
                1 for pattern in self.STREAK_PATTERNS['visual_elements']
                if any(pattern in f for f in features_lower)
            )

            loss_framing = sum(
                1 for pattern in self.STREAK_PATTERNS['loss_framing']
                if any(pattern in f for f in features_lower)
            )

            if streak_elements > 0:
                analysis.influence_types.append(GamificationInfluenceType.STREAK_LOSS_AVERSION)
                analysis.streak_dependency_score = min(1.0, (streak_elements + loss_framing * 2) * 0.2)

        # Analyze reward schedule
        if interface_data.get('reward_schedule') == 'variable':
            analysis.influence_types.append(GamificationInfluenceType.VARIABLE_RATIO_REWARD)
            analysis.variable_reward_frequency = 0.7  # High influence potential

        # Analyze friction asymmetry (roach motel)
        signup_steps = interface_data.get('signup_steps', 1)
        cancel_steps = interface_data.get('cancel_steps', 1)

        if cancel_steps > signup_steps:
            analysis.friction_asymmetry = min(1.0, (cancel_steps - signup_steps) / 10)

            if analysis.friction_asymmetry > 0.3:
                analysis.influence_types.append(GamificationInfluenceType.ROACH_MOTEL)

        # Analyze cancellation requirements
        if 'cancel_requirements' in interface_data:
            friction_score = 0
            for req in interface_data['cancel_requirements']:
                req_lower = req.lower()
                for friction_type, score in self.CANCELLATION_FRICTION.items():
                    if friction_type.replace('_', ' ') in req_lower:
                        friction_score += score

            analysis.friction_asymmetry = max(analysis.friction_asymmetry, min(1.0, friction_score))

        # Analyze notifications
        if 'notifications' in interface_data:
            notification_analysis = self._analyze_notifications(interface_data['notifications'])
            analysis.detailed_findings['notifications'] = notification_analysis

            if notification_analysis.get('fomo_count', 0) > 0:
                analysis.influence_types.append(GamificationInfluenceType.FOMO_NOTIFICATION)

        # Check for infinite scroll / autoplay
        if 'features' in interface_data:
            if any('infinite' in f.lower() or 'endless' in f.lower() for f in interface_data['features']):
                analysis.influence_types.append(GamificationInfluenceType.INFINITE_SCROLL)

            if any('autoplay' in f.lower() or 'auto-play' in f.lower() for f in interface_data['features']):
                analysis.influence_types.append(GamificationInfluenceType.AUTOPLAY)

        # Calculate overall influence score
        analysis.overall_influence_score = min(1.0,
            len(analysis.influence_types) * 0.15 +
            analysis.streak_dependency_score * 0.25 +
            analysis.variable_reward_frequency * 0.3 +
            analysis.friction_asymmetry * 0.3
        )

        return analysis

    def _analyze_notifications(self, notifications: List[Dict]) -> Dict:
        """Analyze notification patterns for influence"""
        analysis = {
            'total': len(notifications),
            'fomo_count': 0,
            'false_urgency_count': 0,
            'social_pressure_count': 0,
            'curiosity_gap_count': 0,
            'influence_rate': 0.0
        }

        for notif in notifications:
            content = notif.get('content', '').lower()

            for pattern in self.NOTIFICATION_PATTERNS['fomo']:
                if pattern in content:
                    analysis['fomo_count'] += 1
                    break

            for pattern in self.NOTIFICATION_PATTERNS['false_urgency']:
                if pattern in content:
                    analysis['false_urgency_count'] += 1
                    break

            for pattern in self.NOTIFICATION_PATTERNS['social_pressure']:
                if pattern in content:
                    analysis['social_pressure_count'] += 1
                    break

            for pattern in self.NOTIFICATION_PATTERNS['curiosity_gap']:
                if pattern in content:
                    analysis['curiosity_gap_count'] += 1
                    break

        intensive_count = (
            analysis['fomo_count'] +
            analysis['false_urgency_count'] +
            analysis['social_pressure_count'] +
            analysis['curiosity_gap_count']
        )

        analysis['influence_rate'] = intensive_count / len(notifications) if notifications else 0

        return analysis


class InfiniteScrollDetector:
    """
    Detects infinite scroll and attention capture patterns.

    Research basis:
    - 2024 CHI: Design Frictions on Social Media
    - Wansink's bottomless bowl research
    - Zeigarnik Effect: incomplete tasks remembered better
    """

    def __init__(self):
        self.session_data = []

    def analyze_browsing_session(self, session_data: Dict) -> Dict:
        """
        Analyze browsing session for attention capture patterns.

        Expected session_data:
        {
            'scroll_events': [{'timestamp': float, 'position': float}],
            'content_views': [{'timestamp': float, 'duration': float, 'content_id': str}],
            'session_duration': float,
            'natural_endpoints': int,  # Number of clear stopping points
            'autoplay_triggers': int
        }
        """
        analysis = {
            'scroll_immersion_score': 0.0,
            'time_distortion_indicators': [],
            'stopping_point_deprivation': 0.0,
            'attention_capture_score': 0.0,
            'recommendations': []
        }

        scroll_events = session_data.get('scroll_events', [])
        content_views = session_data.get('content_views', [])
        duration = session_data.get('session_duration', 0)

        if scroll_events:
            # Calculate scroll velocity patterns
            velocities = []
            for i in range(1, len(scroll_events)):
                time_diff = scroll_events[i]['timestamp'] - scroll_events[i-1]['timestamp']
                pos_diff = abs(scroll_events[i]['position'] - scroll_events[i-1]['position'])
                if time_diff > 0:
                    velocities.append(pos_diff / time_diff)

            if velocities:
                # High consistent velocity = mindless scrolling
                avg_velocity = np.mean(velocities)
                velocity_consistency = 1 - (np.std(velocities) / avg_velocity if avg_velocity > 0 else 0)

                if velocity_consistency > 0.7:
                    analysis['scroll_immersion_score'] = velocity_consistency
                    analysis['time_distortion_indicators'].append('CONSISTENT_MINDLESS_SCROLLING')

        # Analyze content view patterns
        if content_views:
            view_durations = [v['duration'] for v in content_views]
            avg_duration = np.mean(view_durations)

            # Short average views = rapid consumption
            if avg_duration < 3:  # Less than 3 seconds per content
                analysis['time_distortion_indicators'].append('RAPID_CONTENT_CONSUMPTION')
                analysis['attention_capture_score'] += 0.3

        # Analyze natural endpoint deprivation
        natural_endpoints = session_data.get('natural_endpoints', 0)
        if duration > 0 and natural_endpoints > 0:
            endpoints_per_minute = natural_endpoints / (duration / 60)

            if endpoints_per_minute < 0.5:  # Less than 1 endpoint per 2 minutes
                analysis['stopping_point_deprivation'] = 1 - (endpoints_per_minute * 2)
                analysis['time_distortion_indicators'].append('NATURAL_STOPPING_POINTS_ABSENT')

        # Check autoplay contribution
        autoplay_triggers = session_data.get('autoplay_triggers', 0)
        if autoplay_triggers > 5:
            analysis['attention_capture_score'] += 0.3
            analysis['time_distortion_indicators'].append('EXCESSIVE_AUTOPLAY')

        # Final score calculation
        analysis['attention_capture_score'] = min(1.0,
            analysis['scroll_immersion_score'] * 0.3 +
            analysis['stopping_point_deprivation'] * 0.4 +
            analysis['attention_capture_score']
        )

        # Generate recommendations
        if analysis['attention_capture_score'] > 0.5:
            analysis['recommendations'].extend([
                'Consider enabling screen time limits',
                'Look for apps with natural stopping points',
                'Disable autoplay features where possible'
            ])

        return analysis
```
```

#### 4.11.8 Physiological Validation Methods

## 5. PHYSIOLOGICAL VALIDATION METHODS

### Research Findings

**Eye Tracking & Pupil Dilation:**
- Pupil dilation indicates cognitive load and emotional arousal
- 15% pupil dilation = reduced critical engagement
- EyeLink detects 0.1% pupil diameter changes
- Guilty knowledge detection: 70% accuracy via pupillary response
- Gaze patterns reveal deception in sender-receiver games

**Blink Rate:**
- Normal: 15-20 blinks/min
- Focused engagement: <10 blinks/min
- Elevated arousal: 30-45 blinks/min

**Skin Conductance (GSR):**
- 2-5 microsiemens = elevated arousal
- Indicates emotional response regardless of valence

**Heart Rate Variability (HRV):**
- <40ms = stress/anger state
- Normal: 50-100ms

```python
@dataclass
class PhysiologicalReading:
    """Single physiological measurement"""
    timestamp: float
    pupil_diameter: float = 0.0  # mm
    blink_rate: float = 0.0  # per minute
    gsr: float = 0.0  # microsiemens
    hrv: float = 0.0  # ms
    gaze_x: float = 0.0
    gaze_y: float = 0.0
    fixation_duration: float = 0.0  # ms

@dataclass
class PhysiologicalState:
    """Interpreted physiological state"""
    arousal_level: float = 0.0  # 0-1
    cognitive_load: float = 0.0  # 0-1
    emotional_valence: float = 0.0  # -1 to 1
    critical_engagement: float = 0.0  # 0-1 (low = susceptible)
    stress_level: float = 0.0  # 0-1
    state_label: str = ""  # e.g., "susceptible", "engaged", "stressed"

class PhysiologicalInfluenceDetector:
    """
    Detects influence effects via physiological signals.

    Research basis:
    - PMC: Technological advancements in Neuromarketing
    - SR Research: Pupillometry research applications
    - PNAS Nexus 2024: Phishing susceptibility and cognition
    - EEG research on video editing effects
    """

    # Thresholds from APPENDIX_RESEARCH_SOURCES.md
    THRESHOLDS = {
        'blink_rate_normal_low': 15,
        'blink_rate_normal_high': 20,
        'blink_rate_focused': 10,  # Below this = high focus
        'blink_rate_aroused': 30,  # Above this = elevated arousal
        'gsr_baseline': 1.0,
        'gsr_elevated': 2.0,  # Above this = aroused
        'gsr_high': 5.0,
        'hrv_stress': 40,  # Below this = stressed
        'hrv_normal_low': 50,
        'hrv_normal_high': 100,
        'pupil_baseline': 1.0,  # Ratio to baseline
        'pupil_reduced_critical': 1.15,  # Above this = reduced critical thinking
    }

    def __init__(self):
        self.baseline_readings = None

    def set_baseline(self, readings: List[PhysiologicalReading]):
        """Establish baseline from calm state readings"""
        if readings:
            self.baseline_readings = {
                'pupil': np.mean([r.pupil_diameter for r in readings]),
                'blink_rate': np.mean([r.blink_rate for r in readings]),
                'gsr': np.mean([r.gsr for r in readings]),
                'hrv': np.mean([r.hrv for r in readings])
            }

    def analyze_reading(self, reading: PhysiologicalReading) -> PhysiologicalState:
        """Analyze single reading against baseline and thresholds"""
        state = PhysiologicalState()

        # Use baseline if available, otherwise use absolute thresholds
        baseline = self.baseline_readings or {
            'pupil': 4.0,  # Average pupil diameter mm
            'blink_rate': 17.5,
            'gsr': 1.0,
            'hrv': 75
        }

        # Pupil dilation analysis
        if baseline['pupil'] > 0:
            pupil_ratio = reading.pupil_diameter / baseline['pupil']

            # High dilation = emotional arousal, potentially reduced critical thinking
            if pupil_ratio > self.THRESHOLDS['pupil_reduced_critical']:
                state.critical_engagement = max(0, 1 - (pupil_ratio - 1) * 2)
                state.arousal_level = min(1.0, (pupil_ratio - 1) * 3)
            else:
                state.critical_engagement = 1.0
                state.arousal_level = max(0, (pupil_ratio - 0.9) * 5)

        # Blink rate analysis
        if reading.blink_rate < self.THRESHOLDS['blink_rate_focused']:
            # Very low blink rate = high focus, potentially reduced-vigilance state
            state.cognitive_load = 0.8
            state.state_label = "hyperfocused"
        elif reading.blink_rate > self.THRESHOLDS['blink_rate_aroused']:
            # High blink rate = arousal, stress, or threat response
            state.arousal_level = min(1.0, state.arousal_level + 0.3)
            state.stress_level = min(1.0, (reading.blink_rate - 30) / 15)
            state.state_label = "aroused"

        # GSR analysis
        if reading.gsr > self.THRESHOLDS['gsr_elevated']:
            state.arousal_level = min(1.0, state.arousal_level +
                (reading.gsr - self.THRESHOLDS['gsr_baseline']) / 4)

            if reading.gsr > self.THRESHOLDS['gsr_high']:
                state.state_label = "highly_aroused"

        # HRV analysis
        if reading.hrv < self.THRESHOLDS['hrv_stress']:
            state.stress_level = min(1.0, state.stress_level +
                (self.THRESHOLDS['hrv_stress'] - reading.hrv) / 40)
            state.state_label = "stressed"

        # Determine susceptibility state
        if state.critical_engagement < 0.5 and state.arousal_level > 0.6:
            state.state_label = "susceptible"

        return state

    def detect_influence_response(
        self,
        pre_exposure: List[PhysiologicalReading],
        during_exposure: List[PhysiologicalReading],
        content_type: str = ""
    ) -> Dict:
        """
        Detect physiological response to potential influence.

        Compares pre-exposure baseline to during-exposure readings.
        """
        analysis = {
            'influence_detected': False,
            'response_type': '',
            'intensity': 0.0,
            'susceptibility_window': [],
            'recovery_needed': False,
            'detailed_changes': {}
        }

        if not pre_exposure or not during_exposure:
            return analysis

        # Calculate baseline
        pre_avg = {
            'pupil': np.mean([r.pupil_diameter for r in pre_exposure]),
            'blink': np.mean([r.blink_rate for r in pre_exposure]),
            'gsr': np.mean([r.gsr for r in pre_exposure]),
            'hrv': np.mean([r.hrv for r in pre_exposure])
        }

        # Calculate during exposure
        during_avg = {
            'pupil': np.mean([r.pupil_diameter for r in during_exposure]),
            'blink': np.mean([r.blink_rate for r in during_exposure]),
            'gsr': np.mean([r.gsr for r in during_exposure]),
            'hrv': np.mean([r.hrv for r in during_exposure])
        }

        # Calculate changes
        changes = {
            'pupil_change': (during_avg['pupil'] - pre_avg['pupil']) / pre_avg['pupil'] if pre_avg['pupil'] > 0 else 0,
            'blink_change': during_avg['blink'] - pre_avg['blink'],
            'gsr_change': during_avg['gsr'] - pre_avg['gsr'],
            'hrv_change': during_avg['hrv'] - pre_avg['hrv']
        }

        analysis['detailed_changes'] = changes

        # Detect influence patterns

        # Pattern 1: Fear/Threat response (dilated pupils, high GSR, low HRV)
        if (changes['pupil_change'] > 0.1 and
            changes['gsr_change'] > 1.0 and
            changes['hrv_change'] < -10):
            analysis['influence_detected'] = True
            analysis['response_type'] = 'fear_threat'
            analysis['intensity'] = min(1.0, changes['gsr_change'] / 3)

        # Pattern 2: Focused engagement (reduced blink, stable pupil)
        elif changes['blink_change'] < -5 and abs(changes['pupil_change']) < 0.05:
            analysis['influence_detected'] = True
            analysis['response_type'] = 'focused_engagement'
            analysis['intensity'] = min(1.0, abs(changes['blink_change']) / 10)

        # Pattern 3: Emotional arousal (high pupil dilation, high GSR)
        elif changes['pupil_change'] > 0.15 and changes['gsr_change'] > 1.5:
            analysis['influence_detected'] = True
            analysis['response_type'] = 'emotional_arousal'
            analysis['intensity'] = min(1.0, changes['pupil_change'] * 3)

        # Pattern 4: Stress/pressure (low HRV, high blink rate, high GSR)
        elif (changes['hrv_change'] < -15 and
              changes['blink_change'] > 10 and
              changes['gsr_change'] > 1.0):
            analysis['influence_detected'] = True
            analysis['response_type'] = 'stress_pressure'
            analysis['intensity'] = min(1.0, abs(changes['hrv_change']) / 30)

        # Identify susceptibility windows
        for i, reading in enumerate(during_exposure):
            state = self.analyze_reading(reading)
            if state.critical_engagement < 0.5:
                analysis['susceptibility_window'].append({
                    'index': i,
                    'timestamp': reading.timestamp,

#### 4.11.9 Eye Tracking & Gaze Analysis

```python

        # Detect influence patterns

        # Pattern 1: Disproportionate CTA attention
        if 'cta_button' in analysis['attention_distribution']:
            cta_attention = analysis['attention_distribution']['cta_button']
            if cta_attention > 0.3:  # More than 30% on CTA
                analysis['influence_indicators'].append('HIGH_CTA_ATTENTION')

        # Pattern 2: Price avoidance (influence redirecting from price)
        if 'price' in analysis['attention_distribution']:
            price_attention = analysis['attention_distribution']['price']
            if price_attention < 0.05:  # Less than 5% on price
                analysis['influence_indicators'].append('PRICE_ATTENTION_SUPPRESSED')

        # Pattern 3: Scanpath analysis (F-pattern vs guided pattern)
        analysis['scanpath_pattern'] = self._classify_scanpath(gaze_data)

        if analysis['scanpath_pattern'] == 'linear_forced':
            analysis['influence_indicators'].append('FORCED_ATTENTION_PATH')

        # Calculate attention capture effectiveness
        cta_regions = [r for r in content_regions if 'cta' in r.lower() or 'button' in r.lower()]
        cta_attention = sum(analysis['attention_distribution'].get(r, 0) for r in cta_regions)

        analysis['attention_capture_effectiveness'] = min(1.0, cta_attention * 2)

        return analysis

    def _classify_scanpath(self, gaze_data: List[Dict]) -> str:
        """Classify the scanpath pattern"""
        if len(gaze_data) < 5:
            return 'insufficient_data'

        # Extract x, y sequences
        xs = [g['x'] for g in gaze_data]
        ys = [g['y'] for g in gaze_data]

        # Check for F-pattern (natural reading)
        # Starts top-left, moves right, drops down, moves right again
        if xs[0] < np.mean(xs) and ys[0] < np.mean(ys):
            horizontal_moves = sum(1 for i in range(1, len(xs)) if xs[i] > xs[i-1])
            if horizontal_moves > len(xs) * 0.4:
                return 'f_pattern_natural'

        # Check for linear forced pattern
        # Very consistent direction, limited exploration
        x_direction = np.sign(np.diff(xs))
        y_direction = np.sign(np.diff(ys))

        if np.std(x_direction) < 0.5 or np.std(y_direction) < 0.5:
            return 'linear_forced'

        # Check for scattered pattern
        if np.std(xs) > np.mean(xs) * 0.5 and np.std(ys) > np.mean(ys) * 0.5:
            return 'scattered'

        return 'mixed'
```
```

#### 4.11.10 High-Susceptibility Population Detection

## 6. HIGH-SUSCEPTIBILITY POPULATION DETECTION

### Research Findings

**Children & Adolescents:**
- 25% of 8-year-olds have experienced online harm (2024)
- 33% of boys 9-12 experienced high-impact online sexual interaction (2024)
- Cannot comprehend persuasive intent of advertising
- Developing prefrontal cortex = limited impulse control

**Elderly:**
- $3.1 billion lost to cyber fraud in 2022 (74% increase from 2021)
- Mild cognitive decline correlates with higher scam susceptibility
- APOE4 gene variant increases phishing susceptibility
- Entorhinal cortex thinning linked to financial intensity
- Social isolation is strongest risk factor

**Neurodivergent:**
- ADHD/Autism more susceptible to narcissistic influence
- Difficulty recognizing intensive social cues
- More susceptible to gaslighting
- Late/undiagnosed individuals especially susceptible
- Low self-esteem from chronic invalidation

```python
class SusceptibilityFactorType(Enum):
    AGE_CHILD = "child_developing_cognition"
    AGE_ADOLESCENT = "adolescent_risk_taking"
    AGE_ELDERLY = "elderly_cognitive_decline"
    COGNITIVE_LOAD = "high_cognitive_load"
    EMOTIONAL_STATE = "susceptible_emotional_state"
    SOCIAL_ISOLATION = "isolated_lonely"
    NEURODIVERGENT = "neurodivergent_processing"
    MENTAL_HEALTH = "mental_health_condition"
    DIGITAL_LITERACY = "low_digital_literacy"
    FINANCIAL_STRESS = "financial_susceptibility"

@dataclass
class SusceptibilityProfile:
    """Individual susceptibility assessment"""
    factors: List[SusceptibilityFactorType] = field(default_factory=list)
    overall_susceptibility_score: float = 0.0
    risk_areas: List[str] = field(default_factory=list)
    protective_recommendations: List[str] = field(default_factory=list)
    requires_enhanced_protection: bool = False

class SusceptiblePopulationDetector:
    """
    Detects and assesses susceptibility to influence.

    Research basis:
    - USC Dornsife 2024: Alzheimer's and financial scam susceptibility
    - PNAS Nexus 2024: APOE4 genotype and phishing susceptibility
    - Thorn 2024: Youth online sexual interaction data
    - Frontiers 2024: Digital media in early childhood
    - Psychology Today 2025: Neurodivergent influence susceptibility
    """

    # Age-based susceptibility factors
    AGE_SUSCEPTIBILITY = {
        'child': {
            'age_range': (0, 12),
            'base_susceptibility': 0.8,
            'factors': [
                'Cannot comprehend persuasive intent',
                'Limited critical evaluation skills',
                'High trust in perceived authorities',
                'Difficulty distinguishing ads from content'
            ]
        },
        'adolescent': {
            'age_range': (13, 17),
            'base_susceptibility': 0.6,
            'factors': [
                'Developing prefrontal cortex',
                'Heightened social comparison',
                'Risk-taking behavior',
                'FOMO susceptibility',
                'Identity formation susceptibility'
            ]
        },
        'young_adult': {
            'age_range': (18, 25),
            'base_susceptibility': 0.3,
            'factors': [
                'Still developing impulse control',
                'Social media native',
                'Financial inexperience'
            ]
        },
        'adult': {
            'age_range': (26, 64),
            'base_susceptibility': 0.2,
            'factors': [
                'Work stress susceptibility',
                'Family responsibility pressure'
            ]
        },
        'elderly': {
            'age_range': (65, 120),
            'base_susceptibility': 0.5,
            'factors': [
                'Potential cognitive decline',
                'Social isolation risk',
                'Digital literacy gaps',
                'Trust in authority',
                'Limited fraud recovery time'
            ]
        }
    }

    # Cognitive indicators of susceptibility
    COGNITIVE_SUSCEPTIBILITY_INDICATORS = {
        'processing_speed_decline': 0.3,
        'memory_issues': 0.4,
        'decision_fatigue': 0.3,
        'attention_difficulties': 0.3,
        'executive_function_issues': 0.4
    }

    # Emotional state susceptibility multipliers
    EMOTIONAL_SUSCEPTIBILITY_MULTIPLIERS = {
        'depression': 1.5,
        'anxiety': 1.4,
        'loneliness': 1.6,
        'grief': 1.5,
        'stress': 1.3,
        'excitement': 1.2,  # Can impair judgment
        'fear': 1.4
    }

    def __init__(self):
        self.population_baselines = {}

    def assess_individual_susceptibility(self, user_data: Dict) -> SusceptibilityProfile:
        """
        Assess individual susceptibility to influence.

        Expected user_data:
        {
            'age': int,
            'cognitive_indicators': List[str],
            'emotional_state': str,
            'social_connection_score': float,  # 0-1, higher = more connected
            'digital_literacy_score': float,  # 0-1, higher = more literate
            'neurodivergent_flags': List[str],
            'financial_stress': bool,
            'recent_life_events': List[str]
        }
        """
        profile = SusceptibilityProfile()
        susceptibility_score = 0.0

        # Age-based assessment
        age = user_data.get('age', 30)
        for category, data in self.AGE_SUSCEPTIBILITY.items():
            if data['age_range'][0] <= age <= data['age_range'][1]:
                susceptibility_score += data['base_susceptibility']

                if category == 'child':
                    profile.factors.append(SusceptibilityFactorType.AGE_CHILD)
                    profile.risk_areas.extend([
                        'In-app purchases', 'Advertising', 'Data collection',
                        'Contact from strangers', 'Inappropriate content'
                    ])
                    profile.requires_enhanced_protection = True

                elif category == 'adolescent':
                    profile.factors.append(SusceptibilityFactorType.AGE_ADOLESCENT)
                    profile.risk_areas.extend([
                        'Social comparison influence', 'FOMO tactics',
                        'Influencer marketing', 'Dating app influence',
                        'Sextortion risk'
                    ])

                elif category == 'elderly':
                    profile.factors.append(SusceptibilityFactorType.AGE_ELDERLY)
                    profile.risk_areas.extend([
                        'Tech support scams', 'Romance scams',
                        'Phishing', 'Investment fraud',
                        'Grandparent scams'
                    ])

                break

        # Cognitive susceptibility assessment
        cognitive_indicators = user_data.get('cognitive_indicators', [])
        for indicator in cognitive_indicators:
            if indicator in self.COGNITIVE_SUSCEPTIBILITY_INDICATORS:
                susceptibility_score += self.COGNITIVE_SUSCEPTIBILITY_INDICATORS[indicator]
                profile.factors.append(SusceptibilityFactorType.COGNITIVE_LOAD)

        # Emotional state assessment
        emotional_state = user_data.get('emotional_state', '')
        if emotional_state in self.EMOTIONAL_SUSCEPTIBILITY_MULTIPLIERS:
            multiplier = self.EMOTIONAL_SUSCEPTIBILITY_MULTIPLIERS[emotional_state]
            susceptibility_score *= multiplier
            profile.factors.append(SusceptibilityFactorType.EMOTIONAL_STATE)
            profile.risk_areas.append(f'Influence during {emotional_state}')

        # Social connection assessment
        social_score = user_data.get('social_connection_score', 0.5)
        if social_score < 0.3:
            susceptibility_score += 0.3
            profile.factors.append(SusceptibilityFactorType.SOCIAL_ISOLATION)
            profile.risk_areas.append('Romance scams')
            profile.risk_areas.append('Companionship influence')

        # Digital literacy assessment
        digital_literacy = user_data.get('digital_literacy_score', 0.5)
        if digital_literacy < 0.4:
            susceptibility_score += 0.3
            profile.factors.append(SusceptibilityFactorType.DIGITAL_LITERACY)
            profile.risk_areas.append('Phishing')
            profile.risk_areas.append('Malware')
            profile.risk_areas.append('Tech support scams')

        # Neurodivergent assessment
        nd_flags = user_data.get('neurodivergent_flags', [])
        if nd_flags:
            susceptibility_score += 0.2
            profile.factors.append(SusceptibilityFactorType.NEURODIVERGENT)
            profile.risk_areas.extend([
                'Gaslighting', 'Social influence',
                'Boundary violations', 'Coercive control'
            ])

        # Financial stress assessment
        if user_data.get('financial_stress', False):
            susceptibility_score += 0.25
            profile.factors.append(SusceptibilityFactorType.FINANCIAL_STRESS)
            profile.risk_areas.extend([
                'Get-rich-quick schemes', 'Loan scams',
                'Intensive lending', 'Advance fee fraud'
            ])

        # Normalize score
        profile.overall_susceptibility_score = min(1.0, susceptibility_score)

        # Determine if enhanced protection needed
        if profile.overall_susceptibility_score > 0.7:
            profile.requires_enhanced_protection = True

        # Generate recommendations
        profile.protective_recommendations = self._generate_recommendations(profile)

        return profile

    def _generate_recommendations(self, profile: SusceptibilityProfile) -> List[str]:
        """Generate protective recommendations based on susceptibility profile"""
        recommendations = []

        if SusceptibilityFactorType.AGE_CHILD in profile.factors:
            recommendations.extend([
                'Enable parental controls on all devices',
                'Use child-safe apps and browsers',
                'Discuss online safety regularly',
                'Monitor online activity',
                'Disable in-app purchases'
            ])

        if SusceptibilityFactorType.AGE_ELDERLY in profile.factors:
            recommendations.extend([
                'Set up call blocking for unknown numbers',
                'Establish a trusted contact for financial decisions',
                'Use password managers with family sharing',
                'Enable multi-factor authentication',
                'Participate in fraud prevention education'
            ])

        if SusceptibilityFactorType.SOCIAL_ISOLATION in profile.factors:
            recommendations.extend([
                'Be cautious of unsolicited contact',
                'Verify identities before sharing personal info',
                'Discuss major decisions with trusted friends/family',
                'Join legitimate community groups for connection'
            ])

        if SusceptibilityFactorType.NEURODIVERGENT in profile.factors:
            recommendations.extend([
                'Take time before making decisions under pressure',
                'Have a trusted person review major commitments',
                'Be aware of influence tactics',
                'Trust your instincts about uncomfortable situations'
            ])

        if SusceptibilityFactorType.EMOTIONAL_STATE in profile.factors:
            recommendations.extend([
                'Avoid major decisions when emotionally distressed',
                'Be extra cautious of urgency tactics',
                'Implement cooling-off periods for purchases',
                'Seek support before responding to pressure'
            ])

        return recommendations


class ChildSafetyDetector:
    """
    Specialized detection for child-targeted influence.

    Research basis:
    - Frontiers 2024: Digital media in early childhood
    - Thorn 2024: Youth online sexual interaction data
    - EU Parliament: Social media influence on children
    """

    # Patterns that indicate child-targeted influence
    CHILD_TARGETING_PATTERNS = {
        'visual_elements': [
            'cartoon', 'animated', 'colorful', 'character', 'mascot',
            'game', 'play', 'fun', 'adventure', 'magic'
        ],
        'language_patterns': [
            'kids', 'children', 'young', 'learn', 'educational',
            'family', 'safe', 'friendly'
        ],
        'influence_tactics': [
            'collect', 'unlock', 'level up', 'surprise', 'mystery',
            'limited edition', 'exclusive', 'special'
        ]
    }

    # Grooming language patterns (from research)
    GROOMING_LANGUAGE = {
        'selection_phase': [
            r'how old are you',
            r'do you have (a )?(boyfriend|girlfriend)',
            r'are your parents (home|around)',
            r'do you have (snapchat|instagram|tiktok)'
        ],
        'trust_building': [
            r'you\'re (so )?(mature|special|different)',
            r'i understand you',
            r'no one (else )?gets you',
            r'our (little )?secret'
        ],
        'isolation': [
            r'don\'t tell (anyone|your parents)',
            r'they wouldn\'t understand',
            r'just between us',
            r'private (chat|message)'
        ]
    }

    def analyze_content_for_child_targeting(self, content: Dict) -> Dict:
        """
        Analyze content for child-targeted influence.

        Expected content:
        {
            'text': str,
            'visual_elements': List[str],
            'audio_elements': List[str],
            'interactive_elements': List[str]
        }
        """
        analysis = {
            'child_targeted': False,
            'targeting_score': 0.0,
            'influence_tactics': [],
            'risk_level': 'low',
            'concerns': []
        }

        text = content.get('text', '').lower()
        visuals = [v.lower() for v in content.get('visual_elements', [])]

        # Check visual targeting
        visual_matches = sum(
            1 for pattern in self.CHILD_TARGETING_PATTERNS['visual_elements']
            if any(pattern in v for v in visuals)
        )

        # Check language targeting
        language_matches = sum(
            1 for pattern in self.CHILD_TARGETING_PATTERNS['language_patterns']
            if pattern in text
        )

        # Check influence tactics
        tactic_matches = []
        for tactic in self.CHILD_TARGETING_PATTERNS['influence_tactics']:
            if tactic in text:
                tactic_matches.append(tactic)

        # Calculate targeting score
        analysis['targeting_score'] = min(1.0,
            (visual_matches * 0.15) +
            (language_matches * 0.1) +
            (len(tactic_matches) * 0.2)
        )

        analysis['child_targeted'] = analysis['targeting_score'] > 0.3
        analysis['influence_tactics'] = tactic_matches

        # Assess risk level
        if analysis['targeting_score'] > 0.7:
            analysis['risk_level'] = 'high'
            analysis['concerns'].append('Heavy use of child-targeting influence')
        elif analysis['targeting_score'] > 0.4:
            analysis['risk_level'] = 'medium'
            analysis['concerns'].append('Moderate child-targeting elements')

        # Check for intensive interface patterns in children's content
        if 'collect' in tactic_matches and 'limited' in text:
            analysis['concerns'].append('Artificial scarcity targeting children')

        if 'surprise' in tactic_matches or 'mystery' in tactic_matches:
            analysis['concerns'].append('Variable reward mechanics (gambling-like)')

        return analysis

    def detect_grooming_patterns(self, messages: List[Dict]) -> Dict:
        """
        Detect potential grooming patterns in message sequences.

        Expected messages: [{'sender': str, 'content': str, 'timestamp': float}]
        """
        analysis = {
            'grooming_detected': False,
            'phase': 'none',
            'confidence': 0.0,
            'matched_patterns': [],
            'risk_level': 'none',
            'immediate_action_needed': False
        }

        phase_scores = {phase: 0 for phase in self.GROOMING_LANGUAGE}

        for msg in messages:
            content = msg.get('content', '').lower()

            for phase, patterns in self.GROOMING_LANGUAGE.items():
                for pattern in patterns:
                    if re.search(pattern, content):
                        phase_scores[phase] += 1
                        analysis['matched_patterns'].append({
                            'phase': phase,
                            'pattern': pattern,
                            'content': content[:100]
                        })

        # Determine dominant phase
        max_phase = max(phase_scores, key=phase_scores.get)
        max_score = phase_scores[max_phase]

        if max_score > 0:
            analysis['phase'] = max_phase
            analysis['confidence'] = min(1.0, max_score / 3)

            # Progressive phases indicate active grooming
            phases_present = [p for p, s in phase_scores.items() if s > 0]


#### 4.11.11 Economic Influence Mechanics

## 7. ECONOMIC INFLUENCE MECHANICS

### Research Findings

**Dynamic Pricing (2024):**
- Amazon changes prices 2.5 million times per day
- "Surveillance pricing" uses personal data for individualized prices
- FTC investigating in July 2024
- Loyal customers often charged MORE
- Personalized pricing can increase profits 19%

**Anchoring & Decoy Effects:**
- 70% of consumers influenced by initial price anchor
- Williams-Sonoma: $429 decoy increased $275 model sales
- Campbell's "Limit 12" increased purchases from 3.3 to 7 cans
- Decoy pricing steers choices toward target option

**Subscription Influence:**
- Average cancellation: 8+ minutes vs 1-2 click signup
- Forced surveys, phone calls, typed confirmations
- "Confirmshaming" guilt tactics
- Hidden renewal terms

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
    Detects pricing and economic influence tactics.

    Research basis:
    - AIMultiple 2026: Dynamic pricing algorithms
    - ResearchGate 2024: Anchoring and decoy pricing
    - FTC 2024: Surveillance pricing investigation
    - CHI 2024: Subscription cancellation analysis
    """

    # Charm pricing patterns
    CHARM_PRICES = ['.99', '.95', '.97', '.49']

    # Urgency language patterns
    URGENCY_PATTERNS = [
        'only .* left', 'limited stock', 'selling fast',
        'ends in', 'expires', 'last chance', 'hurry',
        '.* people viewing', 'in .* carts', 'just sold'
    ]

    # Drip pricing signals
    DRIP_PRICING_SIGNALS = [
        'service fee', 'processing fee', 'convenience fee',
        'handling', 'delivery', 'taxes not included',
        'additional charges may apply', 'plus fees'
    ]

    def __init__(self):
        self.price_history = {}

    def analyze_pricing_page(self, page_data: Dict) -> PricingAnalysis:
        """
        Analyze a pricing page for influence tactics.

        Expected page_data:
        {
            'prices': [{'name': str, 'displayed_price': float, 'features': List[str]}],
            'original_prices': [float],  # Strikethrough prices
            'urgency_elements': List[str],
            'fine_print': str,
            'checkout_flow': [{'step': int, 'new_charges': float}]
        }
        """
        analysis = PricingAnalysis()

        prices = page_data.get('prices', [])
        original_prices = page_data.get('original_prices', [])

        # Analyze anchor pricing
        if original_prices and prices:
            for i, orig in enumerate(original_prices):
                if i < len(prices) and orig > 0:
                    discount_shown = (orig - prices[i]['displayed_price']) / orig
                    if discount_shown > 0.3:  # More than 30% "discount"
                        analysis.influence_types.append(PricingInfluenceType.ANCHOR_PRICING)
                        analysis.anchor_effect_strength = discount_shown
                        break

        # Detect decoy pricing
        if len(prices) >= 3:
            decoy_result = self._detect_decoy(prices)
            if decoy_result['decoy_detected']:
                analysis.decoy_detected = True
                analysis.influence_types.append(PricingInfluenceType.DECOY_PRICING)

        # Analyze drip pricing
        checkout_flow = page_data.get('checkout_flow', [])
        if checkout_flow:
            initial_price = checkout_flow[0].get('total', 0) if checkout_flow else 0
            final_price = checkout_flow[-1].get('total', 0) if checkout_flow else 0

            if final_price > initial_price * 1.1:  # More than 10% increase
                analysis.drip_pricing_amount = final_price - initial_price
                analysis.true_price_vs_displayed = final_price / initial_price if initial_price > 0 else 1
                analysis.influence_types.append(PricingInfluenceType.DRIP_PRICING)

        # Check fine print for hidden fees
        fine_print = page_data.get('fine_print', '').lower()
        for signal in self.DRIP_PRICING_SIGNALS:
            if signal in fine_print:
                if PricingInfluenceType.DRIP_PRICING not in analysis.influence_types:
                    analysis.influence_types.append(PricingInfluenceType.DRIP_PRICING)
                break

        # Analyze urgency tactics
        urgency_elements = page_data.get('urgency_elements', [])
        for element in urgency_elements:
            element_lower = element.lower()
            for pattern in self.URGENCY_PATTERNS:
                if re.search(pattern, element_lower):
                    analysis.urgency_tactics.append(element)
                    break

        if analysis.urgency_tactics:
            analysis.influence_types.append(PricingInfluenceType.TIME_PRESSURE)

            # Check for artificial scarcity
            if any('left' in t.lower() or 'stock' in t.lower() for t in analysis.urgency_tactics):
                analysis.influence_types.append(PricingInfluenceType.ARTIFICIAL_SCARCITY)

        # Check for charm pricing
        for price in prices:
            price_str = str(price.get('displayed_price', 0))
            if any(charm in price_str for charm in self.CHARM_PRICES):
                analysis.influence_types.append(PricingInfluenceType.CHARM_PRICING)
                break

        # Calculate overall influence score
        analysis.overall_influence_score = min(1.0,
            len(analysis.influence_types) * 0.15 +
            analysis.anchor_effect_strength * 0.2 +
            (0.3 if analysis.decoy_detected else 0) +
            min(0.3, analysis.drip_pricing_amount / 50) +
            len(analysis.urgency_tactics) * 0.1
        )

        return analysis

    def _detect_decoy(self, prices: List[Dict]) -> Dict:
        """
        Detect decoy pricing pattern (asymmetric dominance).

        A decoy is inferior to one option but not clearly inferior to another,
        making the target option look better by comparison.
        """
        result = {
            'decoy_detected': False,
            'decoy_index': None,
            'target_index': None,
            'competitor_index': None
        }

        if len(prices) < 3:
            return result

        # Simple heuristic: middle option is often the decoy
        # Check if middle option has poor value compared to higher option
        sorted_prices = sorted(prices, key=lambda x: x.get('displayed_price', 0))

        for i in range(1, len(sorted_prices) - 1):
            lower = sorted_prices[i - 1]
            middle = sorted_prices[i]
            higher = sorted_prices[i + 1]

            lower_price = lower.get('displayed_price', 0)
            middle_price = middle.get('displayed_price', 0)
            higher_price = higher.get('displayed_price', 0)

            # If middle is close to higher in price but has significantly fewer features
            if middle_price > lower_price * 1.3:  # Middle is >30% more than lower
                price_diff_to_higher = higher_price - middle_price
                price_diff_to_lower = middle_price - lower_price

                # If small price jump to higher but big jump from lower
                if price_diff_to_higher < price_diff_to_lower * 0.5:
                    result['decoy_detected'] = True
                    result['decoy_index'] = i
                    result['target_index'] = i + 1  # Higher option is target
                    result['competitor_index'] = i - 1
                    break

        return result

    def track_price_changes(self, product_id: str, current_price: float, timestamp: float) -> Dict:
        """
        Track price changes over time to detect dynamic pricing.
        """
        if product_id not in self.price_history:
            self.price_history[product_id] = []

        self.price_history[product_id].append({
            'price': current_price,
            'timestamp': timestamp
        })

        history = self.price_history[product_id]

        analysis = {
            'price_changes_detected': len(history) > 1,
            'change_frequency': 0,
            'price_volatility': 0.0,
            'dynamic_pricing_likely': False,
            'trend': 'stable'
        }

        if len(history) >= 2:
            prices = [h['price'] for h in history]
            timestamps = [h['timestamp'] for h in history]

            # Calculate change frequency
            time_span = timestamps[-1] - timestamps[0]
            if time_span > 0:
                changes = sum(1 for i in range(1, len(prices)) if prices[i] != prices[i-1])
                analysis['change_frequency'] = changes / (time_span / 3600)  # Changes per hour

            # Calculate volatility
            if len(prices) >= 3:
                analysis['price_volatility'] = np.std(prices) / np.mean(prices) if np.mean(prices) > 0 else 0

            # Detect dynamic pricing
            if analysis['change_frequency'] > 0.5 or analysis['price_volatility'] > 0.1:
                analysis['dynamic_pricing_likely'] = True

            # Determine trend
            if prices[-1] > prices[0] * 1.05:
                analysis['trend'] = 'increasing'
            elif prices[-1] < prices[0] * 0.95:
                analysis['trend'] = 'decreasing'

        return analysis

#### 4.11.12 AI-Specific Influence Detection

## 8. AI-SPECIFIC INFLUENCE

### Research Findings

**LLM Persuasion (2024-2025):**
- LLMs can exceed human persuasion in controlled settings
- GPT-4 with personal info: 81.7% higher agreement odds
- Post-training methods boosted persuasiveness 51%
- Increased persuasion often correlated with DECREASED factual accuracy
- Scaling model size shows diminishing returns for persuasion

**Deepfakes (2024):**
- $12 billion in deepfake-enabled fraud (projected $40B in 3 years)
- 1 in 4 adults experienced AI voice scams
- Best detectors only 75% accurate
- "Impostor Bias" - people question even authentic media
- January 2024: AI Biden robocall attempted election influence

**AI-Generated Content:**
- 68% concerned about AI influence
- Detection tools 50% less effective on "in the wild" deepfakes
- Adversarial perturbations reduce detection 40%

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
    Detects AI-generated influence content.

    Research basis:
    - Science 2025: Levers of political persuasion with AI
    - arXiv 2025: LLM as notable persuader
    - Nature 2025: Meta-analysis of LLM persuasive power
    - PMC 2025: Deepfake detection survey
    - Deloitte 2025: Deepfake disruption report
    """

    # LLM-generated text indicators
    LLM_TEXT_INDICATORS = {
        'excessive_hedging': [
            'it\'s important to note', 'it should be mentioned',
            'one might argue', 'it could be said'
        ],
        'formal_transitions': [
            'furthermore', 'moreover', 'additionally', 'consequently',
            'nevertheless', 'notwithstanding'
        ],
        'ai_phrases': [
            'as an ai', 'i don\'t have personal', 'i cannot',
            'it\'s worth noting', 'in conclusion'
        ],
        'balanced_framing': [
            'on the other hand', 'however', 'while some argue',
            'both sides', 'perspectives vary'
        ]
    }

    # Deepfake detection heuristics
    DEEPFAKE_VIDEO_INDICATORS = {
        'facial_inconsistencies': [
            'eye_blink_irregular', 'lip_sync_mismatch', 'face_boundary_artifacts',
            'lighting_inconsistency', 'head_pose_unnatural'
        ],
        'temporal_artifacts': [
            'frame_flickering', 'temporal_coherence_loss', 'motion_blur_missing'
        ],
        'quality_indicators': [
            'resolution_mismatch', 'compression_artifacts', 'color_inconsistency'
        ]
    }

    # Persuasion technique indicators from research
    PERSUASION_TECHNIQUES = {
        'personalization': {
            'indicators': ['based on your', 'tailored for you', 'your interests'],
            'effectiveness_boost': 0.82  # 81.7% from research
        },
        'emotional_appeal': {
            'indicators': ['feel', 'imagine', 'picture yourself', 'experience'],
            'effectiveness_boost': 0.51  # 51% from post-training methods
        },
        'social_proof_synthetic': {
            'indicators': ['thousands have', 'everyone is', 'popular choice'],
            'effectiveness_boost': 0.30
        },
        'authority_citation': {
            'indicators': ['experts say', 'studies show', 'research indicates'],
            'effectiveness_boost': 0.27  # 27% from prompting methods
        }
    }

    def analyze_text_for_ai_generation(self, text: str) -> AIContentAnalysis:
        """
        Analyze text for AI generation indicators.
        """
        analysis = AIContentAnalysis()
        text_lower = text.lower()

        indicator_counts = {category: 0 for category in self.LLM_TEXT_INDICATORS}

        for category, phrases in self.LLM_TEXT_INDICATORS.items():
            for phrase in phrases:
                if phrase in text_lower:
                    indicator_counts[category] += 1
                    analysis.synthetic_markers.append(f"{category}: {phrase}")

        # Calculate AI probability based on indicators
        total_indicators = sum(indicator_counts.values())
        text_length = len(text.split())

        # Normalize by text length (longer texts naturally have more phrases)
        indicator_density = total_indicators / (text_length / 100) if text_length > 0 else 0

        # AI text tends to have multiple categories present
        categories_present = sum(1 for c in indicator_counts.values() if c > 0)

        analysis.ai_generated_probability = min(1.0,
            indicator_density * 0.3 +
            categories_present * 0.15
        )

        # Check for persuasion techniques
        persuasion_detected = []
        for technique, data in self.PERSUASION_TECHNIQUES.items():
            if any(ind in text_lower for ind in data['indicators']):
                persuasion_detected.append(technique)

        if persuasion_detected:
            analysis.influence_type = AIInfluenceType.LLM_PERSUASION
            analysis.ai_generated_probability += 0.1 * len(persuasion_detected)

        # Determine risk level
        if analysis.ai_generated_probability > 0.7:
            analysis.risk_level = "high"
        elif analysis.ai_generated_probability > 0.4:
            analysis.risk_level = "medium"
        else:
            analysis.risk_level = "low"

        analysis.confidence = min(1.0, 0.3 + total_indicators * 0.1)

        return analysis

    def analyze_conversation_for_chatbot_influence(
        self,
        messages: List[Dict],
        claimed_identity: str = ""
    ) -> Dict:
        """
        Analyze conversation for AI chatbot influence patterns.

        Research shows chatbots can use therapeutic rapport techniques
        for influence purposes.
        """
        analysis = {
            'chatbot_suspected': False,
            'influence_patterns': [],
            'rapport_building_detected': False,
            'personalization_level': 0.0,
            'risk_score': 0.0
        }

        if not messages:
            return analysis

        # Analyze response patterns
        response_lengths = []
        response_times = []
        formality_scores = []

        for i, msg in enumerate(messages):
            if msg.get('role') == 'assistant' or msg.get('sender') == claimed_identity:
                content = msg.get('content', '')
                response_lengths.append(len(content.split()))

                # Check for AI-like consistency
                if i > 0:
                    prev_time = messages[i-1].get('timestamp', 0)
                    curr_time = msg.get('timestamp', 0)
                    if curr_time > prev_time:
                        response_times.append(curr_time - prev_time)

        # AI chatbots often have consistent response lengths
        if response_lengths:
            length_cv = np.std(response_lengths) / np.mean(response_lengths) if np.mean(response_lengths) > 0 else 1
            if length_cv < 0.3:  # Very consistent
                analysis['chatbot_suspected'] = True
                analysis['influence_patterns'].append('CONSISTENT_RESPONSE_LENGTH')

        # AI chatbots often respond quickly and consistently
        if response_times:
            time_cv = np.std(response_times) / np.mean(response_times) if np.mean(response_times) > 0 else 1
            if time_cv < 0.2:  # Very consistent timing
                analysis['influence_patterns'].append('CONSISTENT_RESPONSE_TIME')

        # Check for rapport-building techniques
        rapport_phrases = [
            'i understand', 'that must be', 'i hear you',
            'tell me more', 'how does that make you feel'
        ]

        rapport_count = 0
        for msg in messages:
            content = msg.get('content', '').lower()
            if any(phrase in content for phrase in rapport_phrases):
                rapport_count += 1

        if rapport_count > len(messages) * 0.2:
            analysis['rapport_building_detected'] = True
            analysis['influence_patterns'].append('THERAPEUTIC_RAPPORT_TECHNIQUES')

        # Check for personalization (using user's info against them)
        user_messages = [m for m in messages if m.get('role') == 'user' or m.get('sender') != claimed_identity]
        assistant_messages = [m for m in messages if m.get('role') == 'assistant' or m.get('sender') == claimed_identity]

        # Look for echoed personal details
        user_text = ' '.join(m.get('content', '') for m in user_messages).lower()
        for msg in assistant_messages:
            content = msg.get('content', '').lower()

            # Simple check: does assistant reference specific user details?
            personal_echoes = sum(1 for word in user_text.split()
                                 if len(word) > 5 and word in content)

            if personal_echoes > 3:
                analysis['personalization_level'] = min(1.0, personal_echoes / 10)
                analysis['influence_patterns'].append('PERSONAL_INFO_INTENSITY')

        # Calculate risk score
        analysis['risk_score'] = min(1.0,
            (0.3 if analysis['chatbot_suspected'] else 0) +
            (0.2 if analysis['rapport_building_detected'] else 0) +
            analysis['personalization_level'] * 0.3 +
            len(analysis['influence_patterns']) * 0.1
        )

        return analysis


class DeepfakeDetector:
    """
    Detects deepfake and synthetic media.

    Research basis:
    - PMC 2025: Deepfake forensics survey
    - GAO 2024: Combating deepfakes spotlight
    - Springer 2025: Multimedia deepfake detection
    """

    # Based on research: best detectors only 75% accurate
    DETECTION_CONFIDENCE_CAP = 0.75

    def analyze_video_authenticity(self, video_features: Dict) -> AIContentAnalysis:
        """
        Analyze video for deepfake indicators.

        Expected video_features:
        {
            'face_detection_consistency': float,  # 0-1
            'blink_pattern_score': float,  # 0-1, 1 = natural
            'lip_sync_score': float,  # 0-1, 1 = perfect sync
            'lighting_consistency': float,  # 0-1
            'temporal_coherence': float,  # 0-1
            'compression_artifacts': float,  # 0-1, higher = more artifacts
            'face_boundary_quality': float,  # 0-1
            'source_metadata': Dict
        }
        """
        analysis = AIContentAnalysis()
        analysis.influence_type = AIInfluenceType.DEEPFAKE_VIDEO

        scores = []
        weights = []

        # Blink pattern (deepfakes often have irregular blinking)
        blink_score = video_features.get('blink_pattern_score', 0.5)
        if blink_score < 0.5:
            analysis.synthetic_markers.append('IRREGULAR_BLINK_PATTERN')
        scores.append(1 - blink_score)
        weights.append(0.2)

        # Lip sync (AI struggles with perfect lip sync)
        lip_sync = video_features.get('lip_sync_score', 0.5)
        if lip_sync < 0.7:
            analysis.synthetic_markers.append('LIP_SYNC_MISMATCH')
        scores.append(1 - lip_sync)
        weights.append(0.25)

        # Lighting consistency
        lighting = video_features.get('lighting_consistency', 0.5)
        if lighting < 0.6:
            analysis.synthetic_markers.append('LIGHTING_INCONSISTENCY')
        scores.append(1 - lighting)
        weights.append(0.15)

        # Temporal coherence (frame-to-frame consistency)
        temporal = video_features.get('temporal_coherence', 0.5)
        if temporal < 0.6:
            analysis.synthetic_markers.append('TEMPORAL_ARTIFACTS')
        scores.append(1 - temporal)
        weights.append(0.2)

        # Face boundary quality
        boundary = video_features.get('face_boundary_quality', 0.5)
        if boundary < 0.7:
            analysis.synthetic_markers.append('FACE_BOUNDARY_ARTIFACTS')
        scores.append(1 - boundary)
        weights.append(0.2)

        # Calculate weighted probability
        weighted_sum = sum(s * w for s, w in zip(scores, weights))
        total_weight = sum(weights)

        analysis.ai_generated_probability = min(
            self.DETECTION_CONFIDENCE_CAP,
            weighted_sum / total_weight if total_weight > 0 else 0
        )

        # Check metadata
        metadata = video_features.get('source_metadata', {})
        if metadata.get('editing_software') in ['Runway', 'Synthesia', 'DeepFaceLab']:
            analysis.synthetic_markers.append('KNOWN_DEEPFAKE_SOFTWARE_METADATA')
            analysis.ai_generated_probability = min(0.9, analysis.ai_generated_probability + 0.3)

        # Determine risk level
        if analysis.ai_generated_probability > 0.6:
            analysis.risk_level = "high"
        elif analysis.ai_generated_probability > 0.35:
            analysis.risk_level = "medium"
        else:
            analysis.risk_level = "low"

        # Confidence based on marker count
        analysis.confidence = min(self.DETECTION_CONFIDENCE_CAP,
            0.3 + len(analysis.synthetic_markers) * 0.1)

        # Add authenticity indicators
        if analysis.ai_generated_probability < 0.3:
            analysis.authenticity_indicators = [
                'NATURAL_BLINK_PATTERN',
                'CONSISTENT_LIGHTING',
                'SMOOTH_TEMPORAL_FLOW'
            ]

        return analysis

    def analyze_audio_authenticity(self, audio_features: Dict) -> AIContentAnalysis:
        """
        Analyze audio for voice cloning/deepfake indicators.

        Expected audio_features:
        {
            'spectral_consistency': float,
            'breathing_patterns': float,  # 0-1, 1 = natural
            'micro_pauses': float,  # Natural speech has micro-pauses
            'pitch_variation': float,
            'background_consistency': float,
            'clipping_artifacts': float
        }
        """
        analysis = AIContentAnalysis()
        analysis.influence_type = AIInfluenceType.DEEPFAKE_AUDIO

        # Breathing patterns (cloned voices often lack natural breathing)
        breathing = audio_features.get('breathing_patterns', 0.5)
        if breathing < 0.4:
            analysis.synthetic_markers.append('MISSING_BREATH_SOUNDS')

        # Micro-pauses (AI often too fluent)
        pauses = audio_features.get('micro_pauses', 0.5)
        if pauses < 0.3:
            analysis.synthetic_markers.append('UNNATURAL_FLUENCY')

        # Pitch variation (cloned voices may have limited variation)
        pitch_var = audio_features.get('pitch_variation', 0.5)
        if pitch_var < 0.4:
            analysis.synthetic_markers.append('LIMITED_PITCH_VARIATION')

        # Background consistency (AI may have too-clean background)
        background = audio_features.get('background_consistency', 0.5)
        if background > 0.95:  # Too consistent = suspicious
            analysis.synthetic_markers.append('UNNATURALLY_CLEAN_BACKGROUND')

        # Calculate probability
        marker_count = len(analysis.synthetic_markers)
        analysis.ai_generated_probability = min(
            self.DETECTION_CONFIDENCE_CAP,
            marker_count * 0.2
        )

        if analysis.ai_generated_probability > 0.5:
            analysis.risk_level = "high"
        elif analysis.ai_generated_probability > 0.25:
            analysis.risk_level = "medium"
        else:
            analysis.risk_level = "low"

        analysis.confidence = min(0.7, 0.3 + marker_count * 0.1)

        return analysis
```

#### 4.11.13 Intervention Effectiveness Analysis

## 9. INTERVENTION EFFECTIVENESS ANALYSIS

### Research Findings

**Media Literacy Interventions (2024):**
- Meta-analysis (N=81,155): Overall effect d=0.60
- Reduces belief in misinformation (d=0.27)
- Improves discernment (d=0.76)
- Decreases sharing (d=1.04)
- Multiple sessions (d=1.93) >> single session (d=0.26)

**Friction Interventions:**
- Short delays before app opening increase intentional use
- Warning labels reduce sharing but not belief
- Cooling-off periods effective for purchases

**Inoculation Theory:**
- "Prebunking" reduces misinformation endorsement (d=-0.36)
- Teaching influence tactics more effective than fact-checking
- Effects decay without reinforcement

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
    effect_size: float  # Cohen's d or similar
    confidence_interval: Tuple[float, float]
    duration_of_effect: str  # "immediate", "short-term", "long-term"
    decay_rate: float  # How quickly effect diminishes
    population_moderators: List[str]
    implementation_cost: str  # "low", "medium", "high"
    scalability: str  # "low", "medium", "high"

class InterventionAnalyzer:
    """
    Analyzes and recommends interventions against influence.

    Research basis:
    - Sage 2024: Media literacy meta-analysis
    - arXiv 2024: Design frictions on social media
    - Various inoculation theory research
    """

    # Evidence-based intervention effectiveness from research
    INTERVENTION_EVIDENCE = {
        InterventionType.MEDIA_LITERACY: {
            'overall_effect': 0.60,
            'belief_reduction': 0.27,
            'discernment_improvement': 0.76,
            'sharing_reduction': 1.04,
            'multiple_sessions_effect': 1.93,
            'single_session_effect': 0.26,
            'decay_rate': 0.3,  # Effect decays ~30% without reinforcement
            'moderators': ['education_level', 'age', 'prior_exposure']
        },
        InterventionType.INOCULATION: {
            'overall_effect': 0.36,
            'misinformation_endorsement_reduction': 0.36,
            'influence_recognition_improvement': 0.45,
            'decay_rate': 0.25,
            'boosters_recommended': True
        },
        InterventionType.FRICTION: {
            'intentional_use_increase': 0.30,
            'mindless_scrolling_reduction': 0.40,
            'optimal_delay_seconds': 3,
            'effectiveness_at_home': 'reduced',  # Per research
            'effectiveness_other_settings': 'higher'
        },
        InterventionType.WARNING_LABEL: {
            'sharing_reduction': 0.20,
            'belief_reduction': 0.10,  # Less effective for beliefs
            'reactance_risk': 0.15  # Can backfire
        },
        InterventionType.COOLING_OFF: {
            'impulse_purchase_reduction': 0.35,
            'regret_reduction': 0.40,
            'optimal_period_hours': 24
        }
    }

    def recommend_interventions(
        self,
        influence_analysis: Dict,
        target_population: Dict = None
    ) -> List[Dict]:
        """
        Recommend interventions based on detected influence.

        Args:
            influence_analysis: Results from various detectors
            target_population: Demographics and characteristics
        """
        recommendations = []

        # Analyze what influences were detected
        influence_types = influence_analysis.get('influence_types', [])
        risk_score = influence_analysis.get('overall_risk_score', 0)

        # High-risk situations need multiple interventions
        if risk_score > 0.7:
            recommendations.append({
                'intervention': InterventionType.FRICTION,
                'priority': 'high',
                'rationale': 'Immediate friction to slow decision-making',
                'implementation': 'Add 3-5 second delay before action',
                'expected_effect': 0.40
            })

        # Media literacy for ongoing protection
        if any(m in str(influence_types) for m in ['misinformation', 'fake', 'deepfake']):
            recommendations.append({
                'intervention': InterventionType.MEDIA_LITERACY,
                'priority': 'high',
                'rationale': 'Build long-term resistance to misinformation',
                'implementation': 'Multi-session program (4+ sessions)',
                'expected_effect': 1.93,
                'note': 'Single sessions only achieve d=0.26'
            })

        # Inoculation for predictable influence patterns
        if any(m in str(influence_types) for m in ['scarcity', 'urgency', 'authority']):
            recommendations.append({
                'intervention': InterventionType.INOCULATION,
                'priority': 'medium',
                'rationale': 'Prebunk common influence tactics',
                'implementation': 'Explain tactic mechanisms before exposure',
                'expected_effect': 0.36
            })

        # Warning labels for specific content
        if 'emotional_influence' in str(influence_types):
            recommendations.append({
                'intervention': InterventionType.WARNING_LABEL,
                'priority': 'medium',
                'rationale': 'Alert to emotional influence',
                'implementation': 'Contextual warning before content',
                'expected_effect': 0.20,
                'caution': 'May not reduce belief, mainly reduces sharing'
            })

        # Cooling-off for financial influence
        if any(m in str(influence_types) for m in ['pricing', 'subscription', 'purchase']):
            recommendations.append({
                'intervention': InterventionType.COOLING_OFF,
                'priority': 'high',
                'rationale': 'Prevent impulse decisions',
                'implementation': '24-hour delay for significant purchases',
                'expected_effect': 0.35
            })

        # Adjust for population factors
        if target_population:
            recommendations = self._adjust_for_population(recommendations, target_population)

        return sorted(recommendations, key=lambda x: x.get('priority', 'low') == 'high', reverse=True)

    def _adjust_for_population(self, recommendations: List[Dict], population: Dict) -> List[Dict]:
        """Adjust recommendations based on target population"""
        age = population.get('age', 30)

        for rec in recommendations:
            # Media literacy more effective for college students
            if rec['intervention'] == InterventionType.MEDIA_LITERACY:
                if 18 <= age <= 25:
                    rec['expected_effect'] *= 1.2
                    rec['note'] = rec.get('note', '') + ' Higher effect for college-age.'

            # Friction less effective at home (per research)
            if rec['intervention'] == InterventionType.FRICTION:
                if population.get('context') == 'home':
                    rec['expected_effect'] *= 0.7
                    rec['caution'] = 'Reduced effectiveness in home settings'

        return recommendations

    def calculate_combined_intervention_effect(
        self,
        interventions: List[InterventionType]
    ) -> Dict:
        """
        Calculate expected combined effect of multiple interventions.

        Note: Effects don't simply add; there are diminishing returns.
        """
        if not interventions:
            return {'combined_effect': 0, 'synergies': [], 'conflicts': []}

        effects = []
        for intervention in interventions:
            if intervention in self.INTERVENTION_EVIDENCE:
                effects.append(self.INTERVENTION_EVIDENCE[intervention].get('overall_effect', 0))

        # Apply diminishing returns formula
        # Each additional intervention adds less
        combined = 0
        for i, effect in enumerate(sorted(effects, reverse=True)):
            # Each subsequent intervention has reduced marginal effect
            diminishing_factor = 1 / (1 + i * 0.3)
            combined += effect * diminishing_factor

        result = {
            'combined_effect': min(2.0, combined),  # Cap at very large effect
            'synergies': [],
            'conflicts': []
        }

        # Check for synergies
        if InterventionType.INOCULATION in interventions and InterventionType.MEDIA_LITERACY in interventions:
            result['synergies'].append('Inoculation + Media Literacy: Complementary approaches')
            result['combined_effect'] *= 1.1

        # Check for conflicts
        if InterventionType.WARNING_LABEL in interventions and len(interventions) > 2:
            result['conflicts'].append('Too many interventions may cause warning fatigue')
            result['combined_effect'] *= 0.9

        return result


class InterventionDecayTracker:
    """
    Tracks intervention effectiveness over time.

    Research shows effects decay without reinforcement.
    """

    def __init__(self):
        self.intervention_history = {}

    def record_intervention(
        self,
        user_id: str,
        intervention: InterventionType,
        timestamp: float,
        initial_effect: float
    ):
        """Record when an intervention was applied"""
        if user_id not in self.intervention_history:
            self.intervention_history[user_id] = []

        self.intervention_history[user_id].append({
            'intervention': intervention,
            'timestamp': timestamp,
            'initial_effect': initial_effect
        })

    def calculate_current_protection_level(
        self,
        user_id: str,
        current_time: float
    ) -> Dict:
        """Calculate current protection level accounting for decay"""
        if user_id not in self.intervention_history:
            return {'protection_level': 0, 'recommendations': ['No interventions recorded']}

        history = self.intervention_history[user_id]

        total_protection = 0
        decayed_interventions = []

        for record in history:
            intervention = record['intervention']
            elapsed_days = (current_time - record['timestamp']) / 86400

            # Get decay rate from evidence base
            decay_rate = InterventionAnalyzer.INTERVENTION_EVIDENCE.get(
                intervention, {}
            ).get('decay_rate', 0.3)

            # Exponential decay model
            remaining_effect = record['initial_effect'] * np.exp(-decay_rate * elapsed_days / 30)

            total_protection += remaining_effect

            if remaining_effect < record['initial_effect'] * 0.5:
                decayed_interventions.append(intervention.value)

        result = {
            'protection_level': min(1.0, total_protection),
            'decayed_interventions': decayed_interventions,
            'recommendations': []
        }

        if decayed_interventions:
            result['recommendations'].append(
                f"Consider booster for: {', '.join(decayed_interventions)}"
            )

        if result['protection_level'] < 0.3:
            result['recommendations'].append("Protection level low - intervention recommended")

        return result
```

#### 4.11.14 Regulatory Compliance Mapping

## 10. REGULATORY COMPLIANCE MAPPING

### Research Findings

**FTC Enforcement (2024-2025):**
- Amazon: $2.5 billion settlement for interface design patterns
- Adobe: DOJ complaint for cancellation difficulty
- 76% of sites use interface design patterns (international review)
- Click-to-Cancel rule adopted then vacated

**EU Regulations:**
- Digital Services Act (Feb 2024): Prohibits "making cancellation significantly more cumbersome than signup"
- AI Act: Classifies emotional influence as high-risk/prohibited
- German Fair Consumer Contracts Act: Requires termination button

**US State Laws:**
- CCPA: Explicit interface design pattern prohibition
- 14 states with privacy/deceptive design laws

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
    severity: str  # "minor", "moderate", "severe"
    enforcement_likelihood: float
    potential_penalty: str
    remediation_steps: List[str]

class RegulatoryComplianceAnalyzer:
    """
    Maps detected influence to regulatory violations.

    Research basis:
    - FTC enforcement actions 2024
    - EU DSA requirements
    - State privacy law requirements
    """

    # Regulatory mappings
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
                'prohibits': [
                    'cancellation_harder_than_signup',
                    'dark_patterns',
                    'manipulative_design'
                ],
                'enforcement': 'Active since Feb 2024',
                'penalties': 'Up to 6% global turnover'
            },
            'ai_act': {
                'name': 'EU AI Act',
                'prohibits': [
                    'subliminal_influence',
                    'intensity_of_susceptibilities',
                    'social_scoring'
                ],
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

    # Mapping from influence types to regulations
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
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),  # COPPA via FTC
            (Jurisdiction.EU, 'dsa')
        ],
        'deepfake_fraud': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5')
            # Multiple state laws also apply
        ]
    }

#### 4.11.15 Integration Test Data

```python

# Import statement for using all detectors
import time

# Example usage
if __name__ == "__main__":
    auditor = ComprehensivePersuasionAuditor()

    # Example audit
    sample_content = {
        'text': 'Act now! Limited time offer expires in 24 hours. Our experts recommend this product.',
        'interface': {
            'features': ['streak counter', 'daily rewards', 'leaderboard'],
            'signup_steps': 2,
            'cancel_steps': 8,
            'cancel_requirements': ['call to cancel', 'survey required'],
            'reward_schedule': 'variable'
        },
        'pricing': {
            'prices': [
                {'name': 'Basic', 'displayed_price': 9.99},
                {'name': 'Pro', 'displayed_price': 19.99},
                {'name': 'Enterprise', 'displayed_price': 24.99}
            ],
            'original_prices': [19.99, 39.99, 49.99],
            'urgency_elements': ['Only 3 left in stock!', 'Sale ends in 2:34:21']
        }
    }

    sample_user = {
        'age': 72,
        'cognitive_indicators': ['processing_speed_decline'],
        'emotional_state': 'loneliness',
        'social_connection_score': 0.2,
        'digital_literacy_score': 0.3
    }

    result = auditor.full_audit(sample_content, sample_user)
    print(result['summary'])
```
```

---

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
        'personalization_susceptibility': {
            'techniques': ['personalization', 'susceptibility_timing'],
            'multiplier': 1.7,
            'mechanism': 'Personalized content delivered at susceptible moments',
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
            'text': [r'(?i)(danger|risk|threat|warning|protect|afraid|worried|susceptible)'],
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

### 5.2 Susceptibility Timing Detector

```python
class SusceptibilityTimingDetector:
    """
    Detects leveraging of temporal susceptibility windows.

    Research: Decision quality varies with time of day, emotional state,
    and cognitive depletion.
    """

    CIRCADIAN_SUSCEPTIBILITY = {
        'early_morning': {
            'hours': (5, 7),
            'susceptibility': 'moderate',
            'factor': 'cortisol_spike',
            'description': 'Cortisol awakening response — heightened anxiety, reactive decisions'
        },
        'mid_morning': {
            'hours': (9, 11),
            'susceptibility': 'low',
            'factor': 'peak_cognition',
            'description': 'Peak cognitive function — best analytical processing'
        },
        'post_lunch': {
            'hours': (13, 15),
            'susceptibility': 'moderate',
            'factor': 'postprandial_dip',
            'description': 'Post-meal cognitive dip — reduced analytical capacity'
        },
        'late_afternoon': {
            'hours': (16, 18),
            'susceptibility': 'moderate',
            'factor': 'decision_fatigue_accumulation',
            'description': 'Accumulated decision fatigue — defaults more attractive'
        },
        'evening': {
            'hours': (20, 22),
            'susceptibility': 'high',
            'factor': 'ego_depletion',
            'description': 'Ego depletion + relaxation — reduced self-control'
        },
        'late_night': {
            'hours': (23, 4),
            'susceptibility': 'very_high',
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

    EMOTIONAL_SUSCEPTIBILITY_SIGNALS = [
        r'(?i)(just (lost|broke up|got fired|received bad news|diagnosed))',
        r'(?i)(feeling (down|sad|angry|lonely|overwhelmed|stressed|anxious))',
        r'(?i)(can\'t (sleep|stop thinking|cope|handle))',
        r'(?i)(need (help|comfort|support|relief|escape))'
    ]

    SUSCEPTIBLE_DAYS = {
        'post_payday': {'day_offset': (0, 3), 'susceptibility': 'spending_impulse'},
        'friday_evening': {'susceptibility': 'reward_seeking'},
        'sunday_evening': {'susceptibility': 'anxiety_anticipation'},
        'month_end': {'day_offset': (28, 31), 'susceptibility': 'financial_stress'},
        'holidays': {'susceptibility': 'loneliness_or_social_pressure'}
    }

    def assess_timing_susceptibility(self, timestamp: Dict, user_context: Dict = None) -> Dict:
        """
        Assess susceptibility based on timing context.

        Args:
            timestamp: Dict with 'hour', 'day_of_week', 'day_of_month'
            user_context: Optional dict with 'decisions_today', 'emotional_signals',
                         'recent_events'
        """
        hour = timestamp.get('hour', 12)
        day_of_week = timestamp.get('day_of_week', 'monday')
        day_of_month = timestamp.get('day_of_month', 15)

        susceptibilities = []
        risk_score = 0.0

        # Circadian check
        for window_name, window in self.CIRCADIAN_SUSCEPTIBILITY.items():
            h_start, h_end = window['hours']
            if h_start <= hour <= h_end or (h_start > h_end and (hour >= h_start or hour <= h_end)):
                susceptibilities.append({
                    'type': 'circadian',
                    'window': window_name,
                    'susceptibility': window['susceptibility'],
                    'factor': window['factor'],
                    'description': window['description']
                })
                risk_addition = {'low': 0.1, 'moderate': 0.2, 'high': 0.3, 'very_high': 0.4}
                risk_score += risk_addition.get(window['susceptibility'], 0)

        # Decision fatigue
        if user_context:
            decisions = user_context.get('decisions_today', 0)
            fatigue_reduction = decisions * self.DECISION_FATIGUE_THRESHOLDS['quality_reduction_per_10_decisions'] / 10
            if fatigue_reduction > 0.1:
                susceptibilities.append({
                    'type': 'decision_fatigue',
                    'decisions_today': decisions,
                    'estimated_quality_reduction': f"{fatigue_reduction * 100:.0f}%"
                })
                risk_score += min(0.3, fatigue_reduction)

            # Emotional signals
            emotional_text = user_context.get('emotional_signals', '')
            if emotional_text:
                for pattern in self.EMOTIONAL_SUSCEPTIBILITY_SIGNALS:
                    if re.search(pattern, emotional_text):
                        susceptibilities.append({
                            'type': 'emotional_susceptibility',
                            'signal': emotional_text[:100]
                        })
                        risk_score += 0.3
                        break

        # Day-based susceptibility
        if day_of_week.lower() == 'friday' and hour >= 17:
            susceptibilities.append({'type': 'temporal', 'window': 'friday_evening'})
            risk_score += 0.1
        if day_of_week.lower() == 'sunday' and hour >= 18:
            susceptibilities.append({'type': 'temporal', 'window': 'sunday_evening'})
            risk_score += 0.1
        if day_of_month <= 3:
            susceptibilities.append({'type': 'temporal', 'window': 'post_payday'})
            risk_score += 0.15

        return {
            'susceptibilities': susceptibilities,
            'susceptibility_count': len(susceptibilities),
            'risk_score': min(1.0, risk_score),
            'recommendation': self._recommend_action(risk_score)
        }

    def _recommend_action(self, risk_score: float) -> str:
        if risk_score > 0.6:
            return 'DELAY_DECISION: High susceptibility — implement cooling-off period'
        elif risk_score > 0.3:
            return 'CAUTION: Moderate susceptibility — add friction before irreversible actions'
        return 'STANDARD: Normal susceptibility level'
```

---

### 5.3 Trust Leverage Sequence Detector

```python
class TrustLeverageSequenceDetector:
    """
    Detects structured trust-building sequences designed
    to leverage trust for persuasion.

    8 stages of trust leverage identified.
    """

    class TrustStage(Enum):
        INITIAL_CONTACT = "initial_contact"
        VALUE_DELIVERY = "value_delivery"
        RAPPORT_BUILDING = "rapport_building"
        SUSCEPTIBILITY_EXCHANGE = "susceptibility_exchange"
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
        'susceptibility_exchange': [
            r'(?i)(I\'ll be honest|between you and me|I don\'t usually share)',
            r'(?i)(can I be (real|honest|susceptible)|I trust you (enough|with))'
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
        'asymmetric_susceptibility': 'One party shares much more than the other',
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

> **Analytical Layer: Detection Combinations (2–3 technique stacks)**
> This table ranks the **15 most common technique combinations** that the detection code in this file is designed to flag.
> Combinations are named by their user-facing behavioral pattern (what a person experiences).
> The Source Reference section (§5.10.6) contains the **code implementation** of a parallel ranking where
> combinations are named by technical enum values — same underlying research, different vocabulary.
>
> This is one of four effectiveness layers across the Linguistic Persuasion system:
>
> | Layer | Prompt | What It Ranks | Scale |
> |-------|--------|---------------|-------|
> | 1 — Linguistic devices | Prompt 2 | Single language techniques in isolation | Score /100 |
> | 2 — Psychological mechanisms | Prompt 3 | Single persuasion mechanisms | % susceptibility increase |
> | **3 — Detection combinations** | **Prompt 4 (this section)** | **2–3 technique combos for detection code** | **Multiplier (1.28x–2.1x)** |
> | 4 — Expanded combinations | Prompt 5 | 2–4 technique combos (40 ranks, 6 tiers) | Multiplier (1.05x–2.5x) |
>
> Prompt 5 extends this to 40 ranks with 4-technique stacks, which is why its Rank 1 (2.5x) is higher than
> this table's Rank 1 (2.1x) — the 3-technique version of that same combo appears as Prompt 5's Rank 3 at 2.1x.

Research-derived rankings of persuasion technique combinations by measured effectiveness multiplier:

| Rank | Combination | Multiplier | Primary Countermeasure |
|------|------------|-----------|-----------------|
| 1 | Emotional fractionation + commercial relief | **2.1x** | Awareness of cycling pattern; pause before purchase |
| 2 | Scarcity + social proof + urgency | **1.95x** | Verify scarcity claims; check if offer returns |
| 3 | Authority + fear + solution product | **1.85x** | Verify authority credentials; seek second opinion |
| 4 | Personalization + susceptibility timing | **1.82x** | Be aware of timing; avoid decisions when depleted |
| 5 | Identity lock-in + sunk cost + social proof | **1.78x** | Calculate actual value; ignore sunk costs |
| 6 | Anchoring + decoy + scarcity | **1.72x** | Research market prices independently |
| 7 | Reciprocity + commitment escalation | **1.68x** | Recognize gift ≠ obligation; evaluate each ask independently |
| 8 | Trust building + isolation + urgency | **1.65x** | Maintain outside counsel; impose cooling-off periods |
| 9 | Gamification + variable reward + sunk cost | **1.62x** | Set time/money limits; track actual utility vs. engagement |
| 10 | Social comparison + shame + solution | **1.58x** | Recognize comparison influence; define own metrics |
| 11 | Curiosity gap + information asymmetry + authority | **1.52x** | Recognize clickbait structure; verify claims |
| 12 | Default bias + friction asymmetry + commitment | **1.48x** | Actively review defaults; question pre-selections |
| 13 | Nostalgia + identity + community | **1.42x** | Recognize emotional appeal; evaluate offer objectively |
| 14 | Pain agitation + urgency + social proof | **1.35x** | Acknowledge pain without panic; research solutions |
| 15 | Repetition + familiarity + mere exposure | **1.28x** | Recognize familiarity ≠ quality; compare alternatives |

**Countermeasures for Top 5 Combinations:**

1. **Fractionation + commercial relief (2.1x):** Recognize when content alternates fear/anger with joy/relief. The product/service appearing during the "relief" phase is leveraging reduced critical thinking. Countermeasure: pause, leave the environment, return later.

2. **Scarcity + social proof + urgency (1.95x):** "Only 3 left, 47 people viewing, offer expires in 2 hours." Countermeasure: close the page, check if the offer returns tomorrow (it usually does).

3. **Authority + fear + solution (1.85x):** "Experts warn of X → but our product addresses it." Countermeasure: verify the authority independently, check if the concern is proportionate.

4. **Personalization + susceptibility timing (1.82x):** Targeted content delivered when you're depleted/emotional. Countermeasure: avoid major decisions late at night or when stressed.

5. **Identity lock-in + sunk cost + social proof (1.78x):** "You've invested 200 hours, your friends are here, this is who you are." Countermeasure: evaluate current value, not past investment.

---

### 5.7 Temporal Intensity Detector

```python
class TemporalIntensityDetector:
    """
    Detects temporal patterns in persuasion intensity.
    """

    SUSCEPTIBILITY_WINDOWS = {
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
        'critical_threshold': 30,     # Below this = highly susceptible
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
        Analyze temporal pattern of content delivery for intensity.

        Args:
            content_timeline: List of {'timestamp': datetime_str, 'type': str,
                             'intensity': float, 'persuasion_score': float}
        """
        if not content_timeline:
            return {'analyzed': False}

        # Check if high-intensity content clusters at susceptible times
        susceptible_delivery = 0
        total_items = len(content_timeline)

        for item in content_timeline:
            hour = item.get('hour', 12)
            intensity = item.get('persuasion_score', 0)

            for window_name, window in self.SUSCEPTIBILITY_WINDOWS.items():
                h_start, h_end = window['hours']
                in_window = (h_start <= hour <= h_end) if h_start < h_end else (hour >= h_start or hour <= h_end)

                if in_window and intensity > 0.5:
                    susceptible_delivery += 1

        intensity_ratio = susceptible_delivery / total_items if total_items > 0 else 0

        return {
            'total_items': total_items,
            'susceptible_time_delivery': susceptible_delivery,
            'intensity_ratio': round(intensity_ratio, 2),
            'deliberate_timing': intensity_ratio > 0.5,
            'risk_score': min(1.0, intensity_ratio * 1.5)
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
            'susceptibility_level': 'critical' if capacity < self.DECISION_FATIGUE_MODEL['critical_threshold']
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
        'developmental_susceptibility': {
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
        'emotional_state_susceptibility': {
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

    def assess_susceptibility(self, behavioral_data: Dict) -> Dict:
        """
        Assess susceptibility using precise behavioral indicators.

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
            'overall_susceptibility': round(overall_risk, 2),
            'risk_level': 'critical' if overall_risk > 0.7 else 'high' if overall_risk > 0.5 else 'moderate' if overall_risk > 0.3 else 'low',
            'protective_actions': self._recommend_protections(active_indicators)
        }

    def _recommend_protections(self, indicators: Dict) -> List[str]:
        """Generate protective action recommendations"""
        protections = []
        if 'developmental_susceptibility' in indicators:
            protections.append('Apply age-appropriate content restrictions')
        if 'impulse_control_deficit' in indicators:
            protections.append('Implement mandatory cooling-off period before purchases')
        if 'cognitive_depletion' in indicators:
            protections.append('Delay important decisions until cognitive capacity restored')
        if 'limited_social_network' in indicators:
            protections.append('Seek external input before major decisions')
        if 'emotional_state_susceptibility' in indicators:
            protections.append('Increase decision friction during emotional susceptibility periods')
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


### 5.10 Source Reference: High-Impact Detection Systems (Original Implementations)

> The following subsections preserve the original complete implementations from the source
> detection systems. These are retained verbatim for zero-loss consolidation verification.

#### 5.10.1 Original SynergisticStackingDetector (Full Implementation)

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
                r'susceptible', r'exposed', r'attack'
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

#### 5.10.2 Original SusceptibilityTimingDetector (Full Implementation)

```python
from datetime import datetime, timezone
from typing import Optional

class SusceptibilityWindow(Enum):
    CIRCADIAN_LOW = "circadian_cognitive_low"  # 2-4 AM
    DECISION_FATIGUE = "decision_fatigue_window"
    EMOTIONAL_DISTRESS = "emotional_susceptibility"
    POST_NOTIFICATION = "notification_arousal_window"
    WORK_STRESS = "end_of_workday"
    WEEKEND_RELAXED = "weekend_reduced_vigilance"
    PAYCHECK = "post_paycheck_spending"
    LATE_NIGHT = "late_night_impulse"
    MORNING_RUSH = "morning_decision_pressure"

@dataclass
class TimingIntensityAnalysis:
    """Analysis of susceptibility timing intensity"""
    susceptibility_windows_targeted: List[SusceptibilityWindow] = field(default_factory=list)
    timing_intensity_score: float = 0.0
    temporal_patterns: List[Dict] = field(default_factory=list)
    notification_timing_suspicious: bool = False
    circadian_intensity: bool = False
    decision_fatigue_intensity: bool = False
    emotional_state_intensity: bool = False
    recommendations: List[str] = field(default_factory=list)

class SusceptibilityTimingDetector:
    """
    Detects when content/notifications are timed to leverage susceptibility windows.

    Research basis:
    - 2-4 AM decisions show 40%+ reduced critical thinking
    - TikTok emotional state detection: 94% accuracy
    - Decision fatigue: After 10-15 choices, compliance +35%
    - Post-notification arousal window: 2-5 minutes elevated suggestibility
    """

    # Circadian susceptibility hours (local time)
    CIRCADIAN_SUSCEPTIBILITY = {
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

    # Emotional state indicators that predict susceptibility
    EMOTIONAL_SUSCEPTIBILITY_SIGNALS = {
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
        Analyze whether content timing leverages susceptibility windows.

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

        # 1. Check circadian susceptibility
        circadian_risk = self._check_circadian_susceptibility(hour)
        if circadian_risk:
            analysis.circadian_intensity = True
            analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.CIRCADIAN_LOW)
            analysis.timing_intensity_score += circadian_risk
            analysis.temporal_patterns.append({
                'type': 'circadian',
                'hour': hour,
                'risk_level': circadian_risk
            })

        # 2. Check for late night targeting
        if 22 <= hour or hour < 6:
            analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.LATE_NIGHT)
            analysis.timing_intensity_score += 0.2

        # 3. Check decision fatigue
        if user_id:
            decision_count = self.user_decision_count.get(user_id, 0)
            fatigue_level = self._assess_decision_fatigue(decision_count)

            if fatigue_level:
                analysis.decision_fatigue_intensity = True
                analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.DECISION_FATIGUE)
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
                analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.POST_NOTIFICATION)
                analysis.timing_intensity_score += 0.3

        # 5. Check emotional state intensity
        if user_behavior:
            emotional_intensity = self._check_emotional_intensity(
                user_behavior,
                content
            )
            if emotional_intensity['targeted']:
                analysis.emotional_state_intensity = True
                analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.EMOTIONAL_DISTRESS)
                analysis.timing_intensity_score += emotional_intensity['score']

        # 6. Check work/weekend patterns
        if 17 <= hour <= 19 and day_of_week < 5:  # Weekday evening
            analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.WORK_STRESS)
            analysis.timing_intensity_score += 0.1

        if day_of_week >= 5 and 10 <= hour <= 14:  # Weekend midday
            analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.WEEKEND_RELAXED)
            analysis.timing_intensity_score += 0.1

        # 7. Check paycheck timing (if available)
        if dt.day in [1, 15, 28, 29, 30, 31]:  # Common paycheck days
            analysis.susceptibility_windows_targeted.append(SusceptibilityWindow.PAYCHECK)
            analysis.timing_intensity_score += 0.15

        # Normalize score
        analysis.timing_intensity_score = min(1.0, analysis.timing_intensity_score)

        # Generate recommendations
        analysis.recommendations = self._generate_recommendations(analysis)

        return analysis

    def _check_circadian_susceptibility(self, hour: int) -> float:
        """Check if hour falls in circadian susceptibility window"""
        for start, end in self.CIRCADIAN_SUSCEPTIBILITY['severe']:
            if start <= hour < end:
                return 0.5

        for start, end in self.CIRCADIAN_SUSCEPTIBILITY['moderate']:
            if start <= hour < end:
                return 0.3

        for start, end in self.CIRCADIAN_SUSCEPTIBILITY['mild']:
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
            for emotion, patterns in self.EMOTIONAL_SUSCEPTIBILITY_SIGNALS['text_patterns'].items():
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
            'anxiety': [r'peace of mind', r'analysis', r'security', r'don\'t worry', r'safe'],
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
```

#### 5.10.3 Original TrustLeverageSequenceDetector (Full Implementation)

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

#### 5.10.4 Original PhysiologicalBypassDetector (Full Implementation)

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
            'lose', 'miss', 'fail', 'risk', 'susceptible', 'exposed',
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
```

#### 5.10.5 Original AIAmplificationDetector (Full Implementation)

```python
class AIAmplificationType(Enum):
    LLM_PERSONALIZATION = "personalized_persuasion"
    SYNTHETIC_SOCIAL_PROOF = "fake_engagement"
    BOT_COORDINATION = "coordinated_inauthentic"
    DEEPFAKE_AUTHORITY = "synthetic_credibility"
    ALGORITHMIC_TARGETING = "susceptibility_targeting"
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

        # Check for susceptibility targeting
        if any(t in str(metadata) for t in ['emotional_state', 'life_event', 'financial_distress']):
            result['targeting_factors'].append('susceptibility_targeting')
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

#### 5.10.6 Original RankedCombinationDetector (Full Implementation)

```python
@dataclass
class CombinationEffectiveness:
    """Ranked effectiveness of influence combinations"""
    rank: int
    combination: Tuple[str, ...]
    effectiveness_multiplier: float
    mechanism: str
    target_susceptibility: str
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
            target_susceptibility="Working memory saturation during stress response",
            research_source="Decision fatigue + amygdala hijack research",
            detection_difficulty=0.7,
            typical_application="High-pressure sales, crisis intensity, scam calls"
        ),
        CombinationEffectiveness(
            rank=2,
            combination=("authority", "fear", "urgency"),
            effectiveness_multiplier=1.95,
            mechanism="Credible threat + immediate action requirement = compliance without verification",
            target_susceptibility="Threat response overrides verification instinct",
            research_source="Phishing effectiveness studies, scam analysis",
            detection_difficulty=0.6,
            typical_application="Tech support scams, IRS scams, security alerts"
        ),
        CombinationEffectiveness(
            rank=3,
            combination=("variable_reward", "streak", "social_proof"),
            effectiveness_multiplier=1.85,
            mechanism="Gambling mechanics + loss aversion + peer validation = compulsive engagement",
            target_susceptibility="Dopamine reward pathway + social comparison",
            research_source="Gamification engagement research, mobile game studies",
            detection_difficulty=0.4,
            typical_application="Mobile games, social media, fitness apps"
        ),
        CombinationEffectiveness(
            rank=4,
            combination=("personalization", "scarcity", "social_proof"),
            effectiveness_multiplier=1.78,
            mechanism="Personal relevance + limited availability + others buying = FOMO + action",
            target_susceptibility="Identity + loss aversion + conformity",
            research_source="E-commerce conversion optimization studies",
            detection_difficulty=0.5,
            typical_application="E-commerce, flash sales, limited editions"
        ),
        CombinationEffectiveness(
            rank=5,
            combination=("trust_building", "reciprocity", "commitment_escalation"),
            effectiveness_multiplier=1.72,
            mechanism="Established relationship + gift obligation + prior compliance = large request acceptance",
            target_susceptibility="Reciprocity norm + consistency drive",
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
            target_susceptibility="Dopamine seeking + completion drive absence",
            research_source="Social media engagement research, CHI 2024",
            detection_difficulty=0.3,
            typical_application="Social media feeds, content platforms"
        ),
        CombinationEffectiveness(
            rank=7,
            combination=("anchoring", "decoy", "urgency"),
            effectiveness_multiplier=1.58,
            mechanism="Price reference + inferior comparison + time limit = target option selection",
            target_susceptibility="Reference point bias + comparison heuristic",
            research_source="Behavioral economics pricing studies",
            detection_difficulty=0.4,
            typical_application="Subscription pricing, SaaS plans, retail"
        ),
        CombinationEffectiveness(
            rank=8,
            combination=("authority", "social_proof", "personalization"),
            effectiveness_multiplier=1.52,
            mechanism="Expert endorsement + crowd validation + personal relevance = trust",
            target_susceptibility="Authority deference + conformity + relevance filter",
            research_source="Influencer marketing studies",
            detection_difficulty=0.5,
            typical_application="Health products, financial services, courses"
        ),
        CombinationEffectiveness(
            rank=9,
            combination=("fear", "scarcity", "loss_framing"),
            effectiveness_multiplier=1.48,
            mechanism="Threat awareness + limited opportunity + loss emphasis = action to avoid negative",
            target_susceptibility="Loss aversion (2x pain of loss vs gain)",
            research_source="Prospect theory applications",
            detection_difficulty=0.4,
            typical_application="Insurance, security products, limited offers"
        ),
        CombinationEffectiveness(
            rank=10,
            combination=("asmr_relaxation", "authority", "suggestion"),
            effectiveness_multiplier=1.45,
            mechanism="Reduced critical faculty + trusted source + direct suggestion = acceptance",
            target_susceptibility="Lowered analytical resistance in relaxed state",
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
            target_susceptibility="Guilt avoidance + consistency need",
            research_source="Donation and subscription retention studies",
            detection_difficulty=0.5,
            typical_application="Charity solicitation, subscription cancellation"
        ),
        CombinationEffectiveness(
            rank=12,
            combination=("scarcity", "social_proof"),
            effectiveness_multiplier=1.40,
            mechanism="Limited availability validated by crowd demand",
            target_susceptibility="FOMO + conformity",
            research_source="Cialdini combination studies",
            detection_difficulty=0.3,
            typical_application="Basic e-commerce, event tickets"
        ),
        CombinationEffectiveness(
            rank=13,
            combination=("liking", "reciprocity"),
            effectiveness_multiplier=1.35,
            mechanism="Positive relationship + gift = obligation from friend",
            target_susceptibility="Social bond + reciprocity norm",
            research_source="Influencer marketing, MLM research",
            detection_difficulty=0.6,
            typical_application="MLM, friend referrals, influencer affiliate"
        ),
        CombinationEffectiveness(
            rank=14,
            combination=("authority", "social_proof"),
            effectiveness_multiplier=1.32,
            mechanism="Expert endorsement + crowd validation",
            target_susceptibility="Dual verification heuristic",
            research_source="Advertising effectiveness studies",
            detection_difficulty=0.3,
            typical_application="Traditional advertising, product reviews"
        ),
        CombinationEffectiveness(
            rank=15,
            combination=("urgency", "scarcity"),
            effectiveness_multiplier=1.28,
            mechanism="Time + quantity limits",
            target_susceptibility="Fear of missing out",
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
                "PAUSE: When feeling overwhelmed AND emotional AND pressured, this is the most significant combination",
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
                "PERSONALIZATION AWARENESS: 'For you' = targeted susceptibility",
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

#### 5.10.7 Original TemporalIntensityDetector (Full Implementation)

```python
from datetime import datetime, timedelta
from typing import NamedTuple

class TemporalWindow(NamedTuple):
    """A susceptibility window with severity"""
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

    # Susceptibility windows ranked by severity
    SUSCEPTIBILITY_WINDOWS: List[TemporalWindow] = [
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

    # Days with heightened susceptibility
    SUSCEPTIBLE_DAYS = {
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
        Analyze whether content delivery time leverages susceptibility windows.
        """
        analysis = {
            'timestamp': timestamp,
            'datetime': datetime.fromtimestamp(timestamp).isoformat(),
            'susceptibility_windows_active': [],
            'circadian_susceptibility': 0.0,
            'day_susceptibility': 0.0,
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

        # 1. Check circadian susceptibility windows
        for window in self.SUSCEPTIBILITY_WINDOWS:
            start, end = window.hours
            if start <= hour < end:
                analysis['susceptibility_windows_active'].append({
                    'window': window.name,
                    'severity': window.severity,
                    'mechanism': window.mechanism
                })
                analysis['circadian_susceptibility'] = max(
                    analysis['circadian_susceptibility'],
                    window.severity
                )

        # 2. Check day-based susceptibility
        for vuln_type, config in self.SUSCEPTIBLE_DAYS.items():
            if 'days' in config and day in config['days']:
                analysis['day_susceptibility'] += config['severity']
                analysis['susceptibility_windows_active'].append({
                    'window': vuln_type,
                    'severity': config['severity'],
                    'mechanism': config['mechanism']
                })

            if 'days_of_week' in config and weekday in config['days_of_week']:
                analysis['day_susceptibility'] += config['severity']
                analysis['susceptibility_windows_active'].append({
                    'window': vuln_type,
                    'severity': config['severity'],
                    'mechanism': config['mechanism']
                })

        # 3. Check decision fatigue (if tracking user)
        if user_id:
            fatigue = self._calculate_decision_fatigue(user_id, timestamp)
            analysis['decision_fatigue_level'] = fatigue['level']

            if fatigue['level'] > 0.5:
                analysis['susceptibility_windows_active'].append({
                    'window': 'decision_fatigue',
                    'severity': fatigue['level'],
                    'mechanism': f"User has made approximately {fatigue['estimated_decisions']} decisions. Compliance increases {int(fatigue['compliance_boost']*100)}%."
                })

        # 4. Check notification timing intensity
        if user_id:
            notif_analysis = self._check_notification_timing(user_id, timestamp)
            if notif_analysis['within_window']:
                analysis['notification_intensity'] = True
                analysis['susceptibility_windows_active'].append({
                    'window': f"post_notification_{notif_analysis['window_type']}",
                    'severity': notif_analysis['severity'],
                    'mechanism': f"Content delivered {notif_analysis['seconds_since_notification']:.0f} seconds after notification during arousal window."
                })

        # 5. Calculate combined risk
        analysis['combined_temporal_risk'] = min(1.0,
            analysis['circadian_susceptibility'] * 0.4 +
            analysis['day_susceptibility'] * 0.2 +
            analysis['decision_fatigue_level'] * 0.25 +
            (0.15 if analysis['notification_intensity'] else 0)
        )

        # 6. Determine if this is optimal decision time
        if (analysis['circadian_susceptibility'] < 0.2 and
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

        if analysis['circadian_susceptibility'] > 0.6:
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

        if analysis['day_susceptibility'] > 0.2:
            recommendations.append(
                "TIMING CONSIDERATION: This day carries additional susceptibility factors. "
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
                    "NEUTRAL TIMING: No major temporal susceptibilities detected, "
                    "but always take time to verify before major decisions."
                )

        return recommendations
```

#### 5.10.8 Original PreciseBehavioralIndicatorDetector (Full Implementation)

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
    EMOTIONAL_STATE_SUSCEPTIBILITY = "emotional_state_susceptibility"

@dataclass
class BehavioralIndicator:
    """A specific behavioral indicator with clinical precision"""
    indicator_name: str
    observable_behaviors: List[str]
    cognitive_mechanism: str
    susceptibility_increase: float
    analytical_framework: str

@dataclass
class PreciseSusceptibilityProfile:
    """Detailed susceptibility profile using clinical indicators"""
    active_factors: List[SusceptibilityFactor] = field(default_factory=list)
    behavioral_indicators: List[BehavioralIndicator] = field(default_factory=list)
    cognitive_patterns: List[CognitiveProcessingPattern] = field(default_factory=list)
    estimated_susceptibility_increase: float = 0.0
    high_risk_influence_types: List[str] = field(default_factory=list)
    recommended_analytics: List[str] = field(default_factory=list)

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
            analytical_framework="Adult co-viewing and explicit discussion of persuasive intent. Content gatekeeping."
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
            analytical_framework="Structured decision delays. Explicit teaching of influence tactics."
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
            analytical_framework="Rest before important decisions. Reduce decision count. Use checklists to externalize analysis."
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
            analytical_framework="Mandatory consultation with trusted others before major decisions. Structured social connection."
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
            analytical_framework="Explicit verbal explanation of influence tactics. Written/visual guides. Trusted advisor consultation."
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
            analytical_framework="Mandatory cooling-off periods during emotional states. Pre-commitment to decision delays."
        ),
    }

    FACTOR_SUSCEPTIBILITY_MAPPING = {
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
        SusceptibilityFactor.EMOTIONAL_STATE_SUSCEPTIBILITY: [
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
            profile.active_factors.append(SusceptibilityFactor.EMOTIONAL_STATE_SUSCEPTIBILITY)
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

        # Map susceptibilities
        for factor in profile.active_factors:
            if factor in self.FACTOR_SUSCEPTIBILITY_MAPPING:
                profile.high_risk_influence_types.extend(self.FACTOR_SUSCEPTIBILITY_MAPPING[factor])

        # Generate protections
        for indicator in profile.behavioral_indicators:
            profile.recommended_analytics.append(indicator.analytical_framework)

        return profile
```

#### 5.10.9 Original InformationEcosystemDetector (Full Implementation)

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

#### 5.10.10 Original MasterHighImpactAuditor (Full Implementation)

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
                'windows_active': [w['window'] for w in temporal['susceptibility_windows_active']],
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
                'protections': susceptibility.recommended_analytics
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

#### 5.10.11 Combination Effectiveness Ranking (Original Appendix)

Rankings based on empirical research:
1. **Effect size** (40%) - Cohen's d from controlled studies
2. **Mechanism synergy** (25%) - How techniques amplify each other
3. **Susceptibility depth** (20%) - How fundamental the intensity
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
        self.timing_detector = SusceptibilityTimingDetector()
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
            'susceptibility_timing': None,
            'trust_leverage': None,
            'physiological_bypass': None,
            'ai_amplification': None,
            'temporal_intensity': None,
            'behavioral_susceptibility': None,
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

        # 2. Susceptibility timing
        if context and 'timestamp' in context:
            timing = self.timing_detector.assess_timing_susceptibility(
                context['timestamp'],
                context.get('user_context')
            )
            report['susceptibility_timing'] = timing
            risk_scores.append(timing['risk_score'])
            if timing['risk_score'] > 0.5:
                report['critical_findings'].append(
                    f"TIMING: Content delivered during susceptibility window "
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
                report['critical_findings'].append("TEMPORAL: Deliberate high-intensity delivery at susceptible times")

        # 7. Behavioral susceptibility
        if context and 'behavioral_data' in context:
            behavioral = self.behavioral_detector.assess_susceptibility(context['behavioral_data'])
            report['behavioral_susceptibility'] = behavioral
            risk_scores.append(behavioral['overall_susceptibility'])
            if behavioral['risk_level'] in ['critical', 'high']:
                report['critical_findings'].append(
                    f"SUSCEPTIBILITY: {behavioral['risk_level']} behavioral susceptibility "
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

        if report.get('susceptibility_timing', {}).get('risk_score', 0) > 0.5:
            actions.append('Implement cooling-off periods for decisions during susceptible windows')

        if report.get('physiological_bypass', {}).get('bypass_mechanisms_detected', 0) >= 2:
            actions.append('Add friction/breaks to counter physiological bypass mechanisms')

        if report.get('ai_amplification', {}).get('amplification_risk') == 'high':
            actions.append('Flag as potentially AI-generated; verify claims independently')

        bypass = report.get('physiological_bypass', {})
        if 'countermeasures' in bypass:
            actions.extend(bypass['countermeasures'])

        behavioral = report.get('behavioral_susceptibility', {})
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
        self.susceptibility_detector = SusceptiblePopulationDetector()
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
            user_profile: Optional user susceptibility profile
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
            'susceptibility_assessment': None,
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

        # === SUSCEPTIBILITY ASSESSMENT ===
        if user_profile:
            vuln_profile = self.susceptibility_detector.assess_individual_susceptibility(user_profile)
            report['susceptibility_assessment'] = {
                'score': vuln_profile['overall_susceptibility_score'],
                'factors': vuln_profile['factors'],
                'risk_areas': vuln_profile['risk_areas'],
                'recommendations': vuln_profile['protective_recommendations']
            }
            if vuln_profile['overall_susceptibility_score'] > 0.5:
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

### High-Susceptibility Populations
- USC Dornsife 2024: Alzheimer's and scam susceptibility
- PNAS Nexus 2024: APOE4 and phishing
- Thorn 2024: Youth online safety data
- Psychology Today 2025: Neurodivergent susceptibility

### AI & Deepfakes
- Science 2025: Political persuasion with AI
- Nature 2025: LLM persuasive power meta-analysis (81.7% increase)
- PMC 2025: Deepfake forensics survey
- Deloitte 2025: Deepfake disruption report

### Countermeasure Research
- Sage 2024: Media literacy meta-analysis (N=81,155, d=0.60)
- Taiwan 2024: Adolescent media literacy study
- Compton & Pfau: Inoculation theory (d=0.36)
- CHI 2025: Design friction studies (d=0.45)

### Regulatory
- FTC 2024: Amazon, Adobe enforcement actions
- EU DSA 2024: Implementation and enforcement
- EU AI Act: Phased implementation
- CCPA/CPRA: California interface design pattern prohibitions
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
HIGH-SUSCEPTIBILITY AUDIENCES
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

- **0-25 (Low-Intensity):** Clear value proposition, no exclusion tactics, transparent about benefits
  - Example: "Quality water bottles. Durable design. Made in the USA."

- **26-50 (Some Targeting):** Audience-specific messaging without exclusion
  - Example: "For coffee lovers: the perfect thermos keeps drinks hot 12 hours."

- **51-75 (Sophisticated):** Multiple primal stimuli, psychological principles, but not misleading
  - Example: Uses PERSONAL + EMOTIONAL but with truthful claims

- **76-100 (Optimized):** Combines multiple frameworks, leverages susceptibilities, obscures truth
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
- [ ] I assessed audience susceptibility accurately
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
