# Planning With Files

> **Work like Manus** — Use persistent markdown files as your "working memory on disk."

A `SKILL.md`-compatible planning skill that transforms your workflow to use persistent markdown files for planning, progress tracking, and knowledge storage.

## The Problem

Most AI agents suffer from:
- **Volatile memory** — Context resets lose history
- **Goal drift** — Long tasks lose focus
- **Hidden errors** — Failures aren't tracked

## The Solution

For every complex task, create THREE files:
- `task_plan.md` (Phases & Progress)
- `findings.md` (Research & Notes)
- `progress.md` (Session Log)

---

## Installation

Copy this folder into your agent's skills directory, or vendor it into a repository that distributes skills.

---

## Usage

### Start Planning

Ask your agent:
```
Use the planning-with-files skill to help me with this task.
```
Or:
```
Start by creating task_plan.md.
```

## Important Limitations

> **Note:** Automatic hooks are agent-specific. This generic copy relies on the core 3-file workflow, templates, and helper scripts instead of non-standard `SKILL.md` hooks.

### What works in a generic agent setup:
- Core 3-file planning pattern
- Templates (task_plan.md, findings.md, progress.md)
- All planning rules and guidelines
- The 2-Action Rule
- The 3-Strike Error Protocol
- Session Recovery (via `session-catchup.py`)

### Session Recovery
If you clear context, recover your state:
```bash
python3 scripts/session-catchup.py .
```

## File Structure

When installed, the skill provides templates to create:

```
your-project/
├── task_plan.md
├── findings.md
├── progress.md
```
