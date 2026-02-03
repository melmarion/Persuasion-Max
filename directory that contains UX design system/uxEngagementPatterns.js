/**
 * UX Engagement Patterns - P1-P12 Design Specifications
 *
 * Consolidated engagement pattern constants, triggers, metrics, and UI specifications.
 * Based on ENGAGEMENT_PATTERNS_P1_P12.md and CROSS_PATTERN_INTERACTION_MAPS.md
 */

// ============================================
// PATTERN 1: Variable Reward Scheduling
// ============================================
export const P1_VARIABLE_REWARD = {
  name: 'Variable Reward Scheduling',
  description: 'Unpredictable rewards create stronger engagement than predictable ones',

  constants: {
    ANTICIPATION_WINDOW: { min: 200, max: 400 }, // milliseconds
    ANTICIPATION_STRETCH: 70, // peak delay in ms
    HIT_FREQUENCY: 0.198, // 19.8% (range 0.15-0.22)
    BONUS_TRIGGER: 37, // prime number
    REWARD_DISTRIBUTION: {
      micro: 0.50,      // 50% micro rewards
      standard: 0.35,   // 35% standard
      major: 0.12,      // 12% major
      legendary: 0.03   // 3% legendary
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

// ============================================
// PATTERN 2: Progress Momentum
// ============================================
export const P2_PROGRESS_MOMENTUM = {
  name: 'Progress Momentum',
  description: 'Near-successes generate continued engagement through reward-like activation',

  constants: {
    OPTIMAL_RATE: 0.30, // 30% near-miss rate
    DOPAMINE_RATIO: 1.20, // 120% baseline (vs 150% win)
    CUMULATIVE_PROGRESS: 3 // 3 near-successes = 1 consolation reward
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
    engagementExtension: 0.22, // 22% longer play sessions
    sessionContinuation: 0.89 // 89% continue playing after near-miss
  }
};

// ============================================
// PATTERN 3: Encouraging Feedback
// ============================================
export const P3_ENCOURAGING_FEEDBACK = {
  name: 'Encouraging Feedback',
  description: 'Positive reinforcement for partial progress and effort',

  uiSpecifications: {
    successColor: '#10b981', // Green
    celebrationAnimation: 'pulse',
    celebrationDuration: '300-500ms',
    feedbackMessage: 'encouraging', // vs neutral or critical
    soundDesign: 'positive-tone',
    hapticFeedback: 'light-impact'
  },

  appliedTo: [
    'Sub-win celebrations',
    'Positive framing of incomplete actions',
    'Milestone recognition'
  ]
};

// ============================================
// PATTERN 4: Progress Protection
// ============================================
export const P4_PROGRESS_PROTECTION = {
  name: 'Progress Protection',
  description: 'Preservation of accumulated progress to prevent loss aversion',

  uiSpecifications: {
    protectionColor: '#fbbf24', // Amber
    protectionIcon: 'shield',
    preservationMessage: 'Your progress is safe',
    lossAversionThreshold: 0.80 // 80% loss triggers stronger response
  },

  appliedTo: [
    'Streak preservation',
    'Loss aversion mechanics',
    'Progress bar safety nets'
  ]
};

// ============================================
// PATTERN 5: Investment Recognition
// ============================================
export const P5_INVESTMENT_RECOGNITION = {
  name: 'Investment Recognition',
  description: 'Display and acknowledge user sunk costs to increase commitment',

  uiSpecifications: {
    investmentColor: '#8b5cf6', // Purple
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

// ============================================
// PATTERN 6: Timely Opportunities
// ============================================
export const P6_TIMELY_OPPORTUNITIES = {
  name: 'Timely Opportunities',
  description: 'Time-limited offers and scarcity mechanics',

  uiSpecifications: {
    urgencyColor: '#f59e0b', // Orange
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

// ============================================
// PATTERN 7: Contextual Offers
// ============================================
export const P7_CONTEXTUAL_OFFERS = {
  name: 'Contextual Offers',
  description: 'Emotion-timed offers and failure recovery mechanics',

  uiSpecifications: {
    triggerContext: 'post-loss',
    recoveryColor: '#10b981', // Green for recovery
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

// ============================================
// PATTERN 8: Immersive Experience
// ============================================
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

// ============================================
// PATTERN 9: Personalized Tiers
// ============================================
export const P9_PERSONALIZED_TIERS = {
  name: 'Personalized Tiers',
  description: 'Tiered engagement based on user spending and responsiveness',

  uiSpecifications: {
    tieringColor: '#8b5cf6', // Purple
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

// ============================================
// PATTERN 10: Community Activity
// ============================================
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

// ============================================
// PATTERN 11: Community Connection
// ============================================
export const P11_COMMUNITY_CONNECTION = {
  name: 'Community Connection',
  description: 'Group pressure and reciprocity through peer relationships',

  uiSpecifications: {
    connectionType: 'social-proof',
    peerInfluenceBoost: 0.45, // 45% conversion boost
    identityLinkingBoost: 0.67, // 67% higher acceptance
    communityValidationBoost: 0.38 // 38% engagement boost
  },

  appliedTo: [
    'Group pressure mechanisms',
    'Reciprocity triggers',
    'Peer recommendations'
  ]
};

// ============================================
// PATTERN 12: Identity & Achievement
// ============================================
export const P12_IDENTITY_ACHIEVEMENT = {
  name: 'Identity & Achievement',
  description: 'Status labels and milestone systems tied to identity',

  uiSpecifications: {
    achievementColor: '#fbbf24', // Amber
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

// ============================================
// CROSS-PATTERN INTERACTION MAPS
// ============================================

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

// ============================================
// PATTERN RESPONSIVENESS BY USER TYPE
// ============================================

export const USER_PATTERN_RESPONSIVENESS = {
  adolescent: {
    age: '12-17',
    mostResponsive: ['P7', 'P8', 'P11', 'P12'],
    multipliers: {
      P7: 3.2, // Contextual offers
      P8: 1.0, // Immersive (95 min daily)
      P11: 1.8, // Community
      P12: 2.1 // Identity & Achievement
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
      P1: 4.2, // Variable reward
      P2: 3.8, // Progress momentum
      P3: 6.1, // Encouraging feedback
      P7: 5.3, // Contextual offers
      P9: 8.2  // Personalized tiers (whale targeting)
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

// ============================================
// ANIMATION SPECIFICATIONS FOR PATTERNS
// ============================================

export const PATTERN_ANIMATIONS = {
  P1_variableRewardReveal: {
    duration: '6.8s', // Average optimized
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

// ============================================
// AUDIO SPECIFICATIONS FOR PATTERNS
// ============================================

export const PATTERN_AUDIO = {
  P1_rewardSound: {
    successFrequency: 880, // A5 note
    successFrequency2: 1320, // E6 (harmonic)
    duration: '150ms',
    envelope: 'ADSR(5, 20, 0.6, 125)'
  },

  P2_nearMissSound: {
    frequency: 440, // A4 - lower than success
    duration: '100ms',
    envelope: 'flat'
  },

  P3_encouragingSound: {
    frequency: 587, // D5
    duration: '150ms',
    tone: 'uplifting'
  },

  P12_achievementSound: {
    baseFrequency: 880,
    triumphant: true,
    duration: '300-500ms'
  }
};

// ============================================
// CONVERSION THRESHOLDS BY PATTERN
// ============================================

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
