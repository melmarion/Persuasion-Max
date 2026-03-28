from __future__ import annotations

"""
Master Technique Library
========================
Unified from:
    - charisma-training-game: 25 techniques with neurological basis + damage scores
    - read-the-room: 40+ techniques as inline tags (LABELING, DOOR-IN-THE-FACE, etc.)
    - Persuade-Me: NLP techniques in scenario briefings
    - Persuasion-Max auditor: 22 detection categories

Single source of truth. Every game imports from here.
"""

from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Technique:
    id: str
    name: str
    category: str
    description: str
    mechanism: str                      # psychological mechanism
    neural_basis: Optional[str] = None  # brain structures involved
    effectiveness: str = "B"            # S/A/B/C/D tier
    risk_level: float = 0.3            # 0-1, how likely to backfire
    detection_markers: list[str] = None # how to spot it being used on you
    counter_strategy: Optional[str] = None
    combos_with: list[str] = None      # technique IDs that synergize
    # Appraisal dimension impacts (from Persuasion-Max core)
    appraisal_shifts: dict = None       # {dimension: shift_value}
    # Source tracking
    sources: list[str] = None           # which repos defined this

    def __post_init__(self):
        self.detection_markers = self.detection_markers or []
        self.combos_with = self.combos_with or []
        self.appraisal_shifts = self.appraisal_shifts or {}
        self.sources = self.sources or []

    def to_dict(self) -> dict:
        return asdict(self)


# ─── The Master Library ─────────────────────────────────────────────────────
# Merged from all repos. Categories unified.

MASTER_TECHNIQUES: dict[str, Technique] = {

    # ═══ INFLUENCE FUNDAMENTALS (from read-the-room + Persuade-Me) ═══════

    "labeling": Technique(
        id="labeling",
        name="Labeling",
        category="rapport",
        description="Name the other person's emotion before they do. Creates feeling of being understood.",
        mechanism="Activates the TPJ (theory of mind). When someone names your feeling accurately, "
                  "the amygdala downregulates — the threat of being misunderstood dissolves.",
        neural_basis="TPJ → amygdala downregulation → oxytocin release",
        effectiveness="A",
        risk_level=0.1,
        detection_markers=["they named my feeling before I did", "felt instantly understood"],
        combos_with=["mirroring", "calibrated_questions"],
        appraisal_shifts={"valence": 0.15, "agency": 0.10, "certainty": 0.10},
        sources=["read-the-room", "charisma-training-game"],
    ),
    "mirroring": Technique(
        id="mirroring",
        name="Mirroring",
        category="rapport",
        description="Repeat the last 1-3 words someone said. Triggers elaboration without asking.",
        mechanism="Mimicry activates mirror neurons. The other person feels synchronized, "
                  "which triggers oxytocin release and approach behavior.",
        neural_basis="Mirror neuron system → oxytocin → approach circuit",
        effectiveness="A",
        risk_level=0.05,
        detection_markers=["they kept repeating my words", "I kept talking without being asked"],
        combos_with=["labeling", "strategic_silence"],
        appraisal_shifts={"valence": 0.10, "certainty": 0.05},
        sources=["read-the-room"],
    ),
    "calibrated_questions": Technique(
        id="calibrated_questions",
        name="Calibrated Questions",
        category="extraction",
        description="Open-ended questions starting with 'how' or 'what' that guide without commanding.",
        mechanism="Gives the target agency (they're choosing to share) while steering the conversation. "
                  "The dlPFC engages in problem-solving mode, not defense mode.",
        neural_basis="dlPFC problem-solving activation, bypasses amygdala defense",
        effectiveness="S",
        risk_level=0.1,
        detection_markers=["kept asking 'how' and 'what' questions", "felt like I was driving but wasn't"],
        combos_with=["labeling", "strategic_silence", "scharff_technique"],
        appraisal_shifts={"agency": 0.20, "coping_potential": 0.10},
        sources=["read-the-room", "Persuade-Me"],
    ),
    "door_in_the_face": Technique(
        id="door_in_the_face",
        name="Door-in-the-Face",
        category="compliance",
        description="Make a large request first, then retreat to your actual (smaller) request.",
        mechanism="Reciprocity + contrast effect. The concession feels like a gift. "
                  "NAc assigns higher value to the smaller request via contrast.",
        neural_basis="Reciprocity circuit (vmPFC) + contrast encoding (NAc)",
        effectiveness="A",
        risk_level=0.3,
        detection_markers=["first ask was way too big", "the 'real' ask felt reasonable by comparison"],
        counter_strategy="Evaluate the second request independently, not relative to the first.",
        combos_with=["foot_in_the_door", "scarcity_takeaway"],
        appraisal_shifts={"coping_potential": 0.15, "valence": 0.10},
        sources=["read-the-room"],
    ),
    "foot_in_the_door": Technique(
        id="foot_in_the_door",
        name="Foot-in-the-Door",
        category="compliance",
        description="Start with a tiny commitment, then escalate. Each yes makes the next yes easier.",
        mechanism="Commitment-consistency bias. The hippocampus retrieves the prior agreement "
                  "and the vmPFC biases toward consistency with past behavior.",
        neural_basis="Hippocampus (prior commitment retrieval) → vmPFC (consistency bias)",
        effectiveness="A",
        risk_level=0.15,
        detection_markers=["started small", "each ask was slightly bigger"],
        combos_with=["door_in_the_face", "identity_locking"],
        appraisal_shifts={"coping_potential": 0.20, "certainty": 0.10},
        sources=["read-the-room", "Persuade-Me"],
    ),
    "strategic_silence": Technique(
        id="strategic_silence",
        name="Strategic Silence",
        category="extraction",
        description="Deliberate pause after someone finishes speaking. The discomfort makes them elaborate.",
        mechanism="The ACC detects social silence as an incomplete exchange. "
                  "The pressure to fill silence is a dlPFC override — they rationalize sharing more.",
        neural_basis="ACC conflict detection → dlPFC override → voluntary disclosure",
        effectiveness="A",
        risk_level=0.2,
        detection_markers=["they just waited", "I kept talking to fill the gap"],
        combos_with=["labeling", "calibrated_questions"],
        appraisal_shifts={"agency": -0.05, "certainty": -0.10},
        sources=["read-the-room", "Persuade-Me"],
    ),
    "presupposition": Technique(
        id="presupposition",
        name="Presupposition",
        category="framing",
        description="Embed an assumption inside a question or statement so it bypasses scrutiny.",
        mechanism="The dlPFC processes the explicit question while the presupposition "
                  "slips past to the hippocampus as accepted context.",
        neural_basis="Dual-process: explicit claim → dlPFC analysis; embedded assumption → hippocampal encoding",
        effectiveness="S",
        risk_level=0.25,
        detection_markers=["the question assumed something that wasn't established"],
        counter_strategy="Identify what the question assumes before answering it.",
        combos_with=["pacing_leading", "embedded_commands"],
        appraisal_shifts={"certainty": 0.15, "agency": -0.10},
        sources=["read-the-room", "Persuade-Me"],
    ),
    "pacing_leading": Technique(
        id="pacing_leading",
        name="Pacing & Leading",
        category="rapport",
        description="Match their current state (pace), then gradually shift to your desired state (lead).",
        mechanism="Pacing builds rapport through synchronization (mirror neuron activation). "
                  "Once rapport is established, the target follows the lead unconsciously.",
        neural_basis="Mirror neurons (pacing) → oxytocin bond → vmPFC trust → following behavior",
        effectiveness="S",
        risk_level=0.15,
        detection_markers=["they matched my energy first", "then I started matching theirs"],
        combos_with=["mirroring", "labeling", "embedded_commands"],
        appraisal_shifts={"valence": 0.15, "agency": 0.05},
        sources=["Persuade-Me"],
    ),
    "embedded_commands": Technique(
        id="embedded_commands",
        name="Embedded Commands",
        category="framing",
        description="Hide a directive inside a larger sentence. 'I'd love for you to find us a spot.'",
        mechanism="The conscious mind processes the polite wrapper while the command "
                  "registers at a preconscious level, priming motor preparation.",
        neural_basis="Premotor cortex activation from action verbs embedded in non-directive syntax",
        effectiveness="B",
        risk_level=0.3,
        detection_markers=["the sentence had a command hidden in it"],
        combos_with=["presupposition", "pacing_leading"],
        appraisal_shifts={"agency": -0.10, "coping_potential": 0.05},
        sources=["Persuade-Me"],
    ),
    "identity_locking": Technique(
        id="identity_locking",
        name="Identity Locking",
        category="compliance",
        description="Assign someone a positive identity trait, then ask them to act consistently with it.",
        mechanism="Once the hippocampus encodes 'I am [trait]', the vmPFC biases "
                  "all future decisions toward consistency with that identity.",
        neural_basis="DMN self-referential processing → hippocampal identity encoding → vmPFC consistency bias",
        effectiveness="S",
        risk_level=0.2,
        detection_markers=["they gave me a label I didn't ask for", "then asked me to live up to it"],
        counter_strategy="Recognize the flattery-before-ask pattern.",
        combos_with=["foot_in_the_door", "social_proof"],
        appraisal_shifts={"goal_relevance": 0.15, "agency": 0.10},
        sources=["read-the-room"],
    ),
    "scarcity_takeaway": Technique(
        id="scarcity_takeaway",
        name="Scarcity / Takeaway",
        category="compliance",
        description="Offer something then withdraw it. The loss-aversion response increases desire.",
        mechanism="NAc assigns higher value to intermittently available rewards. "
                  "The amygdala's loss-aversion response amplifies perceived value.",
        neural_basis="NAc (variable-ratio valuation) + amygdala (loss-aversion)",
        effectiveness="A",
        risk_level=0.4,
        detection_markers=["they offered then pulled back", "I wanted it more after it was taken away"],
        combos_with=["door_in_the_face", "social_proof"],
        appraisal_shifts={"temporal_proximity": 0.20, "agency": -0.15},
        sources=["read-the-room", "Persuade-Me"],
    ),
    "social_proof": Technique(
        id="social_proof",
        name="Social Proof",
        category="compliance",
        description="Reference what others have done to create normative pressure.",
        mechanism="The TPJ processes others' behavior as a proxy for correct action. "
                  "Social proof is a transplanted somatic marker from the vmPFC.",
        neural_basis="TPJ (perspective-taking) → vmPFC (borrowed somatic marker)",
        effectiveness="A",
        risk_level=0.15,
        detection_markers=["they mentioned what everyone else is doing"],
        combos_with=["scarcity_takeaway", "identity_locking"],
        appraisal_shifts={"certainty": 0.20, "goal_relevance": 0.05},
        sources=["read-the-room", "Persuade-Me", "Persuasion-Max"],
    ),
    "reciprocity": Technique(
        id="reciprocity",
        name="Reciprocity",
        category="compliance",
        description="Give something first. The obligation to reciprocate is neurologically hardwired.",
        mechanism="Receiving a gift activates the vmPFC's debt-tracking circuit. "
                  "The discomfort of owing triggers compliance to restore balance.",
        neural_basis="vmPFC debt-tracking → ACC discomfort → compliance to restore balance",
        effectiveness="A",
        risk_level=0.2,
        detection_markers=["they gave me something unexpected", "felt obligated to return the favor"],
        combos_with=["foot_in_the_door"],
        appraisal_shifts={"valence": 0.15, "agency": -0.10},
        sources=["Persuade-Me", "Persuasion-Max"],
    ),
    "power_reversal": Technique(
        id="power_reversal",
        name="Power Reversal",
        category="framing",
        description="Frame yourself as the vulnerable one in a dynamic where you actually hold power.",
        mechanism="The TPJ reads vulnerability signals. When someone more powerful shows weakness, "
                  "the target's threat assessment drops and approach circuit activates.",
        neural_basis="TPJ vulnerability detection → amygdala downregulation → NAc approach",
        effectiveness="S",
        risk_level=0.35,
        detection_markers=["they acted vulnerable but had all the leverage"],
        combos_with=["vulnerability_display", "labeling"],
        appraisal_shifts={"agency": 0.15, "valence": 0.10},
        sources=["read-the-room"],
    ),
    "vulnerability_display": Technique(
        id="vulnerability_display",
        name="Vulnerability Display",
        category="rapport",
        description="Share something genuinely personal. Triggers reciprocal disclosure.",
        mechanism="Vulnerability activates the oxytocin system. The TPJ processes it as trust signal. "
                  "Reciprocal disclosure follows from the same mechanism as reciprocity.",
        neural_basis="Oxytocin release → TPJ trust assessment → reciprocal vmPFC activation",
        effectiveness="S",
        risk_level=0.5,
        detection_markers=["they shared something personal", "I immediately wanted to share back"],
        combos_with=["power_reversal", "labeling", "strategic_silence"],
        appraisal_shifts={"valence": 0.20, "agency": 0.10, "certainty": 0.05},
        sources=["read-the-room", "charisma-training-game"],
    ),
    "tactical_agreement": Technique(
        id="tactical_agreement",
        name="Tactical Agreement",
        category="rapport",
        description="Agree with their position first, then redirect. Bypasses the amygdala's defense response.",
        mechanism="Agreement deactivates the ACC's conflict monitoring. "
                  "Once the threat assessment drops, the redirect encounters no resistance.",
        neural_basis="ACC deactivation (no conflict) → amygdala stands down → redirect accepted",
        effectiveness="A",
        risk_level=0.1,
        combos_with=["pacing_leading", "labeling"],
        appraisal_shifts={"valence": 0.10, "certainty": 0.10},
        sources=["read-the-room"],
    ),
    "scope_expansion": Technique(
        id="scope_expansion",
        name="Scope Expansion",
        category="framing",
        description="Expand the significance of a single event to encompass a larger pattern or identity.",
        mechanism="The hippocampus links the current moment to a broader narrative. "
                  "The vmPFC evaluates the expanded scope as more important, increasing emotional weight.",
        neural_basis="Hippocampal pattern-linking → vmPFC enhanced valuation",
        effectiveness="A",
        risk_level=0.25,
        combos_with=["vulnerability_display", "identity_locking"],
        appraisal_shifts={"goal_relevance": 0.20, "valence": 0.10},
        sources=["read-the-room"],
    ),
    "urgency_framing": Technique(
        id="urgency_framing",
        name="Urgency / Time Pressure",
        category="compliance",
        description="Create a real or perceived time constraint that suppresses deliberation.",
        mechanism="Temporal proximity overrides the deliberation circuit. "
                  "The ACC doesn't have time to escalate to dlPFC analysis.",
        neural_basis="High temporal_proximity → deliberation suppression → amygdala binary decision",
        effectiveness="A",
        risk_level=0.5,
        detection_markers=["sudden deadline appeared", "felt rushed"],
        combos_with=["scarcity_takeaway"],
        appraisal_shifts={"temporal_proximity": 0.30, "certainty": -0.10, "agency": -0.15},
        sources=["Persuade-Me", "Persuasion-Max"],
    ),
    "scharff_technique": Technique(
        id="scharff_technique",
        name="Scharff Technique",
        category="extraction",
        description="Pretend you already know the information. The target corrects your 'mistakes' and reveals truth.",
        mechanism="The hippocampus detects factual errors and the ACC triggers correction impulse. "
                  "Correcting feels like agency (not disclosure), so the amygdala doesn't flag it as threat.",
        neural_basis="Hippocampus error detection → ACC correction impulse → voluntary disclosure framed as correction",
        effectiveness="S",
        risk_level=0.3,
        detection_markers=["they stated something slightly wrong", "I corrected them with real info"],
        combos_with=["calibrated_questions", "naive_play"],
        appraisal_shifts={"agency": 0.15, "certainty": -0.05},
        sources=["read-the-room"],
    ),
    "naive_play": Technique(
        id="naive_play",
        name="Naive Play (Columbo)",
        category="extraction",
        description="Act less informed than you are. Targets lower their guard and over-explain.",
        mechanism="The TPJ assesses you as non-threatening (low competence = low threat). "
                  "The amygdala stands down. Targets shift into expert/helper mode, which feels rewarding.",
        neural_basis="TPJ low-threat assessment → amygdala deactivation → target's NAc activated by teaching",
        effectiveness="A",
        risk_level=0.2,
        combos_with=["scharff_technique", "flattery"],
        appraisal_shifts={"agency": 0.20, "valence": 0.05},
        sources=["read-the-room"],
    ),
    "flattery": Technique(
        id="flattery",
        name="Flattery / Ego Elevation",
        category="rapport",
        description="Elevate someone's self-image. They become invested in maintaining the elevated version.",
        mechanism="DMN self-referential processing encodes the positive identity. "
                  "The vmPFC then biases toward actions consistent with the flattered self-image.",
        neural_basis="DMN identity encoding → vmPFC consistency bias → approach toward flatterer",
        effectiveness="B",
        risk_level=0.35,
        detection_markers=["excessive praise before an ask", "felt good then realized why"],
        counter_strategy="Note when compliments precede requests.",
        combos_with=["naive_play", "identity_locking"],
        appraisal_shifts={"valence": 0.15, "agency": 0.05},
        sources=["read-the-room", "Persuade-Me"],
    ),

    # ═══ DARK PATTERNS (from charisma-training-game — taught for recognition) ═══

    "love_bombing": Technique(
        id="love_bombing",
        name="Love Bombing",
        category="emotional_escalation",
        description="Overwhelming target with attention and validation to create dependency.",
        mechanism="Dopamine spike from intense positive reinforcement creates expectation. "
                  "Followed by withdrawal, the contrast produces addiction-like seeking behavior.",
        neural_basis="NAc reward surge → oxytocin bonding → withdrawal triggers cortisol crash",
        effectiveness="S",
        risk_level=0.9,
        detection_markers=["unusually rapid escalation", "excessive praise", "constant contact"],
        counter_strategy="Notice pattern change — intensity is unsustainable.",
        combos_with=["withdrawal", "intermittent_reinforcement"],
        sources=["charisma-training-game"],
    ),
    "withdrawal": Technique(
        id="withdrawal",
        name="Withdrawal / One-Word Response",
        category="emotional_manipulation",
        description="Abrupt withdrawal of affection after warmth creates contrast shock and anxiety.",
        mechanism="Sudden decrease in positive stimulation triggers cortisol stress response. "
                  "Contrast effect amplifies perceived loss. Initiates addiction-seeking behavior.",
        neural_basis="Dopamine crash → cortisol surge → amygdala threat → seeking behavior",
        effectiveness="S",
        risk_level=0.9,
        detection_markers=["sudden mood shift", "short responses", "reduced initiation"],
        counter_strategy="Don't pursue. Maintain your own baseline.",
        combos_with=["love_bombing", "intermittent_reinforcement"],
        sources=["charisma-training-game"],
    ),
    "intermittent_reinforcement": Technique(
        id="intermittent_reinforcement",
        name="Intermittent Reinforcement",
        category="behavioral_conditioning",
        description="Unpredictable reward schedule — the most addictive conditioning pattern.",
        mechanism="Variable ratio schedule activates dopamine-seeking at maximum intensity. "
                  "Identical to gambling addiction neurology. 20-40% response rate = maximum hook.",
        neural_basis="NAc variable-ratio dopamine firing → compulsive seeking behavior",
        effectiveness="S",
        risk_level=0.95,
        detection_markers=["obsessive monitoring", "constant checking", "hope despite evidence"],
        counter_strategy="Recognize: you're seeking validation from an unreliable source.",
        combos_with=["love_bombing", "withdrawal"],
        sources=["charisma-training-game"],
    ),
    "gaslighting": Technique(
        id="gaslighting",
        name="Gaslighting",
        category="cognitive_distortion",
        description="Denying target's perception to undermine confidence in their own judgment.",
        mechanism="Creates cognitive dissonance — internal evidence conflicts with external denial. "
                  "Over time, the target's ACC learns to distrust its own conflict signals.",
        neural_basis="ACC conflict → repeated external override → learned self-distrust",
        effectiveness="A",
        risk_level=0.95,
        detection_markers=["feeling crazy", "doubting own memory", "seeking proof of reality"],
        counter_strategy="Document events. Trust your memory. Seek outside confirmation.",
        combos_with=["darvo"],
        sources=["charisma-training-game"],
    ),
    "darvo": Technique(
        id="darvo",
        name="DARVO",
        category="cognitive_distortion",
        description="Deny, Attack, Reverse Victim and Offender. The confronted party becomes the 'real' victim.",
        mechanism="Rapid frame inversion overwhelms the dlPFC's working memory. "
                  "By the time you've processed the reversal, you're defending instead of confronting.",
        neural_basis="dlPFC overload from frame inversion → ACC conflict → defensive posture",
        effectiveness="A",
        risk_level=0.9,
        detection_markers=["they turned it around on me", "I ended up apologizing for their behavior"],
        counter_strategy="Name the pattern: 'That's DARVO.' Naming breaks the frame.",
        combos_with=["gaslighting"],
        sources=["charisma-training-game"],
    ),
}


# ─── Categories ──────────────────────────────────────────────────────────────

CATEGORIES = {
    "rapport": "Building connection and trust",
    "extraction": "Getting information without triggering defenses",
    "compliance": "Getting someone to say yes",
    "framing": "Controlling how information is interpreted",
    "emotional_escalation": "Rapidly intensifying emotional bonds (high risk)",
    "emotional_manipulation": "Exploiting emotional states (recognition training)",
    "behavioral_conditioning": "Shaping behavior through reward patterns (recognition training)",
    "cognitive_distortion": "Distorting perception of reality (recognition training)",
}


class TechniqueLibrary:
    """Searchable master technique library."""

    def __init__(self):
        self.techniques = MASTER_TECHNIQUES

    def get(self, technique_id: str) -> dict:
        t = self.techniques.get(technique_id)
        return t.to_dict() if t else None

    def list(self, category: Optional[str] = None) -> list[dict]:
        results = self.techniques.values()
        if category:
            results = [t for t in results if t.category == category]
        return [{"id": t.id, "name": t.name, "category": t.category,
                 "effectiveness": t.effectiveness, "risk_level": t.risk_level}
                for t in results]

    def by_source(self, source: str) -> list[dict]:
        return [t.to_dict() for t in self.techniques.values() if source in t.sources]

    def combos_for(self, technique_id: str) -> list[dict]:
        t = self.techniques.get(technique_id)
        if not t:
            return []
        return [self.techniques[c].to_dict() for c in t.combos_with if c in self.techniques]

    def categories(self) -> dict:
        return CATEGORIES
