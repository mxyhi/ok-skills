---
name: orca-replay
description: Answer questions about an earlier agent run from its recording rather than from memory, and replay or fork that run. Use when the user asks why a previous run did something, which step changed a file or broke the build, whether yesterday's failure still reproduces, or whether a different model would have got it right.
compatibility: "Requires Node 20+ and the `orcareplay` npm package (`npm install -g orcareplay`) with its MCP server registered as `orca`, plus at least one recorded run under the project's `.orca/runs`. Recording is started with `orca record <agent>` — there is no way to recover a session that was never recorded."
license: Apache-2.0
allowed-tools: Bash, Read, Grep
---

# Reading a Recorded Agent Run

A recording is evidence. Your memory of a session is not, and neither is a transcript you were
handed — both are missing the tool results, the exit codes, and the files that changed without
anyone mentioning them.

**The rule: when a question is about something that already happened, read the trace before you
answer.** Do not reconstruct it. If a recording exists, guessing is the wrong move even when the
guess would have been right.

This skill does not drive the agent — it reads what an earlier one did. Pair it with whatever
harness produced the run: Claude Code, Codex, opencode, Cursor, or a framework agent recorded with
`orca record generic-openai -- <cmd>`.

## When to use

- "Why did you delete / overwrite / move X?"
- "What changed this file?" or "Which step broke the build?"
- "Can you reproduce yesterday's failure?"
- "Would a different model have got this right?"

If the user wants to *start* recording rather than read a past run, that is `orca record <agent>`,
not this skill.

## Setup check

```bash
node --version                      # require Node 20+
which orca || npm install -g orcareplay
orca list                           # at least one run, or there is nothing to read
```

## Workflow

### 1. Find the run

`orca_list_runs` — newest first, and it names the run each fork came from. Skip it only when the
user clearly means the most recent one; every other tool defaults to `run: "last"`.

### 2. Narrow to the chain that produced the thing being asked about

`orca_show_run` gives the whole timeline: model turns with token counts and stop reasons, tool
calls with arguments and results, shell commands with exit codes, and every file the run changed.
Good for orientation, long for a specific question.

`orca_graph` is usually the better tool. It returns causal edges — which event produced which. Pass
`to: <event seq>` to get **only** the chain that produced one event. That is the shape of an answer
to "why did this happen"; the full timeline is the shape of an answer to "what happened".

### 3. Report `recorded` and `inferred` differently

Every edge is labelled:

- **`recorded`** — the recorder watched it happen and wrote it into the trace.
- **`inferred`** — derived just now from a rule the edge names. The trace does not vouch for it.

Carry that distinction into your answer. *"The trace shows the `rm` at step 14 removed it"* and
*"this looks like the `rm` at step 14, going by timing"* are different claims, and flattening them
into one confident sentence is the specific failure this skill exists to prevent. Name the rule
when you lean on an inferred edge.

### 4. Reproduce it before explaining it

`orca_replay` re-runs the recording and reports what could not be reproduced — divergences, and
requests the recording could not serve.

**Pass `worktree: true`.** It replays into a scratch copy. Without it, replay restores the recorded
filesystem over the working tree for the duration of the run: uncommitted work is absent in the
meantime, and stays absent if the replay is interrupted before it can restore.

**Check what re-executes before the first replay of a run, not after.** Model responses come from
the trace and no provider is contacted, but the agent process runs again for real — so every shell
command it issued runs again too. Read them with `orca_show_run` first and tell the user what will
re-run. A run that only read files and edited the repository is free and repeatable; one that
reached `/tmp`, Docker, a database, a package manager or another host is not, and needs explicit
approval or a container.

**`reused=3/5` is usually not a partial failure.** Harnesses make calls for themselves — a quota
probe, a session-naming request — and a replay does not repeat them.

**A matching replay is not a determinism result.** The model is not being re-asked; its recorded
answers are served back. If the user wants to know whether a *fresh* run would fail the same way,
say replay cannot answer that.

### 5. Only then consider comparing models

`orca_compare` forks one run onto several models from the same checkpoint — same files, same
conversation prefix, so the model is the only variable. Pick the fork point with `orca_checkpoints`.
Grade with `verify`, a shell command whose exit code is the verdict; use something the repository
already declares (`npm test`, `npm run typecheck`), not `npx <tool>`.

Three separate approvals are needed and they are not the same question:

1. **Disclosure** — each model named receives the run's files and conversation prefix, so whatever
   that run touched is sent to every provider behind those model ids. `orca scrub` first if the
   trace is not safe to send as-is.
2. **Side effects** — each fork is a live agent, not a replay: from the fork point on, the model is
   really being asked and its shell commands execute for real.
3. **Cost** — models times forks, in real money.

Never run it to satisfy curiosity the user did not express.

## If there is no recording

Say so plainly and offer to start one. Do not fall back to reconstructing the session from memory —
that is the failure mode this skill exists to prevent.

```bash
orca record claude          # or codex, opencode, openclaw, grok
```

A run started with its prompt in argv (`orca record claude -- -p "…"`) replays exactly. A session
someone typed into replays approximately, because those prompts were never on the wire and are
recovered from the harness's own transcript; `orca replay` says which is which.

## Sharing a run

`orca export last -o run.html` writes one self-contained file. A trace holds whatever the run held,
so run `orca scrub` first — and treat it as best-effort: it matches known key shapes and
high-entropy strings, and cannot know that a particular internal hostname or customer name is
confidential. Have the user look at what is going out before it goes.

## Limitations

- **It only sees what was recorded.** Unrecorded sessions are unrecoverable.
- **`inferred` edges are not evidence.** They are a reading of the trace, not something the
  recorder witnessed.
- **Not every harness is recordable.** Agents that read no base-URL variable and pin their own
  origin need `--tls-intercept`, and some cannot be reached at all.
- **Replay is not a sandbox.** It blocks model-provider egress, not the network; the run's own
  shell commands reach the world for real.
