# Persuasion-Max v2 — Claude Code Session Playbook
## Copy each prompt into Claude Code sequentially. Each is one session.

---

## SESSION 1: TECHNIQUE DETECTOR (40 Zeng Taxonomy Techniques)

```
Read my entire codebase, especially core/appraisal_extractor.py and the research/ directory. I need a TechniqueDetector that classifies ANY text stimulus against the full 40-technique Zeng et al. (ACL 2024) persuasion taxonomy. Build:

1. `core/technique_detector.py` — TechniqueDetector class with:
   - A `detect(stimulus: str) -> TechniqueResult` method
   - Returns a 40-element dict mapping technique_name -> {detected: bool, confidence: float, span: str|None, ethical: bool}
   - Three detection modes, matching the AppraisalExtractor pattern:
     a) `heuristic` — keyword/regex patterns for high-confidence techniques (loaded_language, repetition, rhetorical_question, scarcity_appeal, etc.)
     b) `ollama` — zero-shot classification using local LLM with technique definitions in system prompt
     c) `claude` — Claude API call with structured output
   - The system prompt must include the FULL definition of each technique, not just the name. Use these 13 umbrella strategies with 40 fine-grained techniques:

   ETHICAL (20):
   - logical_appeal, evidence_based, expert_testimony, non_expert_testimonial
   - social_proof, authority_endorsement, bandwagon
   - emotional_appeal_positive, emotional_appeal_negative, empathy_appeal, storytelling
   - self_disclosure, shared_values, commitment_consistency
   - incentive_appeal, gain_frame, loss_frame
   - scarcity_appeal, urgency_appeal, competition_framing
   - reciprocity, foot_in_the_door, door_in_the_face
   - anchoring, contrast_principle, future_pacing, perspective_shifting
   - rhetorical_question, leading_question, socratic_questioning

   UNETHICAL (20):
   - deceptive_information, emotional_manipulation, gaslighting, false_equivalence
   - guilt_tripping, fear_mongering, false_urgency, false_scarcity
   - ad_hominem, name_calling, straw_man, whataboutism
   - false_dilemma, slippery_slope, red_herring, appeal_to_ignorance
   - flattery (manipulative), appeal_to_pity (manipulative), obfuscation, bandwagon_pressure

   Each technique definition should be 1-2 sentences, grounded in the Zeng et al. paper definitions.

2. `core/technique_to_circuit.py` — TechniqueCircuitMapper class that maps detected techniques to circuit weight modifiers:
   - Each technique modifies specific appraisal dimensions and circuit activations
   - Example mappings:
     social_proof → certainty += 0.15, deliberation *= 0.8
     scarcity_appeal → temporal_proximity += 0.25, avoidance *= 1.1
     loss_frame → valence -= 0.2, avoidance += 0.15, approach += 0.1 (loss aversion)
     fear_mongering → avoidance *= 1.4, insula_activation += 0.25
     logical_appeal → deliberation += 0.15, certainty += 0.1
     storytelling → emotionality_weight *= 1.3, deliberation *= 0.7
     false_urgency → temporal_proximity += 0.3, insula_activation += 0.2 (manipulation detection)
   - Map ALL 40 techniques to specific modifiers. Mark each as CONSTRAINED (from literature) or UNCALIBRATED.

3. Integration with existing CircuitPredictor:
   - Modify predict() to accept optional technique_result parameter
   - When provided, apply technique modifiers AFTER appraisal extraction, BEFORE circuit computation
   - This makes the pipeline: extract_appraisals → detect_techniques → apply_technique_modifiers → compute_circuits → predict_behavior

4. Tests in tests/test_techniques.py:
   - Test each detection mode on 10 known stimuli with labeled techniques
   - Test technique-to-circuit mapping produces expected modifier directions
   - Test that technique-aware prediction differs from technique-naive prediction
   - Test edge cases: stimulus with zero techniques, stimulus with 5+ simultaneous techniques

5. Add a `--techniques` flag to the API endpoints so users can opt into technique detection.

Run all tests. Commit with message: "Add 40-technique detector (Zeng taxonomy) + circuit integration"
```

---

## SESSION 2: RECIPIENT PROFILE MODEL (Full Stack)

```
Read my entire codebase, especially core/circuit_predictor.py and core/technique_detector.py. I need a RecipientProfile system that models WHO is being persuaded, not just WHAT the stimulus contains. Build:

1. `core/recipient_profile.py` — RecipientProfile dataclass with 16 dimensions:

   # Big Five Personality (5 continuous)
   openness: float           # 0.0-1.0
   conscientiousness: float  # 0.0-1.0
   extraversion: float       # 0.0-1.0
   agreeableness: float      # 0.0-1.0
   neuroticism: float        # 0.0-1.0

   # Moral Foundations Theory (6 continuous, Haidt & Graham)
   care_harm: float              # 0.0-1.0
   fairness_cheating: float      # 0.0-1.0
   loyalty_betrayal: float       # 0.0-1.0
   authority_subversion: float   # 0.0-1.0
   sanctity_degradation: float   # 0.0-1.0
   liberty_oppression: float     # 0.0-1.0

   # Political Orientation (2 axes)
   economic_ideology: float      # -1.0 (left) to 1.0 (right)
   social_ideology: float        # -1.0 (libertarian) to 1.0 (authoritarian)

   # Situational (3)
   prior_belief: float           # 0.0-1.0 (pre-existing stance on THIS topic)
   involvement: float            # 0.0-1.0 (how much they care about THIS topic)
   elaboration_likelihood: float # 0.0-1.0 (central vs peripheral processing)

2. `core/recipient_modulator.py` — RecipientModulator class:
   - Takes a RecipientProfile + raw circuit scores
   - Applies trait-specific weight modulations
   - Key modulations (document each with literature citation or mark UNCALIBRATED):

   # Big Five modulations
   high_neuroticism (>0.7):
     amygdala_weight *= 1.3        # heightened threat sensitivity (Eysenck 1967)
     loss_frame_amplifier = 1.4    # stronger loss aversion
     approach_baseline -= 0.1      # lower baseline approach
   high_agreeableness (>0.7):
     compliance_baseline += 0.15   # higher default compliance (Graziano 1996)
     retaliation_probability *= 0.6
     reciprocity_sensitivity *= 1.3
   high_openness (>0.7):
     novelty_weight *= 1.4         # novelty = exciting not threatening
     certainty_weight *= 0.7       # comfortable with ambiguity
   low_conscientiousness (<0.3):
     deliberation_weight *= 0.7    # less systematic processing
     impulse_propensity += 0.2
   high_extraversion (>0.7):
     social_proof_weight *= 1.3    # more susceptible to social influence
     bandwagon_sensitivity *= 1.4

   # Moral Foundations modulations
   high_care_harm (>0.7):
     emotional_narrative_amplifier = 1.4  # empathy-driven approach
   high_loyalty_betrayal (>0.7):
     ingroup_signal_amplifier = 1.5       # tribal appeals hit harder
     authority_appeal_amplifier = 1.2
   high_authority_subversion (>0.7):
     authority_citation_weight *= 1.3     # expert testimony more persuasive
     deliberation_suppression = 0.15      # authority = don't question
   high_sanctity_degradation (>0.7):
     disgust_sensitivity *= 1.4           # lower threshold for insula activation
   high_liberty_oppression (>0.7):
     agency_sensitivity *= 1.5            # reactance to coercion amplified
     false_urgency_retaliation *= 1.8

   # Political modulations
   conservative_profile (economic > 0.3 AND social > 0.3):
     loyalty_betrayal_weight *= 1.2       # Graham et al. 2009
     authority_weight *= 1.2
     sanctity_weight *= 1.2
   liberal_profile (economic < -0.3 AND social < -0.3):
     care_harm_weight *= 1.3
     fairness_weight *= 1.3
     liberty_weight *= 1.2

   # Elaboration Likelihood modulation
   high_EL (>0.7):
     logical_appeal_weight *= 1.4         # central route processing
     emotional_appeal_weight *= 0.7       # peripheral cues discounted
     weak_argument_penalty = -0.3         # flawed logic caught and punished
   low_EL (<0.3):
     social_proof_weight *= 1.4           # peripheral cues dominate
     authority_weight *= 1.3
     emotional_appeal_weight *= 1.2
     logical_appeal_weight *= 0.6         # complex arguments skipped

3. `core/preset_personas.py` — 10 preset recipient archetypes:

   E-COMMERCE PERSONAS:
   - impulse_buyer: high extraversion, low conscientiousness, low EL, high neuroticism
   - price_hunter: high conscientiousness, high EL, low agreeableness, prevention focus
   - brand_loyalist: high loyalty_betrayal, high conscientiousness, high prior_belief
   - social_shopper: high extraversion, high care_harm, high social_proof_sensitivity
   - skeptical_researcher: high openness, high EL, low agreeableness, high agency_sensitivity

   POLITICS/PR PERSONAS:
   - liberal_base: high care/fairness, low loyalty/authority/sanctity, economic < -0.5
   - conservative_base: balanced MFT, high loyalty/authority/sanctity, economic > 0.5
   - persuadable_moderate: moderate everything, high involvement, medium EL
   - disengaged_voter: low involvement, low EL, low prior_belief, peripheral processing
   - issue_activist: very high involvement, very high moral_conviction, high EL, high prior_belief

4. `core/text_profiler.py` — TextProfiler class for inferring recipient traits from text:
   - Takes a list of text samples (tweets, comments, posts) from a person
   - Uses LIWC-equivalent features from linguistic_surface.py to estimate:
     * Pronoun ratios → extraversion proxy (high I-words = introversion, high we-words = agreeableness)
     * Emotional word density → neuroticism proxy
     * Analytical thinking score → conscientiousness/openness proxy
     * Certainty markers → openness proxy (high certainty = low openness)
   - Uses zero-shot LLM classification for:
     * Moral foundations profile (prompt with MFT definitions + example text)
     * Political orientation estimate
   - Returns a RecipientProfile with confidence scores for each dimension
   - Mark EVERY inference as ESTIMATED with a confidence bound

5. Integration with CircuitPredictor:
   - predict() now accepts optional recipient: RecipientProfile parameter
   - Full pipeline: stimulus → extract_appraisals → detect_techniques → apply_technique_modifiers → apply_recipient_modulation → compute_circuits → predict_behavior
   - The SAME stimulus scored against 5 different preset personas must produce 5 DIFFERENT behavioral predictions

6. Tests:
   - Same stimulus ("50% off today only!") scored against impulse_buyer vs skeptical_researcher must differ by >15pp in compliance
   - Same political message scored against liberal_base vs conservative_base must show opposite technique effectiveness patterns
   - TextProfiler tested on 5 sample tweet sets with known political orientation
   - All preset personas produce valid circuit scores (no NaN, no >1.0)

Run all tests. Commit: "Add 16-dim recipient model + 10 preset personas + text profiler"
```

---

## SESSION 3: DOMAIN-SPECIFIC WEIGHT REGISTRIES (E-Commerce + Politics/PR)

```
Read my entire codebase and the research/persuasion-max-v2-full-stack-spec.md. I need domain-specific weight registries — separate fitted parameters for e-commerce and politics/PR. Build:

1. `core/domain_registry.py` — DomainWeightRegistry class:
   - Stores separate weight sets for each domain
   - Each weight has: value, provenance (FITTED/CONSTRAINED/UNCALIBRATED), citation, confidence_interval, domain
   - Factory methods: DomainWeightRegistry.ecommerce() and DomainWeightRegistry.politics()
   - Methods: get_weight(name, domain), list_fitted_weights(domain), list_uncalibrated_weights(domain)

2. E-Commerce weight registry — fitted to purchase/conversion behavior:
   - Key differences from universal weights:
     * scarcity techniques have 2x the circuit modifier weight (drives purchase urgency)
     * loss_frame is the dominant persuasion technique (loss aversion in spending context)
     * social_proof × high_extraversion interaction is amplified (social shopping)
     * price_anchoring maps directly to anchoring technique with higher weight
     * reciprocity (free trials, samples) has strongest approach_circuit activation
   - Document which weights come from Knutson et al. 2007 (NAc/insula predict purchase)
   - Add e-commerce-specific behavioral outcomes:
     purchase_probability, cart_add_probability, return_probability

3. Politics/PR weight registry — fitted to belief change and message amplification:
   - Key differences:
     * moral_reframing is the highest-weight technique (Feinberg & Willer 2015)
       — framing a liberal policy using conservative MFT values (and vice versa) increases support
     * authority_citation weight depends heavily on recipient's authority_subversion MF score
     * in-group signaling (loyalty_betrayal × flag_waving) dominates in partisan messaging
     * fear_appeal has diminishing returns (habituation) — model this as decaying weight over exposure count
     * emotional_narrative is strongest for campaign messaging
     * logical_appeal + evidence_based is strongest for crisis PR (credibility recovery)
   - Two sub-registries:
     a) campaign_messaging: optimizes for belief_shift, vote_intention_shift, share_probability
     b) crisis_pr: optimizes for trust_recovery, counter_narrative_suppression, brand_sentiment_shift
   - Add politics-specific behavioral outcomes:
     belief_change, share_amplify_probability, counter_argue_probability, trust_shift

4. `core/domain_predictor.py` — DomainPredictor class:
   - Wraps CircuitPredictor with domain-specific weight loading
   - predict(stimulus, domain="ecommerce"|"politics_campaign"|"politics_crisis", recipient=None)
   - Returns domain-specific outcome metrics alongside standard circuit scores

5. Crisis PR specific logic:
   - crisis_severity: float (0.0-1.0) — how bad is the situation
   - response_timing: float (0.0-1.0) — how quickly is the response issued
   - stakeholder_type: enum — media, regulators, customers, employees, investors
   - Different stakeholder types activate different recipient profiles automatically:
     * media → high EL, high openness, high agency_sensitivity (they will fact-check)
     * regulators → high authority_subversion, high EL, high conscientiousness
     * customers → mixed EL, high involvement if directly affected
     * investors → high conscientiousness, economic focus, high analytical processing
   - Crisis response technique effectiveness differs from normal politics:
     * transparency (self_disclosure + evidence_based) has 2x weight in crisis
     * defensive techniques (whataboutism, straw_man) have negative effectiveness (amplify retaliation)
     * empathy_appeal works for customers but backfires with regulators (seen as deflection)

6. Tests:
   - Same product description scored in ecommerce vs politics domain must produce different weights
   - Crisis PR response scored against media vs customers recipient profiles must differ
   - Campaign message with loyalty appeal scored against liberal vs conservative must show opposite effectiveness
   - All weights documented with provenance labels

Commit: "Add domain-specific weight registries (ecommerce + politics/PR)"
```

---

## SESSION 4: MULTI-CORPUS CALIBRATION

```
Read my entire codebase, especially validation/run_pfg_calibration.py and core/domain_registry.py. Currently ALL weights are fitted on Persuasion for Good (charity domain, 1017 dialogues). I need multi-domain calibration. Build:

1. `calibration/download_datasets.py` — Dataset downloader:
   - DailyPersuasion: clone from https://github.com/PersuGPT/PersuGPT.github.io, parse the English dataset
     * Split into commercial subset (~50%) and subjective/opinion subset (~50%)
     * Extract per-turn: utterance text, annotated strategy, persuasion outcome
   - HumanChoicePrediction: clone from https://github.com/eilamshapira/HumanChoicePrediction
     * Extract: expert message text, human binary decision (accept/reject), game context
   - Paired Persuasion: clone from https://github.com/marcoguerini/paired_datasets_for_persuasion
     * Extract: persuasive sentence, non-persuasive counterpart (controlled pairs)
   - PERSUADE 2.0: clone from https://github.com/scrosseye/persuade_corpus_2.0
     * Extract: written arguments with quality scores
   - Output all as unified JSON format: {text: str, outcome: float, domain: str, source: str}

2. `calibration/fit_domain_weights.py` — Multi-domain weight fitter:
   - For each domain (ecommerce, politics_campaign, politics_crisis):
     a) Run AppraisalExtractor (heuristic mode for speed) on all stimuli
     b) Run TechniqueDetector (heuristic mode) on all stimuli
     c) Fit logistic regression: features → outcome
     d) Extract fitted weights with confidence intervals
     e) Compare fitted weights vs hand-tuned weights
   - Cross-domain transfer test:
     * Train on PFG (charity), test on DailyPersuasion commercial subset
     * Train on DailyPersuasion commercial, test on DailyPersuasion subjective
     * Report AUC for each transfer direction
   - Output: fitted_weights_{domain}.json with full provenance

3. `calibration/discover_interactions.py` — Cross-layer interaction discovery:
   - THIS IS THE PUBLISHABLE FINDING. Systematically test ALL pairwise interactions:
     * Appraisal × Appraisal (already found: valence × goal_relevance = 0.147)
     * Technique × Appraisal (does social_proof × certainty interact?)
     * Technique × Recipient trait (does scarcity × neuroticism interact?)
     * MFT × Technique (does loyalty_betrayal × flag_waving interact?)
   - Method: add interaction terms to logistic regression one at a time
   - Rank all interactions by incremental AUC lift
   - Report top 20 interaction terms with fitted coefficients and CIs
   - Test: do interactions outperform linear-only model? (Hypothesis: yes, based on PFG finding)

4. `calibration/compare_domains.py` — Domain comparison report:
   - For each weight: is it stable across domains or domain-specific?
   - Generate a weight stability matrix: weight × domain → value
   - Identify universal weights (stable across domains) vs domain-specific weights
   - This determines whether you need N separate registries or can share a core

5. Update DomainWeightRegistry with fitted values:
   - Replace UNCALIBRATED weights with FITTED where data supports it
   - Keep UNCALIBRATED label for weights not covered by available data
   - Document sample size and corpus for each FITTED weight

6. `results/multi_domain_calibration.md` — Auto-generated report:
   - AUC table: {corpus × domain × feature_set}
   - Weight comparison table across domains
   - Top 20 interactions ranked by lift
   - Transfer learning results
   - Honest limitations section

Run all tests. Run calibration. Generate report.
Commit: "Multi-domain calibration: DailyPersuasion + HumanChoicePrediction + interaction discovery"
```

---

## SESSION 5: CROSS-LAYER INTERACTION DEEP DIVE (The Paper)

```
Read my entire codebase, especially calibration/discover_interactions.py results and core/recipient_modulator.py. The interaction term discovery from Session 4 revealed the top cross-layer interactions. Now I need to go deeper. Build:

1. `research/interaction_analysis.py` — Deep interaction analyzer:
   - For each top-20 interaction from Session 4:
     a) Compute the interaction surface (heat map of outcome as function of both variables)
     b) Test whether the interaction is LINEAR (A × B), THRESHOLD (only matters when A > 0.5), or INVERTED-U (peaks at moderate values)
     c) Test 3-way interactions for the strongest 2-way pairs (A × B × C)
     d) Split analysis by domain: does the interaction hold in ecommerce AND politics?

2. `research/technique_x_personality.py` — The novel contribution matrix:
   - For EACH of the 40 techniques × EACH of the Big Five traits:
     * Compute: how does the technique's effectiveness change as the trait increases?
     * Output: 40×5 = 200 interaction coefficients
   - For EACH technique × EACH moral foundation:
     * Same analysis: 40×6 = 240 interaction coefficients
   - Rank all 440 interactions by absolute magnitude
   - Identify the "killer combinations":
     * Which technique works ONLY on certain personality types?
     * Which technique BACKFIRES on certain personality types?
     * These are the findings nobody has published

3. `research/moral_reframing_analysis.py` — Test Feinberg & Willer (2015):
   - Take the same policy message and score it against recipients with different MFT profiles
   - Show that reframing a liberal policy using conservative moral foundations
     (loyalty, authority, sanctity) increases predicted compliance for conservative recipients
   - Show the reverse: conservative policy + care/fairness framing for liberal recipients
   - Quantify the reframing lift in predicted compliance percentage points
   - This is directly applicable to campaign messaging and crisis PR

4. `research/campaign_scenario_test.py` — Real-world scenario simulations:
   - Scenario 1: Product launch email — score against 5 ecommerce personas
   - Scenario 2: Political campaign ad — score against 5 political personas
   - Scenario 3: Crisis PR statement (data breach) — score against media, regulators, customers, investors
   - For each scenario: show which techniques + recipient combinations produce the highest/lowest compliance
   - Generate actionable recommendations: "For [persona], lead with [technique], avoid [technique]"

5. `results/interaction_paper.md` — Paper-shaped findings document:
   - Title: "Cross-Layer Interaction Effects in Computational Persuasion:
     Technique × Personality × Moral Foundations Interaction Matrices"
   - Abstract: 150 words summarizing the novel finding
   - Method: multi-layer architecture, calibration corpora, interaction fitting
   - Results: top interactions, domain specificity, moral reframing quantification
   - Tables: technique × personality matrix, technique × MFT matrix
   - Figures: interaction heatmaps, domain comparison plots
   - Discussion: what this means for personalized persuasion, limitations

Commit: "Cross-layer interaction analysis: technique × personality × MFT matrices"
```

---

## SESSION 6: HONEST VALIDATION & WEIGHT REGISTRY AUDIT

```
Read my entire codebase. This is the final integrity check. Build:

1. `validation/full_audit.py` — Comprehensive validation suite:
   - Run the ENTIRE pipeline (all 5 layers) on EVERY available corpus
   - Report AUC for each configuration:
     * Appraisal only (7 features)
     * Appraisal + Linguistic (19 features)
     * Appraisal + Linguistic + Techniques (19 + 40 features)
     * Full stack including recipient modeling (against preset personas)
   - Cross-validation: 5-fold on each corpus
   - Calibration curves: predicted probability vs observed frequency (are we well-calibrated or overconfident?)
   - Report: which LAYER adds the most predictive lift?
   - Report: which DOMAIN has the best calibration?
   - Report: which interactions survive cross-validation?

2. `validation/weight_registry_audit.py` — Every weight accounted for:
   - Generate a CSV of EVERY parameter in the system:
     * weight_name, value, provenance (FITTED/CONSTRAINED/UNCALIBRATED), source_citation,
       sample_size, confidence_interval, domain, layer, last_calibration_date
   - Count: how many FITTED vs CONSTRAINED vs UNCALIBRATED?
   - For each UNCALIBRATED weight: propose the specific calibration experiment
     (what dataset, what sample size, what test) that would convert it to FITTED
   - Flag any weight that was FITTED on <100 samples (unreliable)
   - Flag any weight where the CI crosses zero (not significantly different from zero)

3. `validation/ablation_report.py` — What matters, what doesn't:
   - Remove each layer one at a time, measure AUC drop
   - Remove each recipient trait one at a time, measure prediction change
   - Remove each technique category one at a time, measure prediction change
   - Rank every component by marginal contribution
   - Identify dead weight: features that add zero predictive value (drop them)

4. Update README.md — Paper-shaped academic document:
   - Title, Abstract, Introduction (the gap between neuroscience and computation)
   - Related Work (PersuGPT, Artificial Societies, Transsuasion, TRIBE v2, MoralBERT)
   - Method (5-layer architecture with formulas)
   - Experiments (multi-domain calibration, interaction discovery, ablation)
   - Results (AUC tables, interaction matrices, domain comparison)
   - Discussion (honest limitations, what's calibrated vs speculative)
   - Future Work (real A/B test validation, biosignal integration, cross-cultural)
   - References (30+ papers)

5. Update the landing page and brain visualization with actual v2 numbers.

6. Final test run: all tests must pass, all validation scripts must complete.

Commit: "v2 final: full audit, weight registry, ablation, paper-shaped README"
```

---

## EXECUTION NOTES

### Dependencies to install before Session 1:
```bash
pip install empath textstat transformers torch --break-system-packages
```

### Dataset downloads needed before Session 4:
```bash
git clone https://github.com/PersuGPT/PersuGPT.github.io.git data/persuGPT
git clone https://github.com/eilamshapira/HumanChoicePrediction.git data/hcp
git clone https://github.com/marcoguerini/paired_datasets_for_persuasion.git data/paired
git clone https://github.com/scrosseye/persuade_corpus_2.0.git data/persuade2
```

### Expected results progression:
```
After Session 1:  70+ techniques detectable, pipeline integrated
After Session 2:  Same stimulus → 5 different predictions for 5 personas
After Session 3:  Separate ecommerce vs politics weight registries
After Session 4:  AUC improvement from multi-domain calibration + interaction discovery
After Session 5:  440 technique × personality interaction coefficients (the paper)
After Session 6:  Full audit, every weight documented, ablation complete
```

### The money metric:
If after Session 6 the ablation shows that technique × personality interactions
add >5pp AUC lift over the technique-only and personality-only models independently,
that's a publishable finding. Nobody has measured this.
