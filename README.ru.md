# OK Skills: AI coding agent skills для Codex, Claude Code, Cursor, OpenClaw и других инструментов

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | Русский | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Кураторская коллекция AI coding agent skills и playbook-файлов `AGENTS.md` для Codex, Claude Code, Cursor, OpenClaw, Trae и других инструментов, совместимых с `SKILL.md`.

Сейчас в этом репозитории собрано **37 переиспользуемых skills**: **29 skills верхнего уровня**, которые поддерживаются прямо здесь, и **8 vendored GSAP animation skills** в каталоге [`gsap-skills/`](gsap-skills/). Достаточно клонировать репозиторий в `~/.agents/skills/ok-skills`; внутренняя структура уже соответствует layout, который ожидают workflows на базе `AGENTS.md`.

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
- [find-docs](find-docs/SKILL.md): получение актуальной документации библиотек, API reference и примеров на базе Context7.
- [agent-browser](agent-browser/SKILL.md): browser automation для скриншотов, форм, scraping и web QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): анализ проваленных проверок GitHub Actions и превращение логов в plan исправления.

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
  find-docs/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

Добавьте простые trigger rules в ваш `AGENTS.md`:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- find-docs: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Дальше можно обращаться естественным языком:

- `Use planning-with-files before refactoring this module.`
- `Use find-docs to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Навигация по skills по сценариям

### Research & Docs

- [find-docs](find-docs/SKILL.md): workflow Context7 CLI для поиска актуальной документации.
- [exa-search](exa-search/SKILL.md): web, code и company research через инструменты Exa.
- [get-api-docs](get-api-docs/SKILL.md): получение актуальной документации сторонних API и SDK перед написанием кода.
- [find-skills](find-skills/SKILL.md): поиск существующих skills, когда пользователю нужна определенная capability.

### Planning & Prompting

- [brainstorming](brainstorming/SKILL.md): прояснять идею, требования и дизайн до начала реализации.
- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning с `task_plan.md`, `findings.md` и `progress.md`.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): находить architecture deepening opportunities, улучшающие locality, leverage, testability и AI navigation.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): мигрировать `as` type assertions в тестах на `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): test-first red-green-refactor для функций, исправлений, рефакторинга и изменений поведения.
- [systematic-debugging](systematic-debugging/SKILL.md): системно искать корневую причину бага, падения теста или странного поведения до предложения фикса.

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): обработка review- и issue-комментариев в текущем PR через `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): анализ проваленных проверок GitHub Actions, суммаризация логов и подготовка плана исправления.
- [yeet](yeet/SKILL.md): использовать только когда пользователь явно просит сделать stage, commit, push и открыть GitHub pull request одним `gh`-flow.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation для навигации, форм, скриншотов и scraping.
- [browser-use](browser-use/SKILL.md): Постоянно работающий CLI для браузерной автоматизации: навигация, проверка состояния страницы, заполнение форм, скриншоты и извлечение данных.
- [browser-trace](browser-trace/SKILL.md): снимает CDP-трейсы, скриншоты и DOM-дампы для отладки браузерной автоматизации.
- [opencli](opencli/opencli-usage/SKILL.md): превращать сайты в CLI-команды за счет повторного использования браузерной сессии, public API и AI-generated adapters.

- [dogfood](dogfood/SKILL.md): структурированное exploratory testing с воспроизводимыми артефактами.
- [electron](electron/SKILL.md): автоматизация Electron desktop apps через Chrome DevTools Protocol.

`dogfood/` и `electron/` по-прежнему vendored из `vercel-labs/agent-browser`, но upstream в commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` переместил их из `skills/` в `skill-data/`, чтобы installer discovery показывал только bootstrap skill `agent-browser`. Этот репозиторий сохраняет эти specialized skills как top-level директории, потому что upstream продолжает их поддерживать и они по-прежнему полезны напрямую.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): создание AI chat UI components для библиотеки `ai-elements`.
- [frontend-skill](frontend-skill/SKILL.md): используйте, когда нужен визуально сильный лендинг, сайт, приложение, прототип, демо или игровой UI.
- [shader-dev](shader-dev/SKILL.md): полный набор техник GLSL для ShaderToy-совместимых визуальных эффектов в реальном времени.
- [better-icons](better-icons/SKILL.md): искать, просматривать и получать SVG-иконки из более чем 200 библиотек Iconify через CLI или MCP.
- [`gsap-skills/`](gsap-skills/): 8 official GSAP animation skills: core, timeline, ScrollTrigger, plugins, utils, React, performance, frameworks.

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): профессиональное создание, редактирование и форматирование DOCX на OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): создание, заполнение и переработка PDF-документов на базе токенизированной дизайн-системы.
- [pptx-generator](pptx-generator/SKILL.md): создание, редактирование и чтение презентаций PowerPoint через PptxGenJS, XML workflows и markitdown.
- [minimax-xlsx](minimax-xlsx/SKILL.md): открывать, создавать, читать, анализировать, редактировать и проверять Excel/табличные файлы с малопотерным XML workflow.

## Vendored Skill Packs

[`gsap-skills/`](gsap-skills/) содержит vendored GSAP animation bundle из [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) на коммите `aed9cfd3277740755f6bfc1155c7aa645403b760`.

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

[`planning-with-files/`](planning-with-files/) использует [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files) как upstream baseline. В этом репозитории сохранено общее имя `planning-with-files`, а Pi-specific package metadata удалены, чтобы skill оставался совместимым со стандартными `SKILL.md` workflows.

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
| [browser-trace](browser-trace/SKILL.md)                             | Снимает CDP-трейсы, скриншоты и DOM-дампы для отладки браузерной автоматизации.                                                                                      | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | Sverkhzhatyi rezhim obshcheniya, kotoryi sokrashchaet tokeny otveta stilem peshchernogo cheloveka bez poteri tekhnicheskoi tochnosti.                                                      | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [find-docs](find-docs/SKILL.md)                                     | Use the Context7 CLI for current documentation lookup, API references, and code examples.                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | Профессиональное создание, редактирование и форматирование DOCX на OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                                 | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Создавать визуально сильные лендинги, сайты, приложения, прототипы, демо или игровые UI.                                                                                                     | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Полный набор техник GLSL для ShaderToy-совместимых визуальных эффектов в реальном времени. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                               | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Address PR review and issue comments on the current branch with `gh`.                                                                                                                        | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspect failing GitHub Actions checks, pull logs, and plan fixes.                                                                                                                            | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Находит architecture deepening opportunities, улучшающие locality, leverage, testability и AI navigation.                                                                                       | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture)                              |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migrates test files from `as` type assertions to `@total-typescript/shoehorn`.                                                                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/migrate-to-shoehorn)                                        |
| [opensrc](opensrc/SKILL.md)                                         | Получать исходный код зависимостей, чтобы давать AI agents более глубокий контекст реализации.                                                                                               | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Превращает сайты в CLI-команды за счет повторного использования браузерной сессии, public API и AI-generated adapters.                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Systematically test web apps and produce reproducible issue reports with screenshots and videos.                                                                                             | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Automate Electron desktop apps through agent-browser and Chrome DevTools Protocol.                                                                                                           | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | Создание, заполнение и переработка PDF-документов на базе токенизированной дизайн-системы. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                                | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | Создание, редактирование и чтение презентаций PowerPoint через PptxGenJS, XML workflows и markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | Use before any feature, bugfix, refactor, or behavior change; prefers public-interface integration tests.                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Использовать при любом баге, падении теста или странном поведении до того, как предлагать фикс.                                            | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Открывать, создавать, читать, анализировать, редактировать и проверять Excel/табличные файлы с малопотерным XML workflow. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using `gh`.                                                                        | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

Примечания:
- `dogfood` и `electron` upstream-ом лежат в `skill-data/`, а не в `skills/`.
- Upstream переместил эти specialized skills в commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0`, чтобы installer discovery находил только bootstrap skill `agent-browser`.
- Этот репозиторий намеренно сохраняет их как vendored top-level skills, потому что upstream продолжает их поддерживать и они остаются напрямую полезными.

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

Некоторые skills содержат дополнительные license-файлы или notices для attribution, включая [`improve-codebase-architecture/`](improve-codebase-architecture/), [`migrate-to-shoehorn/`](migrate-to-shoehorn/), [`minimax-docx/`](minimax-docx/) и [`gsap-skills/`](gsap-skills/).
