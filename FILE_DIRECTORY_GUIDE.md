# PERSUASION MAX - FILE DIRECTORY
## Two-Domain Organization: UX/UI Engagement + Linguistic Persuasion

---

## QUICK START FOR DEVELOPERS

**Want to start coding immediately?**
1. Read `01_TOOLS_YOU_CAN_BUILD.md` (tool overview + tech specs)
2. Open `CODE/04_PRODUCTION_CODE_BASE.md` (Tools 1-3 code)
3. Follow `EXECUTION/08_QUICK_START_CHECKLIST.md` (48-hour setup)

---

## FOLDER STRUCTURE

```
Persuasion Max/
│
├── ROOT (Core Docs)
│   ├── 00_CORE_THESIS.md           # Your unique positioning
│   ├── 01_TOOLS_YOU_CAN_BUILD.md   # 12 tools + tech specs ← START HERE
│   ├── 02_TOOL_SPECIFICATIONS.md   # Detailed technical specs
│   ├── 03_DEVELOPER_QUICKSTART.md  # Week 1-2 implementation
│   ├── EXECUTIVE_SUMMARY.md        # Project overview
│   ├── TERMINOLOGY_AND_DEFINITIONS.md
│   ├── CLAUDE.md                   # Project language guidelines
│   ├── UX_DESIGN_SYSTEM.md         # Tool attractiveness audit framework ← USE FOR IMPLEMENTATIONS
│   └── UX_DESIGN_SYSTEM.js         # Consolidated design tokens, patterns & utilities (all modules inline)
│
├── UX_UI_ENGAGEMENT/               # Interface patterns & gamification ← NEW DOMAIN
│   ├── ENGAGEMENT_PATTERNS_P1_P12.md    # 12 engagement patterns with specs
│   ├── SESSION_ARCHITECTURE.md          # 11-min model, event timestamps
│   ├── NEURO_AESTHETIC_PARAMETERS.md    # Color, audio, haptic specs
│   ├── CROSS_PATTERN_INTERACTION_MAPS.md # Gacha, Fitness, Mobile stacks
│   ├── USER_VULNERABILITY_PROFILES.md   # 6 user types × 12 patterns
│   ├── EXPERIMENTAL_MEASUREMENT_FRAMEWORK.md # A/B protocols, fatigue curves
│   ├── RESEARCH_GAPS.md                 # Open questions & hypotheses
│   └── DETECTION/
│       └── ENGAGEMENT_PATTERN_DETECTION.py # Python detectors for P1-P12
│
├── LINGUISTIC_PERSUASION/          # Rhetorical & cognitive influence ← NEW DOMAIN
│   ├── DETECTION/                  # Detection frameworks & patterns
│   │   ├── 11_TACTICAL_DETECTION_FRAMEWORK.md
│   │   ├── 12_PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.md
│   │   ├── 13_ADVANCED_FRAMEWORKS.md
│   │   ├── 14_DETECTION_FRAMEWORKS_MASTER_INDEX.md
│   │   ├── 15_PROFESSIONAL_AUDITOR_MANUAL.md
│   │   ├── 17_MACHINE_READABLE_DETECTION_SYSTEM.md
│   │   ├── 24_ENHANCED_DETECTION_RESEARCH.md
│   │   ├── 26_COMPREHENSIVE_DETECTION_FRAMEWORKS.md
│   │   ├── BEHAVIORAL_ANALYSIS_FRAMEWORK.md
│   │   ├── LINGUISTIC_DETECTION_FRAMEWORK.md
│   │   └── INTEGRITY_VIOLATION_DETECTION_FRAMEWORK.md
│   │
│   └── RESEARCH/                   # Research foundation & case studies
│       ├── 19_REAL_WORLD_CASE_STUDIES_DETAILED.md
│       ├── 25_EXPANDED_RESEARCH_DIMENSIONS.md
│       ├── 27_HIGH_IMPACT_DETECTION_SYSTEMS.md
│       ├── 28_EXPANDED_RANKED_COMBINATIONS.md
│       ├── APPENDIX_RESEARCH_SOURCES.md
│       ├── BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md
│       ├── CLASSICAL_RHETORICAL_TECHNIQUES.md
│       ├── EMPIRICAL_RESEARCH_SYNTHESIS.md   # Meta-analytic findings ← NEW
│       ├── EVOLUTION_ANALYSIS.md
│       ├── EVOLUTION_PATTERNS_AND_MECHANISMS.md
│       ├── FRACTIONATION_BEHAVIORAL_SCIENCE.md
│       ├── FRACTIONATION_DETECTION_METHODS.md
│       ├── LINGUISTIC_PERSUASION_RESEARCH.md
│       ├── RESEARCH_INDEX.md
│       └── RESEARCH_SUMMARY_AND_NEXT_STEPS.md
│
├── CODE/                           # Production-ready Python
│   ├── 04_PRODUCTION_CODE_BASE.md  # Tools 1-3 code
│   ├── 05_TOOLS_4_TO_8_CODE.md     # Tools 4-8 code
│   ├── 06_TOOLS_9_TO_12_CODE.md    # Tools 9-12 code
│   ├── UNIFIED_AUDITOR.py          # Combined linguistic detection tool
│   └── UNIFIED_GENERATOR.py        # Content generation tool
│
├── EXECUTION/                      # Implementation roadmaps
│   ├── 07_COMPLETE_IMPLEMENTATION_ROADMAP.md
│   ├── 08_QUICK_START_CHECKLIST.md
│   └── 22_IMPLEMENTATION_SPECIFICATION.md
│
├── ETHICS/                         # Ethical framework
│   └── ETHICAL_FRAMEWORK.md
│
├── META/                           # Project status
│   ├── PROJECT_STATUS.md
│   └── 20_COMPREHENSIVE_GAP_ANALYSIS.md
│
└── _archive/                       # (Cleared - original source files removed after integration)
```

---

## THE TWO DOMAINS

### Domain 1: UX/UI Engagement Patterns
**Location:** `UX_UI_ENGAGEMENT/`

Interface-level behavioral influence through design, gamification, and sensory feedback.

| Pattern | Name | Description |
|---------|------|-------------|
| P1 | Variable Reward | Randomized outcomes, gacha mechanics |
| P2 | Progress Momentum | Near-miss effects, progress bars |
| P3 | Encouraging Feedback | Sub-win celebrations, positive framing |
| P4 | Progress Protection | Streak preservation, loss aversion |
| P5 | Investment Recognition | Sunk cost display, benefit enumeration |
| P6 | Timely Opportunities | Scarcity, urgency, countdown timers |
| P7 | Contextual Offers | Emotion-timed offers, failure recovery |
| P8 | Immersive Experience | Flow state, time suppression |
| P9 | Personalized Tiers | Whale targeting, spend-based pricing |
| P10 | Community Activity | Social proof, activity displays |
| P11 | Community Connection | Group pressure, reciprocity |
| P12 | Identity & Achievement | Status labels, milestone systems |

**Key Files:**
- `ENGAGEMENT_PATTERNS_P1_P12.md` - Complete pattern specifications
- `DETECTION/ENGAGEMENT_PATTERN_DETECTION.py` - Python detector classes

### Domain 2: Linguistic Persuasion
**Location:** `LINGUISTIC_PERSUASION/`

Message-level influence through rhetoric, framing, cognitive biases, and emotional language.

**Categories:**
- Cialdini Principles (Reciprocity, Scarcity, Authority, Consistency, Liking, Social Proof, Unity, Contrast)
- Cognitive Biases (Anchoring, Framing, Loss Aversion, Confirmation Bias)
- Rhetorical Techniques (265 classical techniques from Cicero)
- Linguistic Patterns (Hedging, Intensifiers, Metaphors, Questions)
- Emotional Cycling (Fractionation, Emotional Triggers)

**Key Files:**
- `DETECTION/11_TACTICAL_DETECTION_FRAMEWORK.md` - 6 stimulus detection
- `DETECTION/LINGUISTIC_DETECTION_FRAMEWORK.md` - Linguistic pattern code
- `RESEARCH/CLASSICAL_RHETORICAL_TECHNIQUES.md` - 265 techniques
- `CODE/UNIFIED_AUDITOR.py` - Combined Python auditor

---

## BY PURPOSE

### I want to BUILD a detection tool
1. **Linguistic Patterns:** `CODE/UNIFIED_AUDITOR.py` ← Ready-to-run
2. **UX/UI Patterns:** `UX_UI_ENGAGEMENT/DETECTION/ENGAGEMENT_PATTERN_DETECTION.py` ← Ready-to-run
3. `LINGUISTIC_PERSUASION/DETECTION/17_MACHINE_READABLE_DETECTION_SYSTEM.md` - Regex patterns

### I want to UNDERSTAND the patterns being detected

**UX/UI Engagement:**
1. `UX_UI_ENGAGEMENT/ENGAGEMENT_PATTERNS_P1_P12.md` - 12 patterns
2. `UX_UI_ENGAGEMENT/CROSS_PATTERN_INTERACTION_MAPS.md` - How patterns combine
3. `UX_UI_ENGAGEMENT/USER_VULNERABILITY_PROFILES.md` - Who's affected

**Linguistic Persuasion:**
1. `LINGUISTIC_PERSUASION/DETECTION/11_TACTICAL_DETECTION_FRAMEWORK.md` - 6 stimuli
2. `LINGUISTIC_PERSUASION/DETECTION/12_PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.md` - Psychology
3. `LINGUISTIC_PERSUASION/RESEARCH/19_REAL_WORLD_CASE_STUDIES_DETAILED.md` - Famous examples

### I want to see the RESEARCH foundation
1. `LINGUISTIC_PERSUASION/RESEARCH/FRACTIONATION_BEHAVIORAL_SCIENCE.md` - Core mechanism
2. `LINGUISTIC_PERSUASION/RESEARCH/EMPIRICAL_RESEARCH_SYNTHESIS.md` - Meta-analysis
3. `UX_UI_ENGAGEMENT/RESEARCH_GAPS.md` - Open questions

### I want the IMPLEMENTATION roadmap
1. `EXECUTION/08_QUICK_START_CHECKLIST.md` - 48-hour setup
2. `EXECUTION/07_COMPLETE_IMPLEMENTATION_ROADMAP.md` - 24-month plan
3. `EXECUTION/22_IMPLEMENTATION_SPECIFICATION.md` - Full spec

### I want the ETHICAL framework
1. `ETHICS/ETHICAL_FRAMEWORK.md` - Complete boundaries & audit checklists

### I want to BUILD attractive tools (UX/Design)
1. `UX_DESIGN_SYSTEM.md` ← **Tool Attractiveness Audit Framework** - Reference guide with checklist
2. `UX_DESIGN_SYSTEM.js` - Consolidated design tokens & helper functions (for import)
3. All module content (core tokens, engagement patterns P1-P12, session design, neuro-aesthetic parameters, animations, mobile, progress, emotional, social, layout, helpers) is consolidated inline within `UX_DESIGN_SYSTEM.js`

---

## FILE COUNTS BY FOLDER

| Folder | Files | Purpose |
|--------|-------|---------|
| ROOT | 10 | Core docs + entry points + UX design system |
| (consolidated into UX_DESIGN_SYSTEM.js) | — | Design tokens, patterns, helpers |
| UX_UI_ENGAGEMENT | 8 | Interface engagement patterns |
| LINGUISTIC_PERSUASION/DETECTION | 11 | Linguistic detection frameworks |
| LINGUISTIC_PERSUASION/RESEARCH | 15 | Research foundation |
| CODE | 5 | Production Python code |
| EXECUTION | 3 | Implementation roadmaps |
| ETHICS | 1 | Ethical framework |
| META | 2 | Project status |
| _archive | 0 | (Cleared after integration) |
| **TOTAL** | **54** | - |

---

## WHAT'S IN UX_UI_ENGAGEMENT

| File | Content |
|------|---------|
| `ENGAGEMENT_PATTERNS_P1_P12.md` | All 12 patterns with constants, applications, metrics |
| `SESSION_ARCHITECTURE.md` | 11-minute model, event timestamps, return hooks |
| `NEURO_AESTHETIC_PARAMETERS.md` | Color wavelengths, audio frequencies, haptic specs |
| `CROSS_PATTERN_INTERACTION_MAPS.md` | Gacha/Fitness/Mobile/Subscription/Dating stacks |
| `USER_VULNERABILITY_PROFILES.md` | 6×12 responsiveness matrix, behavioral indicators |
| `EXPERIMENTAL_MEASUREMENT_FRAMEWORK.md` | A/B protocols, fatigue curves, cross-cultural validation |
| `RESEARCH_GAPS.md` | Open questions, hypotheses, measurement approaches |
| `DETECTION/ENGAGEMENT_PATTERN_DETECTION.py` | Python detector classes for P1-P12 |

---

## WHAT'S IN LINGUISTIC_PERSUASION/DETECTION

| File | Content |
|------|---------|
| `11_TACTICAL_DETECTION_FRAMEWORK.md` | 6 stimulus detectors (Personal, Emotional, Tangible, etc.) |
| `12_PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.md` | Psychology pattern detection |
| `13_ADVANCED_FRAMEWORKS.md` | Complex multi-pattern detection |
| `14_DETECTION_FRAMEWORKS_MASTER_INDEX.md` | Index to all frameworks |
| `15_PROFESSIONAL_AUDITOR_MANUAL.md` | How to conduct audits |
| `17_MACHINE_READABLE_DETECTION_SYSTEM.md` | Regex patterns, JSON scoring |
| `24_ENHANCED_DETECTION_RESEARCH.md` | Latest research + enhanced code |
| `26_COMPREHENSIVE_DETECTION_FRAMEWORKS.md` | Multimodal, platform-specific, AI detection |
| `BEHAVIORAL_ANALYSIS_FRAMEWORK.md` | Effectiveness metrics & technical specs |
| `LINGUISTIC_DETECTION_FRAMEWORK.md` | Linguistic pattern detection code |
| `INTEGRITY_VIOLATION_DETECTION_FRAMEWORK.md` | Integrity violation detection |

---

## WHAT'S IN LINGUISTIC_PERSUASION/RESEARCH

| File | Content |
|------|---------|
| `19_REAL_WORLD_CASE_STUDIES_DETAILED.md` | Bernays, Goebbels, modern brands |
| `25_EXPANDED_RESEARCH_DIMENSIONS.md` | Extended research dimensions |
| `27_HIGH_IMPACT_DETECTION_SYSTEMS.md` | High-impact detection approaches |
| `28_EXPANDED_RANKED_COMBINATIONS.md` | Ranked pattern combinations |
| `APPENDIX_RESEARCH_SOURCES.md` | Source citations |
| `BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md` | Week-by-week research execution |
| `CLASSICAL_RHETORICAL_TECHNIQUES.md` | 265 Cicero rhetorical techniques |
| `EMPIRICAL_RESEARCH_SYNTHESIS.md` | Meta-analytic findings (compounding, fatigue, temporal) |
| `EVOLUTION_ANALYSIS.md` | 7-phase historical progression |
| `EVOLUTION_PATTERNS_AND_MECHANISMS.md` | Technique transformations |
| `FRACTIONATION_BEHAVIORAL_SCIENCE.md` | Neurochemistry of emotional cycling |
| `FRACTIONATION_DETECTION_METHODS.md` | 14 measurement methods |
| `LINGUISTIC_PERSUASION_RESEARCH.md` | Linguistic influence research |
| `RESEARCH_INDEX.md` | Quick reference + cross-references |
| `RESEARCH_SUMMARY_AND_NEXT_STEPS.md` | 7 research questions + trajectory |

---

## KEY FILES FOR DEVELOPERS

| Priority | File | What It Contains |
|----------|------|------------------|
| 1 | `CODE/UNIFIED_AUDITOR.py` | Linguistic auditing tool (ready-to-run) |
| 2 | `UX_UI_ENGAGEMENT/DETECTION/ENGAGEMENT_PATTERN_DETECTION.py` | UX pattern detector (ready-to-run) |
| 3 | `01_TOOLS_YOU_CAN_BUILD.md` | All 12 tools with tech specs |
| 4 | `CODE/04_PRODUCTION_CODE_BASE.md` | Tools 1-3 ready-to-run code |
| 5 | `UX_UI_ENGAGEMENT/ENGAGEMENT_PATTERNS_P1_P12.md` | Complete P1-P12 specs |
| 6 | `EXECUTION/08_QUICK_START_CHECKLIST.md` | 48-hour setup guide |

---

## START HERE

**For UX/UI Detection:** `UX_UI_ENGAGEMENT/ENGAGEMENT_PATTERNS_P1_P12.md` → `UX_UI_ENGAGEMENT/DETECTION/ENGAGEMENT_PATTERN_DETECTION.py`

**For Linguistic Detection:** `LINGUISTIC_PERSUASION/DETECTION/11_TACTICAL_DETECTION_FRAMEWORK.md` → `CODE/UNIFIED_AUDITOR.py`

**For Researchers:** `LINGUISTIC_PERSUASION/RESEARCH/FRACTIONATION_BEHAVIORAL_SCIENCE.md` → `LINGUISTIC_PERSUASION/RESEARCH/EMPIRICAL_RESEARCH_SYNTHESIS.md`

**For Auditors:** `LINGUISTIC_PERSUASION/DETECTION/15_PROFESSIONAL_AUDITOR_MANUAL.md`

**For Ethics/Policy:** `ETHICS/ETHICAL_FRAMEWORK.md`

---

## CROSS-DOMAIN RELATIONSHIPS

The two domains complement each other:

```
LINGUISTIC_PERSUASION           UX_UI_ENGAGEMENT
────────────────────────        ─────────────────────
Scarcity messaging      <──>    P6: Timely Opportunities
Social proof language   <──>    P10: Community Activity
Loss framing           <──>    P4: Progress Protection
Authority appeals      <──>    P12: Identity & Achievement
Reciprocity language   <──>    P11: Community Connection
```

**Combined Analysis:** For comprehensive auditing, use both:
1. `CODE/UNIFIED_AUDITOR.py` for message-level linguistic patterns
2. `UX_UI_ENGAGEMENT/DETECTION/ENGAGEMENT_PATTERN_DETECTION.py` for interface-level UX patterns
