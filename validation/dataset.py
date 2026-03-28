from __future__ import annotations
"""
Validation Dataset — 50 Labeled UX Stimuli
============================================
25 high-converting (real products) + 25 low-converting (anti-patterns).
Each labeled with:
    - expected dominant circuit (approach/avoidance/deliberation)
    - expected weakest appraisal dimension
    - conversion class (high/low)
    - source product/pattern

Based on the concrete UX mappings from the limbic decision engineering research.
"""


from dataclasses import dataclass


@dataclass
class LabeledStimulus:
    id: str
    text: str
    source: str
    conversion: str            # "high" or "low"
    expected_circuit: str      # "approach", "avoidance", "deliberation"
    expected_weak_dim: str     # the appraisal dimension most responsible
    notes: str = ""
    context: str = "general"   # UX context for LLM extraction


DATASET = [
    # ═══ HIGH-CONVERTING (25) — Real product copy, circuit = approach ═════

    # Duolingo
    LabeledStimulus("h01", "You earned 50 XP! Keep your streak alive.", "Duolingo",
        "high", "approach", "temporal_proximity",
        "Immediate reward + streak loss-aversion. NAc dopamine from XP celebration."),
    LabeledStimulus("h02", "Notifications help you stay on track. Allow notifications?", "Duolingo",
        "high", "approach", "agency",
        "Delayed until after first reward. Request rides positive somatic marker."),

    # Stripe
    LabeledStimulus("h03", "This doesn't look like a complete card number.", "Stripe",
        "high", "approach", "certainty",
        "Orange not red. Hedge language. Routes to deliberation, not avoidance."),
    LabeledStimulus("h04", "Visa ending in 4242", "Stripe",
        "high", "approach", "novelty",
        "Card icon appearing as you type. Micro-reward per correct digit group."),

    # Notion
    LabeledStimulus("h05", "Get Notion free", "Notion",
        "high", "approach", "goal_relevance",
        "3 circuits firing approach simultaneously. 'Get'=motor, 'free'=zero loss."),
    LabeledStimulus("h06", "Your workspace is ready.", "Notion",
        "high", "approach", "novelty",
        "Instant value delivery. Temporal proximity maximized."),

    # Superhuman
    LabeledStimulus("h07", "$30/month. The fastest email experience ever made.", "Superhuman",
        "high", "approach", "novelty",
        "One tier eliminates ACC conflict. Declarative claim = high certainty."),
    LabeledStimulus("h08", "You're in. Welcome to Superhuman.", "Superhuman",
        "high", "approach", "coping_potential",
        "Identity locking. The user IS a Superhuman user now."),

    # Headspace
    LabeledStimulus("h09", "What brought you here today?", "Headspace",
        "high", "approach", "novelty",
        "Single question activates DMN self-referential processing."),
    LabeledStimulus("h10", "Take a deep breath. You're exactly where you need to be.", "Headspace",
        "high", "approach", "certainty",
        "Parasympathetic activation. Interoceptive comfort signal."),

    # Shopify
    LabeledStimulus("h11", "Complete your order", "Shopify",
        "high", "approach", "novelty",
        "Visible finish line. Constant temporal-proximity signal."),
    LabeledStimulus("h12", "Your items are waiting. Free shipping included.", "Shopify",
        "high", "approach", "coping_potential",
        "Personalized + cost removed. NAc approach + zero loss-aversion."),

    # Strava
    LabeledStimulus("h13", "Your friend Sarah just finished a 5K run!", "Strava",
        "high", "approach", "certainty",
        "Event-triggered. TPJ social processing + oxytocin bonding."),

    # Slack
    LabeledStimulus("h14", "Herding cats... one moment.", "Slack",
        "high", "approach", "valence",
        "Humor suppresses insula uncertainty during loading."),

    # Spotify
    LabeledStimulus("h15", "Cancel anytime. Here's what you'll miss:", "Spotify",
        "high", "approach", "valence",
        "Agency preserved. Legitimate loss-aversion, not hostile retention."),

    # Apple
    LabeledStimulus("h16", "Currently unavailable.", "Apple",
        "high", "approach", "valence",
        "Factual scarcity. No insula manipulation trigger. NAc assigns higher value."),

    # Pinterest
    LabeledStimulus("h17", "People with similar taste love these", "Pinterest",
        "high", "approach", "certainty",
        "TPJ social-referencing. Never allows true zero state."),

    # Basecamp
    LabeledStimulus("h18", "We switched from Slack and saved 3 hours a week. — Jason, CTO at Pixelworks", "Basecamp",
        "high", "approach", "novelty",
        "Specific testimonial placed at decision point. Transplanted somatic marker."),

    # Generic high-converting patterns
    LabeledStimulus("h19", "Free 14-day trial. No credit card required. Cancel anytime.", "Generic SaaS",
        "high", "approach", "novelty",
        "Maximizes coping + agency + certainty simultaneously."),
    LabeledStimulus("h20", "Takes 2 minutes. No setup required.", "Generic SaaS",
        "high", "approach", "novelty",
        "Explicit effort estimate. dlPFC can assess total cost at a glance."),
    LabeledStimulus("h21", "You're 90% there. Just one more step.", "Generic Onboarding",
        "high", "approach", "certainty",
        "Near-completion Zeigarnik tension. NAc approach sustained by progress."),
    LabeledStimulus("h22", "Trusted by 50,000 developers. Here's why:", "Generic Landing",
        "high", "approach", "valence",
        "Specific number + promise of explanation. Curiosity gap + social proof."),
    LabeledStimulus("h23", "Your report is ready to download.", "Generic Dashboard",
        "high", "approach", "novelty",
        "Immediate value delivery. Zero ambiguity about next action."),
    LabeledStimulus("h24", "Welcome back. You left off on Chapter 3.", "Generic Learning",
        "high", "approach", "certainty",
        "Hippocampal continuity. Reduces re-entry friction to zero."),
    LabeledStimulus("h25", "Great choice. Your order ships tomorrow.", "Generic E-commerce",
        "high", "approach", "certainty",
        "Validation + concrete timeline. Positive somatic marker encoding."),

    # ═══ LOW-CONVERTING (25) — Anti-patterns ═════════════════════════════

    # Error states
    LabeledStimulus("l01", "ERROR: Invalid input. Please try again.", "Generic Form",
        "low", "avoidance", "valence",
        "Red + ERROR = amygdala threat. Coping 0.1, agency 0.1."),
    LabeledStimulus("l02", "Error 500: Internal Server Error", "Generic Web",
        "low", "avoidance", "coping_potential",
        "Zero user recourse. Complete helplessness = frustration."),
    LabeledStimulus("l03", "Your session has expired. Please log in again.", "Generic Auth",
        "low", "avoidance", "agency",
        "Lost work. Agency violation. Negative somatic marker."),
    LabeledStimulus("l04", "Payment declined. Contact your bank.", "Generic Checkout",
        "low", "avoidance", "coping_potential",
        "Blame shifted to user. External friction with no internal fix."),

    # Hostile patterns
    LabeledStimulus("l05", "No thanks, I don't want to save money.", "Generic Modal",
        "low", "avoidance", "agency",
        "Confirmshaming. Insula disgust + anger. Highest retaliation tendency."),
    LabeledStimulus("l06", "Are you SURE you want to cancel? You'll lose EVERYTHING.", "Generic Retention",
        "low", "avoidance", "agency",
        "Caps + threat = amygdala activation. Agency near zero."),
    LabeledStimulus("l07", "Only 2 left! 12 people viewing! Timer: 04:59", "Booking.com",
        "low", "avoidance", "agency",
        "Fake scarcity stack. Insula disgust after 2-3 exposures."),
    LabeledStimulus("l08", "Act now or miss out forever! Limited time only!", "Generic Ad",
        "low", "avoidance", "agency",
        "Triple urgency. ACC implausibility detector activates."),

    # Deliberation overload
    LabeledStimulus("l09", "Compare our 3 plans: Basic ($9, 5 features), Pro ($29, 15 features), Enterprise ($99, 30 features). See full comparison.", "Generic Pricing",
        "low", "deliberation", "certainty",
        "ACC overload. dlPFC can't hold comparison matrix. Default = DELAY."),
    LabeledStimulus("l10", "Choose your plan. Terms and conditions may apply. Results may vary. Subject to availability.", "Generic Pricing",
        "low", "deliberation", "certainty",
        "Every qualifier reduces certainty. ACC conflict escalates."),
    LabeledStimulus("l11", "Step 1 of 7: Enter your shipping address.", "Generic Checkout",
        "low", "deliberation", "coping_potential",
        "7 steps = 7 ACC re-evaluation points. Cumulative cognitive tax."),
    LabeledStimulus("l12", "Please fill out the following 12 required fields.", "Generic Form",
        "low", "deliberation", "coping_potential",
        "Information load maxed. dlPFC working memory exceeded."),

    # Dead CTAs
    LabeledStimulus("l13", "Submit", "Generic Form",
        "low", "deliberation", "valence",
        "Zero reward prediction. NAc has nothing to predict."),
    LabeledStimulus("l14", "Click here to learn more", "Generic Landing",
        "low", "deliberation", "goal_relevance",
        "No specificity. vmPFC can't compute relevance."),
    LabeledStimulus("l15", "Sign up for our newsletter", "Generic Landing",
        "low", "deliberation", "valence",
        "No value proposition. NAc predicts zero reward."),
    LabeledStimulus("l16", "Proceed to next step", "Generic Flow",
        "low", "deliberation", "valence",
        "No preview of what's next. Insula uncertainty."),

    # Empty/zero states
    LabeledStimulus("l17", "No results found. Try different keywords.", "Generic Search",
        "low", "avoidance", "valence",
        "Maximum negative prediction error. Expected results, got nothing."),
    LabeledStimulus("l18", "Your cart is empty.", "Generic E-commerce",
        "low", "avoidance", "goal_relevance",
        "Zero state with no recovery path. NAc below baseline."),

    # Overloaded copy
    LabeledStimulus("l19", "Our revolutionary AI-powered platform leverages cutting-edge technology to deliver game-changing results for your business.", "Generic SaaS",
        "low", "deliberation", "certainty",
        "Buzzword stack. ACC implausibility detector. Zero specificity."),
    LabeledStimulus("l20", "We're excited to announce our new product! It has features A, B, C, D, E, F, G, H, I, and J!", "Generic Launch",
        "low", "deliberation", "coping_potential",
        "Feature list exceeds working memory. Company-centric framing."),
    LabeledStimulus("l21", "In today's fast-paced digital landscape, businesses need innovative solutions that drive meaningful engagement.", "Generic Landing",
        "low", "deliberation", "goal_relevance",
        "Zero specificity. Generic enough to apply to anything = irrelevant."),

    # Timing failures
    LabeledStimulus("l22", "Rate us 5 stars! (shown on first app launch)", "Generic App",
        "low", "avoidance", "agency",
        "No somatic marker exists yet. Premature ask = amygdala threat."),
    LabeledStimulus("l23", "Trusted by millions! (shown above the fold before any content)", "Generic Landing",
        "low", "deliberation", "goal_relevance",
        "Social proof before ACC conflict exists. Filed as noise."),
    LabeledStimulus("l24", "Over the coming weeks and months, you'll gradually start to see benefits from our program.", "Generic Onboarding",
        "low", "deliberation", "temporal_proximity",
        "Distant benefit. Deliberation dominates when urgency is zero."),
    LabeledStimulus("l25", "Please wait... loading...", "Generic App",
        "low", "avoidance", "certainty",
        "Information vacuum. Insula uncertainty escalates after ~8s."),
]

# ─── Context inference from stimulus ID and content ──────────────────────────

_CONTEXT_MAP = {
    "h01": "notification", "h02": "permission_request", "h03": "error_state",
    "h04": "checkout", "h05": "cta", "h06": "onboarding", "h07": "pricing",
    "h08": "onboarding", "h09": "onboarding", "h10": "onboarding",
    "h11": "checkout", "h12": "checkout", "h13": "notification", "h14": "loading",
    "h15": "cancellation", "h16": "landing", "h17": "empty_state",
    "h18": "pricing", "h19": "cta", "h20": "cta", "h21": "onboarding",
    "h22": "landing", "h23": "notification", "h24": "onboarding", "h25": "checkout",
    "l01": "error_state", "l02": "error_state", "l03": "error_state",
    "l04": "error_state", "l05": "cta", "l06": "cancellation", "l07": "pricing",
    "l08": "cta", "l09": "pricing", "l10": "pricing", "l11": "checkout",
    "l12": "onboarding", "l13": "cta", "l14": "cta", "l15": "cta", "l16": "cta",
    "l17": "empty_state", "l18": "empty_state", "l19": "landing", "l20": "landing",
    "l21": "landing", "l22": "onboarding", "l23": "landing", "l24": "onboarding",
    "l25": "loading",
}

for _s in DATASET:
    _s.context = _CONTEXT_MAP.get(_s.id, "general")

# Convenience accessors
HIGH_CONVERTING = [s for s in DATASET if s.conversion == "high"]
LOW_CONVERTING = [s for s in DATASET if s.conversion == "low"]
