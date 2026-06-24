# OK Skills: AI Coding Agent Skills for Codex, Claude Code, Cursor, OpenClaw, and More

English | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Curated AI coding agent skills and `CLAUDE.md` / `AGENTS.md` playbooks for Codex, Claude Code, Cursor, OpenClaw, Trae, and other `SKILL.md`-compatible tools.

This repo currently bundles **30 reusable skills**, all maintained as top-level skill directories in this repo. Clone it into `~/.agents/skills/ok-skills`; the directories inside already match the layout expected by `AGENTS.md`-driven workflows, and [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) provides a Claude Code-oriented agent playbook.

If you are looking for **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **CLAUDE.md / AGENTS.md** playbooks, or practical **SKILL.md** examples, this repository is designed to be both searchable and immediately usable.

**Popular use cases:** docs lookup, browser automation, prompt engineering, planning workflows, frontend design, PDF/Word/PPTX/XLSX authoring.

## Who This Repo Is For

- You use Codex, Claude Code, Cursor, OpenClaw, Trae, or another AI coding agent and want reusable skills instead of ad-hoc prompts.
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

- [find-docs](find-docs/SKILL.md): focused Context7 CLI workflow for current documentation lookup.
- [exa-search](exa-search/SKILL.md): web, code, and company research with Exa search tools.
- [get-api-docs](get-api-docs/SKILL.md): fetch current third-party API and SDK documentation before coding.
- [find-skills](find-skills/SKILL.md): discover existing skills when a user asks for a capability.

### Planning & Prompting

- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning with `task_plan.md`, `findings.md`, and `progress.md`.
- [autoresearch](autoresearch/SKILL.md): autonomous goal-directed iteration with explicit goals, metrics, verify loops, and keep/discard gates.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): disciplined diagnosis loop for hard bugs and performance regressions.
- [grill-me](grill-me/SKILL.md): stress-test a plan or design through a focused one-question-at-a-time interview.
- [grill-with-docs](grill-with-docs/SKILL.md): challenge a plan against domain language, `CONTEXT.md`, and ADRs while updating docs inline.
- [grilling](grilling/SKILL.md): reusable one-question-at-a-time interview loop behind `grill-me` and `grill-with-docs`.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): find deepening opportunities that improve locality, leverage, testability, and AI navigation.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): behavioral coding guidelines that reduce overcomplication, hidden assumptions, and unverifiable changes.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): migrate test `as` assertions to `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): test-first red-green-refactor for features, bugfixes, refactors, and behavior changes.
- [systematic-debugging](systematic-debugging/SKILL.md): investigate root causes methodically before proposing fixes.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation for navigation, forms, screenshots, and scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): control the user's real browser through a local daemon for navigation, forms, screenshots, page reading, and authenticated sessions.
- [browser-trace](browser-trace/SKILL.md): CDP trace capture for browser automation runs, with screenshots, DOM dumps, and per-page buckets.
- [opencli](opencli/opencli-usage/SKILL.md): turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.
- [xquik-twitter](xquik-twitter/SKILL.md): search X/Twitter data and run approval-gated account actions through the Xquik API.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): build AI chat UI components for the `ai-elements` library.
- [huashu-design](huashu-design/SKILL.md): produce high-fidelity HTML prototypes, slide decks, motion demos, design variants, video exports, and design critiques.
- [better-icons](better-icons/SKILL.md): search, browse, and retrieve SVG icons from 200+ Iconify libraries via CLI or MCP.

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): professional DOCX creation, editing, and formatting with OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): generate, fill, and reformat PDFs with a token-based design system.
- [pptx-generator](pptx-generator/SKILL.md): generate, edit, and read PowerPoint presentations with PptxGenJS, XML workflows, or markitdown.
- [huashu-design](huashu-design/SKILL.md): create HTML decks, editable PPTX exports, MP4/GIF motion pieces, and narrated design videos.
- [minimax-xlsx](minimax-xlsx/SKILL.md): open, create, read, analyze, edit, and validate Excel or spreadsheet files with low-loss XML workflows.

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) tracks [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) as its upstream baseline. This repository keeps that upstream directory as the canonical baseline for the local skill. Local differences are limited to `skills-ref`-compatible `SKILL.md` frontmatter and install-location-independent relative script paths in docs.

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
| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons through CLI or MCP tools.                                                                                                          | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Control the user's real browser through a local daemon for navigation, forms, screenshots, page reading, and authenticated sessions.                                                   | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | Capture CDP traces, screenshots, and DOM dumps for browser automation debugging.                                                                                                        | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | Ultra-compressed communication mode that cuts response tokens by speaking like caveman while keeping technical accuracy.                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Disciplined diagnosis loop for hard bugs and performance regressions.                                                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | Use the Context7 CLI for current documentation lookup, API references, and code examples.                                                                                              | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                      | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | Create high-fidelity HTML prototypes, interactive demos, slide decks, motion design, design variants, video exports, and critiques.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                          | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grill-me](grill-me/SKILL.md)                                 | Interview the user relentlessly about a plan or design until shared understanding is reached.                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)                                |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | Stress-test a plan against domain language, `CONTEXT.md`, and ADRs, updating documentation inline.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [grilling](grilling/SKILL.md)                               | Reusable one-question-at-a-time interview loop behind `grill-me` and `grill-with-docs`.                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Find deepening opportunities that improve locality, leverage, testability, and AI navigation.                                                                                           | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Behavioral coding guidelines that reduce overcomplication, hidden assumptions, and unverifiable changes.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migrate test files from `as` type assertions to `@total-typescript/shoehorn`.                                                                                                           | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.                                                                               | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [xquik-twitter](xquik-twitter/SKILL.md)                         | Search X/Twitter data and run approval-gated account actions through the Xquik API.                                                                                                  | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)             |
| [minimax-pdf](minimax-pdf/SKILL.md) | Generate, fill, and reformat PDF documents with a token-based design system. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                           | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) |
| [pptx-generator](pptx-generator/SKILL.md) | Generate, edit, and read PowerPoint presentations with PptxGenJS, XML workflows, or markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | Use before any feature, bugfix, refactor, or behavior change; prefers public-interface integration tests.                                                                                | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes.                                                                                           | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Open, create, read, analyze, edit, and validate Excel or spreadsheet files with low-loss XML workflows. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
## Contributing

Contributions are welcome for new skills or improvements to existing ones.

1. Keep trigger conditions explicit and testable.
2. Keep examples concise and execution-oriented.
3. If a skill depends on external tools, document that dependency in `SKILL.md`.
4. Update `README.md` and `README.zh-CN.md` when you add or rename a skill, and refresh the other translated READMEs when the public-facing skill index changes.

## License

This repository is licensed under [LICENSE](LICENSE).
