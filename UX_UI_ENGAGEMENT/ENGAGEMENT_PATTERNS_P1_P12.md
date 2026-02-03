# UX/UI Engagement Patterns (P1-P12)
## Digital Product Engagement Mechanics

This document catalogs 12 core engagement patterns used in digital products, with constants, applications, triggers, and documented metrics.

**Cross-Reference:** For linguistic persuasion techniques, see `LINGUISTIC_PERSUASION/DETECTION/`

---

## Pattern 1: Variable Reward Scheduling

Unpredictable rewards create stronger engagement than predictable ones.

### Constants
```
ANTICIPATION_WINDOW: 200-400ms
ANTICIPATION_STRETCH: 70ms at peak
HIT_FREQUENCY: 19.8% (range 15-22%)
BONUS_TRIGGER: 37 (prime number)
REWARD_TIERS: 50% micro, 35% standard, 12% major, 3% legendary
```

### Applied To
- Slot machines: 19.8% hit frequency
- Loot boxes: 0.07% rare drop rates
- Social notifications: clustered batches
- Mobile games: cascade bonuses at 30% rate

### Triggers
- Time elapsed (anticipation window)
- User action (spin/pull/open)
- Algorithmic probability (BONUS_TRIGGER)

### Results
```
ENGAGEMENT_RESPONSE: Higher response rates vs fixed schedules
TIME_ON_DEVICE: 19.8% frequency optimal
RESISTANCE_TO_EXTINCTION: Increased continuation behavior
```

### Documented Metrics

```
Animation Duration Testing:
├── 3s animation: 12% repeat purchase rate
├── 5s animation: 18% repeat purchase rate
├── 8s animation: 23% repeat purchase rate
└── 12s animation: 19% repeat purchase rate (abandonment)

Anticipation Window:
├── 100ms hold: 8% conversion
├── 200ms hold: 14% conversion
├── 400ms hold: 22% conversion
└── 600ms hold: 18% conversion

Sound Design:
├── No audio: 11% repeat purchase
├── Generic audio: 16% repeat purchase
├── Optimized audio: 24% repeat purchase
└── Audio + haptic: 31% repeat purchase

Revenue Impact:
├── Total market: $1.62B (FIFA Ultimate Team)
├── Pack purchases: 78% of segment revenue
├── Average packs per user: 847/year
├── TOTY drop rate: 0.07%
└── Average spend for TOTY: $2,400

Engagement vs Fixed Schedules: 3.2x
Average animation duration: 6.8s
Youth engagement rate: 40%
```

---

## Pattern 2: Progress Momentum

Near-successes generate continued engagement through reward-like activation.

### Constants
```
OPTIMAL_RATE: 30%
DOPAMINE_RATIO: 120% baseline (vs 150% win)
CUMULATIVE_PROGRESS: 3 near-successes = 1 consolation reward
```

### Applied To
- Slot machines: "almost there" displays
- Mobile games: "one move away" board states
- Learning apps: "almost had it" feedback
- Progress bars: fill on unsuccessful attempts

### Triggers
- Outcome within visible range of success (reel position, score threshold)
- Consistent rate maintained (30% of attempts)

### Results
```
DOPAMINE_RESPONSE: 120% baseline activation (vs 85% clear loss)
ENGAGEMENT_EXTENSION: 22% longer play sessions
BEHAVIOR_INTERPRETATION: Near-successes perceived as progress evidence
TIME_ON_DEVICE: 28% increase with optimized momentum feedback
```

### Documented Metrics

```
Brain Activation (fMRI):
├── Win: 150% of baseline
├── Near-miss: 120% of baseline
└── Clear loss: 85% of baseline

Behavioral:
├── Play session extension: 22% longer
├── Continuation likelihood: 34% more likely
├── Perceived progress: Interpreted as evidence

Rate Optimization:
├── 15% near-success: 12% time-on-device increase
├── 30% near-success: 28% time-on-device increase
├── 45% near-success: 18% (diminishing returns)

Engagement:
├── Daily engagement: 23% higher
├── User-perceived vs measured progress: 3x ratio
└── Average session extension: 27 minutes optimized, 40 minutes typical
```

---

## Pattern 3: Encouraging Feedback

Celebration for sub-threshold outcomes creates positive reinforcement.

### Constants
```
CELEBRATION_RATIO: 64%
CELEBRATION_INTENSITY: 70-90% of full achievement
AUDIO: -3dB from full achievement
VISUAL: 0.7x intensity
HAPTIC: 0.8x strength
```

### Applied To
- Slot machines: 64% of returns
- Multiline games: any payline match
- Mobile games: common item rewards
- Fitness apps: partial progress milestones

### Triggers
- Sub-threshold return (below wager amount)
- Any positive payline match (multiline machines)
- Partial achievement completion

### Results
```
SKIN_CONDUCTANCE: 3.8 μS (vs 1.1 μS without feedback)
HEART_RATE_RESPONSE: +6 BPM (75% of full win)
POSITIVE_PERCEPTION: 63% of users perceive as positive experience
ENGAGEMENT_TIME: 34% higher time-on-device
RETURN_FREQUENCY: 45% more frequent visits
```

### Documented Metrics

```
Skin Conductance Response:
├── Full win: 4.2 μS increase
├── Partial with feedback: 3.8 μS increase
└── No feedback: 1.1 μS increase

Heart Rate Response:
├── Full win: +8 BPM
├── Partial with feedback: +6 BPM (75%)
└── No feedback: +1 BPM

User Perception:
├── Positive perception: 63% of users
├── Recall frequency: 2.4x higher than actual
└── Engagement correlation: r = 0.67

Multiline Machines (243-way):
├── Full win rate: 8% of spins
├── Partial return rate: 56% of spins
├── Positive feedback total: 64% of spins

Engagement:
├── Time-on-device: 34% higher
├── User-reported enjoyment: 28% higher
└── Return frequency: 45% more visits
```

---

## Pattern 4: Progress Protection

Losses perceived as 2.25x more impactful than gains (Kahneman & Tversky); protection offers leverage this documented asymmetry.

### Constants
```
MULTIPLIER: 2.25x
STAGING_DELAYS: 0.5s, 1.0s, 0.8s, 1.5s
PROTECTION_PRICING:
  <14 days: $0.99
  <30 days: $1.99
  <90 days: $4.99
  90+: $9.99
URGENCY_WINDOW: 24 hours
```

### Applied To
- Streak systems (Duolingo, Snapchat)
- Subscription cancellation flows (Amazon Prime)
- Mobile game lives/hearts systems
- Progress bars with decay mechanics

### Triggers
- Progress expiration detected
- Streak break event
- Cancellation intent

### Results
```
PROTECTION_PURCHASE_RATE: 12% of conversions
PRICING_EFFECTIVENESS: Scales with investment length (2.25x multiplier)
CHURN_PREVENTION: Multi-step flow reduces 23% → 4.2%
ENGAGEMENT_EXTENSION: 27-minute session increase with optimized messaging
```

### Documented Metrics

```
Streak Impact:
├── 7+ day streak: 4.5x subscription rate
├── Protection purchases: 12% of conversions
├── Pricing: $0.99-$9.99 scaled to streak

Loss Sensitivity Basis: 2.25x
```

---

## Pattern 5: Investment Recognition

Displaying accumulated investment increases continued investment likelihood after 10-hour threshold.

### Constants
```
COMMITMENT_THRESHOLD: 10 hours
VALUE_REMINDER: Display investment at session end
MAINTENANCE_MECHANIC: Progress maintenance over time
```

### Applied To
- Social games: neighbor relationships, care mechanics
- Subscription cancellation: membership duration + usage stats
- Retention flows: time invested, milestones reached
- Progress decay systems: maintenance requirements

### Triggers
- Session completion
- Cancellation intent
- Milestone thresholds

### Results
```
RETENTION_MULTIPLIER: 3x (social features)
7_DAY_STREAK_IMPACT: 4.5x subscription rate
CANCELLATION_RATES: Single-step 23% → Multi-step 4.2%
PERCEIVED_VALUE: Lifetime savings calculations reduce churn
```

### Documented Metrics

```
Cancellation Completion Rates:
├── Single-page: 23%
├── Multi-step with benefits: 8%
├── With savings display: 6%
├── Full flow: 4.2%
```

---

## Pattern 6: Timely Opportunities

Limited availability and time pressure increase perceived value and decision velocity.

### Constants
```
COUNTDOWN_BEHAVIOR: Can restart after expiry
INVENTORY_DISPLAY: Often starts at 30-50% claimed
NOTIFICATION_ESCALATION: 24h → 6h → 1h before expiry
SOCIAL_PROOF_REFRESH: Updates every 30-60s
```

### Applied To
- Travel booking: room/price scarcity indicators
- Gacha games: limited banner windows (2-3 weeks)
- Flash sales: countdown timers with claimed %
- Streak systems: expiration warnings

### Triggers
- Time remaining (countdown)
- Availability limits ("only X left")
- Comparative signals ("X people looking now")

### Results
```
CONVERSION_NO_SCARCITY: 12%
CONVERSION_WITH_SCARCITY: 31% (full suite applied)
DECISION_VELOCITY: Increased with countdown display
PRICE_IMPACT: "Price increased" signal affects repeat visitors
```

### Documented Metrics

```
Display Ranges:
├── "X people looking": 847-2,341 (A/B tested)
├── "Booked X times": 3-12 range
└── Update frequency: 30-60s

Conversion Impact:
├── No scarcity: 12%
├── + Activity count: 18%
├── + Booking count: 24%
└── Full suite: 31%
```

---

## Pattern 7: Contextual Offers

Emotional states determine offer conversion rates and optimal presentation timing.

### Constants
```
CHALLENGED: 3.0s delay, 8% conversion
PROTECTING: 0.5s delay, 12% conversion
MOTIVATED: 2.0s delay, 15% conversion (highest)
CELEBRATING: 5.0s delay, 5% conversion
```

### Applied To
- Mobile games: help/continue offers after loss
- Fitness apps: premium upgrades after workouts
- Dating apps: feature offers during engagement phases
- Game over screens: purchase prompts

### Triggers
- Consecutive failures (frustrated state)
- Near-success outcome (motivated state)
- Progress at risk (protecting state)
- Achievement completion (celebrating state)

### Results
```
CONVERSION_FRUSTRATED: 8%
CONVERSION_PROTECTING: 12%
CONVERSION_MOTIVATED: 15% (peak)
CONVERSION_CELEBRATING: 5%
NEAR_SUCCESS_ENHANCEMENT: Generic "try again" 9% → Progress bar 90%+ 22%
```

### Documented Metrics

```
Emotional Timing:
├── 0.0s delay: 8% conversion
├── 1.5s delay: 12%
├── 2.0s delay: 15% (optimal)
├── 3.0s delay: 11%

Near-Success Messaging:
├── Generic "try again": 9%
├── "You were close": 14%
├── Progress bar 90%+: 22%
```

---

## Pattern 8: Immersive Experience

Deep focus states maintained through flow mechanics; minimize interruptions to extend engagement.

### Constants
```
THRESHOLD: 180 seconds to enter
FOCUS_MULTIPLIER: 2.3x engagement for focus-prone users

INDICATORS:
  input_regularity: >85% consistent timing
  session_duration: >10 minutes
  focus_stability: >75% in engaged states
  interaction_rate: <0.3/second (absorbed)

CONTINUATION: audio shift, visual pulse, new content
```

### Applied To
- Infinite scroll platforms (TikTok, Instagram)
- Streaming services (auto-play, countdown)
- Gaming environments (seamless transitions)
- Slot machines (environmental design)

### Triggers
- 180+ seconds continuous engagement
- Consistent input regularity maintained
- User absorption detected

### Results
```
SESSION_DURATION_NO_INTERRUPTION: 45 min average (infinite scroll)
SESSION_DURATION_WITH_BREAKS: 12 min average
TEEN_DAILY_AVERAGE: 95 minutes
TIME_UNDERESTIMATION: 60% perceive less time than actual
FLOW_STATE_ENGAGEMENT: 2.3x multiplier for susceptible users
```

### Documented Metrics

```
Session Duration:
├── With breaks: 12 min average
├── Infinite scroll: 45 min average
├── Teen daily users: 95 min

Flow Indicators:
├── Input regularity >85%: In flow state
├── Session >10 min: Deep engagement
└── Time underestimation: 60% actual vs perceived
```

---

## Pattern 9: Personalized Experience Tiers

Revenue concentration; 0.19% of users generate 48% of revenue. Tier-specific offers target high-value user LTV.

### Constants
```
DISTRIBUTION: 0.19% of users generate 48% of revenue
TOP_10_PERCENT: 92% of revenue

TIER_THRESHOLDS:
  CASUAL: $0 → $0.99-$1.99 offers
  REGULAR: $10+ → $4.99-$9.99 offers
  ENTHUSIAST: $100+ → $19.99-$49.99 offers
  VIP: $500+ → $199.99-$499.99 offers

VALUE_SIGNALS:
  Sessions >5/week: 2.3x LTV
  Session length >15 min: 1.8x LTV
  Streak >14 days
  First purchase <3 sessions: 3.2x LTV signal
  Protection purchases: 4.1x LTV
```

### Applied To
- Mobile game IAP catalogs (tiered)
- Gacha pity systems
- Subscription tiers
- VIP store access
- Exclusive content gates

### Triggers
- Lifetime spend threshold
- Early purchase signals
- Engagement metrics (sessions, length, streak)
- Protection purchase behavior

### Results
```
AVERAGE_HIGH_VALUE_SPENDING: $450/month
TOP_TIER_CEILING: $10,000+/month
LTV_MULTIPLIER_HIGH_FREQUENCY: 2.3x
LTV_MULTIPLIER_LONG_SESSIONS: 1.8x
LTV_MULTIPLIER_PROTECTION_BUY: 4.1x
```

### Metrics
```
Revenue Distribution:
├── 0.19% of players = 48% of revenue
├── Top 10% = 92% of revenue
├── Average high-value user: $450/month
└── Top tier ceiling: $10,000+/month

LTV Signals:
├── Sessions >5/week: 2.3x LTV
├── Session >15 min: 1.8x LTV
├── Protection purchase: 4.1x LTV
```

---

## Pattern 10: Community Activity Display

Peer activity visibility influences user behavior through social proof and activity signals.

### Constants
```
COMPARISON_OFFSET: +2 to +7 days ahead
TIME_MARGIN: 1.1-1.5x user's time

DISPLAY_RANGES:
  Active "now": 847-2,341
  Engaged/hour: 156-489
  Daily activity: 12,847-34,521

UPDATE_RULE: Maintain active community visibility
REFRESH_CYCLE: Every 30-60s
```

### Applied To
- Travel booking: scarcity ("X people looking")
- Mobile games: online player counts
- E-commerce: cart/item popularity
- Social platforms: activity feeds

### Triggers
- Page load (initial display)
- Refresh interval (30-60s updates)
- Availability signals

### Results
```
CONVERSION_NO_PROOF: 12%
CONVERSION_WITH_ACTIVITY: 18% (+6%)
CONVERSION_WITH_BOOKING_DATA: 24% (+4%)
CONVERSION_FULL_SUITE: 31% (+15% combined)
```

### Metrics & Regulatory
```
Conversion Impact:
├── No social proof: 12%
├── + Activity count: +6%
├── + Booking count: +4%
└── Combined: +15%

UK CMA (2019): Required Booking.com
to clarify "people looking" timeframes
```

---

## Pattern 11: Community Connection

Social commitment and visible individual contribution to collective goals increases engagement 3x.

### Constants
```
RETENTION_MULTIPLIER: 3x
NOTIFICATION_TIMING: After 24h inactivity
GROUP_MECHANIC: Individual actions impact collective outcomes
COMPARISON_OFFSET: Slightly ahead of user
```

### Applied To
- Social gifting systems (neighbor mechanics)
- Group challenges (club competitions)
- Party/team mechanics (shared goals)
- Simultaneous events (synchronized notifications)
- Activity visibility (public feeds)

### Triggers
- Inactivity detection (24h+)
- Group progress milestone
- Member contribution needed
- Collective goal status change

### Results
```
SOCIAL_FEATURES_RETENTION: 3x vs game features alone
RETENTION_WITH_COMMUNITY: 1x base
RETENTION_WITH_NOTIFICATIONS: 1.8x
RETENTION_WITH_VISIBILITY: 2.4x
RETENTION_WITH_GROUP_MECHANICS: 3x
```

### Documented Metrics

```
Social Feature Impact (Zynga 2012):
├── Game mechanics alone: 1x retention
├── + Social notifications: 1.8x
├── + Friend visibility: 2.4x
├── + Group mechanics: 3x
```

---

## Pattern 12: Identity & Achievement

Progressive identity integration through badges and public milestones; increases retention post-achievement.

### Constants
```
PROGRESSION:
  NONE → CURIOUS (3 sessions)
  → PRACTITIONER (7-day streak)
  → DEDICATED (30-day streak)
  → DEVOTED (100-day streak)
  → MASTER (365-day streak)

INVESTMENT_WEIGHTING:
  Time: 30%
  Streak: 30%
  Achievements: 20%
  Social: 10%
  Title: 10%

PUBLIC_SHARING: Creates community and commitment
```

### Applied To
- Achievement badges (milestone unlocks)
- Leaderboard titles and ranks
- Merchandise (identity expression)
- Social share mechanics
- "Year in Review" summaries

### Triggers
- Milestone achievement (100 rides, 365-day streak)
- Rank advancement
- Time-based progression

### Results
```
CHURN_PRE_MILESTONE: 12%
CHURN_POST_MILESTONE: 3%
MERCHANDISE_PURCHASE_RATE: 67% within 30 days
SOCIAL_SHARE_RATE: 84%
90_DAY_RETENTION_0_25_RIDES: 35%
90_DAY_RETENTION_25_50: 58%
90_DAY_RETENTION_50_100: 78%
90_DAY_RETENTION_100_PLUS: 94%
```

### Documented Metrics

```
Milestone Impact:
├── Pre-milestone churn: 12%
├── Post-milestone churn: 3%
├── Merchandise purchase: 67% within 30 days
├── Social share rate: 84%

Retention by Engagement:
├── 0-25 rides: 35% 90-day retention
├── 25-50 rides: 58%
├── 50-100 rides: 78%
├── 100+ rides: 94%
```

---

## Reference Tables

### Timing Constants
| Parameter | Value |
|-----------|-------|
| Anticipation window | 200-400ms |
| Anticipation stretch | 70ms |
| Hit frequency | 19.8% |
| Momentum feedback rate | 30% |
| Bonus trigger interval | 37 |
| Post-reward quiet period | 60s |
| Flow state threshold | 180s |

### Psychological Multipliers
| Parameter | Value |
|-----------|-------|
| Progress protection response | 2.25x |
| Momentum response | 1.20x baseline |
| Encouragement ratio | 64% |
| Focus multiplier | 2.3x |

### Conversion by Context
| Context | Delay | Rate |
|---------|-------|------|
| Challenged | 3.0s | 8% |
| Protecting | 0.5s | 12% |
| Motivated | 2.0s | 15% |
| Celebrating | 5.0s | 5% |

### Experience Tiers
| Tier | Threshold |
|------|-----------|
| Casual | $0 |
| Regular | $10+ |
| Enthusiast | $100+ |
| VIP | $500+ |

**Distribution: 0.19% of users = 48% of revenue**

### Community Activity Ranges
| Metric | Range |
|--------|-------|
| Active "now" | 847-2,341 |
| Engaged/hour | 156-489 |
| Daily count | 12,847-34,521 |
| Comparison offset | +2-7 days |
| Time comparison | 1.1-1.5x |

---

## Cross-References

- **Detection Implementation:** See `UX_UI_ENGAGEMENT/DETECTION/ENGAGEMENT_PATTERN_DETECTION.py`
- **Session Architecture:** See `UX_UI_ENGAGEMENT/SESSION_ARCHITECTURE.md`
- **Pattern Combinations:** See `UX_UI_ENGAGEMENT/CROSS_PATTERN_INTERACTION_MAPS.md`
- **User Profiles:** See `UX_UI_ENGAGEMENT/USER_VULNERABILITY_PROFILES.md`
- **Linguistic Patterns:** See `LINGUISTIC_PERSUASION/DETECTION/`
