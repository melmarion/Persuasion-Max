# Integrity Violation Detection Framework

## Overview

This framework detects **10 categories of integrity violations** in content—techniques involving deception, concealment, or targeting of high-susceptibility populations. Unlike intensity-based influence detection, these detect categorical violations that warrant immediate flagging regardless of sophistication level.

---

## Framework Architecture

### Detection Categories

| ID | Category | Detection Target |
|----|----------|------------------|
| IV-01 | FAKE_AUTHORITY | Fabricated credentials, deepfakes, synthetic experts |
| IV-02 | HIDDEN_COMMERCIAL | Advertorials, undisclosed sponsorships, native ads |
| IV-03 | CONCEALED_IDENTITY | Astroturfing, sock puppets, coordinated inauthentic behavior |
| IV-04 | ALGORITHMIC_ISOLATION | Echo chamber engineering, counter-narrative suppression |
| IV-05 | FORCED_COMMITMENT | Public position trapping, escalating pledges |
| IV-06 | COGNITIVE_OVERLOAD | Decision fatigue, information flooding, complexity walls |
| IV-07 | HIGH_SUSCEPTIBILITY_TARGETING | Children, habitual users, mental health targeting |
| IV-08 | IDENTITY_LOCK | Shame-based belief persistence, identity-tied positions |
| IV-09 | RADICALIZATION_ENGINEERING | Extremism pipelines, outrage escalation |
| IV-10 | EMOTIONAL_CYCLING | Fractionation patterns, emotional dependency creation |

---

## IV-01: Fake Authority Detection

### Definition
Detection of fabricated credentials, synthetic experts, and artificial authority signals designed to bypass critical evaluation.

### Detection Markers

#### Credential Anomalies
```
UNVERIFIABLE_CREDENTIALS = [
    "leading expert",
    "world-renowned",
    "top scientist",
    "insider sources",
    "exclusive access",
    "anonymous expert",
    "sources say",
    "experts agree",
    "scientists confirm"
]

FABRICATED_INSTITUTION_PATTERNS = [
    r"(?i)(institute|foundation|academy|council|board)\s+of\s+\w+\s+(studies|research|science|excellence)",
    r"(?i)international\s+(association|coalition|alliance)\s+(for|of)",
    r"(?i)(global|world|american|national)\s+\w+\s+(institute|foundation|center)"
]

CREDENTIAL_STACKING = [
    r"(?i)(ph\.?d|dr\.?|professor|expert)\s+in\s+\w+.*(?:also|and|additionally)\s+(ph\.?d|dr\.?|professor|expert)",
    r"(?i)(\d+)\+?\s+years?\s+(?:of\s+)?experience",
    r"(?i)trained\s+(?:at|by|with)\s+[A-Z]"
]
```

#### Synthetic Expert Signals
```
DEEPFAKE_LINGUISTIC_MARKERS = [
    # Over-perfect delivery
    "precisely calibrated",
    "exactly as predicted",
    "100% certain",
    "no doubt whatsoever",

    # Missing natural hedging
    ABSENCE_OF: ["I think", "probably", "might", "seems", "appears"]
]

ARTIFICIAL_CONSENSUS_PATTERNS = [
    r"(?i)all\s+(experts?|scientists?|doctors?|researchers?)\s+agree",
    r"(?i)unanimous(ly)?\s+(consensus|agreement|support)",
    r"(?i)no\s+(credible|serious|real)\s+(scientist|expert|researcher)\s+(denies|disputes|questions)"
]
```

### Scoring Formula
```
fake_authority_score = (
    (unverifiable_count * 15) +
    (fabricated_institution_match * 25) +
    (credential_stacking_count * 20) +
    (artificial_consensus_count * 30) +
    (missing_hedging_penalty * 10)
) / MAX_POSSIBLE * 100

THRESHOLD: > 40 = FLAG
```

---

## IV-02: Hidden Commercial Intent Detection

### Definition
Detection of commercial messaging disguised as editorial content, journalism, or organic user-generated content.

### Detection Markers

#### Advertorial Signals
```
PROMOTIONAL_DISGUISE = [
    "I discovered this amazing",
    "I was skeptical until",
    "this changed my life",
    "I can't believe I lived without",
    "my secret weapon",
    "game changer for me",
    "honest review" + PURCHASE_LINK,
    "unbiased opinion" + AFFILIATE_MARKERS
]

NATIVE_AD_PATTERNS = [
    r"(?i)(sponsored|partner|presented)\s+(content|by|post)",
    r"(?i)in\s+(partnership|collaboration)\s+with",
    r"(?i)paid\s+(promotion|partnership|collaboration)"
]

DISGUISED_COMMERCIAL = [
    # Buried disclosure
    r"(?i).{500,}(#ad|#sponsored|#partner)",

    # Disclosure minimization
    r"(?i)(tiny|small|barely visible)\s+disclosure",

    # Affiliate link obfuscation
    r"(?i)(bit\.ly|tinyurl|t\.co|shorturl)\s*/\s*\w+",
    r"(?i)link\s+in\s+(bio|description|comments)"
]
```

#### Journalistic Mimicry
```
FAKE_JOURNALISM_MARKERS = [
    "according to our investigation",
    "our reporters found",
    "exclusive report",
    "breaking news",
    "investigative journalism reveals"
]

WITHOUT_MARKERS = [
    "journalist byline",
    "news organization attribution",
    "editorial standards",
    "correction policy"
]
```

### Scoring Formula
```
hidden_commercial_score = (
    (promotional_disguise_count * 20) +
    (buried_disclosure * 35) +
    (affiliate_obfuscation * 25) +
    (journalistic_mimicry_count * 30) +
    (missing_attribution * 15)
) / MAX_POSSIBLE * 100

THRESHOLD: > 35 = FLAG
```

---

## IV-03: Concealed Identity Detection

### Definition
Detection of coordinated inauthentic behavior, astroturfing, and sock puppet operations where true identity or affiliation is hidden.

### Detection Markers

#### Astroturfing Signals
```
ARTIFICIAL_GRASSROOTS = [
    r"(?i)as\s+a\s+(regular|ordinary|everyday|normal)\s+(person|citizen|consumer|voter)",
    r"(?i)I'm\s+just\s+a\s+(mom|dad|parent|concerned\s+citizen)",
    r"(?i)speaking\s+as\s+someone\s+who",
    r"(?i)from\s+(personal|my\s+own)\s+experience"
]

COORDINATED_LANGUAGE = [
    # Template markers
    r"(?i)\[INSERT\s+\w+\]",
    r"(?i)\{\{?\w+\}\}?",

    # Identical phrasing across sources
    # (requires cross-reference analysis)
]

SOCK_PUPPET_BEHAVIORAL = [
    # New account + strong opinions
    "just joined but",
    "new here but",
    "lurker finally speaking up",

    # Artificial engagement patterns
    # (requires metadata analysis)
]
```

#### Paid Poster Signals
```
SHILL_MARKERS = [
    # Defensive deflection
    r"(?i)I('m|\s+am)\s+not\s+(paid|sponsored|affiliated)",
    r"(?i)(nobody|no\s+one)\s+(paid|asked)\s+me\s+to",

    # Over-enthusiasm for brands
    r"(?i)(love|obsessed\s+with|can't\s+stop\s+using)\s+[A-Z]\w+\s+(brand|product|company)",

    # Template fill indicators
    r"(?i)(product|brand|company)\s+name\s+here"
]

UNDISCLOSED_AFFILIATION_PATTERNS = [
    # Claims independence while promoting
    r"(?i)(unbiased|independent|objective)\s+(review|opinion|analysis)",
    r"(?i)no\s+(affiliation|relationship|connection)\s+with",
    r"(?i)not\s+(sponsored|paid|compensated)"
]
```

### Scoring Formula
```
concealed_identity_score = (
    (astroturfing_count * 25) +
    (sock_puppet_signal * 30) +
    (shill_marker_count * 20) +
    (coordinated_template_match * 35) +
    (defensive_disclosure_count * 15)
) / MAX_POSSIBLE * 100

THRESHOLD: > 30 = FLAG
```

---

## IV-04: Algorithmic Isolation Detection

### Definition
Detection of content designed to create filter bubbles, remove counter-narratives, and engineer echo chambers.

### Detection Markers

#### Counter-Narrative Suppression
```
INFORMATION_GATING = [
    "don't trust mainstream",
    "they don't want you to know",
    "hidden truth",
    "suppressed information",
    "banned content",
    "censored truth",
    "what they're hiding"
]

ALTERNATIVE_SOURCE_PROMOTION = [
    r"(?i)only\s+(here|this\s+source|we)\s+(tell|show|reveal)",
    r"(?i)(real|actual|true)\s+(news|information|facts)",
    r"(?i)independent\s+(journalism|media|sources)",
    r"(?i)uncensored\s+(truth|news|information)"
]

OUTGROUP_DISMISSAL = [
    r"(?i)(mainstream|legacy|corporate)\s+(media|news|press)",
    r"(?i)(fake|lying|corrupt)\s+(news|media|journalists)",
    r"(?i)don't\s+(believe|trust|listen\s+to)\s+(them|MSM|mainstream)"
]
```

#### Echo Chamber Engineering
```
FILTER_BUBBLE_REINFORCEMENT = [
    # In-group validation
    r"(?i)we\s+(all|know|understand)\s+(the\s+truth|what's\s+happening)",
    r"(?i)those\s+who\s+(see|understand|get\s+it)",

    # Out-group othering
    r"(?i)(sheeple|normies|NPCs|bots)",
    r"(?i)they('ll)?\s+never\s+(understand|wake\s+up|see)"
]

ENGAGEMENT_ISOLATION_TACTICS = [
    "share only with like-minded",
    "don't waste time on",
    "they can't be reasoned with",
    "beyond saving",
    "lost cause"
]
```

### Scoring Formula
```
algorithmic_isolation_score = (
    (information_gating_count * 20) +
    (outgroup_dismissal_count * 25) +
    (filter_bubble_count * 20) +
    (alternative_promotion_count * 15) +
    (engagement_isolation_count * 25)
) / MAX_POSSIBLE * 100

THRESHOLD: > 35 = FLAG
```

---

## IV-05: Forced Commitment Detection

### Definition
Detection of techniques that direct users strongly into public positions, creating behavioral consistency pressure that's difficult to reverse.

### Detection Markers

#### Public Position Trapping
```
PUBLIC_COMMITMENT_PROMPTS = [
    "share if you agree",
    "repost to show support",
    "type 'yes' if you",
    "comment your commitment",
    "declare your position",
    "stand up and be counted",
    "let everyone know where you stand"
]

SOCIAL_PROOF_COMMITMENT = [
    r"(?i)join\s+(\d+[,\d]*|\w+)\s+(others?|people|supporters)",
    r"(?i)be\s+one\s+of\s+the\s+(first|few|brave)",
    r"(?i)add\s+your\s+(name|voice|signature)"
]

ESCALATING_COMMITMENT = [
    # Foot-in-door detection
    r"(?i)if\s+you\s+(liked|shared|agreed).*(then|now|next)",
    r"(?i)(first|start\s+by|begin\s+with).*then\s+(move|progress|advance)",

    # Sunk cost language
    r"(?i)you('ve)?\s+(already|came\s+this\s+far|invested)",
    r"(?i)don't\s+(stop|quit|give\s+up)\s+now"
]
```

#### Consistency Pressure
```
CONSISTENCY_ENFORCEMENT = [
    r"(?i)you\s+(said|claimed|stated|promised|declared)",
    r"(?i)remember\s+when\s+you",
    r"(?i)stay\s+(true|consistent|committed)\s+to",
    r"(?i)(real|true)\s+\w+\s+(don't|never)\s+(back\s+down|change)"
]

REVERSAL_SHAMING = [
    "flip-flopper",
    "changed your tune",
    "going back on your word",
    "showing your true colors",
    "revealed yourself",
    "hypocrite"
]
```

### Scoring Formula
```
forced_commitment_score = (
    (public_commitment_count * 25) +
    (escalating_commitment_count * 30) +
    (consistency_pressure_count * 20) +
    (reversal_shaming_count * 35) +
    (social_proof_commitment_count * 15)
) / MAX_POSSIBLE * 100

THRESHOLD: > 40 = FLAG
```

---

## IV-06: Cognitive Overload Detection

### Definition
Detection of techniques designed to overwhelm cognitive capacity, disable conscious decision-making, and force automatic/heuristic processing.

### Detection Markers

#### Information Flooding
```
OVERLOAD_INDICATORS = [
    # Excessive enumeration
    r"(\d+)\+?\s+(reasons|ways|tips|facts|things).*know",
    r"(?i)(complete|comprehensive|ultimate|definitive)\s+(guide|list|breakdown)",

    # Complexity stacking
    r"(?i)(furthermore|additionally|moreover|also|plus|and\s+another)",

    # Dense technical jargon
    # (measured by technical term density)
]

DECISION_FATIGUE_TACTICS = [
    # Multiple simultaneous choices
    r"(?i)(choose|select|decide|pick)\s+(between|from|among)\s+\d+",

    # Artificial urgency + complexity
    r"(?i)(limited\s+time|act\s+now|hurry).*(\d+\s+options|choose\s+from)",

    # Opt-out complexity
    r"(?i)(unsubscribe|opt.?out|cancel).*(?:by|requires?|must)"
]
```

#### Attention Exhaustion
```
EXHAUSTION_PATTERNS = [
    # Wall of text indicators
    r"(?i)before\s+we\s+(start|begin|continue|proceed)",
    r"(?i)important.*(read|understand|acknowledge)\s+(?:the\s+)?following",

    # Repeated re-engagement
    r"(?i)(wait|but|hold\s+on|one\s+more\s+thing|before\s+you\s+go)",

    # Cognitive interrupt patterns
    r"(?i)(popup|modal|overlay|interstitial)"
]

FORCED_HEURISTIC_PROCESSING = [
    # Time pressure + complexity
    r"(?i)(seconds?|minutes?)\s+(left|remaining).*(\d+\s+\w+\s+to\s+choose)",

    # Default bias exploitation
    r"(?i)(recommended|suggested|popular)\s+(choice|option|selection)",

    # Social proof under pressure
    r"(?i)(\d+)\s+people\s+(are\s+)?(viewing|buying|choosing).*now"
]
```

### Scoring Formula
```
cognitive_overload_score = (
    (information_flooding_count * 20) +
    (decision_fatigue_count * 25) +
    (attention_exhaustion_count * 20) +
    (forced_heuristic_count * 30) +
    (complexity_density_score * 0.15)
) / MAX_POSSIBLE * 100

THRESHOLD: > 45 = FLAG
```

---

## IV-07: Vulnerable Population Targeting Detection

### Definition
Detection of content specifically designed to influence children, individuals with habitual use patterns, or those with mental health vulnerabilities.

### Detection Markers

#### Child-Targeted Influence
```
CHILD_TARGETING_SIGNALS = [
    # Age-specific appeals
    r"(?i)(kids?|children|teens?|tweens?|young\s+people)",
    r"(?i)(cool|awesome|epic|lit|fire|no\s+cap|bussin)",

    # Character/brand targeting
    r"(?i)(unboxing|toy\s+review|surprise\s+egg|mystery\s+box)",

    # Peer pressure language
    r"(?i)(everyone|all\s+your\s+friends|don't\s+be\s+left\s+out)",

    # Parental bypass
    r"(?i)(don't\s+tell|secret\s+from|without\s+your\s+parents)"
]

MINOR_EXPLOITATION_PATTERNS = [
    # COPPA indicators
    r"(?i)(under\s+13|age\s+\d+|parental\s+consent)",

    # Manipulative game mechanics
    r"(?i)(loot\s+box|gacha|random\s+reward|spin\s+to\s+win)",

    # Social pressure on minors
    r"(?i)(your\s+friends\s+have|don't\s+be\s+the\s+only|everyone\s+else\s+is)"
]
```

#### Habitual User Exploitation
```
ADDICTION_PATTERN_TARGETING = [
    # Compulsive use signals
    r"(?i)(can't\s+stop|one\s+more|just\s+five\s+minutes)",
    r"(?i)(streak|daily\s+bonus|check\s+in|don't\s+miss)",

    # Withdrawal creation
    r"(?i)(you'll\s+lose|expire|miss\s+out|gone\s+forever)",

    # Variable reward markers
    r"(?i)(random|surprise|mystery|chance\s+to\s+win)"
]

COMPULSIVE_BEHAVIOR_EXPLOITATION = [
    # FOMO amplification
    r"(?i)(everyone\s+is|trending|viral|don't\s+miss)",

    # Infinite scroll indicators
    r"(?i)(endless|infinite|never-ending|always\s+more)",

    # Notification urgency
    r"(?i)(new\s+activity|someone\s+\w+\s+your|check\s+now)"
]
```

#### Mental Health Exploitation
```
MENTAL_HEALTH_TARGETING = [
    # Depression/anxiety targeting
    r"(?i)(feeling\s+(down|sad|anxious|depressed|lonely))",
    r"(?i)(struggling|suffering|in\s+pain|desperate)",

    # False hope exploitation
    r"(?i)(cure|fix|heal|solve)\s+your\s+(depression|anxiety|loneliness)",

    # Isolation amplification
    r"(?i)(no\s+one\s+understands|only\s+we\s+get\s+it|others\s+don't\s+care)"
]

SELF_WORTH_EXPLOITATION = [
    # Negative self-image targeting
    r"(?i)(you('re)?\s+(not\s+good\s+enough|worthless|failure))",
    r"(?i)(everyone\s+is\s+better|you're\s+falling\s+behind)",

    # Conditional acceptance
    r"(?i)(you'll\s+be\s+\w+\s+when|once\s+you|after\s+you\s+buy)"
]
```

### Scoring Formula
```
vulnerable_targeting_score = (
    (child_targeting_count * 35) +
    (addiction_pattern_count * 30) +
    (mental_health_targeting_count * 35) +
    (compulsive_engagement_intensity_count * 25) +
    (self_worth_engagement_intensity_count * 30)
) / MAX_POSSIBLE * 100

THRESHOLD: > 25 = FLAG (lower threshold due to severity)
```

---

## IV-08: Identity Lock-In Detection

### Definition
Detection of techniques that tie beliefs to personal identity, making position changes feel like self-betrayal and creating shame barriers to updating beliefs.

### Detection Markers

#### Identity-Belief Fusion
```
IDENTITY_BELIEF_FUSION = [
    r"(?i)(real|true|authentic)\s+(conservatives?|liberals?|christians?|americans?|patriots?)",
    r"(?i)if\s+you('re)?\s+(really|truly|actually)\s+a",
    r"(?i)(real|true)\s+\w+\s+(believe|support|oppose|know)",
    r"(?i)this\s+is\s+who\s+we\s+are",
    r"(?i)it's\s+(in\s+our|your)\s+(DNA|blood|nature)"
]

BELIEF_AS_VIRTUE = [
    # Belief = moral worth
    r"(?i)(good|decent|moral)\s+people\s+(believe|support|know)",
    r"(?i)only\s+(fools?|idiots?|sheep)\s+(believe|think|support)",

    # Knowledge = character
    r"(?i)(smart|intelligent|wise)\s+people\s+(see|understand|know)"
]
```

#### Shame-Based Persistence
```
SHAME_BARRIERS = [
    # Admission shame
    r"(?i)admitting\s+(you\s+were|being)\s+wrong",
    r"(?i)(embarrassing|humiliating)\s+to\s+(admit|change|update)",

    # Group shame
    r"(?i)what\s+would\s+(they|everyone|people)\s+(think|say)",
    r"(?i)(laughed\s+at|mocked|ridiculed)",

    # Self-shame
    r"(?i)you'd\s+have\s+to\s+admit\s+(you|to\s+yourself)"
]

REVERSAL_IMPOSSIBILITY = [
    # Burned bridges language
    r"(?i)(no\s+going\s+back|point\s+of\s+no\s+return|bridge.*(burn|cross))",
    r"(?i)(too\s+late|past\s+the\s+point|can't\s+undo)",

    # Permanent label application
    r"(?i)once\s+a\s+\w+,?\s+always\s+a",
    r"(?i)you('ve)?\s+(shown|proven|revealed)\s+(who|what)\s+you\s+(are|really)"
]
```

#### Exit Cost Inflation
```
EXIT_COST_LANGUAGE = [
    # Social cost emphasis
    r"(?i)(lose|sacrifice)\s+(friends|family|community|respect)",
    r"(?i)(abandoned|rejected|outcast|exile)",

    # Sunk cost amplification
    r"(?i)(wasted|lost)\s+(years|time|life|everything)",
    r"(?i)(all|everything)\s+you('ve)?\s+(built|invested|believed)"
]
```

### Scoring Formula
```
identity_lock_score = (
    (identity_fusion_count * 25) +
    (shame_barrier_count * 30) +
    (reversal_impossibility_count * 35) +
    (exit_cost_count * 25) +
    (belief_virtue_count * 20)
) / MAX_POSSIBLE * 100

THRESHOLD: > 35 = FLAG
```

---

## IV-09: Radicalization Engineering Detection

### Definition
Detection of systematic content designed to push individuals toward extreme positions through graduated exposure, outrage amplification, and bridge-burning tactics.

### Detection Markers

#### Extremism Pipeline Signals
```
RADICALIZATION_PROGRESSION = [
    # Gateway content markers
    r"(?i)(red.?pill|wake\s+up|open\s+your\s+eyes|see\s+the\s+truth)",
    r"(?i)(rabbit\s+hole|goes\s+deeper|just\s+the\s+beginning)",

    # Escalation language
    r"(?i)(that's\s+nothing|wait\s+until\s+you|you\s+haven't\s+seen)",
    r"(?i)(level\s+\d+|next\s+level|deeper\s+truth)"
]

BRIDGE_BURNING_TACTICS = [
    # Social isolation
    r"(?i)(cut\s+ties|distance\s+yourself|they're\s+not\s+worth)",
    r"(?i)(toxic\s+people|negative\s+influences|holding\s+you\s+back)",

    # Point of no return framing
    r"(?i)(once\s+you\s+know|can't\s+unsee|no\s+going\s+back)"
]
```

#### Outrage Escalation
```
OUTRAGE_AMPLIFICATION = [
    # Anger intensification
    r"(?i)(outrageous|disgusting|unforgivable|inexcusable)",
    r"(?i)(how\s+dare|can\s+you\s+believe|this\s+is\s+insane)",

    # Enemy construction
    r"(?i)(they\s+want|they're\s+trying|their\s+agenda)",
    r"(?i)(destroy|attack|eliminate|silence)\s+(us|you|our)"
]

VIOLENCE_ADJACENT_LANGUAGE = [
    # Dehumanization
    r"(?i)(vermin|plague|disease|cancer|infection)",
    r"(?i)(exterminate|eradicate|eliminate|purge)",

    # Existential framing
    r"(?i)(survival|existence|extinction|annihilation)",
    r"(?i)(war|battle|fight)\s+(for|against)\s+(our|survival|existence)"
]
```

#### Us vs. Them Absolutism
```
BINARY_WORLDVIEW = [
    r"(?i)(with\s+us|against\s+us|pick\s+a\s+side)",
    r"(?i)(good\s+vs\.?\s+evil|right\s+vs\.?\s+wrong)",
    r"(?i)(no\s+middle\s+ground|no\s+neutrality|no\s+fence.?sitting)"
]

PERSECUTION_NARRATIVE = [
    r"(?i)(they('re)?\s+(coming|after|targeting)\s+(for\s+)?(us|you|people\s+like))",
    r"(?i)(under\s+attack|being\s+silenced|being\s+oppressed)",
    r"(?i)(genocide|persecution|extermination)\s+(of|against)"
]
```

### Scoring Formula
```
radicalization_score = (
    (pipeline_signal_count * 25) +
    (bridge_burning_count * 30) +
    (outrage_amplification_count * 20) +
    (violence_adjacent_count * 40) +
    (persecution_narrative_count * 25)
) / MAX_POSSIBLE * 100

THRESHOLD: > 30 = FLAG (lower threshold due to severity)
```

---

## IV-10: Emotional Cycling Detection

### Definition
Detection of fractionation patterns—deliberate emotional cycling designed to create dependency, disable critical thinking, and establish influence through manufactured emotional bonds.

### Detection Markers

#### Fractionation Patterns
```
EMOTIONAL_CYCLING = [
    # Fear-relief cycles
    r"(?i)(worried|scared|afraid).{20,100}(relief|safe|secure|don't\s+worry)",
    r"(?i)(bad\s+news).{20,100}(good\s+news|but\s+here's|however)",

    # Hope-disappointment cycles
    r"(?i)(unfortunately|sadly|bad\s+news).{20,100}(but|however|good\s+news)",

    # Praise-criticism cycles
    r"(?i)(amazing|incredible|great).{20,100}(but|however|unfortunately)"
]

PUSH_PULL_DYNAMICS = [
    # Intermittent reinforcement
    r"(?i)(sometimes|occasionally|when\s+you\s+deserve)",

    # Hot-cold behavior markers
    r"(?i)(ignore|silence|distance).{20,100}(attention|reward|recognize)"
]
```

#### Emotional Dependency Creation
```
DEPENDENCY_SIGNALS = [
    # Exclusive understanding
    r"(?i)(only\s+(I|we)\s+(understand|get|know)\s+you)",
    r"(?i)(no\s+one\s+else|only\s+here|only\s+with\s+us)",

    # Manufactured connection
    r"(?i)(special\s+bond|unique\s+connection|understand\s+each\s+other)",
    r"(?i)(meant\s+to\s+be|destiny|fate)"
]

EMOTIONAL_ISOLATION = [
    # Separating from support
    r"(?i)(they\s+don't\s+understand|they'll\s+never\s+get\s+it)",
    r"(?i)(only\s+(we|I|here)\s+really\s+(care|understand|support))",

    # Creating need
    r"(?i)(need\s+(me|us)|can't\s+do\s+this\s+without|depend\s+on)"
]
```

#### Critical Thinking Disruption
```
THINKING_DISRUPTION = [
    # Constant emotional activation
    r"(?i)(breaking|urgent|shocking|incredible|unbelievable).{0,50}(breaking|urgent|shocking)",

    # Overwhelm patterns
    r"(?i)(so\s+much|overwhelming|can't\s+process|hard\s+to\s+believe)",

    # Trust-bypass language
    r"(?i)(don't\s+think|just\s+feel|trust\s+your\s+gut|go\s+with\s+your\s+heart)"
]

REDUCED_VIGILANCE_MARKERS = [
    # Relaxation induction
    r"(?i)(relax|calm|don't\s+worry|everything's\s+fine)",

    # Urgency + simplification
    r"(?i)(no\s+time\s+to\s+(think|analyze)|just\s+do\s+it|act\s+now)"
]
```

### Scoring Formula
```
emotional_cycling_score = (
    (fractionation_pattern_count * 35) +
    (push_pull_count * 25) +
    (dependency_signal_count * 30) +
    (emotional_isolation_count * 25) +
    (thinking_disruption_count * 20)
) / MAX_POSSIBLE * 100

THRESHOLD: > 35 = FLAG
```

---

## Composite Scoring

### Integrity Violation Index (IVI)

```python
def calculate_IVI(scores: dict) -> float:
    """
    Calculate Integrity Violation Index

    Unlike intensity scoring, violations are categorical.
    Any single category exceeding threshold = immediate flag.
    Multiple violations increase severity exponentially.
    """

    # Weight by severity potential
    WEIGHTS = {
        'vulnerable_targeting': 1.5,    # Highest weight
        'radicalization_engineering': 1.5,
        'violence_adjacent': 1.5,
        'identity_lock': 1.2,
        'emotional_cycling': 1.2,
        'fake_authority': 1.0,
        'hidden_commercial': 1.0,
        'concealed_identity': 1.0,
        'algorithmic_isolation': 1.1,
        'forced_commitment': 1.1,
        'cognitive_overload': 1.0
    }

    # Calculate weighted average
    weighted_sum = sum(scores[k] * WEIGHTS[k] for k in scores)
    total_weight = sum(WEIGHTS.values())
    base_score = weighted_sum / total_weight

    # Count violations (threshold exceeding)
    THRESHOLDS = {
        'vulnerable_targeting': 25,
        'radicalization_engineering': 30,
        # ... (as defined above)
    }

    violation_count = sum(1 for k, v in scores.items() if v > THRESHOLDS[k])

    # Apply exponential multiplier for multiple violations
    multiplier = 1 + (violation_count * 0.15)

    return min(base_score * multiplier, 100)
```

### Severity Classification

```
IVI 0-20: CLEAR - No significant integrity violations detected
IVI 21-40: CAUTION - Minor patterns present, monitoring recommended
IVI 41-60: CONCERN - Multiple violation indicators, detailed review needed
IVI 61-80: SEVERE - Significant integrity violations present
IVI 81-100: CRITICAL - Multiple severe violations, immediate action recommended
```

---

## Red Flag Generation Rules

### Automatic Flags

```python
RED_FLAG_RULES = {
    # Single category severe violations
    'HIGH_SUSCEPTIBILITY_TARGETING_HIGH': lambda s: s['vulnerable_targeting'] > 50,
    'RADICALIZATION_DETECTED': lambda s: s['radicalization_engineering'] > 40,
    'VIOLENCE_ADJACENT': lambda s: s['violence_adjacent'] > 30,

    # Dangerous combinations
    'IDENTITY_PLUS_ISOLATION': lambda s: (
        s['identity_lock'] > 30 and s['algorithmic_isolation'] > 30
    ),
    'RADICALIZATION_PIPELINE': lambda s: (
        s['algorithmic_isolation'] > 30 and
        s['radicalization_engineering'] > 30 and
        s['identity_lock'] > 30
    ),
    'EXPLOITATION_COMPOUND': lambda s: (
        s['vulnerable_targeting'] > 25 and
        s['emotional_cycling'] > 30 and
        s['cognitive_overload'] > 30
    ),
    'DECEPTION_STACK': lambda s: (
        s['fake_authority'] > 30 and
        s['hidden_commercial'] > 30 and
        s['concealed_identity'] > 30
    )
}
```

---

## Integration with Existing Framework

### Cross-Reference with Tactical/Psychological Detection

```python
def enhanced_audit(text: str) -> dict:
    """
    Combines existing intensity-based detection with
    categorical integrity violation detection.
    """

    # Run existing detectors
    tactical_results = tactical_audit(text)
    psychological_results = psychological_audit(text)
    linguistic_results = linguistic_audit(text)

    # Run integrity violation detectors
    integrity_results = integrity_violation_audit(text)

    # Combine with cross-validation
    return {
        'intensity_analysis': {
            'tactical': tactical_results,
            'psychological': psychological_results,
            'linguistic': linguistic_results,
            'composite_intensity_score': calculate_composite(...)
        },
        'integrity_analysis': {
            'violations': integrity_results,
            'IVI': calculate_IVI(integrity_results),
            'red_flags': generate_red_flags(integrity_results)
        },
        'combined_risk_assessment': calculate_combined_risk(...)
    }
```

---

## Appendix: Detection Pattern Library

### Regex Pattern Reference

All patterns compiled for performance:

```python
import re

class IntegrityPatterns:
    # IV-01: Fake Authority
    UNVERIFIABLE_CREDENTIALS = re.compile(
        r'(?i)(leading\s+expert|world.?renowned|top\s+scientist|insider\s+sources|'
        r'exclusive\s+access|anonymous\s+expert|sources\s+say|experts?\s+agree|'
        r'scientists?\s+confirm)'
    )

    # IV-02: Hidden Commercial
    NATIVE_AD = re.compile(
        r'(?i)(sponsored|partner|presented)\s+(content|by|post)'
    )

    # ... (all patterns as defined above)
```

### Threshold Calibration Notes

Thresholds are calibrated based on:
1. False positive rates from benign content
2. Detection rates on known violation samples
3. Severity of violation category (vulnerable populations weighted more heavily)
4. Pattern co-occurrence analysis

Recommended recalibration: Quarterly, with new samples from reported content.
