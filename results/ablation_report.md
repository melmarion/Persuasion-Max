# Ablation Report

**Date:** 2026-03-28

## Recipient Trait Ablation

Max compliance change when each trait is set to default (0.5).

| Trait | Max Impact | Status |
|-------|-----------|--------|
| extraversion | 4.7% | ACTIVE |
| elaboration_likelihood | 4.7% | ACTIVE |
| conscientiousness | 4.0% | ACTIVE |
| agreeableness | 3.5% | ACTIVE |
| neuroticism | 2.4% | ACTIVE |
| involvement | 2.0% | ACTIVE |
| care_harm | 1.3% | ACTIVE |
| loyalty_betrayal | 1.1% | ACTIVE |
| economic_ideology | 1.0% | ACTIVE |
| social_ideology | 1.0% | ACTIVE |
| openness | 0.5% | DEAD |
| liberty_oppression | 0.4% | DEAD |
| fairness_cheating | 0.0% | DEAD |
| authority_subversion | 0.0% | DEAD |
| sanctity_degradation | 0.0% | DEAD |
| prior_belief | 0.0% | DEAD |

Dead traits (< 1pp impact): openness, liberty_oppression, fairness_cheating, authority_subversion, sanctity_degradation, prior_belief

## Technique Category Ablation

| Category | Impact | Status |
|----------|--------|--------|
| framing | 0.4% | DEAD |
| emotion | 0.4% | DEAD |
| rapport | 0.3% | DEAD |
| social | 0.3% | DEAD |
| narrative | 0.2% | DEAD |
| urgency | 0.1% | DEAD |
| reasoning | 0.1% | DEAD |
| manipulation | 0.1% | DEAD |
| attack | 0.0% | DEAD |
| cognitive | 0.0% | DEAD |
| compliance | 0.0% | DEAD |
| credibility | 0.0% | DEAD |
| deception | 0.0% | DEAD |
| fallacy | 0.0% | DEAD |
| linguistic | 0.0% | DEAD |

Dead categories (< 0.5pp impact): framing, emotion, rapport, social, narrative, urgency, reasoning, manipulation, attack, cognitive, compliance, credibility, deception, fallacy, linguistic

## Domain Weight Ablation

| Domain | Universal | Domain-Specific | Difference |
|--------|-----------|----------------|------------|
| ecommerce | 55.0% | 67.9% | 12.9pp |
| campaign | 48.0% | 48.0% | 0.0pp |
| crisis_pr | 48.3% | 48.6% | 0.3pp |