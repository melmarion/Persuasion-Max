# Build a "Grammarly for Persuasion" Tool

## Overview

Create a real-time copy enhancement tool that analyzes text and suggests persuasion improvements, similar to how Grammarly suggests grammar corrections. The tool should provide inline suggestions, explanations, and one-click enhancements.

---

## Core Concept

**Grammarly fixes grammar. This tool enhances persuasion.**

- User writes copy (email, sales page, ad, social post, etc.)
- Tool analyzes persuasion strength in real-time
- Tool highlights weak areas and suggests improvements
- User clicks to accept suggestions or ignore them
- Tool explains WHY each suggestion makes copy more persuasive

---

## Foundation: Use Existing Codebase

This project already contains the detection and generation engines you need:

### **Detection Engine** (`CODE/UNIFIED_AUDITOR.py`)
- Analyzes text for 22 persuasion techniques across 3 frameworks
- Scores copy on 0-100 scale
- Identifies which techniques are present/missing
- Generates "red flags" for areas needing improvement

### **Generation Engine** (`CODE/UNIFIED_GENERATOR.py`)
- Enhances text with specific persuasion techniques
- Supports 22 techniques with 200+ templates
- Calculates synergy between techniques
- Verifies output quality

### **Research Foundation** (10+ framework documents in `DETECTION/` folder)
- Complete pattern definitions for all 22 techniques
- Examples and detection markers
- Intensity scoring methodology

---

## Required Features

### 1. **Real-Time Analysis**
As the user types, continuously analyze:
- **Persuasion Score**: 0-100 overall effectiveness rating
- **Technique Coverage**: Which of the 22 techniques are present
- **Gaps**: Which high-impact techniques are missing
- **Intensity Level**: Subtle → Moderate → Strong → Maximum

### 2. **Inline Suggestions**
Highlight text segments with improvement opportunities:

```
ORIGINAL TEXT (highlighted in yellow):
"Our product is available now."

SUGGESTION CARD:
❌ Weak persuasion (Score: 15/100)
💡 Add urgency + scarcity
✏️ Suggested rewrite: "Join 500+ customers who secured their spot this week—only 12 units left at this price."
📊 Impact: +65 points (urgency, social proof, scarcity)
[Accept] [Edit] [Ignore]
```

### 3. **Technique Suggestions**
Recommend which techniques to add based on:
- **Copy type** (email subject, headline, CTA, product description)
- **Current gaps** (missing high-impact techniques)
- **Goal** (urgency, trust, action, connection, memory, exclusivity)

Example:
```
DETECTED: Email subject line
CURRENT TECHNIQUES: None detected (Score: 10/100)
RECOMMENDED: Add curiosity + urgency
SUGGESTION: "You're missing out on [benefit]—here's how to fix it before [deadline]"
```

### 4. **Goal-Based Presets**
Let users select their goal, then auto-suggest techniques:

| Goal | Recommended Techniques | Example |
|------|----------------------|---------|
| **Urgency** | Scarcity + Emotional + Framing | "Last chance—price increases in 3 hours" |
| **Trust** | Authority + Social Proof + Unity | "Join 10,000 verified professionals" |
| **Action** | Commitment + Reciprocity + Scarcity | "Claim your free trial (no credit card)—limited spots" |
| **Connection** | Liking + Unity + Personal | "People like you have achieved [result]" |
| **Memory** | Memorable + Rhetorical + Emotional | "Remember when [pain point]? Never again." |
| **Exclusivity** | Personal + Scarcity + Contrastable | "Not for everyone—only serious [audience]" |

### 5. **Before/After Comparison**
Show side-by-side transformation:

```
BEFORE (Score: 22/100)
"Check out our new course on marketing."

AFTER (Score: 78/100)
"Join 1,247 marketers who've already transformed their results—early bird pricing ends Friday."

IMPROVEMENTS:
✓ Social proof added (+25 points)
✓ Urgency added (+20 points)
✓ Tangible results added (+11 points)
```

### 6. **Intensity Control**
Slider to control how aggressive the persuasion is:

```
[Subtle] ----●---- [Moderate] -------- [Strong] -------- [Maximum]

Subtle: "Many professionals find this helpful"
Moderate: "Join 500+ professionals using this daily"
Strong: "Don't miss what 500+ pros already know—act now"
Maximum: "LAST CHANCE: 500+ pros secured their spot. Only 3 left!"
```

### 7. **Explanation Mode**
For each suggestion, explain the psychology:

```
SUGGESTION: Add "Join 10,000+ professionals"

WHY THIS WORKS:
• Social Proof: People follow the actions of others (Cialdini principle)
• Specific Numbers: "10,000+" is more credible than "many"
• Identity Alignment: "professionals" creates in-group connection
• FOMO Activation: Implies others are benefiting, reader is missing out

EXPECTED IMPACT: +28 persuasion points
```

---

## Technical Architecture

### **Option A: Browser Extension** (Like Grammarly)
- Real-time text analysis in Gmail, Google Docs, LinkedIn, etc.
- Inline suggestion cards that appear as user types
- Click to accept/reject suggestions
- Sidebar showing overall persuasion score

**Tech Stack:**
- Frontend: Chrome Extension (JavaScript + React)
- Backend: Python FastAPI server running UNIFIED_AUDITOR + UNIFIED_GENERATOR
- Real-time: WebSocket for live analysis
- Storage: Save user preferences and accepted suggestions

### **Option B: Web App** (Like Hemingway Editor)
- Paste text into editor
- Real-time analysis as user types
- Highlighted suggestions with click-to-apply
- Dashboard showing persuasion metrics

**Tech Stack:**
- Frontend: React + rich text editor (Draft.js, Slate, or Lexical)
- Backend: Python FastAPI with existing detection/generation engines
- Real-time: Debounced API calls on text change

### **Option C: API + Integrations** (Like Grammarly Business)
- RESTful API for third-party integration
- Plugins for Google Docs, Microsoft Word, Notion, etc.
- Embeddable widget for any website

**Tech Stack:**
- API: FastAPI with authentication
- Integrations: Google Docs API, Office Add-ins API
- SDKs: JavaScript, Python client libraries

---

## Core User Workflow

### **Step 1: User Writes Copy**
```
User types in editor:
"We have a new product launching soon. It's really great. Check it out."
```

### **Step 2: Real-Time Analysis**
```
PERSUASION SCORE: 12/100 ⚠️

DETECTED TECHNIQUES: None
MISSING HIGH-IMPACT:
• No urgency (add scarcity/deadline)
• No credibility (add authority/social proof)
• No emotional hook (add pain/relief narrative)
• Vague claims ("really great" is weak)
```

### **Step 3: Inline Suggestions Appear**
```
We have a new product launching soon. It's really great. Check it out.
     ↑                           ↑              ↑
   [Weak]                    [Vague]        [Weak CTA]

SUGGESTIONS:
1. "We have a new product" → "Join 200+ early adopters who've"
2. "It's really great" → "saving an average of 12 hours per week"
3. "Check it out" → "Secure your spot before we sell out (only 15 left)"
```

### **Step 4: User Accepts Suggestions**
```
ENHANCED VERSION: (Score: 74/100 ✓)
"Join 200+ early adopters saving an average of 12 hours per week.
Secure your spot before we sell out—only 15 left at launch pricing."

TECHNIQUES APPLIED:
✓ Social Proof (200+ early adopters)
✓ Tangible Benefit (12 hours per week)
✓ Scarcity (only 15 left)
✓ Urgency (launch pricing)
```

---

## Key Features to Build

### **Must-Have (MVP):**
1. ✅ Real-time persuasion scoring (0-100)
2. ✅ Inline suggestion highlights
3. ✅ Click-to-apply enhancements
4. ✅ Technique detection and gap analysis
5. ✅ Before/after comparison
6. ✅ Explanation of why suggestions work

### **Should-Have (Version 2):**
7. Goal-based presets (urgency, trust, action, etc.)
8. Industry templates (email, ad, sales page, etc.)
9. Intensity slider (subtle → maximum)
10. Learning mode (educate users on persuasion psychology)
11. A/B testing suggestions (show multiple options)
12. Export enhanced copy

### **Nice-to-Have (Future):**
13. Team collaboration features
14. Brand voice consistency checker
15. Compliance checking (intensity thresholds)
16. Performance analytics (which techniques convert best)
17. Integration with marketing tools (Mailchimp, HubSpot, etc.)
18. Custom technique libraries (user-defined patterns)

---

## Data Flow

```
USER INPUT (text)
    ↓
UNIFIED_AUDITOR.audit(text)
    ↓
DETECTION RESULTS:
- Persuasion score: 35/100
- Detected techniques: [AUTHORITY, TANGIBLE]
- Missing techniques: [SCARCITY, SOCIAL_PROOF, URGENCY]
- Red flags: ["Vague claims", "Weak CTA"]
    ↓
SUGGESTION GENERATOR:
For each red flag:
    - Identify target technique to add
    - Use UNIFIED_GENERATOR to create enhanced version
    - Calculate score improvement
    ↓
DISPLAY SUGGESTIONS:
- Highlight weak text
- Show suggestion card
- Display expected impact
- Provide explanation
    ↓
USER ACCEPTS SUGGESTION
    ↓
UPDATE TEXT + RE-ANALYZE
    ↓
NEW SCORE: 78/100 ✓
```

---

## Example Suggestion Cards

### **Suggestion Card 1: Weak CTA**
```
┌─────────────────────────────────────┐
│ ⚠️ WEAK CALL-TO-ACTION (Score: 15) │
├─────────────────────────────────────┤
│ ORIGINAL:                           │
│ "Check it out"                      │
│                                     │
│ 💡 SUGGESTED:                       │
│ "Claim your free trial now (no     │
│ credit card required)"              │
│                                     │
│ WHY THIS WORKS:                     │
│ • Reciprocity: "free" triggers     │
│   obligation                        │
│ • Commitment: "no credit card"     │
│   removes friction                  │
│ • Urgency: "now" creates time      │
│   pressure                          │
│                                     │
│ IMPACT: +42 points                  │
│                                     │
│ [Accept] [Show Alternatives] [Ignore]│
└─────────────────────────────────────┘
```

### **Suggestion Card 2: Missing Social Proof**
```
┌─────────────────────────────────────┐
│ 💡 ADD SOCIAL PROOF (+28 points)   │
├─────────────────────────────────────┤
│ Insert after "our new product":    │
│                                     │
│ "Join 1,500+ professionals who've  │
│ already upgraded their workflow"    │
│                                     │
│ TECHNIQUE: Social Proof             │
│ PSYCHOLOGY: People follow the       │
│ actions of others, especially       │
│ similar others ("professionals")    │
│                                     │
│ [Insert] [Customize] [Ignore]       │
└─────────────────────────────────────┘
```

### **Suggestion Card 3: Vague Claims**
```
┌─────────────────────────────────────┐
│ ❌ VAGUE CLAIM DETECTED              │
├─────────────────────────────────────┤
│ "It's really great"                 │
│ ↓                                   │
│ TOO ABSTRACT - Add tangible details│
│                                     │
│ SUGGESTIONS:                        │
│ • "Save 15 hours per week"         │
│ • "Reduce costs by 40%"            │
│ • "Get results in 48 hours"        │
│                                     │
│ PRINCIPLE: Tangible Stimulus        │
│ Concrete > Abstract                 │
│                                     │
│ [Choose one] [Write custom]         │
└─────────────────────────────────────┘
```

---

## Integration with Existing Code

### **Use UNIFIED_AUDITOR for Detection**
```python
from CODE.UNIFIED_AUDITOR import UnifiedPersuasionAuditor

auditor = UnifiedPersuasionAuditor()

# Analyze user's text
result = auditor.audit(user_text)

# Get persuasion score
score = result.composite_scores['overall']  # 0-100

# Identify gaps (missing techniques)
detected_techniques = result.techniques_detected
all_techniques = ['SCARCITY', 'AUTHORITY', 'SOCIAL_PROOF', ...]
missing = [t for t in all_techniques if t not in detected_techniques]

# Get red flags (areas to improve)
red_flags = result.red_flags  # List of weaknesses
```

### **Use UNIFIED_GENERATOR for Suggestions**
```python
from CODE.UNIFIED_GENERATOR import UnifiedInfluenceGenerator, GenerationConfig

generator = UnifiedInfluenceGenerator()

# Generate enhancement with missing technique
config = GenerationConfig(
    techniques=['SOCIAL_PROOF', 'SCARCITY'],
    intensity='MODERATE'
)

result = generator.enhance(user_text, config)
enhanced_text = result.enhanced_text
improvement = result.verification_score - original_score
```

### **Suggest Techniques Based on Goal**
```python
# User selects "urgency" goal
suggestions = generator.suggest_techniques(goal="urgency")

# Returns:
# {
#   "techniques": ["SCARCITY", "EMOTIONAL", "FRAMING"],
#   "synergy_multiplier": 1.35,
#   "rationale": "These techniques synergize well for urgency goals"
# }
```

---

## User Interface Examples

### **Main Editor View**
```
┌─────────────────────────────────────────────────────────┐
│ Persuasion Score: 45/100 ⚠️                    [Save]   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Our product is available now. It's really great.      │
│      ↑                             ↑                    │
│   [Weak]                        [Vague]                 │
│                                                         │
│  Check it out.                                          │
│      ↑                                                  │
│  [Weak CTA]                                             │
│                                                         │
├─────────────────────────────────────────────────────────┤
│ SUGGESTIONS (3):                                        │
│ • Add social proof (+28 points)                         │
│ • Strengthen CTA (+35 points)                           │
│ • Replace vague claims with tangible benefits (+22)     │
└─────────────────────────────────────────────────────────┘
```

### **Sidebar Analytics**
```
┌──────────────────────────┐
│ PERSUASION ANALYSIS      │
├──────────────────────────┤
│ Overall: 45/100 ⚠️       │
│                          │
│ DETECTED TECHNIQUES:     │
│ ✓ None                   │
│                          │
│ MISSING HIGH-IMPACT:     │
│ ❌ Social Proof          │
│ ❌ Scarcity              │
│ ❌ Urgency               │
│ ❌ Authority             │
│                          │
│ INTENSITY: Subtle        │
│ [━━━━━━━━━━━━━━━━━━━━]   │
│                          │
│ GOAL PRESETS:            │
│ • Urgency                │
│ • Trust                  │
│ • Action ←               │
│ • Connection             │
│                          │
│ [Apply Preset]           │
└──────────────────────────┘
```

---

## Prompt for AI/Developer

Use this exact prompt to build the tool:

---

**PROMPT:**

Build a "Grammarly for Persuasion" tool that analyzes text in real-time and suggests persuasion enhancements.

**Foundation:**
- Use the existing `UNIFIED_AUDITOR.py` for detecting persuasion techniques
- Use the existing `UNIFIED_GENERATOR.py` for generating enhanced copy
- Reference the 22 techniques defined in `DETECTION/` framework documents

**Core Features:**
1. Real-time persuasion scoring (0-100 scale)
2. Inline suggestions that highlight weak areas
3. Click-to-apply enhancements
4. Explanations of why each suggestion works
5. Before/after comparison
6. Goal-based presets (urgency, trust, action, connection, memory, exclusivity)

**User Experience:**
- As user types, continuously analyze and score copy
- Highlight text segments with improvement opportunities
- Show suggestion cards with:
  - Original text
  - Suggested enhancement
  - Psychological explanation
  - Expected score improvement
  - [Accept] [Edit] [Ignore] buttons
- Update score in real-time as suggestions are accepted

**Technical Requirements:**
- Frontend: Web-based rich text editor with real-time highlighting
- Backend: Python FastAPI serving the auditor and generator
- Real-time: Debounced analysis (500ms after user stops typing)
- Display: Inline suggestion cards + sidebar analytics

**Suggestion Logic:**
1. Run `auditor.audit(text)` to get current score and detected techniques
2. Identify gaps (missing high-impact techniques)
3. For each gap, use `generator.enhance()` to create improved version
4. Calculate score improvement
5. Display top 3 suggestions sorted by impact

**Output Format:**
Each suggestion should show:
- Highlighted text needing improvement
- Specific enhancement
- Technique being applied
- Psychology explanation
- Score impact (+X points)

**Use existing codebase patterns:**
- Import detection patterns from `Patterns` class in UNIFIED_AUDITOR.py
- Use `GenerationConfig` for configuring enhancements
- Use `suggest_techniques(goal)` method for goal-based presets
- Use `synergy.calculate_synergy()` for technique combinations

Build this as a web application with a clean, modern interface similar to Hemingway Editor or Grammarly.

---

## Success Criteria

The tool is successful if:

1. ✅ User can paste any copy and immediately see a persuasion score
2. ✅ Weak areas are clearly highlighted with specific suggestions
3. ✅ Suggestions can be applied with one click
4. ✅ Score updates in real-time as improvements are made
5. ✅ Users understand WHY suggestions make copy more persuasive
6. ✅ Enhanced copy scores 60+ points higher than original
7. ✅ Tool works for common copy types: emails, ads, sales pages, CTAs
8. ✅ Interface is intuitive enough that non-experts can use it

---

## Next Steps

1. **Choose architecture**: Browser extension, web app, or API?
2. **Set up development environment**: Install Python, FastAPI, React
3. **Import existing code**: Copy UNIFIED_AUDITOR.py and UNIFIED_GENERATOR.py
4. **Build MVP**: Basic editor + real-time scoring + 1-2 suggestion types
5. **Test with real copy**: Email subjects, headlines, product descriptions
6. **Iterate based on feedback**: Add more suggestion types, improve UX
7. **Add advanced features**: Goal presets, intensity slider, A/B testing

---

## Example Use Cases

### **Use Case 1: Email Subject Line**
```
INPUT: "Newsletter for this week"
SCORE: 8/100

SUGGESTION: "You're missing out on [benefit]—here's what 500+ subscribers discovered this week"
SCORE: 72/100

TECHNIQUES: Curiosity + FOMO + Social Proof + Personal
```

### **Use Case 2: Product Description**
```
INPUT: "High-quality software for teams"
SCORE: 18/100

SUGGESTION: "Join 2,400+ teams saving 15 hours/week with our platform—see results in 48 hours or your money back"
SCORE: 81/100

TECHNIQUES: Social Proof + Tangible + Urgency + Reciprocity
```

### **Use Case 3: CTA Button**
```
INPUT: "Learn more"
SCORE: 12/100

SUGGESTION: "Start your free trial (no credit card required)"
SCORE: 68/100

TECHNIQUES: Commitment + Reciprocity + Friction Removal
```

---

## Language Guidelines

Follow the neutral professional language standards defined in `CLAUDE.md`:

- Use "influence technique" not "manipulation"
- Use "behavioral influence" not "dark pattern"
- Use "interface design pattern" not "deceptive pattern"
- Use "intensity" not "exploitation"

The tool should:
- Educate users about persuasion psychology
- Include option to check compliance with intensity thresholds
- Default to MODERATE intensity, not EXTREME

---

**This prompt contains everything needed to build a "Grammarly for Persuasion" tool using your existing codebase as the foundation.**
