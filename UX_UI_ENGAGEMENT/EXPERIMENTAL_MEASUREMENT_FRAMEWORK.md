# Experimental Measurement Framework
## Protocols for Measuring Pattern Effectiveness

This document provides research protocols for measuring engagement pattern effectiveness, including A/B testing, fatigue measurement, temporal analysis, and cross-cultural validation.

**Cross-Reference:** For pattern definitions, see `ENGAGEMENT_PATTERNS_P1_P12.md`

---

## A/B Testing Protocol for Pattern Effectiveness

### Single Pattern Validation

```
MINIMUM VIABLE EXPERIMENT DESIGN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Single Pattern Validation:
├── Control: No pattern applied
├── Treatment: Single pattern at documented intensity
├── Sample size: N ≥ 5,000 per arm (10,000 total)
├── Duration: 14-30 days minimum
├── Primary metric: Conversion rate
├── Secondary: Session duration, return rate, LTV at 30d
└── Power: 80% to detect 15% relative lift
```

### Two-Pattern Interaction Test

```
Two-Pattern Interaction Test:
├── Arms: Control, P_a only, P_b only, P_a + P_b
├── Sample size: N ≥ 3,000 per arm (12,000 total)
├── Analysis: 2x2 factorial ANOVA
├── Interaction term: Tests superadditive vs subadditive
└── Threshold: Interaction p < 0.05
```

**Interpretation Guide:**
- **Significant positive interaction:** Superadditive (patterns amplify)
- **Significant negative interaction:** Subadditive (patterns compete)
- **Non-significant interaction:** Additive (patterns independent)

### Sequence Testing (Latin Square)

```
Sequence Testing (Latin Square):
├── Patterns: 3 patterns = 6 permutations
├── Sample size: N ≥ 2,000 per sequence (12,000 total)
├── Design: Balanced Latin square
├── Analysis: Repeated measures ANOVA
└── Post-hoc: Tukey HSD for pairwise sequence comparison
```

**Example 3-Pattern Permutations:**
| Sequence | Order |
|----------|-------|
| S1 | P1 → P6 → P4 |
| S2 | P1 → P4 → P6 |
| S3 | P6 → P1 → P4 |
| S4 | P6 → P4 → P1 |
| S5 | P4 → P1 → P6 |
| S6 | P4 → P6 → P1 |

---

## Fatigue Curve Measurement

### Longitudinal Tracking Protocol

```
LONGITUDINAL TRACKING PROTOCOL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Exposure Counting:
├── Log: Pattern_id, user_id, timestamp, context
├── Metric: Response rate per exposure number
├── Window: Rolling 7-day, 30-day, 90-day
└── Segmentation: By user engagement tier
```

### Decay Curve Fitting

```
Decay Curve Fitting:
├── Model: Response(t) = R_0 × e^(-λt)
├── Parameters: R_0 (initial response), λ (decay rate)
├── Half-life: t_½ = ln(2) / λ
└── Recovery: Test after 7d, 14d, 30d gap
```

**Formula Explanation:**
- `R_0`: Initial response rate (baseline effectiveness)
- `λ`: Decay constant (higher = faster fatigue)
- `t_½`: Time until 50% effectiveness
- `e`: Euler's number (~2.718)

### Pattern Rotation Protocol

```
Pattern Rotation Protocol:
├── Arm 1: P_a constant
├── Arm 2: P_a → P_b → P_a rotation (7-day cycles)
├── Arm 3: P_a → P_b → P_c rotation
├── Hypothesis: Rotation maintains higher sustained response
└── Metric: Area under response curve over 90 days
```

**Expected Outcomes:**
| Arm | Predicted AUC | Rationale |
|-----|---------------|-----------|
| Constant | 0.65 | Fatigue accumulates |
| 2-Pattern Rotation | 0.78 | Partial recovery |
| 3-Pattern Rotation | 0.85 | Maximum recovery |

---

## Temporal Effect Measurement

### Hour-of-Day Analysis

```
TIME-STRATIFIED A/B TEST:
━━━━━━━━━━━━━━━━━━━━━━━━

Hour-of-Day Analysis:
├── Bins: 4-hour windows (6 bins per day)
├── Control for: User timezone, engagement history
├── Sample: Minimum 500 users per bin
├── Metric: Conversion rate by hour
└── Analysis: Time-series regression with hour fixed effects
```

**Time Bins:**
| Bin | Hours | Expected Vulnerability |
|-----|-------|------------------------|
| 1 | 00:00-03:59 | High (fatigue) |
| 2 | 04:00-07:59 | Low (waking) |
| 3 | 08:00-11:59 | Moderate |
| 4 | 12:00-15:59 | Moderate |
| 5 | 16:00-19:59 | High (decision fatigue) |
| 6 | 20:00-23:59 | High (relaxation) |

### Day-of-Week Analysis

```
Day-of-Week Analysis:
├── Bins: 7 days, weekday vs weekend aggregate
├── Duration: Minimum 4 weeks for stability
├── Control for: Seasonal effects, paycheck timing
└── Analysis: Day-of-week dummy variables in regression
```

### Optimal Timing Discovery

```
Optimal Timing Discovery:
├── Multi-armed bandit: Thompson sampling
├── Arms: 24 hour slots or 168 hour-day combinations
├── Exploration: 20% random allocation
├── Exploitation: 80% to best-performing slots
└── Convergence: ~10,000 observations per pattern
```

---

## Cross-Cultural Validation Protocol

### Multi-Market Testing

```
MULTI-MARKET TESTING:
━━━━━━━━━━━━━━━━━━━━━

Minimum Market Requirements:
├── Sample: N ≥ 5,000 per market per pattern
├── Markets: Minimum 3 cultures per Hofstede dimension
├── Controls: Language, payment method, platform penetration
└── Normalization: Conversion rates indexed to market baseline
```

### Hofstede Dimension Controls

```
Hofstede Dimension Controls:
├── Individualism/Collectivism: US, AU vs JP, KR, CN
├── Uncertainty Avoidance: DE, JP vs UK, SG
├── Power Distance: MX, IN vs DK, IL
├── Masculinity/Femininity: JP, IT vs SE, NO
├── Long-term Orientation: CN, JP vs US, UK
└── Indulgence/Restraint: MX, NG vs PK, EG
```

**Market Selection Matrix:**
| Dimension | High Markets | Low Markets |
|-----------|-------------|-------------|
| Individualism | US, AU, UK | JP, KR, CN |
| Uncertainty Avoidance | DE, JP | UK, SG |
| Power Distance | MX, IN | DK, IL |
| Masculinity | JP, IT | SE, NO |
| Long-term | CN, JP | US, UK |
| Indulgence | MX, NG | PK, EG |

### Analysis Framework

```
Analysis Framework:
├── Multi-level model: User nested in market
├── Random effects: Market-level intercept
├── Fixed effects: Hofstede scores as continuous predictors
├── Interaction: Pattern × Hofstede dimension
└── Output: Pattern-specific cultural coefficients
```

---

## Key Performance Indicators by Research Question

```
┌────────────────────────────────────────────────────────────────────────┐
│ Research Question      │ Primary KPI        │ Secondary KPIs          │
├────────────────────────┼────────────────────┼─────────────────────────┤
│ Compounding effects    │ Interaction lift   │ Incremental LTV,        │
│                        │ (obs vs expected)  │ engagement depth        │
├────────────────────────┼────────────────────┼─────────────────────────┤
│ Pattern fatigue        │ Half-life (days)   │ Recovery rate,          │
│                        │                    │ rotation efficacy       │
├────────────────────────┼────────────────────┼─────────────────────────┤
│ Temporal effects       │ Conversion rate    │ Decision latency,       │
│                        │ by hour/day        │ session initiation time │
├────────────────────────┼────────────────────┼─────────────────────────┤
│ Sequence dependency    │ Final conversion   │ Drop-off rate per step, │
│                        │ by sequence        │ time-to-completion      │
├────────────────────────┼────────────────────┼─────────────────────────┤
│ Cross-cultural         │ Pattern coefficient│ Loss aversion λ,        │
│                        │ by market          │ social proof β          │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Sample Size Calculator

### Required N by Effect Size

| Effect Size | Power 80% | Power 90% | Power 95% |
|-------------|-----------|-----------|-----------|
| Small (d=0.2) | 393/arm | 527/arm | 651/arm |
| Medium (d=0.5) | 64/arm | 86/arm | 105/arm |
| Large (d=0.8) | 26/arm | 34/arm | 42/arm |

### Recommended Minimums

| Design | Arms | N per Arm | Total N |
|--------|------|-----------|---------|
| Single pattern | 2 | 5,000 | 10,000 |
| 2-pattern interaction | 4 | 3,000 | 12,000 |
| 3-pattern sequence | 6 | 2,000 | 12,000 |
| Cross-cultural | varies | 5,000/market | 15,000+ |

---

## Data Collection Schema

### Event Log Structure

```json
{
  "event_id": "uuid",
  "timestamp": "ISO8601",
  "user_id": "hashed_id",
  "pattern_id": "P1-P12",
  "exposure_number": "int",
  "context": {
    "session_duration_ms": "int",
    "time_of_day": "hour",
    "day_of_week": "int",
    "device_type": "string",
    "market": "ISO_country"
  },
  "response": {
    "converted": "boolean",
    "latency_ms": "int",
    "amount_if_purchase": "float"
  }
}
```

---

## Cross-References

- **Pattern Definitions:** `ENGAGEMENT_PATTERNS_P1_P12.md`
- **User Profiles:** `USER_VULNERABILITY_PROFILES.md`
- **Pattern Combinations:** `CROSS_PATTERN_INTERACTION_MAPS.md`
- **Research Findings:** See `LINGUISTIC_PERSUASION/RESEARCH/EMPIRICAL_RESEARCH_SYNTHESIS.md`
