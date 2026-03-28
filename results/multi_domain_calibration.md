# Multi-Domain Calibration Report

**Date:** 2026-03-28
**Pipeline:** calibration/download_datasets.py → fit_domain_weights.py → discover_interactions.py → compare_domains.py

## Table 1: Dataset Summary

| Source | N | Domain | Outcome Type | Notes |
|--------|---|--------|-------------|-------|
| DailyPersuasion (PersuGPT) | 77,999 | 53,525 opinion_change + 24,474 commercial | Binary (accepted/rejected from persuadee response) | 13,000 scenarios × 6 sessions, 34 domain labels |
| HumanChoicePrediction | 48,289 | commercial | Binary (didGo: player chose to book hotel based on review) | Real human binary decisions, strongest ground truth |
| Paired Persuasion | 0 | — | — | Data in GitHub releases, not in repo. Skipped. |
| PERSUADE 2.0 | 0 | — | — | Data on Google Drive, not in repo. Skipped. |
| **Total** | **126,288** | **72,763 commercial / 53,525 opinion_change** | | |

## Table 2: AUC by Feature Set x Corpus

| Feature Set | DailyPersuasion | HCP |
|-------------|----------------|-----|
| Appraisal only (7 dims) | 0.563 | 0.550 |
| Appraisal + Technique (47 dims) | 0.584 | 0.549 |
| Appraisal + Linguistic (19 dims) | 0.667 | 0.634 |
| All 59 features | 0.667 | 0.634 |

**Key finding:** Linguistic surface features provide +10pp AUC lift over appraisal alone. Technique binary features add no incremental lift on top of linguistic features — the linguistic layer already captures the signal that technique detection provides.

## Table 3: Cross-Domain Transfer Matrix (Train x Test → AUC)

| Train \ Test | DailyPersuasion | HCP |
|-------------|----------------|-----|
| DailyPersuasion | **0.682** | 0.547 |
| HCP | 0.521 | **0.648** |

**Key finding:** Cross-domain transfer drops AUC by 10-13pp (0.682→0.547, 0.648→0.521). Weights fitted on persuasion dialogues do NOT predict hotel booking decisions, confirming the need for domain-specific registries built in Session 3.

## Table 4: Top 7 Cross-Layer Interactions (ranked by AUC lift)

| # | Feature A | Feature B | Layer A | Layer B | AUC Lift | AUC w/ Interaction |
|---|-----------|-----------|---------|---------|----------|-------------------|
| 1 | valence | reading_difficulty | appraisal | linguistic | +0.0077 | 0.644 |
| 2 | word_count | evidence_based | linguistic | technique | +0.0053 | 0.641 |
| 3 | goal_relevance | self_reference | appraisal | linguistic | +0.0048 | 0.641 |
| 4 | reading_difficulty | bandwagon | linguistic | technique | +0.0039 | 0.640 |
| 5 | reading_difficulty | gain_frame | linguistic | technique | +0.0038 | 0.640 |
| 6 | reading_difficulty | social_proof | linguistic | technique | +0.0036 | 0.640 |
| 7 | word_count | scarcity_appeal | linguistic | technique | +0.0030 | 0.639 |

**Interaction stacking results:**

| Top N Interactions | AUC | Lift over Linear |
|-------------------|-----|-----------------|
| Linear only | 0.636 | — |
| +5 interactions | 0.655 | +0.019 |
| +10 interactions | 0.658 | +0.022 |

**Key finding:** Stacking top 5 interactions adds +1.9pp AUC over linear-only model. Top interaction is **valence × reading_difficulty** (cross-layer: appraisal × linguistic) — positive valence matters more in simple text. The PFG-discovered valence × goal_relevance interaction did not replicate as a top interaction in this larger multi-corpus analysis, suggesting it may be charity-domain-specific.

## Table 5: Weight Stability Matrix

| Classification | Count | % | Interpretation |
|---------------|-------|---|----------------|
| UNIVERSAL | 13 | 22% | Consistent sign and magnitude across corpora — shared core weights |
| DOMAIN-SPECIFIC | 33 | 56% | Sign flips or magnitude varies >3x — separate domain registries needed |
| INSIGNIFICANT | 13 | 22% | Near-zero weight in all corpora — candidates for ablation |

**Top universal features (consistent across corpora):**

| Feature | Mean Weight | CV | Layer |
|---------|------------|-----|-------|
| self_reference | +0.234 | 0.18 | linguistic |
| tone_positive | +0.132 | 0.20 | linguistic |
| temporal_proximity | -0.085 | 0.25 | appraisal |
| goal_relevance | -0.062 | 0.41 | appraisal |
| analytical_thinking | -0.051 | 0.19 | linguistic |

**Notable domain-specific features (validates Session 3 registries):**

| Feature | Classification | Evidence |
|---------|---------------|----------|
| valence | DOMAIN-SPECIFIC | Weight varies >3x across corpora |
| certainty | DOMAIN-SPECIFIC | Weight varies >3x across corpora |
| social_proof | DOMAIN-SPECIFIC | Sign flips between commercial and opinion-change |
| scarcity_appeal | DOMAIN-SPECIFIC | Weight varies >3x across corpora |
| emotional_appeal_positive | DOMAIN-SPECIFIC | Weight varies >3x across corpora |
| authority_endorsement | DOMAIN-SPECIFIC | Weight varies >3x across corpora |

This validates the Session 3 domain registry design: scarcity, social proof, emotional appeal, and authority all behave differently across commercial vs opinion-change contexts.

## Domain Split: Interaction Transfer

| Domain | Base AUC | Top interactions that transfer |
|--------|----------|------------------------------|
| commercial (N=4,588) | 0.612 | 4/7 (valence×reading_difficulty, word_count×evidence, reading_difficulty×bandwagon, reading_difficulty×gain_frame) |
| opinion_change (N=3,412) | 0.673 | 1/7 (only goal_relevance×self_reference) |

**Key finding:** Most top interactions are commercial-specific. The opinion-change domain relies on different interaction patterns — further evidence for domain-specific weight registries.

## Honest Limitations

1. **Two of four datasets unavailable:** Paired Persuasion (data in GitHub releases, not repo) and PERSUADE 2.0 (data on Google Drive) could not be parsed. This limits the transfer matrix to 2×2 instead of the planned 4×4.

2. **DailyPersuasion is synthetic:** The 13,000 persuasion scenarios are GPT-generated dialogues, not real human conversations. The outcome labels (accepted/rejected) are inferred from the generated persuadee response, not from actual behavioral change. This inflates the positive rate (64.6%) and may not reflect real-world persuasion dynamics.

3. **HCP outcomes are confounded:** The didGo decision depends on game context (hotel score, round number, strategy) not just the review text. The review text is only one input to the player's decision. This introduces noise that depresses AUC for text-only predictors.

4. **Heuristic extraction bottleneck:** All fitting uses heuristic mode (regex keyword matching). The Claude/Ollama extractors would likely improve AUC substantially, but have not been tested at scale due to cost and latency.

5. **Sample size concerns for rare techniques:** Many of the 40 technique detectors fire rarely (e.g., gaslighting, appeal_to_ignorance). Their fitted weights have wide CIs and should not be trusted individually.

6. **Interaction stacking lift is below 3pp target:** The +2.2pp lift from top-10 interactions is meaningful but below the +3pp threshold hypothesized as the "publishable finding." This may improve with LLM extraction or additional corpora.

7. **Weights still lacking empirical grounding:** The following weights from domain_registry.py have no corpus coverage and remain UNCALIBRATED:
   - All crisis_pr weights (no crisis PR corpus available)
   - Campaign-specific moral reframing weights (no political persuasion corpus)
   - Stakeholder-type modulations (no stakeholder-specific outcome data)
   - Response timing modulator (no temporal data in any corpus)
