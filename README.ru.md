# OK Skills: AI coding agent skills для Codex, Claude Code, Cursor, OpenClaw и других инструментов

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | Русский | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Кураторская коллекция AI coding agent skills и playbook-файлов `AGENTS.md` для Codex, Claude Code, Cursor, OpenClaw, Trae и других инструментов, совместимых с `SKILL.md`.

Сейчас в этом репозитории собрано **58 переиспользуемых skills**: **27 skills верхнего уровня**, которые поддерживаются прямо здесь, **5 vendored HyperFrames video skills** в каталоге [`hyperframes/`](hyperframes/README.md), **18 vendored design skills** в каталоге [`impeccable/`](impeccable/README.md) и **8 vendored GSAP animation skills** в каталоге [`gsap-skills/`](gsap-skills/). Достаточно клонировать репозиторий в `~/.agents/skills/ok-skills`; внутренняя структура уже соответствует layout, который ожидают workflows на базе `AGENTS.md`.

It includes:

- `hyperframes`
- `hyperframes-cli`
- `hyperframes-registry`
- `gsap`
- `website-to-hyperframes`

Attribution and legal files are preserved in [`hyperframes/LICENSE`](hyperframes/LICENSE).

[`impeccable/`](impeccable/README.md) и **8 vendored GSAP animation skills** в каталоге [`gsap-skills/`](gsap-skills/). Достаточно клонировать репозиторий в `~/.agents/skills/ok-skills`; внутренняя структура уже соответствует layout, который ожидают workflows на базе `AGENTS.md`.

Если вы ищете **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, переиспользуемые playbook-файлы **AGENTS.md** или практичные примеры **SKILL.md**, этот репозиторий специально оформлен так, чтобы его было легко найти и сразу использовать.

**Популярные сценарии:** поиск актуальной документации, автоматизация браузера, отладка GitHub Actions, prompt engineering, планирование сложных задач, frontend design и работа с PDF / Word / PPTX / XLSX.

## Для кого этот репозиторий

- Вы используете Codex, Claude Code, Cursor, OpenClaw, Trae или другого AI coding agent и хотите опираться на переиспользуемые skills, а не на одноразовые prompts.
- Вы поддерживаете workflows на базе `AGENTS.md` / `SKILL.md` и хотите переносимые инструкции, которые работают в разных проектах.
- Вам нужны проверенные skills для поиска документации, автоматизации браузера, GitHub workflow, planning, prompt engineering, frontend design, PDF, Office-документов, презентаций и таблиц.

## С чего начать

Если сначала хотите установить только несколько skills, начните с этих:

- [brainstorming](brainstorming/SKILL.md): прояснять идею, требования и дизайн до начала реализации.
- [planning-with-files](planning-with-files/SKILL.md): file-based planning для сложных задач, исследований и долгих рабочих циклов.
- [context7-cli](context7-cli/SKILL.md): получение актуальной документации библиотек и reference-материалов на базе Context7.
- [agent-browser](agent-browser/SKILL.md): browser automation для скриншотов, форм, scraping и web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): анализ проваленных проверок GitHub Actions и превращение логов в plan исправления.
- [impeccable](impeccable/impeccable/SKILL.md): core impeccable design skill и полный пакет сопутствующих design-команд.

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

- [brainstorming](brainstorming/SKILL.md): прояснять идею, требования и дизайн до начала реализации.
- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning с `task_plan.md`, `findings.md` и `progress.md`.
- [test-driven-development](test-driven-development/SKILL.md): требование писать тесты до реализации.

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): обработка review- и issue-комментариев в текущем PR через `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): анализ проваленных проверок GitHub Actions, суммаризация логов и подготовка плана исправления.
- [yeet](yeet/SKILL.md): использовать только когда пользователь явно просит сделать stage, commit, push и открыть GitHub pull request одним `gh`-flow.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation для навигации, форм, скриншотов и scraping.
- [browser-use](browser-use/SKILL.md): Постоянно работающий CLI для браузерной автоматизации: навигация, проверка состояния страницы, заполнение форм, скриншоты и извлечение данных.
- [opencli](opencli/opencli-usage/SKILL.md): превращать сайты в CLI-команды за счет повторного использования браузерной сессии, public API и AI-generated adapters.

- [dogfood](dogfood/SKILL.md): структурированное exploratory testing с воспроизводимыми артефактами.
- [electron](electron/SKILL.md): автоматизация Electron desktop apps через Chrome DevTools Protocol.

`dogfood/` и `electron/` по-прежнему vendored из `vercel-labs/agent-browser`, но upstream в commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` переместил их из `skills/` в `skill-data/`, чтобы installer discovery показывал только bootstrap skill `agent-browser`. Этот репозиторий сохраняет эти specialized skills как top-level директории, потому что upstream продолжает их поддерживать и они по-прежнему полезны напрямую.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): создание AI chat UI components для библиотеки `ai-elements`.
- [frontend-skill](frontend-skill/SKILL.md): используйте, когда нужен визуально сильный лендинг, сайт, приложение, прототип, демо или игровой UI.
- [shader-dev](shader-dev/SKILL.md): полный набор техник GLSL для ShaderToy-совместимых визуальных эффектов в реальном времени.
- [better-icons](better-icons/SKILL.md): искать, просматривать и получать SVG-иконки из более чем 200 библиотек Iconify через CLI или MCP.
- [remotion-best-practices](remotion-best-practices/SKILL.md): guidance по Remotion для video work на React.
- [`gsap-skills/`](gsap-skills/): 8 official GSAP animation skills: core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks.
- [`impeccable/`](impeccable/README.md): 18 vendored frontend design skills, включая `impeccable`, `adapt`, `audit`, `polish` и другие.

### Video & Motion

- [hyperframes](hyperframes/hyperframes/SKILL.md): create HTML-native video compositions, captions, TTS voiceovers, audio-reactive visuals, and scene transitions.
- [hyperframes-cli](hyperframes/hyperframes-cli/SKILL.md): scaffold, lint, preview, render, transcribe, and troubleshoot HyperFrames projects.
- [hyperframes-registry](hyperframes/hyperframes-registry/SKILL.md): install registry blocks and components, then wire them into compositions.
- [gsap](hyperframes/gsap/SKILL.md): HyperFrames-focused GSAP reference for timelines, easing, effects, and performance.
- [website-to-hyperframes](hyperframes/website-to-hyperframes/SKILL.md): capture a website and turn it into a scripted HyperFrames promo or product video.

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): профессиональное создание, редактирование и форматирование DOCX на OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): создание, заполнение и переработка PDF-документов на базе токенизированной дизайн-системы.
- [pptx-generator](pptx-generator/SKILL.md): создание, редактирование и чтение презентаций PowerPoint через PptxGenJS, XML workflows и markitdown.
- [minimax-xlsx](minimax-xlsx/SKILL.md): открывать, создавать, читать, анализировать, редактировать и проверять Excel/табличные файлы с малопотерным XML workflow.
- [skill-creator](skill-creator/SKILL.md): создание или обновление skills с более сильной структурой и tool integrations.

## Vendored Skill Packs

[`hyperframes/`](hyperframes/README.md) contains a video-focused bundle vendored from [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) at commit `42d39866ffb52c1c377f5f384b760f2de8519982`.

It includes:

- `hyperframes`
- `hyperframes-cli`
- `hyperframes-registry`
- `gsap`
- `website-to-hyperframes`

Attribution and legal files are preserved in [`hyperframes/LICENSE`](hyperframes/LICENSE).

[`impeccable/`](impeccable/README.md) содержит vendored design-focused bundle из [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) на коммите `00d485659af82982aef0328d0419c49a2716d123`.

В него входят:

- `impeccable`: флагманский frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `harden`, `layout`, `optimize`, `overdrive`, `polish`, `quieter`, `shape`, `typeset`

Файлы attribution и legal сохранены в [`impeccable/NOTICE.md`](impeccable/NOTICE.md) и [`impeccable/LICENSE`](impeccable/LICENSE).

[`gsap-skills/`](gsap-skills/) содержит vendored GSAP animation bundle из [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) на коммите `03d9f0c3dbf91e0b60582b64ed040c8911ca0174`.

В него входят:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

Файлы attribution и legal сохранены в [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) и [`gsap-skills/LICENSE`](gsap-skills/LICENSE).

## Общие предварительные требования

- Некоторые skills предполагают, что `gh` установлен и авторизован.
- Skills, связанные с браузером, могут требовать среды с поддержкой Chrome/CDP.
- Skills для поиска сторонней документации могут зависеть от внешних CLI или MCP tools; детали смотрите в соответствующих `SKILL.md`.

## Полный индекс skills

`Source URL` указывает на canonical upstream для vendored/imported skill; в остальных случаях он указывает на каталог skill внутри этого репозитория.

### Skills верхнего уровня

| Skill                                                               | Описание                                                                                                                                                                                     | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | Browser automation CLI for AI agents: navigation, form filling, screenshots, extraction, and web testing.                                                                                    | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | Create new AI chat interface components for the ai-elements library with composable patterns and shadcn/ui conventions.                                                                      | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons via CLI or MCP tools.                                                                                                                   | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | Превращает идеи в подтвержденные дизайн-решения и спецификации через совместный диалог до начала реализации.                                                                              | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | Постоянно работающий CLI для браузерной автоматизации: навигация, проверка состояния страницы, заполнение форм, скриншоты и извлечение данных.                                               | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | Sverkhzhatyi rezhim obshcheniya, kotoryi sokrashchaet tokeny otveta stilem peshchernogo cheloveka bez poteri tekhnicheskoi tochnosti.                                                      | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [context7-cli](context7-cli/SKILL.md)                               | Use the Context7 CLI for docs lookup, skill management, and MCP setup.                                                                                                                       | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | Профессиональное создание, редактирование и форматирование DOCX на OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                                 | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Создавать визуально сильные лендинги, сайты, приложения, прототипы, демо или игровые UI.                                                                                                     | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Полный набор техник GLSL для ShaderToy-совместимых визуальных эффектов в реальном времени. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                               | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Address PR review and issue comments on the current branch with `gh`.                                                                                                                        | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspect failing GitHub Actions checks, pull logs, and plan fixes.                                                                                                                            | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | Получать исходный код зависимостей, чтобы давать AI agents более глубокий контекст реализации.                                                                                               | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Превращает сайты в CLI-команды за счет повторного использования браузерной сессии, public API и AI-generated adapters.                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Systematically test web apps and produce reproducible issue reports with screenshots and videos.                                                                                             | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Automate Electron desktop apps through agent-browser and Chrome DevTools Protocol.                                                                                                           | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | Создание, заполнение и переработка PDF-документов на базе токенизированной дизайн-системы. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                                | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | Создание, редактирование и чтение презентаций PowerPoint через PptxGenJS, XML workflows и markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | Best practices for building videos in React with Remotion.                                                                                                                                   | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | Guide for creating or updating skills with specialized knowledge and tool integrations.                                                                                                      | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [test-driven-development](test-driven-development/SKILL.md)         | Use before implementing any feature or bugfix.                                                                                                                                               | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Открывать, создавать, читать, анализировать, редактировать и проверять Excel/табличные файлы с малопотерным XML workflow. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using `gh`.                                                                        | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

Примечания:
- `dogfood` и `electron` upstream-ом лежат в `skill-data/`, а не в `skills/`.
- Upstream переместил эти specialized skills в commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0`, чтобы installer discovery находил только bootstrap skill `agent-browser`.
- Этот репозиторий намеренно сохраняет их как vendored top-level skills, потому что upstream продолжает их поддерживать и они остаются напрямую полезными.

### Vendored `hyperframes/` Skills

| Skill | Description | Source URL |
| --- | --- | --- |
| [hyperframes](hyperframes/hyperframes/SKILL.md) | Create HTML-native video compositions, captions, TTS voiceovers, audio-reactive visuals, and transitions. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes) |
| [hyperframes-cli](hyperframes/hyperframes-cli/SKILL.md) | CLI workflow for HyperFrames: init, lint, preview, render, transcribe, TTS, and environment diagnosis. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-cli) |
| [hyperframes-registry](hyperframes/hyperframes-registry/SKILL.md) | Install registry blocks/components and wire them into HyperFrames compositions. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-registry) |
| [gsap](hyperframes/gsap/SKILL.md) | HyperFrames-focused GSAP reference for timelines, easing, effects, and performance. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/gsap) |
| [website-to-hyperframes](hyperframes/website-to-hyperframes/SKILL.md) | Capture a website and turn it into a HyperFrames video workflow with design, script, storyboard, voiceover, and build steps. | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes/tree/main/skills/website-to-hyperframes) |

### Vendored `impeccable/` Skills

| Skill                                                    | Описание                                                                                   | Source URL                                                  |
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
| [layout](impeccable/layout/SKILL.md)                       | Улучшает макет, интервалы и визуальный ритм.                                               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | Improve frontend performance, rendering, motion, and bundle efficiency.                    | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [overdrive](impeccable/overdrive/SKILL.md)                 | Выводит интерфейсы за привычные пределы за счет технически амбициозных реализаций.         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | Final quality pass for alignment, spacing, consistency, and detail.                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | Reduce visual aggression while preserving design quality.                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [shape](impeccable/shape/SKILL.md)                         | Планирует UX и UI функции до написания кода.                                               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [typeset](impeccable/typeset/SKILL.md)                     | Улучшает типографику, исправляя выбор шрифтов, иерархию, размеры, насыщенность и читаемость. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

### Vendored `gsap-skills/` Skills

| Skill                                                         | Описание                                                                              | Source URL                                                                                            |
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

Приветствуются новые skills и улучшения существующих.

1. Делайте trigger conditions явными и проверяемыми.
2. Держите примеры краткими и ориентированными на выполнение.
3. Если skill зависит от внешних инструментов, документируйте эту зависимость в `SKILL.md`.
4. Обновляйте `README.md` и `README.zh-CN.md`, когда добавляете или переименовываете skill, и обновляйте остальные переведенные README, если меняется публичный skill index.

## License

Этот репозиторий распространяется по лицензии [LICENSE](LICENSE).

Некоторые skills содержат дополнительные license-файлы или notices для attribution, включая [`minimax-docx/`](minimax-docx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), и [`skill-creator/`](skill-creator/).
