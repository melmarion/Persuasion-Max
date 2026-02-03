# Session Architecture
## Optimized Engagement Session Design

This document defines the temporal structure of engagement sessions, including reward probability curves, key event timestamps, and return hook patterns.

**Cross-Reference:** For pattern details, see `ENGAGEMENT_PATTERNS_P1_P12.md`

---

## 11-Minute Model

The optimal session follows an 11-minute arc with varying reward probability:

```
Phase        Time       Reward Probability    Purpose
─────────────────────────────────────────────────────────────
Entry        0-1 min    5%                    Low barrier, orientation
Build        1-3 min    15%                   Increasing engagement
Challenge    3-6 min    25%                   Peak difficulty zone
Peak         6-8 min    35%                   Maximum reward density
Integrate    8-10 min   20%                   Consolidation
Close        10-11 min  10%                   Session wrap, hook setup
```

### Visual Representation

```
Reward Probability (%)
     35% ─────────────────────────────●●●●────────────────────
     30% ─────────────────────●●●●●●●●        ●●●●────────────
     25% ─────────────●●●●●●●●                    ●●●●────────
     20% ─────────●●●●                                ●●●●────
     15% ─────●●●●                                        ●●──
     10% ──●●●                                              ●●
      5% ●●
         └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴────
         0     1     2     3     4     5     6     7     8    9    10   11
                                   Minutes
```

---

## Event Timestamps

Critical moments designed to establish patterns and create memorable peaks:

```
Timestamp    Event                    Purpose
──────────────────────────────────────────────────────────────
45s          First reward             Pattern establishment
120s         Value confirmation       Investment validation
240s         Deep engagement reward   Peak experience creation
400s         Late-session moment      Memorable close, return motivation
```

### Timestamp Rationale

| Time | Seconds | Psychological Function |
|------|---------|------------------------|
| 45s | 0:45 | Early reward establishes expectation; prevents abandonment |
| 120s | 2:00 | Confirms investment was worthwhile; sunk cost activation |
| 240s | 4:00 | Deep engagement reward during challenge phase |
| 400s | 6:40 | Creates peak-end memory for return motivation |

---

## Return Hooks

End-of-session elements designed to drive next-session engagement:

| Hook Type | Example | Psychological Mechanism |
|-----------|---------|------------------------|
| **Preview** | "Tomorrow: New challenge available" | Curiosity, anticipation |
| **Progress** | "You're 80% to next milestone" | Zeigarnik effect (incomplete tasks) |
| **Streak** | "Day 5 complete" | Commitment, loss aversion |
| **Mystery** | "Something changes at day 7..." | Information gap curiosity |

### Hook Effectiveness by User Type

```
Hook Type    Completion-Oriented    Social-Oriented    Casual
─────────────────────────────────────────────────────────────────
Preview      ██████ (High)          ████ (Moderate)    ███ (Low)
Progress     ████████ (Very High)   ████ (Moderate)    ██ (Low)
Streak       ████████ (Very High)   ██████ (High)      ████ (Moderate)
Mystery      ████ (Moderate)        ██████ (High)      ██████ (High)
```

---

## Session Phase Details

### Entry Phase (0-1 min)
- **Goal:** Minimize friction, establish engagement
- **Reward probability:** 5% (low to avoid overwhelming)
- **UI considerations:**
  - Minimal loading time
  - Immediate interaction opportunity
  - Clear next-action indication

### Build Phase (1-3 min)
- **Goal:** Gradual investment escalation
- **Reward probability:** 15% (increasing)
- **UI considerations:**
  - Progressive complexity
  - Encouragement feedback at 2:00 mark
  - Progress visibility

### Challenge Phase (3-6 min)
- **Goal:** Peak engagement, skill application
- **Reward probability:** 25%
- **UI considerations:**
  - Optimal difficulty calibration
  - Near-miss feedback at 30% rate
  - Flow state maintenance

### Peak Phase (6-8 min)
- **Goal:** Maximum reward density, memorable experience
- **Reward probability:** 35% (highest)
- **UI considerations:**
  - Multi-sensory feedback
  - Achievement celebrations
  - Peak-end memory creation

### Integrate Phase (8-10 min)
- **Goal:** Consolidation, value recognition
- **Reward probability:** 20% (declining)
- **UI considerations:**
  - Summary displays
  - Investment recognition
  - Social sharing prompts

### Close Phase (10-11 min)
- **Goal:** Session wrap, return motivation
- **Reward probability:** 10%
- **UI considerations:**
  - Return hooks display
  - Preview of next session
  - Streak/progress reminders

---

## Integration with Patterns

| Session Phase | Primary Patterns | Secondary Patterns |
|---------------|------------------|-------------------|
| Entry | P8 (Immersive) | P1 (Variable Reward) |
| Build | P2 (Momentum) | P3 (Encouraging) |
| Challenge | P1 (Variable Reward) | P7 (Contextual) |
| Peak | P3 (Encouraging) | P1 (Variable Reward) |
| Integrate | P5 (Investment) | P12 (Identity) |
| Close | P4 (Protection) | P6 (Timely) |

---

## Cross-References

- **Pattern Definitions:** `ENGAGEMENT_PATTERNS_P1_P12.md`
- **Neuro-Aesthetics:** `NEURO_AESTHETIC_PARAMETERS.md`
- **User Profiles:** `USER_VULNERABILITY_PROFILES.md`
- **Detection:** `DETECTION/ENGAGEMENT_PATTERN_DETECTION.py`
