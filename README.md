# OK Skills

English | [简体中文](README.zh-CN.md)

A curated collection of skills for the pi coding agent / Codex / Claude Code and other agents.

## Skills

| Skill                                                               | Description                                                                                     |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [agent-browser](agent-browser/SKILL.md)                             | Automates browser interactions for web testing, form filling, screenshots, and data extraction. |
| [brainstorming](brainstorming/SKILL.md)                             | Use before any creative work to clarify intent, requirements, and design.                       |
| [context7](context7/SKILL.md)                                       | Fetch up-to-date library docs via Context7 for APIs, examples, and correct usage.               |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web/code/company research with parameters and examples; for online search.          |
| [find-skills](find-skills/SKILL.md)                                 | Discover and install existing skills when users ask for specialized capabilities.               |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Address PR review/issue comments with gh CLI after verifying auth.                              |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspect failing GitHub Actions checks, summarize logs, and plan fixes.                          |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using task_plan/findings/progress.                        |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Advanced prompt engineering patterns for reliable, production LLMs.                             |
| [skill-creator](skill-creator/SKILL.md)                             | Guide for creating or updating skills with specialized knowledge, workflows, and tool integrations. |
| [test-driven-development](test-driven-development/SKILL.md)         | TDD workflow: write tests first for any feature or fix.                                         |
| [xlsx](xlsx/SKILL.md)                                               | Comprehensive spreadsheet creation, editing, and analysis with formulas, formatting, and charts.|

## Structure

```
skill-name/
  SKILL.md
  scripts/       # optional
  references/    # optional
  assets/        # optional
```

## Usage

1. Pick a skill directory.
2. Read `SKILL.md` for triggers and workflow.
3. Load the skill with your agent's skill manager.
