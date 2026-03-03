# OK Skills

English | [简体中文](README.zh-CN.md)

A curated collection of skills for the pi coding agent / Codex / Claude Code and other agents.

## What This Repo Includes

- Ready-to-use skills under separate folders (`<skill-name>/SKILL.md`).
- Optional references/scripts/licenses bundled with individual skills when needed.
- A bilingual overview (`README.md` + `README.zh-CN.md`).

## Quick Start

1. Clone this repository.
2. Copy the skill folders you need into your local skill directory (for example: `~/.codex/skills` or `~/.agents/skills`).
3. In your project instructions (such as `AGENTS.md`), define when each skill should be triggered.
4. Invoke by name or ask naturally; the agent can pick matching skills based on intent.

No build step is required.

## Skills

| Skill                                                               | Description                                                                                     |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [agent-browser](agent-browser/SKILL.md)                             | Automates browser interactions for web testing, form filling, screenshots, and data extraction. |
| [brainstorming](brainstorming/SKILL.md)                             | Use before any creative work to clarify intent, requirements, and design.                       |
| [context7](context7/SKILL.md)                                       | Fetch up-to-date library docs via Context7 for APIs, examples, and correct usage.               |
| [dogfood](dogfood/SKILL.md)                                         | Systematically test web apps and deliver reproducible issue reports with screenshots/videos.     |
| [electron](electron/SKILL.md)                                       | Automate Electron desktop apps via agent-browser and Chrome DevTools Protocol (CDP).            |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web/code/company research with parameters and examples; for online search.          |
| [find-skills](find-skills/SKILL.md)                                 | Discover and install existing skills when users ask for specialized capabilities.               |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Address PR review/issue comments with gh CLI after verifying auth.                              |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspect failing GitHub Actions checks, summarize logs, and plan fixes.                          |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using task_plan/findings/progress.                        |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Advanced prompt engineering patterns for reliable, production LLMs.                             |
| [skill-creator](skill-creator/SKILL.md)                             | Guide for creating or updating skills with specialized knowledge, workflows, and tool integrations. |
| [taste-skill](taste-skill/SKILL.md)                                 | Senior UI/UX engineering skill for intentional, high-quality frontend design decisions.         |
| [test-driven-development](test-driven-development/SKILL.md)         | TDD workflow: write tests first for any feature or fix.                                         |
| [xlsx](xlsx/SKILL.md)                                               | Comprehensive spreadsheet creation, editing, and analysis with formulas, formatting, and charts.|

## Structure

```text
ok-skills/
  README.md
  README.zh-CN.md
  <skill-name>/
    SKILL.md
    references / scripts / examples (optional)
```

## Contributing

Contributions are welcome for new skills or improvements to existing ones.

1. Keep trigger conditions explicit and testable.
2. Keep examples concise and execution-oriented.
3. If a skill depends on external tools, document that dependency in `SKILL.md`.

## License

This repository is licensed under [LICENSE](LICENSE).
Some skills may include additional license files for skill-specific assets (for example under `xlsx/` and `skill-creator/`).
