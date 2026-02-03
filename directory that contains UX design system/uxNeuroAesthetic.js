/**
 * UX Neuro-Aesthetic Parameters - Sensory Design Specifications
 *
 * Consolidated color, audio, haptic, and environmental design parameters
 * optimized for engagement and sensory perception.
 * Based on NEURO_AESTHETIC_PARAMETERS.md
 */

// ============================================
// COLOR PARAMETERS - WAVELENGTH SPECIFICATIONS
// ============================================

export const COLOR_WAVELENGTHS = {
  CALMING_BLUE: {
    wavelength: 450, // nanometers
    hex: '#2563eb',
    psychologicalEffect: 'Calm, trust, reduced anxiety',
    useCase: 'Background, loading states',
    saturation: '20%',
    brightness: '70%'
  },

  RELAXING_BLUE: {
    wavelength: 490,
    hex: '#0891b2', // Cyan-blue
    psychologicalEffect: 'Relaxed focus, engagement',
    useCase: 'Active UI elements',
    saturation: '25%',
    brightness: '70%'
  },

  WARM_ACCENT: {
    wavelengthRange: '580-620',
    hex: '#f59e0b', // Orange
    psychologicalEffect: 'Attention, urgency',
    useCase: 'CTAs, notifications, variable rewards',
    saturation: '30%', // Cap at 30% max
    brightness: '70%'
  },

  NEUTRAL: {
    psychologicalEffect: 'Cognitive rest',
    useCase: 'Content areas, background',
    saturation: '0-10%',
    brightness: '70%'
  }
};

// ============================================
// COLOR PSYCHOLOGY APPLICATION TABLE
// ============================================

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

// ============================================
// SATURATION GUIDELINES
// ============================================

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
    saturation: '30%', // HARD CAP
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

// ============================================
// AUDIO PARAMETERS - FREQUENCY SPECIFICATIONS
// ============================================

export const AUDIO_FREQUENCIES = {
  THETA_WAVE: {
    frequency: 6.0, // Hz
    purpose: 'Relaxed focus state induction',
    binaural: false,
    effectDuration: '20-30 min'
  },

  ASMR_FUNDAMENTAL: {
    frequency: 180, // Hz
    purpose: 'Pleasant tingling response',
    application: 'Subtle background sounds',
    perceptualEffect: 'Calming, pleasant'
  },

  SCHUMANN_FREQUENCY: {
    frequency: 7.83, // Hz
    purpose: 'Earth resonance, grounding',
    application: 'Ambient environmental audio',
    perceptualEffect: 'Natural, grounded'
  },

  BINAURAL_BASE: {
    leftEar: 180, // Hz
    rightEar: 186, // Hz
    perceivedDifference: 6, // Hz (theta range)
    effect: 'Relaxed focus, reduced critical thinking',
    safetyNote: 'Use only with explicit consent'
  }
};

// ============================================
// BINAURAL BEAT DESIGN
// ============================================

export const BINAURAL_BEAT_CONFIGURATION = {
  leftEar: 180, // Hz base frequency
  rightEar: 186, // Hz offset
  perceivedFrequency: 6, // Hz (difference tone)
  perceptualRange: 'theta', // 4-8 Hz range
  psychologicalEffect: 'Relaxed focus, reduced critical thinking',
  safetyConsiderations: [
    'Not recommended for children under 18',
    'Requires explicit user consent',
    'May interfere with medical conditions',
    'Headphones required for binaural effect'
  ]
};

// ============================================
// AUDIO INTENSITY BY ENGAGEMENT PATTERN
// ============================================

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

// ============================================
// SOUND DESIGN METRICS & IMPACT
// ============================================

export const SOUND_DESIGN_IMPACT = {
  repeatPurchaseRates: {
    noAudio: 0.11,          // 11% baseline
    genericAudio: 0.16,     // 16% generic audio
    optimizedAudio: 0.24,   // 24% with pattern-optimized audio
    audioWithHaptic: 0.31   // 31% audio + haptic combined
  },

  improvementMetrics: {
    genericAudioGain: '45%', // (16-11)/11
    optimizedAudioGain: '118%', // (24-11)/11
    fullAudioHapticGain: '182%' // (31-11)/11
  },

  soundDesignRecommendation: 'Optimal audio adds 13-20% to engagement metrics'
};

// ============================================
// HAPTIC PARAMETERS - DURATION SPECIFICATIONS
// ============================================

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

// ============================================
// HAPTIC INTENSITY MAPPING
// ============================================

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

// ============================================
// MULTI-SENSORY COORDINATION TIMING
// ============================================

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

// ============================================
// ANIMATION DURATION RESEARCH
// ============================================

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

// ============================================
// ENVIRONMENTAL DESIGN CONDITIONS
// ============================================

export const ENVIRONMENTAL_CONDITIONS = {
  lightingConditions: {
    optimalBrightness: '70%',
    recommendation: 'Account for dark mode (reduced brightness)',
    adaptiveColor: true,
    contrastMinimum: '4.5:1' // WCAG AA
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
    maxSPL: '85dB' // Safe listening standard
  }
};

// ============================================
// TIME PERCEPTION MANIPULATION
// ============================================

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
    actual: '95 minutes', // With optimal design
    timePerceptionGap: '784%', // 95/11
    note: 'Adolescent brains particularly susceptible to time suppression'
  }
};

// ============================================
// SENSORY DESIGN RECOMMENDATIONS BY CONTEXT
// ============================================

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

// ============================================
// ACCESSIBILITY COMPLIANCE
// ============================================

export const ACCESSIBILITY_SPECS = {
  colorContrast: {
    standard: '4.5:1', // WCAG AA
    enhanced: '7:1',   // WCAG AAA
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
