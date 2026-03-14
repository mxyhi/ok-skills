# OK Skills: AI coding agent skills для Codex, Claude Code, Cursor, OpenClaw и других инструментов

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | Русский | [हिन्दी](README.hi.md)

Кураторская коллекция AI coding agent skills и playbook-файлов `AGENTS.md` для Codex, Claude Code, Cursor, OpenClaw, Trae и других инструментов, совместимых с `SKILL.md`.

Сейчас в этом репозитории собрано **41 переиспользуемых skills**: **23 skills верхнего уровня**, которые поддерживаются прямо здесь, и еще **18 vendored design skills** в каталоге [`impeccable/`](impeccable/README.md). Достаточно клонировать репозиторий в `~/.agents/skills/ok-skills`; внутренняя структура уже соответствует layout, который ожидают workflows на базе `AGENTS.md`.

Если вы ищете **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, переиспользуемые playbook-файлы **AGENTS.md** или практичные примеры **SKILL.md**, этот репозиторий специально оформлен так, чтобы его было легко найти и сразу использовать.

**Популярные сценарии:** поиск актуальной документации, автоматизация браузера, отладка GitHub Actions, prompt engineering, планирование сложных задач, frontend design и работа с PDF / Word / PPTX / XLSX.

## Для кого этот репозиторий

- Вы используете Codex, Claude Code, Cursor, OpenClaw, Trae или другого AI coding agent и хотите опираться на переиспользуемые skills, а не на одноразовые prompts.
- Вы поддерживаете workflows на базе `AGENTS.md` / `SKILL.md` и хотите переносимые инструкции, которые работают в разных проектах.
- Вам нужны проверенные skills для поиска документации, автоматизации браузера, GitHub workflow, planning, prompt engineering, frontend design, PDF, Office-документов, презентаций и таблиц.

## С чего начать

Если сначала хотите установить только несколько skills, начните с этих:

- [planning-with-files](planning-with-files/SKILL.md): file-based planning для сложных задач, исследований и долгих рабочих циклов.
- [context7-cli](context7-cli/SKILL.md): получение актуальной документации библиотек и reference-материалов на базе Context7.
- [agent-browser](agent-browser/SKILL.md): browser automation для скриншотов, форм, scraping и web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): анализ проваленных проверок GitHub Actions и превращение логов в plan исправления.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): production-oriented prompt patterns для более надежных LLM workflows.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): high-quality frontend design skill и полный пакет сопутствующих design-команд.

## Быстрый старт за 1 минуту

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

После клонирования репозиторий будет расположен в `~/.agents/skills/ok-skills`, а вложенные каталоги уже соответствуют ожидаемому layout:

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

Добавьте простые trigger rules в ваш `AGENTS.md`:

```md
## Skills
- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- context7-cli: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Дальше можно обращаться естественным языком:

- `Use planning-with-files before refactoring this module.`
- `Use context7-cli to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Навигация по skills по сценариям

### Research & Docs

- [context7-cli](context7-cli/SKILL.md): официальный workflow Context7 CLI для поиска документации, управления skills и настройки MCP.
- [exa-search](exa-search/SKILL.md): web, code и company research через инструменты Exa.
- [get-api-docs](get-api-docs/SKILL.md): получение актуальной документации сторонних API и SDK перед написанием кода.
- [find-skills](find-skills/SKILL.md): поиск существующих skills, когда пользователю нужна определенная capability.

### Planning & Prompting

- [brainstorming](brainstorming/SKILL.md): прояснение намерения, требований и дизайна перед реализацией.
- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning с `task_plan.md`, `findings.md` и `progress.md`.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): продвинутые prompt design patterns для production LLM systems.
- [test-driven-development](test-driven-development/SKILL.md): требование писать тесты до реализации.

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): обработка review- и issue-комментариев в текущем PR через `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): анализ проваленных проверок GitHub Actions, суммаризация логов и подготовка плана исправления.
- [yeet](yeet/SKILL.md): использовать только когда пользователь явно просит сделать stage, commit, push и открыть GitHub pull request одним `gh`-flow.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation для навигации, форм, скриншотов и scraping.
- [pinchtab](pinchtab/SKILL.md): управление Chrome через локальный HTTP API Pinchtab со стабильными accessibility refs.
- [electron](electron/SKILL.md): автоматизация Electron desktop apps через Chrome DevTools Protocol.
- [dogfood](dogfood/SKILL.md): структурированное exploratory testing с воспроизводимыми артефактами.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): создание AI chat UI components для библиотеки `ai-elements`.
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): guidance по React и Next.js performance от Vercel Engineering.
- [remotion-best-practices](remotion-best-practices/SKILL.md): guidance по Remotion для video work на React.
- [`impeccable/`](impeccable/README.md): 18 vendored frontend design skills, включая `frontend-design`, `adapt`, `audit`, `polish` и другие.

### Utilities & Authoring

- [docx](docx/SKILL.md): создание, чтение, редактирование и обработка Word-документов с formatting, comments и tracked changes.
- [pdf](pdf/SKILL.md): чтение, создание и проверка PDF с учетом рендеринга.
- [pptx](pptx/SKILL.md): создание, чтение, редактирование и обработка slide decks, templates и presentation content.
- [xlsx](xlsx/SKILL.md): создание и редактирование таблиц, formulas и analysis.
- [skill-creator](skill-creator/SKILL.md): создание или обновление skills с более сильной структурой и tool integrations.

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) содержит vendored design-focused bundle из [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) на коммите `0df1ba59dc80b8b1891ee42eed0ef4e03d7ef165`.

В него входят:

- `frontend-design`: флагманский frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

Файлы attribution и legal сохранены в [`impeccable/NOTICE.md`](impeccable/NOTICE.md) и [`impeccable/LICENSE`](impeccable/LICENSE).

## Общие предварительные требования

- Некоторые skills предполагают, что `gh` установлен и авторизован.
- Skills, связанные с браузером, могут требовать среды с поддержкой Chrome/CDP.
- Skills для поиска сторонней документации могут зависеть от внешних CLI или MCP tools; детали смотрите в соответствующих `SKILL.md`.

## Полный индекс skills

`Source URL` указывает на canonical upstream для vendored/imported skill; в остальных случаях он указывает на каталог skill внутри этого репозитория.

### Skills верхнего уровня

| Skill | Описание | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | Browser automation CLI for AI agents: navigation, form filling, screenshots, extraction, and web testing. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | Create new AI chat interface components for the ai-elements library with composable patterns and shadcn/ui conventions. | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [brainstorming](brainstorming/SKILL.md) | Clarify intent, requirements, and design before implementation work. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [context7-cli](context7-cli/SKILL.md) | Use the Context7 CLI for docs lookup, skill management, and MCP setup. | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | Create, read, edit, and manipulate Word documents with formatting, comments, tracked changes, and image updates. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | Systematically test web apps and produce reproducible issue reports with screenshots and videos. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | Automate Electron desktop apps through agent-browser and Chrome DevTools Protocol. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | Use Exa for web, code, and company research. | Custom |
| [find-skills](find-skills/SKILL.md) | Discover existing skills when users need specialized capabilities. | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | Fetch current third-party API or SDK docs before writing code. | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | Address PR review and issue comments on the current branch with `gh`. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | Inspect failing GitHub Actions checks, pull logs, and plan fixes. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [pdf](pdf/SKILL.md) | Read, create, and review PDF files with rendering checks and Python tooling. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | Control a headless or headed Chrome browser via Pinchtab's HTTP API for web automation, scraping, form filling, navigation, screenshots, and extraction with stable accessibility refs. | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skill/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`. | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.agent/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | Create, read, edit, and manipulate PowerPoint presentations, templates, layouts, notes, and slide content. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Advanced prompt engineering patterns for reliable, production LLM workflows. | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | Best practices for building videos in React with Remotion. | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | Guide for creating or updating skills with specialized knowledge and tool integrations. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [test-driven-development](test-driven-development/SKILL.md) | Use before implementing any feature or bugfix. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidance from Vercel Engineering. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | Spreadsheet creation, editing, formulas, formatting, and analysis. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using `gh`. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### Vendored `impeccable/` Skills

| Skill | Описание | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | Create distinctive, production-grade frontend interfaces with high design quality. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | Adapt designs across screen sizes, devices, and contexts. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | Add purposeful motion and micro-interactions. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | Audit interface quality across accessibility, performance, theming, and responsive design. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | Make safe or boring designs more visually interesting. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | Improve unclear UX copy and instructions. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | Add strategic color to overly monochrome features. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | Evaluate design effectiveness from a UX perspective. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | Add personality and memorable moments to interfaces. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | Strip designs down to their essential form. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | Consolidate reusable components, tokens, and patterns into a design system. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | Improve resilience around errors, i18n, overflow, and edge cases. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | Normalize a feature to match a design system. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | Design or improve onboarding and first-time user experience. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | Improve frontend performance, rendering, motion, and bundle efficiency. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | Final quality pass for alignment, spacing, consistency, and detail. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | Reduce visual aggression while preserving design quality. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | Gather design context and save it as persistent guidance for future work. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## Contributing

Приветствуются новые skills и улучшения существующих.

1. Делайте trigger conditions явными и проверяемыми.
2. Держите примеры краткими и ориентированными на выполнение.
3. Если skill зависит от внешних инструментов, документируйте эту зависимость в `SKILL.md`.
4. Обновляйте `README.md` и `README.zh-CN.md`, когда добавляете или переименовываете skill, и обновляйте остальные переведенные README, если меняется публичный skill index.

## License

Этот репозиторий распространяется по лицензии [LICENSE](LICENSE).

Некоторые skills содержат дополнительные license-файлы или notices для attribution, включая [`docx/`](docx/), [`pptx/`](pptx/), [`impeccable/`](impeccable/README.md), [`skill-creator/`](skill-creator/) и [`xlsx/`](xlsx/).
