#!/usr/bin/env python3
"""
Zero-loss consolidation verifier.
For each source file, extracts every data-bearing line and checks
whether the data appears in the target prompt file.

Data-bearing = contains any of: numbers, URLs, Python code identifiers,
regex patterns, specific names/citations, table rows with |.

Outputs: lines from source NOT found in target (potential losses).
"""

import re
import sys
import subprocess
import os

REPO_DIR = r"C:\Users\Mario\Downloads\UX & Persuasion\Persuasion Max"
PROMPT_DIR = os.path.join(REPO_DIR, "LINGUISTIC_PERSUASION")

# Source-to-target mapping
MAPPING = {
    # Prompt 1 sources
    "LINGUISTIC_PERSUASION/DETECTION/11_TACTICAL_DETECTION_FRAMEWORK.md": "1_DETECTION_FRAMEWORKS_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/12_PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.md": "1_DETECTION_FRAMEWORKS_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/13_ADVANCED_FRAMEWORKS.md": "1_DETECTION_FRAMEWORKS_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md": "1_DETECTION_FRAMEWORKS_PROMPT.md",
    # Prompt 2 sources
    "LINGUISTIC_PERSUASION/RESEARCH/LINGUISTIC_PERSUASION_RESEARCH.md": "2_LINGUISTIC_RHETORICAL_PATTERNS_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/CLASSICAL_RHETORICAL_TECHNIQUES.md": "2_LINGUISTIC_RHETORICAL_PATTERNS_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/LINGUISTIC_DETECTION_FRAMEWORK.md": "2_LINGUISTIC_RHETORICAL_PATTERNS_PROMPT.md",
    # Prompt 3 sources
    "LINGUISTIC_PERSUASION/RESEARCH/FRACTIONATION_BEHAVIORAL_SCIENCE.md": "3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/FRACTIONATION_DETECTION_METHODS.md": "3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/BEHAVIORAL_ANALYSIS_FRAMEWORK.md": "3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/INTEGRITY_VIOLATION_DETECTION_FRAMEWORK.md": "3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md",
    # Prompt 4 sources
    "LINGUISTIC_PERSUASION/DETECTION/15_PROFESSIONAL_AUDITOR_MANUAL.md": "4_DETECTION_CODE_SCORING_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/17_MACHINE_READABLE_DETECTION_SYSTEM.md": "4_DETECTION_CODE_SCORING_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/24_ENHANCED_DETECTION_RESEARCH.md": "4_DETECTION_CODE_SCORING_PROMPT.md",
    "LINGUISTIC_PERSUASION/DETECTION/26_COMPREHENSIVE_DETECTION_FRAMEWORKS.md": "4_DETECTION_CODE_SCORING_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/27_HIGH_IMPACT_DETECTION_SYSTEMS.md": "4_DETECTION_CODE_SCORING_PROMPT.md",
    # Prompt 5 sources
    "LINGUISTIC_PERSUASION/RESEARCH/28_EXPANDED_RANKED_COMBINATIONS.md": "5_RANKINGS_EFFECTIVENESS_DATA_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/25_EXPANDED_RESEARCH_DIMENSIONS.md": "5_RANKINGS_EFFECTIVENESS_DATA_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/EMPIRICAL_RESEARCH_SYNTHESIS.md": "5_RANKINGS_EFFECTIVENESS_DATA_PROMPT.md",
    # Prompt 6 sources
    "LINGUISTIC_PERSUASION/RESEARCH/EVOLUTION_ANALYSIS.md": "6_CASE_STUDIES_RESEARCH_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/EVOLUTION_PATTERNS_AND_MECHANISMS.md": "6_CASE_STUDIES_RESEARCH_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/19_REAL_WORLD_CASE_STUDIES_DETAILED.md": "6_CASE_STUDIES_RESEARCH_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/APPENDIX_RESEARCH_SOURCES.md": "6_CASE_STUDIES_RESEARCH_PROMPT.md",
    "LINGUISTIC_PERSUASION/RESEARCH/RESEARCH_SUMMARY_AND_NEXT_STEPS.md": "6_CASE_STUDIES_RESEARCH_PROMPT.md",
}

def get_source_content(git_path):
    """Get file content from git HEAD."""
    result = subprocess.run(
        ["git", "show", f"HEAD:{git_path}"],
        capture_output=True, text=True, cwd=REPO_DIR, encoding='utf-8', errors='replace'
    )
    return result.stdout

def is_data_line(line):
    """Check if a line contains substantive data worth verifying."""
    stripped = line.strip()
    if not stripped:
        return False
    # Skip pure markdown formatting
    if stripped in ('---', '```', '```python', '```markdown', '```json'):
        return False
    if stripped.startswith('<!--') or stripped.startswith('-->'):
        return False
    # Skip pure heading lines (we check content, not structure)
    if re.match(r'^#{1,6}\s', stripped):
        return False
    # Skip very short generic lines
    if len(stripped) < 8:
        return False

    # INCLUDE if line has any data fingerprint:
    has_number = bool(re.search(r'\d{2,}', stripped))  # 2+ digit numbers
    has_url = 'http' in stripped.lower()
    has_pipe = '|' in stripped and not stripped.startswith('|--')  # table rows (not separators)
    has_code_id = bool(re.search(r'(?:class |def |self\.|import |from |r\'|r"|\bregex\b)', stripped))
    has_specific = bool(re.search(r'(?:\d+%|\d+x\b|\d+\.\d+|lambda|coefficient|threshold|\$\d)', stripped))
    has_citation = bool(re.search(r'(?:\(\d{4}\)|et al|Journal|PMC|arXiv|Nature|Science\b|Springer|ScienceDirect)', stripped))
    has_name = bool(re.search(r'(?:Cialdini|Kahneman|Bernays|Goebbels|Tversky|Skinner|Freud|Sunstein|Thaler)', stripped))
    has_enum = bool(re.search(r'(?:class\s+\w+(?:Type|Result|Analysis|Profile|Metrics)\b|@dataclass|Enum\))', stripped))

    return any([has_number, has_url, has_pipe, has_code_id, has_specific, has_citation, has_name, has_enum])

def extract_search_key(line):
    """Extract the most distinctive substring from a line for searching."""
    stripped = line.strip()

    # For table rows, extract cell contents
    if '|' in stripped:
        cells = [c.strip() for c in stripped.split('|') if c.strip()]
        # Return the most distinctive cell (longest non-generic one)
        if cells:
            best = max(cells, key=lambda c: len(c) if not c.startswith('-') else 0)
            if len(best) > 5:
                return best

    # For code lines, extract identifiers
    code_match = re.search(r'(?:class |def )(\w+)', stripped)
    if code_match:
        return code_match.group(1)

    # For URLs, extract the URL
    url_match = re.search(r'https?://\S+', stripped)
    if url_match:
        return url_match.group(0).rstrip(')')

    # For citations, extract author + year
    cite_match = re.search(r'(\w+(?:\s+(?:et al\.?|&\s+\w+))?)\s*\((\d{4})\)', stripped)
    if cite_match:
        return cite_match.group(0)

    # For specific numbers, extract the number with context
    num_match = re.search(r'(\d+\.?\d*[%x]?\b)', stripped)
    if num_match:
        # Get surrounding context
        start = max(0, num_match.start() - 15)
        end = min(len(stripped), num_match.end() + 15)
        return stripped[start:end].strip()

    # Fallback: use longest word sequence (8+ chars)
    words = stripped.split()
    long_words = [w for w in words if len(w) >= 6 and w.isalpha()]
    if long_words:
        return long_words[0]

    return stripped[:40]

def check_presence(search_key, target_content):
    """Check if search key appears in target content."""
    # Normalize both for comparison
    key_lower = search_key.lower().strip()
    target_lower = target_content.lower()

    if key_lower in target_lower:
        return True

    # Try with common substitutions
    # Arrow notation variants
    for old, new in [(' then ', ' → '), (' → ', ' then '), ('→', '->'), ('->', '→')]:
        if old in key_lower:
            if key_lower.replace(old, new) in target_lower:
                return True

    # Try just the core data (strip markdown formatting)
    core = re.sub(r'[*_`\[\]()]', '', key_lower).strip()
    if len(core) > 5 and core in target_lower:
        return True

    return False

def verify_source(git_path, target_file):
    """Verify all data lines from source exist in target."""
    source_content = get_source_content(git_path)
    target_path = os.path.join(PROMPT_DIR, target_file)

    with open(target_path, 'r', encoding='utf-8', errors='replace') as f:
        target_content = f.read()

    missing = []
    checked = 0

    for i, line in enumerate(source_content.split('\n'), 1):
        if not is_data_line(line):
            continue

        checked += 1
        search_key = extract_search_key(line)

        if not check_presence(search_key, target_content):
            # Double-check with the full line content
            line_stripped = line.strip()
            # Try finding any 15-char substring
            found_substring = False
            for start in range(0, len(line_stripped) - 15, 5):
                substr = line_stripped[start:start+15].lower()
                if substr in target_content.lower():
                    found_substring = True
                    break

            if not found_substring:
                missing.append((i, search_key, line.strip()))

    return checked, missing

def main():
    print("=" * 80)
    print("ZERO-LOSS CONSOLIDATION VERIFICATION")
    print("=" * 80)

    # Group by target prompt
    by_target = {}
    for src, tgt in MAPPING.items():
        by_target.setdefault(tgt, []).append(src)

    total_checked = 0
    total_missing = 0
    all_missing = {}

    for target, sources in sorted(by_target.items()):
        print(f"\n{'='*60}")
        print(f"TARGET: {target}")
        print(f"{'='*60}")

        target_missing = []
        target_checked = 0

        for src in sorted(sources):
            checked, missing = verify_source(src, target)
            target_checked += checked
            total_checked += checked

            src_short = src.split('/')[-1]
            if missing:
                print(f"\n  SOURCE: {src_short}")
                print(f"  Checked: {checked} data lines | MISSING: {len(missing)}")
                for line_num, key, full_line in missing:
                    print(f"    Line {line_num}: [{key[:50]}]")
                    print(f"      Full: {full_line[:100]}")
                target_missing.extend([(src_short, *m) for m in missing])
                total_missing += len(missing)
            else:
                print(f"  ✅ {src_short}: {checked} data lines all verified")

        if target_missing:
            all_missing[target] = target_missing

        print(f"  --- {target}: {target_checked} checked, {len(target_missing)} missing ---")

    print(f"\n{'='*80}")
    print(f"SUMMARY: {total_checked} data lines checked across {len(MAPPING)} source files")
    print(f"MISSING: {total_missing} data points not found in targets")
    print(f"MATCH RATE: {(total_checked - total_missing) / total_checked * 100:.1f}%")
    print(f"{'='*80}")

    if all_missing:
        print(f"\nDETAILED MISSING ITEMS BY TARGET:")
        for target, items in all_missing.items():
            print(f"\n--- {target} ---")
            for src, line_num, key, full_line in items:
                print(f"  [{src} L{line_num}] {full_line[:120]}")

if __name__ == '__main__':
    main()
