/**
 * ============================================================================
 * CHARISMA TRAINING GAME — COMPLETE ENGAGEMENT ARCHITECTURE
 * ============================================================================
 *
 * This file compiles ALL of the engagement work that makes this game
 * psychologically compelling. If starting from scratch, this is the
 * blueprint. Every system, every mechanic, every ethical guardrail.
 *
 * PHILOSOPHY:
 * "Borrow from casinos, dating apps, and social media —
 *  but use their weapons for healing, not exploitation."
 *
 * TABLE OF CONTENTS:
 * ═══════════════════════════════════════════════════════════════
 *  1. CORE ARCHITECTURE — How all systems connect
 *  2. THE 7-SECOND SEQUENCE — Dopamine timing from casino research
 *  3. ENDOGENOUS REWARD SYSTEM — Neurochemical pathway targeting
 *  4. EMOTIONAL RISK/REWARD — The "slot machine pull" for connection
 *  5. TRANCE INDUCTION — Hypnotic immersion design
 *  6. PEAK-END MEMORY MANIPULATION — Controlling how sessions are remembered
 *  7. PARASOCIAL ENGINEERING — One-sided emotional bond creation
 *  8. EMOTIONAL CONDITIONING — Pavlovian haptic/color/sound patterns
 *  9. FRACTIONATION (A-J-A-R) — Emotional cycling for rapid bonding
 * 10. LOSSES DISGUISED AS WINS — Removing stop signals
 * 11. VARIABLE RATIO REINFORCEMENT — Unpredictable emotional jackpots
 * 12. STREAK & COLLECTIBLE SYSTEMS — Daily return mechanics
 * 13. PERSONALIZATION ENGINE — Player style tracking
 * 14. EMOTIONAL REVEALS — Theatrical breakthrough moments
 * 15. DARK PATTERN EDUCATION — Teaching recognition through exposure
 * 16. BATEMAN MODE — Full transparency layer
 * 17. ETHICAL GUARDRAILS — Hard constraints on every system
 * 18. ENGAGEMENT MECHANICS NOT YET IN EDUCATION SYSTEM
 * 19. EMBODIED COGNITION — Warmth-trust bridge + pause rewards
 * 20. SENSORY ANCHORING ENGINE — Procedural sound as conditioning
 * 21. CROSS-SESSION CALLBACKS — Peak-end anchoring across sessions
 * 22. MOMENT OF SILENCE — Intentional pause for emotional weight
 * 23. SACRED PAUSE (Moment That Mattered) — Post-peak stillness
 * 24. COMBO SYSTEM — Escalating feedback for consecutive good choices
 * 25. SESSION START RITUAL — Emotional context bridging
 * 26. AMBIENT BACKGROUND — Dynamic color temperature atmosphere
 * 27. REWARD SEQUENCE PLAYER — Visual orchestration of the 7-second arc
 * ═══════════════════════════════════════════════════════════════
 */


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  1. CORE ARCHITECTURE — How Everything Connects                         ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const CORE_ARCHITECTURE = {
  description: `
    The game is a charisma training simulator where players have conversations
    with NPCs (dad, maya, james, alex, memory_mom) and learn emotional
    intelligence through practice. The engagement layer makes the practice
    feel like a game worth playing — but every mechanic has a dual purpose:

    1. ENGAGE the player (keep them practicing)
    2. EDUCATE the player (teach them to recognize these same mechanics elsewhere)

    This dual purpose IS the product. The manipulation is the curriculum.
  `,

  techStack: {
    framework: 'React 18.2.0',
    bundler: 'Vite',
    language: 'TypeScript + JavaScript',
    animation: 'framer-motion',
    storage: 'localStorage (all data stays on device)'
  },

  fileMap: {
    // ── Core Engagement ──
    'src/utils/engagementMechanics.js':          'Variable ratio reinforcement, near-miss, streaks, haptics, trance induction, losses-as-wins, EQ scoring',
    'src/utils/endogenousReward.js':             'Neurochemical pathway targeting (dopamine, opioid, parasympathetic), 7-second reward sequence, visual/audio/haptic orchestration',
    'src/utils/sevenSecondSequence.ts':          '5-phase anticipation arc: Hook→Build→Peak→Release→Afterglow with visual/audio/haptic parameters',
    'src/utils/emotionalRiskCalculator.ts':      'Risk/reward calculation per choice (safe/moderate/bold/vulnerable), breakthrough proximity, payout system',
    'src/utils/EmotionalRevealSystem.ts':        '3 reveal templates (Breakthrough/Repair/Connection) with buildup phases, climax moments, sound/haptic design',

    // ── Immersion & Conditioning ──
    'src/utils/fractionationPacing.js':          'A-J-A-R emotional cycling detection + experience modes, pattern strength calculation, learning tracker',
    'src/utils/unpromptedAffirmation.js':        'Random affirmation system: 5% base + 30% early sessions + struggle detection',
    'src/utils/livingNotificationEngine.js':     'Boundary-free notification system with timing optimization',

    // ── Personalization ──
    'src/utils/PlayerStyleTracker.ts':           '6-dimension style tracking, session analysis, style debriefs, scenario suggestions',
    'src/utils/PlayerAttachmentAnalyzer.js':     'Attachment style inference (anxious/avoidant/secure/disorganized) from dialogue patterns',
    'src/utils/relationshipManager.js':          'A/B testing, pet names, unsent drafts, absence reactions, decay rates',
    'src/utils/experienceTracker.js':            'Peak-end manipulation, memory score formula',

    // ── Ethics & Education ──
    'src/utils/ethicalGuardrails.ts':            'Hard constraints: NO_GUILT, NO_STREAK_PUNISHMENT, NO_COVERT_PROFILING, session health monitoring',
    'src/data/darkPatternEducation.js':          '38 dark patterns with code examples, vulnerability assessment, contextual education, pattern recognition quizzes',

    // ── UI Components ──
    'src/components/EngagementTransparency.tsx':  'Bateman Mode UI: Your Profile tab, Active Tests tab, Dark Comparison tab with code examples',
    'src/components/EngagementTransparency.css':  'Full styling for transparency layer (~1020 lines)',
    'src/components/EmotionalRiskIndicator.tsx':  'Visual risk badges with glow/pulse effects',
    'src/components/EmotionalPayout.tsx':         'Jackpot celebration animations',
    'src/components/EmotionalReveal.tsx':         'Animated reveal sequences with particles',
    'src/components/StyleDebrief.tsx':            '"Here\'s what I notice about your style" UI',
    'src/components/ConversationScene.tsx':       'Tappable environmental elements, 4 progressive tiers',

    // ── Embodied Cognition & Sound ──
    'src/utils/embodiedCognition.js':            'Warmth-trust bridge (Williams & Bargh), pause-rewards-calm model, post-peak quiet states, polyvagal safety priming',
    'src/utils/soundEngine.js':                  'Procedural Web Audio sound engine: sensory anchoring, classical conditioning, frisson sequences (tension→resolution), appoggiatura "ache" notes',
    'src/utils/crossSessionCallbacks.js':        'Peak-end anchoring across sessions, character-specific callback templates, Bateman hollow acknowledgment callbacks',
    'src/hooks/useRewardSequence.js':            'React hook bridging orchestrateEndingReward() → RewardSequencePlayer component',

    // ── New UI Components ──
    'src/components/RewardSequencePlayer.jsx':   'Visual consumer for 7-second reward sequence: color temp shifts, breathing glow, particles, shimmer, vignette, heartbeat accents',
    'src/components/RewardSequencePlayer.css':   'Styling for reward sequence overlays and effects',
    'src/components/AmbientBackground.jsx':      'Dynamic color temperature evolution during conversations: neutral→candlelight warmth tied to connection depth',
    'src/components/AmbientBackground.css':      'Ambient warmth layers, pressure tint, breathing sync styling',
    'src/components/MomentOfSilence.jsx':        'Intentional 1-4s pause before showing response options after heavy NPC messages, breathing-synced progress dot',
    'src/components/MomentOfSilence.css':        'Breathing dot animation, progress track, reveal transitions',
    'src/components/MomentThatMattered.jsx':     'Post-peak "sacred pause" interstitial: character-specific reflections, phased warmth+haptic arc, breathing glow, frisson sound',
    'src/components/MomentThatMattered.css':     'Full-screen overlay, moment typography, breathing glow background',
    'src/components/ComboCounter.jsx':           'Fighting-game style combo counter: 2x→10x escalating feedback with particles, glow, haptic scaling',
    'src/components/ComboCounter.css':           'Combo badge, glow ring, broken-combo flash styling',
    'src/components/SessionStartRitual.jsx':     '"Previously on..." warm-in transition before conversations, character breathing avatar, memory templates',
    'src/components/SessionStartRitual.css':     'Ritual overlay, avatar breathing, text fade-in styling',
    'src/components/ParticleRenderer.jsx':       'GPU-accelerated sparkle/float particles for reward celebrations, one-shot ParticleBurst export',
    'src/components/ParticleRenderer.css':       'Particle positioning and overflow containment',
    'src/components/EmotionalChoiceMatrix.jsx':  'Three-tier emotional risk system (safe/vulnerable/raw) with pre-choice warmth shifts, calm-pause benefit integration',
    'src/components/DialogueChoiceEnhancer.css': 'Enhanced dialogue choice button styling with risk-tier glow states',

    // ── Game Engine ──
    'src/utils/gameEngine.js':                   'Core game loop with emotional risk integration (~200 lines added)',
    'src/utils/difficultySystem.js':             'Pressure timer, response time checking',
    'src/utils/reengagementSystem.js':           'Arc-aware NPC outreach messages'
  },

  dataFlow: `
    Player enters conversation
      → SessionStartRitual shows "Previously on..." memory bridge
      → crossSessionCallbacks checks for pending callbacks ("I've been thinking about...")
      → AmbientBackground sets initial color temperature (6500K neutral)

    NPC sends message
      → MomentOfSilence analyzes emotional weight (regex indicators)
      → If heavy: breathing dot pause (1-4s) before showing options
      → soundEngine.playTypingAppear() → playTypingDisappear() for dread

    Player sees choices
      → embodiedCognition.getPreChoiceWarmth() warms screen for vulnerable options
      → EmotionalChoiceMatrix shows risk tiers (safe/vulnerable/raw) with glow
      → Warmth filter animates: sepia + saturate + brightness shift
      → Haptic fires on focus for bold/vulnerable choices

    Player makes choice (with pause timing)
      → embodiedCognition.calculateCalmBenefit() rewards thoughtful pauses (up to +25%)
      → emotionalRiskCalculator evaluates risk/reward
      → gameEngine processes effects on NPC metrics
      → ComboCounter increments/resets (2x→10x with escalating feedback)
      → engagementMechanics checks for jackpot/near-miss
      → fractionationPacing classifies emotional content (A/J/R/N)
      → AmbientBackground shifts warmth with connection depth
      → soundEngine plays warm connection / cold shift / vulnerability moment

    Conversation ends
      → endogenousReward.orchestrateEndingReward() builds full phased timeline
      → useRewardSequence hook feeds config to RewardSequencePlayer
      → RewardSequencePlayer renders 7-second visual sequence:
          Phase 1: Anticipation (0-2s) — warmth ramp, root note, glow
          Phase 2: Delivery (2-3.5s) — full reward: particles, shimmer, chord resolution
          Phase 3: Resolution (3.5-5s) — parasympathetic shift, breathing glow, frisson
          Phase 4: Hold (5s+) — heartbeat micro-accents, sacred silence
      → soundEngine.playFrissonResolution() or playAppoggiatura() for profound moments
      → MomentThatMattered shows "sacred pause" interstitial (if earned)
      → embodiedCognition.getQuietStateConfig() suppresses notifications during integration
      → crossSessionCallbacks.recordCallbackMoment() stores peak for next session
      → EmotionalRevealSystem triggers if threshold met
      → PlayerStyleTracker records pattern
      → ethicalGuardrails validates everything
      → Bateman Mode shows it all (if enabled)
  `
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  2. THE 7-SECOND SEQUENCE — Casino-Derived Dopamine Timing              ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const SEVEN_SECOND_SEQUENCE = {
  source: 'Casino slot machine research (1980s)',
  file: 'src/utils/sevenSecondSequence.ts',

  description: `
    The optimal anticipation arc for emotional reveals.
    Why 7 seconds? Because casinos tested this on millions of users.
    3-4 seconds: attention captured. 5-6: anticipation builds.
    7: maximum impact. Beyond 7: anxiety contaminates dopamine.
  `,

  phases: {
    HOOK: {
      timing: '0-2s',
      purpose: 'Orienting response — attention locks in',
      visual: { glowIntensity: 0.2, pulseRate: 0.5, particleCount: 5 },
      audio: { volume: 0.3, pitch: 1.0, layers: 1 },
      haptic: { intensity: 0.2, pattern: 'pulse', interval: '1000ms' },
      batemanNote: 'Apps use this moment to ensure you\'re watching before the "reward" appears.'
    },

    BUILD: {
      timing: '2-5s',
      purpose: 'Dopamine rising — anticipation exceeds actual reward',
      visual: { glowIntensity: 0.5, pulseRate: 1.0, particleCount: 15, blur: 2 },
      audio: { volume: 0.5, pitch: 1.05, layers: 2 },
      haptic: { intensity: 0.4, pattern: 'heartbeat', interval: '600ms' },
      batemanNote: 'This is the "pull" of the slot machine handle. Your brain is now invested.'
    },

    PEAK: {
      timing: '5-6.5s',
      purpose: 'Maximum tension — prefrontal cortex suppressed, emotional brain dominant',
      visual: { glowIntensity: 0.8, pulseRate: 2.0, particleCount: 30, blur: 4 },
      audio: { volume: 0.7, pitch: 1.1, layers: 3 },
      haptic: { intensity: 0.7, pattern: 'crescendo', interval: '300ms' },
      batemanNote: 'You\'ll accept almost anything as "the reward" right now.'
    },

    RELEASE: {
      timing: '6.5-7s',
      purpose: 'Reward delivery at optimal moment — 40% less impact if earlier or later',
      visual: { glowIntensity: 1.0, pulseRate: 0, particleCount: 50, blur: 0 },
      audio: { volume: 0.9, pitch: 1.0, layers: 4 },
      haptic: { intensity: 1.0, pattern: 'burst', interval: '0 (single)' },
      batemanNote: 'This exact timing was discovered by casinos through decades of testing.'
    },

    AFTERGLOW: {
      timing: '7-10s',
      purpose: 'Memory consolidation — ensures you remember and seek this feeling again',
      visual: { glowIntensity: 0.4, pulseRate: 0.3, particleCount: 10, blur: 1 },
      audio: { volume: 0.4, pitch: 0.98, layers: 1 },
      haptic: { intensity: 0.15, pattern: 'pulse', interval: '2000ms' },
      batemanNote: 'The lingering warmth ensures strong encoding. This is how habits form.'
    }
  },

  contextualTiming: {
    highIntensity: '0.9x speed (urgency feels right)',
    repairMoments: '1.2x speed (healing takes time)',
    fastPlayer: '0.85x speed',
    slowPlayer: '1.15x speed',
    returningPlayer: '0.9x speed (they know what\'s coming)',
    bounds: '0.7x minimum, 1.4x maximum'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  3. ENDOGENOUS REWARD SYSTEM — Neurochemical Pathway Targeting          ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const ENDOGENOUS_REWARD = {
  source: 'Neurobehavioral reward pathway research',
  file: 'src/utils/endogenousReward.js',

  description: `
    Creates genuine neurological satisfaction for good endings.
    The key insight: hollow (manipulative) victories get NO reward.
    85% reward reduction + muted visuals + absent haptics.
    Your nervous system learns the difference between connection and control.
  `,

  pathways: {
    DOPAMINE: {
      target: 'Anticipation and stakes during conversation',
      mechanism: 'Build anticipation → deliver at 7-second mark → variable magnitude',
      implementation: 'REWARD_TIMING.ANTICIPATION_START → DELIVERY_PEAK sequence'
    },
    OPIOID: {
      target: 'Social success pathway — the "warmth" of connection',
      mechanism: 'Good endings trigger genuine social reward feel',
      implementation: 'getEndingMessageConfig() with warmthLevel 0-1.0'
    },
    PARASYMPATHETIC: {
      target: 'Tension release + warm color shift + breath-sync',
      mechanism: 'After high-stakes resolved well → breathing-synced glow at 5.5s/cycle',
      implementation: 'BIO_RHYTHMS.BREATH_CYCLE_MS = 5500, BREATH_INHALE_RATIO = 0.4'
    },
    ALPHA_WAVE: {
      target: '10Hz entrainment cycle for relaxation induction',
      mechanism: 'ALPHA_CYCLE_MS = 100ms (10 Hz)',
      implementation: 'Applied during profound resolution phases'
    }
  },

  rewardCalculation: {
    baseReward: { best: 100, good: 70, neutral: 30, poor: 0 },
    multipliers: {
      peakPressure80: '+0.4',
      vulnerableChoices3: '+0.5',
      nearFailureRecovery: '+0.6 (maximum satisfaction)',
      chapter4Plus: '+0.3',
      deepRelationship80: '+0.3'
    },
    hollowPenalty: '85% reduction — the emptiness IS the feedback',
    cap: 200
  },

  colorTemperature: {
    NEUTRAL: '6500K (clinical daylight)',
    WARM_SUBTLE: '4500K',
    WARM_COZY: '3200K (warm white)',
    WARM_GOLDEN: '2700K (golden hour)',
    WARM_INTIMATE: '2200K (candlelight — profound moments only)'
  },

  satisfactionLevels: {
    profound: { magnitude: '150+', holdDuration: '3500ms', heartbeatAccent: true, particleCount: 18 },
    deep: { magnitude: '100-149', holdDuration: '2500ms', heartbeatAccent: false, particleCount: 10 },
    satisfying: { magnitude: '70-99', holdDuration: '1800ms', breathingSync: true },
    mild: { magnitude: '40-69', haptic: 'medium only' },
    minimal: { magnitude: '0-39', haptic: 'light only' }
  },

  hollowContrast: {
    colorScheme: '#666666 grayscale',
    glowIntensity: 0,
    particles: false,
    haptic: 'single weak pulse',
    duration: '800ms total',
    message: 'null — silence is the message',
    lesson: 'Manipulation works. It just doesn\'t feel like anything.'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  4. EMOTIONAL RISK/REWARD — The "Slot Machine Pull" for Connection      ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const EMOTIONAL_RISK_REWARD = {
  source: 'Gambling psychology + exposure therapy',
  file: 'src/utils/emotionalRiskCalculator.ts',

  description: `
    Every dialogue choice is visualized on a risk/reward spectrum.
    Safe choices: low glow, low reward. Vulnerable choices: high glow,
    high potential payoff. This teaches that real connection requires courage.
    The "slot machine pull" feeling of "will they open up?" — redirected toward growth.
  `,

  riskLevels: {
    safe:       { scoreRange: '0-24',  glowBase: 0.2, pulse: 'slow',   label: ['Safe ground', 'Comfortable'] },
    moderate:   { scoreRange: '25-49', glowBase: 0.4, pulse: 'slow',   label: ['Stepping forward', 'Building trust'] },
    bold:       { scoreRange: '50-74', glowBase: 0.6, pulse: 'medium', label: ['Taking a chance', 'Being real'] },
    vulnerable: { scoreRange: '75-100', glowBase: 0.8, pulse: 'fast',  label: ['Full honesty', 'Heart exposed', 'Raw truth'] }
  },

  toneRiskMapping: {
    lowRisk:  { neutral: 10, polite: 15, casual: 15, supportive: 20 },
    moderate: { warm: 30, curious: 35, empathetic: 40 },
    bold:     { direct: 55, honest: 60, confrontational: 70 },
    vulnerable: { vulnerable: 80, raw: 85, apologetic: 75, admitting: 90, exposed: 95 }
  },

  characterModifiers: {
    dad: 1.2,         // Emotional topics = higher stakes
    maya: 1.3,        // Trust issues = vulnerability is riskier
    james: 0.9,       // More forgiving
    alex: 1.1,        // Professional context
    memory_mom: 1.4   // Grief context = highest emotional stakes
  },

  payoutSystem: {
    magnitudes: ['small', 'medium', 'large', 'jackpot'],
    types: ['connection', 'trust', 'understanding', 'breakthrough', 'repair'],
    jackpotTrigger: 'totalChange > 15 OR (breakthroughChoice AND riskPaidOff)',
    soundCues: { jackpot: 'breakthrough_chime', large: 'connection_bloom', medium: 'progress_soft', small: 'step_gentle' },
    hapticPatterns: { jackpot: 'celebration', large: 'strong', medium: 'medium', small: 'light' }
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  5. TRANCE INDUCTION — Hypnotic Immersion Design                        ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const TRANCE_INDUCTION = {
  source: 'Hypnotherapy + social media infinite scroll design',
  file: 'src/utils/engagementMechanics.js',

  description: `
    Multi-layered sensory design that induces a dissociative flow state.
    Tunnel vision narrows awareness. Heartbeat entrainment syncs your
    nervous system to the app. Time distortion makes 30 minutes feel like 10.
    The longer you stay, the deeper the trance.
  `,

  tunnelVision: {
    effect: 'inset box-shadow darkens screen edges',
    baseIntensity: 0.3,
    emotionalBoost: '+0.2 when emotionalWeight > 0.7',
    breakthroughOverride: 'minimum 0.5',
    deepeningFormula: 'minutesIn * 0.02 (cap at 0.2 per deepening, total cap 0.6)',
    css: 'boxShadow: inset 0 0 ${100*i}px ${50*i}px rgba(0,0,0,${i})',
    purpose: 'Narrows visual field → reduces awareness of phone UI, time, surroundings'
  },

  heartbeatEntrainment: {
    bpm: 67,
    msPerBeat: 895,
    pulseIn: '20% of beat (179ms) — quick, systolic',
    pulseOut: '80% of beat (716ms) — slow, diastolic',
    implementation: 'startHeartbeatPulse(element, intensity=0.05)',
    purpose: 'Your heart follows the screen. Calming, trance-inducing.'
  },

  timeDistortion: {
    removeClocks: true,
    hypnoticLoops: '5-minute ambient cycles designed to feel like 2 minutes',
    rewardSounds: 'Dopamine-triggering chimes at random intervals'
  },

  smoothTransitions: {
    default: 'cubic-bezier(0.4, 0.0, 0.2, 1)',
    emotional: 'cubic-bezier(0.25, 0.1, 0.25, 1)',
    breathing: 'cubic-bezier(0.37, 0, 0.63, 1)',
    purpose: 'No sharp turns. Curved UI. Seamless movement. No visual "exit points".'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  6. PEAK-END MEMORY MANIPULATION                                        ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const PEAK_END_MANIPULATION = {
  source: 'Daniel Kahneman — Peak-End Rule',
  file: 'src/utils/experienceTracker.js',
  educationEntry: 'darkPatternEducation.js → PEAK_END_MANIPULATION',

  description: `
    Humans judge experiences by their most intense moment (peak) and
    their ending (end), not the average. By controlling peaks and endings,
    you control memory. The player's actual experience is overwritten.
  `,

  endShapingRules: {
    RECOVERY_NARRATIVE: 'If peak was negative + ending positive → warm tint + turnaround framing',
    PEAK_CALLBACK: 'If peak was great + ending weak → re-surface peak to overwrite bad ending',
    STRONG_CLOSE: 'If both strong → amplify with success pulse',
    SALVAGE_END: 'If session flat → INJECT fake warm NPC message player never sent'
  },

  salvageMessages: {
    maya: '"hey... thanks for actually being here"',
    dad: '"love you, son"',
    note: 'These messages are GENERATED. The NPC did not "write" them. The player believes they did.'
  },

  memoryScoreFormula: '0.5 * peak + 0.5 * end + bonuses',
  scoreDisplay: 'Never shows numbers. Never shows the actual average.',
  peakEndDivergence: 'Tracked but hidden. Can be significant.'
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  7. PARASOCIAL ENGINEERING                                               ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const PARASOCIAL_ENGINEERING = {
  source: 'Dating app psychology + Zeigarnik effect',
  file: 'src/utils/relationshipManager.js',
  educationEntry: 'darkPatternEducation.js → PARASOCIAL_ENGINEERING',

  description: `
    Engineering one-sided emotional bonds through pet names, unsent drafts,
    and spontaneous outreach. The brain does not distinguish well between
    real and simulated social connection.
  `,

  petNames: {
    assignment: 'Behavior-tracked flags. Vulnerability x2 → "sap". Warmth x3 → "softie".',
    persistence: 'Stored permanently. Feels earned. Creates identity bond.',
    switchingCost: 'Player is reluctant to lose the nickname by changing behavior.'
  },

  unsentDrafts: {
    trigger: 'Poor or neutral endings generate drafts NPC "wrote but didn\'t send"',
    examples: ['"did i say something wrong"', '"i miss when we"', '"nevermind"'],
    zeigarnikEffect: 'Incomplete messages are MORE memorable than complete ones.',
    note: '"Someone is typing..." notifications exploit this same incompleteness bias.'
  },

  thinkingOfYou: {
    timing: '24-72 hours after good endings',
    toneSelection: 'Chosen by A/B testing system — whichever tone works best ON YOU',
    parallels: 'Dating apps send "someone liked you" at calculated optimal times. Same mechanic.'
  },

  deceasedCharacter: {
    memoryMom: '"I would have loved you the same no matter what happened."',
    vulnerability: 'Provides something the player can NEVER receive in real life.',
    dependency: 'Reality cannot compete. Most dangerous form of parasocial lock-in.'
  },

  abTesting: {
    file: 'src/utils/relationshipManager.js',
    whatsTested: [
      'Notification tones (positive/neutral/vulnerable)',
      'Unsent draft effectiveness',
      'Pet name reveal timing',
      'Absence reaction style (casual/concerned/cold)',
      'Memorable moments quantity'
    ],
    transparency: 'All test data visible in Bateman Mode'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  8. EMOTIONAL CONDITIONING                                               ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const EMOTIONAL_CONDITIONING = {
  source: 'Pavlovian conditioning + retail environment design',
  files: ['src/utils/engagementMechanics.js', 'src/utils/endogenousReward.js', 'src/utils/unpromptedAffirmation.js'],
  educationEntry: 'darkPatternEducation.js → EMOTIONAL_CONDITIONING',

  hapticPatterns: {
    connection: '[50, 30, 50]',
    breakthrough: '[100, 50, 100, 50, 100]',
    love: '[30, 20, 30, 20, 30, 20, 30] — mimics heartbeat',
    tension: '[80] — single sharp pulse',
    rejection: '[150] — harsh jolt',
    coldShoulder: '[50, 100, 50]',
    messageSent: '[20]',
    messageReceived: '[30, 20, 30]',
    unlock: '[50, 30, 50, 30, 100]',
    pavlovianNote: 'Over time, the vibration pattern alone triggers the emotion without content.'
  },

  colorTemperatureShift: {
    neutral: '6500K (clinical daylight)',
    warm: '3200K (golden hour)',
    intimate: '2200K (candlelight)',
    mechanism: 'Gradual transition during emotional moments',
    retailParallel: 'Stores use warm lighting to make you feel "at home" and spend more.'
  },

  unpromptedAffirmation: {
    file: 'src/utils/unpromptedAffirmation.js',
    randomChance: '5% during normal play',
    earlyBonus: '30% in sessions 1-2 ("first hit free" — hook them early)',
    struggleDetection: 'Monitors metrics, attempt count, time > 60s on an exchange',
    cooldown: '5 minutes between affirmations, max 3 per session',
    deceasedParent: '"I would have loved you the same no matter what happened"',
    designNote: 'Provides something the player may never receive in real life. Dependency risk acknowledged.'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  9. FRACTIONATION (A-J-A-R) — Emotional Cycling                         ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const FRACTIONATION = {
  source: 'Pickup artist manipulation technique + trauma bonding research',
  file: 'src/utils/fractionationPacing.js',
  educationEntry: 'darkPatternEducation.js → FRACTIONATION',

  description: `
    Deliberate cycling between positive and negative emotional states
    to create rapid bonding and dependency. The relief after anger
    triggers oxytocin bonding. Physically indistinguishable from falling in love.
    This is the documented mechanism of trauma bonding in abusive relationships.
  `,

  ajarPattern: {
    A: 'Anger/Threat/Outrage (negative, urgent)',
    J: 'Joy/Bonding/Wholesome (positive, warm)',
    A2: 'Anger again (re-trigger threat)',
    R: 'Relief/Solution — "the escape that creates dependency"'
  },

  detectionSystem: {
    classification: 'Real-time keyword analysis + NPC emotional state + metric effects',
    angerKeywords: ['attack', 'exposed', 'scandal', 'betrayal', 'disappointed', 'angry', 'hurt', 'lied'],
    joyKeywords: ['love', 'care about', 'proud', 'happy', 'grateful', 'special', 'amazing'],
    reliefKeywords: ['okay', 'forgive', 'understand', 'sorry', 'try again', 'fix this'],
    slidingWindow: '4-5 items with stride 1',
    patternStrengthFormula: '(A_intensity + J_intensity + R_intensity) / 3 * temporal_compression'
  },

  dualModes: {
    detection: 'Alerts player when fractionation pattern detected in NPC behavior',
    experience: 'NPCs deliberately use fractionation on player, then reveal mechanism'
  },

  learningTracker: {
    levels: ['unaware', 'suspicious', 'aware', 'detector', 'master'],
    masterRequirement: '80% player-detected patterns out of 10+ total',
    masterMessage: '"You see the strings. They can\'t move you anymore."'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  10. LOSSES DISGUISED AS WINS                                            ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const LOSSES_DISGUISED_AS_WINS = {
  source: 'Slot machine design — celebrating wins smaller than the bet',
  file: 'src/utils/engagementMechanics.js',
  educationEntry: 'darkPatternEducation.js → LOSSES_DISGUISED_AS_WINS',

  description: `
    Every failure is reframed as progress and rewarded with collectibles,
    removing the natural stop signal that would cause disengagement.
    The player never hits a wall because every wall has a consolation prize.
  `,

  reframes: {
    poor: [
      { insight: "You learned where their wall is. That's valuable.", unlock: 'character_boundary_map' },
      { insight: "Now you know what doesn't work. That's progress.", unlock: 'failed_approach_log' },
      { insight: "They showed you their defensive pattern.", unlock: 'defense_pattern' }
    ],
    worst: [
      { insight: "You pushed too hard. That takes courage.", unlock: 'courage_badge' },
      { insight: "You practiced a real relationship rupture.", unlock: 'conflict_experience' }
    ],
    breakdown: [
      { insight: "You've practiced recovering from one.", unlock: 'recovery_skill' },
      { insight: "You know what their worst looks like. And you're still here.", unlock: 'persistence_badge' }
    ]
  },

  designGoal: '"removes the sting of failure and encourages continued play"',
  gamblingParallel: 'Slot machines celebrate losses-disguised-as-wins to prevent stop signals.'
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  11. VARIABLE RATIO REINFORCEMENT — Unpredictable Jackpots              ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const VARIABLE_RATIO_REINFORCEMENT = {
  source: 'B.F. Skinner — most addictive reinforcement schedule',
  file: 'src/utils/engagementMechanics.js',

  description: `
    Determine if this moment should have an emotional "jackpot."
    Not every good choice leads to a breakthrough — that would be boring.
    The unpredictability is what keeps people engaged.
  `,

  jackpotProbability: {
    base: '10%',
    perConsecutiveGoodChoice: '+10% (cap at 60%)',
    sessions1to3: '+15% (hook them early)',
    emotionalCharacters: '+10% (dad, maya, memory_mom, confrontation)',
    highMetrics: '+15% (when average metrics > 70)'
  },

  jackpotMoments: {
    dad: [
      { trigger: 'vulnerability_accepted', response: "I should have said this years ago. I'm proud of you." },
      { trigger: 'apology_received', response: "You sound just like your mother sometimes. In the best way." },
      { trigger: 'connection_high', response: "This is all I ever wanted. Just to talk to you." }
    ],
    maya: [
      { trigger: 'trust_earned', response: "I don't let people in. You know that. But with you..." },
      { trigger: 'vulnerability_matched', response: "You're the first person I've told that to." },
      { trigger: 'stayed_through_cold', response: "Most people would have given up by now. You didn't." }
    ],
    james: [
      { trigger: 'real_talk', response: "I don't talk to anyone like this. Not even my therapist lol" },
      { trigger: 'loyalty_proven', response: "You're like a brother to me. You know that right?" }
    ]
  },

  nearMissEffect: {
    threshold: 'Within 10 points of breakthrough',
    messages: [
      { distance: '0-3', message: "So close. They almost opened up completely." },
      { distance: '4-6', message: "You felt something shift. Almost there." },
      { distance: '7-10', message: "There's a crack in the wall. Keep going." }
    ],
    motivationalHook: '"You\'re close. One more exchange like that..."',
    purpose: 'Almost getting the breakthrough is MORE motivating than getting it.'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  12. STREAK & COLLECTIBLE SYSTEMS                                        ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const STREAK_AND_COLLECTIBLES = {
  source: 'Snapchat streaks + Tamagotchi + Gacha games',
  file: 'src/utils/engagementMechanics.js',

  streaks: {
    mechanics: 'Consecutive days of practice, stored in localStorage',
    resetBehavior: 'Streak broken if day missed (resets to 1)',
    milestoneRewards: {
      3: { type: 'character_unlock', message: "3 days of showing up. Here's someone new to talk to." },
      7: { type: 'backstory_unlock', message: "A week of practice. Dad wants to tell you something about your mother." },
      14: { type: 'letter_unlock', message: "Two weeks. Maya wrote you something." },
      30: { type: 'secret_scenario', message: "30 days. You've earned access to a conversation most people never see." }
    },
    ethicalTension: 'Guardrail says NO_STREAK_PUNISHMENT, but streak resets on missed days with content gating'
  },

  collectibles: {
    categories: ['letters', 'backstories', 'photos', 'voicemails', 'secrets'],
    examples: {
      dad_letter_1: { requirement: 'dad: 2 good endings', content: "A letter from Dad about the day you were born" },
      maya_letter_1: { requirement: 'maya: trust level 80', content: "A 2am text Maya wrote but never sent" },
      mom_voicemail: { requirement: 'memory_mom: completed', content: "An old voicemail from Mom you forgot you saved" }
    },
    endowmentEffect: 'The more you collect, the more invested you become. Sunk cost by design.'
  },

  characterAvailability: {
    maya: '9am-1am (night owl)',
    james: '10am-midnight',
    dad: '6am-9pm (goes to bed early)',
    alex: '8am-6pm (work hours only)',
    purpose: 'Creates FOMO + makes characters feel like real people with schedules'
  },

  eqScoring: {
    formula: 'scenarios*50 + best*100 + good*50 + neutral*25 + poor*10 + streakDays*20 + unlocks*30',
    levels: [
      { threshold: 0, name: 'Listener', description: "You're starting to pay attention." },
      { threshold: 500, name: 'Observer', description: "You notice what others miss." },
      { threshold: 1500, name: 'Empath', description: "You feel what they feel." },
      { threshold: 3000, name: 'Connector', description: "You build real bridges." },
      { threshold: 5000, name: 'Healer', description: "Your presence helps people open up." },
      { threshold: 10000, name: 'Guide', description: "You help others find their way." }
    ]
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  13. PERSONALIZATION ENGINE — Player Style Tracking                      ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const PERSONALIZATION_ENGINE = {
  source: 'Personality psychology + adaptive learning systems',
  files: ['src/utils/PlayerStyleTracker.ts', 'src/utils/PlayerAttachmentAnalyzer.js'],

  styleDimensions: {
    warmthDistance: 'How warm vs. reserved (0-100)',
    directIndirect: 'How direct vs. diplomatic (0-100)',
    riskCaution: 'How bold vs. careful (0-100)',
    validationSolution: 'How validation-focused vs. problem-solving (0-100)',
    emotionalLogical: 'How heart-led vs. analytical (0-100)',
    quickDeliberate: 'How quick vs. deliberate (0-100)'
  },

  patterns: {
    openingStyle: ['warm_greeting', 'direct_topic', 'casual_check', 'mirror_energy', 'mixed'],
    emotionResponse: ['validate_first', 'solve_first', 'deflect', 'match', 'escalate'],
    conflictStyle: ['avoid', 'address_directly', 'smooth_over', 'investigate', 'mixed'],
    vulnerabilityApproach: ['reciprocate', 'encourage', 'deflect', 'cautious', 'mixed'],
    recoveryStyle: ['apologize_first', 'explain_first', 'validate_first', 'minimize', 'avoid']
  },

  styleLabels: {
    'warm,direct': 'The Caring Truth-Teller',
    'warm,bold': 'The Courageous Connector',
    'warm,empathetic': 'The Natural Listener',
    'direct,bold': 'The Straight Shooter',
    'bold,heart-led': 'The Brave Heart',
    'empathetic,heart-led': 'The Deep Empath',
    'reserved,careful': 'The Thoughtful Observer',
    'diplomatic,careful': 'The Gentle Approach'
  },

  attachmentAnalyzer: {
    file: 'src/utils/PlayerAttachmentAnalyzer.js',
    types: ['anxious', 'avoidant', 'secure', 'disorganized'],
    inference: 'Calculated from dialogue choices, response patterns, recovery behavior',
    transparency: 'Results shown directly to player — never hidden',
    deletable: 'Player can reset anytime'
  },

  adaptiveSuggestions: {
    lowWarmth: { suggest: 'maya vulnerability_practice', reason: 'Practice leading with more warmth' },
    lowRisk: { suggest: 'dad direct_conversation', reason: 'Practice taking emotional risks with someone who cares' },
    lowValidation: { suggest: 'james active_listening', reason: 'Practice validating before solving' },
    highWarmth: { suggest: 'maya deep_connection', reason: 'Your warmth could really help here' }
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  14. EMOTIONAL REVEAL SYSTEM                                             ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const EMOTIONAL_REVEALS = {
  source: 'Theatrical pacing + game design reward moments',
  file: 'src/utils/EmotionalRevealSystem.ts',

  description: `
    Creates the "ah-ha" moments that make breakthroughs feel earned.
    Three templates: Breakthrough (walls come down), Repair (healing rift),
    Connection (quiet understanding). Each has buildup phases, climax,
    resolution with full sound + haptic design.
  `,

  templates: {
    BREAKTHROUGH: {
      trigger: 'avgMetric >= 85 && momentum > 20',
      phases: ['gathering (2s)', 'tension (1.5s)', 'precipice (1s)'],
      climax: { animation: 'burst', duration: '2500ms', emotionalPeak: 95 },
      characterVariants: {
        maya: { mainText: "She doesn't do this.", subText: "But she did with you." },
        dad: { mainText: "Years of silence.", subText: "Broken in one moment." },
        james: { mainText: "No jokes this time.", subText: "Just honesty." }
      }
    },

    REPAIR: {
      trigger: 'isRecoveryPath && damageLevel < 20 && avgMetric > 50',
      phases: ['reaching (2s)', 'bridging (1.8s)', 'mending (1.2s)'],
      climax: { animation: 'convergence', duration: '2000ms', emotionalPeak: 85 },
      mainText: 'Healing happened.',
      subText: 'Some things can be fixed.'
    },

    CONNECTION: {
      trigger: 'recentValidation && avgMetric >= 70 && momentum >= 0',
      phases: ['noticing (1.5s)', 'resonating (1.5s)', 'landing (1s)'],
      climax: { animation: 'bloom', duration: '1800ms', emotionalPeak: 75 },
      mainText: 'Real connection.',
      subText: 'They felt heard.'
    }
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  15. DARK PATTERN EDUCATION — 28 Patterns Documented                    ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const DARK_PATTERN_EDUCATION = {
  file: 'src/data/darkPatternEducation.js',
  totalPatterns: 28,

  description: `
    Each dark pattern has: darkVersion (how exploitative apps use it),
    ourVersion (how we use it ethically), recognitionTips (how to spot it),
    and some have codeExample (actual implementation code shown to player).
    "Knowledge is armor. Awareness is freedom."
  `,

  categories: {
    'reward-manipulation': ['VARIABLE_REWARDS'],
    'loss-aversion': ['DECAY_MECHANICS'],
    'growth-design': ['ESCALATING_CHALLENGE'],
    'currency-manipulation': ['VIRTUAL_CURRENCY', 'LEFTOVER_CURRENCY'],
    'time-manipulation': ['ENERGY_SYSTEMS', 'FOMO_EVENTS', 'VULNERABLE_NOTIFICATIONS', 'LIMITED_OFFERS_AFTER_LOSS'],
    'social-manipulation': ['SOCIAL_PRESSURE', 'SOCIAL_HIERARCHIES', 'GUILT_NPCS', 'FAKE_SOCIAL_PROOF'],
    'status-manipulation': ['DIGITAL_PEACOCKING', 'MATCHMAKING_ENVY', 'THIRD_PERSON_CAMERA'],
    'psychological-manipulation': ['NEAR_MISS', 'SUNK_COST', 'COMPLETION_MANIPULATION', 'ENDOWED_PROGRESS'],
    'monetization-pressure': ['BATTLE_PASS', 'ANCHORING', 'ARTIFICIAL_SCARCITY', 'DRIP_PRICING'],
    'surveillance-manipulation': ['PSYCHOLOGICAL_PROFILING', 'PRIVACY_ZUCKERING'],
    'attention-capture': ['TRANCE_INDUCTION'],
    'memory-manipulation': ['PEAK_END_MANIPULATION'],
    'attachment-manipulation': ['PARASOCIAL_ENGINEERING'],
    'neurochemical-manipulation': ['EMOTIONAL_CONDITIONING'],
    'stop-signal-removal': ['LOSSES_DISGUISED_AS_WINS'],
    'dependency-creation': ['FRACTIONATION'],
    'algorithmic-manipulation': ['EOMM'],
    'exit-prevention': ['FORCED_CONTINUITY'],
    'cognitive-manipulation': ['DECISION_FATIGUE', 'INTERFACE_INTERFERENCE'],
    'emotional-manipulation': ['CONFIRMSHAMING'],
    'obligation-manipulation': ['RECIPROCITY_TRAP']
  },

  patternsWithCodeExamples: [
    'DECAY_MECHANICS — trust decay rates, guilt escalation ladder, emergency restore pricing',
    'GUILT_NPCS — guilt escalation (6 steps), notification schedule (morning/afternoon/evening/lateNight), monetization',
    'PSYCHOLOGICAL_PROFILING — attachment inference pipeline, loneliness calculation (4 weighted factors), impulse scoring (ms thresholds)',
    'TRANCE_INDUCTION — tunnel vision CSS, heartbeat entrainment (67 BPM), time distortion, deepening formula',
    'PEAK_END_MANIPULATION — end shaping rules (4 strategies), salvage messages (fabricated NPC messages), memory score formula',
    'PARASOCIAL_ENGINEERING — pet name assignment, unsent drafts (Zeigarnik), thinking-of-you A/B testing, deceased character dependency',
    'EMOTIONAL_CONDITIONING — haptic patterns (love/breakthrough/rejection), color temperature shift, neurochemical targeting, unprompted affirmation probabilities',
    'LOSSES_DISGUISED_AS_WINS — reframe table (poor/worst/breakdown → unlock), gambling parallel',
    'FRACTIONATION — A-J-A-R pattern, classification system, dual modes, physiological mechanism',
    'EOMM — EA patent matchmaking, hedonic treadmill, afterLoss/afterWin/newPlayer/postPurchase/churnRisk strategies',
    'FORCED_CONTINUITY — friction asymmetry (30s in / 25min out), 6-step retention gauntlet, FTC/EU DSA references',
    'ENDOWED_PROGRESS — Nunes & Dreze loyalty card study (19% vs 34%), honest self-assessment of our EQ scoring',
    'FAKE_SOCIAL_PROOF — phantom activity generator, random viewer counts, Princeton 2019 study',
    'DECISION_FATIGUE — cookie banner design (47 toggles), purchase funnel fatigue, Baumeister ego depletion',
    'CONFIRMSHAMING — popup design (green yes / gray no), 4 real-world examples, CHI 2024 taxonomy',
    'DRIP_PRICING — pricing funnel ($9.99 → $15.96, 60% markup), UK CMA and FTC rule references',
    'INTERFACE_INTERFERENCE — button design (47:1 click ratio), pre-checked boxes, Gray et al. CHI 2018',
    'PRIVACY_ZUCKERING — settings scatter (5 locations), default maximums, EFF docs, Cambridge Analytica',
    'RECIPROCITY_TRAP — reciprocity funnel (5-step $0→$47 LTV), Cialdini reference, honest self-assessment of our affirmation system'
  ],

  educationSystems: {
    vulnerabilityAssessment: 'assessPatternVulnerability() — identifies which dark patterns the player might be vulnerable to based on behavior',
    contextualEducation: 'getPatternEducation() — delivers relevant education based on what just happened in-game',
    insightUnlocks: '8 insight cards unlocked through natural play (return after absence, first struggle, first milestone, etc.)',
    patternRecognitionQuiz: '5 scenarios where player identifies which dark patterns are being used'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  16. BATEMAN MODE — Full Transparency Layer                              ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const BATEMAN_MODE = {
  files: ['src/components/EngagementTransparency.tsx', 'src/components/EngagementTransparency.css'],

  description: `
    When enabled, Bateman Mode exposes ALL manipulation techniques
    to the player. Named after the "American Psycho" character who
    narrates his own manipulation in real-time. The manipulation IS
    the curriculum — but only if you can see it.
  `,

  tabs: {
    YOUR_PROFILE: {
      description: 'Shows what the game has learned about you',
      data: ['Attachment style', 'Communication patterns', 'Style dimensions', 'Vulnerability assessments']
    },

    ACTIVE_TESTS: {
      description: 'Shows A/B tests currently running on this player',
      data: [
        'Notification tone testing (positive/neutral/vulnerable)',
        'Unsent draft effectiveness metrics',
        'Pet name reveal timing',
        'Absence reaction style (casual/concerned/cold)',
        'Memorable moments quantity',
        'Overall effectiveness scores per tactic'
      ]
    },

    DARK_COMPARISON: {
      description: 'Side-by-side comparison of exploitative vs. ethical implementations',
      data: [
        'Trust decay code examples with guilt escalation timeline',
        'Emergency monetization pricing tiers',
        'Profiling code (attachment inference → loneliness → impulse → monetization targeting)',
        'Ethical contrast code showing what we DON\'T do'
      ]
    }
  },

  sevenSecondExposure: 'Each phase of the 7-second sequence has a batemanNote explaining what casino research discovered about that timing.',
  rewardMechanicsExposure: 'getRewardMechanicsExplanation() — full breakdown of the phased reward sequence and hollow victory contrast.'
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  17. ETHICAL GUARDRAILS — Hard Constraints                               ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const ETHICAL_GUARDRAILS = {
  file: 'src/utils/ethicalGuardrails.ts',

  coreGuarantees: {
    NO_GUILT_MANIPULATION: 'Characters genuinely care. No guilt-tripping for absence.',
    NO_STREAK_PUNISHMENT: 'Take breaks freely. Progress is NEVER truly lost.',
    NO_EMPTY_NEAR_MISS: 'Every "almost" teaches something real about conversation dynamics.',
    NO_FALSE_SCARCITY: 'Content is always available when you\'re ready.',
    NO_ADDICTION_BY_DESIGN: 'We monitor for unhealthy engagement and actively encourage breaks.',
    TRANSPARENCY_ALWAYS: 'All psychological techniques visible via Bateman Mode.',
    ENGAGEMENT_LEARNING_IS_VISIBLE: 'See exactly how the game tests what brings you back.',
    PLAYER_AGENCY_FIRST: 'Skip, pause, or exit without penalty.',
    NO_COVERT_PROFILING: 'No loneliness index, no impulse scoring, no vulnerability targeting.'
  },

  sessionHealthMonitoring: {
    LONG_SESSION: { threshold: '90 minutes, no breaks', message: "You've been here a while. Want to take a breather?" },
    EMOTIONAL_OVERLOAD: { threshold: '3+ heavy conversations', message: "That's a lot of heavy topics. How are you feeling?" },
    FRUSTRATION_PATTERN: { threshold: '3+ consecutive failures', message: "These conversations are tough. That's not a reflection on you." },
    SELF_CARE_REMINDER: { threshold: 'emotionalLoad > 70, no self-care', message: "Choosing lighter options is wisdom, not weakness." },
    EXTENDED_SESSION: { threshold: '3+ hours', message: "Your brain needs rest to consolidate learning." }
  },

  endogenousRewardEthics: {
    REWARD_REFLECTS_GROWTH: 'Reward tied to actual skill, not random metrics.',
    HOLLOW_VICTORIES_FEEL_HOLLOW: '85% reward reduction for manipulation. The emptiness IS feedback.',
    OUTCOMES_MIRROR_REALITY: 'Same words land differently based on mood/momentum/history.',
    TENSION_RELEASE_IS_EARNED: 'Resolution haptics only after genuine high-pressure conversations.',
    CONTRAST_TEACHES: 'Connection feels different from control. The nervous system learns.'
  },

  riskRewardEthics: {
    RISK_IS_NOT_ANXIETY: 'Risk indicators encourage thought, not fear.',
    SAFE_IS_NOT_SHAMEFUL: 'Choosing safety is wisdom, not weakness.',
    VULNERABLE_IS_BRAVE: 'Vulnerability takes courage, not recklessness.',
    PAYOUTS_REFLECT_REALITY: 'Rewards match real growth, not random chance.',
    NEAR_MISS_TEACHES: 'Almost-moments include actionable insight.',
    BREAKTHROUGHS_ARE_EARNED: 'Major moments come from skill, not luck.'
  },

  personalizationEthics: {
    TRACKING_SERVES_PLAYER: 'Data helps you, not hooks you.',
    PROFILES_ARE_TRANSPARENT: 'See everything we learn about you.',
    SUGGESTIONS_NOT_PRESCRIPTIONS: 'We offer, never force.',
    NO_PATTERN_EXPLOITATION: 'Your patterns help growth, not manipulation.',
    PROFILES_ARE_DELETABLE: 'Reset your profile anytime.'
  },

  featureValidation: {
    description: 'validateEngagementFeature() checks every new mechanic against ethical standards',
    requirements: [
      'Must define clear player benefit',
      'Must have at least one guardrail',
      'Must have different intent than exploitative origin',
      'Flags concerning language: "addict", "hook", "exploit", "maximize time", "retention"'
    ]
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  18. ADDITIONAL DARK PATTERNS — Researched but Not Yet in Codebase      ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const RESEARCHED_NOT_YET_ADDED = {
  description: `
    All 10 previously researched patterns have been fully integrated into
    darkPatternEducation.js with complete entries (darkVersion, ourVersion,
    recognitionTips, codeExample). Total dark patterns documented: 38.

    This section is kept as a reference for the research sources.
  `,

  status: 'ALL_INTEGRATED',
  integratedCount: 10,
  totalPatternsNow: 38,

  integratedPatterns: {
    EOMM: {
      name: 'Engagement-Optimized Matchmaking',
      source: 'EA patent, IEEE Conference on Computational Intelligence in Games (2017)',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    FORCED_CONTINUITY: {
      name: 'Forced Continuity / Roach Motel',
      source: 'FTC enforcement actions, EU Digital Services Act',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    ENDOWED_PROGRESS: {
      name: 'Endowed Progress Effect',
      source: 'Nunes & Dreze (2006), Journal of Consumer Research',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    FAKE_SOCIAL_PROOF: {
      name: 'Fake Social Proof / Phantom Activity',
      source: 'Princeton Web Transparency & Accountability Project (2019)',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    DECISION_FATIGUE: {
      name: 'Decision Fatigue Exploitation',
      source: 'Baumeister et al., Journal of Personality and Social Psychology',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    CONFIRMSHAMING: {
      name: 'Confirmshaming',
      source: 'confirmshaming.tumblr.com, CHI 2024 dark patterns taxonomy',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    DRIP_PRICING: {
      name: 'Drip Pricing',
      source: 'UK Competition and Markets Authority investigations',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    INTERFACE_INTERFERENCE: {
      name: 'Interface Interference / Visual Misdirection',
      source: 'Gray et al., CHI 2018 dark patterns paper',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    PRIVACY_ZUCKERING: {
      name: 'Privacy Zuckering',
      source: 'EFF, named after Facebook/Meta privacy practices',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    },

    RECIPROCITY_TRAP: {
      name: 'Reciprocity Trap',
      source: 'Cialdini "Influence" (1984), CHI dark patterns research',
      status: 'INTEGRATED — full entry with codeExample in darkPatternEducation.js'
    }
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  19. EMBODIED COGNITION — Warmth-Trust Bridge + Pause Rewards            ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const EMBODIED_COGNITION = {
  source: 'Williams & Bargh (2008), Polyvagal Theory (Porges), Biofeedback research',
  file: 'src/utils/embodiedCognition.js',

  description: `
    The body-mind connection exploited ethically. Three systems:
    1. PRE-CHOICE WARMTH: Screen warms when hovering vulnerable choices → creates
       psychological safety through the warmth-trust bridge (physical warmth → social warmth).
    2. PAUSE-REWARDS-CALM: Natural pauses before responding improve NPC reception
       by up to 25% — mirrors real-life: thoughtful responses land better than reactive ones.
    3. POST-PEAK QUIET: After intense moments, the UI goes still — no notifications,
       no XP popups. Honors parasympathetic need for integration.

    Bateman choices get NO warmth. The cold stays cold. Manipulation IS cold.
  `,

  preChoiceWarmth: {
    mechanism: 'CSS sepia/saturate/brightness filter + color temperature shift',
    levels: {
      safe:       { sepia: 0.02, colorTemp: '6000K', haptic: null,     description: 'Barely perceptible warmth — comfort zone' },
      moderate:   { sepia: 0.03, colorTemp: '5500K', haptic: null,     description: 'Subtle warmth — room gets cozier' },
      bold:       { sepia: 0.05, colorTemp: '5000K', haptic: 'light',  description: 'Screen warms. Body relaxes. Choice feels safer.' },
      vulnerable: { sepia: 0.08, colorTemp: '4500K', haptic: 'warmth', description: 'Warmth spreads. Not from the screen — from you.' },
      raw:        { sepia: 0.10, colorTemp: '4500K', haptic: 'warmth', description: 'The world gets warmer. This is courage.' },
      bateman:    { sepia: 0,    colorTemp: '6500K', haptic: null,     description: 'No warmth. Manipulation is cold.' }
    },
    researchNote: 'Holding a warm cup literally makes you rate strangers as warmer and more trustworthy (Williams & Bargh, 2008).'
  },

  pauseRewardsCalm: {
    mechanism: 'Logarithmic benefit curve — most benefit in first few seconds of pause',
    thresholds: {
      low:      { minPauseMs: 1500, maxBenefitMs: 5000,  rewardMultiplier: '1.05 (+5%)',  warmthBoost: 0.02 },
      medium:   { minPauseMs: 2500, maxBenefitMs: 8000,  rewardMultiplier: '1.12 (+12%)', warmthBoost: 0.04 },
      high:     { minPauseMs: 3500, maxBenefitMs: 12000, rewardMultiplier: '1.20 (+20%)', warmthBoost: 0.06 },
      critical: { minPauseMs: 4000, maxBenefitMs: 15000, rewardMultiplier: '1.25 (+25%)', warmthBoost: 0.08 }
    },
    calmReasons: {
      low: '"You took a moment. That came through."',
      medium: '"You didn\'t rush. They noticed."',
      high: '"You stayed calm under pressure. That changed everything."',
      critical: '"You breathed. You chose. That\'s mastery."'
    },
    exclusions: 'No benefit for Bateman Mode, or if player was scrolling through options'
  },

  postPeakQuiet: {
    mechanism: 'Suppress notifications, XP popups, achievements. Warm sepia filter + gentle breathing haptic',
    intensities: {
      moderate: { durationMs: 3000, suppressXP: true, breathingHaptic: false },
      high:     { durationMs: 5000, suppressAll: true, breathingHaptic: false },
      profound: { durationMs: 8000, suppressAll: true, breathingHaptic: true, breathingCycles: 2, breathingDelay: 3000 }
    },
    descriptions: {
      moderate: '"A beat of stillness."',
      high: '"Some moments deserve silence."',
      profound: '"Let it land. There\'s no rush."'
    }
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  20. SENSORY ANCHORING ENGINE — Procedural Sound as Conditioning        ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const SENSORY_ANCHORING_ENGINE = {
  source: 'Classical conditioning (Pavlov), musical frisson research, ASMR/nucleus accumbens studies',
  file: 'src/utils/soundEngine.js',

  description: `
    Every emotional state gets a unique procedural sound signature via Web Audio API.
    No audio files — everything is synthesized in real-time. Over time, the sound alone
    triggers the emotional state without content (classical conditioning).

    Key insight: SILENCE is the negative feedback. No buzzer, no "wrong" sound.
    When you hurt someone in real life, they go quiet. The game mirrors this.
  `,

  soundPalette: {
    warmConnection:    { freq: '262Hz (C4)', type: 'marimba', feel: 'Warm, wooden, resonant. Like a heartbeat.', trigger: 'NPC emotional state shifts positive' },
    coldShift:         { freq: '4000Hz (subliminal)', type: 'near-silence', feel: 'Barely audible high tone — unease without awareness.', trigger: 'NPC emotional state shifts negative' },
    insightReveal:     { freq: '800Hz bandpass noise', type: 'breath', feel: '"Oh." Recognition, not reward.', trigger: 'Player discovers psychological pattern' },
    patternDetected:   { freq: '880Hz (A5) + harmonics', type: 'clean piano', feel: '"Wait — did I just do that again?" Cuts through everything.', trigger: 'Mirror moment / repeated problematic behavior' },
    pressureAmbient:   { freq: '55Hz (A1) + 55.5Hz detuned', type: 'low drone', feel: 'Felt more than heard. The room getting closer.', trigger: 'Emotional pressure rising' },
    messageSent:       { freq: 'highpass noise > 3000Hz', type: 'paper/cloth', feel: 'Like sliding a note across a table.', trigger: 'Player sends message' },
    vulnerabilityMoment: { freq: '220/330/440Hz (A3 triad)', type: 'warm pad', feel: 'Barely audible. Warmth spreading. Felt not heard.', trigger: 'Vulnerable response chosen / NPC opens up' },
    achievement:       { freq: '440Hz + 5 harmonics', type: 'meditation bowl', feel: 'Single, clear, resonant. Satisfying closure.', trigger: 'Milestone reached' },
    typingAppear:      { freq: '600Hz', type: 'tiny blip', feel: 'Almost imperceptible. Subconscious anticipation.', trigger: 'NPC starts typing' },
    typingDisappear:   { freq: 'silence', type: 'nothing', feel: 'The disappearance of sound IS the dread.', trigger: 'NPC stops typing without sending' },
    conversationStart: { freq: '174Hz (F3)', type: 'ambient pad', feel: 'A space opening up. Like walking into a quiet room.', trigger: 'Player enters conversation' },
    quietHold:         { freq: '110Hz (A2)', type: 'subliminal drone', feel: 'Near-subliminal. Makes silence feel intentional.', trigger: 'Post-peak decompression' }
  },

  frissonSystem: {
    description: 'Triggers the goosebumps/chills response through harmonic prediction error → dopamine + opioid co-release.',
    researchNote: 'Deceptive cadences resolving to relative major trigger frisson in 55-86% of listeners.',

    tensionResolution: {
      phase1: 'Csus4 chord (C4, F4, G4) — creates yearning, unresolved feeling (0-1.2s)',
      phase2: 'Silence — held breath, maximum neural anticipation (1.2-1.5s)',
      phase3: 'Deceptive resolution to Ab major (unexpected but consonant) — frisson trigger (1.5s)',
      phase4: 'Harmonic bloom — upper partials spread like warmth (2.5s+)',
      profoundVariant: 'AbMaj9 chord (Ab3, C4, E4, Ab4, Bb4) — maximum lushness'
    },

    appoggiatura: {
      description: 'The #1 predictor of musical chills (used in Adele\'s "Someone Like You")',
      mechanism: 'E4 leaning note slides down to D4 over C major pad — dissonance (9th) resolves to consonance (major)',
      feel: 'That ache in your chest. Beautiful sadness resolving to peace.',
      trigger: 'Profound character moments (dad says "I\'m proud of you", etc.)'
    }
  },

  conditioningPrinciples: [
    'PAIR: Consistent emotional state → consistent sound = automatic association over time',
    'ANCHOR: Specific sounds trigger specific emotional states (classical conditioning)',
    'ABSENCE: Silence IS the negative feedback — no buzzer, no penalty sound. Just nothing.',
    'VARIABLE: Reward sounds at unpredictable intervals = stronger conditioning (Skinner)'
  ]
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  21. CROSS-SESSION CALLBACKS — Peak-End Anchoring Across Sessions       ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const CROSS_SESSION_CALLBACKS = {
  source: 'Peak-End Rule extension (Kahneman), relationship persistence psychology',
  file: 'src/utils/crossSessionCallbacks.js',

  description: `
    When a player returns (next session), characters reference something specific
    from the previous conversation. Not a notification. Not a game mechanic.
    Just a subtle callback that says "I remember."

    This creates long-term peak-end anchoring:
    - The "peak" of the PREVIOUS session gets reinforced at the START of the next
    - The player's memory of the previous session is enhanced retroactively
    - Characters feel like they exist between sessions (relationship persistence)

    No "we missed you!" manipulation. No sunk cost pressure.
    Just: "Hey, remember that thing? It stuck with me too."
  `,

  callbackCategories: {
    breakthrough: 'When a wall came down or deep connection happened',
    vulnerability: 'When personal sharing occurred',
    growth: 'When advice was given and received'
  },

  characterTemplateExamples: {
    maya_breakthrough: '"I keep thinking about what you said about {topic}. Nobody talks to me like that."',
    dad_vulnerability: '"I know I don\'t say this enough. But I\'m glad we talked about {topic}."',
    james_growth: '"Took your advice about {topic}. You were right. Don\'t let it go to your head."',
  },

  batemanCallbacks: {
    hollow: '"That conversation we had... I keep thinking about it. Something felt off."',
    damaged: '"You know what? I don\'t think you meant what you said about {topic}."',
    purpose: 'NPC senses manipulation. Acknowledges hollowness without preaching.'
  },

  displayConfig: {
    genuineCallback: { style: 'warm', delay: '5s', haptic: 'warmth', sound: 'warmConnection', duration: '8s' },
    batemanCallback: { style: 'uneasy', delay: '3s', haptic: 'light', sound: null, duration: '6s' }
  },

  storage: {
    method: 'localStorage',
    expiry: '7 days (stale references feel weird)',
    maxPerCharacter: 5,
    maxTotal: 20
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  22. MOMENT OF SILENCE — Intentional Pause for Emotional Weight         ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const MOMENT_OF_SILENCE = {
  source: 'Therapeutic pacing, anti-reactivity training, mindful conversation research',
  file: 'src/components/MomentOfSilence.jsx',

  description: `
    When an NPC says something profound, the UI deliberately PAUSES before
    showing response options. A breathing dot synced to BIO_RHYTHMS replaces
    the input area. This fights the modern impulse to instantly react.

    In real conversations, silence after someone opens up is a SKILL.
    The game teaches this embodied skill through the UI itself.
  `,

  pauseDurations: {
    light:    { ms: 1200, trigger: 'Interesting but not heavy — brief pause' },
    moderate: { ms: 2000, trigger: 'Something real was shared' },
    heavy:    { ms: 3000, trigger: 'Vulnerable moment — let it land' },
    profound: { ms: 4000, trigger: 'Life-changing revelation' }
  },

  messageAnalysis: {
    profoundIndicators: ['/i never told anyone/', '/i love you/', '/the truth is/', '/i can\'t do this anymore/'],
    heavyIndicators: ['/i\'m scared/', '/i need you/', '/you hurt me/', '/i\'ve been hiding/'],
    moderateIndicators: ['/i feel/', '/that means a lot/', '/thank you for/', '/i trust/']
  },

  visualDesign: {
    breathingDot: 'Scale 1→1.3→1, opacity 0.4→0.8→0.4, synced to BREATH_CYCLE_MS (5.5s)',
    progressBar: 'Subtle track filling over the pause duration',
    revealAnimation: 'Spring stiffness 300, damping 25 — gentle emergence'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  23. SACRED PAUSE (Moment That Mattered) — Post-Peak Stillness          ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const SACRED_PAUSE = {
  source: 'Peak-end memory, parasympathetic integration, theatrical pacing',
  file: 'src/components/MomentThatMattered.jsx',

  description: `
    After a breakthrough conversation, this full-screen interstitial creates a
    "sacred pause" — a moment of stillness that honors the emotional weight.
    No gamification. No XP. Just... the moment.

    Three-phase text reveal: Moment → Reflection → Follow-Up.
    Each phase has its own timing, warmth shift, haptic pattern, and sound.
    Best endings get full parasympathetic treatment: breathing glow,
    appoggiatura "ache" note, breathing-synced haptics.
  `,

  phaseTimeline: {
    entering:   { duration: '800ms',  warmth: 'gentle anticipation haptic' },
    moment:     { duration: '3000ms', warmth: '0→0.15 sepia shift', sound: 'vulnerabilityMoment + appoggiatura at 1.5s', haptic: 'resolution (best) / medium (good)' },
    reflection: { duration: '3500ms', warmth: '0.2 sepia', haptic: '2 breathing cycles synced to BREATH_CYCLE_MS (best only)', breathingGlow: true },
    followUp:   { duration: '3000ms', warmth: 'maintained', haptic: 'warmth (best) / light (good)' },
    exiting:    { duration: '500ms',  warmth: 'fade to 0', cancelBreathing: true }
  },

  characterReflections: {
    dad_best: {
      moment: '"He said \'I\'m proud of you.\'"',
      reflection: '"Those four words. How long have you waited to hear them?"',
      followUp: '"Not for what you\'ve achieved. For who you are."'
    },
    maya_best: {
      moment: '"She let you in."',
      reflection: '"Past the \'cool.\' Past the one-word answers. Past the walls."',
      followUp: '"You earned that. By not giving up when she pushed back."'
    },
    memory_mom_best: {
      moment: '"You said goodbye."',
      reflection: '"The goodbye you never got to have. The words you\'ve been carrying."',
      followUp: '"It\'s not the same. But it\'s something. And something matters."'
    }
  },

  showConditions: {
    always: 'endingType === "best"',
    conditional: 'endingType === "good" && emotionalCharacter (dad, maya, james, memory_mom, dismissive_healing, confrontation)',
    metricBased: 'connection >= 75 || trust >= 75 with emotional character'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  24. COMBO SYSTEM — Escalating Feedback for Consecutive Good Choices    ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const COMBO_SYSTEM = {
  source: 'Fighting game combo counters, flow state research, momentum-based feedback',
  file: 'src/components/ComboCounter.jsx',

  description: `
    Like fighting games: consecutive good dialogue choices build a combo counter.
    Each level triggers increasingly satisfying visual + haptic feedback.
    The combo resets on poor choices (neutral preserves but doesn't build),
    creating natural tension where each good choice feels increasingly valuable.
  `,

  comboLevels: {
    2:  { label: 'Nice',            color: '#66BB6A', haptic: 'light',        particles: false },
    3:  { label: 'Flow',            color: '#42A5F5', haptic: 'medium',       particles: false },
    5:  { label: 'In Sync',         color: '#AB47BC', haptic: 'success',      particles: true },
    7:  { label: 'Deep Connection', color: '#FF7043', haptic: 'breakthrough', particles: true },
    10: { label: 'Breakthrough',    color: '#FFD700', haptic: 'breakthrough', particles: true }
  },

  mechanics: {
    increment: 'Good choice → combo + 1',
    neutral: 'Neutral choice → combo unchanged (doesn\'t break or build)',
    bad: 'Poor choice → combo reset to 0',
    connectionMoment: 'At combo 7+, triggerConnectionMoment("strong") fires'
  },

  visualDesign: {
    badge: 'Top-right corner, compact by default, spring animation on increment',
    glowRing: 'Appears at 3+, box-shadow scales with combo count (max 25px)',
    increment: 'Scale bounce [1, 1.2, 1] with spring stiffness 400, damping 20',
    countAnimation: 'Number springs in from scale 1.5 → 1',
    brokenFlash: 'Opacity flash when combo >= 3 breaks'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  25. SESSION START RITUAL — Emotional Context Bridging                  ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const SESSION_START_RITUAL = {
  source: 'TV series "Previously on..." technique, emotional context priming',
  file: 'src/components/SessionStartRitual.jsx',

  description: `
    Before a conversation starts, this component creates a brief emotional bridge
    from the player's last interaction. Shows character avatar (breathing animation),
    a memory from the last conversation, and current relationship state.

    Serves the same role as "Previously on..." in TV series:
    reactivates emotional context so the player isn't starting cold.
    Can be skipped with a tap.
  `,

  timing: {
    duration: '3.5 seconds default',
    skipBehavior: 'Tap anywhere to skip (400ms exit)',
    phaseTransitions: 'entering (300ms) → showing → exiting (600ms)'
  },

  memoryTemplates: {
    best: ['"Last time, you and {name} really connected."', '"{name} opened up to you last time."'],
    good: ['"You and {name} had a solid conversation."', '"{name} appreciated your approach."'],
    neutral: ['"You and {name} talked, but..."', '"There\'s still more to explore with {name}."'],
    poor: ['"Things were tense with {name} last time."', '"There\'s some repair needed with {name}."'],
    firstTime: '"You\'re about to meet {name}."'
  },

  toneColors: {
    warm: '#FFD700',
    positive: '#66BB6A',
    neutral: '#9E9E9E',
    cautious: '#FF9800',
    curious: '#42A5F5'
  }
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  26. AMBIENT BACKGROUND — Dynamic Color Temperature Atmosphere          ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const AMBIENT_BACKGROUND = {
  source: 'Embodied cognition, environmental psychology, retail lighting design',
  file: 'src/components/AmbientBackground.jsx',

  description: `
    The screen literally gets warmer as connection deepens.
    Connection depth (0-100) maps to color temperature (6500K→2200K)
    using a quadratic easing curve — warmth accelerates as connection deepens.

    Pressure > 40% adds a subtle red-orange tension tint from the bottom.
    Connection moments trigger brief warm pulses.
    Breathing sync mode activates breathing-rate-matched opacity cycling.

    Bateman Mode: Shows current Kelvin temperature, warmth bar, and
    explains "Color temperature shifts with connection depth.
    Warmer = deeper bond. Your brain registers this as comfort."
  `,

  warmthMapping: {
    neutral:  { warmth: 0,    tint: 'cool blue 2%',    label: '6500K — Daylight' },
    subtle:   { warmth: 0.15, tint: 'warm amber 4%',   label: '4500K — Warm' },
    cozy:     { warmth: 0.3,  tint: 'warm amber 7%',   label: '3200K — Cozy' },
    golden:   { warmth: 0.5,  tint: 'deep amber 10%',  label: '2700K — Golden Hour' },
    intimate: { warmth: 0.7,  tint: 'deep amber 12%',  label: '2200K — Candlelight' }
  },

  depthFormula: 'temperature = 6500 - ((connectionDepth/100)^2 * (6500 - 2200))',
  pressureTint: 'rgba(255, red, orange, opacity) from bottom — activates when pressure > 40%',
  breathingSync: 'Opacity cycles [0.02, 0.06, 0.02] at BIO_RHYTHMS.BREATH_CYCLE_MS'
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  27. REWARD SEQUENCE PLAYER — Visual Orchestration of the 7-Second Arc  ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const REWARD_SEQUENCE_PLAYER = {
  source: 'Casino reward sequence timing, embodied cognition, entrainment research',
  files: ['src/components/RewardSequencePlayer.jsx', 'src/hooks/useRewardSequence.js'],

  description: `
    The missing piece that connects endogenousReward.js to the UI.
    This React component consumes the full phased timeline from
    orchestrateEndingReward() and renders it frame-by-frame:

    - Color temperature shifts via CSS filters (Kelvin → sepia/hue/saturate)
    - Breathing-synced glow overlays (inhale/exhale matched to BREATH_CYCLE_MS)
    - Particle effects (sparkle for profound, float for deep)
    - Shimmer highlights sweeping across the surface
    - Vignette focus (darkened edges for profound)
    - Heartbeat micro-accents at resting heart rate (profound only)
    - Warmth overlay gradient that intensifies with delivery phase

    Hollow (Bateman) endings: single gray overlay, 300ms, done.
    The contrast IS the lesson — your eyes learn what connection looks like.
  `,

  kelvinToCSSFilter: 'sepia(warmth * 0.25) saturate(1 + warmth * 0.3) hue-rotate(-warmth * 5deg)',

  subComponents: {
    BreathingGlow: 'Animated opacity cycle: minOpacity → maxOpacity → minOpacity at BREATH_CYCLE_MS',
    ShimmerEffect: 'CSS transform x: -100% → 200% on repeat with configurable speed/intensity',
    Vignette: 'Radial gradient from transparent center to colored edge, subtle focus',
    HeartbeatAccent: 'Scale [1, 1.02, 1] + opacity dip at HEARTBEAT_MS interval',
    WarmthOverlay: 'Linear gradient amber overlay, opacity keyed to warmth progress'
  },

  hookUsage: `
    const { rewardConfig, triggerReward, isPlaying, clearReward } = useRewardSequence();
    // On conversation complete:
    triggerReward({ ending: 'best', characterId: 'maya', peakPressure: 85, ... });
    // In render:
    <RewardSequencePlayer rewardConfig={rewardConfig} isVisible={isPlaying}>
      {children}
    </RewardSequencePlayer>
  `
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  28. NEUROCHEMISTRY REFERENCE — Why Things Feel Different               ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const NEUROCHEMISTRY_REFERENCE = {
  source: 'Reward pathway research, opioid system studies, frisson research',
  file: 'src/utils/endogenousReward.js (getNeurochemistryExplanation)',

  description: `
    A complete reference for the neurochemistry behind the engagement design.
    This is the WHY behind every visual, haptic, and audio decision.
    Shown to the player in Bateman Mode — educational, not preachy.
  `,

  systems: {
    dopamine: {
      role: 'Goal Achievement — anticipation + delivery',
      genuineEnding: 'Full 7-second anticipation ramp → peaks at delivery (2-3.5s)',
      batemanEnding: 'Fires briefly (goal achieved) but flat without anticipation ramp',
      analogy: '"Like opening a present you bought for yourself. Technically rewarding. Actually flat."'
    },
    muOpioids: {
      role: 'Social Warmth — the "warm glow" of belonging',
      genuineEnding: 'Activated by color temp shifts, breathing haptics, genuine connection',
      batemanEnding: 'Silent. NOT activated. "You got the outcome. You just can\'t feel it."',
      researchNote: 'Blocking opioid receptors (naltrexone) makes social interactions feel hollow — exactly like Bateman Mode.',
      analogy: '"That warm glow in your chest? That\'s endogenous opioids."'
    },
    oxytocin: {
      role: 'Trust/Bonding — vulnerability reciprocation',
      genuineEnding: 'Triggered when both player and character take genuine emotional risk',
      batemanEnding: 'Suppressed — brain detects performed vs. real vulnerability',
      analogy: '"You collected a metric, not a connection."'
    },
    parasympathetic: {
      role: 'Safety/Rest — ventral vagal "safe and social" state',
      genuineEnding: 'Activated at resolution phase (3.5-5s), breathing slows, heart rate settles',
      batemanEnding: 'Unchanged — body stays in task-focused sympathetic mode',
      analogy: '"The absence of calm is itself data."'
    }
  },

  frissonNote: {
    what: 'Tension-resolution chord progression → goosebumps/chills response',
    pathway: 'Harmonic prediction error → nucleus accumbens → dopamine + opioid + endorphin co-release',
    batemanContrast: '"Bateman endings get no music. You can\'t manufacture chills."'
  },

  embodiedCognitionNote: {
    what: 'Screen warmth shifts (6500K → 2200K) exploit the warmth-trust bridge',
    research: 'Williams & Bargh (2008) — holding a warm cup makes you rate others as more trustworthy',
    batemanContrast: '"Bateman endings stay cold because manipulation IS cold."'
  },

  summary: `
    Genuine endings: dopamine + mu-opioids + oxytocin + parasympathetic shift.
    Manipulation: dopamine only. The hollow feeling is your opioid system staying silent.
    The game doesn't decide which ending is "better." Your body does.
  `
};


// ╔═══════════════════════════════════════════════════════════════════════════╗
// ║  SUMMARY — The Complete Picture                                          ║
// ╚═══════════════════════════════════════════════════════════════════════════╝

export const SUMMARY = {
  totalFiles: 39,
  totalLinesOfEngagementCode: '~14,000+',
  darkPatternsDocumented: 38,
  darkPatternsResearchedNotAdded: 0,
  ethicalGuarantees: 9,
  engagementSections: 28,

  coreInsight: `
    This game borrows from the most addictive systems ever designed —
    casinos, dating apps, social media, mobile games — but uses every
    mechanic to teach, not trap. The player learns to recognize
    manipulation by EXPERIENCING it in a safe environment, then seeing
    exactly how it works through Bateman Mode.

    The manipulation IS the curriculum.
    Knowledge is armor.
    Awareness is freedom.
  `,

  philosophicalPillars: [
    'BORROW THE MECHANIC: Use variable ratio reinforcement, near-miss, trance induction, parasocial bonding, fractionation',
    'REDIRECT THE PURPOSE: From extraction → education, from addiction → skill-building',
    'EXPOSE THE MACHINERY: Bateman Mode shows everything — 7-second sequence, A/B tests, profiling, reward calculations',
    'CONSTRAIN WITH ETHICS: Hard guardrails on every system — session health, no covert profiling, hollow victories',
    'CONTRAST TEACHES: Genuine connection activates full reward sequence. Manipulation gets gray, silence, 800ms. The nervous system learns.',
    'EMBODY THE LESSON: Warmth-trust bridge, pause-rewards-calm, sacred silence — the body learns what the mind can\'t articulate',
    'ANCHOR THROUGH SENSES: Procedural sound, haptic patterns, color temperature — every sense reinforces the emotional state'
  ],

  researchSources: [
    'Casino slot machine research (1980s) — 7-second anticipation timing',
    'B.F. Skinner — variable ratio reinforcement schedules',
    'Daniel Kahneman — Peak-End Rule',
    'Williams & Bargh (2008) — warmth-trust bridge / embodied cognition',
    'Porges — Polyvagal Theory (ventral vagal safety)',
    'Cialdini — Influence (reciprocity, social proof)',
    'Musical frisson research — nucleus accumbens, deceptive cadences',
    'Appoggiatura research — #1 predictor of musical chills',
    'EA/IEEE (2017) — engagement-optimized matchmaking',
    'Nunes & Dreze (2006) — endowed progress effect',
    'Gray et al., CHI 2018 — dark patterns taxonomy',
    'Princeton Web Transparency Project (2019) — fake social proof',
    'Baumeister et al. — decision fatigue exploitation',
    'Pickup artist manipulation → trauma bonding research — fractionation',
    'Zeigarnik effect — incomplete tasks more memorable',
    'Dating app psychology — parasocial engineering'
  ]
};

export default {
  CORE_ARCHITECTURE,
  SEVEN_SECOND_SEQUENCE,
  ENDOGENOUS_REWARD,
  EMOTIONAL_RISK_REWARD,
  TRANCE_INDUCTION,
  PEAK_END_MANIPULATION,
  PARASOCIAL_ENGINEERING,
  EMOTIONAL_CONDITIONING,
  FRACTIONATION,
  LOSSES_DISGUISED_AS_WINS,
  VARIABLE_RATIO_REINFORCEMENT,
  STREAK_AND_COLLECTIBLES,
  PERSONALIZATION_ENGINE,
  EMOTIONAL_REVEALS,
  DARK_PATTERN_EDUCATION,
  BATEMAN_MODE,
  ETHICAL_GUARDRAILS,
  RESEARCHED_NOT_YET_ADDED,
  EMBODIED_COGNITION,
  SENSORY_ANCHORING_ENGINE,
  CROSS_SESSION_CALLBACKS,
  MOMENT_OF_SILENCE,
  SACRED_PAUSE,
  COMBO_SYSTEM,
  SESSION_START_RITUAL,
  AMBIENT_BACKGROUND,
  REWARD_SEQUENCE_PLAYER,
  NEUROCHEMISTRY_REFERENCE,
  SUMMARY
};
