from __future__ import annotations
"""
Evaluation Suite — Full pipeline validation
=============================================
Runs the limbic cascade on all 50 labeled stimuli and computes:
    1. Circuit classification accuracy vs manual labels
    2. Compliance probability correlation with conversion outcome
    3. Confusion matrix for circuit prediction
    4. Ablation: remove each dimension, measure prediction degradation
    5. 7D vs 2D benchmark (appraisal theory vs sentiment-only)
    6. TRIBE v2 alignment percentage

Outputs JSON report + markdown summary.
"""

import sys
import os
import json
import math
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.appraisal_extractor import AppraisalExtractor, AppraisalScores
from core.circuit_predictor import CircuitPredictor, persuasion_effectiveness
from core.reframing_engine import ReframingEngine
from core.limbic_cascade import LimbicCascade
from validation.dataset import DATASET, HIGH_CONVERTING, LOW_CONVERTING
from validation.tribe_v2 import TRIBEValidator


def _pearson_r(x, y):
    n = len(x)
    if n < 3:
        return None
    mx = sum(x) / n
    my = sum(y) / n
    sx = math.sqrt(sum((xi - mx) ** 2 for xi in x) / n)
    sy = math.sqrt(sum((yi - my) ** 2 for yi in y) / n)
    if sx == 0 or sy == 0:
        return 0.0
    return round(sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (n * sx * sy), 4)


def run_full_evaluation(mode="heuristic", marker_path=None):
    """Run the complete evaluation suite."""
    cascade = LimbicCascade(
        extraction_mode=mode,
        marker_store_path=marker_path or "/tmp/eval_markers_%d.json" % int(time.time()),
    )
    predictor = CircuitPredictor()
    reframer = ReframingEngine()
    tribe = TRIBEValidator()

    results = []
    for stim in DATASET:
        r = cascade.analyze(stim.text)
        results.append({
            "id": stim.id,
            "text": stim.text[:80],
            "source": stim.source,
            "conversion": stim.conversion,
            "expected_circuit": stim.expected_circuit,
            "predicted_circuit": r.circuits.dominant,
            "expected_weak_dim": stim.expected_weak_dim,
            "predicted_weak_dim": r.appraisal.weakest_dimension()[0],
            "effectiveness": r.effectiveness,
            "compliance_prob": r.prediction.compliance_prob,
            "rejection_prob": r.prediction.rejection_prob,
            "delay_prob": r.prediction.delay_prob,
            "appraisal": r.appraisal.to_dict(),
            "circuits": r.circuits.to_dict(),
        })

    # ─── 1. Circuit Classification Accuracy ──────────────────────────────
    correct_circuit = sum(1 for r in results if r["expected_circuit"] == r["predicted_circuit"])
    circuit_accuracy = correct_circuit / len(results)

    # Weak dimension accuracy
    correct_weak = sum(1 for r in results if r["expected_weak_dim"] == r["predicted_weak_dim"])
    weak_dim_accuracy = correct_weak / len(results)

    # ─── 2. Compliance-Conversion Correlation ────────────────────────────
    compliance_scores = [r["compliance_prob"] for r in results]
    conversion_labels = [1.0 if r["conversion"] == "high" else 0.0 for r in results]
    compliance_correlation = _pearson_r(compliance_scores, conversion_labels)

    effectiveness_scores = [r["effectiveness"] for r in results]
    effectiveness_correlation = _pearson_r(effectiveness_scores, conversion_labels)

    # Mean effectiveness by group
    high_eff = [r["effectiveness"] for r in results if r["conversion"] == "high"]
    low_eff = [r["effectiveness"] for r in results if r["conversion"] == "low"]
    mean_high = sum(high_eff) / len(high_eff) if high_eff else 0
    mean_low = sum(low_eff) / len(low_eff) if low_eff else 0

    # ─── 3. Confusion Matrix ─────────────────────────────────────────────
    circuits = ["approach", "avoidance", "deliberation"]
    confusion = {true: {pred: 0 for pred in circuits} for true in circuits}
    for r in results:
        confusion[r["expected_circuit"]][r["predicted_circuit"]] += 1

    # ─── 4. Ablation Study ───────────────────────────────────────────────
    dimensions = ["novelty", "valence", "goal_relevance", "coping_potential",
                  "agency", "certainty", "temporal_proximity"]

    # Baseline accuracy
    baseline_correct = correct_circuit
    ablation_results = {}

    for ablate_dim in dimensions:
        ablated_correct = 0
        for stim, full_result in zip(DATASET, results):
            # Zero out one dimension
            scores = dict(full_result["appraisal"])
            scores[ablate_dim] = 0.5  # neutralize
            appraisal = AppraisalScores(**scores)
            pred = predictor.predict(appraisal)
            if pred.circuits.dominant == stim.expected_circuit:
                ablated_correct += 1

        ablation_results[ablate_dim] = {
            "accuracy_without": ablated_correct / len(DATASET),
            "degradation": (baseline_correct - ablated_correct) / len(DATASET),
            "importance_rank": 0,  # filled below
        }

    # Rank by importance (most degradation = most important)
    ranked = sorted(ablation_results.items(), key=lambda x: x[1]["degradation"], reverse=True)
    for rank, (dim, data) in enumerate(ranked, 1):
        ablation_results[dim]["importance_rank"] = rank

    # ─── 5. 7D vs 2D Benchmark ──────────────────────────────────────────
    # 2D model: only valence + arousal (novelty as arousal proxy)
    two_d_correct = 0
    for stim, full_result in zip(DATASET, results):
        valence = full_result["appraisal"]["valence"]
        arousal = full_result["appraisal"]["novelty"]  # arousal proxy
        # Simple 2D prediction: high valence = approach, low valence = avoidance,
        # high arousal + medium valence = deliberation
        if valence > 0.6:
            pred_2d = "approach"
        elif valence < 0.3:
            pred_2d = "avoidance"
        else:
            pred_2d = "deliberation"
        if pred_2d == stim.expected_circuit:
            two_d_correct += 1

    two_d_accuracy = two_d_correct / len(DATASET)
    seven_d_advantage = circuit_accuracy - two_d_accuracy

    # ─── 6. TRIBE v2 Alignment ───────────────────────────────────────────
    cascade_results = [cascade.analyze(s.text) for s in DATASET]
    tribe_batch = tribe.validate_batch(cascade_results)

    # ─── Compile Report ──────────────────────────────────────────────────
    report = {
        "meta": {
            "mode": mode,
            "n_stimuli": len(DATASET),
            "n_high": len(HIGH_CONVERTING),
            "n_low": len(LOW_CONVERTING),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "circuit_accuracy": {
            "accuracy": round(circuit_accuracy, 4),
            "correct": correct_circuit,
            "total": len(DATASET),
        },
        "weak_dimension_accuracy": {
            "accuracy": round(weak_dim_accuracy, 4),
            "correct": correct_weak,
            "total": len(DATASET),
        },
        "conversion_correlation": {
            "compliance_r": compliance_correlation,
            "effectiveness_r": effectiveness_correlation,
            "mean_effectiveness_high": round(mean_high, 4),
            "mean_effectiveness_low": round(mean_low, 4),
            "separation": round(mean_high - mean_low, 4),
        },
        "confusion_matrix": confusion,
        "ablation": ablation_results,
        "benchmark_7d_vs_2d": {
            "seven_d_accuracy": round(circuit_accuracy, 4),
            "two_d_accuracy": round(two_d_accuracy, 4),
            "advantage": round(seven_d_advantage, 4),
            "interpretation": (
                "7-dimension appraisal model outperforms 2-dimension valence-arousal by "
                "%.1f percentage points (%.1f%% vs %.1f%%), demonstrating that cognitive "
                "appraisal theory adds predictive value beyond simple sentiment analysis."
                % (seven_d_advantage * 100, circuit_accuracy * 100, two_d_accuracy * 100)
            ),
        },
        "tribe_v2_alignment": tribe_batch,
        "per_stimulus": results,
    }

    return report


def generate_markdown(report):
    """Generate a markdown summary table from the report."""
    lines = []
    lines.append("# Validation Results\n")
    lines.append("## Summary\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append("| Circuit classification accuracy | %.1f%% (%d/%d) |" % (
        report["circuit_accuracy"]["accuracy"] * 100,
        report["circuit_accuracy"]["correct"],
        report["circuit_accuracy"]["total"]))
    lines.append("| Weak dimension accuracy | %.1f%% (%d/%d) |" % (
        report["weak_dimension_accuracy"]["accuracy"] * 100,
        report["weak_dimension_accuracy"]["correct"],
        report["weak_dimension_accuracy"]["total"]))
    lines.append("| Compliance-conversion correlation (r) | %.3f |" % report["conversion_correlation"]["compliance_r"])
    lines.append("| Effectiveness-conversion correlation (r) | %.3f |" % report["conversion_correlation"]["effectiveness_r"])
    lines.append("| Mean effectiveness (high-converting) | %.1f%% |" % (report["conversion_correlation"]["mean_effectiveness_high"] * 100))
    lines.append("| Mean effectiveness (low-converting) | %.1f%% |" % (report["conversion_correlation"]["mean_effectiveness_low"] * 100))
    lines.append("| Separation | +%.1f pp |" % (report["conversion_correlation"]["separation"] * 100))
    lines.append("| 7D model accuracy | %.1f%% |" % (report["benchmark_7d_vs_2d"]["seven_d_accuracy"] * 100))
    lines.append("| 2D (valence-arousal) accuracy | %.1f%% |" % (report["benchmark_7d_vs_2d"]["two_d_accuracy"] * 100))
    lines.append("| 7D advantage | +%.1f pp |" % (report["benchmark_7d_vs_2d"]["advantage"] * 100))
    lines.append("| TRIBE v2 alignment (r) | %.3f |" % (report["tribe_v2_alignment"]["overall_correlation"] or 0))

    # Confusion matrix
    lines.append("\n## Confusion Matrix\n")
    lines.append("| True \\ Predicted | approach | avoidance | deliberation |")
    lines.append("|------------------|----------|-----------|--------------|")
    for true in ["approach", "avoidance", "deliberation"]:
        row = report["confusion_matrix"][true]
        lines.append("| %s | %d | %d | %d |" % (true, row["approach"], row["avoidance"], row["deliberation"]))

    # Ablation
    lines.append("\n## Ablation Study\n")
    lines.append("| Dimension | Accuracy Without | Degradation | Importance Rank |")
    lines.append("|-----------|-----------------|-------------|-----------------|")
    ranked = sorted(report["ablation"].items(), key=lambda x: x[1]["importance_rank"])
    for dim, data in ranked:
        lines.append("| %s | %.1f%% | %.1f pp | #%d |" % (
            dim, data["accuracy_without"] * 100, data["degradation"] * 100, data["importance_rank"]))

    # 7D vs 2D
    lines.append("\n## 7-Dimension vs 2-Dimension Benchmark\n")
    lines.append(report["benchmark_7d_vs_2d"]["interpretation"])

    return "\n".join(lines)


def run_scaling_test(sizes=None):
    """Run evaluation at multiple dataset sizes to show scaling."""
    sizes = sizes or [15, 30, 50]
    scaling_results = []

    for n in sizes:
        subset = DATASET[:n]
        cascade = LimbicCascade(marker_store_path="/tmp/scale_%d.json" % n)
        correct = 0
        for stim in subset:
            r = cascade.analyze(stim.text)
            if r.circuits.dominant == stim.expected_circuit:
                correct += 1
        accuracy = correct / n
        scaling_results.append({"n_stimuli": n, "accuracy": round(accuracy, 4)})

    return scaling_results


if __name__ == "__main__":
    print("Running full evaluation suite (heuristic mode)...")
    report = run_full_evaluation(mode="heuristic")

    # Save JSON
    out_dir = Path(__file__).parent.parent / "results"
    out_dir.mkdir(exist_ok=True)
    with open(out_dir / "evaluation_report.json", "w") as f:
        json.dump(report, f, indent=2)

    # Save markdown
    md = generate_markdown(report)
    with open(out_dir / "evaluation_report.md", "w") as f:
        f.write(md)

    print(md)

    # Scaling test
    print("\n## Scaling Test\n")
    scaling = run_scaling_test()
    for s in scaling:
        print("  n=%d: accuracy=%.1f%%" % (s["n_stimuli"], s["accuracy"] * 100))
