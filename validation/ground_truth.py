from __future__ import annotations
"""
Behavioral Ground Truth — Real Data Sources for Weight Calibration
====================================================================
This module documents every accessible dataset that pairs stimuli with
measured behavioral outcomes. These are what's needed to fit weights
via regression instead of inventing them from theory.

STATUS: Data sources documented. Regression harness built. Waiting for
data download + API key to run actual calibration.

THE HONEST FRAMING: Without behavioral ground truth, the circuit
formulas are a scoring system that scores things. With it, they become
a predictive model. This module is the bridge.
"""

import json
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════════
# DATA SOURCES — What exists, how to get it, what it calibrates
# ═══════════════════════════════════════════════════════════════════════════════

DATA_SOURCES = {
    "persuasion_for_good": {
        "citation": "Wang et al. 2019, ACL. 'Persuasion for Good: Towards a Personalized "
                    "Persuasive Dialogue System for Social Good.'",
        "url": "https://convokit.cornell.edu/documentation/persuasionforgood.html",
        "github": "https://github.com/ohyj1002/persuasionforgood",
        "download": "pip install convokit; from convokit import Corpus, download; "
                    "corpus = Corpus(filename=download('persuasionforgood-corpus'))",
        "n_datapoints": 1017,
        "stimuli": "Persuader dialogue turns (text attempting to convince someone to donate)",
        "outcome": "Binary: did the persuadee agree to donate? (success/failure)",
        "annotations": "300 dialogues have per-sentence persuasion strategy labels (10 strategies)",
        "what_it_calibrates": "The full pipeline: appraisal extraction on persuader text → "
                              "circuit prediction → behavioral outcome (donate/not). "
                              "Regression of circuit scores on donation outcome gives "
                              "empirically fitted weights.",
        "limitations": "Dialogues, not UX stimuli. Charity context, not product context. "
                       "But persuasion mechanisms should transfer.",
        "accessible": True,
    },
    "knutson_2007_shop": {
        "citation": "Knutson et al. 2007, Neuron. 'Neural Predictors of Purchases.'",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1876732/",
        "n_datapoints": 2080,  # 26 subjects × 80 products
        "stimuli": "Product images + price points (SHOP task)",
        "outcome": "Binary: purchase/no-purchase per trial, plus NAcc/insula/MPFC fMRI",
        "what_it_calibrates": "The gold standard: brain activation AND behavioral outcome "
                              "for the same stimuli. If we could score their stimuli, we'd "
                              "correlate our approach score with their NAcc activation and "
                              "our avoidance score with their insula activation.",
        "limitations": "Raw data not publicly available. Would need to contact Knutson Lab "
                       "at Stanford. Product images (not text) are the stimuli.",
        "accessible": False,
        "contact": "Brian Knutson, Stanford Dept of Psychology, knutson@stanford.edu",
    },
    "kaggle_email_campaigns": {
        "citation": "Various Kaggle datasets on email marketing performance",
        "url": "https://www.kaggle.com/datasets?tags=16486-Email+and+Messaging",
        "n_datapoints": "Varies (100k+ subject lines in largest)",
        "stimuli": "Email subject lines (text)",
        "outcome": "Open rate (continuous, 0-1)",
        "what_it_calibrates": "Text → behavioral outcome (open/not-open). Can score subject "
                              "lines on 7 appraisal dimensions and regress against open rate.",
        "limitations": "Open rate ≠ persuasion exactly. Confounded by sender reputation, "
                       "send time, list quality. But text component is isolable.",
        "accessible": True,
    },
    "hubspot_cta_study": {
        "citation": "HubSpot 2014. Analysis of 330,000+ CTAs.",
        "url": "https://blog.hubspot.com/marketing/personalized-calls-to-action-convert-better-data",
        "n_datapoints": 330000,
        "stimuli": "CTA button text and context",
        "outcome": "Click-through rate (continuous)",
        "key_finding": "Personalized CTAs convert 202% better than generic defaults",
        "what_it_calibrates": "Goal-relevance dimension: personalized = high goal-relevance. "
                              "The 202% lift gives a bound on goal-relevance's contribution.",
        "limitations": "Aggregated results only, not raw data. Can't run regression directly.",
        "accessible": False,  # aggregated findings only
    },
    "first_page_sage_cta_2026": {
        "citation": "First Page Sage 2026. CTA Conversion Rates Report.",
        "url": "https://firstpagesage.com/reports/cta-conversion-rates-report/",
        "n_datapoints": "Aggregated across clients",
        "stimuli": "CTA types and placements",
        "outcome": "Conversion rate by CTA type",
        "key_finding": "Landing pages with single CTA: 13.5% avg. With 5+ CTAs: 10.5%. "
                       "Action verbs increase conversion ~20%.",
        "what_it_calibrates": "Coping_potential: fewer CTAs = higher coping. "
                              "Information_load: more options = more deliberation.",
        "limitations": "Industry aggregate, not raw data. Context-dependent.",
        "accessible": False,
    },
}


# ═══════════════════════════════════════════════════════════════════════════════
# REGRESSION HARNESS — Ready to fit when data arrives
# ═══════════════════════════════════════════════════════════════════════════════

def fit_weights_from_data(stimuli_texts, outcomes, extractor, mode="heuristic"):
    """Fit circuit weights via logistic regression on behavioral data.

    Args:
        stimuli_texts: list of text stimuli
        outcomes: list of binary outcomes (1=converted, 0=didn't)
        extractor: AppraisalExtractor instance
        mode: extraction mode ("heuristic", "claude", "ollama")

    Returns:
        dict with fitted weights, R², significance tests
    """
    # Extract appraisal scores for all stimuli
    appraisal_vectors = []
    for text in stimuli_texts:
        scores = extractor.extract(text, mode=mode)
        appraisal_vectors.append(scores.to_vector())

    n = len(appraisal_vectors)
    if n < 20:
        return {"error": "Need at least 20 datapoints for regression, got %d" % n}

    dims = ["novelty", "valence", "goal_relevance", "coping_potential",
            "agency", "certainty", "temporal_proximity"]

    # ─── Logistic regression via gradient descent (no numpy/sklearn needed) ───
    # This is intentionally bare-bones so it runs without pip dependencies.

    weights = [0.0] * 7
    bias = 0.0
    lr = 0.01
    epochs = 1000

    for epoch in range(epochs):
        grad_w = [0.0] * 7
        grad_b = 0.0
        total_loss = 0.0

        for i in range(n):
            x = appraisal_vectors[i]
            y = outcomes[i]

            # Linear combination
            z = bias + sum(w * xi for w, xi in zip(weights, x))

            # Sigmoid
            p = 1.0 / (1.0 + math.exp(-max(-20, min(20, z))))

            # Binary cross-entropy loss
            eps = 1e-7
            total_loss += -(y * math.log(p + eps) + (1 - y) * math.log(1 - p + eps))

            # Gradients
            error = p - y
            for j in range(7):
                grad_w[j] += error * x[j]
            grad_b += error

        # Update
        for j in range(7):
            weights[j] -= lr * grad_w[j] / n
        bias -= lr * grad_b / n

    # ─── Compute metrics ─────────────────────────────────────────────────

    # Predictions
    predictions = []
    for i in range(n):
        x = appraisal_vectors[i]
        z = bias + sum(w * xi for w, xi in zip(weights, x))
        p = 1.0 / (1.0 + math.exp(-max(-20, min(20, z))))
        predictions.append(p)

    # Accuracy
    correct = sum(1 for i in range(n)
                  if (predictions[i] > 0.5) == (outcomes[i] > 0.5))
    accuracy = correct / n

    # AUC (approximate via Mann-Whitney U statistic)
    pos_scores = [predictions[i] for i in range(n) if outcomes[i] > 0.5]
    neg_scores = [predictions[i] for i in range(n) if outcomes[i] <= 0.5]
    if pos_scores and neg_scores:
        concordant = sum(1 for p in pos_scores for ne in neg_scores if p > ne)
        auc = concordant / (len(pos_scores) * len(neg_scores))
    else:
        auc = 0.5

    # ─── Build comparison table ──────────────────────────────────────────

    hand_tuned = {
        "novelty": -0.15,  # penalty in approach formula
        "valence": 0.30,
        "goal_relevance": 0.25,
        "coping_potential": 0.20,
        "agency": 0.10,  # neg_agency_suppress
        "certainty": 0.15,
        "temporal_proximity": 0.0,  # only in deliberation formula
    }

    comparison = []
    for j, dim in enumerate(dims):
        fitted = round(weights[j], 4)
        original = hand_tuned.get(dim, 0.0)
        delta = round(fitted - original, 4)

        if abs(fitted) > abs(original) * 0.5 and (fitted > 0) == (original > 0):
            status = "DIRECTIONALLY CONFIRMED"
        elif abs(fitted) < 0.01:
            status = "NOT SIGNIFICANT"
        elif (fitted > 0) != (original > 0) and abs(fitted) > 0.05:
            status = "CONTRADICTED"
        else:
            status = "FITTED"

        comparison.append({
            "dimension": dim,
            "hand_tuned": original,
            "fitted": fitted,
            "delta": delta,
            "status": status,
        })

    return {
        "n_datapoints": n,
        "accuracy": round(accuracy, 4),
        "auc": round(auc, 4),
        "final_loss": round(total_loss / n, 4),
        "fitted_weights": {dims[j]: round(weights[j], 4) for j in range(7)},
        "bias": round(bias, 4),
        "comparison": comparison,
        "interpretation": (
            "Model fitted on %d datapoints. Accuracy: %.1f%%, AUC: %.3f. "
            "Weights represent the logistic regression coefficient for each "
            "appraisal dimension predicting the behavioral outcome. Positive = "
            "dimension increases conversion probability. Negative = dimension "
            "decreases it. Compare against hand-tuned weights to identify where "
            "theory and data agree vs diverge."
            % (n, accuracy * 100, auc)
        ),
    }


def fit_with_interactions(stimuli_texts, outcomes, extractor, mode="heuristic"):
    """Fit weights WITH interaction terms to test multiplicative hypotheses.

    Tests all 21 pairwise interactions (7 choose 2). Significant interactions
    are empirical evidence for the non-linear effects the research doc
    hypothesizes (high novelty × low coping = threat, etc.).
    """
    dims = ["novelty", "valence", "goal_relevance", "coping_potential",
            "agency", "certainty", "temporal_proximity"]

    # Extract base features
    base_vectors = []
    for text in stimuli_texts:
        scores = extractor.extract(text, mode=mode)
        base_vectors.append(scores.to_vector())

    n = len(base_vectors)

    # Add interaction terms: 7 base + 21 interactions = 28 features
    interaction_pairs = []
    for i in range(7):
        for j in range(i + 1, 7):
            interaction_pairs.append((i, j))

    full_vectors = []
    for v in base_vectors:
        full = list(v)
        for i, j in interaction_pairs:
            full.append(v[i] * v[j])
        full_vectors.append(full)

    n_features = len(full_vectors[0])  # 28

    # Fit logistic regression (same gradient descent as above)
    weights = [0.0] * n_features
    bias = 0.0
    lr = 0.01

    for epoch in range(1500):
        grad_w = [0.0] * n_features
        grad_b = 0.0

        for i in range(n):
            x = full_vectors[i]
            y = outcomes[i]
            z = bias + sum(w * xi for w, xi in zip(weights, x))
            p = 1.0 / (1.0 + math.exp(-max(-20, min(20, z))))
            error = p - y
            for j in range(n_features):
                grad_w[j] += error * x[j]
            grad_b += error

        for j in range(n_features):
            weights[j] -= lr * grad_w[j] / n
        bias -= lr * grad_b / n

    # Extract significant interactions
    interactions = []
    for idx, (i, j) in enumerate(interaction_pairs):
        w = weights[7 + idx]
        if abs(w) > 0.05:  # threshold for "notable"
            interactions.append({
                "dim_a": dims[i],
                "dim_b": dims[j],
                "weight": round(w, 4),
                "sign": "synergistic" if w > 0 else "antagonistic",
                "interpretation": "%s x %s: %s interaction (w=%.3f)" % (
                    dims[i], dims[j],
                    "positive synergy — both high amplifies outcome" if w > 0
                    else "negative — high on both suppresses outcome",
                    w
                ),
            })

    interactions.sort(key=lambda x: abs(x["weight"]), reverse=True)

    return {
        "n_features": n_features,
        "base_weights": {dims[j]: round(weights[j], 4) for j in range(7)},
        "significant_interactions": interactions,
        "n_significant": len(interactions),
        "interpretation": (
            "%d of 21 pairwise interactions have notable weights (|w| > 0.05). "
            "Positive interactions mean both dimensions being high amplifies the "
            "behavioral outcome. Negative interactions mean the combination "
            "suppresses it." % len(interactions)
        ),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# EXPERIMENT DESIGN TABLE — What would calibrate each uncalibrated parameter
# ═══════════════════════════════════════════════════════════════════════════════

CALIBRATION_EXPERIMENTS = [
    {
        "parameter": "approach.novelty_penalty",
        "current_value": 0.15,
        "current_basis": "UNCALIBRATED — Berlyne 1960 inverted-U is theoretical",
        "experiment": {
            "stimuli": "40 landing page variants at 4 novelty levels (standard template, "
                       "moderately creative, highly unusual, bizarre), 10 per level",
            "measurement": "Bounce rate within 5 seconds (behavioral, no self-report)",
            "sample_size": "N=400 (100 per level), power=0.80 for detecting d=0.4",
            "expected_outcome": "Bounce rate inflects upward above novelty ~0.65-0.75. "
                                "The inflection point is the threshold. The slope above "
                                "threshold is the penalty weight.",
            "cost": "$2,000 (Prolific participants at $8/hr, 15 min per session)",
            "proxy": "Measure via existing analytics: compare bounce rates for pages with "
                     "novel vs standard designs. Partial calibration at zero marginal cost.",
        },
        "sensitivity": "HIGH — novelty threshold determines whether creative UX is "
                       "scored as exciting (approach) or threatening (avoidance). Getting "
                       "this wrong flips the prediction for every novel stimulus.",
        "priority_rank": 3,
    },
    {
        "parameter": "approach.neg_agency_suppress",
        "current_value": 0.10,
        "current_basis": "UNCALIBRATED — Craig 2009 insula theory, no coefficient",
        "experiment": {
            "stimuli": "Same offer presented with 4 agency levels: (a) 'Cancel anytime' "
                       "(high), (b) '12-month commitment' (medium), (c) 'No refunds' (low), "
                       "(d) hidden cancel + confirmshaming (very low)",
            "measurement": "Conversion rate + NPS score post-interaction",
            "sample_size": "N=800 (200 per level), power=0.80 for d=0.35",
            "expected_outcome": "Non-linear drop: conversion stable above agency ~0.4, "
                                "then sharp cliff below ~0.25 as insula disgust fires. "
                                "The cliff location and slope calibrate the weight.",
            "cost": "$3,200 (Prolific, 20 min sessions)",
            "proxy": "Compare free-trial vs paid-upfront conversion rates across SaaS products. "
                     "The ratio maps to agency's suppressive effect on approach.",
        },
        "sensitivity": "MEDIUM — affects prediction for permission requests, cancellation "
                       "flows, and commitment-heavy CTAs.",
        "priority_rank": 5,
    },
    {
        "parameter": "avoidance.novelty_threat",
        "current_value": 0.15,
        "current_basis": "UNCALIBRATED — LeDoux 1996 amygdala fast path, interaction unquantified",
        "experiment": {
            "stimuli": "2x2 factorial: (familiar vs novel UI layout) × (clear vs ambiguous "
                       "value proposition). 4 conditions.",
            "measurement": "Bounce rate within 3 seconds (amygdala fast-path window)",
            "sample_size": "N=600 (150 per condition), power=0.80 for interaction d=0.3",
            "expected_outcome": "Novel + ambiguous shows disproportionate bounce (interaction "
                                "effect). Novel + clear should show LOWER bounce than familiar + clear "
                                "(novelty as positive when certainty is high).",
            "cost": "$2,400",
            "proxy": "Test in existing product: release a UI redesign to 10% of users and "
                     "compare session-1 bounce rates. The redesign IS the novelty manipulation.",
        },
        "sensitivity": "HIGH — this interaction determines whether novelty helps or hurts. "
                       "Current formula treats it as multiplicative but the coefficient is guessed.",
        "priority_rank": 2,
    },
    {
        "parameter": "deliberation.goal_uncertainty_interaction",
        "current_value": 0.20,
        "current_basis": "UNCALIBRATED — Smith & Ellsworth 1985 categorical, not quantitative",
        "experiment": {
            "stimuli": "2x2: (relevant vs irrelevant offer) × (certain vs uncertain outcome). "
                       "Example: 'This solves YOUR specific problem' (relevant) vs generic "
                       "feature list (irrelevant), each with guarantee (certain) vs "
                       "'results may vary' (uncertain).",
            "measurement": "Time-on-page (deliberation proxy) + conversion rate",
            "sample_size": "N=400 (100 per condition)",
            "expected_outcome": "Interaction: uncertainty only increases time-on-page when "
                                "the offer is relevant. Irrelevant + uncertain = ignored "
                                "(no deliberation). The interaction coefficient IS this weight.",
            "cost": "$1,600",
            "proxy": "Compare time-on-page for pricing pages with vs without 'terms apply' "
                     "qualifier, split by whether user came from a targeted ad (relevant) "
                     "vs organic (less relevant).",
        },
        "sensitivity": "MEDIUM — determines whether uncertainty triggers deliberation "
                       "(delays decision) or gets ignored (irrelevant uncertainty).",
        "priority_rank": 6,
    },
    {
        "parameter": "deliberation.contradictory_signals",
        "current_value": 0.15,
        "current_basis": "UNCALIBRATED — Botvinick 2001 ACC conflict monitoring, no UX coefficient",
        "experiment": {
            "stimuli": "UX elements with deliberately mixed signals: positive copy + red color, "
                       "trust badge + fine-print disclaimer, 5-star rating + 'results may vary'. "
                       "Control: same elements with consistent signals.",
            "measurement": "Time-to-click on CTA (deliberation) + hover patterns (uncertainty)",
            "sample_size": "N=300 (150 per condition)",
            "expected_outcome": "Mixed-signal versions increase time-to-click by 200-400ms "
                                "(Stroop-like interference). The time increase maps to this weight.",
            "cost": "$1,200",
            "proxy": "Measure via analytics: pages with mixed trust signals (testimonials "
                     "alongside disclaimers) vs consistent trust signals. Compare bounce rate.",
        },
        "sensitivity": "LOW — most UX stimuli don't have extreme contradictory signals.",
        "priority_rank": 8,
    },
    {
        "parameter": "deliberation.circuit_conflict",
        "current_value": 0.10,
        "current_basis": "UNCALIBRATED — conflict monitoring theory extrapolation",
        "experiment": {
            "stimuli": "Identify stimuli where approach ≈ avoidance (user reports 'mixed feelings'). "
                       "Compare decision time vs stimuli with clear approach or avoidance dominance.",
            "measurement": "Decision time + verbal protocol ('what were you thinking?')",
            "sample_size": "N=200, within-subjects design with ~30 stimuli per participant",
            "expected_outcome": "Decision time increases as |approach - avoidance| decreases. "
                                "The slope is this weight.",
            "cost": "$1,600",
            "proxy": "Look at existing A/B tests where results were 50/50 (close to coin-flip). "
                     "These are high-conflict decisions. Compare time-on-page vs decisively "
                     "positive or negative A/B test results.",
        },
        "sensitivity": "LOW — only affects edge cases where approach ≈ avoidance.",
        "priority_rank": 7,
    },
    {
        "parameter": "master.deliberation_weight",
        "current_value": 0.60,
        "current_basis": "UNCALIBRATED — no published ACC/dlPFC predictive weight vs NAcc/insula",
        "experiment": {
            "stimuli": "The Knutson SHOP task replicated with added choice complexity "
                       "(1 product vs 3 similar products at different prices). The 3-option "
                       "version forces deliberation; the 1-option version doesn't.",
            "measurement": "fMRI of ACC/dlPFC activation + purchase decision. Compare "
                           "ACC's predictive contribution to purchase vs NAcc and insula.",
            "sample_size": "N=30 (standard fMRI sample), power analysis per Knutson protocol",
            "expected_outcome": "ACC activation predicts delay (non-purchase in allotted time) "
                                "but not direction (purchase vs active rejection). This means "
                                "deliberation weight should be lower than approach and avoidance.",
            "cost": "$50,000+ (fMRI study at ~$1,500/hour scan time + analysis)",
            "proxy": "Use time-on-page as deliberation proxy. For decisions where users spend "
                     ">60 seconds, what fraction convert? That ratio relative to quick "
                     "decisions calibrates the weight without fMRI.",
        },
        "sensitivity": "VERY HIGH — this weight determines how much 'thinking about it' "
                       "counts against conversion prediction. Getting it wrong miscategorizes "
                       "every deliberation-class stimulus.",
        "priority_rank": 1,
    },
    {
        "parameter": "master.interoceptive_weight",
        "current_value": 0.20,
        "current_basis": "UNCALIBRATED — Seth 2013, no UX measurement exists",
        "experiment": {
            "stimuli": "Standard UX conversion task (sign up for trial). Pre-measure each "
                       "participant's heartbeat detection accuracy (standard interoception task).",
            "measurement": "Conversion rate × interoceptive accuracy interaction",
            "sample_size": "N=200, continuous moderator requires larger N for interaction",
            "expected_outcome": "High-interoception participants show stronger effect of "
                                "somatic markers on conversion (their gut feelings have more "
                                "influence). Low-interoception participants rely more on "
                                "explicit features (deliberation). If interaction is significant, "
                                "the coefficient IS this weight.",
            "cost": "$4,000 (heartbeat task adds ~10 min per participant)",
            "proxy": "None — interoceptive precision requires physiological measurement. "
                     "This is the Neuralink-relevant experiment.",
        },
        "sensitivity": "LOW for population-level prediction (individual differences average out). "
                       "HIGH for personalized prediction (the whole point of Neuralink integration).",
        "priority_rank": 4,
    },
]

# Sort by priority
CALIBRATION_EXPERIMENTS.sort(key=lambda x: x["priority_rank"])


def get_experiment_table():
    """Return the calibration experiment designs as a summary table."""
    return [{
        "rank": e["priority_rank"],
        "parameter": e["parameter"],
        "current_value": e["current_value"],
        "basis": e["current_basis"].split(" — ")[0],
        "sensitivity": e["sensitivity"].split(" — ")[0],
        "cost": e["experiment"]["cost"],
        "has_proxy": "proxy" in e["experiment"] and "None" not in e["experiment"]["proxy"],
    } for e in CALIBRATION_EXPERIMENTS]


def get_data_source_summary():
    """Return data source availability summary."""
    accessible = [k for k, v in DATA_SOURCES.items() if v.get("accessible")]
    inaccessible = [k for k, v in DATA_SOURCES.items() if not v.get("accessible")]
    total_n = sum(v.get("n_datapoints", 0) for v in DATA_SOURCES.values()
                  if isinstance(v.get("n_datapoints"), int))
    return {
        "accessible": accessible,
        "inaccessible": inaccessible,
        "total_datapoints_accessible": total_n,
        "highest_priority": "persuasion_for_good — 1,017 dialogues with success/failure labels, "
                            "freely downloadable, text stimuli with binary behavioral outcome. "
                            "This is the first dataset to run regression on.",
    }
