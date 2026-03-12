# OK Skills: AI Coding Agent Skills for Codex, Claude Code, Cursor, and More

English | [简体中文](README.zh-CN.md)

Curated AI coding agent skills and AGENTS.md playbooks for Codex, Claude Code, Cursor, Trae, and other SKILL.md-compatible tools.

This repo currently bundles **38 reusable skills**: **20 top-level skills** maintained directly in this repo, plus **18 vendored design skills** under [`impeccable/`](impeccable/README.md). The repository layout already matches the skills convention, so you can clone it directly into `~/.agents/skills` and trigger skills from `AGENTS.md`.

## Who This Repo Is For

- You use Codex, Claude Code, Cursor, Trae, or another AI coding agent and want reusable skills instead of ad-hoc prompts.
- You maintain `AGENTS.md` / `SKILL.md` workflows and want portable instructions that work across projects.
- You need battle-tested skills for docs lookup, browser automation, GitHub workflow, planning, prompt engineering, frontend design, PDF, and spreadsheets.

## Start Here

If you only install a few skills first, start with these:

- [planning-with-files](planning-with-files/SKILL.md): file-based planning for complex tasks, research, and long-running work.
- [ctx7-cli](ctx7-cli/SKILL.md): fetch current library docs and Context7-backed references.
- [agent-browser](agent-browser/SKILL.md): browser automation for screenshots, forms, scraping, and web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspect failing GitHub Actions checks and turn logs into a fix plan.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): production-oriented prompt patterns for more reliable LLM workflows.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): high-quality frontend design skill plus a full bundle of companion design commands.

## 1-Minute Quick Start

```bash
git clone https://github.com/mxyhi/ok-skills.git ~/.agents/skills
```

This works because the repo root already follows the expected layout:

```text
~/.agents/skills/
  planning-with-files/
    SKILL.md
  ctx7-cli/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

Add simple trigger rules to your `AGENTS.md`:

```md
## Skills
- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- ctx7-cli: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Then ask naturally:

- `Use planning-with-files before refactoring this module.`
- `Use ctx7-cli to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Browse Skills by Use Case

### Research & Docs

- [ctx7-cli](ctx7-cli/SKILL.md): official Context7 CLI workflow for docs lookup, skill management, and MCP setup.
- [exa-search](exa-search/SKILL.md): web, code, and company research with Exa search tools.
- [get-api-docs](get-api-docs/SKILL.md): fetch current third-party API and SDK documentation before coding.
- [find-skills](find-skills/SKILL.md): discover existing skills when a user asks for a capability.

### Planning & Prompting

- [brainstorming](brainstorming/SKILL.md): clarify intent, requirements, and design before implementation.
- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning with `task_plan.md`, `findings.md`, and `progress.md`.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): advanced prompt design patterns for production LLM systems.
- [test-driven-development](test-driven-development/SKILL.md): enforce writing tests before implementation work.

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): address review and issue comments on the current PR with `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspect failing GitHub Actions checks, summarize logs, and plan fixes.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation for navigation, forms, screenshots, and scraping.
- [electron](electron/SKILL.md): automate Electron desktop apps over Chrome DevTools Protocol.
- [dogfood](dogfood/SKILL.md): structured exploratory testing with reproducible evidence.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): build AI chat UI components for the `ai-elements` library.
- [design-taste-frontend](design-taste-frontend/SKILL.md): senior frontend design guidance for intentional interfaces.
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): React and Next.js performance guidance from Vercel Engineering.
- [remotion-best-practices](remotion-best-practices/SKILL.md): Remotion guidance for React-based video work.
- [`impeccable/`](impeccable/README.md): 18 vendored frontend design skills, including `frontend-design`, `adapt`, `audit`, `polish`, and more.

### Utilities & Authoring

- [pdf](pdf/SKILL.md): read, create, and review PDFs with rendering-aware checks.
- [xlsx](xlsx/SKILL.md): spreadsheet creation, editing, formulas, and analysis.
- [skill-creator](skill-creator/SKILL.md): create or update skills with stronger structure and tool integrations.

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) contains a vendored design-focused bundle from [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) at commit `0df1ba59dc80b8b1891ee42eed0ef4e03d7ef165`.

It includes:

- `frontend-design`: the flagship frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

Attribution and legal files are preserved in [`impeccable/NOTICE.md`](impeccable/NOTICE.md) and [`impeccable/LICENSE`](impeccable/LICENSE).

## Common Prerequisites

- Some skills assume `gh` is installed and authenticated.
- Browser-focused skills may require a Chrome/CDP-capable environment.
- Third-party doc lookup skills may depend on external CLIs or MCP tools; check each `SKILL.md` for details.

## Full Skill Index

### Top-Level Skills

| Skill | Description |
| --- | --- |
| [agent-browser](agent-browser/SKILL.md) | Browser automation CLI for AI agents: navigation, form filling, screenshots, extraction, and web testing. |
| [ai-elements](ai-elements/SKILL.md) | Create new AI chat interface components for the ai-elements library with composable patterns and shadcn/ui conventions. |
| [brainstorming](brainstorming/SKILL.md) | Clarify intent, requirements, and design before implementation work. |
| [ctx7-cli](ctx7-cli/SKILL.md) | Use the Context7 CLI for docs lookup, skill management, and MCP setup. |
| [design-taste-frontend](design-taste-frontend/SKILL.md) | Senior UI/UX engineering guidance for intentional, high-quality frontend design. |
| [dogfood](dogfood/SKILL.md) | Systematically test web apps and produce reproducible issue reports with screenshots and videos. |
| [electron](electron/SKILL.md) | Automate Electron desktop apps through agent-browser and Chrome DevTools Protocol. |
| [exa-search](exa-search/SKILL.md) | Use Exa for web, code, and company research. |
| [find-skills](find-skills/SKILL.md) | Discover existing skills when users need specialized capabilities. |
| [get-api-docs](get-api-docs/SKILL.md) | Fetch current third-party API or SDK docs before writing code. |
| [gh-address-comments](gh-address-comments/SKILL.md) | Address PR review and issue comments on the current branch with `gh`. |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | Inspect failing GitHub Actions checks, pull logs, and plan fixes. |
| [pdf](pdf/SKILL.md) | Read, create, and review PDF files with rendering checks and Python tooling. |
| [planning-with-files](planning-with-files/SKILL.md) | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`. |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Advanced prompt engineering patterns for reliable, production LLM workflows. |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | Best practices for building videos in React with Remotion. |
| [skill-creator](skill-creator/SKILL.md) | Guide for creating or updating skills with specialized knowledge and tool integrations. |
| [test-driven-development](test-driven-development/SKILL.md) | Use before implementing any feature or bugfix. |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidance from Vercel Engineering. |
| [xlsx](xlsx/SKILL.md) | Spreadsheet creation, editing, formulas, formatting, and analysis. |

### Vendored `impeccable/` Skills

| Skill | Description |
| --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | Create distinctive, production-grade frontend interfaces with high design quality. |
| [adapt](impeccable/adapt/SKILL.md) | Adapt designs across screen sizes, devices, and contexts. |
| [animate](impeccable/animate/SKILL.md) | Add purposeful motion and micro-interactions. |
| [audit](impeccable/audit/SKILL.md) | Audit interface quality across accessibility, performance, theming, and responsive design. |
| [bolder](impeccable/bolder/SKILL.md) | Make safe or boring designs more visually interesting. |
| [clarify](impeccable/clarify/SKILL.md) | Improve unclear UX copy and instructions. |
| [colorize](impeccable/colorize/SKILL.md) | Add strategic color to overly monochrome features. |
| [critique](impeccable/critique/SKILL.md) | Evaluate design effectiveness from a UX perspective. |
| [delight](impeccable/delight/SKILL.md) | Add personality and memorable moments to interfaces. |
| [distill](impeccable/distill/SKILL.md) | Strip designs down to their essential form. |
| [extract](impeccable/extract/SKILL.md) | Consolidate reusable components, tokens, and patterns into a design system. |
| [harden](impeccable/harden/SKILL.md) | Improve resilience around errors, i18n, overflow, and edge cases. |
| [normalize](impeccable/normalize/SKILL.md) | Normalize a feature to match a design system. |
| [onboard](impeccable/onboard/SKILL.md) | Design or improve onboarding and first-time user experience. |
| [optimize](impeccable/optimize/SKILL.md) | Improve frontend performance, rendering, motion, and bundle efficiency. |
| [polish](impeccable/polish/SKILL.md) | Final quality pass for alignment, spacing, consistency, and detail. |
| [quieter](impeccable/quieter/SKILL.md) | Reduce visual aggression while preserving design quality. |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | Gather design context and save it as persistent guidance for future work. |

## Contributing

Contributions are welcome for new skills or improvements to existing ones.

1. Keep trigger conditions explicit and testable.
2. Keep examples concise and execution-oriented.
3. If a skill depends on external tools, document that dependency in `SKILL.md`.
4. Update both `README.md` and `README.zh-CN.md` when you add or rename a skill.

## License

This repository is licensed under [LICENSE](LICENSE).

Some skills include additional license files or notices for skill-specific assets and attribution, including [`impeccable/`](impeccable/README.md), [`skill-creator/`](skill-creator/), and [`xlsx/`](xlsx/).
