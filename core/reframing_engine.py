"""
Reframing Engine — Targeted Fix Suggestions
============================================
When persuasion effectiveness is low, identifies the weakest appraisal
dimension and suggests specific, actionable fixes.

Not generic advice ('make it more positive') but targeted interventions
('coping_potential is 0.25 — add explicit effort estimate or pre-fill the form').

Uses the UX pattern library for concrete examples.
"""

from dataclasses import dataclass
from typing import Optional

from core.appraisal_extractor import AppraisalScores
from core.circuit_predictor import CircuitActivations, BehavioralPrediction
from core.ux_patterns import UXPatternLibrary


@dataclass
class ReframingSuggestion:
    target_dimension: str
    current_score: float
    target_score: float
    strategy: str
    specific_fix: str
    reference_pattern: Optional[str] = None  # product example
    expected_circuit_shift: str = ""


# ─── Dimension-specific reframing strategies ────────────────────────────────

REFRAMING_STRATEGIES: dict[str, list[dict]] = {
    "novelty": [
        {
            "when": "too_low",
            "threshold": 0.3,
            "strategy": "Introduce pattern interruption",
            "fixes": [
                "Replace generic copy with unexpected framing (Slack: 'Herding cats...')",
                "Add a counterintuitive data point or stat",
                "Use an unexpected visual metaphor instead of stock imagery",
                "Break a UI convention in one small, delightful way",
            ],
        },
        {
            "when": "too_high",
            "threshold": 0.7,
            "strategy": "Anchor novelty with familiar scaffolding",
            "fixes": [
                "Add a recognizable UI pattern (familiar nav, standard layout)",
                "Reference a known brand or established concept",
                "Use 'like X but for Y' framing to give the hippocampus a prior",
                "Keep novel content within a familiar container (standard card, list, modal)",
            ],
        },
    ],
    "valence": [
        {
            "when": "too_low",
            "threshold": 0.4,
            "strategy": "Replace aversive signals with approach signals",
            "fixes": [
                "Replace red error states with orange/amber + hedge language (Stripe: 'doesn't look like...')",
                "Replace negative framing ('Don't miss out') with positive framing ('Get started today')",
                "Add micro-celebrations for completed actions (chime + spring animation + text)",
                "Replace 'Error:' prefix with actionable guidance ('Try a different...')",
            ],
        },
    ],
    "goal_relevance": [
        {
            "when": "too_low",
            "threshold": 0.4,
            "strategy": "Make the user's goal explicit before presenting value",
            "fixes": [
                "Add a single onboarding question: 'What brought you here?' (Headspace model)",
                "Replace feature lists with outcome statements ('You'll be able to...')",
                "Use second-person language that references the user's specific situation",
                "Remove company-centric copy ('We built...') — replace with user-centric ('You get...')",
            ],
        },
    ],
    "coping_potential": [
        {
            "when": "too_low",
            "threshold": 0.4,
            "strategy": "Reduce perceived effort and show the finish line",
            "fixes": [
                "Add explicit time estimate ('Takes 2 minutes')",
                "Pre-fill form fields with smart defaults",
                "Show progress indicator with visible endpoint",
                "Collapse multi-step into single visible surface (Shopify one-page checkout)",
                "Replace empty text fields with selection/toggle inputs",
            ],
        },
    ],
    "agency": [
        {
            "when": "too_low",
            "threshold": 0.3,
            "strategy": "Restore user control — this is the insula disgust threshold",
            "fixes": [
                "Add visible 'Skip' or 'Not now' option to every interruptive element",
                "Replace confirmshaming with neutral decline copy ('No thanks' not 'No, I hate saving money')",
                "Make cancellation/exit as easy as sign-up (Spotify model)",
                "Show what the user controls: 'You can change this anytime in settings'",
                "Replace forced flows with optional ones — real scarcity, not fake urgency",
            ],
        },
    ],
    "certainty": [
        {
            "when": "too_low",
            "threshold": 0.4,
            "strategy": "Place social proof and specificity at the decision point",
            "fixes": [
                "Move testimonials to directly below the decision (Basecamp model, not above the fold)",
                "Replace vague claims with specific numbers ('47% faster' not 'blazing fast')",
                "Add preview/demo before commitment (show the product working)",
                "Add money-back or free-tier signal at the CTA, not in the FAQ",
                "Use declarative copy (Superhuman: 'The fastest email experience ever made')",
            ],
        },
    ],
    "temporal_proximity": [
        {
            "when": "too_low",
            "threshold": 0.4,
            "strategy": "Make the benefit immediate and concrete",
            "fixes": [
                "Replace 'Over the coming weeks...' with 'Starts today'",
                "Show immediate value before asking for investment (Duolingo: first lesson before signup)",
                "Use event-triggered notifications instead of scheduled ones (Strava model)",
                "Add instant feedback loops — every action produces a visible result",
                "Replace future promises with present demonstrations",
            ],
        },
    ],
}


class ReframingEngine:
    """Analyze appraisal scores and suggest targeted fixes."""

    def __init__(self):
        self.patterns = UXPatternLibrary()

    def diagnose(
        self,
        appraisal: AppraisalScores,
        prediction: BehavioralPrediction,
    ) -> list[ReframingSuggestion]:
        """Identify all weak dimensions and generate fix suggestions."""
        suggestions = []
        scores = appraisal.to_dict()

        for dimension, strategies in REFRAMING_STRATEGIES.items():
            current = scores[dimension]
            for strat in strategies:
                threshold = strat["threshold"]

                if strat["when"] == "too_low" and current < threshold:
                    # Find a reference pattern
                    ref_patterns = self.patterns.for_weak_dimension(dimension)
                    ref = ref_patterns[0].product if ref_patterns else None

                    for fix in strat["fixes"]:
                        suggestions.append(ReframingSuggestion(
                            target_dimension=dimension,
                            current_score=current,
                            target_score=min(1.0, threshold + 0.2),
                            strategy=strat["strategy"],
                            specific_fix=fix,
                            reference_pattern=ref,
                            expected_circuit_shift=self._predict_shift(dimension, prediction),
                        ))

                elif strat["when"] == "too_high" and current > threshold:
                    for fix in strat["fixes"]:
                        suggestions.append(ReframingSuggestion(
                            target_dimension=dimension,
                            current_score=current,
                            target_score=max(0.0, threshold - 0.1),
                            strategy=strat["strategy"],
                            specific_fix=fix,
                            expected_circuit_shift=self._predict_shift(dimension, prediction),
                        ))

        # Sort: most impactful fixes first (biggest gap from threshold)
        suggestions.sort(key=lambda s: abs(s.current_score - s.target_score), reverse=True)
        return suggestions

    def _predict_shift(self, dimension: str, prediction: BehavioralPrediction) -> str:
        """Describe expected circuit shift if this dimension improves."""
        shifts = {
            "novelty": "Reduces amygdala threat response if too high; increases NAc salience if too low",
            "valence": "Shifts dominance from avoidance to approach circuit",
            "goal_relevance": "Increases both approach and deliberation — but approach more",
            "coping_potential": "Directly reduces avoidance (helplessness) and deliberation (effort calculation)",
            "agency": "Below 0.3 triggers insula disgust — fixing this removes the strongest avoidance signal",
            "certainty": "Reduces deliberation circuit activation; suppresses ACC conflict monitoring",
            "temporal_proximity": "Suppresses deliberation (urgency overrides analysis) and boosts approach",
        }
        return shifts.get(dimension, "")

    def top_fix(
        self,
        appraisal: AppraisalScores,
        prediction: BehavioralPrediction,
    ) -> Optional[ReframingSuggestion]:
        """Return the single highest-impact suggestion."""
        suggestions = self.diagnose(appraisal, prediction)
        return suggestions[0] if suggestions else None
