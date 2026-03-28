# Cross-Layer Interaction Effects in Computational Persuasion: Technique × Personality × Moral Foundations Interaction Matrices

## Abstract

We present a 5-layer mechanistic model for predicting persuasion outcomes that operates across cognitive appraisal, linguistic surface features, persuasion technique detection, recipient personality profiling, and domain-specific weight registries. Calibrated on N=126,288 samples across two corpora (DailyPersuasion, HumanChoicePrediction), the model achieves AUC 0.667-0.682 within-corpus. We find that (1) linguistic surface features contribute +10.4pp AUC over appraisal dimensions alone, while technique binary detection adds zero incremental signal; (2) cross-domain transfer drops AUC by 10-13pp, confirming the need for domain-specific weight registries; (3) the top cross-layer interaction (valence × reading_difficulty) follows an inverted-U shape and adds +0.77pp AUC; (4) stacking top-5 interactions yields +1.9pp over the linear model. We compute the first systematic 400-cell technique × personality interaction matrix and 480-cell technique × moral foundations matrix, identifying persona-sensitive techniques (emotional_appeal_positive: 21.8pp spread across personas) and persona-insensitive blunt instruments (rhetorical_question: 3.2pp spread). Moral reframing (Feinberg & Willer 2015) is partially captured: care framing produces 8.4pp higher compliance for liberal profiles than loyalty framing, though the reciprocal effect on conservative profiles is modest (0.8pp) due to heuristic extraction limitations.

## 1. Introduction

Computational models of persuasion typically operate at a single analytical layer: either detecting which persuasion techniques are present (Zeng et al. 2024), predicting which message framings will be effective (Shapira et al. 2025), or modeling individual differences in persuasion susceptibility (Matz et al. 2024). The gap is integration: no existing system models the interaction between technique deployment, recipient personality, moral foundations, and linguistic presentation simultaneously.

We address this gap with a 5-layer architecture that computes persuasion outcomes mechanistically:
1. **Linguistic surface** — 12 text features (emotionality, reading difficulty, lexical diversity, etc.)
2. **Cognitive appraisal** — 7 dimensions per Smith & Ellsworth (1985) and Scherer (2001)
3. **Technique detection** — 40 techniques from the Zeng et al. (2024) taxonomy
4. **Recipient modulation** — 16-dimension profile (Big Five, Moral Foundations, political orientation, situational)
5. **Domain-specific weights** — separate registries for e-commerce, campaign messaging, and crisis PR

The model outputs competing circuit activations (approach/avoidance/deliberation) inspired by Knutson et al. (2007) and predicts three behavioral horizons: immediate compliance, repeat compliance, and retaliation probability.

This paper reports three contributions:
- **Cross-layer interaction discovery** across 126K samples from two corpora
- **The 400-cell technique × personality matrix** — which specific techniques work on which personality types
- **Quantification of moral reframing** — the Feinberg & Willer (2015) effect computed as percentage-point compliance shifts

## 2. Related Work

**Persuasion technique detection.** Zeng et al. (2024) define a 40-technique taxonomy (20 high-intensity, 20 low-intensity) and train classifiers for technique identification. PersuGPT (Li et al. 2024) extends this to multi-turn dialogue with strategy-aware generation across 13,000 scenarios. Our work uses their taxonomy as Layer 3 but finds that binary technique detection carries zero incremental predictive signal — the predictive value lies in technique × context interactions.

**Computational persuasion prediction.** Shapira et al. (2025) model human choice prediction in persuasion games, achieving strong predictive performance using BERT embeddings and game-theoretic features. Their HumanChoicePrediction dataset provides our strongest ground truth (real binary decisions). Our approach differs in using interpretable mechanistic features rather than black-box embeddings.

**Individual differences in persuasion.** Matz et al. (2024) demonstrate that psychologically targeted messaging increases persuasion effectiveness. Our recipient modulation layer (16 dimensions × 10 preset personas) operationalizes this finding computationally, allowing prediction of which message works on which personality type.

**Moral Foundations and persuasion.** Feinberg & Willer (2015) show that reframing policies using the audience's moral foundations increases support across the political spectrum. Our MFT interaction matrix quantifies this effect computationally.

**Related systems.** Transsuasion (Deng et al. 2023) generates paraphrases optimized for persuasiveness. TRIBE v2 (Wilczynski et al. 2024) detects influence operations via linguistic analysis. MoralBERT (Trager et al. 2022) classifies moral foundations in text. Our system integrates these capabilities — detection, prediction, and generation — in a single mechanistic pipeline.

## 3. Method

### 3.1 Architecture

The pipeline processes a text stimulus through five sequential layers:

**Layer 1: Linguistic Surface (12 features, $0 compute cost)**
Dictionary-based extraction of word count, emotionality, concreteness, analytical thinking, lexical diversity, hedge density, certainty markers, self-reference, other-reference, reading difficulty, and sentiment polarity. Based on LIWC-22 (Boyd et al. 2022) dictionaries.

**Layer 2: Cognitive Appraisal (7 dimensions)**
Extraction of novelty, valence, goal_relevance, coping_potential, agency, certainty, and temporal_proximity. Three extraction modes: heuristic (regex, $0), Ollama (local LLM), Claude API (highest quality).

**Layer 3: Technique Detection (40 binary features)**
Classification of persuasion techniques from the Zeng et al. (2024) taxonomy. Each technique detection triggers appraisal shifts and circuit modifier multipliers defined in a 40-entry modifier map.

**Layer 4: Recipient Modulation (16 dimensions)**
Individual-difference modulation via Big Five personality (5), Moral Foundations Theory (6), political orientation (2), and situational factors (3). Each trait modulates circuit weights based on literature-constrained rules.

**Layer 5: Domain-Specific Weights**
Separate weight registries for e-commerce, campaign messaging, and crisis PR contexts, with domain-specific outcome metrics.

**Output:** Three competing circuit activations (approach via NAcc, avoidance via amygdala, deliberation via ACC/dlPFC), converted to behavioral probabilities via softmax, plus three temporal horizons and domain-specific outcomes.

### 3.2 Calibration Corpora

| Corpus | N | Domain | Outcome | Source |
|--------|---|--------|---------|--------|
| DailyPersuasion | 77,999 | 53K opinion + 24K commercial | Binary (accepted/rejected) | Li et al. 2024 |
| HumanChoicePrediction | 48,289 | Commercial | Binary (go/no-go) | Shapira et al. 2025 |
| **Total** | **126,288** | | | |

### 3.3 Feature Extraction

All calibration uses heuristic extraction mode for speed. Each stimulus yields a 59-dimensional feature vector: 7 appraisal + 12 linguistic + 40 technique binary.

### 3.4 Interaction Discovery

We test 844 pairwise cross-layer interactions. For each pair (A, B): fit base logistic regression (59 linear features, L2 regularization, 5-fold CV), add interaction term A×B, measure AUC lift. Interactions with lift > 0.3pp are retained. Top interactions are tested for shape (linear vs threshold vs inverted-U) via BIC comparison.

## 4. Results

### Table 1: AUC by Feature Set × Corpus

| Feature Set | DailyPersuasion | HCP |
|-------------|----------------|-----|
| Appraisal only (7) | 0.563 | 0.550 |
| + Technique binary (47) | 0.584 | 0.549 |
| + Linguistic (19) | **0.667** | **0.634** |
| All 59 features | 0.667 | 0.634 |

**Finding 1:** Linguistic surface features provide +10.4pp AUC lift over appraisal alone (DailyPersuasion). Technique binary features add zero incremental signal on top of linguistic features. This suggests that the linguistic layer already captures the textual properties that technique detection attempts to classify — technique presence is redundant with linguistic style.

### Table 2: Cross-Domain Transfer Matrix

| Train \ Test | DailyPersuasion | HCP |
|-------------|----------------|-----|
| DailyPersuasion | **0.682** | 0.547 |
| HCP | 0.521 | **0.648** |

**Finding 2:** Cross-domain AUC drops 10-13pp. Weights fitted on persuasion dialogues do not predict hotel booking decisions. This confirms the need for domain-specific weight registries.

### Table 3: Top 7 Cross-Layer Interactions

| # | Feature A | Feature B | AUC Lift | Shape |
|---|-----------|-----------|----------|-------|
| 1 | valence | reading_difficulty | +0.77pp | INVERTED_U |
| 2 | word_count | evidence_based | +0.53pp | LINEAR |
| 3 | goal_relevance | self_reference | +0.48pp | LINEAR |
| 4 | reading_difficulty | bandwagon | +0.39pp | INVERTED_U |
| 5 | reading_difficulty | gain_frame | +0.38pp | INVERTED_U |
| 6 | reading_difficulty | social_proof | +0.36pp | INVERTED_U |
| 7 | word_count | scarcity_appeal | +0.30pp | LINEAR |

**Finding 3:** The top interaction (valence × reading_difficulty) follows an inverted-U shape — positive valence helps most at moderate reading difficulty, with diminishing returns at extremes. Stacking top-5 interactions yields +1.9pp over linear-only (0.636 → 0.655).

**Finding 4:** All top interactions are domain-unstable — they hold in commercial but not opinion-change contexts. No interaction is reliable across both domains.

### Table 4: Technique × Persona Matrix (Selected Cells)

**Highest compliance combinations:**

| Technique | Persona | Compliance |
|-----------|---------|-----------|
| emotional_appeal_positive | social_shopper | 74.7% |
| emotional_appeal_positive | liberal_base | 73.1% |
| empathy_appeal | social_shopper | 68.0% |
| bandwagon_pressure | impulse_buyer | 67.3% |
| empathy_appeal | liberal_base | 66.6% |

**Highest retaliation combinations:**

| Technique | Persona | Retaliation |
|-----------|---------|------------|
| emotional_manipulation | impulse_buyer | 30.3% |
| emotional_manipulation | issue_activist | 25.4% |
| emotional_manipulation | skeptical_researcher | 25.2% |

**Finding 5:** Persona-sensitive techniques show >20pp compliance spread across personas: emotional_appeal_positive (21.8pp) and bandwagon_pressure (20.3pp). These are the personalization-responsive techniques. Persona-insensitive techniques (rhetorical_question: 3.2pp, red_herring: 4.0pp) work roughly the same on everyone.

**Finding 6:** Most susceptible persona: impulse_buyer (56.8% avg compliance). Most resistant: disengaged_voter (49.5%). The 7.3pp gap between most and least susceptible personas is narrower than the 21.8pp technique sensitivity spread, suggesting technique selection matters more than audience selection.

### Table 5: Moral Reframing (Scenario 2)

| Frame | Liberal Base | Conservative Base | Lift |
|-------|-------------|------------------|------|
| Care/fairness | 56.6% | 47.7% | — |
| Loyalty/heritage | 48.3% | 48.5% | +0.8pp for conservatives |

**Finding 7:** Care framing produces 8.4pp higher compliance for liberal profiles than loyalty framing (56.6% vs 48.3%). The reciprocal effect — loyalty framing increasing conservative compliance — is present but small (0.8pp), likely due to heuristic extraction limitations that fail to differentiate the moral content of the two frames at the appraisal level.

### Table 6: Crisis PR Scenario Results

| Approach | Media Trust | Customer Trust | Regulator Trust | Retaliation |
|----------|-----------|----------------|-----------------|------------|
| Transparent | 52.3% | 50.3% | 51.7% | 0.0% |
| Defensive | 25.9% | 24.1% | 24.0% | 46.5% |

**Finding 8:** Transparent crisis response produces 2x the trust recovery of defensive response across all stakeholder types. Defensive techniques (whataboutism, straw_man) produce 46.5% retaliation probability — the highest retaliation rate in any scenario tested.

### Weight Stability Classification

| Classification | Count | % |
|---------------|-------|---|
| UNIVERSAL | 13 | 22% |
| DOMAIN-SPECIFIC | 33 | 56% |
| INSIGNIFICANT | 13 | 22% |

## 5. Discussion

### Technique binary = noise; technique × context = signal

The most surprising finding is that technique binary detection adds zero incremental AUC over linguistic surface features. This does not mean techniques are irrelevant — the technique × personality interaction matrix produces meaningful 20pp+ compliance spreads. Rather, it means that detecting technique *presence* is redundant with measuring linguistic *properties*: a text that uses social proof naturally exhibits higher self-reference density and lower reading difficulty, which the linguistic layer already captures.

The implication for computational persuasion: stop building better technique classifiers. Build better interaction models.

### Linguistic layer outperforms technique layer

The +10.4pp AUC contribution of 12 dictionary-based linguistic features over 7 appraisal dimensions is unexpectedly large. These features cost nothing to compute (no LLM calls), run in <1ms, and capture properties of the text that the appraisal extractor misses: reading difficulty, emotionality density, self-reference patterns. This suggests that the "how it's written" signal is as important as the "what it says" signal for predicting persuasion outcomes.

### Domain-specific weights are mandatory

The 10-13pp transfer gap between corpora confirms that persuasion mechanics differ across contexts. A weight set that predicts charity donation success fails at predicting hotel booking decisions. The 33 features classified as DOMAIN-SPECIFIC (56% of all features) validate the domain registry architecture.

### Honest limitations

1. **Heuristic extraction ceiling.** All results use regex-based extraction. LLM extraction would likely improve AUC by 5-15pp based on the PFG pilot (0.589 heuristic → 0.654 Ollama). The moral reframing quantification is particularly limited — the heuristic extractor cannot differentiate care vs loyalty framing at the appraisal level, producing the weak 0.8pp conservative reframing effect.

2. **Synthetic training data.** DailyPersuasion (77K of 126K samples) is GPT-generated. The outcome labels are inferred from generated persuadee responses, not from actual behavioral change. This inflates within-corpus AUC and may not reflect real persuasion dynamics.

3. **No real behavioral validation.** Neither corpus provides actual conversion data, click-through rates, or measured attitude change. The HCP dataset is closest (real human binary decisions) but is confounded by game context.

4. **Interaction effects are modest.** The +1.9pp stacking lift from top-5 interactions is below the 3pp threshold for a standalone publishable finding. The interactions are theoretically grounded but empirically small.

5. **UNCALIBRATED weights.** All crisis PR, campaign moral reframing, and stakeholder-type weights remain hand-tuned with no empirical grounding. No corpus in our collection covers these domains.

6. **Persona spread may be architectural.** The 21.8pp technique × persona spread is a property of the model's modulation rules, not of independently measured behavioral data. It reflects how we built the recipient modulator, not necessarily how real humans respond.

## 6. Future Work

1. **LLM extraction at scale.** Running Claude API extraction on the full 126K corpus would test whether the heuristic ceiling is the binding constraint on AUC.

2. **Real A/B test validation.** Scoring actual A/B test variants (CTAs, email subject lines, landing pages) with known conversion rates would provide the first behavioral validation of circuit predictions.

3. **Cross-cultural MFT calibration.** Moral Foundations vary across cultures (Graham et al. 2011). The current MFT profiles are U.S.-centric.

4. **Biosignal integration.** Aligning circuit predictions with fMRI (NAcc activation → approach, insula → avoidance) or GSR (arousal) would test the neuroanatomical claims directly.

5. **Temporal dynamics.** The model treats each stimulus as independent. Real persuasion is sequential — the effect of technique N depends on what techniques 1 through N-1 have already deployed.

## References

- Bechara, A., Damasio, H., Tranel, D., & Damasio, A. R. (1997). Deciding advantageously before knowing the advantageous strategy. Science, 275(5304), 1293-1295.
- Berns, G. S., & Moore, S. E. (2012). A neural predictor of cultural popularity. Journal of Consumer Psychology, 22(1), 154-160.
- Botvinick, M. M., Braver, T. S., Barch, D. M., Carter, C. S., & Cohen, J. D. (2001). Conflict monitoring and cognitive control. Psychological Review, 108(3), 624-652.
- Boyd, R. L., Ashokkumar, A., Seraj, S., & Pennebaker, J. W. (2022). The development and psychometric properties of LIWC-22. UT Austin.
- Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. PNAS, 114(28), 7313-7318.
- Cialdini, R. B. (2001). Influence: Science and Practice (4th ed.). Allyn & Bacon.
- Craig, A. D. (2009). How do you feel—now? The anterior insula and human awareness. Nature Reviews Neuroscience, 10(1), 59-70.
- Deng, Y., et al. (2023). Transsuasion: Automatic paraphrase for persuasion. arXiv:2302.00994.
- Falk, E. B., et al. (2012). From neural responses to population behavior: Neural focus group predicts population-level media effects. Psychological Science, 23(5), 439-445.
- Feinberg, M., & Willer, R. (2015). From gulf to bridge: When do moral arguments facilitate political influence? Personality and Social Psychology Bulletin, 41(12), 1665-1681.
- Graham, J., Haidt, J., & Nosek, B. A. (2009). Liberals and conservatives rely on different sets of moral foundations. Journal of Personality and Social Psychology, 96(5), 1029-1046.
- Knutson, B., Rick, S., Wimmer, G. E., Prelec, D., & Loewenstein, G. (2007). Neural predictors of purchases. Neuron, 53(1), 147-156.
- Li, Y., et al. (2024). PersuGPT: DailyPersuasion dataset and benchmark. GitHub/PersuGPT.
- Matz, S. C., et al. (2024). The potential of generative AI for personalized persuasion at scale. Scientific Reports, 14, 4692.
- Petty, R. E., & Cacioppo, J. T. (1986). The Elaboration Likelihood Model of persuasion. Advances in Experimental Social Psychology, 19, 123-205.
- Scherer, K. R. (2001). Appraisal considered as a process of multilevel sequential checking. In K. R. Scherer, A. Schorr, & T. Johnstone (Eds.), Appraisal Processes in Emotion.
- Shapira, E., et al. (2025). Human choice prediction in language-based persuasion games. GitHub/HumanChoicePrediction.
- Smith, C. A., & Ellsworth, P. C. (1985). Patterns of cognitive appraisal in emotion. Journal of Personality and Social Psychology, 48(4), 813-838.
- Trager, J., et al. (2022). The Moral Foundations Reddit Corpus. arXiv:2208.05545.
- Wang, X., et al. (2019). Persuasion for good: Towards a personalized persuasive dialogue system for social good. ACL.
- Wilczynski, A., et al. (2024). TRIBE v2: Influence operation detection via linguistic analysis.
- Zeng, G., et al. (2024). A taxonomy of persuasion techniques. ACL.
