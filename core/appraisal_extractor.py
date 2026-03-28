from __future__ import annotations
"""
Appraisal Extractor — 7 Cognitive Appraisal Dimensions
=======================================================
Scores any text stimulus on the 7 dimensions from Smith & Ellsworth (1985)
and Scherer (2001) that the limbic system evaluates before generating
an emotional response.

Dimensions:
    1. Novelty (0-1) — how unexpected/unprecedented
    2. Valence (0-1) — pleasant vs aversive
    3. Goal Relevance (0-1) — alignment with user's goals
    4. Coping Potential (0-1) — perceived ease/capability
    5. Agency (0-1) — user autonomy vs external control
    6. Certainty (0-1) — confidence in outcome
    7. Temporal Proximity (0-1) — immediacy of benefit

Two extraction modes:
    - prompt: Structured LLM prompt via Ollama or any OpenAI-compatible API
    - heuristic: Fast regex/keyword scoring without LLM (for batch processing)
"""

import json
import re
from dataclasses import dataclass, asdict, field
from typing import Optional


@dataclass
class AppraisalScores:
    """7-dimension appraisal vector for a stimulus."""
    novelty: float = 0.5
    valence: float = 0.5
    goal_relevance: float = 0.5
    coping_potential: float = 0.5
    agency: float = 0.5
    certainty: float = 0.5
    temporal_proximity: float = 0.5

    def to_dict(self) -> dict:
        return asdict(self)

    def to_vector(self) -> list:
        return [
            self.novelty, self.valence, self.goal_relevance,
            self.coping_potential, self.agency, self.certainty,
            self.temporal_proximity,
        ]

    @property
    def mean(self) -> float:
        return sum(self.to_vector()) / 7

    def weakest_dimension(self) -> tuple:
        d = self.to_dict()
        name = min(d, key=d.get)
        return name, d[name]

    def strongest_dimension(self) -> tuple:
        d = self.to_dict()
        name = max(d, key=d.get)
        return name, d[name]


# ─── Heuristic signals (all patterns use \b word boundaries) ────────────────

_NOVELTY_HIGH = re.compile(
    r'\b(introducing|unveiled?|never[- ]before|first[- ]ever|breakthrough|'
    r'revolutionary|reimagined?|reinvent|disrupt|unprecedented|surprise|'
    r'exclusive|secret|hidden|shocking|unexpected)\b', re.I
)
_NOVELTY_LOW = re.compile(
    r'\b(standard|traditional|classic|conventional|usual|typical|'
    r'familiar|normal|regular|default|basic|simple)\b', re.I
)

_VALENCE_POS = re.compile(
    r'\b(free|love|beautiful|celebrate|reward|bonus|gift|win|'
    r'congrats|welcome|thank|enjoy|delight|happy|success|perfect|'
    r'amazing|incredible|wonderful|brilliant|excellent)\b', re.I
)
_VALENCE_NEG = re.compile(
    r'\b(error|fail(?:ed|ure)?|invalid|wrong|denied|rejected|expired|'
    r'warning|danger|risk|threat|problem|issue|broken|lost|miss(?:ed)?|'
    r'unfortunately|sorry|mistake|hate|terrible|awful)\b', re.I
)

_GOAL_RELEVANCE_HIGH = re.compile(
    r'\b(you|your|my|personali[sz]ed|for you|tailored|custom|'
    r'based on your|recommended for|matches? your|fits? your|'
    r'goals?|needs?|what you (?:want|need|care)|matters? to you)\b', re.I
)
_GOAL_RELEVANCE_LOW = re.compile(
    r'\b(we (?:built|made|created)|our (?:team|company|platform)|'
    r'features? include|announcing|introducing our|learn more about us)\b', re.I
)

_COPING_HIGH = re.compile(
    r'\b(easy|simple|one[- ]click|instant|automatic|no[- ]setup|'
    r'takes? \d+\s*(?:seconds?|minutes?|min)|step[- ]by[- ]step|guided|'
    r'pre[- ]?filled|template|ready[- ]made|done|quick)\b', re.I
)
_COPING_LOW = re.compile(
    r'\b(complex|difficult|advanced|requires?|mandatory|must|'
    r'multi[- ]step|extensive|comprehensive|complete all|fill out|'
    r'submit .{0,20} documents?|upload .{0,20} files?)\b', re.I
)

_AGENCY_HIGH = re.compile(
    r'\b(choose|option|prefer|skip|later|no thanks|decline|'
    r'your choice|you decide|opt[- ]?(?:in|out)|customize|control|'
    r'manage|cancel anytime|no commitment)\b', re.I
)
_AGENCY_LOW = re.compile(
    r'\b(required|mandatory|must|forced?|cannot skip|'
    r'no option|only way|you (?:have|need) to|non[- ]?negotiable|'
    r'are you sure|don.t miss|last chance)\b', re.I
)

_CERTAINTY_HIGH = re.compile(
    r'\b(guaranteed?|money[- ]back|refund|proven|verified|'
    r'trusted by \d|rated \d|\d+\s*stars?|100%|risk[- ]free|'
    r'no[- ]risk|case stud|testimonial|specific|exactly)\b', re.I
)
_CERTAINTY_LOW = re.compile(
    r'\b(maybe|might|could|possibly|results may vary|'
    r'no guarantee|subject to|terms apply|conditions|'
    r'estimated|approximately|uncertain)\b', re.I
)

_TEMPORAL_HIGH = re.compile(
    r'\b(now|today|instant|immediate|right away|starts? (?:now|today)|'
    r'already|live|real[- ]time|currently|this (?:second|moment)|'
    r'just (?:happened|finished|completed))\b', re.I
)
_TEMPORAL_LOW = re.compile(
    r'\b(eventually|over time|long[- ]term|in the (?:future|coming)|'
    r'weeks?|months?|years?|someday|gradually|soon|later|upcoming)\b', re.I
)


# ─── Negation-aware scoring ─────────────────────────────────────────────────

_NEGATION_WINDOW = re.compile(
    r'\b(no|not|don.?t|won.?t|can.?t|never|without|neither|nor|lack|'
    r'fail(?:ed|ure)?|miss(?:ing|ed)?|zero|none)\s+\w*\s*', re.I
)


def _count_negated(text, pattern):
    """Count how many matches from pattern are preceded by a negation word."""
    negated = 0
    for m in pattern.finditer(text):
        start = max(0, m.start() - 30)
        prefix = text[start:m.start()]
        if _NEGATION_WINDOW.search(prefix):
            negated += 1
    return negated


def _score_regex_dimension(text, high, low):
    """Score a dimension 0-1 based on keyword matches with negation awareness."""
    h = len(high.findall(text))
    l = len(low.findall(text))
    h_negated = _count_negated(text, high)
    l_negated = _count_negated(text, low)
    h_effective = (h - h_negated) + l_negated
    l_effective = (l - l_negated) + h_negated
    total = abs(h_effective) + abs(l_effective)
    if total == 0:
        return 0.5
    raw = max(0, h_effective) / total
    return round(min(1.0, max(0.0, raw)), 3)


# ─── Extraction prompt ──────────────────────────────────────────────────────

APPRAISAL_PROMPT = """You are a cognitive appraisal scoring system based on Smith & Ellsworth (1985) and Scherer (2001).

Score the following stimulus text on 7 dimensions. Each score is 0.0 to 1.0.

DIMENSIONS:
1. novelty — 0.0 = completely familiar/expected, 1.0 = completely unprecedented/surprising
   Sweet spot 0.3-0.6. Above 0.7 becomes threatening.
2. valence — 0.0 = strongly aversive, 1.0 = strongly rewarding/pleasant
3. goal_relevance — 0.0 = irrelevant to user's goals, 1.0 = directly addresses primary need
4. coping_potential — 0.0 = completely overwhelmed, 1.0 = effortlessly capable
   Sweet spot 0.6-0.8.
5. agency — 0.0 = completely controlled by external force, 1.0 = completely autonomous
   Below 0.3 triggers disgust/retaliation.
6. certainty — 0.0 = complete uncertainty about outcome, 1.0 = complete confidence
7. temporal_proximity — 0.0 = benefit is distant/abstract, 1.0 = benefit is immediate/concrete

Return ONLY a JSON object with these 7 keys and float values. No explanation.

STIMULUS:
{text}"""


class AppraisalExtractor:
    """Extract cognitive appraisal dimensions from text stimuli."""

    def __init__(self, ollama_model="llama3.2", ollama_url="http://localhost:11434"):
        self.model = ollama_model
        self.url = ollama_url

    def extract_heuristic(self, text):
        """Fast regex-based extraction. No LLM required."""
        return AppraisalScores(
            novelty=_score_regex_dimension(text, _NOVELTY_HIGH, _NOVELTY_LOW),
            valence=_score_regex_dimension(text, _VALENCE_POS, _VALENCE_NEG),
            goal_relevance=_score_regex_dimension(text, _GOAL_RELEVANCE_HIGH, _GOAL_RELEVANCE_LOW),
            coping_potential=_score_regex_dimension(text, _COPING_HIGH, _COPING_LOW),
            agency=_score_regex_dimension(text, _AGENCY_HIGH, _AGENCY_LOW),
            certainty=_score_regex_dimension(text, _CERTAINTY_HIGH, _CERTAINTY_LOW),
            temporal_proximity=_score_regex_dimension(text, _TEMPORAL_HIGH, _TEMPORAL_LOW),
        )

    def extract_prompt(self, text):
        """LLM-based extraction via Ollama. More accurate, slower."""
        import urllib.request

        payload = json.dumps({
            "model": self.model,
            "prompt": APPRAISAL_PROMPT.format(text=text[:3000]),
            "stream": False,
            "format": "json",
        }).encode()

        req = urllib.request.Request(
            "%s/api/generate" % self.url,
            data=payload,
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())

        raw = result.get("response", "{}")
        scores = json.loads(raw)

        dimension_keys = [
            "novelty", "valence", "goal_relevance", "coping_potential",
            "agency", "certainty", "temporal_proximity",
        ]
        cleaned = {}
        for k in dimension_keys:
            v = scores.get(k, 0.5)
            cleaned[k] = round(min(1.0, max(0.0, float(v))), 3)

        return AppraisalScores(**cleaned)

    def extract(self, text, mode="heuristic"):
        """Extract appraisal scores. mode='heuristic' or 'prompt'."""
        if mode == "prompt":
            return self.extract_prompt(text)
        return self.extract_heuristic(text)
