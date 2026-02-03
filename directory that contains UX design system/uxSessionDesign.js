/**
 * UX Session Design - Temporal Architecture for Engagement
 *
 * Consolidated session architecture constants, reward probability curves,
 * event timestamps, and return hook patterns.
 * Based on SESSION_ARCHITECTURE.md
 */

// ============================================
// 11-MINUTE OPTIMAL SESSION ARC
// ============================================

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

// ============================================
// SESSION PHASE TIMELINE (minutes)
// ============================================

export const SESSION_TIMELINE = {
  rewardProbabilityByMinute: {
    0: 0.05,   // Entry start
    1: 0.05,   // Entry end
    2: 0.10,   // Build early
    3: 0.15,   // Build end
    4: 0.20,   // Challenge start
    5: 0.25,   // Challenge
    6: 0.35,   // Peak start
    7: 0.35,   // Peak
    8: 0.28,   // Peak/Integrate transition
    9: 0.20,   // Integrate
    10: 0.15,  // Integrate/Close transition
    11: 0.10   // Close
  },

  // ASCII representation of reward curve
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

// ============================================
// CRITICAL EVENT TIMESTAMPS
// ============================================

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
      phase: SESSION_PHASES.ENTRY,
      rewardProbability: 0.05,
      messaging: 'Welcome reward - builds expectation'
    },
    120: {
      name: 'Value Confirmation',
      phase: SESSION_PHASES.BUILD,
      rewardProbability: 0.10,
      messaging: 'Your investment is paying off'
    },
    240: {
      name: 'Deep Engagement Reward',
      phase: SESSION_PHASES.CHALLENGE,
      rewardProbability: 0.25,
      messaging: 'Major achievement unlocked'
    },
    400: {
      name: 'Late-Session Peak',
      phase: SESSION_PHASES.PEAK,
      rewardProbability: 0.35,
      messaging: 'Memorable conclusion reward'
    }
  }
};

// ============================================
// RETURN HOOKS
// ============================================

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

// ============================================
// HOOK EFFECTIVENESS BY USER TYPE
// ============================================

export const HOOK_EFFECTIVENESS = {
  completionOriented: {
    userType: 'Completion-Oriented',
    hookRanking: {
      'Progress': 'VERY HIGH',    // ████████
      'Streak': 'VERY HIGH',      // ████████
      'Preview': 'HIGH',          // ██████
      'Mystery': 'MODERATE'       // ████
    },
    dominantMotive: 'Goal achievement'
  },

  socialOriented: {
    userType: 'Social-Oriented',
    hookRanking: {
      'Streak': 'HIGH',           // ██████
      'Mystery': 'HIGH',          // ██████
      'Progress': 'MODERATE',     // ████
      'Preview': 'MODERATE'       // ████
    },
    dominantMotive: 'Social connection'
  },

  casual: {
    userType: 'Casual',
    hookRanking: {
      'Mystery': 'HIGH',          // ██████
      'Preview': 'LOW',           // ███
      'Streak': 'MODERATE',       // ████
      'Progress': 'LOW'           // ██
    },
    dominantMotive: 'Variety and novelty'
  }
};

// ============================================
// PHASE-SPECIFIC UI PATTERNS
// ============================================

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

// ============================================
// SESSION ARCHITECTURE TEMPLATES
// ============================================

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
    duration: 300, // 5 minutes shorter
    phases: ['ENTRY', 'BUILD', 'CHALLENGE', 'PEAK', 'CLOSE'],
    patternFocus: ['P2', 'P3', 'P4', 'P12'],
    streakProtection: true,
    expectedRepeats: 2.8
  },

  socialExperience: {
    name: 'Social Experience Session',
    duration: 720, // 2 minutes longer for social content
    phases: ['ENTRY', 'BUILD', 'CHALLENGE', 'PEAK', 'INTEGRATE', 'CLOSE'],
    patternFocus: ['P8', 'P10', 'P11'],
    communityElements: true,
    expectedRepeats: 2.5
  }
};

// ============================================
// RETURN HOOK SEQUENCING
// ============================================

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

// ============================================
// PERFORMANCE METRICS BY SESSION STRUCTURE
// ============================================

export const SESSION_PERFORMANCE_METRICS = {
  retention: {
    day1: 0.42,    // 42% day 1 retention baseline
    day7: 0.18,    // 18% day 7 baseline
    withOptimizedHooks: {
      day1: 0.52,  // +10% improvement
      day7: 0.28   // +10% improvement
    }
  },

  sessionLength: {
    targetMinutes: 11,
    adolescentAverage: 95, // Can extend significantly
    completionOrientedAverage: 12
  },

  peakEngagement: {
    phase: 'PEAK (6-8 min)',
    rewardDensity: 0.35,
    expectedEngagementScore: 0.89
  }
};
