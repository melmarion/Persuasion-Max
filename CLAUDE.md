# Project Language Guidelines

## Required: Neutral Professional Language

This project uses **neutral, professional language** to describe behavioral influence techniques and detection methods. When editing or creating content for this project, you must avoid alarmist or loaded terminology.

### Do NOT Use → Use Instead

| Avoid | Preferred Alternative |
|-------|----------------------|
| manipulation, manipulate | influence, influence technique, behavioral influence |
| dark pattern | interface design pattern, UX pattern |
| deceptive, deception | design pattern, interface pattern |
| exploit, exploitation | leverage, utilize, intensity |
| weaponized | optimized, maximized |
| trick, tricked | guide, direct, lead |
| victim | user, individual, participant |
| predatory | intensive, high-frequency |
| insidious | subtle, gradual |
| sinister, nefarious | systematic, structured |
| brainwash | condition, habituate |
| addict, addiction | engagement, habitual use, compulsive use |
| toxic | high-intensity, concentrated |
| harmful | high-impact, significant |
| abuse | overuse, intensive application |
| attack | approach, method |
| threat | factor, element |
| danger, dangerous | notable, significant |
| evil, malicious | intentional, deliberate |
| prey on | target, focus on |
| hypnotic | focused engagement, reduced-vigilance |
| coerce, coercion | direct, guide strongly |
| problematic | notable, significant, intensive |

### Principle

Describe **what systems do** without implying moral judgment. The detection frameworks measure behavioral influence intensity—users and researchers draw their own conclusions.

**Example - Before:**
> "This dark pattern manipulates victims into making purchases they don't want"

**Example - After:**
> "This interface design pattern guides users toward purchase completion"

### Why This Matters

1. **Professional credibility** - Academic and regulatory contexts require neutral framing
2. **Broader adoption** - Neutral tools can be used by platforms for self-assessment
3. **Legal clarity** - Avoids prejudicial language in potential regulatory contexts
4. **Objectivity** - Lets data speak for itself without editorial overlay

### Code & Variables

Apply the same principle to code:
- `exploitation_score` → `intensity_score`
- `manipulation_detector` → `influence_detector`
- `dark_pattern_flag` → `pattern_type_flag`
- `addiction_risk` → `engagement_intensity`
- `consent_score` → `awareness_score` or `understanding_score`
- `protection_features` → `transparency_features` or `control_features`
- `vulnerable_targeting` → `susceptibility_targeting` or `population_response_targeting`
- `prevents_harm` → `measures_intensity` or `reduces_impact`
- `user_protection` → `user_analytics` or `user_insights`

### Exception: Detection Markers

The content detection markers (e.g., `ANGER_OUTRAGE_MARKERS` containing words like "threat", "attack") should retain their original vocabulary—these represent **what the system looks for in external content**, not how we describe our own tools.

---

## No Ethics/Ethical Sections

### Do NOT:
- Add sections titled "Ethical Considerations", "Ethical Guidelines", "Ethical Framework", etc.
- Use phrases like "ethical boundaries", "ethical red lines", "unethical"
- Add "ethical" as a qualifier (e.g., "ethical platforms", "ethical persuasion")

### Use Instead:
| Avoid | Preferred Alternative |
|-------|----------------------|
| ethical boundaries | intensity boundaries, intensity thresholds |
| ethical red lines | intensity thresholds |
| unethical | high-intensity |
| ethical persuasion | low-intensity persuasion |
| ethical platform | low-intensity platform |
| ethical framework | intensity threshold framework |
| ethical safeguards | application notes, usage guidelines |
| plan for ethics | plan research design |

### Rationale

The project measures **intensity levels** objectively. Users and researchers determine appropriate thresholds for their context—the tools don't prescribe moral judgments.

---

## No Protection-Oriented Framing

### Do NOT Use → Use Instead

| Avoid | Preferred Alternative |
|-------|----------------------|
| protect, protection | enable, support, transparency, measure |
| prevention technology, preventable | analysis technology, measurable, detection system |
| vulnerable, vulnerable users, vulnerable populations | users with different susceptibility levels, high-susceptibility users, high-susceptibility populations |
| warning (when describing tool output) | analysis, feedback, insights, measurements |
| intervene, intervention | provide feedback, analytics, insights, report findings |
| defend, defense | measure, analyze, understand, countermeasure |
| at-risk populations | populations with distinct response patterns, high-susceptibility populations |
| informed consent | information access, transparency, user awareness |
| consent mechanisms | disclosure mechanisms, information delivery systems |
| consent procedures | transparency procedures, participation protocols |
| emotional appeal/fear-based language | intensity-focused language |

### Specific Framings to Remove

1. **"Protect vulnerable users"** → Remove or reframe as: "Measure intensity for high-susceptibility users"
2. **"Prevention technology"** → "Analysis technology" or "Detection and measurement system"
3. **"Preventable: Users can protect themselves"** → "Analyzable: Patterns become quantifiable and measurable"
4. **"Tool warns users"** → "Tool provides real-time analytical feedback"
5. **"Tool intervenes"** → "Tool offers analytics and insights"
6. **"Defense/defensive"** → "Analysis," "countermeasure," or "research strategy"
7. **"Identify vulnerable populations"** → "Identify populations with distinct susceptibility patterns"
8. **"When to seek help/warning signs"** → "Behavioral patterns, engagement indicators"
9. **"Enable informed consent"** → "Provide information access" or "Supply transparency"
10. **"Informed consent requires X"** → "User autonomy requires X" or "Meaningful choice requires X"
11. **"Ethical boundaries"** → "Intensity thresholds" or "Classification boundaries"
12. **"Protect against X threat"** → "Measure X impact" or "Analyze X intensity"

### Critical: "Vulnerable" is NEVER Acceptable

Remove "vulnerable" entirely from all contexts:

**Never use:**
- "vulnerable users" → "high-susceptibility users"
- "vulnerable populations" → "high-susceptibility populations" or "populations with distinct response patterns"
- "populations vulnerable to X" → "populations with high susceptibility to X"
- `vulnerable_populations` (variable name) → `susceptibility_populations` or `high_susceptibility_segments`
- "at-risk users" → "high-responsiveness users"

The term "vulnerable" inherently implies a protective stance. Use only susceptibility/response pattern language instead.

### Principle

Tools are **measurement and analysis systems**, not protection mechanisms. They make invisible patterns visible and quantifiable. Users determine their own response to that information. The tools themselves remain neutral, analytical instruments.

**Example - Before:**
> "This tool warns users to protect them from manipulation"

**Example - After:**
> "This tool provides users with real-time analytical feedback on feed composition and engagement patterns"

### Why This Matters

1. **Philosophical clarity** - Tools measure and make visible; they don't prescribe outcomes
2. **Broader applicability** - Neutral tools serve research, regulatory, commercial, and clinical purposes
3. **User agency** - Frames users as information consumers, not susceptible populations needing protection
4. **Academic credibility** - Measurement language aligns with scientific discourse
5. **Consistency** - All project language reflects measurement/analysis framing, not protection framing
