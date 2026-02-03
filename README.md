# Communication Pattern Framework

A comprehensive communication pattern analysis and content enhancement system combining detection frameworks, generation tools, and research foundations across psychology, neuroscience, linguistics, and behavioral economics.

---

## Quick Start

### For Developers
See **[03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md)** for Week 1-2 implementation guide.

### For Researchers
See **[COMMUNICATION_PATTERNS/RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md](COMMUNICATION_PATTERNS/RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md)** for research execution plans.

---

## What's Included

### Production Code
- **[CODE/UNIFIED_ANALYZER.py](CODE/UNIFIED_ANALYZER.py)** (2,304 lines)
  Complete detection tool analyzing text across 22 communication techniques in 3 frameworks

- **[CODE/UNIFIED_GENERATOR.py](CODE/UNIFIED_GENERATOR.py)** (2,945 lines)
  Content enhancement tool for applying communication techniques with LLM integration

### Detection Frameworks (10 documents)
- 6 Tactical Stimulus patterns (Personal, Contrastable, Tangible, Memorable, Visual, Emotional)
- 8 Psychological Principles (Cialdini + cognitive biases)
- 8 Linguistic Patterns (rhetorical devices, syntactic patterns, framing)
- 265 Classical rhetorical techniques

### Research Foundation (14 documents)
- Incremental engagement behavioral science & detection methods
- Historical evolution analysis
- Real-world case studies with detection rules
- Cross-domain measurement frameworks

### Implementation Guides
- **[01_TOOLS_YOU_CAN_BUILD.md](01_TOOLS_YOU_CAN_BUILD.md)** - 12 tool specifications
- **[EXECUTION/22_IMPLEMENTATION_SPECIFICATION.md](EXECUTION/22_IMPLEMENTATION_SPECIFICATION.md)** - Full specification

---

## Installation

### Requirements
- Python 3.8+
- Optional: OpenAI API key or Anthropic API key (for LLM enhancement)

### Basic Setup

```bash
# Clone repository
git clone <your-repo-url>
cd communication-pattern-framework

# No external dependencies required for core detection
# Optional: Install for LLM integration
pip install openai anthropic
```

### Quick Test

```python
from CODE.UNIFIED_ANALYZER import UnifiedPatternAnalyzer

# Analyze text for communication patterns
analyzer = UnifiedPatternAnalyzer()
result = analyzer.analyze("Your text here")

print(f"Pattern Score: {result.composite_scores['overall']}/100")
print(f"Classification: {result.classification}")
```

---

## Use Cases

### 1. Content Analysis
Analyze copy for communication pattern intensity:
```python
from CODE.UNIFIED_ANALYZER import UnifiedPatternAnalyzer

analyzer = UnifiedPatternAnalyzer()
result = analyzer.analyze("""
Join 10,000+ professionals who've already upgraded.
Only 5 spots left at this price—claim yours now!
""")

# Returns: Score 78/100, HIGH intensity
# Techniques detected: SOCIAL_PROOF, SCARCITY, URGENCY
```

### 2. Copy Enhancement
Transform basic copy into engaging content:
```python
from CODE.UNIFIED_GENERATOR import UnifiedPatternGenerator, GenerationConfig

generator = UnifiedPatternGenerator()
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
generator = UnifiedPatternGenerator()
suggestions = generator.suggest_techniques(goal="urgency")

# Returns recommended techniques with synergy info
print(suggestions['techniques'])  # ['SCARCITY', 'EMOTIONAL', 'FRAMING']
print(suggestions['synergy_multiplier'])  # 1.35
```

---

## Documentation Structure

```
Communication Pattern Framework/
├── README.md (you are here)
│
├── ROOT DOCUMENTS
│   ├── 01_TOOLS_YOU_CAN_BUILD.md (12 tool specifications)
│   ├── 02_TOOL_SPECIFICATIONS.md (technical specs)
│   ├── 03_DEVELOPER_QUICKSTART.md (implementation guide)
│   ├── FILE_DIRECTORY_GUIDE.md (navigation)
│   └── TERMINOLOGY_AND_DEFINITIONS.md (standardized terms)
│
├── CODE/ (Production code + specifications)
│   ├── UNIFIED_ANALYZER.py
│   ├── UNIFIED_GENERATOR.py
│   ├── CONSISTENCY_ANALYZER.py
│   ├── 04_PRODUCTION_CODE_BASE.md
│   ├── 05_TOOLS_4_TO_8_CODE.md
│   └── 06_TOOLS_9_TO_12_CODE.md
│
├── COMMUNICATION_PATTERNS/
│   ├── DETECTION/ (10 framework documents)
│   │   ├── 11_TACTICAL_DETECTION_FRAMEWORK.md
│   │   ├── 12_PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.md
│   │   ├── LINGUISTIC_DETECTION_FRAMEWORK.md
│   │   └── ... (7 more)
│   │
│   └── RESEARCH/ (14 research documents)
│       ├── INCREMENTAL_ENGAGEMENT_SCIENCE.md
│       ├── INCREMENTAL_PATTERN_METHODS.md
│       ├── BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md
│       └── ... (11 more)
│
├── EXECUTION/ (Implementation roadmaps)
│   └── 22_IMPLEMENTATION_SPECIFICATION.md
│
└── UX_UI_ENGAGEMENT/ (Interface patterns)
    ├── CROSS_PATTERN_INTERACTION_MAPS.md
    ├── ENGAGEMENT_PATTERNS_P1_P12.md
    ├── USER_RESPONSE_PROFILES.md
    └── ... (5 more)
```

---

## Core Features

### Detection Engine (UNIFIED_ANALYZER.py)
- **22 Communication Techniques** across 3 frameworks
- **Pattern Matching** using 400+ regex patterns and keyword lists
- **Composite Scoring** with weighted averaging
- **Classification** (MINIMAL, LOW, MODERATE, HIGH, EXTREME)
- **Findings Generation** with intensity levels
- **JSON Output** with complete analysis details

### Generation Engine (UNIFIED_GENERATOR.py)
- **22 Technique Generators** with 200+ templates
- **LLM Integration** (OpenAI, Anthropic, or custom)
- **Synergy Calculation** for technique combinations
- **Intensity Control** (LOW, MODERATE, HIGH, EXTREME)
- **Quality Verification** using detection engine
- **Goal-Based Presets** (urgency, trust, action, etc.)

---

## Key Documents

| Document | Purpose | Audience |
|----------|---------|----------|
| [03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md) | Week 1-2 implementation guide | Developers |
| [01_TOOLS_YOU_CAN_BUILD.md](01_TOOLS_YOU_CAN_BUILD.md) | 12 complete tool specifications | All |
| [COMMUNICATION_PATTERNS/DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md](COMMUNICATION_PATTERNS/DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md) | Index to all detection frameworks | Technical |
| [COMMUNICATION_PATTERNS/RESEARCH/RESEARCH_INDEX.md](COMMUNICATION_PATTERNS/RESEARCH/RESEARCH_INDEX.md) | Research quick reference | Researchers |

---

## Detection Frameworks

### Framework 1: Tactical Stimulus (6 categories)
Detects psychological engagement patterns:
- **PERSONAL** - Self-centered targeting
- **CONTRASTABLE** - Binary framing
- **TANGIBLE** - Concrete vs. abstract properties
- **MEMORABLE** - U-curve narrative structure
- **VISUAL** - Aesthetic presentation patterns
- **EMOTIONAL** - Emotional arc structure

### Framework 2: Psychological Principles (8 categories)
Detects engagement mechanisms (Cialdini + biases):
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
- **FRAMING_EFFECTS** - Linguistic frame patterns
- **PRAGMATIC_PATTERNS** - Implicature, presupposition
- **DISCOURSE_MARKERS** - Connectives, topic shifts
- **HEDGING_CERTAINTY** - Confidence modulation
- **REGISTER_FORMALITY** - Formality level effects
- **CONCEPTUAL_METAPHOR** - Metaphorical framing

---

## Example Workflows

### Workflow 1: Analyze Email Subject Line
```python
from CODE.UNIFIED_ANALYZER import UnifiedPatternAnalyzer

analyzer = UnifiedPatternAnalyzer()
subject = "Last chance: 50% off ends tonight!"

result = analyzer.analyze(subject)
print(f"Score: {result.composite_scores['overall']}/100")
print(f"Techniques: {result.techniques_detected}")
# Output: Score 82/100, Techniques: ['SCARCITY', 'URGENCY', 'FRAMING']
```

### Workflow 2: Enhance Product Description
```python
from CODE.UNIFIED_GENERATOR import UnifiedPatternGenerator, GenerationConfig

generator = UnifiedPatternGenerator()
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

---

## Output Examples

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
  "findings": [
    {
      "intensity": "MEDIUM",
      "category": "SCARCITY",
      "description": "Urgency pattern detected",
      "evidence": ["only 3 left", "ends tonight"]
    }
  ]
}
```

---

## Language Guidelines

This project uses **neutral professional language** to describe communication techniques.

### Key Principles:
- Use "communication technique" not loaded terminology
- Use "engagement pattern" for interface patterns
- Use "intensity" for measurement scales
- Describe what systems do without moral judgment

---

## Project Status

**Current Version:** 1.1 (Production-Ready)

**Completion Status:**
- 2 production Python modules (5,250+ lines)
- 10 detection framework documents
- 14 research foundation documents
- Implementation specifications
- Complete intensity threshold framework
- 40+ total documentation files

---

## Support

For questions about:
- **Implementation**: See [03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md)
- **Research**: See [COMMUNICATION_PATTERNS/RESEARCH/RESEARCH_INDEX.md](COMMUNICATION_PATTERNS/RESEARCH/RESEARCH_INDEX.md)
- **Detection Frameworks**: See [COMMUNICATION_PATTERNS/DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md](COMMUNICATION_PATTERNS/DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md)
- **File Navigation**: See [FILE_DIRECTORY_GUIDE.md](FILE_DIRECTORY_GUIDE.md)

---

## License

Copyright 2025. All rights reserved.

This is proprietary software. See [LICENSE](LICENSE) for details.

---

## Next Steps

1. **For Developers**: Start with [03_DEVELOPER_QUICKSTART.md](03_DEVELOPER_QUICKSTART.md)
2. **For Research**: Follow [COMMUNICATION_PATTERNS/RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md](COMMUNICATION_PATTERNS/RESEARCH/BEHAVIORAL_SCIENTIST_RESEARCH_PACKAGE.md)
3. **For Analysis**: Run `python CODE/UNIFIED_ANALYZER.py` with demo text

---

**Built with:** Python 3.8+ | No external dependencies for core detection | Optional LLM integration
