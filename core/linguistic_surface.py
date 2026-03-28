from __future__ import annotations
"""
Linguistic Surface Features — Zero-cost predictive signal layer
================================================================
12 features extracted via dictionary lookup and regex. No LLM calls.
Based on Ta et al. 2022, LIWC-22 (Boyd et al. 2022), and the
Wilczynski et al. 2024 finding that manipulative content is measurably
MORE emotional, LESS analytical, LONGER, with HIGHER lexical diversity.

These features are orthogonal to the 7 appraisal dimensions — they
measure properties of the TEXT, not the READER'S evaluation. Adding
them should lift AUC independently of the appraisal extractor.
"""

import re
import math
from dataclasses import dataclass, asdict


# ═══════════════════════════════════════════════════════════════════════════════
# DICTIONARIES — Lightweight LIWC-equivalent word lists
# ═══════════════════════════════════════════════════════════════════════════════

_EMOTION_WORDS = set("""
happy sad angry afraid disgusted surprised joy love hate fear anxiety
excited frustrated confused proud ashamed guilty hopeful desperate
thrilled worried furious terrified delighted heartbroken grateful
resentful jealous lonely peaceful miserable ecstatic nervous brave
""".split())

_POSITIVE_WORDS = set("""
happy joy love beautiful wonderful excellent amazing great perfect
brilliant good nice awesome fantastic incredible delightful pleased
grateful thankful satisfied cheerful optimistic hopeful excited
free reward bonus gift win congratulations welcome celebrate
""".split())

_NEGATIVE_WORDS = set("""
sad angry hate fear terrible awful bad wrong ugly horrible
disgusting painful miserable frustrated annoyed disappointed
worried anxious scared fail error broken lost missing denied
rejected expired warning danger risk threat problem issue mistake
""".split())

_CONCRETE_WORDS = set("""
hand eye face door window house car road tree water food money
phone screen button click page form field box table chair floor
wall room bed light sound color red blue green dark bright
""".split())

_ABSTRACT_WORDS = set("""
freedom justice democracy liberty equality innovation paradigm
synergy leverage ecosystem disruption strategy framework concept
philosophy methodology approach perspective transformation vision
""".split())

_HEDGE_WORDS = set("""
maybe perhaps might could possibly somewhat arguably potentially
approximately roughly nearly probably seems appears suggests likely
tends generally typically often usually sometimes occasionally
""".split())

_CERTAINTY_WORDS = set("""
definitely absolutely certainly clearly obviously undoubtedly always
never completely entirely totally surely truly indeed precisely exactly
guaranteed proven confirmed verified without doubt unquestionably
""".split())

_ANALYTICAL_WORDS = set("""
because therefore however although despite consequently furthermore
specifically particularly notably significantly importantly essentially
fundamentally additionally meanwhile conversely alternatively whereas
""".split())


@dataclass
class LinguisticFeatures:
    """12 surface features extracted from text. No LLM inference required."""
    word_count: int = 0
    emotionality: float = 0.0        # % words in emotion categories
    concreteness: float = 0.5        # concrete vs abstract language ratio
    analytical_thinking: float = 0.0  # % analytical/causal connectors
    lexical_diversity: float = 0.0   # type-token ratio
    hedge_density: float = 0.0       # % hedging words
    certainty_markers: float = 0.0   # % certainty words
    self_reference: float = 0.0      # % first-person pronouns
    other_reference: float = 0.0     # % second-person pronouns (you/your)
    reading_difficulty: float = 0.0  # 0=easy, 1=hard (Flesch-Kincaid based)
    tone_positive: float = 0.0      # % positive sentiment words
    tone_negative: float = 0.0      # % negative sentiment words

    def to_dict(self) -> dict:
        return asdict(self)

    def to_vector(self) -> list:
        return [
            self.word_count / 500.0,  # normalize to ~0-1 range
            self.emotionality,
            self.concreteness,
            self.analytical_thinking,
            self.lexical_diversity,
            self.hedge_density,
            self.certainty_markers,
            self.self_reference,
            self.other_reference,
            self.reading_difficulty,
            self.tone_positive,
            self.tone_negative,
        ]


def extract_linguistic_features(text: str) -> LinguisticFeatures:
    """Extract all 12 linguistic surface features from text.

    Pure dictionary + regex. No API calls. Runs in <1ms.
    """
    if not text or not text.strip():
        return LinguisticFeatures()

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    n = len(words) or 1
    word_set = set(words)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    n_sentences = max(len(sentences), 1)

    # Word count
    word_count = len(words)

    # Emotionality: % words in emotion dictionary
    emotion_hits = sum(1 for w in words if w in _EMOTION_WORDS)
    emotionality = emotion_hits / n

    # Concreteness: concrete/(concrete+abstract), 0.5 if neither
    concrete_hits = sum(1 for w in words if w in _CONCRETE_WORDS)
    abstract_hits = sum(1 for w in words if w in _ABSTRACT_WORDS)
    total_ca = concrete_hits + abstract_hits
    concreteness = concrete_hits / total_ca if total_ca > 0 else 0.5

    # Analytical thinking: % analytical/causal connectors
    analytical_hits = sum(1 for w in words if w in _ANALYTICAL_WORDS)
    analytical_thinking = analytical_hits / n

    # Lexical diversity: type-token ratio (unique words / total words)
    lexical_diversity = len(word_set) / n if n > 0 else 0

    # Hedge density: % hedging words
    hedge_hits = sum(1 for w in words if w in _HEDGE_WORDS)
    hedge_density = hedge_hits / n

    # Certainty markers: % certainty words
    certainty_hits = sum(1 for w in words if w in _CERTAINTY_WORDS)
    certainty_markers = certainty_hits / n

    # Self-reference: % first-person pronouns
    self_pronouns = sum(1 for w in words if w in {"i", "me", "my", "mine", "myself", "we", "us", "our"})
    self_reference = self_pronouns / n

    # Other-reference: % second-person pronouns
    other_pronouns = sum(1 for w in words if w in {"you", "your", "yours", "yourself"})
    other_reference = other_pronouns / n

    # Reading difficulty: simplified Flesch-Kincaid
    # FK = 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59
    avg_sentence_len = n / n_sentences
    # Rough syllable count: count vowel groups
    syllable_count = sum(len(re.findall(r'[aeiouy]+', w)) for w in words) or n
    avg_syllables = syllable_count / n
    fk_raw = 0.39 * avg_sentence_len + 11.8 * avg_syllables - 15.59
    # Normalize to 0-1 (FK grade 0-20 maps to 0-1)
    reading_difficulty = min(1.0, max(0.0, fk_raw / 20.0))

    # Tone: positive and negative sentiment word ratios
    pos_hits = sum(1 for w in words if w in _POSITIVE_WORDS)
    neg_hits = sum(1 for w in words if w in _NEGATIVE_WORDS)
    tone_positive = pos_hits / n
    tone_negative = neg_hits / n

    return LinguisticFeatures(
        word_count=word_count,
        emotionality=round(emotionality, 4),
        concreteness=round(concreteness, 4),
        analytical_thinking=round(analytical_thinking, 4),
        lexical_diversity=round(lexical_diversity, 4),
        hedge_density=round(hedge_density, 4),
        certainty_markers=round(certainty_markers, 4),
        self_reference=round(self_reference, 4),
        other_reference=round(other_reference, 4),
        reading_difficulty=round(reading_difficulty, 4),
        tone_positive=round(tone_positive, 4),
        tone_negative=round(tone_negative, 4),
    )
