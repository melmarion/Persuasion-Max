# Persuasion Max

A comprehensive behavioral influence analysis and content enhancement system combining detection frameworks, generation tools, and research foundations across psychology, neuroscience, linguistics, and behavioral economics.

---

## 🎯 Quick Start

### For Developers
See **[03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md)** for Week 1-2 implementation guide.

### For Copywriters
See **[PROMPT_PERSUASION_GRAMMARLY.md](PROMPT_PERSUASION_GRAMMARLY.md)** to build a "Grammarly for Persuasion" tool.

### For Researchers
See **[RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md](RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md)** for research execution plans.

---

## 📦 What's Included

### Production Code
- **[CODE/UNIFIED_AUDITOR.py](CODE/UNIFIED_AUDITOR.py)** (2,304 lines)
  Complete detection tool analyzing text across 22 persuasion techniques in 3 frameworks

- **[CODE/UNIFIED_GENERATOR.py](CODE/UNIFIED_GENERATOR.py)** (2,945 lines)
  Content enhancement tool for applying persuasion techniques with LLM integration

### Detection Frameworks (10 documents)
- 6 Tactical Stimulus patterns (Personal, Contrastable, Tangible, Memorable, Visual, Emotional)
- 8 Psychological Principles (Cialdini + cognitive biases)
- 8 Linguistic Patterns (rhetorical devices, syntactic patterns, framing)
- 265 Classical rhetorical techniques

### Research Foundation (14 documents)
- Fractionation behavioral science & detection methods
- Historical evolution analysis (Bernays → Platforms → AI)
- Real-world case studies with detection rules
- Cross-domain measurement frameworks

### Implementation Guides
- **[01_TOOLS_YOU_CAN_BUILD.md](01_TOOLS_YOU_CAN_BUILD.md)** - 12 tool specifications
- **[EXECUTION/07_COMPLETE_IMPLEMENTATION_ROADMAP.md](EXECUTION/07_COMPLETE_IMPLEMENTATION_ROADMAP.md)** - 24-month development plan
- **[EXECUTION/08_QUICK_START_CHECKLIST.md](EXECUTION/08_QUICK_START_CHECKLIST.md)** - 48-hour setup guide

---

## 🚀 Installation

### Requirements
- Python 3.8+
- Optional: OpenAI API key or Anthropic API key (for LLM enhancement)

### Basic Setup

```bash
# Clone repository
git clone <your-repo-url>
cd Persuasion-Max

# No external dependencies required for core detection
# Optional: Install for LLM integration
pip install openai anthropic
```

### Quick Test

```python
from CODE.UNIFIED_AUDITOR import UnifiedPersuasionAuditor

# Analyze text for persuasion techniques
auditor = UnifiedPersuasionAuditor()
result = auditor.audit("Your text here")

print(f"Persuasion Score: {result.composite_scores['overall']}/100")
print(f"Classification: {result.classification}")
```

---

## 💡 Use Cases

### 1. Content Analysis
Analyze copy for persuasion intensity:
```python
from CODE.UNIFIED_AUDITOR import UnifiedPersuasionAuditor

auditor = UnifiedPersuasionAuditor()
result = auditor.audit("""
Join 10,000+ professionals who've already upgraded.
Only 5 spots left at this price—claim yours now!
""")

# Returns: Score 78/100, HIGH intensity
# Techniques detected: SOCIAL_PROOF, SCARCITY, URGENCY
```

### 2. Copy Enhancement
Transform basic copy into persuasive content:
```python
from CODE.UNIFIED_GENERATOR import UnifiedInfluenceGenerator, GenerationConfig

generator = UnifiedInfluenceGenerator()
config = GenerationConfig(
    techniques=["SOCIAL_PROOF", "SCARCITY"],
    intensity="MODERATE"
)

result = generator.enhance("Our product is available now.", config)
print(result.enhanced_text)
# Output: "Join 500+ customers who've secured their spot this week..."
```

### 3. Goal-Based Suggestions
Get technique recommendations for specific goals:
```python
generator = UnifiedInfluenceGenerator()
suggestions = generator.suggest_techniques(goal="urgency")

# Returns recommended techniques with synergy info
print(suggestions['techniques'])  # ['SCARCITY', 'EMOTIONAL', 'FRAMING']
print(suggestions['synergy_multiplier'])  # 1.35
```

---

## 📚 Documentation Structure

```
Persuasion Max/
├── README.md (you are here)
├── CLAUDE.md (language guidelines - neutral professional terminology)
├── PROMPT_PERSUASION_GRAMMARLY.md (build a Grammarly-style tool)
│
├── ROOT DOCUMENTS (7 files)
│   ├── 00_CORE_THESIS.md (research positioning)
│   ├── 01_TOOLS_YOU_CAN_BUILD.md (12 tool specifications)
│   ├── 02_TOOL_SPECIFICATIONS.md (technical specs)
│   ├── 03_DEVELOPER_QUICKSTART.md (implementation guide)
│   ├── EXECUTIVE_SUMMARY.md (project overview)
│   ├── FILE_DIRECTORY_GUIDE.md (navigation)
│   └── TERMINOLOGY_AND_DEFINITIONS.md (standardized terms)
│
├── CODE/ (Production code + specifications)
│   ├── UNIFIED_AUDITOR.py ⭐
│   ├── UNIFIED_GENERATOR.py ⭐
│   ├── 04_PRODUCTION_CODE_BASE.md
│   ├── 05_TOOLS_4_TO_8_CODE.md
│   └── 06_TOOLS_9_TO_12_CODE.md
│
├── DETECTION/ (10 framework documents)
│   ├── 11_TACTICAL_DETECTION_FRAMEWORK.md
│   ├── 12_PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.md
│   ├── 13_ADVANCED_FRAMEWORKS.md
│   ├── LINGUISTIC_DETECTION_FRAMEWORK.md
│   └── ... (6 more)
│
├── RESEARCH/ (14 research documents)
│   ├── FRACTIONATION_BEHAVIORAL_SCIENCE.md
│   ├── FRACTIONATION_DETECTION_METHODS.md
│   ├── BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md
│   ├── EVOLUTION_ANALYSIS.md
│   ├── CLASSICAL_RHETORICAL_TECHNIQUES.md
│   └── ... (9 more)
│
├── EXECUTION/ (Implementation roadmaps)
│   ├── 07_COMPLETE_IMPLEMENTATION_ROADMAP.md
│   ├── 08_QUICK_START_CHECKLIST.md
│   └── 22_IMPLEMENTATION_SPECIFICATION.md
│
├── ETHICS/ (Intensity framework)
│   └── ETHICAL_FRAMEWORK.md
│
├── META/ (Project status & analysis)
│   ├── PROJECT_STATUS.md
│   └── 20_COMPREHENSIVE_GAP_ANALYSIS.md
│
├── UX_UI_ENGAGEMENT/ (Interface patterns)
│   ├── CROSS_PATTERN_INTERACTION_MAPS.md
│   ├── ENGAGEMENT_PATTERNS_P1_P12.md
│   ├── USER_VULNERABILITY_PROFILES.md
│   └── ... (5 more)
│
└── LINGUISTIC_PERSUASION/ (Linguistic resources)
    └── (Additional linguistic research)
```

---

## 🔧 Core Features

### Detection Engine (UNIFIED_AUDITOR.py)
- **22 Persuasion Techniques** across 3 frameworks
- **Pattern Matching** using 400+ regex patterns and keyword lists
- **Composite Scoring** with weighted averaging
- **Classification** (MINIMAL, LOW, MODERATE, HIGH, EXTREME)
- **Red Flag Generation** with severity levels
- **JSON Output** with complete analysis details

### Generation Engine (UNIFIED_GENERATOR.py)
- **22 Technique Generators** with 200+ templates
- **LLM Integration** (OpenAI, Anthropic, or custom)
- **Synergy Calculation** for technique combinations
- **Intensity Control** (LOW, MODERATE, HIGH, EXTREME)
- **Quality Verification** using detection engine
- **Goal-Based Presets** (urgency, trust, action, etc.)

---

## 📖 Key Documents

| Document | Purpose | Audience |
|----------|---------|----------|
| [PROMPT_PERSUASION_GRAMMARLY.md](PROMPT_PERSUASION_GRAMMARLY.md) | Build a Grammarly-style persuasion tool | Developers, Product |
| [03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md) | Week 1-2 implementation guide | Developers |
| [01_TOOLS_YOU_CAN_BUILD.md](01_TOOLS_YOU_CAN_BUILD.md) | 12 complete tool specifications | All |
| [00_CORE_THESIS.md](00_CORE_THESIS.md) | Research positioning & unique value | Researchers |
| [DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md](DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md) | Index to all detection frameworks | Technical |
| [RESEARCH/RESEARCH_INDEX.md](RESEARCH/RESEARCH_INDEX.md) | Research quick reference | Researchers |
| [ETHICS/ETHICAL_FRAMEWORK.md](ETHICS/ETHICAL_FRAMEWORK.md) | Intensity boundaries & constraints | All |

---

## 🎓 Detection Frameworks

### Framework 1: Tactical Stimulus (6 categories)
Detects primal psychological triggers:
- **PERSONAL** - Self-centered targeting
- **CONTRASTABLE** - Binary ideological framing
- **TANGIBLE** - Concrete vs. abstract properties
- **MEMORABLE** - U-curve narrative structure
- **VISUAL** - Anti-aesthetic vs. polished presentation
- **EMOTIONAL** - Pain → Relief arc

### Framework 2: Psychological Principles (8 categories)
Detects influence mechanisms (Cialdini + biases):
- **AUTHORITY** - Credentials, expertise
- **SOCIAL_PROOF** - Consensus, similarity
- **RECIPROCITY** - Free offerings, obligation
- **COMMITMENT** - Small asks, escalation
- **SCARCITY** - Limitation, urgency
- **LIKING** - Similarity, compliments
- **UNITY** - In-group identity
- **FRAMING** - Context effects

### Framework 3: Linguistic Patterns (8 categories)
Detects language-based techniques:
- **RHETORICAL_DEVICES** - Metaphors, parallelism
- **SYNTACTIC_PATTERNS** - Sentence structure effects
- **FRAMING_EFFECTS** - Linguistic frame manipulation
- **PRAGMATIC_PATTERNS** - Implicature, presupposition
- **DISCOURSE_MARKERS** - Connectives, topic shifts
- **HEDGING_CERTAINTY** - Confidence modulation
- **REGISTER_FORMALITY** - Formality level effects
- **CONCEPTUAL_METAPHOR** - Metaphorical framing

---

## 🛠️ Example Workflows

### Workflow 1: Analyze Email Subject Line
```python
from CODE.UNIFIED_AUDITOR import UnifiedPersuasionAuditor

auditor = UnifiedPersuasionAuditor()
subject = "Last chance: 50% off ends tonight!"

result = auditor.audit(subject)
print(f"Score: {result.composite_scores['overall']}/100")
print(f"Techniques: {result.techniques_detected}")
# Output: Score 82/100, Techniques: ['SCARCITY', 'URGENCY', 'FRAMING']
```

### Workflow 2: Enhance Product Description
```python
from CODE.UNIFIED_GENERATOR import UnifiedInfluenceGenerator, GenerationConfig

generator = UnifiedInfluenceGenerator()
basic_copy = "High-quality software for teams."

config = GenerationConfig(
    techniques=['SOCIAL_PROOF', 'TANGIBLE', 'AUTHORITY'],
    intensity='MODERATE'
)

result = generator.enhance(basic_copy, config)
print(result.enhanced_text)
# Output: "Join 2,400+ teams saving 15 hours/week with our platform,
#          trusted by Fortune 500 companies."
```

### Workflow 3: Get Goal-Based Suggestions
```python
generator = UnifiedInfluenceGenerator()

# Get recommendations for "urgency" goal
suggestions = generator.suggest_techniques(goal="urgency")
print(suggestions['techniques'])  # ['SCARCITY', 'EMOTIONAL', 'FRAMING']
print(suggestions['synergy_multiplier'])  # 1.35

# Get recommendations for "trust" goal
trust_suggestions = generator.suggest_techniques(goal="trust")
print(trust_suggestions['techniques'])  # ['AUTHORITY', 'SOCIAL_PROOF', 'UNITY']
```

---

## 📊 Output Examples

### Detection Output (JSON)
```json
{
  "composite_scores": {
    "tactical_stimulus": 68,
    "psychological_principles": 75,
    "linguistic_patterns": 42,
    "overall": 62
  },
  "classification": "MODERATE",
  "techniques_detected": [
    "SOCIAL_PROOF",
    "SCARCITY",
    "AUTHORITY"
  ],
  "red_flags": [
    {
      "severity": "MEDIUM",
      "category": "SCARCITY",
      "description": "Artificial urgency detected",
      "evidence": ["only 3 left", "ends tonight"]
    }
  ]
}
```

### Generation Output
```python
{
  "original_text": "Buy our product today.",
  "enhanced_text": "Join 1,500+ customers who've already secured their discount—only 8 spots left at this price.",
  "techniques_applied": ["SOCIAL_PROOF", "SCARCITY"],
  "synergy_multiplier": 1.25,
  "intensity_achieved": "MODERATE",
  "verification_score": 74
}
```

---

## 🔍 Language Guidelines

This project uses **neutral professional language** to describe behavioral influence techniques. See [CLAUDE.md](CLAUDE.md) for complete guidelines.

### Key Principles:
- Use "influence technique" not "manipulation"
- Use "behavioral influence" not "dark pattern"
- Use "intensity" not "exploitation"
- Describe what systems do without moral judgment

---

## 📈 Project Status

**Current Version:** 1.1 (Production-Ready)

**Completion Status:**
- ✅ 2 production Python modules (5,250+ lines)
- ✅ 10 detection framework documents
- ✅ 14 research foundation documents
- ✅ 3 implementation roadmaps
- ✅ Complete intensity threshold framework
- ✅ 40+ total documentation files

See [META/PROJECT_STATUS.md](META/PROJECT_STATUS.md) for detailed status.

---

## 🤝 Support

For questions about:
- **Implementation**: See [03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md)
- **Research**: See [RESEARCH/RESEARCH_INDEX.md](RESEARCH/RESEARCH_INDEX.md)
- **Detection Frameworks**: See [DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md](DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md)
- **File Navigation**: See [FILE_DIRECTORY_GUIDE.md](FILE_DIRECTORY_GUIDE.md)

---

## 📄 License

Copyright © 2025 Mario. All rights reserved.

This is proprietary software. See [LICENSE](LICENSE) for details.

---

## 🗺️ Next Steps

1. **For Developers**: Start with [03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md)
2. **For Product**: Build the Grammarly tool using [PROMPT_PERSUASION_GRAMMARLY.md](PROMPT_PERSUASION_GRAMMARLY.md)
3. **For Research**: Follow [RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md](RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md)
4. **For Analysis**: Run `python CODE/UNIFIED_AUDITOR.py` with demo text

---

**Built with:** Python 3.8+ | No external dependencies for core detection | Optional LLM integration

**Documentation:** 41,420 lines across 40+ files | Complete research foundation | Production-ready code
