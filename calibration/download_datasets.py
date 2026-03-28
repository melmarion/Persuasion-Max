#!/usr/bin/env python3
"""
Multi-Corpus Dataset Parser — Extract (text, outcome, domain) from 4 corpora
==============================================================================
Parses already-cloned repos into unified JSONL format:
    {"text": str, "outcome": float, "domain": str, "source": str, "metadata": dict}

Datasets:
    1. DailyPersuasion (persuGPT) — 13,000 persuasion dialogues across 34 domains
    2. HumanChoicePrediction (hcp) — 71K hotel review decisions (binary go/no-go)
    3. Paired Persuasion — controlled persuasive/non-persuasive sentence pairs
    4. PERSUADE 2.0 — argumentative essays with quality scores

Usage:
    python calibration/download_datasets.py
"""

import sys
import os
import json
import csv
import re
import zipfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_DIR = Path(__file__).parent.parent / "calibration" / "parsed"


def parse_daily_persuasion():
    """Parse DailyPersuasion from persuGPT repo.

    13,000 records × 6 sessions each. Extract persuader text as stimulus,
    classify outcome from last persuadee turn (accepted/rejected).
    Split into commercial (~Business/Marketing/Finance) vs opinion-change subsets.
    """
    samples = []
    skipped = 0

    # Try full version zip first, then example
    zip_path = DATA_DIR / "persuGPT" / "DailyPersuasion_full_version.zip"
    example_path = DATA_DIR / "persuGPT" / "DailyPersuasion_example.json"

    if zip_path.exists():
        with zipfile.ZipFile(zip_path) as z:
            with z.open("DailyPersuasion_full_version.json") as f:
                records = json.load(f)
    elif example_path.exists():
        with open(example_path) as f:
            records = json.load(f)
    else:
        print("  WARNING: No DailyPersuasion data found")
        return []

    # Commercial domains
    commercial_domains = {
        "Business", "Marketing", "Finance", "Economics", "Fashion",
        "Technology", "Career",
    }

    # Acceptance indicators in persuadee response
    accept_patterns = re.compile(
        r"\b(alright|okay|fine|agree|yes|sure|convinced|willing|"
        r"let'?s|i'?ll (try|do|give|go|join|accept|consider|think about)|"
        r"deal|sounds (good|great|fair|like a plan)|you'?ve convinced|"
        r"count me in|sign me up|i'?m in|why not)\b",
        re.I,
    )
    reject_patterns = re.compile(
        r"\b(no thanks|i refuse|i won'?t|still not (sure|convinced|interested)|"
        r"i (can'?t|don'?t think|'?m not)|not interested|absolutely not|"
        r"i decline|pass on|rather not)\b",
        re.I,
    )

    for rec in records:
        try:
            # Get domains
            rec_domains = set()
            for de in rec.get("scenario", {}).get("domain", []):
                for dd in de.get("domain", []):
                    rec_domains.add(dd)

            is_commercial = bool(rec_domains & commercial_domains)
            domain_label = "commercial" if is_commercial else "opinion_change"

            # Process each session as a separate sample
            dialog = rec.get("dialog", {})
            for session_key, turns in dialog.items():
                if not isinstance(turns, list) or len(turns) < 2:
                    continue

                # Extract persuader text (concatenated turns)
                persuader_text = " ".join(
                    t.get("response", "") for t in turns
                    if t.get("role") == "persuader" and t.get("response")
                )

                if len(persuader_text) < 20:
                    skipped += 1
                    continue

                # Classify outcome from last persuadee turn
                last_persuadee = None
                for t in reversed(turns):
                    if t.get("role") == "persuadee":
                        last_persuadee = t.get("response", "")
                        break

                if not last_persuadee:
                    skipped += 1
                    continue

                # Score outcome
                has_accept = bool(accept_patterns.search(last_persuadee))
                has_reject = bool(reject_patterns.search(last_persuadee))

                if has_accept and not has_reject:
                    outcome = 1.0
                elif has_reject and not has_accept:
                    outcome = 0.0
                elif has_accept and has_reject:
                    outcome = 0.5  # ambiguous
                else:
                    # Default: check sentiment heuristic
                    outcome = 0.5  # uncertain

                samples.append({
                    "text": persuader_text[:3000],
                    "outcome": outcome,
                    "domain": domain_label,
                    "source": "daily_persuasion",
                    "metadata": {
                        "id": rec.get("id", ""),
                        "session": session_key,
                        "domains": list(rec_domains),
                        "goal": rec.get("scenario", {}).get("goal", ""),
                    },
                })

        except Exception as e:
            skipped += 1

    print("  DailyPersuasion: %d samples extracted, %d skipped" % (len(samples), skipped))
    return samples


def parse_hcp():
    """Parse HumanChoicePrediction — hotel review persuasion decisions.

    Players see a hotel review and decide whether to "go" (book).
    didGo=True means the review persuaded them. Link review text via
    game_reviews/{gameId}.csv using reviewId.
    """
    samples = []
    skipped = 0

    games_x = DATA_DIR / "hcp" / "data" / "games_clean_X.csv"
    review_dir = DATA_DIR / "hcp" / "data" / "game_reviews"

    if not games_x.exists():
        print("  WARNING: HCP games_clean_X.csv not found")
        return []

    # Load all reviews into a lookup: {reviewId: text}
    # Review files are named by hotelId, each row is: reviewId, hotelName, roomType, reviewText, score
    review_lookup = {}
    if review_dir.exists():
        for fn in os.listdir(review_dir):
            if not fn.endswith(".csv"):
                continue
            try:
                with open(review_dir / fn, encoding="utf-8", errors="replace") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) >= 5:
                            review_id = row[0].strip()
                            review_text = row[3].strip() if len(row) > 3 else ""
                            if review_text and len(review_text) > 10:
                                review_lookup[review_id] = review_text
            except Exception:
                pass

    print("    Loaded %d review texts" % len(review_lookup))

    # Parse game decisions
    with open(games_x, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                review_id = row["reviewId"]
                did_go = row["didGo"] == "True"

                # Look up review text by reviewId
                review_text = review_lookup.get(review_id, "")

                if not review_text or len(review_text) < 10:
                    skipped += 1
                    continue

                samples.append({
                    "text": review_text[:3000],
                    "outcome": 1.0 if did_go else 0.0,
                    "domain": "commercial",
                    "source": "hcp",
                    "metadata": {
                        "game_id": row.get("gameId", ""),
                        "review_id": review_id,
                        "hotel_score": float(row.get("hotelScore", 0)),
                        "round_num": int(row.get("roundNum", 0)),
                        "strategy_id": row.get("strategy_id", ""),
                    },
                })

            except Exception:
                skipped += 1

    print("  HCP: %d samples extracted, %d skipped" % (len(samples), skipped))
    return samples


def parse_paired():
    """Parse Paired Persuasion dataset — controlled pairs.

    Data is in GitHub releases. If not downloaded, skip gracefully.
    """
    samples = []
    paired_dir = DATA_DIR / "paired"

    # Check for data files in any format
    data_files = []
    for ext in ["*.csv", "*.tsv", "*.json", "*.txt"]:
        data_files.extend(paired_dir.glob(ext))

    # Also check if release was downloaded
    for ext in ["*.csv", "*.tsv", "*.json", "*.txt"]:
        data_files.extend((paired_dir / "data").glob(ext)) if (paired_dir / "data").exists() else None or []

    if not data_files:
        print("  WARNING: Paired Persuasion — no data files found (data in GitHub releases, not repo)")
        print("           To include: download from https://github.com/marcoguerini/paired_datasets_for_persuasion/releases")
        return []

    # Try to parse whatever format we find
    for fp in data_files:
        try:
            if fp.suffix == ".csv":
                with open(fp) as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        # Expect columns like: persuasive, non_persuasive, topic
                        for key in ["persuasive", "sentence_1", "text_1"]:
                            if key in row and row[key]:
                                samples.append({
                                    "text": row[key][:3000],
                                    "outcome": 1.0,
                                    "domain": "opinion_change",
                                    "source": "paired",
                                    "metadata": {"file": fp.name},
                                })
                        for key in ["non_persuasive", "sentence_2", "text_2"]:
                            if key in row and row[key]:
                                samples.append({
                                    "text": row[key][:3000],
                                    "outcome": 0.0,
                                    "domain": "opinion_change",
                                    "source": "paired",
                                    "metadata": {"file": fp.name},
                                })
        except Exception:
            pass

    print("  Paired: %d samples extracted" % len(samples))
    return samples


def parse_persuade2():
    """Parse PERSUADE 2.0 — argumentative essays with quality scores.

    Actual data is on Google Drive (too large for GitHub).
    Check if user downloaded it manually.
    """
    samples = []
    persuade_dir = DATA_DIR / "persuade2"

    # Look for CSV files that might have been manually downloaded
    data_files = list(persuade_dir.glob("*.csv"))
    data_files.extend(persuade_dir.glob("**/*.csv"))

    if not data_files:
        print("  WARNING: PERSUADE 2.0 — no CSV data found (data hosted on Google Drive)")
        print("           To include: download from links in data/persuade2/README.md")
        return []

    for fp in data_files:
        try:
            with open(fp, encoding="utf-8", errors="replace") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    text = row.get("full_text", row.get("essay", row.get("text", "")))
                    score = row.get("holistic_essay_score", row.get("score", ""))

                    if not text or len(text) < 20:
                        continue

                    try:
                        outcome = float(score) / 6.0  # normalize to 0-1 if on 1-6 scale
                        outcome = min(1.0, max(0.0, outcome))
                    except (ValueError, TypeError):
                        outcome = 0.5

                    samples.append({
                        "text": text[:3000],
                        "outcome": outcome,
                        "domain": "opinion_change",
                        "source": "persuade2",
                        "metadata": {"file": fp.name},
                    })
        except Exception:
            pass

    print("  PERSUADE 2.0: %d samples extracted" % len(samples))
    return samples


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Parsing datasets...")
    print()

    all_samples = []

    # Parse each source
    dp_samples = parse_daily_persuasion()
    all_samples.extend(dp_samples)

    hcp_samples = parse_hcp()
    all_samples.extend(hcp_samples)

    paired_samples = parse_paired()
    all_samples.extend(paired_samples)

    persuade_samples = parse_persuade2()
    all_samples.extend(persuade_samples)

    # Write unified JSONL
    output_path = OUTPUT_DIR / "unified_dataset.jsonl"
    with open(output_path, "w") as f:
        for s in all_samples:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")

    # Print summary
    print()
    print("=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)

    sources = {}
    domains = {}
    for s in all_samples:
        src = s["source"]
        dom = s["domain"]
        sources[src] = sources.get(src, 0) + 1
        domains[dom] = domains.get(dom, 0) + 1

    print("Total samples: %d" % len(all_samples))
    print()
    print("By source:")
    for src, count in sorted(sources.items(), key=lambda x: -x[1]):
        outcomes = [s["outcome"] for s in all_samples if s["source"] == src]
        pos = sum(1 for o in outcomes if o > 0.5)
        print("  %-25s %6d samples  (%.1f%% positive)" % (src, count, pos / len(outcomes) * 100))

    print()
    print("By domain:")
    for dom, count in sorted(domains.items(), key=lambda x: -x[1]):
        print("  %-25s %6d samples" % (dom, count))

    print()
    print("Output: %s" % output_path)
    print("=" * 60)

    return all_samples


if __name__ == "__main__":
    main()
