# Terminology and Definitions

## Core Concepts

### Fractionation

**Definition (Executive):**
Fractionation is the rapid cycling of emotional states designed to temporarily exceed working memory capacity, reducing prefrontal cortex engagement and increasing behavioral suggestibility.

**Definition (Technical):**
Fractionation is a rapid emotional sequencing pattern (anger-joy-anger-relief, denoted A-J-A-R) deployed by algorithms to create neurochemical states that reduce prefrontal cortex engagement, increase amygdala dominance, temporarily reduce critical evaluation capacity, and increase behavioral suggestibility by 200%+. The pattern is characterized by specific psychophysiological markers: elevated cortisol, reduced heart rate variability, dramatically reduced blink rate during relief phase (<10 blinks/min), and increased skin conductance.

**Definition (Mechanistic):**
The fractionation sequence operates as follows:
- **Cycle 1 (Anger Phase):** Exposure to threat/outrage content activates the amygdala (fear-anger pathway), increasing cortisol and blink rate (35-45 blinks/min). Prefrontal engagement is reduced as threat-detection circuits dominate.
- **Cycle 2 (Joy Phase):** Exposure to bonding/achievement content activates reward circuits, releasing dopamine and temporarily improving mood. Blink rate drops to 20-25 blinks/min as attention narrows.
- **Cycle 3 (Second Anger):** Return to threat/outrage content reactivates amygdala while dopamine levels remain elevated, creating a conflict between threat-detection and reward systems.
- **Cycle 4 (Relief Phase):** Exposure to solution/product/relief content creates a sense of resolution. Working memory is severely overloaded from three emotional reversals; blink rate drops below 10 blinks/min (hypnotic focus state); prefrontal engagement is minimized; behavioral suggestions encounter minimal critical evaluation.

---

### Emotional Sequencing

**Canonical Term:** "Emotional sequencing" (preferred term)
**Alternate Terms (deprecated, use emotional sequencing):** "Emotional cycling"

Emotional sequencing refers to the deliberate ordering of content designed to evoke specific emotional states in rapid succession. In the context of fractionation research, this specifically refers to A-J-A-R patterns.

**Usage:**
- Use "emotional sequencing" in all contexts (research, technical, documentation)
- When describing the full pattern, use: "A-J-A-R emotional sequencing" or "the A-J-A-R pattern of emotional sequencing"

---

### A-J-A-R Pattern

**Canonical Notation:** "A-J-A-R"
**Full Expansion:** anger-joy-anger-relief
**Alternative Notations (deprecated):**
- A-J-A-R (non-hyphenated uppercase)
- anger → joy → anger → relief (arrow notation)

**Components:**
- **A (Anger):** Threat/outrage/fear content; activates amygdala; increases cortisol
- **J (Joy):** Bonding/achievement/wholesome content; activates reward circuits; releases dopamine
- **A (Anger - second):** Return to threat content; amygdala reactivates with elevated dopamine
- **R (Relief):** Solution/product/resolution content; creates sense of closure; induces hypnotic focus state

**Usage:**
- Use "A-J-A-R" for the notation when referencing the pattern
- In first mention, expand to "A-J-A-R (anger-joy-anger-relief)" for clarity
- Use "A-J-A-R emotional sequencing" to specify this is a type of emotional sequencing

---

### Vulnerability vs. Susceptibility

**Vulnerability (Technical/Code Context):**
Used in software development, code variables, class names, and technical specifications.
- Example: VulnerabilityScorer class
- Example: "vulnerability assessment module"
- Indicates: Technical implementation of measurement systems

**Susceptibility (Research/Behavioral Context):**
Used in research, behavioral analysis, clinical assessment, and empirical documentation.
- Example: "Patients with high susceptibility to fractionation..."
- Example: "Susceptibility factors include trait anxiety..."
- Indicates: Behavioral/psychological characteristics and research findings

**Usage Rule:** Choose based on context, not content. If writing code or technical specs → "vulnerability". If writing research, behavioral analysis, or clinical content → "susceptibility".

---

### Blink Rate Measurements

**Notation Standard:** Always use "X blinks/min" format with explicit units

**Normal Baseline State:**
- "15-20 blinks/min" (standard awake, attentive baseline)
- Measured in relaxed, focused attention without emotional priming

**Fractionation State Phases:**
- **Anger Phase (Initial):** 35-45 blinks/min (elevated arousal, threat detection)
- **Joy Phase:** 20-25 blinks/min (moderate arousal, positive emotion)
- **Relief Phase (Hypnotic Focus):** <10 blinks/min (severe attentional narrowing, reduced critical evaluation)

**Stress/High Arousal State:**
- 30+ blinks/min (general elevated arousal, not specific to fractionation)

**Usage:**
- Always include "blinks/min" units
- Never use abbreviated forms like "15-20" or "15-20/min" without context
- When comparing states, use explicit notation: "Normal baseline (15-20 blinks/min) vs. relief phase (<10 blinks/min)"
- When citing specific ranges in fractionation research, use the detailed phase descriptions above

---

## Standardized Terminology Reference

### Terms to Use Consistently

| Concept | Use This | NOT This |
|---------|----------|----------|
| The 4-cycle emotional pattern | A-J-A-R | A-J-A-R, anger→joy→anger→relief |
| Emotional state ordering | emotional sequencing | emotional cycling |
| Code/technical context | vulnerability | susceptibility |
| Research/behavioral context | susceptibility | vulnerability |
| Measurement notation | "15-20 blinks/min" | "15-20", "15-20/minute" |
| Pattern notation (first mention) | "A-J-A-R (anger-joy-anger-relief)" | "A-J-A-R", arrow notation |
| Pattern notation (subsequent) | "A-J-A-R" | Full spelling |

---

## Implementation Notes

### When Writing New Content:
1. Check TERMINOLOGY_AND_DEFINITIONS.md before introducing terms
2. Use canonical terms from this document
3. On first use of technical terms, expand abbreviations: "A-J-A-R (anger-joy-anger-relief)"
4. For blink rate data, always include units: "blinks/min"

### When Updating Existing Content:
1. Replace non-canonical terms with approved versions
2. Check context to ensure "vulnerability" vs "susceptibility" distinction is correct
3. Standardize notation to "A-J-A-R" format
4. Add units to all blink rate measurements

### When Ambiguous:
1. Refer to this document for guidance
2. When term usage is context-dependent, choose based on domain (code vs research)
3. Document any deviations with clear rationale

---

## Rationale for Standardization

### Why "Emotional Sequencing" over "Emotional Cycling"?
"Sequencing" emphasizes the deliberate ordering and design aspect, while "cycling" suggests repetitive loops without intentional design. Both describe the same phenomenon, but "sequencing" better reflects the algorithmic and intentional nature of platform design.

### Why "A-J-A-R" hyphenated notation?
Hyphenation creates clear visual separation between components and prevents confusion with acronyms (A-J-A-R appears to be a word). Consistency with hyphenated notation is standard in technical documentation.

### Why Separate "Vulnerability" and "Susceptibility"?
- **Vulnerability** historically appears in software security and technical contexts
- **Susceptibility** aligns with psychological/behavioral research terminology
- This distinction prevents confusion between technical measurement systems and behavioral characteristics

### Why Explicit Units for Blink Rate?
Blink rate measurements are quantitative and appear in multiple formats across literature. Explicit units ("blinks/min") prevent interpretation errors when data is cited or referenced outside original context.
