# UX Design System - Master Reference for Tool Attractiveness Audit

This master document consolidates all UX design system guidance for implementing attractive tools. Use this when auditing new tool implementations to ensure they follow established design patterns and principles that drive engagement and usability.

**Purpose**: Create tools that feel responsive, intentional, and delightful through consistent application of UX laws and design principles.

---

## Quick Import Reference

```javascript
// Import all exports from main entry point
import {
  // Core tokens
  TOUCH_TARGETS, SPACING, TYPOGRAPHY, COLORS, HIERARCHY,
  RESPONSE_TIMES, CHUNK_LIMITS, A11Y,
  EASING, SPRINGS, TIMINGS, HAPTIC_RULES,
  THUMB_ZONES, GESTURE_SHORTCUTS, SCREEN_PRIORITIES,
  PROGRESS, PROGRESS_MESSAGING, EMOTIONAL_DESIGN,
  VERTICAL_RHYTHM, OPTICAL_GUIDE, BREAKPOINTS,
  getProgressPercent, shouldShowProgress, spacing, withOpacity,

  // Engagement patterns (P1-P12)
  P1_VARIABLE_REWARD, P2_PROGRESS_MOMENTUM, /* ... P3-P12 */
  USER_PATTERN_RESPONSIVENESS, PATTERN_COMBINATIONS,

  // Session design
  SESSION_PHASES, CRITICAL_EVENTS, RETURN_HOOKS,

  // Neuro-aesthetic parameters
  COLOR_WAVELENGTHS, AUDIO_FREQUENCIES, HAPTIC_SPECIFICATIONS
} from './UX_DESIGN_SYSTEM';
```

---

## 1. Core Design Tokens

### Touch Targets (Fitts's Law)
**Module**: `uxConstants.js`

- **Mobile Minimum**: 44px (Apple HIG, Android Material standard)
- **Desktop Minimum**: 24px
- **Recommended Sizes**:
  - Small: 36px (secondary actions, icons)
  - Medium: 44px (primary actions, buttons)
  - Large: 48px (critical CTAs)
  - XLarge: 56px (hero CTAs)

**Implementation**: Always use minimum 44px for mobile, 24px+ for desktop.

---

### Response Times (Doherty Threshold)
**Module**: `uxConstants.js`

- **Instant**: 0ms (hover states, immediate feedback)
- **Fast**: 100ms (button press feedback)
- **Ideal**: 400ms (maximum for addictive feel)
- **Acceptable**: 1000ms (show loading states)
- **Slow**: 2000ms+ (require progress indicators)

**Implementation**: All interactions must respond within 400ms for optimal feel.

---

### Information Chunking (Miller's Law)
**Module**: `uxConstants.js`

- **Navigation Max**: 7 items before submenus
- **Options per Group**: 7 options before categorization
- **Form Fields per Step**: 7 fields before multi-step
- **List Items before Pagination**: 9 items before pagination

**Implementation**: Break content into groups of 5-7 items.

---

### Spacing System (8px Grid - Law of Proximity)
**Module**: `uxConstants.js`

**Grid Values**:
- 1: 8px
- 2: 16px
- 3: 24px
- 4: 32px
- 5: 40px
- 6: 48px
- 8: 64px
- 10: 80px
- 12: 96px

**Semantic Names**:
- **XS**: 4px (tight grouping - form labels to fields)
- **SM**: 8px (standard grouping)
- **MD**: 12px (comfortable grouping)
- **LG**: 16px (loose grouping)
- **XL**: 24px (section separation)
- **2XL**: 32px (major section separation)
- **3XL**: 48px (page-level separation)
- **4XL**: 64px (hero section separation)
- **5XL**: 80px (large page separation)

**Implementation**: Use spacing multiples for consistent visual rhythm.

---

### Typography Scale (Law of Prägnanz - Simplicity)
**Module**: `uxConstants.js`

**Font Sizes**:
- **XS**: 10px (labels, captions)
- **SM**: 12px (small text, helper text)
- **BASE**: 14px (body text)
- **MD**: 16px (subheadings)
- **LG**: 18px (section headings)
- **XL**: 24px (page headings)
- **2XL**: 32px (hero headings)
- **3XL**: clamp(32px, 5vw, 48px) (H1 mobile)
- **4XL**: clamp(48px, 6vw, 72px) (H1 desktop)

**Font Weights** (max 2-3 weights):
- **NORMAL**: 400
- **MEDIUM**: 500
- **SEMIBOLD**: 600
- **BOLD**: 700

**Line Heights**:
- **TIGHT**: 1.1 (headlines)
- **NORMAL**: 1.5 (body text)
- **RELAXED**: 1.6 (comfortable reading)

**Implementation**: Use max 2-3 weights per section; max line width 60-80ch.

---

### Color System (60-30-10 Rule - Von Restorff Effect)
**Module**: `uxConstants.js`

**60% - Neutrals** (background, surfaces, text):
- BG: #0a0a0f
- SURFACE: #0f1419
- TEXT: rgba(255,255,255,0.9)
- MUTED: rgba(255,255,255,0.5)
- SUBTLE: rgba(255,255,255,0.3)

**30% - Brand** (purple - sections, backgrounds, icons):
- PRIMARY: #8b5cf6
- LIGHT: rgba(139, 92, 246, 0.2)
- DARK: #6d28d9

**10% - Accent** (orange - CTA ONLY, creates focus):
- CTA: #f59e0b
- CTA_HOVER: #d97706

**Semantic Colors**:
- SUCCESS: #10b981
- ERROR: #ef4444
- WARNING: #f59e0b
- INFO: #3b82f6

**Implementation**: 60% neutral base, 30% brand support, 10% accent for CTAs only.

---

### Visual Hierarchy (Von Restorff Effect)
**Module**: `uxConstants.js`

**Z-Index Layers**:
- Z_BASE: 1
- Z_DROPDOWN: 100
- Z_MODAL: 1000
- Z_TOAST: 10000

**Opacity Levels**:
- DISABLED: 0.3
- MUTED: 0.5
- SUBTLE: 0.7
- NORMAL: 1.0

**Implementation**: Use consistent z-index and opacity to establish clear hierarchy.

---

### Icon Sizes (Fitts's Law)
**Module**: `uxConstants.js`

- **XS**: 12px (inline with small text)
- **SM**: 16px (standard icon)
- **MD**: 20px (medium icon)
- **LG**: 24px (large icon)
- **XL**: 32px (extra large icon)
- **2XL**: 48px (hero icons)

---

### Common Patterns
**Module**: `uxConstants.js`

**Cards**:
- Padding: 24px (SPACING.XL)
- Border Radius: 12px
- Gap: 12px (SPACING.MD)

**Modals**:
- Padding: 32px (SPACING.2XL)
- Border Radius: 16px
- Max Width: 600px

**Sections**:
- Gap: 32px (SPACING.2XL)
- Padding: 48px 24px (3XL horizontal, XL vertical)

**Border Radius Scale**:
- SM: 4px
- MD: 8px
- LG: 12px
- XL: 16px
- FULL: 999px

---

## 2. Animations & Motion

**Module**: `uxAnimations.js`

### Easing Functions
- Linear, EaseInQuad, EaseOutQuad, EaseInOutQuad
- EaseInCubic, EaseOutCubic, EaseInOutCubic
- Custom cubic-bezier values

### Springs
- SNAPPY, BOUNCY, SMOOTH, HEAVY, LIGHT spring configurations
- Each with stiffness, damping, mass parameters

### Timing Categories
- INSTANT, FAST, SNAPPY, SMOOTH, SLOW
- Values: 0-500ms depending on interaction type

### Duration Calculation
- Function: `calculateDuration(distance, intensity)`
- Supports gesture-based animation timing

### Haptic Feedback Rules
- Light, Medium, Heavy, Success, Error feedback patterns
- Calibrated for different platforms

### Sound Specs
- Volume calibration functions
- Audio identity configurations

### Animation Parameters
- Get optimal params based on interaction type
- Harmonious ratios for consistency

---

## 3. Mobile Optimizations

**Module**: `uxMobile.js`

### Thumb Zones
- Reachable zone: center-bottom of screen
- Difficult zone: top-right corner
- Primary actions in easy zones

### Gesture Shortcuts
- Swipe patterns for common actions
- Gesture-based navigation

### Screen Priorities
- Hierarchy of information on mobile
- Content ordering based on usage patterns

### Core User Journey
- Optimized flow for mobile users
- Minimum interactions to goal

### Responsive Breakpoints
- Mobile: ≤768px
- Tablet: 768px-1024px
- Desktop: >1024px

---

## 4. Progress Indicators

**Module**: `uxProgress.js`

### Progress Display Rules
- Show at 1000ms+ (Doherty threshold)
- Messaging indicates current step
- Layered progress information
- Different formats (bar, circular, text)

### Threshold Rules
- When to show, hide, or change progress display
- Notification triggers for milestones

---

## 5. Emotional Design

**Module**: `uxEmotional.js`

### Core Emotion Strategy
- Emotional framework for product
- Personality and voice guidelines

### Emotional Design Elements
- Visual design that conveys feeling
- Micro-interactions that delight

### Onboarding Emotion Sequence
- Progressive emotional engagement
- Building user investment over time

### Emotional Feedback
- Feedback that reinforces emotional connection
- Celebration and acknowledgment patterns

### Audio Identity
- Sound design guidelines
- Sonic branding consistency

---

## 6. Social Proof

**Module**: `uxSocial.js`

### Social Proof Display Types
- User counts, reviews, testimonials
- Social proof messaging patterns
- Proof type configurations

---

## 7. Layout Patterns

**Module**: `uxLayout.js`

### Vertical Rhythm
- Consistent spacing relationship
- Harmonious layout flow

### Optical Guide
- Visual alignment guidelines
- Balance and proportion rules

### Container Widths
- Max-width constraints for readability
- Responsive width configurations

### Breakpoints
- Standard responsive breakpoints
- Mobile, tablet, desktop specifications

---

## 8. Helper Functions

**Module**: `uxHelpers.js`

```javascript
// Progress Calculations
getProgressPercent(current, total)
shouldShowProgress(elapsedTime)

// Data Management
getChunkedItems(items, chunkSize)
getScrollPhysics(velocity, friction)
getTouchFeedback(touchType)

// Styling Utilities
spacing(value)           // Convert to spacing unit
withOpacity(color, percent) // Add opacity to color
responsiveFontSize(mobile, tablet, desktop) // Responsive typography
```

---

## 9. Layout Specifications

**From**: `UX_LAYOUT_DESCRIPTION.md`

These specifications serve as reference for designing tool interfaces. Apply these patterns when creating:
- Tool headers and navigation areas
- Main content and preview regions
- Control panels and options sidebars
- Action button layouts
- Modal and dialog patterns

**Key Layout Principles**:
- Fixed headers/footers for persistent navigation (56px+)
- Main content area: 60-70% width, secondary controls: 30-40%
- Responsive collapse to stacked layout at 768px breakpoint
- Consistent spacing using 8px grid system
- Visual hierarchy through color, size, and position
- Micro-interactions and feedback for user actions

---

## 10. Design Principles & Laws Applied

### UX Laws Implemented
1. **Fitts's Law** → Touch target minimums
2. **Doherty Threshold** → Response time targets
3. **Miller's Law** → Information chunking
4. **Law of Proximity** → Spacing relationships
5. **Law of Prägnanz** → Typography simplicity
6. **Von Restorff Effect** → Visual hierarchy
7. **Postel's Law** → Form robustness
8. **Law of Similarity** → Consistent button styles
9. **60-30-10 Rule** → Color system

---

## 11. Tool Attractiveness Audit Checklist

Use this checklist when auditing new tools for implementation:

### Response & Feedback
- [ ] All interactions respond in <400ms (Doherty threshold)
- [ ] Visual feedback on all clickable elements (hover, active states)
- [ ] Loading indicators visible at 1000ms+
- [ ] Success/error feedback is clear and immediate
- [ ] Animations use appropriate easing from uxAnimations

### Touch & Interaction
- [ ] Min touch targets: 44px mobile, 24px desktop
- [ ] Adequate spacing between interactive elements
- [ ] Focus states visible on keyboard navigation
- [ ] Gestures supported on mobile (swipe, tap)
- [ ] Cursor changes appropriate (pointer, not-allowed, etc.)

### Content Organization
- [ ] Information chunked in groups of 5-7 items
- [ ] Clear visual hierarchy with 60-30-10 color rule
- [ ] Max 7 navigation items before submenus
- [ ] Consistent spacing using 8px grid

### Visual Design
- [ ] Typography: max 2-3 weights per section
- [ ] Colors: 60% neutral, 30% brand, 10% accent CTA
- [ ] Border radius consistent across components
- [ ] Opacity levels follow hierarchy (disabled 0.3, muted 0.5, etc.)
- [ ] Shadows create depth hierarchy

### Mobile & Responsive
- [ ] Mobile-first approach: design for small screens first
- [ ] Responsive breakpoints: 768px (tablet), 1024px (desktop)
- [ ] Touch targets remain minimum 44px on all devices
- [ ] Layout stacks/reflows appropriately
- [ ] Thumb zones: primary actions in reach zone

### Accessibility & Standards
- [ ] Color contrast: WCAG AA minimum 4.5:1
- [ ] All buttons have aria-labels or visible text
- [ ] Focus rings visible and colored (#f59e0b focus color)
- [ ] Max line width: 60-80 characters for readability
- [ ] Semantic HTML used (button, input, etc.)

### Emotional Design
- [ ] Micro-interactions delight users
- [ ] Success states celebrated (color change, animation)
- [ ] Error states are helpful, not punishing
- [ ] Loading states feel purposeful
- [ ] Overall feel matches product personality

---

## 12. File Reference Guide

All content is consolidated into root-level files:

| File | Purpose | Key Exports |
|--------|---------|-------------|
| **`UX_DESIGN_SYSTEM.js`** | **MAIN ENTRY POINT** | **All consolidated exports - import from here** |
| **`UX_DESIGN_SYSTEM.md`** | **This document** | Master reference & audit checklist |

### Sections within `UX_DESIGN_SYSTEM.js`

| Section | Purpose | Key Exports |
|---------|---------|-------------|
| Core Constants | Design tokens | Spacing, colors, typography, touch targets |
| Animations & Motion | Motion & animation | Easing, springs, haptic rules, sound specs |
| Mobile Optimizations | Mobile design | Thumb zones, gestures, screen priorities |
| Progress Indicators | Progress & Zeigarnik | Progress rules, messaging, triggers |
| Emotional Design | Emotion framework | Core emotion, feedback patterns |
| Social Proof | Social patterns | Display types, proof patterns |
| Layout Patterns | Layout specs | Vertical rhythm, breakpoints, widths |
| Helper Functions | Utilities | Spacing, styling, responsive helpers |
| Engagement Patterns (P1-P12) | User engagement specs | P1-P12 constants, user responsiveness, metrics |
| Session Design | Session architecture | 11-min phases, event timestamps, hooks |
| Neuro-Aesthetic Parameters | Sensory design specs | Colors, audio frequencies, haptic, environmental |

---

## Notes for Implementation

1. **Always import from main entry point** (`UX_DESIGN_SYSTEM.js`) for convenience
2. **Use named imports** for better tree-shaking and clarity
3. **Reference this master document** when implementing features
4. **Test on mobile** to ensure touch targets and gestures work
5. **Verify animations** complete within Doherty threshold
6. **Validate color contrast** against WCAG AA standards

### Consolidated Modules (all in `UX_DESIGN_SYSTEM.js`)
- **Engagement Patterns (P1-P12)**: User responsiveness multipliers, metrics per pattern
- **Session Architecture**: 11-minute reward curves, critical event timestamps, return hooks
- **Neuro-Aesthetic**: Color wavelengths, audio frequencies, haptic durations, sensory timing

---

## Quick Implementation Guide

### Creating a Button
```javascript
import { TOUCH_TARGETS, SPACING, TYPOGRAPHY, COLORS } from './UX_DESIGN_SYSTEM';

const buttonStyle = {
  minHeight: TOUCH_TARGETS.MEDIUM,        // 44px
  padding: `${SPACING.MD} ${SPACING.XL}`, // 12px 24px
  fontSize: TYPOGRAPHY.BASE,               // 14px
  fontWeight: TYPOGRAPHY.SEMIBOLD,         // 600
  borderRadius: '12px',
  backgroundColor: COLORS.ACCENT.CTA,      // Orange
  color: 'white',
};
```

### Creating Responsive Spacing
```javascript
import { SPACING } from './UX_DESIGN_SYSTEM';

const containerStyle = {
  padding: SPACING.XL,        // 24px
  marginBottom: SPACING['2XL'], // 32px
  gap: SPACING.LG,            // 16px
};
```

### Mobile-First Approach
```javascript
import { BREAKPOINTS } from './UX_DESIGN_SYSTEM';

const responsiveStyle = {
  width: '100%',
  padding: SPACING.SM,
  '@media (min-width: 768px)': {
    width: '50%',
    padding: SPACING.MD,
  },
  '@media (min-width: 1024px)': {
    width: '33%',
    padding: SPACING.LG,
  },
};
```

