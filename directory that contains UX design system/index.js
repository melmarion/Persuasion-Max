/**
 * UX Design System - Consolidated Master File
 *
 * Single import source for all UX design tokens, patterns, and utilities.
 * Use this for all UX implementations and tool attractiveness audits.
 *
 * Usage:
 *   import { TOUCH_TARGETS, SPACING, COLORS, EASING, ... } from './index';
 *
 * Also exports engagement patterns, session design, and neuro-aesthetic specs:
 *   import { P1_VARIABLE_REWARD, SESSION_PHASES, COLOR_WAVELENGTHS, ... } from './index';
 */

// ============================================
// RE-EXPORTS FROM SPECIALIZED MODULES
// ============================================

// Engagement Patterns (P1-P12)
export {
  P1_VARIABLE_REWARD,
  P2_PROGRESS_MOMENTUM,
  P3_ENCOURAGING_FEEDBACK,
  P4_PROGRESS_PROTECTION,
  P5_INVESTMENT_RECOGNITION,
  P6_TIMELY_OPPORTUNITIES,
  P7_CONTEXTUAL_OFFERS,
  P8_IMMERSIVE_EXPERIENCE,
  P9_PERSONALIZED_TIERS,
  P10_COMMUNITY_ACTIVITY,
  P11_COMMUNITY_CONNECTION,
  P12_IDENTITY_ACHIEVEMENT,
  PATTERN_COMBINATIONS,
  USER_PATTERN_RESPONSIVENESS,
  PATTERN_ANIMATIONS,
  PATTERN_AUDIO,
  PATTERN_CONVERSION_THRESHOLDS
} from './uxEngagementPatterns';

// Session Design
export {
  SESSION_PHASES,
  SESSION_TIMELINE,
  CRITICAL_EVENTS,
  RETURN_HOOKS,
  HOOK_EFFECTIVENESS,
  PHASE_UI_PATTERNS,
  SESSION_TEMPLATES,
  HOOK_SEQUENCES,
  SESSION_PERFORMANCE_METRICS
} from './uxSessionDesign';

// Neuro-Aesthetic Parameters
export {
  COLOR_WAVELENGTHS,
  COLOR_PSYCHOLOGY_MATRIX,
  SATURATION_GUIDELINES,
  AUDIO_FREQUENCIES,
  BINAURAL_BEAT_CONFIGURATION,
  AUDIO_INTENSITY_BY_PATTERN,
  SOUND_DESIGN_IMPACT,
  HAPTIC_SPECIFICATIONS,
  HAPTIC_INTENSITY_MAPPING,
  MULTISENSORY_TIMING,
  ANIMATION_DURATION_RESEARCH,
  ENVIRONMENTAL_CONDITIONS,
  TIME_PERCEPTION_FACTORS,
  SENSORY_CONTEXT_RECOMMENDATIONS,
  ACCESSIBILITY_SPECS
} from './uxNeuroAesthetic';

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
