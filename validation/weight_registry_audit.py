#!/usr/bin/env python3
"""
Weight Registry Audit — Every numeric parameter documented
=============================================================
Crawls all modules containing numeric parameters, generates CSV
with provenance and flags unreliable weights.

Usage:
    python validation/weight_registry_audit.py
"""

import sys
import os
import csv
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.circuit_predictor import WEIGHT_REGISTRY
from core.technique_to_circuit import TECHNIQUE_MODIFIERS
from core.domain_registry import DomainWeightRegistry
from core.influence_detector import (
    TECHNIQUE_COUNT_THRESHOLDS, LINGUISTIC_ANOMALY_WEIGHTS,
    SUSPICIOUS_TECHNIQUE_STACKS,
)
from core.stealth_optimizer import SUBREDDIT_NORMS

OUTPUT_DIR = Path(__file__).parent.parent / "results"


def collect_all_weights():
    """Collect every numeric parameter across all modules."""
    weights = []

    # 1. Circuit predictor weights (32)
    for name, entry in WEIGHT_REGISTRY.items():
        weights.append({
            "weight_name": name,
            "module": "circuit_predictor",
            "value": entry["value"],
            "provenance": entry["status"],
            "source_citation": entry["citation"][:100] if entry.get("citation") else "",
            "sample_size": "1017 (PFG)" if entry["status"] == "FITTED" else "",
            "confidence_interval": entry.get("bounds", ""),
            "domain": "universal",
            "layer": "L2_circuit",
            "last_calibration_date": "2026-03-27" if entry["status"] == "FITTED" else "",
        })

    # 2. Technique-to-circuit modifiers (54 techniques × ~4 params each)
    for tech_name, mods in TECHNIQUE_MODIFIERS.items():
        provenance = "UNCALIBRATED"
        citation = ""
        prov_str = mods.get("provenance", "")
        if "CONSTRAINED" in prov_str:
            provenance = "CONSTRAINED"
        elif "FITTED" in prov_str:
            provenance = "FITTED"
        citation = prov_str[:100]

        for dim, val in mods.get("appraisal_shifts", {}).items():
            weights.append({
                "weight_name": "tech.%s.appraisal.%s" % (tech_name, dim),
                "module": "technique_to_circuit",
                "value": val,
                "provenance": provenance,
                "source_citation": citation,
                "sample_size": "",
                "confidence_interval": "",
                "domain": "universal",
                "layer": "L3_technique",
                "last_calibration_date": "",
            })

        for circuit, mult in mods.get("circuit_mods", {}).items():
            weights.append({
                "weight_name": "tech.%s.circuit.%s" % (tech_name, circuit),
                "module": "technique_to_circuit",
                "value": mult,
                "provenance": provenance,
                "source_citation": citation,
                "sample_size": "",
                "confidence_interval": "",
                "domain": "universal",
                "layer": "L3_technique",
                "last_calibration_date": "",
            })

        weights.append({
            "weight_name": "tech.%s.insula_mod" % tech_name,
            "module": "technique_to_circuit",
            "value": mods.get("insula_mod", 0.0),
            "provenance": provenance,
            "source_citation": citation,
            "sample_size": "",
            "confidence_interval": "",
            "domain": "universal",
            "layer": "L3_technique",
            "last_calibration_date": "",
        })

    # 3. Recipient modulator thresholds
    # These are hardcoded thresholds in the modulate() method
    modulator_params = [
        ("mod.neuroticism_threshold", 0.7, "CONSTRAINED", "Eysenck 1967"),
        ("mod.neuroticism_avoidance_mult", 1.4, "CONSTRAINED", "Eysenck 1967"),
        ("mod.neuroticism_fomo_approach_mult", 1.3, "UNCALIBRATED", "Vohs & Faber 2007"),
        ("mod.agreeableness_threshold", 0.7, "CONSTRAINED", "Graziano 1996"),
        ("mod.agreeableness_approach_mult", 1.15, "CONSTRAINED", "Graziano 1996"),
        ("mod.openness_threshold", 0.7, "UNCALIBRATED", "McCrae 1987"),
        ("mod.openness_approach_mult", 1.2, "UNCALIBRATED", "McCrae 1987"),
        ("mod.conscientiousness_threshold", 0.3, "CONSTRAINED", "ELM Petty & Cacioppo 1986"),
        ("mod.conscientiousness_delib_mult", 0.6, "CONSTRAINED", "ELM"),
        ("mod.extraversion_threshold", 0.7, "CONSTRAINED", "Eysenck 1967"),
        ("mod.extraversion_social_mult", 1.4, "CONSTRAINED", "Eysenck 1967"),
        ("mod.care_harm_threshold", 0.7, "UNCALIBRATED", "Haidt 2001"),
        ("mod.care_harm_approach_mult", 1.35, "UNCALIBRATED", "Haidt 2001"),
        ("mod.loyalty_threshold", 0.7, "UNCALIBRATED", "Haidt & Graham 2007"),
        ("mod.loyalty_approach_mult", 1.3, "UNCALIBRATED", "Haidt & Graham 2007"),
        ("mod.authority_threshold", 0.7, "CONSTRAINED", "Milgram 1963"),
        ("mod.authority_approach_mult", 1.15, "CONSTRAINED", "Milgram 1963"),
        ("mod.sanctity_threshold", 0.7, "UNCALIBRATED", "Inbar 2009"),
        ("mod.sanctity_insula_mult", 1.4, "UNCALIBRATED", "Inbar 2009"),
        ("mod.liberty_threshold", 0.7, "UNCALIBRATED", "Brehm 1966"),
        ("mod.liberty_avoidance_mult", 1.5, "UNCALIBRATED", "Brehm 1966"),
        ("mod.high_el_threshold", 0.7, "CONSTRAINED", "ELM Petty & Cacioppo 1986"),
        ("mod.high_el_delib_mult", 1.25, "CONSTRAINED", "ELM"),
        ("mod.low_el_threshold", 0.3, "CONSTRAINED", "ELM"),
        ("mod.low_el_delib_mult", 0.7, "CONSTRAINED", "ELM"),
        ("mod.high_involvement_threshold", 0.7, "UNCALIBRATED", ""),
        ("mod.low_involvement_threshold", 0.3, "UNCALIBRATED", ""),
    ]

    for name, val, prov, cite in modulator_params:
        weights.append({
            "weight_name": name,
            "module": "recipient_modulator",
            "value": val,
            "provenance": prov,
            "source_citation": cite,
            "sample_size": "",
            "confidence_interval": "",
            "domain": "universal",
            "layer": "L4_recipient",
            "last_calibration_date": "",
        })

    # 4. Domain registry weights
    for domain_name in ["ecommerce", "campaign", "crisis_pr"]:
        reg = getattr(DomainWeightRegistry, domain_name)()
        for w in reg.list_all_weights():
            weights.append({
                "weight_name": w.name,
                "module": "domain_registry",
                "value": w.value,
                "provenance": w.provenance,
                "source_citation": w.citation[:100],
                "sample_size": "",
                "confidence_interval": str(w.confidence_interval) if w.confidence_interval != (None, None) else "",
                "domain": domain_name,
                "layer": "L5_domain",
                "last_calibration_date": "",
            })

    # 5. Influence detector thresholds
    for threshold_name, (lo, hi) in TECHNIQUE_COUNT_THRESHOLDS.items():
        weights.append({
            "weight_name": "detector.technique_count.%s.lo" % threshold_name,
            "module": "influence_detector",
            "value": lo,
            "provenance": "UNCALIBRATED",
            "source_citation": "organic content baseline",
            "sample_size": "",
            "confidence_interval": "",
            "domain": "universal",
            "layer": "detector",
            "last_calibration_date": "",
        })

    for feat, weight in LINGUISTIC_ANOMALY_WEIGHTS.items():
        weights.append({
            "weight_name": "detector.linguistic_anomaly.%s" % feat,
            "module": "influence_detector",
            "value": weight,
            "provenance": "UNCALIBRATED",
            "source_citation": "organic content baseline comparison",
            "sample_size": "",
            "confidence_interval": "",
            "domain": "universal",
            "layer": "detector",
            "last_calibration_date": "",
        })

    return weights


def flag_unreliable(weights):
    """Flag weights that might be unreliable."""
    # Compute median absolute value per layer
    layer_values = {}
    for w in weights:
        layer = w["layer"]
        if layer not in layer_values:
            layer_values[layer] = []
        layer_values[layer].append(abs(w["value"]))

    layer_medians = {k: sorted(v)[len(v) // 2] if v else 0.1 for k, v in layer_values.items()}

    for w in weights:
        flags = []

        # Low N
        if w["provenance"] == "FITTED" and w["sample_size"]:
            try:
                n = int(str(w["sample_size"]).split()[0])
                if n < 100:
                    flags.append("LOW_N")
            except (ValueError, IndexError):
                pass

        # CI crosses zero
        ci = w["confidence_interval"]
        if ci and isinstance(ci, str) and "," in ci:
            try:
                parts = ci.strip("()[]").split(",")
                lo, hi = float(parts[0]), float(parts[1])
                if lo < 0 < hi:
                    flags.append("NOT_SIGNIFICANT")
            except (ValueError, IndexError):
                pass

        # Outlier: magnitude >5x median for its layer
        median = layer_medians.get(w["layer"], 0.1)
        if median > 0 and abs(w["value"]) > 5 * median:
            flags.append("OUTLIER")

        w["flags"] = ", ".join(flags) if flags else ""


def generate_summary(weights):
    """Generate summary statistics."""
    total = len(weights)
    by_provenance = {}
    by_layer = {}
    by_module = {}

    for w in weights:
        by_provenance[w["provenance"]] = by_provenance.get(w["provenance"], 0) + 1
        by_layer[w["layer"]] = by_layer.get(w["layer"], 0) + 1
        by_module[w["module"]] = by_module.get(w["module"], 0) + 1

    fitted = by_provenance.get("FITTED", 0)
    calibrated = by_provenance.get("CALIBRATED", 0)
    constrained = by_provenance.get("CONSTRAINED", 0)
    uncalibrated = by_provenance.get("UNCALIBRATED", 0)

    empirical = fitted + calibrated + constrained
    empirical_pct = round(empirical / total * 100, 1) if total else 0

    flagged = sum(1 for w in weights if w.get("flags"))

    return {
        "total_parameters": total,
        "by_provenance": by_provenance,
        "by_layer": by_layer,
        "by_module": by_module,
        "empirically_grounded": empirical,
        "empirically_grounded_pct": empirical_pct,
        "uncalibrated": uncalibrated,
        "uncalibrated_pct": round(uncalibrated / total * 100, 1) if total else 0,
        "flagged_unreliable": flagged,
    }


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    weights = collect_all_weights()
    flag_unreliable(weights)
    summary = generate_summary(weights)

    # Write CSV
    csv_path = OUTPUT_DIR / "weight_registry.csv"
    fields = ["weight_name", "module", "value", "provenance", "source_citation",
              "sample_size", "confidence_interval", "domain", "layer",
              "last_calibration_date", "flags"]
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for w in sorted(weights, key=lambda x: (x["module"], x["weight_name"])):
            writer.writerow(w)

    # Write summary markdown
    md_lines = [
        "# Weight Registry Audit Summary",
        "",
        "**Date:** 2026-03-28",
        "**Total parameters:** %d" % summary["total_parameters"],
        "",
        "## Provenance Breakdown",
        "",
        "| Status | Count | % |",
        "|--------|-------|---|",
    ]
    for status, count in sorted(summary["by_provenance"].items()):
        pct = round(count / summary["total_parameters"] * 100, 1)
        md_lines.append("| %s | %d | %.1f%% |" % (status, count, pct))

    md_lines.extend([
        "",
        "**Empirically grounded (FITTED + CALIBRATED + CONSTRAINED):** %d (%.1f%%)" % (
            summary["empirically_grounded"], summary["empirically_grounded_pct"]),
        "**Uncalibrated (theoretical only):** %d (%.1f%%)" % (
            summary["uncalibrated"], summary["uncalibrated_pct"]),
        "**Flagged as potentially unreliable:** %d" % summary["flagged_unreliable"],
        "",
        "## By Layer",
        "",
        "| Layer | Count |",
        "|-------|-------|",
    ])
    for layer, count in sorted(summary["by_layer"].items()):
        md_lines.append("| %s | %d |" % (layer, count))

    md_lines.extend([
        "",
        "## By Module",
        "",
        "| Module | Count |",
        "|--------|-------|",
    ])
    for module, count in sorted(summary["by_module"].items()):
        md_lines.append("| %s | %d |" % (module, count))

    md_lines.extend([
        "",
        "## Flagged Weights",
        "",
    ])
    flagged = [w for w in weights if w.get("flags")]
    if flagged:
        md_lines.append("| Weight | Module | Value | Flags |")
        md_lines.append("|--------|--------|-------|-------|")
        for w in flagged:
            md_lines.append("| %s | %s | %s | %s |" % (
                w["weight_name"][:40], w["module"], w["value"], w["flags"]))
    else:
        md_lines.append("No weights flagged.")

    md_path = OUTPUT_DIR / "weight_audit_summary.md"
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines))

    # Print summary
    print("=" * 60)
    print("WEIGHT REGISTRY AUDIT")
    print("=" * 60)
    print("Total parameters:     %d" % summary["total_parameters"])
    print()
    print("By provenance:")
    for status, count in sorted(summary["by_provenance"].items()):
        pct = round(count / summary["total_parameters"] * 100, 1)
        print("  %-15s %4d  (%.1f%%)" % (status, count, pct))
    print()
    print("Empirically grounded: %d (%.1f%%)" % (
        summary["empirically_grounded"], summary["empirically_grounded_pct"]))
    print("Uncalibrated:         %d (%.1f%%)" % (
        summary["uncalibrated"], summary["uncalibrated_pct"]))
    print("Flagged unreliable:   %d" % summary["flagged_unreliable"])
    print()
    print("CSV: %s" % csv_path)
    print("Summary: %s" % md_path)

    return summary


if __name__ == "__main__":
    main()
