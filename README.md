# OK Skills: AI Coding Agent Skills for Codex, Claude Code, Cursor, OpenClaw, Autohand Code, and More

English | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

> Maintainer-only global installation branch. External contributions must target `main`. See [MAINTAINER_GLOBAL.md](MAINTAINER_GLOBAL.md).

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Curated AI coding agent skills and `CLAUDE.md` / `AGENTS.md` playbooks for Codex, Claude Code, Cursor, OpenClaw, Autohand Code, Trae, and other `SKILL.md`-compatible tools.

This repo currently bundles **18 reusable skills**, all maintained as top-level skill directories in this repo. Clone it into `~/.agents/skills/ok-skills`; the directories inside already match the layout expected by `AGENTS.md`-driven workflows, and [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) provides a Claude Code-oriented agent playbook.

If you are looking for **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **CLAUDE.md / AGENTS.md** playbooks, or practical **SKILL.md** examples, this repository is designed to be both searchable and immediately usable.


## Who This Repo Is For

- You use Codex, Claude Code, Cursor, OpenClaw, Autohand Code, Trae, or another AI coding agent and want reusable skills instead of ad-hoc prompts.
- You maintain `CLAUDE.md` / `AGENTS.md` / `SKILL.md` workflows and want portable instructions that work across projects.

## Start Here

If you only install a few skills first, start with these:

- [planning-with-files](planning-with-files/SKILL.md): file-based planning for complex tasks, research, and long-running work.
- [find-docs](find-docs/SKILL.md): fetch current library docs, API references, and Context7-backed examples.
- [agent-browser](agent-browser/SKILL.md): browser automation for screenshots, forms, scraping, and web QA.

## 1-Minute Quick Start

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

For Autohand Code, clone the repo into either the user-level or project-level skills directory:

```bash
# User-level skills
mkdir -p ~/.autohand/skills
git clone https://github.com/mxyhi/ok-skills.git ~/.autohand/skills/ok-skills

# Project-level skills
mkdir -p .autohand/skills
git clone https://github.com/mxyhi/ok-skills.git .autohand/skills/ok-skills
```

After cloning, the repo lives at `~/.agents/skills/ok-skills`, and the directories inside already follow the expected layout:

```text
~/.agents/skills/ok-skills/
  CLAUDE_AGENTS.md
  planning-with-files/
    SKILL.md
  find-docs/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

For Claude Code or Codex global instructions, start from [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) and copy or merge it into Claude Code's `CLAUDE.md` or Codex's `AGENTS.md`. It packages a Chinese-first, KISS-oriented workflow with current-doc/source checks, multi-agent preference, `caveman` / `planning-with-files` / `karpathy-guidelines` defaults, strict TypeScript expectations, and context-mode routing rules. Before reusing it, edit the `语言要求` section for your project. The `其他注意项` section is intentionally project-local and can be edited as needed.

Add simple trigger rules to your `AGENTS.md`, or merge the same skill triggers into `CLAUDE.md` / `AGENTS.md`:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- find-docs: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Then ask naturally:

- `Use planning-with-files before refactoring this module.`
- `Use find-docs to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Browse Skills by Use Case

### Research & Docs

- [ax](ax/SKILL.md): AI-era curl for agents — fetch, discover page structure, and extract structured data without throwaway parsers.
- [find-docs](find-docs/SKILL.md): focused Context7 CLI workflow for current documentation lookup.
- [exa-search](exa-search/SKILL.md): web, code, and company research with Exa search tools.
- [get-api-docs](get-api-docs/SKILL.md): fetch current third-party API and SDK documentation before coding.
- [find-skills](find-skills/SKILL.md): discover existing skills when a user asks for a capability.

### Planning & Prompting

- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning with `task_plan.md`, `findings.md`, and `progress.md`.
- [autoresearch](autoresearch/SKILL.md): autonomous goal-directed iteration with explicit goals, metrics, verify loops, and keep/discard gates.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): disciplined diagnosis loop for hard bugs and performance regressions.
- [grilling](grilling/SKILL.md): reusable one-question-at-a-time interview loop for direct grill sessions.
- [teach](teach/SKILL.md): run a stateful teaching workspace with missions, resources, lessons, and learning records.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): behavioral coding guidelines that reduce overcomplication, hidden assumptions, and unverifiable changes.
- [tdd](tdd/SKILL.md): test-first red-green-refactor for features, bugfixes, refactors, and behavior changes.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation for navigation, forms, screenshots, and scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): control the user's real browser through a local daemon for navigation, forms, screenshots, page reading, and authenticated sessions.

### Frontend & Design

- [better-icons](better-icons/SKILL.md): search, browse, and retrieve SVG icons from 200+ Iconify libraries via CLI or MCP.
- [diagram-design](diagram-design/SKILL.md): editorial HTML/SVG diagrams across 27 types, with brand tokens and draw.io/Mermaid redraw.

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) tracks [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) as its upstream baseline. This repository keeps that upstream directory as the canonical baseline for the local skill. Local differences are limited to `skills-ref`-compatible `SKILL.md` frontmatter and install-location-independent relative script paths in docs.

## Common Prerequisites

- The `ax` skill requires the `ax` CLI (`curl -fsSL https://ax.yusuke.run/install | sh`).
- The `diagram-design` skill uses Python 3 for import extraction and the packaged self-check.
- Some skills assume `gh` is installed and authenticated.
- Browser-focused skills may require a Chrome/CDP-capable environment.
- Third-party doc lookup skills may depend on external CLIs or MCP tools; check each `SKILL.md` for details.

## Full Skill Index

`Source URL` points to the canonical upstream when a skill is vendored/imported; otherwise it points to the skill directory in this repository.

### Top-Level Skills

| Skill                                                               | Description                                                                                                                                                                             | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [ax](ax/SKILL.md)                                                   | AI-era curl for agents: fetch URLs, discover page structure, and extract structured data without throwaway parsers.                                                                  | [yusukebe/ax](https://github.com/yusukebe/ax/tree/main/skills/ax)                                                              |
| [agent-browser](agent-browser/SKILL.md)                             | Browser automation CLI for AI agents: navigation, form filling, screenshots, extraction, and web testing.                                                                               | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [autoresearch](autoresearch/SKILL.md)                               | Autonomous goal-directed iteration engine for modify, verify, keep/discard, and repeat workflows.                                                                                      | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons through CLI or MCP tools.                                                                                                          | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Control the user's real browser through a local daemon for navigation, forms, screenshots, page reading, and authenticated sessions.                                                   | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [caveman](caveman/SKILL.md)                                         | Ultra-compressed communication mode that cuts response tokens by speaking like caveman while keeping technical accuracy.                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Disciplined diagnosis loop for hard bugs and performance regressions.                                                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [diagram-design](diagram-design/SKILL.md)                             | Editorial HTML/SVG/PNG diagrams across 27 types; onboard brand tokens; redraw draw.io or Mermaid sources.                                                                                                | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design/tree/main/skills/diagram-design) |
| [find-docs](find-docs/SKILL.md)                                     | Use the Context7 CLI for current documentation lookup, API references, and code examples.                                                                                              | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                      | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                          | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grilling](grilling/SKILL.md)                               | Reusable one-question-at-a-time interview loop for direct grill sessions.                                                                                      | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | Teach a user a skill or concept through a stateful workspace of missions, resources, lessons, and learning records. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Behavioral coding guidelines that reduce overcomplication, hidden assumptions, and unverifiable changes.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                           | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) |
| [tdd](tdd/SKILL.md)                                                 | Use before any feature, bugfix, refactor, or behavior change; prefers public-interface integration tests.                                                                                | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## Contributing

Contributions are welcome for new skills or improvements to existing ones.

1. Keep trigger conditions explicit and testable.
2. Keep examples concise and execution-oriented.
3. If a skill depends on external tools, document that dependency in `SKILL.md`.
4. Update `README.md` and `README.zh-CN.md` when you add or rename a skill, and refresh the other translated READMEs when the public-facing skill index changes.

## License

This repository is licensed under [LICENSE](LICENSE).
