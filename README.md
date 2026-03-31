# Persuasion-Max: A Multi-Layer Mechanistic Predictor of Persuasive Effectiveness

Research codebase for computational persuasion modeling by a behavioral scientist who treats influence as a mechanistic system rather than a copywriting vibe.

**5-layer architecture grounded in limbic neuroscience. 302 parameters (62.6% empirically grounded). Calibrated on 126K interactions across 2 corpora. 297 tests passing.**

## Abstract

Existing computational persuasion tools predict *whether* a message persuades but not *why* it succeeds or *how to improve it*. We present a 5-layer mechanistic framework that models the competition between approach (nucleus accumbens), avoidance (amygdala), and deliberation (ACC/dlPFC) circuits as a function of cognitive appraisal dimensions, linguistic surface features, persuasion technique detection, recipient personality modulation, and domain-specific weight registries. Calibrated on N=126,288 samples from DailyPersuasion (78K multi-domain dialogues) and HumanChoicePrediction (48K real human binary decisions), the model achieves AUC 0.638-0.652 within-corpus via 5-fold cross-validation. We find that (1) linguistic surface features contribute +8.3-9.3pp AUC over appraisal-only, while technique binary detection adds zero incremental signal — and actually *hurts* by 0.2-0.6pp; (2) cross-domain transfer drops AUC by 10-13pp, confirming the need for domain-specific weight registries; (3) the 400-cell technique x personality interaction matrix reveals persona-sensitive techniques with 21.8pp compliance spread across recipients; (4) moral reframing (Feinberg & Willer 2015) is architecturally supported but produces 0pp lift with heuristic extraction — the regex extractor cannot differentiate care vs loyalty framing at the appraisal level; LLM extraction is required to unlock this capability. A full weight registry audit documents all 302 parameters with provenance labels. The ablation report identifies 6 dead recipient traits and confirms that technique binary detection is the only layer that adds no marginal signal.

**Honest status:** 62.6% of parameters are empirically grounded (FITTED + CALIBRATED + CONSTRAINED). The remaining 37.4% are theory-derived with proposed calibration experiments. No real behavioral validation exists — all outcomes are proxies (donation decisions, game choices, synthetic acceptance labels). The heuristic extraction mode (regex keyword matching) imposes a ceiling that LLM extraction would likely raise by 5-15pp.

## Architecture

```
Text Stimulus
    │
    ├─── L1: Linguistic Surface (12 features, $0)
    │         word_count, emotionality, concreteness, analytical_thinking,
    │         lexical_diversity, hedge_density, certainty_markers,
    │         self_reference, other_reference, reading_difficulty, sentiment
    │
    ├─── L2: Cognitive Appraisal (7 dimensions)
    │         novelty, valence, goal_relevance, coping_potential,
    │         agency, certainty, temporal_proximity
    │         Extraction: heuristic ($0) | Ollama (local) | Claude API
    │
    ├─── L3: Technique Detection (54 techniques)
    │         40 Zeng taxonomy + 14 practitioner techniques
    │         Each triggers appraisal shifts + circuit modifier multipliers
    │
    ├─── L4: Recipient Modulation (16-dimension profile)
    │         Big Five (5) + Moral Foundations (6) + Political (2) + Situational (3)
    │         10 preset personas: impulse_buyer → issue_activist
    │
    └─── L5: Domain-Specific Weights
              ecommerce | campaign | crisis_pr registries
              Domain-specific outcome metrics (purchase_prob, trust_recovery, etc.)
              │
              ▼
    OUTPUT: approach / avoidance / deliberation activations
            → softmax → compliance / rejection / delay probabilities
            → 3 time horizons: immediate, repeat, retaliation
            → domain-specific outcomes
```

## Key Empirical Results

### Multi-Domain Calibration (N=126,288)

| Feature Set | DailyPersuasion (5-fold CV) | HCP (5-fold CV) |
|-------------|---------------------------|-----------------|
| L2: Appraisal only (7 dims) | 0.558 | 0.556 |
| L1+L2: + Linguistic (19 dims) | **0.652** | **0.638** |
| L1+L2+L3: + Technique binary (59 dims) | 0.650 | 0.632 |

**Finding:** Linguistic surface features provide +8-9pp AUC lift. Technique binary detection adds zero — it actually *reduces* AUC by 0.2-0.6pp (adds noise, not signal).

### Cross-Domain Transfer

| Train \ Test | DailyPersuasion | HCP |
|-------------|----------------|-----|
| DailyPersuasion | **0.682** | 0.547 |
| HCP | 0.521 | **0.648** |

**Finding:** 10-13pp transfer penalty. Weights fitted on persuasion dialogues do not predict hotel booking decisions. Domain-specific registries are mandatory.

### Technique × Personality Matrix (400 cells)

| Combination | Compliance |
|-------------|-----------|
| emotional_appeal_positive × social_shopper | **74.7%** |
| emotional_appeal_positive × liberal_base | 73.1% |
| empathy_appeal × social_shopper | 68.0% |
| bandwagon_pressure × impulse_buyer | 67.3% |

- Most susceptible persona: impulse_buyer (56.8% avg compliance)
- Most resistant persona: disengaged_voter (49.5%)
- Highest persona sensitivity: emotional_appeal_positive (21.8pp spread)
- Highest retaliation: emotional_manipulation × impulse_buyer (30.3%)

### Crisis PR Simulation

| Approach | Trust Recovery | Retaliation |
|----------|---------------|------------|
| Transparent | 50-52% | 0% |
| Defensive | 24-26% | **46.5%** |

### Weight Registry (302 parameters)

| Provenance | Count | % |
|-----------|-------|---|
| FITTED | 3 | 1.0% |
| CALIBRATED | 2 | 0.7% |
| CONSTRAINED | 184 | 60.9% |
| UNCALIBRATED | 113 | 37.4% |

62.6% empirically grounded. Full registry: `results/weight_registry.csv`.

### Ablation: What's Dead

**Dead recipient traits** (< 1pp impact when ablated): openness, liberty_oppression, fairness_cheating, authority_subversion, sanctity_degradation, prior_belief.

**Dead layer:** Technique binary detection (L3) — zero marginal AUC, confirmed across both corpora.

**Active layers:** L1 Linguistic (+8-9pp), L2 Appraisal (base), L4 Recipient (4.7pp max trait impact), L5 Domain (12.9pp ecommerce lift).

## Related Work

- **PersuGPT** (Li et al., 2024) — 13K multi-domain persuasion scenarios. Our DailyPersuasion calibration corpus.
- **HumanChoicePrediction** (Shapira et al., 2025) — Binary persuasion decisions in strategic games. Our strongest ground truth.
- **Zeng et al.** (ACL 2024) — 40-technique persuasion taxonomy. Our L3 technique detector.
- **Matz et al.** (Scientific Reports 2024) — LLM personalized persuasion at scale. Our L4 recipient modulation.
- **Feinberg & Willer** (PSPB 2015) — Moral reframing across political spectrum. Our MFT interaction matrix.
- **Knutson et al.** (Neuron 2007) — NAcc/insula predict purchase decisions at ~60%. Our circuit model foundation.
- **Smith & Ellsworth** (JPSP 1985) — Cognitive appraisal dimensions of emotion. Our L2 appraisal model.
- **Petty & Cacioppo** (1986) — Elaboration Likelihood Model. Our EL modulation in L4.
- **Graham, Haidt & Nosek** (JPSP 2009) — Moral Foundations Theory. Our 6-foundation MFT profiles.
- **Damasio** (1994) — Somatic marker hypothesis. Our somatic marker store.
- **Berns & Moore** (JCP 2012) — NAcc predicts cultural popularity, self-report doesn't.
- **Brady et al.** (PNAS 2017) — +20% diffusion per moral-emotional word.
- **Transsuasion** (Deng et al., 2023) — Persuasive paraphrase generation.
- **TRIBE v2** (Meta FAIR, 2026) — Brain encoding model for language.
- **MoralBERT** (Preniqi et al., 2022) — Moral foundations classification in text.
- **Cialdini** (2001, 2016) — Influence principles, Pre-Suasion, Unity.

## Running

```bash
# Single stimulus analysis
python analyze.py "Get Notion free"
python analyze.py compare "Submit" "Get Notion free"

# Domain-specific prediction
python -c "
from core.domain_predictor import DomainPredictor
dp = DomainPredictor()
r = dp.predict('50% off today only!', domain='ecommerce')
print(r.to_dict())
"

# API server (15 endpoints, CORS enabled)
pip install fastapi uvicorn
uvicorn api.server:app --port 8100

# Full calibration pipeline
python calibration/download_datasets.py      # parse corpora
python calibration/fit_domain_weights.py     # fit weights per domain
python calibration/discover_interactions.py  # cross-layer interactions
python calibration/compare_domains.py        # weight stability analysis

# Validation
python validation/full_audit.py              # layer ablation × corpus
python validation/weight_registry_audit.py   # parameter inventory
python validation/ablation_report.py         # dead feature identification

# Tests (297 passing)
python tests/test_pipeline.py      # 70 tests
python tests/test_recipient.py     # 71 tests
python tests/test_domain.py        # 87 tests
python tests/test_calibration.py   # 41 tests
python tests/test_research.py      # 28 tests
```

## Honest Limitations

1. **Heuristic extraction ceiling.** All calibration uses regex keyword matching. The Claude API extractor would likely raise AUC by 5-15pp but hasn't been tested at scale. The moral reframing conservative-side lift (+0.8pp) is suppressed because the heuristic extractor can't differentiate care vs loyalty language at the appraisal level.

2. **No real behavioral validation.** Neither corpus provides actual conversion rates, click-through rates, or measured attitude change. DailyPersuasion outcomes are inferred from GPT-generated persuadee responses. HCP outcomes are real human decisions but confounded by game context.

3. **Technique binary = noise.** The heuristic regex detector is too crude to reliably classify 54 techniques from short text. Technique binary detection *reduces* AUC by 0.2-0.6pp. The technique × personality matrix (21.8pp spread) reflects the model's modulation rules, not independently validated behavioral data.

4. **Interaction instability.** All top 7 cross-layer interactions are domain-unstable — they hold in one corpus but not the other. The +1.9pp interaction stacking lift is likely optimistic.

5. **UNCALIBRATED majority in key modules.** 37.4% of parameters (113/302) are theory-derived guesses. All crisis PR, campaign moral reframing, and stakeholder-type weights have no empirical grounding.

6. **Overfit risk.** 297 tests may encode specific weight values rather than structural truths. The test suite validates the architecture's internal consistency, not its external predictive validity.

## Project Structure

```
core/                          # Pipeline modules
  circuit_predictor.py         # 32 weights, 3 circuits, 3 time horizons
  appraisal_extractor.py       # 7-dim extraction (heuristic/ollama/claude)
  technique_detector.py        # 54-technique Zeng + practitioner taxonomy
  technique_to_circuit.py      # Technique → appraisal shift + circuit modifier maps
  recipient_profile.py         # 16-dimension RecipientProfile dataclass
  recipient_modulator.py       # Trait-specific circuit weight modulations
  preset_personas.py           # 10 archetypes (5 ecommerce + 5 politics)
  domain_registry.py           # Domain-specific weight registries
  domain_predictor.py          # Domain-aware prediction wrapper
  linguistic_surface.py        # 12 zero-cost text features
  influence_detector.py        # Influence operation detection
  stealth_optimizer.py         # Maximize persuasion while passing organic detection
  optimization_engine.py       # Iterative persuasive content generation
  sequence_analyzer.py         # Multi-step flow trajectory analysis

calibration/                   # Multi-corpus weight fitting
  download_datasets.py         # Parse DailyPersuasion + HCP into unified JSONL
  fit_domain_weights.py        # Logistic regression per domain with bootstrap CIs
  discover_interactions.py     # 844 cross-layer interaction pairs tested
  compare_domains.py           # Weight stability: universal vs domain-specific

validation/                    # Audit and validation
  full_audit.py                # Layer ablation × corpus with 5-fold CV
  weight_registry_audit.py     # 302-parameter inventory with provenance
  ablation_report.py           # Dead feature identification
  run_pfg_calibration.py       # Persuasion for Good baseline calibration

research/                      # Analysis scripts
  technique_x_personality.py   # 400-cell technique × persona matrix
  technique_x_mft.py           # 480-cell technique × MFT matrix
  interaction_analysis.py      # Interaction shape classification
  campaign_scenario_test.py    # 4 real-world scenario simulations

results/                       # Generated reports
  multi_domain_calibration.md  # Session 4 calibration report
  interaction_paper.md         # Paper draft with 8 findings
  weight_registry.csv          # Full parameter inventory
  weight_audit_summary.md      # Audit summary
  ablation_report.md           # Dead feature report
  full_audit_results.json      # Layer ablation AUC tables

tests/                         # 297 passing tests
  test_pipeline.py             # Core pipeline (70)
  test_recipient.py            # Recipient system (71)
  test_domain.py               # Domain registries (87)
  test_calibration.py          # Calibration pipeline (41)
  test_research.py             # Research analyses (28)

api/server.py                  # FastAPI server (15 endpoints)
```

## Discussion

The central empirical finding across Sessions 4-6 is that **linguistic surface features dominate** the predictive signal. Twelve dictionary-based features extracted in under 1ms contribute more AUC lift (+8-9pp) than the entire 54-technique detection layer, which actually hurts prediction when added. This implies that *how something is written* — reading difficulty, emotionality density, self-reference patterns — carries more predictive signal than *which persuasion techniques are deployed*. The practical implication: invest in linguistic analysis, not technique classification.

The technique × personality interaction matrix (400 cells) demonstrates that while technique *presence* is uninformative, technique × *context* interactions produce meaningful variation. The 21.8pp compliance spread for emotional_appeal_positive across personas shows that the same technique can be highly effective or completely neutral depending on who receives it. This validates the core architectural decision: multi-layer interaction modeling adds value that no single layer provides alone.

The domain transfer penalty (10-13pp) confirms that persuasion mechanics are not universal. A model fitted on charity persuasion dialogues fails to predict hotel booking decisions. Domain-specific weight registries are not an optional enhancement — they are a structural requirement for any computational persuasion system that operates across contexts.

## What Would Make This Better

1. **Claude API extraction at scale** — expected AUC jump to 0.70+ and moral reframing symmetry
2. **Real A/B test data** — conversion rates from actual product CTAs, email subject lines
3. **Biosignal alignment** — fMRI/GSR correlation with circuit predictions
4. **Cross-cultural MFT calibration** — non-WEIRD populations
5. **Technique confidence scores** — replace binary with continuous technique deployment quality

## References

1. Bechara, A., Damasio, H., Tranel, D., & Damasio, A. R. (1997). Deciding advantageously before knowing the advantageous strategy. *Science*, 275(5304), 1293-1295.
2. Berns, G. S., & Moore, S. E. (2012). A neural predictor of cultural popularity. *Journal of Consumer Psychology*, 22(1), 154-160.
3. Brady, W. J., et al. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS*, 114(28), 7313-7318.
4. Cialdini, R. B. (2001). *Influence: Science and Practice* (4th ed.). Allyn & Bacon.
5. Cialdini, R. B. (2016). *Pre-Suasion*. Simon & Schuster.
6. Craig, A. D. (2009). How do you feel — now? *Nature Reviews Neuroscience*, 10(1), 59-70.
7. Damasio, A. R. (1994). *Descartes' Error*. Putnam.
8. Deng, Y., et al. (2023). Transsuasion: Automatic paraphrase for persuasion. arXiv:2302.00994.
9. Falk, E. B., et al. (2012). From neural responses to population behavior. *Psychological Science*, 23(5), 439-445.
10. Feinberg, M., & Willer, R. (2015). From gulf to bridge: When do moral arguments facilitate political influence? *PSPB*, 41(12), 1665-1681.
11. Graham, J., Haidt, J., & Nosek, B. A. (2009). Liberals and conservatives rely on different sets of moral foundations. *JPSP*, 96(5), 1029-1046.
12. Knutson, B., et al. (2007). Neural predictors of purchases. *Neuron*, 53(1), 147-156.
13. Li, Y., et al. (2024). PersuGPT: DailyPersuasion dataset and benchmark. GitHub/PersuGPT.
14. Matz, S. C., et al. (2024). The potential of generative AI for personalized persuasion at scale. *Scientific Reports*, 14, 4692.
15. Petty, R. E., & Cacioppo, J. T. (1986). The Elaboration Likelihood Model of persuasion. *Advances in Experimental Social Psychology*, 19, 123-205.
16. Scherer, K. R. (2001). Appraisal considered as a process of multilevel sequential checking.
17. Shapira, E., et al. (2025). Human choice prediction in language-based persuasion games. GitHub/HumanChoicePrediction.
18. Smith, C. A., & Ellsworth, P. C. (1985). Patterns of cognitive appraisal in emotion. *JPSP*, 48(4), 813-838.
19. Wang, X., et al. (2019). Persuasion for good. *ACL*.
20. Zeng, G., et al. (2024). A taxonomy of persuasion techniques. *ACL*.
