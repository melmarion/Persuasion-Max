# Persuasion-Max

Persuasion-Max is a behavioral mechanics engine for influence analysis.

The project starts from a harder premise than most persuasion tools: fluent copy is not enough. Messages work or fail because they move through a layered system of appraisal, reward prediction, threat detection, recipient fit, and domain context. Persuasion-Max tries to model that system explicitly instead of treating persuasion as a bag of vibes, frameworks, or prompt tricks.

This repo is not a polished SaaS and not a generic copy generator. It is a research-heavy instrument for asking questions like:

- Why did this message create approach, delay, or backlash?
- Which part of the message is weak: valence, certainty, agency, urgency, fit?
- What changes improve short-term compliance but damage repeat compliance?
- Which persuasion mechanics transfer across domains, and which collapse?
- When is the right answer “insufficient signal” rather than false certainty?

## What It Actually Does

At the center of the repo is a multi-layer pipeline that converts a text stimulus into:

- cognitive appraisal scores
- circuit-level activations for approach / avoidance / deliberation
- predicted behaviors such as compliance / rejection / delay
- durability estimates across immediate, repeat, and retaliation horizons
- operator-readable interpretations of what the pattern likely means

The important part is not just prediction. It is decomposition.

Persuasion-Max is built to make the internal shape of influence legible:

- where the message is pulling
- where it is creating friction
- what it likely means behaviorally
- what that does *not* prove
- which response posture fits the pattern

## Why It’s Interesting

Most persuasion software collapses three different things into one blur:

- wording quality
- recipient psychology
- actual behavioral consequence

Persuasion-Max keeps them separate on purpose.

That separation leads to sharper findings:

- linguistic surface features add real predictive lift
- binary technique detection adds surprisingly little and can even hurt
- domain transfer is expensive
- technique effects are context-sensitive, not universal
- some outputs should be interpreted as diagnostic, not directive

In other words: influence is not just “say the right line.” It is a system with structure, tradeoffs, and failure modes.

## At A Glance

- Core idea: mechanize persuasive effectiveness as a multi-layer behavioral system
- Architecture: 5-layer prediction stack plus limbic-style cascade analysis
- Parameter registry: 302 tracked weights with provenance labels
- Calibration footprint: 126K-sample evaluation across 2 corpora
- Test surface: hundreds of passing tests across pipeline, domain, calibration, and research layers
- Best use: research, operator analysis, experimentation, and internal tooling
- Worst use: pretending this is ground-truth human mind reading

## The Best Entry Points

If you are new to the repo, start here:

- [README.md](/Users/infiniteupside/Persuasion-Max/README.md)
  This file. Project framing and where to look next.
- [analyze.py](/Users/infiniteupside/Persuasion-Max/analyze.py)
  The fastest way to use the system from the terminal.
- [core/limbic_cascade.py](/Users/infiniteupside/Persuasion-Max/core/limbic_cascade.py)
  The cleanest single-entry pipeline for full analysis.
- [core/relational_interpreter.py](/Users/infiniteupside/Persuasion-Max/core/relational_interpreter.py)
  The user-facing interpretation layer: what the signal means, what not to infer, and what response posture fits.
- [results/weight_registry.csv](/Users/infiniteupside/Persuasion-Max/results/weight_registry.csv)
  The actual parameter inventory with provenance.
- [EXECUTIVE_SUMMARY.md](/Users/infiniteupside/Persuasion-Max/EXECUTIVE_SUMMARY.md)
  The shortest high-level narrative for non-technical readers.

## How The System Is Organized

### `core/`
The live machinery.

- `linguistic_surface.py`
  Cheap surface features like concreteness, emotionality, self-reference, and difficulty.
- `appraisal_extractor.py`
  Converts text into appraisal dimensions such as valence, agency, certainty, and coping potential.
- `circuit_predictor.py`
  Maps the appraisal state into approach / avoidance / deliberation dynamics and outcome probabilities.
- `limbic_cascade.py`
  Full orchestrated analysis path with stage traces and operator summaries.
- `relational_interpreter.py`
  Private explanation layer that translates mechanics into plain-English pattern reads.
- `recipient_modulator.py`, `preset_personas.py`, `recipient_profile.py`
  Recipient fit and trait-level modulation.
- `domain_registry.py`, `domain_predictor.py`
  Domain-specific weight systems and wrappers.
- `reframing_engine.py`
  Tradeoff projections and highest-leverage fix suggestions.
- `sequence_analyzer.py`
  Multi-step flow analysis for longer persuasion sequences.

### `calibration/`
Where the weights stop being purely theoretical.

- dataset download and parsing
- domain-specific fitting
- interaction discovery
- universal vs domain stability checks

### `validation/`
Where the repo checks itself instead of trusting its own elegance.

- full audits
- ablation studies
- registry audits
- corpus comparisons

### `results/`
The empirical paper trail.

- weight registry
- calibration reports
- ablation reports
- interaction findings

### `research/`
Exploratory analyses and specific behavioral questions.

This is where the repo feels most like a lab notebook with teeth.

### `tests/`
Pipeline, domain, recipient, calibration, and research tests.

### `api/` and `mcp/`
Interfaces for using the engine outside the bare terminal.

## Running It

```bash
# Single analysis
python analyze.py "Get Notion free"

# Mechanical output if you want the denser readout
python analyze.py "Get Notion free" --surface mechanical

# Compare two messages
python analyze.py compare "Submit" "Get Notion free"

# Browse success/failure patterns
python analyze.py patterns --category error
python analyze.py patterns --weak agency

# API server
pip install fastapi uvicorn
uvicorn api.server:app --port 8100
```

## What The Current CLI Is Good At

The current CLI is strongest when you want a fast operator read:

- what behavior the message is likely pulling toward
- which dimension is weakest
- what the cleanest interpretation is
- what that interpretation does *not* justify claiming
- which response style makes sense

That surface was intentionally tightened so the output feels more like an instrument panel and less like spelunking through raw internals.

## Empirical Spine

These are the most important findings currently documented in the repo:

- Linguistic surface features carry real predictive signal.
- Technique binaries are much weaker than expected and can add noise.
- Cross-domain transfer is costly enough that domain registries matter.
- Recipient interactions matter more than universal persuasion folklore suggests.
- A lot of persuasive prediction work still suffers from proxy-outcome ceilings.

This matters because it keeps the repo honest. Persuasion-Max is not impressive because it has many knobs. It is interesting because some of its own cherished mechanisms survive contact with calibration and some do not.

## What This Is Not

Persuasion-Max is not:

- a magic mind-reading machine
- a proof that a message will convert in the real world
- a substitute for real A/B testing
- a clean behavioral truth engine with no uncertainty
- a universal copywriter that works equally well in every domain

The project is strongest when used as a disciplined analytic system with explicit caveats.

## Honest Limitations

The repo still has real ceilings:

1. Extraction quality still constrains downstream quality.
   Heuristic extraction is useful, but it limits what the richer architecture can express.

2. Proxy outcomes are still proxy outcomes.
   Calibration corpora are valuable, but they are not the same thing as direct measured field behavior.

3. Some modules are stronger than others.
   The repo is not uniformly mature. Some layers are empirically sharper; others are still theory-heavy.

4. Operator friction still exists.
   The engine is stronger than the surface. A future UI or tighter product shell would improve accessibility substantially.

5. Interpretation must stay humble.
   The system can identify pattern shape. It should not overclaim hidden motives or inner states.

## Why Keep Working On It

Because the project already contains something rare: a serious attempt to treat persuasion as a structured behavioral system rather than an aesthetic.

The next gains are not about stuffing in more theory. They are about:

- cleaner interfaces
- better extraction
- better uncertainty handling
- stronger real-world validation
- better packaging for non-terminal use

That is a better problem to have than “there is nothing here.”

## References

The repo draws from work in appraisal theory, persuasion, reward prediction, influence, moral framing, and decision neuroscience, including Damasio, Knutson, Petty & Cacioppo, Feinberg & Willer, Graham/Haidt/Nosek, Brady et al., and related modern persuasion datasets and benchmarks already cited in the project materials.
