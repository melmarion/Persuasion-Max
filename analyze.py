#!/usr/bin/env python3
"""
Persuasion-Max CLI — Limbic Decision Cascade Analyzer

Usage:
    python analyze.py "Get Notion free"
    python analyze.py "Your copy here" --mode prompt
    python analyze.py compare "Submit" "Get Notion free"
    python analyze.py patterns --category error
    python analyze.py patterns --weak agency
"""

import sys
import json
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core.limbic_cascade import LimbicCascade
from core.ux_patterns import UXPatternLibrary


def cmd_analyze(args):
    cascade = LimbicCascade(extraction_mode=args.mode)
    result = cascade.analyze(
        args.text,
        context=args.context,
        multimodal_channels=args.channels,
    )
    if args.json:
        print(json.dumps(result.to_dict(), indent=2))
    else:
        print(result.summary())
        if args.verbose:
            print("\n--- Stage Trace ---")
            for s in result.stages:
                print(f"  Stage {s.stage}: {s.name} ({s.structure}) [{s.timing_ms}]")
                for k, v in s.output.items():
                    if k != "note":
                        print(f"    {k}: {v}")
            print("\n--- All Suggestions ---")
            for s in result.suggestions[:5]:
                print(f"  [{s.target_dimension} {s.current_score:.2f}] {s.specific_fix}")


def cmd_compare(args):
    cascade = LimbicCascade(extraction_mode=args.mode)
    comp = cascade.compare(args.text_a, args.text_b)
    if args.json:
        print(json.dumps(comp, indent=2))
    else:
        print(f"A: \"{comp['a']['text']}\"")
        print(f"   Effectiveness: {comp['a']['effectiveness']:.0%} | Behavior: {comp['a']['behavior']}")
        print(f"B: \"{comp['b']['text']}\"")
        print(f"   Effectiveness: {comp['b']['effectiveness']:.0%} | Behavior: {comp['b']['behavior']}")
        print(f"\nWinner: {comp['winner'].upper()} (delta: {comp['delta_effectiveness']:+.0%})")


def cmd_patterns(args):
    lib = UXPatternLibrary()
    if args.weak:
        patterns = lib.for_weak_dimension(args.weak)
        print(f"Success patterns strong on '{args.weak}':\n")
    elif args.category:
        patterns = lib.by_category(args.category)
        print(f"Patterns in '{args.category}':\n")
    elif args.search:
        patterns = lib.search(args.search)
        print(f"Search results for '{args.search}':\n")
    else:
        print(f"Categories: {', '.join(lib.categories())}")
        print(f"Total patterns: {len(lib.patterns)}")
        return

    for p in patterns:
        icon = "+" if p.outcome == "success" else "-"
        print(f"  [{icon}] {p.product}: {p.description}")
        print(f"      Circuit: {p.circuit} | {p.circuit_detail}")
        print(f"      Mechanism: {p.mechanism[:120]}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Limbic Decision Cascade Analyzer")
    sub = parser.add_subparsers(dest="command")
    command_aliases = {"analyze", "a", "compare", "c", "patterns", "p", "-h", "--help"}

    # analyze subcommand (also the default)
    an = sub.add_parser("analyze", aliases=["a"])
    an.add_argument("text")
    an.add_argument("--mode", default="heuristic", choices=["heuristic", "prompt"])
    an.add_argument("--json", action="store_true")
    an.add_argument("--verbose", "-v", action="store_true")
    an.add_argument("--context", default=None)
    an.add_argument("--channels", type=int, default=1)

    # compare subcommand
    cmp = sub.add_parser("compare", aliases=["c"])
    cmp.add_argument("text_a")
    cmp.add_argument("text_b")
    cmp.add_argument("--mode", default="heuristic", choices=["heuristic", "prompt"])
    cmp.add_argument("--json", action="store_true")

    # patterns subcommand
    pat = sub.add_parser("patterns", aliases=["p"])
    pat.add_argument("--category", default=None)
    pat.add_argument("--weak", default=None)
    pat.add_argument("--search", default=None)

    # If no subcommand, treat first arg as text to analyze
    if len(sys.argv) > 1 and sys.argv[1] not in command_aliases:
        sys.argv.insert(1, "analyze")

    args = parser.parse_args()

    if args.command in ("compare", "c"):
        cmd_compare(args)
    elif args.command in ("patterns", "p"):
        cmd_patterns(args)
    elif args.command in ("analyze", "a"):
        cmd_analyze(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
