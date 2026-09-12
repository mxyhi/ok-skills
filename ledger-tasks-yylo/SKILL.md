---
name: ledger-tasks-yylo
description: Durable in-repo task state for coding agents — Kanban tasks with stable IDs, evidence-backed status marks, blocked-by dependencies, and next-ready selection. Use when starting, selecting, sequencing, or closing implementation tasks for a coding-agent project.
---

# YYLO Ledger Task Management

Use this skill when a coding agent needs durable, reviewable task state that lives in the repository instead of a chat transcript. YYLO Ledger is the source of truth for task state; this skill teaches the working loop.

Adapted from the canonical [`ledger-tasks-yylo`](https://github.com/yylo-dev/yylo-skills/tree/main/skills/ledger-tasks-yylo) skill in yylo-dev/yylo-skills; see the upstream `SKILL.md` for the full CLI reference (archives, multi-directory merges, controller routing).

## When to Use

- Decide which task is safe to start next (`ready` = all blockers done)
- Start assigned work and record an evidence receipt (`mark in_progress --response`)
- Close a task with what changed and how it was tested (`mark done --response --commit`)
- Declare dependencies between tasks before creating them
- Sequence parallel work topologically (`order --scores`)

## Workflow

1. Pick work: `yy ledger ready` (or `yy ledger list --status todo,in_progress`).
2. Inspect full state before any mutation: `yy ledger get TASK_ID` (includes resolved `blocked_by` and related tasks).
3. Start: `yy ledger mark in_progress --id TASK_ID --response "Starting: <plan>"`.
4. Finish: `yy ledger mark done --id TASK_ID --response "Done: <what> — tested <how>" --commit <sha>`.
5. If the task cannot proceed, keep the blocker explicit instead of closing it silently.

## Core Commands

```bash
yy ledger create "Short, one-iteration task" --status backlog --tags feature,backend
yy ledger list --status todo,in_progress --limit 10
yy ledger search --tag backend --open
yy ledger get TASK_ID
yy ledger update TASK_ID --tags backend,urgent
yy ledger deps add --id TASK_ID --blocked-by BLOCKER1 BLOCKER2
yy ledger ready --tag backend
yy ledger order --scores
yy ledger archive TASK_ID        # soft delete, preserves data
```

Inline body markup is parsed on create/update, so dependencies can be declared in prose:

```
[blocked_by]TASK_ID[/blocked_by]     — this task waits on TASK_ID
[task_id]RELATED_ID[/task_id]        — cross-reference a related task
```

## Best Practices

- Keep tasks small enough to finish in one iteration without filling the context window.
- Status flow: `backlog -> todo -> in_progress -> done` (`archive` for abandoned tasks).
- Always pass `--response` on `mark`; attach `--commit` when marking done so task history links to the diff.
- Use `ready` before starting, and `order --scores` when planning parallel pipelines.
- Read state with `get` before mutating; never bypass the CLI with direct file edits.

## Prerequisites

- YYLO CLI: `npm install --global '@yylo/cli@latest'` (Node.js 20.10+, npm, Git). `yy ledger` delegates to the standalone [YYLO Ledger](https://github.com/yylo-dev/yylo-ledger) Git-native task store (MIT).
- Task state lives under the repository's `.juno_task/` directory and is committed with the project, so any agent or reviewer can reconstruct decisions from history.
