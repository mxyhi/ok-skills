---
name: autoresearch:learn
description: "Scout codebase and auto-generate docs with validation-fix loop"
argument-hint: "[Mode: <init|update|check|summarize>] [Scope: <glob>] [Iterations: N] [--depth <level>] [--evals]"
---

EXECUTE IMMEDIATELY.

## Parse Arguments

Extract from $ARGUMENTS:
- `Mode:` or `--mode` — init (create from scratch), update (refresh existing), check (validate), summarize (brief overview)
- `Scope:` or `--scope` — file globs to document
- `Depth:` or `--depth` — overview, standard, comprehensive
- `--file <path>` — specific file to document
- `--scan` — force fresh codebase scout
- `--topics` — comma-separated focus topics
- `--no-fix` — validate only, don't auto-fix issues
- `--format` — markdown (default), json, rst
- `Iterations:` or `--iterations` — default 10. "unlimited" for unbounded.
- `--evals`, `--evals-interval N`, `--chain`, `--<subcommand>`

## Setup (if Mode or Scope missing)

request_user_input (single batch):
  Q1 (Mode): "What to do?" — init (generate docs), update (refresh), check (validate), summarize (overview)
  Q2 (Scope): "Which files?" — suggested globs + entire codebase
  Q3 (Depth): "How detailed?" — overview only, standard, comprehensive
  Q4 (Topics): "Focus on?" — architecture, API, database, testing, all
If all provided → skip.

## Establish Baseline

1. Scout codebase: file tree, imports/exports, existing docs
2. Identify documentation gaps (undocumented files, outdated docs, missing READMEs)
3. Create output directory: `autoresearch/learn-{YYMMDD}-{HHMM}/`
4. TSV header: `# metric_direction: higher_is_better\niteration\ttimestamp\tfile_documented\tvalidation_status\tissues_found\tissues_fixed\tdescription`
5. Metric = files with valid documentation (higher is better)

## Summarize Mode (no loop)

If mode == summarize:
- One-shot: scan codebase → produce structured summary
- Write summary.md to output directory
- Skip iteration loop entirely

## Iteration Loop (init/update/check modes)

### Phase 1: Scout
- Scan for documentation gaps
- Prioritize: no docs → outdated docs → incomplete docs
- If no gaps remain → early stop (SUCCESS)

### Phase 2: Generate/Update
- Pick highest-priority gap
- Write or update documentation for ONE file/module
- Follow project conventions for doc format and location

### Phase 3: Validate
- Check generated docs against code: descriptions accurate? Examples valid? Links work?
- Run doc linters if available
- Record: validation_status (pass/fail), issues found

### Phase 4: Fix (unless --no-fix)
- If validation finds issues → fix the doc
- Commit clean doc: `docs: document {file/module}`

### Phase 5: Log
Append to TSV: iteration, timestamp, file_documented, validation_status, issues_found, issues_fixed, description

### Eval Checkpoint
If --evals: check if current_iteration % interval == 0 → run checkpoint.

### Bounded Check
If bounded: current_iteration >= max_iterations → exit loop.

## Output

- `learn-results.tsv`
- `summary.md` — documentation overview
- `validation-report.md` — issues found/fixed

## Summary

Print: files documented, validation pass rate, issues found/fixed, remaining gaps.

## Eval Checkpoint (--evals flag)

If --evals present:
- Compute interval: floor(max_iterations / 3), min 1. Fixed 10 if unbounded.
- Print: `--- Eval Checkpoint (iterations {X}-{Y}) ---\nDocs written: {n} | Validation: {pass}/{total} | Gaps remaining: {m}\n{recommendation}\n---`
- If 3+ checkpoints with no new docs → recommend early stop.
- At loop end → full evals summary to evals-summary.md.

## Chain Handoff

After completion, write handoff.json: version "2.1.0", source "learn", timestamp, status, results_tsv path, findings = documentation gaps remaining, config{mode, scope, depth}.
Invoke next target in --chain order. Propagate --evals flag.
