# OK Skills: AI Coding Agent Skills for Codex, Claude Code, Cursor, OpenClaw, and More

English | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Curated AI coding agent skills and AGENTS.md playbooks for Codex, Claude Code, Cursor, OpenClaw, Trae, and other SKILL.md-compatible tools.

This repo currently bundles **58 reusable skills**: **27 top-level skills** maintained directly in this repo, plus **5 vendored HyperFrames video skills** under [`hyperframes/`](hyperframes/README.md), plus **18 vendored design skills** under [`impeccable/`](impeccable/README.md), plus **8 vendored GSAP animation skills** under [`gsap-skills/`](gsap-skills/). Clone it into `~/.agents/skills/ok-skills`; the directories inside already match the layout expected by `AGENTS.md`-driven workflows.

If you are looking for **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **AGENTS.md** playbooks, or practical **SKILL.md** examples, this repository is designed to be both searchable and immediately usable.

**Popular use cases:** docs lookup, browser automation, GitHub Actions debugging, prompt engineering, planning workflows, frontend design, PDF/Word/PPTX/XLSX authoring.

## Who This Repo Is For

- You use Codex, Claude Code, Cursor, OpenClaw, Trae, or another AI coding agent and want reusable skills instead of ad-hoc prompts.
- You maintain `AGENTS.md` / `SKILL.md` workflows and want portable instructions that work across projects.
- You need battle-tested skills for docs lookup, browser automation, GitHub workflow, planning, prompt engineering, frontend design, PDFs, Office documents, slide decks, and spreadsheets.

## Start Here

If you only install a few skills first, start with these:

- [brainstorming](brainstorming/SKILL.md): explore ideas, requirements, and design before implementation begins.
- [planning-with-files](planning-with-files/SKILL.md): file-based planning for complex tasks, research, and long-running work.
- [context7-cli](context7-cli/SKILL.md): fetch current library docs and Context7-backed references.
- [agent-browser](agent-browser/SKILL.md): browser automation for screenshots, forms, scraping, and web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspect failing GitHub Actions checks and turn logs into a fix plan.
- [impeccable](impeccable/impeccable/SKILL.md): core impeccable design skill plus a full bundle of companion design commands.

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

- [brainstorming](brainstorming/SKILL.md): explore ideas, requirements, and design before implementation begins.
- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning with `task_plan.md`, `findings.md`, and `progress.md`.
- [test-driven-development](test-driven-development/SKILL.md): enforce writing tests before implementation work.

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): address review and issue comments on the current PR with `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspect failing GitHub Actions checks, summarize logs, and plan fixes.
- [yeet](yeet/SKILL.md): use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one `gh`-driven flow.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation for navigation, forms, screenshots, and scraping.
- [browser-use](browser-use/SKILL.md): persistent browser automation CLI for navigation, state inspection, form filling, screenshots, and extraction.
- [opencli](opencli/opencli-usage/SKILL.md): turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.
- [dogfood](dogfood/SKILL.md): structured exploratory testing with reproducible evidence.
- [electron](electron/SKILL.md): automate Electron desktop apps over Chrome DevTools Protocol.

`dogfood/` and `electron/` are still vendored from `vercel-labs/agent-browser`, but upstream moved them from `skills/` to `skill-data/` in commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` so installer discovery only exposes the bootstrap `agent-browser` skill. This repo keeps those specialized skills as top-level directories because they are still maintained upstream and remain directly usable.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): build AI chat UI components for the `ai-elements` library.
- [frontend-skill](frontend-skill/SKILL.md): use when you need a visually strong landing page, website, app, prototype, demo, or game UI.
- [shader-dev](shader-dev/SKILL.md): comprehensive GLSL shader techniques for ShaderToy-compatible real-time visual effects.
- [better-icons](better-icons/SKILL.md): search, browse, and retrieve SVG icons from 200+ Iconify libraries via CLI or MCP.
- [remotion-best-practices](remotion-best-practices/SKILL.md): Remotion guidance for React-based video work.
- [`gsap-skills/`](gsap-skills/): 8 official GSAP animation skills: core, timelines, ScrollTrigger, plugins, utils, React, performance, frameworks.
- [`impeccable/`](impeccable/README.md): 18 vendored frontend design skills, including `impeccable`, `adapt`, `audit`, `polish`, and more.

### Video & Motion

- [hyperframes](hyperframes/hyperframes/SKILL.md): create HTML-native video compositions, captions, TTS voiceovers, audio-reactive visuals, and scene transitions.
- [hyperframes-cli](hyperframes/hyperframes-cli/SKILL.md): scaffold, lint, preview, render, transcribe, and troubleshoot HyperFrames projects.
- [hyperframes-registry](hyperframes/hyperframes-registry/SKILL.md): install registry blocks and components, then wire them into compositions.
- [gsap](hyperframes/gsap/SKILL.md): HyperFrames-focused GSAP reference for timelines, easing, effects, and performance.
- [website-to-hyperframes](hyperframes/website-to-hyperframes/SKILL.md): capture a website and turn it into a scripted HyperFrames promo or product video.

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): professional DOCX creation, editing, and formatting with OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): generate, fill, and reformat PDFs with a token-based design system.
- [pptx-generator](pptx-generator/SKILL.md): generate, edit, and read PowerPoint presentations with PptxGenJS, XML workflows, or markitdown.
- [minimax-xlsx](minimax-xlsx/SKILL.md): open, create, read, analyze, edit, and validate Excel or spreadsheet files with low-loss XML workflows.
- [skill-creator](skill-creator/SKILL.md): create or update skills with stronger structure and tool integrations.

## Vendored Skill Packs

[`hyperframes/`](hyperframes/README.md) contains a video-focused bundle vendored from [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) at commit `42d39866ffb52c1c377f5f384b760f2de8519982`.

It includes:

- `hyperframes`
- `hyperframes-cli`
- `hyperframes-registry`
- `gsap`
- `website-to-hyperframes`

Attribution and legal files are preserved in [`hyperframes/LICENSE`](hyperframes/LICENSE).

[`impeccable/`](impeccable/README.md) contains a vendored design-focused bundle from [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) at commit `00d485659af82982aef0328d0419c49a2716d123`.

It includes:

- `impeccable`: the flagship frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `harden`, `layout`, `optimize`, `overdrive`, `polish`, `quieter`, `shape`, `typeset`

Attribution and legal files are preserved in [`impeccable/NOTICE.md`](impeccable/NOTICE.md) and [`impeccable/LICENSE`](impeccable/LICENSE).

[`gsap-skills/`](gsap-skills/) contains an animation-focused bundle vendored from [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) at commit `03d9f0c3dbf91e0b60582b64ed040c8911ca0174`.

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
| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons through CLI or MCP tools.                                                                                                          | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | Turn ideas into validated designs and specs through collaborative dialogue before implementation.                                                                                         | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | Persistent browser automation CLI for navigation, state inspection, form filling, screenshots, and extraction.                                                                          | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | Ultra-compressed communication mode that cuts response tokens by speaking like caveman while keeping technical accuracy.                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [context7-cli](context7-cli/SKILL.md)                               | Use the Context7 CLI for docs lookup, skill management, and MCP setup.                                                                                                                  | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | Professional DOCX document creation, editing, and formatting using OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                      | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Build visually strong landing pages, websites, apps, prototypes, demos, or game UIs.                                                                                                    | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Comprehensive GLSL shader techniques for ShaderToy-compatible real-time visual effects. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                          | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Address PR review and issue comments on the current branch with `gh`.                                                                                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspect failing GitHub Actions checks, pull logs, and plan fixes.                                                                                                                       | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | Fetch dependency source code to give AI agents deeper implementation context.                                                                                                           | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Turn websites into CLI commands with browser session reuse, public API access, and AI-generated adapters.                                                                               | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Systematically test web apps and produce reproducible issue reports with screenshots and videos.                                                                                        | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Automate Electron desktop apps through agent-browser and Chrome DevTools Protocol.                                                                                                      | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | Generate, fill, and reformat PDF documents with a token-based design system. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                           | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | Generate, edit, and read PowerPoint presentations with PptxGenJS, XML workflows, or markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | Best practices for building videos in React with Remotion.                                                                                                                              | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | Guide for creating or updating skills with specialized knowledge and tool integrations.                                                                                                 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [test-driven-development](test-driven-development/SKILL.md)         | Use before implementing any feature or bugfix.                                                                                                                                          | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Open, create, read, analyze, edit, and validate Excel or spreadsheet files with low-loss XML workflows. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using `gh`.                                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

Notes:
- `dogfood` and `electron` come from upstream `skill-data/`, not upstream `skills/`.
- Upstream moved these specialized skills in commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` so installer discovery only finds the bootstrap `agent-browser` skill.
- This repository intentionally keeps them as top-level vendored skills because they are still maintained upstream and remain directly useful.

### Vendored `hyperframes/` Skills

| Skill | Description | Source URL |
| --- | --- | --- |
| [hyperframes](hyperframes/hyperframes/SKILL.md) | Create HTML-native video compositions, captions, TTS voiceovers, audio-reactive visuals, and transitions. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes) |
| [hyperframes-cli](hyperframes/hyperframes-cli/SKILL.md) | CLI workflow for HyperFrames: init, lint, preview, render, transcribe, TTS, and environment diagnosis. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-cli) |
| [hyperframes-registry](hyperframes/hyperframes-registry/SKILL.md) | Install registry blocks/components and wire them into HyperFrames compositions. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-registry) |
| [gsap](hyperframes/gsap/SKILL.md) | HyperFrames-focused GSAP reference for timelines, easing, effects, and performance. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/gsap) |
| [website-to-hyperframes](hyperframes/website-to-hyperframes/SKILL.md) | Capture a website and turn it into a HyperFrames video workflow with design, script, storyboard, voiceover, and build steps. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/website-to-hyperframes) |

### Vendored `impeccable/` Skills

| Skill                                                    | Description                                                                                | Source URL                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| [impeccable](impeccable/impeccable/SKILL.md)   | Create distinctive, production-grade frontend interfaces with high design quality.         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md)                       | Adapt designs across screen sizes, devices, and contexts.                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md)                   | Add purposeful motion and micro-interactions.                                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md)                       | Audit interface quality across accessibility, performance, theming, and responsive design. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md)                     | Make safe or boring designs more visually interesting.                                     | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md)                   | Improve unclear UX copy and instructions.                                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md)                 | Add strategic color to overly monochrome features.                                         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md)                 | Evaluate design effectiveness from a UX perspective.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md)                   | Add personality and memorable moments to interfaces.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md)                   | Strip designs down to their essential form.                                                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md)                     | Improve resilience around errors, i18n, overflow, and edge cases.                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [layout](impeccable/layout/SKILL.md)                       | Improve layout, spacing, and visual rhythm.                                                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | Improve frontend performance, rendering, motion, and bundle efficiency.                    | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [overdrive](impeccable/overdrive/SKILL.md)                 | Push interfaces past conventional limits with technically ambitious implementations.       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | Final quality pass for alignment, spacing, consistency, and detail.                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | Reduce visual aggression while preserving design quality.                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [shape](impeccable/shape/SKILL.md)                         | Plan the UX and UI for a feature before writing code.                                      | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [typeset](impeccable/typeset/SKILL.md)                     | Improve typography by fixing font choices, hierarchy, sizing, weight, and readability.     | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

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

Some skills include additional license files or notices for skill-specific assets and attribution, including [`caveman/`](caveman/), [`minimax-docx/`](minimax-docx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), and [`skill-creator/`](skill-creator/).
