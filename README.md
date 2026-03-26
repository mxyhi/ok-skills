# OK Skills: AI Coding Agent Skills for Codex, Claude Code, Cursor, OpenClaw, and More

English | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

Curated AI coding agent skills and AGENTS.md playbooks for Codex, Claude Code, Cursor, OpenClaw, Trae, and other SKILL.md-compatible tools.

This repo currently bundles **55 reusable skills**: **29 top-level skills** maintained directly in this repo, plus **18 vendored design skills** under [`impeccable/`](impeccable/README.md), plus **8 vendored GSAP animation skills** under [`gsap-skills/`](gsap-skills/). Clone it into `~/.agents/skills/ok-skills`; the directories inside already match the layout expected by `AGENTS.md`-driven workflows.

If you are looking for **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **AGENTS.md** playbooks, or practical **SKILL.md** examples, this repository is designed to be both searchable and immediately usable.

**Popular use cases:** docs lookup, browser automation, GitHub Actions debugging, prompt engineering, planning workflows, frontend design, PDF/Word/PPTX/XLSX authoring.

## Who This Repo Is For

- You use Codex, Claude Code, Cursor, OpenClaw, Trae, or another AI coding agent and want reusable skills instead of ad-hoc prompts.
- You maintain `AGENTS.md` / `SKILL.md` workflows and want portable instructions that work across projects.
- You need battle-tested skills for docs lookup, browser automation, GitHub workflow, planning, prompt engineering, frontend design, PDFs, Office documents, slide decks, and spreadsheets.

## Start Here

If you only install a few skills first, start with these:

- [planning-with-files](planning-with-files/SKILL.md): file-based planning for complex tasks, research, and long-running work.
- [context7-cli](context7-cli/SKILL.md): fetch current library docs and Context7-backed references.
- [agent-browser](agent-browser/SKILL.md): browser automation for screenshots, forms, scraping, and web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspect failing GitHub Actions checks and turn logs into a fix plan.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): production-oriented prompt patterns for more reliable LLM workflows.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): high-quality frontend design skill plus a full bundle of companion design commands.

## 1-Minute Quick Start

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

After cloning, the repo lives at `~/.agents/skills/ok-skills`, and the directories inside already follow the expected layout:

```text
~/.agents/skills/ok-skills/
  planning-with-files/
    SKILL.md
  context7-cli/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

Add simple trigger rules to your `AGENTS.md`:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- context7-cli: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Then ask naturally:

- `Use planning-with-files before refactoring this module.`
- `Use context7-cli to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Browse Skills by Use Case

### Research & Docs

- [context7-cli](context7-cli/SKILL.md): official Context7 CLI workflow for docs lookup, skill management, and MCP setup.
- [exa-search](exa-search/SKILL.md): web, code, and company research with Exa search tools.
- [get-api-docs](get-api-docs/SKILL.md): fetch current third-party API and SDK documentation before coding.
- [find-skills](find-skills/SKILL.md): discover existing skills when a user asks for a capability.

### Planning & Prompting

- [brainstorming](brainstorming/SKILL.md): clarify intent, requirements, and design before implementation.
- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning with `task_plan.md`, `findings.md`, and `progress.md`.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): advanced prompt design patterns for production LLM systems.
- [subagent-driven-development](subagent-driven-development/SKILL.md): execute implementation plans with independent tasks in the current session using fresh subagents and staged reviews.
- [test-driven-development](test-driven-development/SKILL.md): enforce writing tests before implementation work.

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): address review and issue comments on the current PR with `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspect failing GitHub Actions checks, summarize logs, and plan fixes.
- [yeet](yeet/SKILL.md): use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one `gh`-driven flow.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation for navigation, forms, screenshots, and scraping.
- [browser-use](browser-use/SKILL.md): persistent browser automation CLI for navigation, state inspection, form filling, screenshots, and extraction.
- [bb-browser](bb-browser/SKILL.md): information retrieval and browser automation through the user's real browser and logged-in session.
- [pinchtab](pinchtab/SKILL.md): control Chrome through Pinchtab's local HTTP API using stable accessibility refs.
- [electron](electron/SKILL.md): automate Electron desktop apps over Chrome DevTools Protocol.
- [opencli](opencli/SKILL.md): turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.
- [dogfood](dogfood/SKILL.md): structured exploratory testing with reproducible evidence.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): build AI chat UI components for the `ai-elements` library.
- [frontend-skill](frontend-skill/SKILL.md): use when you need a visually strong landing page, website, app, prototype, demo, or game UI.
- [better-icons](better-icons/SKILL.md): search, browse, and retrieve SVG icons from 200+ Iconify libraries via CLI or MCP.
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): React and Next.js performance guidance from Vercel Engineering.
- [remotion-best-practices](remotion-best-practices/SKILL.md): Remotion guidance for React-based video work.
- [`gsap-skills/`](gsap-skills/): 8 official GSAP animation skills: core, timelines, ScrollTrigger, plugins, utils, React, performance, frameworks.
- [`impeccable/`](impeccable/README.md): 18 vendored frontend design skills, including `frontend-design`, `adapt`, `audit`, `polish`, and more.

### Utilities & Authoring

- [docx](docx/SKILL.md): create, read, edit, and manipulate Word documents with formatting, comments, and tracked changes.
- [pdf](pdf/SKILL.md): read, create, and review PDFs with rendering-aware checks.
- [pptx](pptx/SKILL.md): create, read, edit, and manipulate slide decks, templates, and presentation content.
- [xlsx](xlsx/SKILL.md): spreadsheet creation, editing, formulas, and analysis.
- [skill-creator](skill-creator/SKILL.md): create or update skills with stronger structure and tool integrations.

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) contains a vendored design-focused bundle from [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) at commit `9d368b777d222e213c9a8f4fa78f6f1d29cb492d`.

It includes:

- `frontend-design`: the flagship frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

Attribution and legal files are preserved in [`impeccable/NOTICE.md`](impeccable/NOTICE.md) and [`impeccable/LICENSE`](impeccable/LICENSE).

[`gsap-skills/`](gsap-skills/) contains an animation-focused bundle vendored from [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) at commit `4300e310513b0ddc0b121a5c0e0bd2e5c2325ff2`.

It includes:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

Attribution and legal files are preserved in [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) and [`gsap-skills/LICENSE`](gsap-skills/LICENSE).

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
| [bb-browser](bb-browser/SKILL.md)                                   | Information retrieval and browser automation through the user's real browser and logged-in session, covering public pages, internal systems, and logged-in workflows.                   | [epiral/bb-browser](https://github.com/epiral/bb-browser/tree/main/skills/bb-browser)                                          |
| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons through CLI or MCP tools.                                                                                                          | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                             | Clarify intent, requirements, and design before implementation work.                                                                                                                    | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                         |
| [browser-use](browser-use/SKILL.md)                                 | Persistent browser automation CLI for navigation, state inspection, form filling, screenshots, and extraction.                                                                          | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [context7-cli](context7-cli/SKILL.md)                               | Use the Context7 CLI for docs lookup, skill management, and MCP setup.                                                                                                                  | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [docx](docx/SKILL.md)                                               | Create, read, edit, and manipulate Word documents with formatting, comments, tracked changes, and image updates.                                                                        | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx)                                                |
| [dogfood](dogfood/SKILL.md)                                         | Systematically test web apps and produce reproducible issue reports with screenshots and videos.                                                                                        | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood)                             |
| [electron](electron/SKILL.md)                                       | Automate Electron desktop apps through agent-browser and Chrome DevTools Protocol.                                                                                                      | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron)                            |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                      | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Build visually strong landing pages, websites, apps, prototypes, demos, or game UIs.                                                                                                    | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                          | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Address PR review and issue comments on the current branch with `gh`.                                                                                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspect failing GitHub Actions checks, pull logs, and plan fixes.                                                                                                                       | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opencli](opencli/SKILL.md)                                         | Turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.                                                                               | [jackwener/opencli](https://github.com/jackwener/opencli)                                                                      |
| [pdf](pdf/SKILL.md)                                                 | Read, create, and review PDF files with rendering checks and Python tooling.                                                                                                            | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf)                                                |
| [pinchtab](pinchtab/SKILL.md)                                       | Control a headless or headed Chrome browser via Pinchtab's HTTP API for web automation, scraping, form filling, navigation, screenshots, and extraction with stable accessibility refs. | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skills/pinchtab)                                            |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                           | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx](pptx/SKILL.md)                                               | Create, read, edit, and manipulate PowerPoint presentations, templates, layouts, notes, and slide content.                                                                              | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx)                                                |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Advanced prompt engineering patterns for reliable, production LLM workflows.                                                                                                            | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | Best practices for building videos in React with Remotion.                                                                                                                              | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | Guide for creating or updating skills with specialized knowledge and tool integrations.                                                                                                 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [subagent-driven-development](subagent-driven-development/SKILL.md) | Execute implementation plans with independent tasks in the current session using fresh subagents and staged reviews.                                                                    | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development)                           |
| [test-driven-development](test-driven-development/SKILL.md)         | Use before implementing any feature or bugfix.                                                                                                                                          | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidance from Vercel Engineering.                                                                                                            | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)                  |
| [xlsx](xlsx/SKILL.md)                                               | Spreadsheet creation, editing, formulas, formatting, and analysis.                                                                                                                      | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx)                                                |
| [yeet](yeet/SKILL.md)                                               | Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using `gh`.                                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

### Vendored `impeccable/` Skills

| Skill                                                    | Description                                                                                | Source URL                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| [frontend-design](impeccable/frontend-design/SKILL.md)   | Create distinctive, production-grade frontend interfaces with high design quality.         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md)                       | Adapt designs across screen sizes, devices, and contexts.                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md)                   | Add purposeful motion and micro-interactions.                                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md)                       | Audit interface quality across accessibility, performance, theming, and responsive design. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md)                     | Make safe or boring designs more visually interesting.                                     | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md)                   | Improve unclear UX copy and instructions.                                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md)                 | Add strategic color to overly monochrome features.                                         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md)                 | Evaluate design effectiveness from a UX perspective.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md)                   | Add personality and memorable moments to interfaces.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md)                   | Strip designs down to their essential form.                                                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md)                   | Consolidate reusable components, tokens, and patterns into a design system.                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md)                     | Improve resilience around errors, i18n, overflow, and edge cases.                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md)               | Normalize a feature to match a design system.                                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md)                   | Design or improve onboarding and first-time user experience.                               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | Improve frontend performance, rendering, motion, and bundle efficiency.                    | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | Final quality pass for alignment, spacing, consistency, and detail.                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | Reduce visual aggression while preserving design quality.                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | Gather design context and save it as persistent guidance for future work.                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

### Vendored `gsap-skills/` Skills

| Skill                                                         | Description                                                                           | Source URL                                                                                            |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | Core API: gsap.to()/from()/fromTo(), easing, duration, stagger, defaults, matchMedia. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timelines: sequencing, position parameter, labels, nesting, playback.                 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: scroll-linked animation, pinning, scrub, triggers, refresh, cleanup.   | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | Plugins: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase, and more.           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils helpers: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe.    | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React: useGSAP, refs, gsap.context(), cleanup, SSR.                                   | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | Performance tips: transforms, will-change, batching, ScrollTrigger tips.              | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue, Svelte, and other frameworks: lifecycle, scoping selectors, cleanup on unmount.  | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## Contributing

Contributions are welcome for new skills or improvements to existing ones.

1. Keep trigger conditions explicit and testable.
2. Keep examples concise and execution-oriented.
3. If a skill depends on external tools, document that dependency in `SKILL.md`.
4. Update `README.md` and `README.zh-CN.md` when you add or rename a skill, and refresh the other translated READMEs when the public-facing skill index changes.

## License

This repository is licensed under [LICENSE](LICENSE).

Some skills include additional license files or notices for skill-specific assets and attribution, including [`docx/`](docx/), [`pptx/`](pptx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), [`skill-creator/`](skill-creator/), and [`xlsx/`](xlsx/).
