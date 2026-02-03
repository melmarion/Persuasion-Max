/**
 * UX Design System - Consolidated Master File
 *
 * Single import source for all UX design tokens, patterns, and utilities.
 * Use this for all UX implementations and tool attractiveness audits.
 *
 * Usage:
 *   import { TOUCH_TARGETS, SPACING, COLORS, EASING, ... } from './UX_DESIGN_SYSTEM';
 *
 * Also exports engagement patterns, session design, and neuro-aesthetic specs:
 *   import { P1_VARIABLE_REWARD, SESSION_PHASES, COLOR_WAVELENGTHS, ... } from './UX_DESIGN_SYSTEM';
 */

// ============================================
// CORE CONSTANTS (UX Laws & Design Tokens)
// ============================================

// Fitts's Law - Touch Target Sizes
export const TOUCH_TARGETS = {
  MOBILE_MIN: 44,
  DESKTOP_MIN: 24,
  SMALL: 36,
  MEDIUM: 44,
  LARGE: 48,
  XLARGE: 56,
};

// Doherty Threshold - Response Times
export const RESPONSE_TIMES = {
  INSTANT: 0,
  FAST: 100,
  IDEAL: 400,
  ACCEPTABLE: 1000,
  SLOW: 2000,
};

// Miller's Law - Information Chunking
export const CHUNK_LIMITS = {
  NAVIGATION_MAX: 7,
  OPTIONS_PER_GROUP: 7,
  FORM_FIELDS_PER_STEP: 7,
  LIST_ITEMS_BEFORE_PAGINATION: 9,
};

export const BASE = 8; // Base unit for 8px grid system

// Law of Proximity - Spacing System
export const SPACING = {
  1: '8px',
  2: '16px',
  3: '24px',
  4: '32px',
  5: '40px',
  6: '48px',
  8: '64px',
  10: '80px',
  12: '96px',
  XS: '4px',
  SM: '8px',
  MD: '12px',
  LG: '16px',
  XL: '24px',
  '2XL': '32px',
  '3XL': '48px',
  '4XL': '64px',
  '5XL': '80px',
};

// Law of Prägnanz - Typography Scale
export const TYPOGRAPHY = {
  XS: '10px',
  SM: '12px',
  BASE: '14px',
  MD: '16px',
  LG: '18px',
  XL: '24px',
  '2XL': '32px',
  '3XL': 'clamp(32px, 5vw, 48px)',
  '4XL': 'clamp(48px, 6vw, 72px)',
  NORMAL: 400,
  MEDIUM: 500,
  SEMIBOLD: 600,
  BOLD: 700,
  TIGHT: 1.1,
  NORMAL_LH: 1.5,
  RELAXED: 1.6,
  MAX_LINE_WIDTH: '60-80ch',
};

// Von Restorff Effect - Visual Hierarchy
export const HIERARCHY = {
  Z_BASE: 1,
  Z_DROPDOWN: 100,
  Z_MODAL: 1000,
  Z_TOAST: 10000,
  DISABLED: 0.3,
  MUTED: 0.5,
  SUBTLE: 0.7,
  NORMAL: 1.0,
};

// Icon Sizes (Fitts's Law)
export const ICON_SIZES = {
  XS: 12,
  SM: 16,
  MD: 20,
  LG: 24,
  XL: 32,
  '2XL': 48,
};

// 60-30-10 Color Rule - Von Restorff Effect
export const COLORS = {
  NEUTRAL: {
    BG: '#0a0a0f',
    SURFACE: '#0f1419',
    TEXT: 'rgba(255,255,255,0.9)',
    MUTED: 'rgba(255,255,255,0.5)',
    SUBTLE: 'rgba(255,255,255,0.3)',
  },
  BRAND: {
    PRIMARY: '#8b5cf6',
    LIGHT: 'rgba(139, 92, 246, 0.2)',
    DARK: '#6d28d9',
  },
  ACCENT: {
    CTA: '#f59e0b',
    CTA_HOVER: '#d97706',
  },
  SUCCESS: '#10b981',
  ERROR: '#ef4444',
  WARNING: '#f59e0b',
  INFO: '#3b82f6',
};

// Form Elements (Postel's Law)
export const FORM = {
  INPUT_PADDING: '12px 12px',
  INPUT_MIN_HEIGHT: 44,
  INPUT_BORDER_RADIUS: '8px',
  LABEL_MARGIN_BOTTOM: '8px',
  FIELD_GAP: '12px',
  GROUP_GAP: '24px',
};

// Common Patterns
export const PATTERNS = {
  CARD_PADDING: '24px',
  CARD_BORDER_RADIUS: '12px',
  CARD_GAP: '12px',
  MODAL_PADDING: '32px',
  MODAL_BORDER_RADIUS: '16px',
  MODAL_MAX_WIDTH: '600px',
  SECTION_GAP: '32px',
  SECTION_PADDING: '48px 24px',
  RADIUS: {
    SM: '4px',
    MD: '8px',
    LG: '12px',
    XL: '16px',
    FULL: '999px',
  },
};

// Accessibility
export const A11Y = {
  FOCUS_RING: '0 0 0 2px rgba(245, 158, 11, 0.4)',
  FOCUS_RING_OFFSET: '2px',
  MIN_CONTRAST_RATIO: 4.5,
  LARGE_TEXT_CONTRAST: 3.0,
};

export const getButtonStyles = () => ({
  PRIMARY: {
    minHeight: 44,
    padding: '12px 24px',
    fontSize: '14px',
    fontWeight: 600,
  },
  SECONDARY: {
    minHeight: 44,
    padding: '12px 24px',
    fontSize: '14px',
    fontWeight: 500,
  },
  TERTIARY: {
    minHeight: 36,
    padding: '12px 24px',
    fontSize: '12px',
    fontWeight: 500,
  },
  ICON_ONLY: {
    minWidth: 44,
    minHeight: 44,
    padding: '8px',
  },
});

// ============================================
// ANIMATIONS & MOTION
// ============================================

export const EASING = {
  DEFAULT: 'cubic-bezier(0.4, 0.0, 0.2, 1.0)',
  EASE_OUT: 'cubic-bezier(0.0, 0.0, 0.2, 1.0)',
  EASE_IN: 'cubic-bezier(0.4, 0.0, 1.0, 1.0)',
  SHARP: 'cubic-bezier(0.4, 0.0, 0.6, 1.0)',
  EMPHASIZED: 'cubic-bezier(0.0, 0.0, 0.2, 1.0)',
};

export const SPRINGS = {
  snappy: {
    damping: 20,
    stiffness: 300,
    mass: 0.5
  },
  smooth: {
    damping: 30,
    stiffness: 300,
    mass: 1
  },
  bouncy: {
    damping: 15,
    stiffness: 150,
    mass: 1
  },
  heavy: {
    damping: 25,
    stiffness: 200,
    mass: 2
  }
};

export const TIMINGS = {
  immediate: 100,
  responsive: 200,
  acceptable: 300,
  noticeable: 500,
  frustrating: 1000
};

export const DURATIONS = {
  microInteraction: 150,
  transition: 300,
  reveal: 400,
  emphasis: 500
};

export const calculateDuration = (distancePx) => {
  const baseSpeed = 500;
  const minDuration = 200;
  const maxDuration = 600;
  const calculated = (distancePx / baseSpeed) * 1000;
  return Math.max(minDuration, Math.min(maxDuration, calculated));
};

export const HAPTIC_RULES = {
  buttonPress: { type: 'impactMedium', timing: 'onPressIn' },
  toggle: { type: 'selection', timing: 'onChange' },
  pullToRefresh: {
    type: 'impactHeavy',
    timing: 'onThresholdCross',
    threshold: 88
  },
  taskComplete: {
    type: 'notificationSuccess',
    timing: 'afterAPIConfirm',
    delay: 200
  },
  scrollSnap: {
    type: 'impactLight',
    timing: 'onSnapAlign',
    throttle: 100
  }
};

export const getHapticStyle = (elementSize) => {
  if (elementSize < 44) return 'impactLight';
  if (elementSize < 88) return 'impactMedium';
  return 'impactHeavy';
};

export const SOUND_SPECS = {
  success: {
    frequency1: 880,
    frequency2: 1320,
    duration: 150,
    envelope: 'ADSR(5, 20, 0.6, 125)'
  },
  tap: {
    frequency: 1300,
    duration: 10,
    envelope: 'ADSR(1, 3, 0, 6)'
  },
  error: {
    frequency: 250,
    duration: 200,
    envelope: 'ADSR(5, 40, 0.4, 155)'
  }
};

export const calibrateVolume = (systemVolume) => {
  const targetDB = -20;
  return systemVolume * Math.pow(10, targetDB / 20);
};

export const HARMONIOUS_RATIOS = {
  octave: 2/1,
  perfectFifth: 3/2,
  perfectFourth: 4/3,
  majorThird: 5/4,
};

export const getAnimationParams = (elementSize) => {
  const area = elementSize.width * elementSize.height;
  const mass = Math.sqrt(area) / 100;

  return {
    damping: 20 + (mass * 2),
    stiffness: 300 - (mass * 20),
    mass: mass,
    duration: 200 + (mass * 30)
  };
};

// ============================================
// MOBILE OPTIMIZATIONS
// ============================================

export const THUMB_ZONES = {
  natural: {
    area: 'bottom-center to bottom-right',
    coordinates: { x: '50-100%', y: '75-100%' },
    effort: 'zero-strain'
  },
  stretch: {
    area: 'middle-right',
    coordinates: { x: '70-100%', y: '40-75%' },
    effort: 'slight-strain'
  },
  awkward: {
    area: 'top-left',
    coordinates: { x: '0-30%', y: '0-25%' },
    effort: 'reposition-required'
  }
};

export const BUTTON_SIZES = {
  primary: {
    width: 88,
    height: 55,
    placement: 'THUMB_ZONES.natural'
  },
  secondary: {
    width: 55,
    height: 44,
    placement: 'THUMB_ZONES.stretch'
  },
  destructive: {
    width: 44,
    height: 44,
    placement: 'THUMB_ZONES.awkward'
  }
};

export const MIN_TOUCH_TARGET = 44;

export const GESTURE_SHORTCUTS = {
  delete: 'swipe-left',
  archive: 'swipe-right',
  refresh: 'pull-down',
  dismiss: 'swipe-down'
};

export const SCREEN_PRIORITIES = {
  primaryAction: {
    size: 'large',
    text: 'Continue Your Streak',
    placement: 'center-top'
  },
  secondaryActions: {
    size: 'small',
    text: ['Browse', 'Settings'],
    placement: 'bottom'
  },
  tertiaryActions: {
    location: 'hamburger-menu'
  }
};

export const coreUserJourney = [
  'Open app',
  'Navigate to main feature',
  'Complete primary action',
  'View result',
  'Exit'
];

// ============================================
// PROGRESS INDICATORS (Zeigarnik Effect)
// ============================================

export const PROGRESS = {
  BAR_HEIGHT: '8px',
  BAR_BORDER_RADIUS: '999px',
  BAR_BACKGROUND: 'rgba(255, 255, 255, 0.08)',
  BAR_FILL: 'rgba(139, 92, 246, 0.9)',
  TRANSITION: 'width 200ms ease',
};

export const PROGRESS_MESSAGING = (percent) => {
  if (percent < 50) {
    return "You're making progress!";
  } else if (percent >= 50 && percent < 80) {
    return "Halfway there!";
  } else if (percent >= 80 && percent < 95) {
    return "So close! Just a bit more!";
  } else if (percent >= 95) {
    return "Almost perfect! Finish now!";
  }
  return "Keep going!";
};

export const PROGRESS_LAYERS = {
  daily: {
    goal: 'Complete 1 task',
    resets: 'Every 24 hours',
    urgency: 'HIGH (today only)'
  },
  weekly: {
    goal: 'Complete 5 days this week',
    resets: 'Every Monday',
    urgency: 'MEDIUM (this week)'
  },
  monthly: {
    goal: 'Hit 20-day streak',
    resets: 'Never (accumulates)',
    urgency: 'LOW (long-term)'
  },
  lifetime: {
    goal: 'Reach Level 50',
    resets: 'Never',
    urgency: 'BACKGROUND'
  }
};

export const PROGRESS_FORMATS = {
  percentage: 'percentage',
  bar: 'bar',
  fraction: 'fraction',
  checklist: 'checklist',
  level: 'level'
};

export const THRESHOLD_RULES = {
  goodThresholds: [10, 25, 50, 75, 100, 150, 250],
  badThresholds: [100, 500, 1000, 5000],
  maxDistancePercent: 20
};

export const NOTIFICATION_TRIGGERS = {
  daily: {
    time: '8:00 PM',
    condition: 'dailyProgress < 100%',
    message: 'You\'re at 67%! Just one task to complete your day 🎯'
  },
  weekly: {
    day: 'Sunday 6:00 PM',
    condition: 'weeklyProgress >= 80%',
    message: 'You\'re SO close to your weekly goal! 1 more day 🔥'
  },
  streak: {
    time: '9:00 PM',
    condition: 'todayIncomplete && streakCount >= 3',
    message: 'Don\'t lose your streak! 🚨 (5 min to complete)'
  }
};

// ============================================
// EMOTIONAL DESIGN
// ============================================

export const CORE_EMOTION = {
  options: [
    'Calm/Peace',
    'Energy/Excitement',
    'Confidence/Empowerment',
    'Joy/Playfulness',
    'Trust/Security',
    'Focus/Flow'
  ],
  yourApp: 'CHOOSE ONE',
};

export const EMOTIONAL_DESIGN = {
  calm: {
    colors: ['#E8F4F8', '#B8D4E0', '#7AB8D4'],
    animations: { speed: 'slow', easing: 'ease-out', duration: 600 },
    sounds: { frequency: '200-400Hz', volume: -25 },
    typography: { weight: 300, spacing: 1.6 },
    spacing: { density: 'loose', padding: '×1.5' }
  },
  energetic: {
    colors: ['#FF6B35', '#F7931E', '#FDC70D'],
    animations: { speed: 'fast', easing: 'bounce', duration: 200 },
    sounds: { frequency: '800-1500Hz', volume: -15 },
    typography: { weight: 700, spacing: 1.2 },
    spacing: { density: 'tight', padding: '×0.75' }
  },
  trustworthy: {
    colors: ['#0A2E4D', '#1E5A8E', '#5B9BD5'],
    animations: { speed: 'medium', easing: 'linear', duration: 300 },
    sounds: { frequency: '400-600Hz', volume: -20 },
    typography: { weight: 500, spacing: 1.4 },
    spacing: { density: 'structured', padding: '×1' }
  }
};

export const ONBOARDING_EMOTION_SEQUENCE = [
  {
    screen: 'splash',
    duration: 2000,
    emotion: 'anticipation',
    technique: 'Slow fade-in with ambient sound'
  },
  {
    screen: 'welcome',
    duration: 3000,
    emotion: 'warmth',
    technique: 'Friendly illustration + welcoming copy'
  },
  {
    screen: 'value-prop',
    duration: 4000,
    emotion: 'confidence',
    technique: 'Show social proof + clear benefit'
  }
];

export const EMOTIONAL_FEEDBACK = {
  buttonPress: {
    calm: 'Gentle scale(0.95) with soft haptic',
    energetic: 'Bounce scale(1.1) with sharp haptic',
    trustworthy: 'Firm scale(0.98) with medium haptic'
  },
  success: {
    calm: 'Soft glow fadeIn, low chime',
    energetic: 'Confetti burst, bright sound',
    trustworthy: 'Checkmark slide, confirmation tone'
  },
  loading: {
    calm: 'Breathing circle (slow pulse)',
    energetic: 'Spinning dots (fast)',
    trustworthy: 'Progress bar (linear)'
  }
};

export const AUDIO_IDENTITY = {
  calmApp: {
    baseFrequency: 432,
    timbre: 'soft-sine',
    reverb: 'cathedral',
    volume: -25
  },
  energeticApp: {
    baseFrequency: 880,
    timbre: 'bright-square',
    reverb: 'room',
    volume: -15
  }
};

export const emotionalAudit = (targetEmotion) => {
  return [
    `Does this color make me feel ${targetEmotion}?`,
    `Does this animation speed match ${targetEmotion}?`,
    `Does this copy tone convey ${targetEmotion}?`,
    `Would I describe this screen as ${targetEmotion}?`
  ];
};

// ============================================
// SOCIAL PROOF
// ============================================

export const SOCIAL_PROOF_DISPLAYS = {
  liveUsers: '3,421 people using this now',
  liveActivity: '127 items created in the last hour',
  trending: '🔥 Most popular today',
  velocity: '+18 new members this week'
};

export const PROOF_TYPES = {
  realTime: {
    strength: 10,
    examples: ['23 viewing now', '5 people just did this']
  },
  specific: {
    strength: 8,
    examples: ['10,482 users', 'Sarah and 12 others']
  },
  vague: {
    strength: 5,
    examples: ['Thousands of users', 'Popular choice']
  },
  none: {
    strength: 0,
    examples: ['No social indicators']
  }
};

// ============================================
// LAYOUT PATTERNS
// ============================================

export const VERTICAL_RHYTHM = {
  HERO: {
    height: '80vh',
    width: '100%',
    type: 'large'
  },
  DEMO: {
    height: 'auto',
    width: 'contained',
    type: 'small'
  },
  TRANSFORMATION: {
    height: 'auto',
    width: '100%',
    type: 'large'
  },
  IDENTITY_HOOK: {
    height: 'auto',
    width: 'contained',
    type: 'small'
  }
};

export const OPTICAL_GUIDE = {
  HEADLINE: {
    maxWidth: '600px',
    alignment: 'left'
  },
  DESCRIPTION: {
    maxWidth: '500px',
    alignment: 'left'
  },
  CTA: {
    maxWidth: 'auto',
    alignment: 'left',
    whiteSpace: 'nowrap'
  }
};

export const CONTAINER_WIDTHS = {
  SM: '640px',
  MD: '768px',
  LG: '1024px',
  XL: '1280px',
  FULL: '100%'
};

export const BREAKPOINTS = {
  SM: '640px',
  MD: '768px',
  LG: '1024px',
  XL: '1280px',
  '2XL': '1536px'
};

// ============================================
// HELPER FUNCTIONS
// ============================================

export const getProgressPercent = (completed, total) => {
  if (total === 0) return 0;
  return Math.round((completed / total) * 100);
};

export const shouldShowProgress = (items, maxItems = CHUNK_LIMITS.LIST_ITEMS_BEFORE_PAGINATION) => {
  return items.length > maxItems;
};

export const getChunkedItems = (items, chunkSize = CHUNK_LIMITS.OPTIONS_PER_GROUP) => {
  const chunks = [];
  for (let i = 0; i < items.length; i += chunkSize) {
    chunks.push(items.slice(i, i + chunkSize));
  }
  return chunks;
};

export const getScrollPhysics = (contentHeight) => {
  const viewportHeight = typeof window !== 'undefined' ? window.innerHeight : 800;
  const scrollableDistance = contentHeight - viewportHeight;
  const mass = Math.min(scrollableDistance / 1000, 5);

  return {
    damping: 20 + (mass * 2),
    stiffness: 300 - (mass * 20),
    mass: mass
  };
};

export const getTouchFeedback = (elementSize) => {
  if (elementSize < 44) return { haptic: 'light', scale: 0.95 };
  if (elementSize < 88) return { haptic: 'medium', scale: 0.98 };
  return { haptic: 'heavy', scale: 0.99 };
};

export const spacing = (multiplier) => {
  return `${BASE * multiplier}px`;
};

export const withOpacity = (color, opacity) => {
  if (color.startsWith('#')) {
    const r = parseInt(color.slice(1, 3), 16);
    const g = parseInt(color.slice(3, 5), 16);
    const b = parseInt(color.slice(5, 7), 16);
    return `rgba(${r}, ${g}, ${b}, ${opacity})`;
  }
  return color;
};

export const responsiveFontSize = (minSize, maxSize, viewportWidth = '5vw') => {
  return `clamp(${minSize}px, ${viewportWidth}, ${maxSize}px)`;
};

// ============================================
// ENGAGEMENT PATTERNS (P1-P12)
// Based on ENGAGEMENT_PATTERNS_P1_P12.md and
// CROSS_PATTERN_INTERACTION_MAPS.md
// ============================================

// PATTERN 1: Variable Reward Scheduling
export const P1_VARIABLE_REWARD = {
  name: 'Variable Reward Scheduling',
  description: 'Unpredictable rewards create stronger engagement than predictable ones',

  constants: {
    ANTICIPATION_WINDOW: { min: 200, max: 400 },
    ANTICIPATION_STRETCH: 70,
    HIT_FREQUENCY: 0.198,
    BONUS_TRIGGER: 37,
    REWARD_DISTRIBUTION: {
      micro: 0.50,
      standard: 0.35,
      major: 0.12,
      legendary: 0.03
    }
  },

  appliedTo: [
    'Slot machines: 19.8% hit frequency',
    'Loot boxes: 0.07% rare drop rates',
    'Social notifications: clustered batches',
    'Mobile games: cascade bonuses at 30% rate'
  ],

  triggers: [
    'Time elapsed (anticipation window)',
    'User action (spin/pull/open)',
    'Algorithmic probability (BONUS_TRIGGER)'
  ],

  metrics: {
    animationDuration: {
      '3s': { repeatPurchaseRate: 0.12 },
      '5s': { repeatPurchaseRate: 0.18 },
      '8s': { repeatPurchaseRate: 0.23 },
      '12s': { repeatPurchaseRate: 0.19, note: 'Abandonment' }
    },
    anticipationWindow: {
      '100ms': { conversionRate: 0.08 },
      '200ms': { conversionRate: 0.14 },
      '400ms': { conversionRate: 0.22 },
      '600ms': { conversionRate: 0.18 }
    },
    soundDesign: {
      noAudio: { repeatPurchaseRate: 0.11 },
      genericAudio: { repeatPurchaseRate: 0.16 },
      optimizedAudio: { repeatPurchaseRate: 0.24 },
      audioWithHaptic: { repeatPurchaseRate: 0.31 }
    },
    revenueImpact: {
      totalMarket: '$1.62B',
      packPurchasesRevenue: 0.78,
      averagePacksPerUserPerYear: 847,
      totyDropRate: 0.0007,
      averageSpendForToty: '$2,400'
    },
    engagementVsFixed: 3.2,
    averageAnimationDuration: '6.8s',
    youthEngagementRate: 0.40
  }
};

// PATTERN 2: Progress Momentum
export const P2_PROGRESS_MOMENTUM = {
  name: 'Progress Momentum',
  description: 'Near-successes generate continued engagement through reward-like activation',

  constants: {
    OPTIMAL_RATE: 0.30,
    DOPAMINE_RATIO: 1.20,
    CUMULATIVE_PROGRESS: 3
  },

  appliedTo: [
    'Slot machines: "almost there" displays',
    'Mobile games: "one move away" board states',
    'Learning apps: "almost had it" feedback',
    'Progress bars: fill on unsuccessful attempts'
  ],

  triggers: [
    'Outcome within visible range of success',
    'Consistent rate maintained (30% of attempts)'
  ],

  metrics: {
    dopamineResponse: 1.20,
    engagementExtension: 0.22,
    sessionContinuation: 0.89
  }
};

// PATTERN 3: Encouraging Feedback
export const P3_ENCOURAGING_FEEDBACK = {
  name: 'Encouraging Feedback',
  description: 'Positive reinforcement for partial progress and effort',

  uiSpecifications: {
    successColor: '#10b981',
    celebrationAnimation: 'pulse',
    celebrationDuration: '300-500ms',
    feedbackMessage: 'encouraging',
    soundDesign: 'positive-tone',
    hapticFeedback: 'light-impact'
  },

  appliedTo: [
    'Sub-win celebrations',
    'Positive framing of incomplete actions',
    'Milestone recognition'
  ]
};

// PATTERN 4: Progress Protection
export const P4_PROGRESS_PROTECTION = {
  name: 'Progress Protection',
  description: 'Preservation of accumulated progress to prevent loss aversion',

  uiSpecifications: {
    protectionColor: '#fbbf24',
    protectionIcon: 'shield',
    preservationMessage: 'Your progress is safe',
    lossAversionThreshold: 0.80
  },

  appliedTo: [
    'Streak preservation',
    'Loss aversion mechanics',
    'Progress bar safety nets'
  ]
};

// PATTERN 5: Investment Recognition
export const P5_INVESTMENT_RECOGNITION = {
  name: 'Investment Recognition',
  description: 'Display and acknowledge user sunk costs to increase commitment',

  uiSpecifications: {
    investmentColor: '#8b5cf6',
    displayType: 'cumulative-stats',
    recognitionMessage: 'You\'ve invested X hours/currency',
    sunkCostDisplay: true
  },

  appliedTo: [
    'Sunk cost display',
    'Benefit enumeration',
    'Time/money invested counters'
  ]
};

// PATTERN 6: Timely Opportunities
export const P6_TIMELY_OPPORTUNITIES = {
  name: 'Timely Opportunities',
  description: 'Time-limited offers and scarcity mechanics',

  uiSpecifications: {
    urgencyColor: '#f59e0b',
    countdownDisplay: true,
    countdownDuration: '15min-24h',
    urgencyMessage: 'Limited time offer',
    scarcityMessage: 'Only X left'
  },

  appliedTo: [
    'Scarcity messaging',
    'Urgency timers',
    'Countdown displays',
    'Limited inventory'
  ]
};

// PATTERN 7: Contextual Offers
export const P7_CONTEXTUAL_OFFERS = {
  name: 'Contextual Offers',
  description: 'Emotion-timed offers and failure recovery mechanics',

  uiSpecifications: {
    triggerContext: 'post-loss',
    recoveryColor: '#10b981',
    recoveryMessage: 'Try again with help',
    emotionTimingWindow: '30-120s',
    adolescentEngagementMultiplier: 3.2
  },

  appliedTo: [
    'Emotion-timed offers',
    'Failure recovery',
    'Loss-triggered incentives'
  ]
};

// PATTERN 8: Immersive Experience
export const P8_IMMERSIVE_EXPERIENCE = {
  name: 'Immersive Experience',
  description: 'Flow state induction and time suppression',

  uiSpecifications: {
    flowStateIndicators: {
      timePerception: 'suppressed',
      environmentalFocus: 'maximized',
      distractionMinimization: 'enabled',
      contextualConsistency: 'high'
    },
    adolescentAverageDuration: '95 min',
    flowStateActivation: 'seamless-progression'
  },

  appliedTo: [
    'Flow state creation',
    'Time suppression',
    'Continuous engagement loops'
  ]
};

// PATTERN 9: Personalized Tiers
export const P9_PERSONALIZED_TIERS = {
  name: 'Personalized Tiers',
  description: 'Tiered engagement based on user spending and responsiveness',

  uiSpecifications: {
    tieringColor: '#8b5cf6',
    tierDisplay: 'visible-hierarchy',
    whaleTierMultiplier: 8.2,
    targetingBasis: 'spending-patterns'
  },

  appliedTo: [
    'Whale targeting',
    'Spend-based pricing',
    'VIP tiers'
  ]
};

// PATTERN 10: Community Activity
export const P10_COMMUNITY_ACTIVITY = {
  name: 'Community Activity',
  description: 'Social proof through activity displays and social signals',

  uiSpecifications: {
    proofType: 'real-time-activity',
    displayFormat: 'live-user-count',
    updateFrequency: '3-5s',
    examples: [
      '23 people viewing now',
      '5 people just completed this',
      '127 items created this hour'
    ]
  },

  appliedTo: [
    'Live user displays',
    'Activity feeds',
    'Real-time notifications'
  ]
};

// PATTERN 11: Community Connection
export const P11_COMMUNITY_CONNECTION = {
  name: 'Community Connection',
  description: 'Group pressure and reciprocity through peer relationships',

  uiSpecifications: {
    connectionType: 'social-proof',
    peerInfluenceBoost: 0.45,
    identityLinkingBoost: 0.67,
    communityValidationBoost: 0.38
  },

  appliedTo: [
    'Group pressure mechanisms',
    'Reciprocity triggers',
    'Peer recommendations'
  ]
};

// PATTERN 12: Identity & Achievement
export const P12_IDENTITY_ACHIEVEMENT = {
  name: 'Identity & Achievement',
  description: 'Status labels and milestone systems tied to identity',

  uiSpecifications: {
    achievementColor: '#fbbf24',
    statusDisplay: 'prominent',
    milestoneFormat: 'badge-system',
    adolescentMilestoneEngagement: 2.1,
    adolescentIdentityFormationMultiplier: 2.1
  },

  appliedTo: [
    'Status labels',
    'Achievement badges',
    'Milestone celebrations',
    'Rank displays'
  ]
};

// CROSS-PATTERN INTERACTION MAPS
export const PATTERN_COMBINATIONS = {
  gacha: {
    description: 'Loot box mechanics (P1 + P9 + P6)',
    patterns: ['P1_VARIABLE_REWARD', 'P9_PERSONALIZED_TIERS', 'P6_TIMELY_OPPORTUNITIES'],
    implementation: 'Variable rewards + tiered pricing + scarcity',
    revenueMultiplier: 3.5
  },

  fitness: {
    description: 'Habit formation (P2 + P4 + P12)',
    patterns: ['P2_PROGRESS_MOMENTUM', 'P4_PROGRESS_PROTECTION', 'P12_IDENTITY_ACHIEVEMENT'],
    implementation: 'Near-miss progress + streak protection + identity badges',
    retentionMultiplier: 2.8
  },

  mobile: {
    description: 'Mobile gaming stack (P1 + P3 + P8 + P11)',
    patterns: ['P1_VARIABLE_REWARD', 'P3_ENCOURAGING_FEEDBACK', 'P8_IMMERSIVE_EXPERIENCE', 'P11_COMMUNITY_CONNECTION'],
    implementation: 'Rewards + positive feedback + flow state + social features',
    engagementMultiplier: 4.2
  }
};

// PATTERN RESPONSIVENESS BY USER TYPE
export const USER_PATTERN_RESPONSIVENESS = {
  adolescent: {
    age: '12-17',
    mostResponsive: ['P7', 'P8', 'P11', 'P12'],
    multipliers: {
      P7: 3.2,
      P8: 1.0,
      P11: 1.8,
      P12: 2.1
    },
    avgSessionDuration: '95 min',
    characteristics: [
      'Identity formation stage',
      'Developing prefrontal cortex',
      'Strong peer influence',
      'FOMO particularly strong'
    ]
  },

  highSensitivityReward: {
    name: 'High-Sensitivity Reward Processing',
    mostResponsive: ['P1', 'P2', 'P3', 'P7', 'P9'],
    multipliers: {
      P1: 4.2,
      P2: 3.8,
      P3: 6.1,
      P7: 5.3,
      P9: 8.2
    },
    engagementMetrics: {
      sessionDurationOver3h: 0.34,
      sessionExtensionRate: 0.67,
      investmentIncreaseAttempts: 1.56,
      continuationAfterLoss: 0.78,
      responseLatencyToLossRecovery: '0.3s'
    },
    behavioralSignals: [
      'Dopamine system hyperresponsive',
      'Near-miss effect amplified',
      'Interpret near-miss as progress (89% vs 22% baseline)',
      'Loss continuation seeking (67% vs 8% baseline)',
      'Believe they influence chance outcomes (76%)',
      'Underestimate duration (87%)',
      'Expected value assessment error: -$340 vs -$12 baseline'
    ]
  },

  completionOriented: {
    name: 'Completion-Oriented',
    mostResponsive: ['P2', 'P4', 'P5', 'P6', 'P12'],
    multipliers: {
      P2: 1.0,
      P4: 4.0,
      P5: 4.0,
      P6: 3.0,
      P12: 4.0
    }
  },

  sociallyConnected: {
    name: 'Socially-Connected',
    mostResponsive: ['P8', 'P11', 'P12'],
    multipliers: {
      P8: 4.0,
      P11: 4.0,
      P12: 3.0
    }
  }
};

// ANIMATION SPECIFICATIONS FOR PATTERNS
export const PATTERN_ANIMATIONS = {
  P1_variableRewardReveal: {
    duration: '6.8s',
    easing: 'cubic-bezier(0.4, 0.0, 0.2, 1.0)',
    stages: {
      build: '0-3s',
      anticipation: '3-5s',
      reveal: '5-6.8s'
    }
  },

  P2_nearMissDisplay: {
    duration: '400-600ms',
    easing: 'ease-out',
    visual: 'shake-or-slide-near-alignment'
  },

  P3_encouragementPulse: {
    duration: '300-500ms',
    easing: 'ease-in-out',
    visual: 'subtle-pulse-or-scale'
  },

  P4_progressBar: {
    duration: '200ms',
    easing: 'linear',
    visual: 'smooth-fill'
  },

  P12_achievement: {
    duration: '500-800ms',
    easing: 'bounce',
    visual: 'entrance-celebration'
  }
};

// AUDIO SPECIFICATIONS FOR PATTERNS
export const PATTERN_AUDIO = {
  P1_rewardSound: {
    successFrequency: 880,
    successFrequency2: 1320,
    duration: '150ms',
    envelope: 'ADSR(5, 20, 0.6, 125)'
  },

  P2_nearMissSound: {
    frequency: 440,
    duration: '100ms',
    envelope: 'flat'
  },

  P3_encouragingSound: {
    frequency: 587,
    duration: '150ms',
    tone: 'uplifting'
  },

  P12_achievementSound: {
    baseFrequency: 880,
    triumphant: true,
    duration: '300-500ms'
  }
};

// CONVERSION THRESHOLDS BY PATTERN
export const PATTERN_CONVERSION_THRESHOLDS = {
  P1: {
    optimalAnimationDuration: '8s',
    optimalAnticipationWindow: '400ms',
    targetConversionRate: 0.22
  },
  P2: {
    optimalNearMissRate: 0.30,
    targetEngagementExtension: 0.22
  },
  P6: {
    optimalUrgencyWindow: '15min-24h',
    targetConversionBoost: 0.35
  },
  P7: {
    optimalTriggerWindow: '30-120s',
    targetConversionRate: 0.40
  },
  P9: {
    whaleTierEffectiveness: 8.2
  }
};

// ============================================
// SESSION DESIGN - Temporal Architecture
// Based on SESSION_ARCHITECTURE.md
// ============================================

// 11-MINUTE OPTIMAL SESSION ARC
export const SESSION_PHASES = {
  ENTRY: {
    phase: 'Entry',
    duration: { start: 0, end: 60 },
    durationSeconds: 60,
    rewardProbability: 0.05,
    purpose: 'Low barrier, orientation',
    uiConsiderations: [
      'Minimal loading time',
      'Immediate interaction opportunity',
      'Clear next-action indication'
    ],
    timingNote: 'First 60 seconds critical for retention'
  },

  BUILD: {
    phase: 'Build',
    duration: { start: 60, end: 180 },
    durationSeconds: 120,
    rewardProbability: 0.15,
    purpose: 'Increasing engagement',
    uiConsiderations: [
      'Visible progress accumulation',
      'Incrementally increasing challenge',
      'Positive reinforcement signals'
    ]
  },

  CHALLENGE: {
    phase: 'Challenge',
    duration: { start: 180, end: 360 },
    durationSeconds: 180,
    rewardProbability: 0.25,
    purpose: 'Peak difficulty zone',
    uiConsiderations: [
      'Maintain focus through difficulty',
      'Near-miss feedback (P2)',
      'Progress momentum (P2)'
    ]
  },

  PEAK: {
    phase: 'Peak',
    duration: { start: 360, end: 480 },
    durationSeconds: 120,
    rewardProbability: 0.35,
    purpose: 'Maximum reward density',
    uiConsiderations: [
      'Multiple simultaneous rewards',
      'Celebratory feedback (P3)',
      'Flow state maintained'
    ],
    timingNote: 'Peak engagement window - critical for retention'
  },

  INTEGRATE: {
    phase: 'Integrate',
    duration: { start: 480, end: 600 },
    durationSeconds: 120,
    rewardProbability: 0.20,
    purpose: 'Consolidation',
    uiConsiderations: [
      'Reward consolidation display (P5)',
      'Achievement acknowledgment (P12)',
      'Gradual difficulty reduction'
    ]
  },

  CLOSE: {
    phase: 'Close',
    duration: { start: 600, end: 660 },
    durationSeconds: 60,
    rewardProbability: 0.10,
    purpose: 'Session wrap, hook setup',
    uiConsiderations: [
      'Session summary display',
      'Return hook presentation',
      'Mystery element introduction (P6)'
    ],
    timingNote: 'Set expectation for next session'
  }
};

// SESSION PHASE TIMELINE (minutes)
export const SESSION_TIMELINE = {
  rewardProbabilityByMinute: {
    0: 0.05,
    1: 0.05,
    2: 0.10,
    3: 0.15,
    4: 0.20,
    5: 0.25,
    6: 0.35,
    7: 0.35,
    8: 0.28,
    9: 0.20,
    10: 0.15,
    11: 0.10
  },

  visualization: `
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
  `
};

// CRITICAL EVENT TIMESTAMPS
export const CRITICAL_EVENTS = {
  events: [
    {
      timestamp: '45s',
      seconds: 45,
      event: 'First reward',
      purpose: 'Pattern establishment',
      psychologicalFunction: 'Early reward establishes expectation; prevents abandonment',
      importance: 'CRITICAL'
    },
    {
      timestamp: '120s',
      seconds: 120,
      event: 'Value confirmation',
      purpose: 'Investment validation',
      psychologicalFunction: 'Confirms investment was worthwhile; sunk cost activation',
      importance: 'HIGH'
    },
    {
      timestamp: '240s',
      seconds: 240,
      event: 'Deep engagement reward',
      purpose: 'Peak experience creation',
      psychologicalFunction: 'Major reward during challenge phase; memory anchor',
      importance: 'HIGH'
    },
    {
      timestamp: '400s',
      seconds: 400,
      event: 'Late-session moment',
      purpose: 'Memorable close, return motivation',
      psychologicalFunction: 'Creates peak-end memory for return motivation',
      importance: 'MEDIUM'
    }
  ],

  bySeconds: {
    45: {
      name: 'First Reward',
      phase: 'ENTRY',
      rewardProbability: 0.05,
      messaging: 'Welcome reward - builds expectation'
    },
    120: {
      name: 'Value Confirmation',
      phase: 'BUILD',
      rewardProbability: 0.10,
      messaging: 'Your investment is paying off'
    },
    240: {
      name: 'Deep Engagement Reward',
      phase: 'CHALLENGE',
      rewardProbability: 0.25,
      messaging: 'Major achievement unlocked'
    },
    400: {
      name: 'Late-Session Peak',
      phase: 'PEAK',
      rewardProbability: 0.35,
      messaging: 'Memorable conclusion reward'
    }
  }
};

// RETURN HOOKS
export const RETURN_HOOKS = {
  PREVIEW: {
    hookType: 'Preview',
    example: 'Tomorrow: New challenge available',
    psychologicalMechanism: 'Curiosity, anticipation',
    messaging: 'Tease upcoming content',
    timing: 'Close phase',
    implementation: 'Text notification or banner'
  },

  PROGRESS: {
    hookType: 'Progress',
    example: 'You\'re 80% to next milestone',
    psychologicalMechanism: 'Zeigarnik effect (incomplete tasks)',
    messaging: 'Show proximity to goal',
    timing: 'Close phase',
    implementation: 'Progress bar visualization',
    effectiveness: 'VERY HIGH'
  },

  STREAK: {
    hookType: 'Streak',
    example: 'Day 5 complete',
    psychologicalMechanism: 'Commitment, loss aversion',
    messaging: 'Display current streak count',
    timing: 'Close phase',
    implementation: 'Number badge or counter',
    effectiveness: 'VERY HIGH'
  },

  MYSTERY: {
    hookType: 'Mystery',
    example: 'Something changes at day 7...',
    psychologicalMechanism: 'Information gap curiosity',
    messaging: 'Hint at unrevealed content',
    timing: 'Close phase',
    implementation: 'Teaser text or visual',
    effectiveness: 'HIGH'
  }
};

// HOOK EFFECTIVENESS BY USER TYPE
export const HOOK_EFFECTIVENESS = {
  completionOriented: {
    userType: 'Completion-Oriented',
    hookRanking: {
      'Progress': 'VERY HIGH',
      'Streak': 'VERY HIGH',
      'Preview': 'HIGH',
      'Mystery': 'MODERATE'
    },
    dominantMotive: 'Goal achievement'
  },

  socialOriented: {
    userType: 'Social-Oriented',
    hookRanking: {
      'Streak': 'HIGH',
      'Mystery': 'HIGH',
      'Progress': 'MODERATE',
      'Preview': 'MODERATE'
    },
    dominantMotive: 'Social connection'
  },

  casual: {
    userType: 'Casual',
    hookRanking: {
      'Mystery': 'HIGH',
      'Preview': 'LOW',
      'Streak': 'MODERATE',
      'Progress': 'LOW'
    },
    dominantMotive: 'Variety and novelty'
  }
};

// PHASE-SPECIFIC UI PATTERNS
export const PHASE_UI_PATTERNS = {
  entry: {
    phase: 'ENTRY (0-1 min)',
    goal: 'Minimize friction, establish engagement',
    rewardProbability: 0.05,
    uiElements: [
      'Minimal loading time',
      'Immediate interaction opportunity',
      'Clear next-action indication',
      'Reduced cognitive load'
    ],
    patternApplications: [
      'P8: Immersive experience (start flow state)'
    ],
    colorScheme: 'neutral-welcoming',
    animationIntensity: 'subtle'
  },

  build: {
    phase: 'BUILD (1-3 min)',
    goal: 'Increase engagement incrementally',
    rewardProbability: 0.15,
    uiElements: [
      'Visible progress accumulation',
      'Incrementally increasing challenge',
      'Positive reinforcement signals',
      'Encouraging feedback'
    ],
    patternApplications: [
      'P2: Progress momentum (visible near-miss)',
      'P3: Encouraging feedback'
    ],
    colorScheme: 'brand-primary',
    animationIntensity: 'moderate'
  },

  challenge: {
    phase: 'CHALLENGE (3-6 min)',
    goal: 'Maintain engagement through difficulty',
    rewardProbability: 0.25,
    uiElements: [
      'Difficulty indicators',
      'Near-miss visual feedback',
      'Progress preservation display',
      'Contextual help cues'
    ],
    patternApplications: [
      'P2: Progress momentum (active)',
      'P4: Progress protection (visible safety net)',
      'P7: Contextual offers (if failure occurs)'
    ],
    colorScheme: 'accent-focus',
    animationIntensity: 'high'
  },

  peak: {
    phase: 'PEAK (6-8 min)',
    goal: 'Deliver maximum reward experience',
    rewardProbability: 0.35,
    uiElements: [
      'Multi-layered reward display',
      'Celebration animations',
      'Achievement recognition',
      'Sound/haptic celebration'
    ],
    patternApplications: [
      'P1: Variable reward (major reveal)',
      'P3: Encouraging feedback (celebratory)',
      'P5: Investment recognition'
    ],
    colorScheme: 'accent-celebration',
    animationIntensity: 'intense'
  },

  integrate: {
    phase: 'INTEGRATE (8-10 min)',
    goal: 'Consolidate rewards, acknowledge achievement',
    rewardProbability: 0.20,
    uiElements: [
      'Reward consolidation display',
      'Session stats summary',
      'Achievement badges',
      'Investment summary'
    ],
    patternApplications: [
      'P5: Investment recognition (total display)',
      'P12: Identity & achievement (badge awards)'
    ],
    colorScheme: 'neutral-reflective',
    animationIntensity: 'moderate'
  },

  close: {
    phase: 'CLOSE (10-11 min)',
    goal: 'Set expectation for return, deploy hook',
    rewardProbability: 0.10,
    uiElements: [
      'Session summary',
      'Return hook display',
      'Next-session teaser',
      'Call-to-action gentle'
    ],
    patternApplications: [
      'P6: Timely opportunities (preview window)',
      'Return hooks (all types)',
      'Mystery element'
    ],
    colorScheme: 'neutral-forward-looking',
    animationIntensity: 'subtle'
  }
};

// SESSION ARCHITECTURE TEMPLATES
export const SESSION_TEMPLATES = {
  standardGacha: {
    name: 'Standard Gacha Session',
    duration: 660,
    phases: ['ENTRY', 'BUILD', 'CHALLENGE', 'PEAK', 'INTEGRATE', 'CLOSE'],
    patternFocus: ['P1', 'P3', 'P6', 'P9'],
    expectedRepeats: 3.2
  },

  fitnessHabit: {
    name: 'Fitness Habit Session',
    duration: 300,
    phases: ['ENTRY', 'BUILD', 'CHALLENGE', 'PEAK', 'CLOSE'],
    patternFocus: ['P2', 'P3', 'P4', 'P12'],
    streakProtection: true,
    expectedRepeats: 2.8
  },

  socialExperience: {
    name: 'Social Experience Session',
    duration: 720,
    phases: ['ENTRY', 'BUILD', 'CHALLENGE', 'PEAK', 'INTEGRATE', 'CLOSE'],
    patternFocus: ['P8', 'P10', 'P11'],
    communityElements: true,
    expectedRepeats: 2.5
  }
};

// RETURN HOOK SEQUENCING
export const HOOK_SEQUENCES = {
  day1to3: {
    period: 'Days 1-3',
    primaryHook: 'PROGRESS',
    secondaryHook: 'STREAK',
    messaging: 'Emphasize habit formation'
  },

  day4to7: {
    period: 'Days 4-7',
    primaryHook: 'STREAK',
    secondaryHook: 'MYSTERY',
    messaging: 'Build commitment, tease special unlocks'
  },

  week2plus: {
    period: 'Week 2+',
    primaryHook: 'MYSTERY',
    secondaryHook: 'PREVIEW',
    messaging: 'Maintain novelty, manage retention churn'
  }
};

// PERFORMANCE METRICS BY SESSION STRUCTURE
export const SESSION_PERFORMANCE_METRICS = {
  retention: {
    day1: 0.42,
    day7: 0.18,
    withOptimizedHooks: {
      day1: 0.52,
      day7: 0.28
    }
  },

  sessionLength: {
    targetMinutes: 11,
    adolescentAverage: 95,
    completionOrientedAverage: 12
  },

  peakEngagement: {
    phase: 'PEAK (6-8 min)',
    rewardDensity: 0.35,
    expectedEngagementScore: 0.89
  }
};

// ============================================
// NEURO-AESTHETIC PARAMETERS
// Based on NEURO_AESTHETIC_PARAMETERS.md
// ============================================

// COLOR PARAMETERS - WAVELENGTH SPECIFICATIONS
export const COLOR_WAVELENGTHS = {
  CALMING_BLUE: {
    wavelength: 450,
    hex: '#2563eb',
    psychologicalEffect: 'Calm, trust, reduced anxiety',
    useCase: 'Background, loading states',
    saturation: '20%',
    brightness: '70%'
  },

  RELAXING_BLUE: {
    wavelength: 490,
    hex: '#0891b2',
    psychologicalEffect: 'Relaxed focus, engagement',
    useCase: 'Active UI elements',
    saturation: '25%',
    brightness: '70%'
  },

  WARM_ACCENT: {
    wavelengthRange: '580-620',
    hex: '#f59e0b',
    psychologicalEffect: 'Attention, urgency',
    useCase: 'CTAs, notifications, variable rewards',
    saturation: '30%',
    brightness: '70%'
  },

  NEUTRAL: {
    psychologicalEffect: 'Cognitive rest',
    useCase: 'Content areas, background',
    saturation: '0-10%',
    brightness: '70%'
  }
};

// COLOR PSYCHOLOGY APPLICATION TABLE
export const COLOR_PSYCHOLOGY_MATRIX = {
  deepBlue: {
    wavelength: 450,
    effect: 'Calm, trust, reduced anxiety',
    usage: 'Background, loading states, safe contexts'
  },

  cyanBlue: {
    wavelength: 490,
    effect: 'Relaxed focus, engagement',
    usage: 'Active UI elements, interactive components'
  },

  warmAccent: {
    wavelength: '580-620',
    effect: 'Attention, urgency, reward',
    usage: 'CTAs, notifications, achievements, variable rewards'
  },

  neutral: {
    wavelength: 'N/A',
    effect: 'Cognitive rest, processing space',
    usage: 'Content areas, text backgrounds'
  }
};

// SATURATION GUIDELINES
export const SATURATION_GUIDELINES = {
  background: {
    saturation: '10-15%',
    reasoning: 'Visual comfort, extended use',
    exampleColors: ['#0f1419', '#1f2937']
  },

  secondaryElements: {
    saturation: '20-25%',
    reasoning: 'Subtle differentiation',
    exampleColors: ['#2563eb', '#0891b2']
  },

  primaryElements: {
    saturation: '30%',
    reasoning: 'Attention without fatigue',
    exampleColors: ['#f59e0b', '#10b981']
  },

  alertRewardStates: {
    saturation: '40-50%',
    reasoning: 'Momentary high-attention',
    duration: 'Only for alert moments, not persistent',
    exampleColors: ['#ef4444', '#ec4899']
  }
};

// AUDIO PARAMETERS - FREQUENCY SPECIFICATIONS
export const AUDIO_FREQUENCIES = {
  THETA_WAVE: {
    frequency: 6.0,
    purpose: 'Relaxed focus state induction',
    binaural: false,
    effectDuration: '20-30 min'
  },

  ASMR_FUNDAMENTAL: {
    frequency: 180,
    purpose: 'Pleasant tingling response',
    application: 'Subtle background sounds',
    perceptualEffect: 'Calming, pleasant'
  },

  SCHUMANN_FREQUENCY: {
    frequency: 7.83,
    purpose: 'Earth resonance, grounding',
    application: 'Ambient environmental audio',
    perceptualEffect: 'Natural, grounded'
  },

  BINAURAL_BASE: {
    leftEar: 180,
    rightEar: 186,
    perceivedDifference: 6,
    effect: 'Relaxed focus, reduced critical thinking',
    safetyNote: 'Use only with explicit consent'
  }
};

// BINAURAL BEAT DESIGN
export const BINAURAL_BEAT_CONFIGURATION = {
  leftEar: 180,
  rightEar: 186,
  perceivedFrequency: 6,
  perceptualRange: 'theta',
  psychologicalEffect: 'Relaxed focus, reduced critical thinking',
  safetyConsiderations: [
    'Not recommended for children under 18',
    'Requires explicit user consent',
    'May interfere with medical conditions',
    'Headphones required for binaural effect'
  ]
};

// AUDIO INTENSITY BY ENGAGEMENT PATTERN
export const AUDIO_INTENSITY_BY_PATTERN = {
  P1_VariableReward: {
    pattern: 'P1 (Variable Reward)',
    approach: 'Build + reveal',
    dBRelative: '+6dB peak',
    dynamicsRange: '6dB envelope'
  },

  P2_ProgressMomentum: {
    pattern: 'P2 (Near-miss)',
    approach: 'Similar to win but softer',
    dBRelative: '-3dB from win',
    dynamicsRange: '3dB envelope'
  },

  P3_EncouragingFeedback: {
    pattern: 'P3 (Encouraging)',
    approach: 'Celebration but not peak',
    dBRelative: '-3dB from full win',
    dynamicsRange: 'Uplifting tone'
  },

  P8_ImmersiveExperience: {
    pattern: 'P8 (Immersive)',
    approach: 'Ambient continuity',
    dBRelative: 'Baseline',
    dynamicsRange: 'Subtle, non-intrusive'
  },

  P12_Achievement: {
    pattern: 'P12 (Achievement)',
    approach: 'Triumphant celebration',
    dBRelative: '+3dB from baseline',
    dynamicsRange: 'Fuller frequency range'
  }
};

// SOUND DESIGN METRICS & IMPACT
export const SOUND_DESIGN_IMPACT = {
  repeatPurchaseRates: {
    noAudio: 0.11,
    genericAudio: 0.16,
    optimizedAudio: 0.24,
    audioWithHaptic: 0.31
  },

  improvementMetrics: {
    genericAudioGain: '45%',
    optimizedAudioGain: '118%',
    fullAudioHapticGain: '182%'
  },

  soundDesignRecommendation: 'Optimal audio adds 13-20% to engagement metrics'
};

// HAPTIC PARAMETERS - DURATION SPECIFICATIONS
export const HAPTIC_SPECIFICATIONS = {
  microTap: {
    duration: '10-15ms',
    purpose: 'Subtle feedback, scroll interactions',
    intensity: 'light',
    frequency: 'high (frequent)'
  },

  lightTap: {
    duration: '20-30ms',
    purpose: 'Button press feedback',
    intensity: 'light',
    frequency: 'medium'
  },

  standardImpact: {
    duration: '40-60ms',
    purpose: 'Standard action confirmation',
    intensity: 'medium',
    frequency: 'medium'
  },

  strongPulse: {
    duration: '80-150ms',
    purpose: 'Major event, achievement, error',
    intensity: 'heavy',
    frequency: 'low'
  },

  sustainedVibration: {
    duration: '200-800ms',
    purpose: 'Sustained attention (alerts)',
    intensity: 'medium',
    frequency: 'varying'
  }
};

// HAPTIC INTENSITY MAPPING
export const HAPTIC_INTENSITY_MAPPING = {
  byPattern: {
    P1_variableReward: {
      anticipationPhase: { duration: '50-100ms', intensity: 'light-to-medium' },
      revealPhase: { duration: '100-200ms', intensity: 'heavy' }
    },

    P2_nearMiss: {
      nearMissIndication: { duration: '30-50ms', intensity: 'light' },
      frequency: 'single tap'
    },

    P3_encouragingFeedback: {
      successPulse: { duration: '60-100ms', intensity: 'medium' },
      frequency: 'single pulse'
    },

    P4_progressProtection: {
      protectionConfirmation: { duration: '50-80ms', intensity: 'light-medium' },
      frequency: 'double tap'
    },

    P12_achievement: {
      achievementCelebration: { duration: '100-200ms', intensity: 'heavy' },
      frequency: 'multiple pulses'
    }
  }
};

// MULTI-SENSORY COORDINATION TIMING
export const MULTISENSORY_TIMING = {
  audioToHapticSync: {
    optimalDelay: '0-50ms',
    reasoning: 'Audio and haptic should feel simultaneous to human perception'
  },

  visualToAudioSync: {
    optimalDelay: '0-100ms',
    reasoning: 'Visual event should precede audio (McGuirk effect)'
  },

  visualToHapticSync: {
    optimalDelay: '20-80ms',
    reasoning: 'Visual onset typically 20-80ms before haptic for natural feel'
  },

  fullyCoordinatedReward: {
    visual: 'starts at 0ms',
    audio: 'starts at 50-100ms',
    haptic: 'peaks at 100-150ms',
    totalDuration: '500-800ms'
  }
};

// ANIMATION DURATION RESEARCH
export const ANIMATION_DURATION_RESEARCH = {
  optimalRanges: {
    microInteraction: '100-200ms',
    standardTransition: '300-500ms',
    majorReveal: '600-1000ms',
    celebrationSequence: '1000-2000ms'
  },

  engagementByDuration: {
    '3s_animation': { repeatPurchaseRate: 0.12 },
    '5s_animation': { repeatPurchaseRate: 0.18 },
    '8s_animation': { repeatPurchaseRate: 0.23, note: 'OPTIMAL' },
    '12s_animation': { repeatPurchaseRate: 0.19, note: 'Abandonment increases' }
  },

  keyFinding: 'Optimal animation duration is 6-8 seconds for variable reward reveals'
};

// ENVIRONMENTAL DESIGN CONDITIONS
export const ENVIRONMENTAL_CONDITIONS = {
  lightingConditions: {
    optimalBrightness: '70%',
    recommendation: 'Account for dark mode (reduced brightness)',
    adaptiveColor: true,
    contrastMinimum: '4.5:1'
  },

  temperatureEnvironment: {
    optimalTemperature: '68-72°F (20-22°C)',
    effect: 'Cognitive performance optimization',
    note: 'Consider user location variability'
  },

  seatingPosition: {
    recommendation: 'Seated, device at arm\'s length',
    visionAngle: '20-30 degrees below horizontal',
    effect: 'Reduces eye strain, improves focus'
  },

  audioEnvironment: {
    optimalNoise: '-20dB to -10dB from baseline',
    recommendation: 'Account for variable user environments',
    adaptiveVolume: true,
    maxSPL: '85dB'
  }
};

// TIME PERCEPTION FACTORS
export const TIME_PERCEPTION_FACTORS = {
  factors: [
    {
      factor: 'Attention focus',
      effect: 'Increased focus suppresses time perception',
      implementation: 'P8 (Immersive experience)'
    },
    {
      factor: 'Reward frequency',
      effect: 'More rewards compress perceived time',
      implementation: 'P1 (Variable reward) at peak density'
    },
    {
      factor: 'Environmental consistency',
      effect: 'Monotonous environments feel longer',
      implementation: 'Use environmental variation (P8)'
    },
    {
      factor: 'Flow state',
      effect: 'Time disappears in flow state',
      implementation: 'P8 + multi-pattern stacking'
    },
    {
      factor: 'Audio continuity',
      effect: 'Continuous audio masks time passage',
      implementation: 'Ambient audio design'
    }
  ],

  adolescentSessionDuration: {
    target: '11 minutes',
    actual: '95 minutes',
    timePerceptionGap: '784%',
    note: 'Adolescent brains particularly susceptible to time suppression'
  }
};

// SENSORY DESIGN RECOMMENDATIONS BY CONTEXT
export const SENSORY_CONTEXT_RECOMMENDATIONS = {
  variableRewardP1: {
    visuals: {
      color: 'WARM_ACCENT (#f59e0b)',
      saturation: '30%',
      animation: '6-8s reveal',
      intensity: 'high'
    },
    audio: {
      frequency: '880Hz (A5) + 1320Hz (E6)',
      dBLevel: '+6dB peak',
      duration: '150ms',
      envelope: 'ADSR(5,20,0.6,125)'
    },
    haptic: {
      duration: '100-200ms',
      intensity: 'heavy',
      pattern: 'pulse-peak'
    },
    totalExperience: 'Celebratory, attention-demanding'
  },

  nearMissP2: {
    visuals: {
      color: 'NEUTRAL or CALMING_BLUE',
      saturation: '15-20%',
      animation: '400-600ms shake',
      intensity: 'moderate'
    },
    audio: {
      frequency: '440Hz (A4) - lower than success',
      dBLevel: '-3dB from win',
      duration: '100ms',
      envelope: 'flat'
    },
    haptic: {
      duration: '30-50ms',
      intensity: 'light',
      pattern: 'single-tap'
    },
    totalExperience: 'Encouragement mixed with anticipation'
  },

  immersiveP8: {
    visuals: {
      color: 'RELAXING_BLUE (#0891b2)',
      saturation: '20-25%',
      animation: 'smooth, continuous',
      intensity: 'moderate-consistent'
    },
    audio: {
      frequency: 'ambient or binaural',
      dBLevel: 'baseline',
      duration: 'continuous',
      envelope: 'sustained'
    },
    haptic: {
      duration: 'minimal/none',
      intensity: 'light if present',
      pattern: 'infrequent'
    },
    totalExperience: 'Flow-inducing, non-intrusive'
  }
};

// ACCESSIBILITY COMPLIANCE
export const ACCESSIBILITY_SPECS = {
  colorContrast: {
    standard: '4.5:1',
    enhanced: '7:1',
    requirement: 'All foreground/background combinations must meet standard'
  },

  audioAccessibility: {
    transcript: 'All meaningful audio must have text alternative',
    volume: 'User-controllable, never auto-play with sound > -20dB',
    frequency: 'Avoid sustained tones >6Hz (binaural safety)'
  },

  hapticAccessibility: {
    optout: 'Must be disableable in settings',
    intensity: 'Should respect device vibration settings',
    notification: 'Users should know haptic will be used'
  },

  motionAccessibility: {
    respectPreferences: 'Honor prefers-reduced-motion media query',
    alternativesFastMotion: 'Provide static alternatives or slower versions',
    vestibularConsiderations: 'Avoid rapid rotation/scaling'
  }
};
