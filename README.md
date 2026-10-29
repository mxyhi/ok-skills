# OK Skills: AI Coding Agent Skills for Codex, Claude Code, Cursor, OpenClaw, Autohand Code, and More

English | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli) [![Install with AIPM](https://www.aipm-registry.com/install-with-aipm.svg)](https://www.aipm-registry.com/skills/mxyhi/agent-browser/1.0.0?utm_source=github&utm_medium=readme&utm_campaign=package_badge)

Curated AI coding agent skills and `CLAUDE.md` / `AGENTS.md` playbooks for Codex, Claude Code, Cursor, OpenClaw, Autohand Code, Trae, and other `SKILL.md`-compatible tools.

This repo currently bundles **33 reusable skills**, all maintained as top-level skill directories in this repo. Clone it into `~/.agents/skills/ok-skills`; the directories inside already match the layout expected by `AGENTS.md`-driven workflows, and [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) provides a Claude Code-oriented agent playbook.

If you are looking for **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **CLAUDE.md / AGENTS.md** playbooks, or practical **SKILL.md** examples, this repository is designed to be both searchable and immediately usable.

**Popular use cases:** docs lookup, browser automation, prompt engineering, planning workflows, task management, codebase understanding, frontend design, PDF/Word/PPTX/XLSX authoring.

## Who This Repo Is For

- You use Codex, Claude Code, Cursor, OpenClaw, Autohand Code, Trae, or another AI coding agent and want reusable skills instead of ad-hoc prompts.
- You maintain `CLAUDE.md` / `AGENTS.md` / `SKILL.md` workflows and want portable instructions that work across projects.
- You need battle-tested skills for docs lookup, browser automation, planning, prompt engineering, frontend design, PDFs, Office documents, slide decks, and spreadsheets.

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

For Claude Code or Codex global instructions, start from [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) and copy or merge it into Claude Code's `CLAUDE.md` or Codex's `AGENTS.md`. It packages a Chinese-first, KISS-oriented workflow with current-doc/source checks, multi-agent preference, `planning-with-files` / `karpathy-guidelines` defaults, strict TypeScript expectations, and context-mode routing rules. Before reusing it, edit the `语言要求` section for your project. The `其他注意项` section is intentionally project-local and can be edited as needed.

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

- [find-docs](find-docs/SKILL.md): focused Context7 CLI workflow for current documentation lookup.
- [exa-search](exa-search/SKILL.md): web, code, and company research with Exa search tools.
- [reverse-engineer-anything](reverse-engineer-anything/SKILL.md): investigate shipped applications and binaries when source code does not explain behavior; use REA's CLI/MCP to gather evidence and compare versions.
- [get-api-docs](get-api-docs/SKILL.md): fetch current third-party API and SDK documentation before coding.
- [find-skills](find-skills/SKILL.md): discover existing skills when a user asks for a capability.
- [ax](ax/SKILL.md): AI-era curl — fetch pages, discover structure, extract structured data without throwaway parsing scripts.

### Planning & Prompting

- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning with `task_plan.md`, `findings.md`, and `progress.md`.
- [ledger-tasks-yylo](ledger-tasks-yylo/SKILL.md): durable in-repo task state for coding agents — Kanban tasks with stable IDs, evidence-backed status marks, blocked-by dependencies, and next-ready selection.
- [product-decision-agent](product-decision-agent/SKILL.md): Chinese-first product decision support for bottleneck diagnosis, prioritization, growth, metrics, operations, and cross-team delivery.
- [autoresearch](autoresearch/SKILL.md): autonomous goal-directed iteration with explicit goals, metrics, verify loops, and keep/discard gates.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): disciplined diagnosis loop for hard bugs and performance regressions.
- [grilling](grilling/SKILL.md): reusable design-tree interview loop for direct grill sessions.
- [teach](teach/SKILL.md): run a stateful teaching workspace with missions, resources, lessons, and learning records.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `GLOSSARY.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): find deepening opportunities that improve locality, leverage, testability, and AI navigation.
- [prototype](prototype/SKILL.md): build throwaway logic or UI prototypes to answer design questions quickly.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): behavioral coding guidelines that reduce overcomplication, hidden assumptions, and unverifiable changes.
- [ponytail](ponytail/SKILL.md): Apply YAGNI, reuse existing code, and prefer standard-library and native-platform solutions to reduce over-engineering; supports lite, full, and ultra modes.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): migrate test `as` assertions to `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): test-first red-green-refactor for features, bugfixes, refactors, and behavior changes.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation for navigation, forms, screenshots, and scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): control the user's real browser through a local daemon for navigation, forms, screenshots, page reading, and authenticated sessions.
- [browser-trace](browser-trace/SKILL.md): CDP trace capture for browser automation runs, with screenshots, DOM dumps, and per-page buckets.
- [opencli](opencli/opencli-usage/SKILL.md): turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.
- [orca-replay](orca-replay/SKILL.md): answer questions about an earlier agent run from its recording instead of from memory, and replay or fork that run offline.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): build AI chat UI components for the `ai-elements` library.
- [huashu-design](huashu-design/SKILL.md): produce high-fidelity HTML prototypes, slide decks, motion demos, design variants, video exports, and design critiques.
- [imagegen-frontend-web](imagegen-frontend-web/SKILL.md): generate premium frontend reference images, one horizontal image per section, with strong art direction.
- [better-icons](better-icons/SKILL.md): search, browse, and retrieve SVG icons from 200+ Iconify libraries via CLI or MCP.

### Utilities & Authoring

- [bopomofo-rescue](bopomofo-rescue/SKILL.md): recover Chinese typed on a Taiwanese Bopomofo (注音) keyboard while the IME was stuck in English mode, e.g. su3cl3a8 → 你好嗎.
- [skill-skill](skill-skill/SKILL.md): write, upgrade, and audit Claude skills, with a static audit script that reports a 0-100 health score.
- [huashu-design](huashu-design/SKILL.md): create HTML decks, editable PPTX exports, MP4/GIF motion pieces, and narrated design videos.

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) tracks [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) as its upstream baseline. This repository keeps that upstream directory as the canonical baseline for the local skill. Local differences are limited to `skills-ref`-compatible `SKILL.md` frontmatter and install-location-independent relative script paths in docs.

### Upstream Migration Notes (2026-09-30)

- The Matt Pocock engineering skills now use `GLOSSARY.md` and `GLOSSARY-MAP.md` for domain vocabulary. Existing `CONTEXT.md` / `CONTEXT-MAP.md` glossaries need to be renamed and their links updated; ADRs stay under `docs/adr/`.
- OpenCLI upstream removed sitemap skills, bundled sitemaps, and external CLI passthrough. Use the current browser/adapter skills and site memory; invoke external CLIs directly.

### Upstream Migration Notes (2026-10-18)

- OpenCLI commands now default to `{ok:true,data:...}` JSON results. Adapter creation and validation use `opencli adapter init|check|test`; update scripts that parse the old output or use the former browser adapter commands. The CLI itself must support these commands.
- Huashu Design 3.0 organizes work by output module and starts new visual designs with six thumbnails and three complete directions for selection. Pure exports and mechanical edits are exempt.
- Kimi WebBridge skill 2.0.24 documents tab attachment and paginated ARIA snapshots. These features require a matching daemon and browser extension; syncing this repository only updates the skill files.

### Upstream Migration Notes (2026-10-29)

- Planning with Files 3.26.0 adds explicit plan-format validation (`check-complete.sh --validate` / `check-complete.ps1 -Validate`). New plans must retain native phase headings and status markers; existing plans are reported without being rewritten. `PWF_SKIP_SUBAGENTS=1` optionally skips subagent tool-hook injection.
- REA skill version 55 adds AgentEnv bundles, more artifact/runtime workflows, and separate recovery guidance for plugin-owned and setup-owned MCP registrations. Use the capabilities advertised by the installed REA runtime; syncing the skill does not upgrade it.
- `imagegen-frontend-web` moved to [`Leonxlnx/imagegen-skills`](https://github.com/Leonxlnx/imagegen-skills/tree/main/skills/imagegen-frontend-web). Its skill name and vendored content are unchanged.

## Common Prerequisites

- Some skills assume `gh` is installed and authenticated.
- Browser-focused skills may require a Chrome/CDP-capable environment.
- Third-party doc lookup skills may depend on external CLIs or MCP tools; check each `SKILL.md` for details.

## Full Skill Index

`Source URL` points to the canonical upstream when a skill is vendored/imported; otherwise it points to the skill directory in this repository.

### Top-Level Skills

| Skill                                                               | Description                                                                                                                                                                             | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | Browser automation CLI for AI agents: navigation, form filling, screenshots, extraction, and web testing.                                                                               | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | Create new AI chat interface components for the ai-elements library with composable patterns and shadcn/ui conventions.                                                                 | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [autoresearch](autoresearch/SKILL.md)                               | Autonomous goal-directed iteration engine for modify, verify, keep/discard, and repeat workflows.                                                                                      | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [ax](ax/SKILL.md)                                                   | AI-era curl: fetch URLs, discover page structure, and extract structured data from HTML without throwaway parsing scripts.                                                  | [yusukebe/ax](https://github.com/yusukebe/ax/tree/main/skills/ax)                                                             |

| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons through CLI or MCP tools.                                                                                                          | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [bopomofo-rescue](bopomofo-rescue/SKILL.md) | Recover Chinese typed on a Taiwanese Bopomofo (注音) keyboard while the IME was stuck in English mode, e.g. su3cl3a8 → 你好嗎. | [Oliviaiii/bopomofo-rescue](https://github.com/Oliviaiii/bopomofo-rescue) |
| [skill-skill](skill-skill/SKILL.md) | Write, upgrade, or audit a Claude skill so it changes what gets generated, with forcing functions, trigger-ready descriptions, and a static lint script that scores skill health 0-100. | [https://github.com/jack-reson8/skill-skill](https://github.com/jack-reson8/skill-skill) |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Control the user's real browser through a local daemon for navigation, forms, screenshots, page reading, and authenticated sessions.                                                   | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | Capture CDP traces, screenshots, and DOM dumps for browser automation debugging.                                                                                                        | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Disciplined diagnosis loop for hard bugs and performance regressions.                                                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [deep-research](deep-research/SKILL.md)                                       | Professional deep research reports with multi-agent parallel writing, current-data targeting, multilingual output, and built-in quality checks.                                      | [hoolulu/deep-research](https://github.com/hoolulu/deep-research/tree/main)                                                        |
| [find-docs](find-docs/SKILL.md)                                     | Use the Context7 CLI for current documentation lookup, API references, and code examples.                                                                                              | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                            | Custom                                                                                                                         |
| [reverse-engineer-anything](reverse-engineer-anything/SKILL.md) | Investigate shipped applications and binaries when source code does not explain behavior; use REA's CLI/MCP to gather evidence and compare versions. | [morluto/rea](https://github.com/morluto/rea/tree/main/.agents/skills/reverse-engineer-anything) |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                      | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | Create high-fidelity HTML prototypes, interactive demos, slide decks, motion design, design variants, video exports, and critiques.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [imagegen-frontend-web](imagegen-frontend-web/SKILL.md) | Generate premium frontend reference images, one horizontal image per section, with strong art direction. | [Leonxlnx/imagegen-skills](https://github.com/Leonxlnx/imagegen-skills/tree/main/skills/imagegen-frontend-web) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                          | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grilling](grilling/SKILL.md)                               | Reusable design-tree interview loop for direct grill sessions.                                                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | Teach a user a skill or concept through a stateful workspace of missions, resources, lessons, and learning records. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `GLOSSARY.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Find deepening opportunities that improve locality, leverage, testability, and AI navigation.                                                                                           | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [prototype](prototype/SKILL.md) | Build throwaway logic or UI prototypes to answer design questions quickly. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Behavioral coding guidelines that reduce overcomplication, hidden assumptions, and unverifiable changes.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [ponytail](ponytail/SKILL.md) | Apply YAGNI, reuse existing code, and prefer standard-library and native-platform solutions to reduce over-engineering; supports lite, full, and ultra modes. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/main/skills/ponytail) |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migrate test files from `as` type assertions to `@total-typescript/shoehorn`.                                                                                                           | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.                                                                               | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                           | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) |
| [product-decision-agent](product-decision-agent/SKILL.md)           | Chinese-first product decision support for bottleneck diagnosis, prioritization, growth, metrics, operations, and cross-team delivery.                                                | [atdy/maoxuan-product-agent](https://github.com/atdy/maoxuan-product-agent/tree/main/product-decision-agent)                    |
| [ledger-tasks-yylo](ledger-tasks-yylo/SKILL.md)                     | Durable in-repo task state for coding agents: Kanban tasks with stable IDs, evidence-backed status marks, blocked-by dependencies, and next-ready selection.                            | [yylo-dev/yylo-skills](https://github.com/yylo-dev/yylo-skills/tree/main/skills/ledger-tasks-yylo)                             |
| [tdd](tdd/SKILL.md)                                                 | Use before any feature, bugfix, refactor, or behavior change; prefers public-interface integration tests.                                                                                | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## Contributing

Contributions are welcome for new skills or improvements to existing ones.

1. Keep trigger conditions explicit and testable.
2. Keep examples concise and execution-oriented.
3. If a skill depends on external tools, document that dependency in `SKILL.md`.
4. Update `README.md` and `README.zh-CN.md` when you add or rename a skill, and refresh the other translated READMEs when the public-facing skill index changes.

## License

This repository is licensed under [LICENSE](LICENSE).
