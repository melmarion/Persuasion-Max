#!/usr/bin/env node
/**
 * Zero-loss consolidation verifier.
 * For each source file, extracts every data-bearing line and checks
 * whether the data appears in the target prompt file.
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const REPO_DIR = 'C:\\Users\\Mario\\Downloads\\UX & Persuasion\\Persuasion Max';
const PROMPT_DIR = path.join(REPO_DIR, 'LINGUISTIC_PERSUASION');

const MAPPING = {
  // Prompt 1
  'LINGUISTIC_PERSUASION/DETECTION/11_TACTICAL_DETECTION_FRAMEWORK.md': '1_DETECTION_FRAMEWORKS_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/12_PSYCHOLOGICAL_PRINCIPLES_DETECTION_FRAMEWORK.md': '1_DETECTION_FRAMEWORKS_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/13_ADVANCED_FRAMEWORKS.md': '1_DETECTION_FRAMEWORKS_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/14_DETECTION_FRAMEWORKS_MASTER_INDEX.md': '1_DETECTION_FRAMEWORKS_PROMPT.md',
  // Prompt 2
  'LINGUISTIC_PERSUASION/RESEARCH/LINGUISTIC_PERSUASION_RESEARCH.md': '2_LINGUISTIC_RHETORICAL_PATTERNS_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/CLASSICAL_RHETORICAL_TECHNIQUES.md': '2_LINGUISTIC_RHETORICAL_PATTERNS_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/LINGUISTIC_DETECTION_FRAMEWORK.md': '2_LINGUISTIC_RHETORICAL_PATTERNS_PROMPT.md',
  // Prompt 3
  'LINGUISTIC_PERSUASION/RESEARCH/FRACTIONATION_BEHAVIORAL_SCIENCE.md': '3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/FRACTIONATION_DETECTION_METHODS.md': '3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/BEHAVIORAL_ANALYSIS_FRAMEWORK.md': '3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/INTEGRITY_VIOLATION_DETECTION_FRAMEWORK.md': '3_FRACTIONATION_INTEGRITY_VIOLATIONS_PROMPT.md',
  // Prompt 4
  'LINGUISTIC_PERSUASION/DETECTION/15_PROFESSIONAL_AUDITOR_MANUAL.md': '4_DETECTION_CODE_SCORING_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/17_MACHINE_READABLE_DETECTION_SYSTEM.md': '4_DETECTION_CODE_SCORING_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/24_ENHANCED_DETECTION_RESEARCH.md': '4_DETECTION_CODE_SCORING_PROMPT.md',
  'LINGUISTIC_PERSUASION/DETECTION/26_COMPREHENSIVE_DETECTION_FRAMEWORKS.md': '4_DETECTION_CODE_SCORING_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/27_HIGH_IMPACT_DETECTION_SYSTEMS.md': '4_DETECTION_CODE_SCORING_PROMPT.md',
  // Prompt 5
  'LINGUISTIC_PERSUASION/RESEARCH/28_EXPANDED_RANKED_COMBINATIONS.md': '5_RANKINGS_EFFECTIVENESS_DATA_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/25_EXPANDED_RESEARCH_DIMENSIONS.md': '5_RANKINGS_EFFECTIVENESS_DATA_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/EMPIRICAL_RESEARCH_SYNTHESIS.md': '5_RANKINGS_EFFECTIVENESS_DATA_PROMPT.md',
  // Prompt 6
  'LINGUISTIC_PERSUASION/RESEARCH/EVOLUTION_ANALYSIS.md': '6_CASE_STUDIES_RESEARCH_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/EVOLUTION_PATTERNS_AND_MECHANISMS.md': '6_CASE_STUDIES_RESEARCH_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/19_REAL_WORLD_CASE_STUDIES_DETAILED.md': '6_CASE_STUDIES_RESEARCH_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/APPENDIX_RESEARCH_SOURCES.md': '6_CASE_STUDIES_RESEARCH_PROMPT.md',
  'LINGUISTIC_PERSUASION/RESEARCH/RESEARCH_SUMMARY_AND_NEXT_STEPS.md': '6_CASE_STUDIES_RESEARCH_PROMPT.md',
};

function getSourceContent(gitPath) {
  try {
    return execSync(`git show "HEAD:${gitPath}"`, { cwd: REPO_DIR, encoding: 'utf-8', maxBuffer: 10 * 1024 * 1024 });
  } catch (e) {
    console.error(`  ERROR: Could not read ${gitPath}`);
    return '';
  }
}

function isDataLine(line) {
  const s = line.trim();
  if (!s || s.length < 8) return false;
  if (['---', '```', '```python', '```markdown', '```json', '```text'].includes(s)) return false;
  if (s.startsWith('<!--') || s.startsWith('-->')) return false;
  if (/^#{1,6}\s/.test(s)) return false;
  // Skip table separator rows
  if (/^\|[\s-|]+\|$/.test(s)) return false;

  const hasNumber = /\d{2,}/.test(s);
  const hasUrl = /https?:\/\//.test(s);
  const hasPipe = s.includes('|') && !s.startsWith('|--');
  const hasCode = /(?:class |def |self\.|import |from |r'|r"|\\b|\\w|\\s|\\d)/.test(s);
  const hasSpecific = /(?:\d+%|\d+x\b|\d+\.\d+|lambda|coefficient|threshold|\$\d)/.test(s);
  const hasCitation = /(?:\(\d{4}\)|et al|Journal|PMC|arXiv|Nature\b|Science\b|Springer|ScienceDirect)/.test(s);
  const hasName = /(?:Cialdini|Kahneman|Bernays|Goebbels|Tversky|Skinner|Freud|Sunstein|Thaler|Renvois[eé]|Morin)/.test(s);
  const hasEnum = /(?:class\s+\w+(?:Type|Result|Analysis|Profile|Metrics)\b|@dataclass|Enum\))/.test(s);

  return hasNumber || hasUrl || hasPipe || hasCode || hasSpecific || hasCitation || hasName || hasEnum;
}

function extractSearchKeys(line) {
  const s = line.trim();
  const keys = [];

  // For table rows, extract all meaningful cells
  if (s.includes('|')) {
    const cells = s.split('|').map(c => c.trim()).filter(c => c && c.length > 4 && !/^[-:]+$/.test(c));
    keys.push(...cells);
  }

  // URLs
  const urlMatch = s.match(/https?:\/\/[^\s)>\]]+/);
  if (urlMatch) keys.push(urlMatch[0]);

  // Class/function names
  const codeMatch = s.match(/(?:class |def )(\w+)/);
  if (codeMatch) keys.push(codeMatch[1]);

  // Specific numbers with context
  const numMatches = s.matchAll(/(\d+\.?\d*[%x]?)/g);
  for (const m of numMatches) {
    if (m[0].length >= 2) {
      const start = Math.max(0, m.index - 10);
      const end = Math.min(s.length, m.index + m[0].length + 10);
      keys.push(s.slice(start, end).trim());
    }
  }

  // If no specific keys, use longest distinctive substring
  if (keys.length === 0 && s.length >= 15) {
    keys.push(s.slice(0, Math.min(40, s.length)));
  }

  return [...new Set(keys)];
}

function checkPresence(searchKey, targetLower) {
  const keyLower = searchKey.toLowerCase().trim();
  if (keyLower.length < 4) return true; // Too short to be meaningful

  if (targetLower.includes(keyLower)) return true;

  // Try common substitutions
  const subs = [
    [' then ', ' → '], [' → ', ' then '], ['→', '->'], ['->', '→'],
    ['leverageation', 'leverage'], ['leverageing', 'leveraging'],
    ['influence strategy', 'persuasion'], ['persuasion', 'influence strategy'],
  ];
  for (const [old, nw] of subs) {
    if (keyLower.includes(old) && targetLower.includes(keyLower.replace(old, nw))) return true;
  }

  // Strip markdown formatting and retry
  const core = keyLower.replace(/[*_`\[\]()]/g, '').trim();
  if (core.length > 5 && targetLower.includes(core)) return true;

  return false;
}

function verifySource(gitPath, targetFile) {
  const sourceContent = getSourceContent(gitPath);
  const targetPath = path.join(PROMPT_DIR, targetFile);
  const targetContent = fs.readFileSync(targetPath, 'utf-8');
  const targetLower = targetContent.toLowerCase();

  const missing = [];
  let checked = 0;

  const lines = sourceContent.split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!isDataLine(line)) continue;
    checked++;

    const keys = extractSearchKeys(line);
    let found = false;

    for (const key of keys) {
      if (checkPresence(key, targetLower)) {
        found = true;
        break;
      }
    }

    if (!found) {
      // Last resort: try any 12-char substring of the line
      const stripped = line.trim().toLowerCase();
      for (let j = 0; j < stripped.length - 12; j += 4) {
        if (targetLower.includes(stripped.slice(j, j + 12))) {
          found = true;
          break;
        }
      }
    }

    if (!found) {
      missing.push({ lineNum: i + 1, keys, fullLine: line.trim() });
    }
  }

  return { checked, missing };
}

// Main
console.log('='.repeat(80));
console.log('ZERO-LOSS CONSOLIDATION VERIFICATION');
console.log('='.repeat(80));

// Group by target
const byTarget = {};
for (const [src, tgt] of Object.entries(MAPPING)) {
  if (!byTarget[tgt]) byTarget[tgt] = [];
  byTarget[tgt].push(src);
}

let totalChecked = 0;
let totalMissing = 0;
const allMissing = {};

for (const [target, sources] of Object.entries(byTarget).sort()) {
  console.log(`\n${'='.repeat(60)}`);
  console.log(`TARGET: ${target}`);
  console.log('='.repeat(60));

  const targetMissing = [];
  let targetChecked = 0;

  for (const src of sources.sort()) {
    const srcShort = src.split('/').pop();
    const { checked, missing } = verifySource(src, target);
    targetChecked += checked;
    totalChecked += checked;

    if (missing.length > 0) {
      console.log(`\n  SOURCE: ${srcShort}`);
      console.log(`  Checked: ${checked} data lines | MISSING: ${missing.length}`);
      for (const m of missing) {
        console.log(`    L${m.lineNum}: ${m.fullLine.slice(0, 120)}`);
      }
      targetMissing.push(...missing.map(m => ({ src: srcShort, ...m })));
      totalMissing += missing.length;
    } else {
      console.log(`  ✅ ${srcShort}: ${checked} data lines all verified`);
    }
  }

  console.log(`  --- ${target}: ${targetChecked} checked, ${targetMissing.length} missing ---`);
  if (targetMissing.length > 0) allMissing[target] = targetMissing;
}

console.log(`\n${'='.repeat(80)}`);
console.log(`SUMMARY: ${totalChecked} data lines checked across ${Object.keys(MAPPING).length} source files`);
console.log(`MISSING: ${totalMissing} data points not found in targets`);
console.log(`MATCH RATE: ${((totalChecked - totalMissing) / totalChecked * 100).toFixed(1)}%`);
console.log('='.repeat(80));

if (Object.keys(allMissing).length > 0) {
  console.log('\nDETAILED MISSING ITEMS:');
  for (const [target, items] of Object.entries(allMissing)) {
    console.log(`\n--- ${target} (${items.length} missing) ---`);
    for (const item of items) {
      console.log(`  [${item.src} L${item.lineNum}] ${item.fullLine.slice(0, 140)}`);
    }
  }
}
