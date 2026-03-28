# Persuasion-Max v2: Research Expansion Architecture

## Status: v1 Limitation Diagnosis → v2 Blueprint

**v1 operated on a single theoretical substrate** — Smith & Ellsworth (1985) cognitive appraisal theory, 7 continuous dimensions, calibrated on 1 corpus (Persuasion for Good, charity domain only). This document maps the full landscape of computational persuasion research as of March 2026 and architects the expanded system.

---

## PART 1: WHAT v1 MISSED (Gap Analysis)

### 1.1 The 7-Dimension Bottleneck

v1 extracts 7 appraisal dimensions from stimulus text:
- novelty, valence, goal_relevance, coping_potential, agency, certainty, temporal_proximity

These measure **how a person evaluates a situation** (cognitive appraisal). But persuasion research has identified at least **4 orthogonal prediction surfaces** that v1 ignores entirely:

| Surface | What It Measures | Signal Source | v1 Coverage |
|---------|-----------------|---------------|-------------|
| Cognitive Appraisal | How the recipient evaluates the stimulus | LLM inference | 7/7 dimensions |
| Linguistic Surface | Measurable textual properties correlated with persuasion | Dictionary lookup (LIWC) | 0/10+ features |
| Technique Taxonomy | Which discrete persuasion technique is deployed | Span-level classification | 0/25+ techniques |
| Recipient Profile | Who is being persuaded (personality, ideology, priors) | Big Five + demographics | 0/5+ traits |
| Strategy Sequencing | Which technique to deploy at which point in a dialogue | Intent-to-strategy reasoning | Partial (SequenceAnalyzer) |

### 1.2 Single-Corpus Calibration

v1 was fitted exclusively on Persuasion for Good (Wang et al. 2019) — 1,017 dialogues, all charity persuasion, all English, all Amazon Mechanical Turk workers. This means:
- Every weight reflects "what persuades American crowdworkers to donate to charity"
- Zero signal about e-commerce, political, health, marketing, or adversarial persuasion
- Zero cross-cultural validity
- Zero personality-conditioned variation

---

## PART 2: AVAILABLE DATASETS (Downloadable Now)

### Tier 1: Primary Calibration Corpora

| Dataset | Size | Domain | Ground Truth | Source | Access |
|---------|------|--------|--------------|--------|--------|
| **DailyPersuasion** | 78,000 dialogues | 35 domains | Intent + strategy annotations | PersuGPT (ACL 2024) | https://persugpt.github.io — English dataset released 03/2024 |
| **HumanChoicePrediction** | 87,000 decisions | Language-based persuasion games | Real human binary choices | Shapira et al. (TACL 2025) | https://github.com/eilamshapira/HumanChoicePrediction |
| **Persuasion for Good** | 1,017 dialogues | Charity donation | Donation amount (continuous) | Wang et al. 2019 | Already integrated in v1 |
| **PERSUADE 2.0** | Large-scale | Written argumentation | Quality scores | Crossley et al. 2024 | https://github.com/scrosseye/persuade_corpus_2.0 |
| **Paired Persuasion** | Sentence pairs | General | Persuasive vs. non-persuasive (controlled for topic, author, length) | Guerini et al. (NAACL 2015) | https://github.com/marcoguerini/paired_datasets_for_persuasion |

### Tier 2: Technique Detection Training Data

| Dataset | Size | Labels | Languages | Source |
|---------|------|--------|-----------|--------|
| **SemEval 2023 Task 3** | Multi-lingual news | 23 persuasion techniques, paragraph-level | 6+ languages | Piskorski et al. 2023 |
| **SemEval 2024 Task 4** | Memes | Persuasion techniques in multimodal content | 12 subtasks | Dimitrov et al. 2024 |
| **CLEF 2024 CheckThat! Task 3** | News articles | Span-level technique detection | FR, DE, IT, BG, PL, RU | Piskorski et al. 2024 |
| **SlavicNLP 2025** | Parliamentary debates + social media | 25 techniques, span-level | BG, HR, PL, RU, SI | Piskorski et al. 2025 |

### Tier 3: Behavioral Outcome Data

| Dataset | Size | Signal | Why It Matters |
|---------|------|--------|---------------|
| **Transsuasion (PersuasionBench)** | Tweet pairs | Same meaning, different wording → different likes | Isolates WORDING effect from CONTENT effect |
| **r/ChangeMyView (WinningArguments)** | Large | Delta awards = "this changed my mind" | Real-world belief change with natural language |
| **BIG5-CHAT** | Large-scale dialogue | Personality-conditioned conversations | Recipient personality modeling training data |
| **APE (AttemptPersuadeEval)** | Multi-turn | Persuasion attempts across harmful/benign topics | Safety-oriented persuasion measurement |

### Tier 4: Emerging / Multimodal

| Dataset | Signal | Status |
|---------|--------|--------|
| **MMPersuade** | Multimodal persuasion (text + image + video) | 2025, 450 dialogues, 3 persuasion contexts |
| **PersuasiveToM** | Theory of Mind in persuasive dialogues | Built on DailyPersuasion, evaluates mental state tracking |
| **FARM** | Adversarial fact-based persuasion | 1,500 sessions |

---

## PART 3: EXPANDED FEATURE ARCHITECTURE

### Layer 1: Cognitive Appraisal (Existing — 7 dimensions)

Smith & Ellsworth 1985. Currently extracted via heuristic/Ollama/Claude modes.

```
novelty:            [0.0 – 1.0]  How unexpected/familiar
valence:            [-1.0 – 1.0] Positive/negative hedonic tone
goal_relevance:     [0.0 – 1.0]  How much it matters to recipient's goals
coping_potential:   [0.0 – 1.0]  Can the recipient handle the ask?
agency:             [0.0 – 1.0]  Who controls the outcome?
certainty:          [0.0 – 1.0]  How predictable is the outcome?
temporal_proximity: [0.0 – 1.0]  How urgent/immediate?
```

**Calibration status:** 5 FITTED weights, 2 CALIBRATED, interaction terms discovered (valence × goal_relevance = 0.147, valence × agency = 0.136).

### Layer 2: Linguistic Surface Features (NEW — 10+ dimensions)

Based on Ta et al. 2022 and LIWC-22 (Boyd et al. 2022). These require NO LLM inference — pure dictionary/regex extraction.

```
word_count:          int       Raw length of stimulus
emotionality:        [0.0-1.0] % words in LIWC emotion categories
concreteness:        [0.0-1.0] Concrete vs. abstract language ratio
analytical_thinking:  [0.0-1.0] LIWC analytical thinking score
lexical_diversity:   [0.0-1.0] Type-token ratio
hedge_density:       [0.0-1.0] % hedging words (might, perhaps, could)
certainty_markers:   [0.0-1.0] % certainty words (definitely, always, clearly)
self_reference:      [0.0-1.0] % first-person pronouns (I, me, my)
reading_difficulty:  [0.0-1.0] Flesch-Kincaid or similar
pronoun_ratio:       float     You-words / I-words ratio (status/clout signal)
tone_positive:       [0.0-1.0] % positive sentiment words
tone_negative:       [0.0-1.0] % negative sentiment words
```

**Empirical finding already documented:** Manipulative content is measurably MORE emotional, LESS analytical, LONGER, with HIGHER lexical diversity, and contains MORE self-reference and certainty words than truthful content (Wilczyński et al. 2024). GPT-4 was the only model that reversed this pattern, producing shorter manipulative content (matching human behavior).

**Implementation:** Open-source LIWC-equivalent dictionaries exist. Can also use `empath` (Python), `textstat` (readability), or custom regex. No API costs.

### Layer 3: Persuasion Technique Detection (NEW — 25 binary classifiers)

Based on the SemEval/CLEF taxonomy (Piskorski et al. 2023, extended 2025):

```
TECHNIQUES (25 categories):
├── Emotional Appeals
│   ├── appeal_to_fear
│   ├── appeal_to_pity (NEW in 2025 taxonomy)
│   ├── flag_waving
│   └── loaded_language
├── Logical Fallacies
│   ├── false_dilemma
│   ├── false_equivalence (NEW in 2025 taxonomy)
│   ├── straw_man
│   ├── red_herring
│   └── whataboutism
├── Credibility Attacks/Appeals
│   ├── appeal_to_authority
│   ├── name_calling_labeling
│   ├── doubt
│   └── guilt_by_association
├── Simplification
│   ├── causal_oversimplification
│   ├── black_and_white_fallacy
│   └── thought_terminating_cliché
├── Social Pressure
│   ├── bandwagon
│   ├── appeal_to_popularity
│   └── appeal_to_values
├── Repetition/Emphasis
│   ├── repetition
│   ├── slogans
│   └── exaggeration_minimisation
└── Deception
    ├── obfuscation
    ├── smears
    └── misrepresentation
```

**Implementation options:**
1. **Zero-shot LLM classification** — prompt Claude/Ollama with technique definitions, get binary labels per span
2. **Fine-tuned transformer** — train on SemEval 2023/2024 labeled data (best F1 scores from competition: 0.49–0.78 depending on technique)
3. **Hybrid** — LLM for initial detection, regex patterns for high-confidence techniques (loaded language, repetition)

**Novel contribution:** No existing system combines technique detection WITH appraisal scoring WITH circuit prediction. Technique detection tells you WHAT is being used. Appraisal scoring tells you HOW the recipient processes it. Circuit prediction tells you WHAT BEHAVIOR results.

### Layer 4: Recipient Profile Model (NEW — 5+ trait dimensions)

Based on Big Five personality model + persuasion personalization literature (Matz et al. 2024, Kaptein et al. 2015).

```
RECIPIENT TRAITS:
openness:           [0.0-1.0]  → modulates: novelty sensitivity, curiosity response
conscientiousness:  [0.0-1.0]  → modulates: certainty weight, analytical processing
extraversion:       [0.0-1.0]  → modulates: social proof sensitivity, bandwagon
agreeableness:      [0.0-1.0]  → modulates: compliance baseline, reciprocity
neuroticism:        [0.0-1.0]  → modulates: threat sensitivity, loss aversion

OPTIONAL EXTENSIONS:
political_ideology: [left-right scale]  → modulates: authority appeal, flag-waving
moral_foundations:  [care/fairness/loyalty/authority/purity scores]
prior_belief:       [0.0-1.0]  → initial stance on the specific topic
```

**Key research finding:** LLMs adapt their persuasive linguistic style when given personality trait cues — especially for Neuroticism (more anxiety words), Conscientiousness (more achievement words), and Openness (fewer cognitive process words). This means the SAME stimulus scores differently depending on who receives it.

**Implementation:** Recipient profile modulates the circuit weights:
- High-Neuroticism recipient: amygdala_weight × 1.3, approach_weight × 0.8
- High-Agreeableness recipient: compliance_baseline += 0.15, retaliation_probability × 0.6
- High-Openness recipient: novelty_weight × 1.4, certainty_weight × 0.7

These modulation coefficients need empirical fitting from personality-conditioned persuasion data (BIG5-CHAT, Matz et al. 2024).

### Layer 5: Strategy Sequencing (EXPANDED — from SequenceAnalyzer)

v1's SequenceAnalyzer tracked trajectory through 7D appraisal space. v2 expands to:

```
STRATEGY SEQUENCING:
├── Turn-level intent classification (what is each utterance trying to do?)
├── Strategy selection (which of 40+ techniques to deploy next?)
├── Prediction error engineering (does this turn violate recipient expectations?)
├── Cumulative persuasion score (running total across turns)
├── Resistance detection (when does the recipient show counter-arguing signals?)
└── Optimal strategy ordering (which sequence of techniques maximizes compliance?)
```

**Data source:** DailyPersuasion (78K dialogues) has per-turn intent + strategy annotations across 35 domains. PersuGPT's model does intent-to-strategy reasoning. HumanChoicePrediction has 87K real decisions under different expert agent strategies.

---

## PART 4: EXPANDED CIRCUIT MODEL

### v1 Circuit Formula (3 circuits, linear + 2 interaction terms)

```
approach     = w1*valence + w2*goal_relevance + w3*coping_potential + w4*agency
             + β1*(valence × goal_relevance) + β2*(valence × agency)
avoidance    = w5*(-valence) + w6*goal_relevance + w7*(1-coping_potential) + w8*certainty
deliberation = w9*novelty + w10*(1-certainty) + w11*goal_relevance
```

### v2 Circuit Formula (3 circuits, multi-layer input)

```
# LAYER 1: Appraisal inputs (existing)
appraisal_approach     = f(novelty, valence, goal_relevance, coping_potential, agency, certainty, temporal_proximity)
appraisal_avoidance    = g(...)
appraisal_deliberation = h(...)

# LAYER 2: Linguistic surface modifiers
linguistic_modifier = {
    emotionality     → amplifies approach OR avoidance (sign depends on tone)
    concreteness     → reduces deliberation (concrete = easier to process)
    certainty_markers → suppresses deliberation, amplifies approach
    hedge_density    → increases deliberation, weakens approach
    reading_difficulty → increases deliberation (cognitive load)
    self_reference   → signals manipulation (insula activation)
}

# LAYER 3: Technique multipliers
technique_multiplier = {
    appeal_to_fear   → avoidance × 1.4
    social_proof     → approach × 1.2, deliberation × 0.8
    scarcity         → temporal_proximity += 0.3, avoidance × 1.1
    authority        → certainty += 0.2, deliberation × 0.7
    loaded_language  → emotionality += 0.3
    repetition       → certainty += 0.15 (familiarity = fluency = truth)
}

# LAYER 4: Recipient modulation
recipient_mod = {
    high_neuroticism    → avoidance × 1.3
    high_agreeableness  → compliance_baseline += 0.15
    high_openness       → novelty_sensitivity × 1.4
    low_conscientiousness → deliberation × 0.7
}

# FINAL PREDICTION
approach_final     = appraisal_approach × linguistic_modifier × technique_multiplier × recipient_mod
avoidance_final    = appraisal_avoidance × linguistic_modifier × technique_multiplier × recipient_mod  
deliberation_final = appraisal_deliberation × linguistic_modifier × technique_multiplier × recipient_mod

behavior = {
    immediate_compliance:  sigmoid(approach_final - avoidance_final - deliberation_final × 0.3)
    repeat_compliance:     f(approach_final, deliberation_suppression, insula_activation)
    retaliation_probability: g(avoidance_final, agency_type, insula_activation)
}
```

---

## PART 5: IMPLEMENTATION PRIORITY SEQUENCE

### Phase 1: Linguistic Surface Layer (Cheapest, Fastest)
- Implement LIWC-equivalent extraction using open-source dictionaries
- Add 10+ features with zero API cost
- Cross-validate against PFG corpus: do linguistic features predict donation independently of appraisal scores?
- Expected: 5-15pp AUC improvement from orthogonal signal

### Phase 2: Multi-Corpus Calibration
- Download and process DailyPersuasion (78K dialogues, 35 domains)
- Download and process HumanChoicePrediction (87K decisions)
- Download Paired Persuasion dataset (controlled pairs)
- Re-fit ALL weights across multiple domains simultaneously
- Measure: do weights generalize or are they domain-specific? (likely domain-specific)

### Phase 3: Technique Detection
- Build 25-class technique detector using SemEval training data
- Test zero-shot LLM classification accuracy against labeled spans
- Integrate technique labels as categorical inputs to circuit model
- Novel contribution: technique × appraisal interaction terms (does "appeal to fear" interact with certainty differently than "social proof"?)

### Phase 4: Recipient Modeling
- Integrate Big Five as circuit weight modulators
- Calibrate personality × persuasion interactions using BIG5-CHAT data
- Test: same stimulus, 5 different personality profiles → 5 different behavioral predictions
- This is where the Google interview demo becomes powerful: "I can show you how the SAME ad copy activates different circuits depending on recipient personality"

### Phase 5: Cross-Validation & Weight Registry
- Full weight registry with provenance: FITTED (from data), CONSTRAINED (from literature), UNCALIBRATED (theoretical)
- Cross-domain transfer tests: do charity weights predict e-commerce behavior?
- Interaction term discovery across all layers: which cross-layer interactions dominate?

---

## PART 6: KEY PAPERS (Expanded Bibliography)

### Foundational
1. Smith & Ellsworth (1985) — Patterns of Cognitive Appraisal in Emotion (the 7 dimensions)
2. Damasio (1994) — Somatic Marker Hypothesis
3. Petty & Cacioppo (1986) — Elaboration Likelihood Model
4. Cialdini (2001) — 6 Principles of Persuasion

### Computational Persuasion (2024-2026)
5. Jin et al. (ACL 2024) — PersuGPT: 13K scenarios, 35 domains, intent-to-strategy reasoning
6. Shapira et al. (TACL 2025) — 87K human decisions, simulation-based off-policy evaluation
7. Singh et al. (2024) — Transsuasion: tweet pairs, PersuasionBench, PersuasionArena
8. Piskorski et al. (2023/2024/2025) — 25 persuasion technique taxonomy, SemEval/CLEF shared tasks
9. Bassi et al. (Frontiers 2024) — Systematic survey: ML/NLP methods for persuasion study

### Personalization & Personality
10. Matz et al. (2024) — LLM personalized persuasion at scale
11. Mieleszczenko-Kowszewicz et al. (2024) — Dark patterns of personalized persuasion, LIWC features × Big Five
12. Salvi et al. (2024) — Personal information increases LLM persuasiveness
13. Vu et al. (2024) — BIG5-CHAT: training personality into LLMs

### Meta-Analyses & Benchmarks
14. Huang & Wang (Nature 2025) — Meta-analysis: LLMs show no significant overall difference from humans (g=0.02)
15. Pauli et al. (2025) — Regression model scoring persuasiveness of LLM rewrites
16. Alignment Research Center (2025) — APE: multi-turn persuasion attempt evaluation

### Linguistic Features
17. Boyd et al. (2022) — LIWC-22: 12,000+ words mapped to 100+ psychological categories
18. Ta et al. (2022) — 10 linguistic features linked to persuasiveness
19. Pennebaker et al. (2001/2014) — LIWC: analytical thinking, clout, authenticity, emotional tone

### Neuroscience (from v1)
20. TRIBE v2 (Meta, March 2026) — Open-source brain encoding model, 70K cortical vertices
21. Falk et al. (2010) — Neural correlates of feeling persuaded

---

## PART 7: COMPETITIVE LANDSCAPE (Updated)

| Tool | Approach | Strength | Weakness |
|------|----------|----------|----------|
| **Artificial Societies** | Synthetic population simulation (300-5K personas) | Social graph dynamics, visual narrative | Black box, no mechanistic diagnosis |
| **Blok** | Synthetic users interacting with prototypes | Product testing, UI evaluation | Not persuasion-specific |
| **Synthetic Users** | AI personas for user research | UX research automation | No behavioral prediction |
| **PersuGPT** | Fine-tuned LLM for persuasive dialogue | Intent-to-strategy reasoning, 35 domains | Generates persuasion, doesn't predict outcomes |
| **PersuasionBench** | Benchmark suite for LLM persuasiveness | Standardized evaluation, transsuasion tasks | Measurement only, no diagnosis |
| **ADPT-AI** | Transformer-based technique detection | Span-level persuasion technique classification | Detection only, no prediction |
| **Persuasion-Max v2** | Multi-layer mechanistic predictor | White-box diagnosis, circuit-level explanation, technique + appraisal + personality integration | Early-stage, needs multi-domain calibration |

**Unique positioning:** No existing tool combines ALL of:
- Appraisal dimension extraction
- Linguistic surface analysis
- Technique detection
- Recipient personality modeling
- Circuit competition prediction
- Behavioral outcome forecasting
- Mechanistic diagnosis ("here's WHY it fails and WHAT to change")

---

## PART 8: HONEST UNCERTAINTY REGISTER

### What We Know (Empirically Validated)
- Appraisal interaction terms outpredict linear weights (PFG calibration)
- Linguistic surface features discriminate manipulative from truthful content
- Personality traits modulate persuasion susceptibility (multiple RCTs)
- LLMs are approximately as persuasive as humans (meta-analysis, g=0.02)

### What We Suspect (Theoretically Grounded, Not Yet Calibrated)
- Cross-layer interactions (technique × personality) will dominate linear effects
- Domain-specific weights will outperform universal weights
- Linguistic surface features will provide independent predictive signal above appraisal

### What We Don't Know
- Whether appraisal scores computed by LLMs correlate with actual human appraisals
- Whether circuit competition model generalizes beyond charity persuasion
- Whether personality modulation coefficients are stable across contexts
- The full interaction structure across 25+ features (combinatorial explosion)

---

*Document generated March 28, 2026. Research sweep covers publications through March 2026.*
*All datasets listed have been verified as publicly accessible or available upon request.*
