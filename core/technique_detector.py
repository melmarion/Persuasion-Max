from __future__ import annotations
"""
Technique Detector — 40-Technique Zeng Taxonomy Classification
================================================================
Detects which specific persuasion techniques are present in any text.
Based on the Zeng et al. (ACL 2024) taxonomy split into ethical (20)
and unethical (20) categories.

Three detection modes matching AppraisalExtractor:
    heuristic — keyword/regex patterns, fast, moderate accuracy
    ollama — zero-shot LLM classification with definitions
    claude — Claude API structured output, highest accuracy

The pipeline becomes:
    extract_appraisals → detect_techniques → apply_modifiers → compute_circuits
"""

import re
import json
import os
from dataclasses import dataclass, asdict, field
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════════
# TECHNIQUE DEFINITIONS — Full Zeng Taxonomy
# ═══════════════════════════════════════════════════════════════════════════════

TECHNIQUES = {
    # ─── ETHICAL (20) ────────────────────────────────────────────────────

    "logical_appeal": {
        "category": "reasoning", "ethical": True,
        "definition": "Using logic, data, or structured reasoning to support a claim.",
        "patterns": [r"\b(because|therefore|data shows|evidence|research|study|logically|statistically)\b"],
    },
    "evidence_based": {
        "category": "reasoning", "ethical": True,
        "definition": "Citing specific facts, statistics, or research findings.",
        "patterns": [r"\d+%", r"\b(study|research|found that|according to|data|survey|report)\b"],
    },
    "expert_testimony": {
        "category": "credibility", "ethical": True,
        "definition": "Citing a named expert or credentialed authority.",
        "patterns": [r"\b(dr\.|professor|expert|researcher|scientist|according to [A-Z])\b"],
    },
    "social_proof": {
        "category": "social", "ethical": True,
        "definition": "Referencing what others have done or chosen to create normative pressure.",
        "patterns": [r"\b(everyone|most people|others|popular|trending|thousands|millions|community)\b"],
    },
    "authority_endorsement": {
        "category": "credibility", "ethical": True,
        "definition": "Citing endorsement from a recognized institution or authority figure.",
        "patterns": [r"\b(endorsed|approved|recommended|certified|trusted by|backed by)\b"],
    },
    "bandwagon": {
        "category": "social", "ethical": True,
        "definition": "Suggesting momentum or widespread adoption to encourage joining.",
        "patterns": [r"\b(join|joining|growing|movement|wave|everyone.s doing|don.t be left)\b"],
    },
    "emotional_appeal_positive": {
        "category": "emotion", "ethical": True,
        "definition": "Evoking positive emotions (joy, hope, inspiration) to motivate action.",
        "patterns": [r"\b(imagine|dream|hope|inspire|beautiful|amazing|wonderful|celebrate)\b"],
    },
    "emotional_appeal_negative": {
        "category": "emotion", "ethical": True,
        "definition": "Evoking negative emotions (sadness, concern) to motivate action.",
        "patterns": [r"\b(suffer|struggling|pain|crisis|urgent need|devastating|tragic)\b"],
    },
    "empathy_appeal": {
        "category": "emotion", "ethical": True,
        "definition": "Asking the audience to consider another's perspective or feelings.",
        "patterns": [r"\b(put yourself|imagine (if|how)|how would you feel|walk in|empathize)\b"],
    },
    "storytelling": {
        "category": "narrative", "ethical": True,
        "definition": "Using a personal or third-party narrative to illustrate a point.",
        "patterns": [r"\b(I remember|one day|there was|story|when I was|years ago|let me tell)\b"],
    },
    "self_disclosure": {
        "category": "rapport", "ethical": True,
        "definition": "Sharing personal information or vulnerability to build trust.",
        "patterns": [r"\b(I (admit|confess|honestly|personally)|to be honest|can I be real)\b"],
    },
    "commitment_consistency": {
        "category": "compliance", "ethical": True,
        "definition": "Referencing a prior commitment or stated value to encourage consistent behavior.",
        "patterns": [r"\b(you (said|agreed|promised|committed)|as you mentioned|consistent with)\b"],
    },
    "reciprocity": {
        "category": "compliance", "ethical": True,
        "definition": "Offering value first to create an obligation to reciprocate.",
        "patterns": [r"\b(free|gift|bonus|no (cost|charge)|on us|complimentary|as a thank you)\b"],
    },
    "scarcity_appeal": {
        "category": "urgency", "ethical": True,
        "definition": "Highlighting genuine limited availability.",
        "patterns": [r"\b(limited|only \d+ left|while supplies|exclusive|rare|few remaining)\b"],
    },
    "urgency_appeal": {
        "category": "urgency", "ethical": True,
        "definition": "Creating legitimate time pressure.",
        "patterns": [r"\b(today only|ends (today|tonight|soon)|deadline|act now|time.sensitive)\b"],
    },
    "gain_frame": {
        "category": "framing", "ethical": True,
        "definition": "Framing the message in terms of what the audience gains.",
        "patterns": [r"\b(you.ll (get|gain|earn|receive|save)|benefit|advantage|reward|unlock)\b"],
    },
    "loss_frame": {
        "category": "framing", "ethical": True,
        "definition": "Framing the message in terms of what the audience loses by not acting.",
        "patterns": [r"\b(you.ll (miss|lose|forfeit)|don.t miss|risk losing|without this)\b"],
    },
    "anchoring": {
        "category": "cognitive", "ethical": True,
        "definition": "Establishing a reference point that influences subsequent judgment.",
        "patterns": [r"\b(was \$\d+|originally|compared to|normally|regular price|value of)\b"],
    },
    "rhetorical_question": {
        "category": "linguistic", "ethical": True,
        "definition": "Asking a question to make a point rather than seek information.",
        "patterns": [r"(isn.t it\?|don.t you think\?|wouldn.t you\?|who wouldn.t\?|how can we not\?)"],
    },
    "perspective_shifting": {
        "category": "cognitive", "ethical": True,
        "definition": "Reframing an issue from a different viewpoint to change evaluation.",
        "patterns": [r"\b(think of it (as|this way)|from (another|their|this) (angle|perspective)|consider)\b"],
    },

    # ─── UNETHICAL (20) ──────────────────────────────────────────────────

    "deceptive_information": {
        "category": "deception", "ethical": False,
        "definition": "Presenting false or misleading information as fact.",
        "patterns": [r"\b(proven fact|everyone knows|scientifically proven|studies show)\b"],
    },
    "emotional_manipulation": {
        "category": "manipulation", "ethical": False,
        "definition": "Deliberately exploiting emotional vulnerability for compliance.",
        "patterns": [r"\b(you.d be (heartless|cruel|selfish|terrible)|how could you not|think of the children)\b"],
    },
    "gaslighting": {
        "category": "manipulation", "ethical": False,
        "definition": "Denying the audience's perception of reality to undermine their judgment.",
        "patterns": [r"\b(that never happened|you.re (imagining|overreacting|being dramatic|too sensitive))\b"],
    },
    "false_equivalence": {
        "category": "fallacy", "ethical": False,
        "definition": "Equating two things that are not comparable to falsely strengthen an argument.",
        "patterns": [r"\b(just like|same as|no different (than|from)|equivalent to)\b"],
    },
    "guilt_tripping": {
        "category": "manipulation", "ethical": False,
        "definition": "Making the audience feel guilty to compel action.",
        "patterns": [r"\b(after (all|everything) I|you owe|the least you can|how could you|shame on)\b"],
    },
    "fear_mongering": {
        "category": "manipulation", "ethical": False,
        "definition": "Amplifying or fabricating threats to provoke fear-based compliance.",
        "patterns": [r"\b(catastroph|disaster|destroy|collapse|threat to|end of|you.ll regret)\b"],
    },
    "false_urgency": {
        "category": "manipulation", "ethical": False,
        "definition": "Creating artificial time pressure where none genuinely exists.",
        "patterns": [r"\b(act (fast|immediately)|before it.s too late|this won.t last|hurry)\b"],
    },
    "false_scarcity": {
        "category": "manipulation", "ethical": False,
        "definition": "Claiming limited availability when supply is not actually constrained.",
        "patterns": [r"\b(\d+ people (viewing|watching|looking)|selling fast|almost gone)\b"],
    },
    "ad_hominem": {
        "category": "attack", "ethical": False,
        "definition": "Attacking the person instead of the argument.",
        "patterns": [r"\b(idiot|fool|ignorant|stupid|incompetent|clown|corrupt|liar)\b"],
    },
    "name_calling": {
        "category": "attack", "ethical": False,
        "definition": "Using pejorative labels to discredit or dehumanize.",
        "patterns": [r"\b(extremist|radical|elitist|snowflake|sheep|puppet|shill)\b"],
    },
    "straw_man": {
        "category": "fallacy", "ethical": False,
        "definition": "Misrepresenting an opponent's position to make it easier to attack.",
        "patterns": [r"\b(so you.re saying|what they really want|their true (agenda|goal))\b"],
    },
    "whataboutism": {
        "category": "fallacy", "ethical": False,
        "definition": "Deflecting criticism by pointing to someone else's wrongdoing.",
        "patterns": [r"\b(what about|but they|you (also|too)|look at (what|how) they)\b"],
    },
    "false_dilemma": {
        "category": "fallacy", "ethical": False,
        "definition": "Presenting only two options when more exist.",
        "patterns": [r"\b(either.or|you (either|must choose)|only (two|2) (options|choices)|it.s (this|us) or)\b"],
    },
    "slippery_slope": {
        "category": "fallacy", "ethical": False,
        "definition": "Arguing that one action will inevitably lead to extreme consequences.",
        "patterns": [r"\b(lead to|slippery slope|before you know it|next thing|where does it end|open the door to)\b"],
    },
    "red_herring": {
        "category": "fallacy", "ethical": False,
        "definition": "Introducing an irrelevant topic to divert attention from the main issue.",
        "patterns": [r"\b(but (what about|the real issue)|let.s not forget|more importantly|the real question)\b"],
    },
    "appeal_to_ignorance": {
        "category": "fallacy", "ethical": False,
        "definition": "Arguing that something is true because it hasn't been proven false.",
        "patterns": [r"\b(no (one|evidence) (has |can )?(prove|disprove|shown)|can.t prove it.s not)\b"],
    },
    "manipulative_flattery": {
        "category": "manipulation", "ethical": False,
        "definition": "Using excessive praise specifically to lower critical evaluation before an ask.",
        "patterns": [r"\b(someone as (smart|intelligent|sophisticated) as you|you.re (too smart|above|better than))\b"],
    },
    "appeal_to_pity": {
        "category": "manipulation", "ethical": False,
        "definition": "Using sympathy to override rational evaluation.",
        "patterns": [r"\b(please (I.m|we.re) (begging|desperate)|have (mercy|pity|a heart)|for the sake of)\b"],
    },
    "obfuscation": {
        "category": "deception", "ethical": False,
        "definition": "Using deliberately complex or vague language to hide meaning.",
        "patterns": [r"\b(synergistic|paradigm|leverage|ecosystem|disruptive innovation|holistic)\b"],
    },
    "bandwagon_pressure": {
        "category": "manipulation", "ethical": False,
        "definition": "Coercive social pressure implying exclusion for non-compliance.",
        "patterns": [r"\b(everyone else (is|has)|you.ll be the only|don.t (want to )?be left (out|behind))\b"],
    },
}


@dataclass
class TechniqueResult:
    """Detection results for all 40 techniques."""
    techniques: dict = field(default_factory=dict)
    total_detected: int = 0
    ethical_count: int = 0
    unethical_count: int = 0

    def to_dict(self):
        return {
            "techniques": self.techniques,
            "total_detected": self.total_detected,
            "ethical_count": self.ethical_count,
            "unethical_count": self.unethical_count,
            "detected_names": self.detected_names,
        }

    @property
    def detected_names(self):
        return [k for k, v in self.techniques.items() if v.get("detected")]


# ═══════════════════════════════════════════════════════════════════════════════
# LLM SYSTEM PROMPT — Full definitions for zero-shot classification
# ═══════════════════════════════════════════════════════════════════════════════

_TECHNIQUE_LIST = "\n".join(
    "%d. %s: %s" % (i + 1, name, t["definition"])
    for i, (name, t) in enumerate(TECHNIQUES.items())
)

DETECTION_SYSTEM_PROMPT = """You are a persuasion technique classifier based on the Zeng et al. (ACL 2024) taxonomy.

Given a text stimulus, identify which persuasion techniques are present. Score each as 0.0 (not present) to 1.0 (clearly present).

TECHNIQUES:
%s

Return ONLY a JSON object mapping technique_name -> confidence (0.0-1.0).
Only include techniques with confidence >= 0.3.""" % _TECHNIQUE_LIST


class TechniqueDetector:
    """Detect persuasion techniques in text using the 40-technique Zeng taxonomy."""

    def __init__(
        self,
        anthropic_api_key=None,
        ollama_model="llama3.2",
    ):
        self.api_key = anthropic_api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        self.ollama_model = ollama_model

    def detect(self, text, mode="heuristic"):
        """Detect techniques present in text.

        Args:
            text: stimulus to analyze
            mode: "heuristic", "ollama", or "claude"
        """
        if not text or not text.strip():
            return TechniqueResult()

        if mode == "claude":
            return self._detect_llm(text, use_claude=True)
        elif mode == "ollama":
            return self._detect_llm(text, use_claude=False)
        return self._detect_heuristic(text)

    def _detect_heuristic(self, text):
        """Regex-based detection. Fast, moderate accuracy."""
        results = {}
        ethical_count = 0
        unethical_count = 0

        for name, tech in TECHNIQUES.items():
            detected = False
            confidence = 0.0

            for pattern in tech["patterns"]:
                matches = re.findall(pattern, text, re.I)
                if matches:
                    detected = True
                    confidence = min(1.0, 0.4 + len(matches) * 0.2)
                    break

            results[name] = {
                "detected": detected,
                "confidence": round(confidence, 2),
                "category": tech["category"],
                "ethical": tech["ethical"],
            }

            if detected:
                if tech["ethical"]:
                    ethical_count += 1
                else:
                    unethical_count += 1

        total = ethical_count + unethical_count
        return TechniqueResult(
            techniques=results,
            total_detected=total,
            ethical_count=ethical_count,
            unethical_count=unethical_count,
        )

    def _detect_llm(self, text, use_claude=False):
        """LLM-based detection via Claude API or Ollama."""
        import urllib.request

        user_msg = 'Analyze this text for persuasion techniques:\n\n"%s"' % text[:3000]

        if use_claude and self.api_key:
            try:
                payload = json.dumps({
                    "model": "claude-sonnet-4-20250514",
                    "max_tokens": 800,
                    "system": DETECTION_SYSTEM_PROMPT,
                    "messages": [{"role": "user", "content": user_msg}],
                }).encode()
                req = urllib.request.Request(
                    "https://api.anthropic.com/v1/messages",
                    data=payload,
                    headers={
                        "Content-Type": "application/json",
                        "x-api-key": self.api_key,
                        "anthropic-version": "2023-06-01",
                    },
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    result = json.loads(resp.read())
                raw = "".join(b.get("text", "") for b in result.get("content", []))
            except Exception:
                return self._detect_heuristic(text)
        else:
            try:
                payload = json.dumps({
                    "model": self.ollama_model,
                    "prompt": DETECTION_SYSTEM_PROMPT + "\n\n" + user_msg,
                    "stream": False,
                    "format": "json",
                }).encode()
                req = urllib.request.Request(
                    "http://localhost:11434/api/generate",
                    data=payload,
                    headers={"Content-Type": "application/json"},
                )
                with urllib.request.urlopen(req, timeout=30) as resp:
                    result = json.loads(resp.read())
                raw = result.get("response", "{}")
            except Exception:
                return self._detect_heuristic(text)

        # Parse LLM output
        try:
            raw = re.sub(r'^```(?:json)?\s*', '', raw.strip())
            raw = re.sub(r'\s*```$', '', raw)
            scores = json.loads(raw)
        except json.JSONDecodeError:
            match = re.search(r'\{[^}]+\}', raw, re.DOTALL)
            if match:
                try:
                    scores = json.loads(match.group())
                except json.JSONDecodeError:
                    return self._detect_heuristic(text)
            else:
                return self._detect_heuristic(text)

        # Build result from LLM scores
        results = {}
        ethical_count = 0
        unethical_count = 0

        for name, tech in TECHNIQUES.items():
            confidence = float(scores.get(name, 0.0))
            confidence = min(1.0, max(0.0, confidence))
            detected = confidence >= 0.3

            results[name] = {
                "detected": detected,
                "confidence": round(confidence, 2),
                "category": tech["category"],
                "ethical": tech["ethical"],
            }

            if detected:
                if tech["ethical"]:
                    ethical_count += 1
                else:
                    unethical_count += 1

        return TechniqueResult(
            techniques=results,
            total_detected=ethical_count + unethical_count,
            ethical_count=ethical_count,
            unethical_count=unethical_count,
        )
