# Neuro-Aesthetic Parameters
## Sensory Design Specifications for Engagement

This document defines the precise color, audio, and haptic parameters used in engagement-optimized interfaces.

**Cross-Reference:** For pattern applications, see `ENGAGEMENT_PATTERNS_P1_P12.md`

---

## Color Parameters

### Wavelength Specifications

```
Parameter          Value      Purpose
──────────────────────────────────────────────────────────
CALMING_BLUE       450nm      Deep blue, calming effect
RELAXING_BLUE      490nm      Cyan-blue, relaxed alertness
SATURATION_CAP     30%        Prevents overstimulation
BRIGHTNESS_TARGET  70%        Optimal visibility without strain
```

### Color Psychology Application

| Color Range | Wavelength | Psychological Effect | Use Case |
|-------------|------------|---------------------|----------|
| Deep Blue | 450nm | Calm, trust, reduced anxiety | Background, loading states |
| Cyan-Blue | 490nm | Relaxed focus, engagement | Active UI elements |
| Warm Accent | 580-620nm | Attention, urgency | CTAs, notifications |
| Neutral | N/A | Cognitive rest | Content areas |

### Saturation Guidelines

```
Element Type           Saturation    Reasoning
──────────────────────────────────────────────────────────────
Background             10-15%        Visual comfort, extended use
Secondary Elements     20-25%        Subtle differentiation
Primary Elements       30% (cap)     Attention without fatigue
Alert/Reward States    40-50%        Momentary high-attention
```

---

## Audio Parameters

### Frequency Specifications

```
Parameter            Value           Purpose
──────────────────────────────────────────────────────────────
THETA_WAVE           6.0 Hz          Relaxed focus state induction
ASMR_FUNDAMENTAL     180 Hz          Pleasant tingling response
SCHUMANN_FREQUENCY   7.83 Hz         Earth resonance, grounding
BINAURAL_BASE        180 Hz          Base tone for binaural beats
BINAURAL_OFFSET      186 Hz          Creates 6 Hz difference
```

### Binaural Beat Design

```
Binaural Configuration:
├── Left ear:  180 Hz
├── Right ear: 186 Hz
├── Perceived: 6 Hz (theta range)
└── Effect:    Relaxed focus, reduced critical thinking
```

### Audio Intensity by Pattern

| Pattern | Audio Approach | dB Relative |
|---------|----------------|-------------|
| P1 (Variable Reward) | Build + reveal | +6dB peak |
| P2 (Near-miss) | Similar to win | -3dB from win |
| P3 (Encouraging) | Celebration | -3dB from full win |
| P8 (Immersive) | Ambient continuity | Baseline |
| P12 (Achievement) | Triumphant | +3dB from baseline |

### Sound Design Metrics

From documented research:
```
Audio Impact on Repeat Purchase:
├── No audio:        11% repeat rate
├── Generic audio:   16% repeat rate
├── Optimized audio: 24% repeat rate
└── Audio + haptic:  31% repeat rate

Optimal audio adds 13-20% to engagement metrics
```

---

## Haptic Parameters

### Duration Specifications

```
Parameter       Duration    Purpose
──────────────────────────────────────────────────────────────
MICRO           15ms        Subtle confirmation, button press
BREATH_SYNC     50ms        Gentle rhythm, breathing alignment
EMPHASIS        200ms       Important feedback, rewards
INTEGRATION     800ms       Major achievements, session milestones
LEAD_TIME       16-50ms     Anticipatory pulse before visual
```

### Haptic Intensity by Pattern

| Pattern | Haptic Type | Intensity |
|---------|-------------|-----------|
| P1 (Variable Reward) | Scaled to outcome | 0.5-1.0x |
| P2 (Near-miss) | Similar to win | 0.85x |
| P3 (Encouraging) | Sub-win celebration | 0.8x |
| P7 (Contextual) | Attention pulse | 0.6x |
| P12 (Achievement) | Full celebration | 1.0x |

### Haptic Timing Principles

```
Sensory Integration Timeline:
├── 0ms:      Visual cue initiated
├── 16-50ms:  Haptic anticipation (LEAD_TIME)
├── 50ms:     Visual fully rendered
├── 70ms:     Audio sync point
└── 100ms+:   Sustained feedback as needed

Lead Time Optimization:
├── 16ms: Minimum perceivable lead
├── 33ms: Optimal anticipation
├── 50ms: Maximum before disconnect
```

---

## Recognition Timing

### Micro-Expression Parameters

```
Parameter        Value     Purpose
──────────────────────────────────────────────────────────────
PERSONAL_PULSE   150ms     Micro-expression timing match
                           Creates sense of being "seen"
```

### Recognition Application

The 150ms timing aligns with human micro-expression duration, creating an unconscious sense of personal recognition when UI elements respond within this window.

---

## Multi-Sensory Coordination

### Synchronized Feedback Table

| Event | Visual | Audio | Haptic | Total Duration |
|-------|--------|-------|--------|----------------|
| Button press | Immediate | +15ms | 15ms | 30ms |
| Small reward | 200ms | +50ms | 50ms | 300ms |
| Medium reward | 500ms | +100ms | 200ms | 800ms |
| Large reward | 1000ms | +200ms | 800ms | 2000ms |
| Achievement | 2000ms | +500ms | 800ms | 3300ms |

### Animation Duration Research

```
Animation Duration Impact on Repeat Purchase:
├── 3s animation:  12% repeat purchase rate
├── 5s animation:  18% repeat purchase rate
├── 8s animation:  23% repeat purchase rate (optimal)
└── 12s animation: 19% repeat purchase rate (abandonment)

Optimal animation duration: 6.8s average
```

---

## Environmental Design

### Ambient Conditions

```
Condition         Specification    Effect
──────────────────────────────────────────────────────────────
Lighting          Dim preferred    Reduces external awareness
Sound isolation   High             Maintains immersion
Temperature       68-72°F          Cognitive comfort zone
Seating           Reclined option  Relaxation, extended sessions
```

### Time Perception Factors

```
Time Underestimation Factors:
├── Flow state:           60% perceive less time
├── Absent clock display: 45% longer sessions
├── Dim lighting:         30% time underestimation
├── Continuous audio:     25% time underestimation
└── Combined:             Up to 80% underestimation
```

---

## Cross-References

- **Pattern Applications:** `ENGAGEMENT_PATTERNS_P1_P12.md`
- **Session Timing:** `SESSION_ARCHITECTURE.md`
- **Detection Methods:** `DETECTION/ENGAGEMENT_PATTERN_DETECTION.py`
- **User Profiles:** `USER_VULNERABILITY_PROFILES.md`
