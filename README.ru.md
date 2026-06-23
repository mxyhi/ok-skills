# OK Skills: AI coding agent skills для Codex, Claude Code, Cursor, OpenClaw и других инструментов

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | Русский | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Кураторская коллекция AI coding agent skills и playbook-файлов `CLAUDE.md` / `AGENTS.md` для Codex, Claude Code, Cursor, OpenClaw, Trae и других инструментов, совместимых с `SKILL.md`.

Сейчас в этом репозитории собрано **30 переиспользуемых skills**, все они поддерживаются прямо здесь как каталоги skills верхнего уровня. Достаточно клонировать репозиторий в `~/.agents/skills/ok-skills`; внутренняя структура уже соответствует layout, который ожидают workflows на базе `AGENTS.md`, а [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) содержит agent playbook для Claude Code.

Если вы ищете **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, переиспользуемые playbook-файлы **CLAUDE.md / AGENTS.md** или практичные примеры **SKILL.md**, этот репозиторий специально оформлен так, чтобы его было легко найти и сразу использовать.

**Популярные сценарии:** поиск актуальной документации, автоматизация браузера, prompt engineering, планирование сложных задач, frontend design и работа с PDF / Word / PPTX / XLSX.

## Для кого этот репозиторий

- Вы используете Codex, Claude Code, Cursor, OpenClaw, Trae или другого AI coding agent и хотите опираться на переиспользуемые skills, а не на одноразовые prompts.
- Вы поддерживаете workflows на базе `CLAUDE.md` / `AGENTS.md` / `SKILL.md` и хотите переносимые инструкции, которые работают в разных проектах.
- Вам нужны проверенные skills для поиска документации, автоматизации браузера, planning, prompt engineering, frontend design, PDF, Office-документов, презентаций и таблиц.

## С чего начать

Если сначала хотите установить только несколько skills, начните с этих:

- [planning-with-files](planning-with-files/SKILL.md): file-based planning для сложных задач, исследований и долгих рабочих циклов.
- [find-docs](find-docs/SKILL.md): получение актуальной документации библиотек, API reference и примеров на базе Context7.
- [agent-browser](agent-browser/SKILL.md): browser automation для скриншотов, форм, scraping и web QA.

## Быстрый старт за 1 минуту

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

После клонирования репозиторий будет расположен в `~/.agents/skills/ok-skills`, а вложенные каталоги уже соответствуют ожидаемому layout:

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

Для глобальных инструкций Claude Code или Codex начните с [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md), затем скопируйте или объедините его с `CLAUDE.md` для Claude Code или `AGENTS.md` для Codex. Он включает Chinese-first и KISS-ориентированный workflow, проверки актуальной документации/source, предпочтение multi-agent, включенные по умолчанию `caveman` / `planning-with-files` / `karpathy-guidelines`, строгие ожидания к TypeScript и правила маршрутизации context-mode. Перед повторным использованием отредактируйте раздел `语言要求` под ваш проект. Раздел `其他注意项` намеренно является проектно-локальным и может редактироваться по мере необходимости.

Добавьте простые trigger rules в ваш `AGENTS.md` или перенесите те же skill triggers в `CLAUDE.md` / `AGENTS.md`:

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

- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning с `task_plan.md`, `findings.md` и `progress.md`.
- [autoresearch](autoresearch/SKILL.md): автономная goal-directed iteration с явными целями, метриками, verify loops и keep/discard gates.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): disciplined diagnosis loop для сложных bugs и performance regressions.
- [grill-me](grill-me/SKILL.md): stress-test плана или design через вопросы по одному до общего понимания.
- [grill-with-docs](grill-with-docs/SKILL.md): проверяет план против domain language, `CONTEXT.md` и ADRs, обновляя docs inline.
- [grilling](grilling/SKILL.md): reusable one-question-at-a-time interview loop behind `grill-me` and `grill-with-docs`.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): находить architecture deepening opportunities, улучшающие locality, leverage, testability и AI navigation.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): coding guidelines, снижающие overcomplication, скрытые assumptions и неверифицируемые изменения.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): мигрировать `as` type assertions в тестах на `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): test-first red-green-refactor для функций, исправлений, рефакторинга и изменений поведения.
- [systematic-debugging](systematic-debugging/SKILL.md): системно искать корневую причину бага, падения теста или странного поведения до предложения фикса.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation для навигации, форм, скриншотов и scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): Управляет реальным браузером пользователя через локальный daemon для навигации, форм, скриншотов, чтения страниц и авторизованных сессий.
- [browser-trace](browser-trace/SKILL.md): снимает CDP-трейсы, скриншоты и DOM-дампы для отладки браузерной автоматизации.
- [opencli](opencli/opencli-usage/SKILL.md): превращать сайты в CLI-команды за счет повторного использования браузерной сессии, public API и AI-generated adapters.
- [xquik-twitter](xquik-twitter/SKILL.md): искать данные X/Twitter и выполнять подтвержденные действия аккаунта через Xquik API.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): создание AI chat UI components для библиотеки `ai-elements`.
- [huashu-design](huashu-design/SKILL.md): создавать high-fidelity HTML prototypes, interactive demos, slide decks, motion design, design variants, video exports и design critique.
- [better-icons](better-icons/SKILL.md): искать, просматривать и получать SVG-иконки из более чем 200 библиотек Iconify через CLI или MCP.

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): профессиональное создание, редактирование и форматирование DOCX на OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): создание, заполнение и переработка PDF-документов на базе токенизированной дизайн-системы.
- [pptx-generator](pptx-generator/SKILL.md): создание, редактирование и чтение презентаций PowerPoint через PptxGenJS, XML workflows и markitdown.
- [huashu-design](huashu-design/SKILL.md): делать HTML decks, editable PPTX, MP4/GIF motion pieces и narrated design videos.
- [minimax-xlsx](minimax-xlsx/SKILL.md): открывать, создавать, читать, анализировать, редактировать и проверять Excel/табличные файлы с малопотерным XML workflow.

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) использует [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files) как upstream baseline. В этом репозитории этот upstream-каталог используется как canonical baseline для локального skill. Локальные отличия ограничены сохранением публичного имени `planning-with-files` и нормализацией frontmatter в `SKILL.md` для совместимости с `skills-ref`.

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
| [autoresearch](autoresearch/SKILL.md)                               | Автономный goal-directed iteration engine для workflows modify, verify, keep/discard и repeat.                                                                                         | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons via CLI or MCP tools.                                                                                                                   | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Управляет реальным браузером пользователя через локальный daemon для навигации, форм, скриншотов, чтения страниц и авторизованных сессий.                                                    | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | Снимает CDP-трейсы, скриншоты и DOM-дампы для отладки браузерной автоматизации.                                                                                      | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | Sverkhzhatyi rezhim obshcheniya, kotoryi sokrashchaet tokeny otveta stilem peshchernogo cheloveka bez poteri tekhnicheskoi tochnosti.                                                      | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Disciplined diagnosis loop для сложных bugs и performance regressions.                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | Use the Context7 CLI for current documentation lookup, API references, and code examples.                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | Профессиональное создание, редактирование и форматирование DOCX на OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                                 | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | Создавать high-fidelity HTML prototypes, interactive demos, slide decks, motion design, design variants, video exports и design critique.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | Fetch current third-party API or SDK docs before writing code.                                                                                                                               | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grill-me](grill-me/SKILL.md)                                 | Relentless interview по plan или design до общего понимания.                                                                                        | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)                                |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | Stress-test plan против domain language, `CONTEXT.md` и ADRs с inline обновлением docs.                                                             | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [grilling](grilling/SKILL.md)                               | Reusable one-question-at-a-time interview loop behind `grill-me` and `grill-with-docs`.                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Находит architecture deepening opportunities, улучшающие locality, leverage, testability и AI navigation.                                                                                       | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Coding guidelines, снижающие overcomplication, скрытые assumptions и неверифицируемые изменения.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migrates test files from `as` type assertions to `@total-typescript/shoehorn`.                                                                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Превращает сайты в CLI-команды за счет повторного использования браузерной сессии, public API и AI-generated adapters.                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [xquik-twitter](xquik-twitter/SKILL.md)                         | Искать данные X/Twitter и выполнять подтвержденные действия аккаунта через Xquik API.                                                                                                      | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)             |
| [minimax-pdf](minimax-pdf/SKILL.md) | Создание, заполнение и переработка PDF-документов на базе токенизированной дизайн-системы. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                                | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | Создание, редактирование и чтение презентаций PowerPoint через PptxGenJS, XML workflows и markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | Use before any feature, bugfix, refactor, or behavior change; prefers public-interface integration tests.                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Использовать при любом баге, падении теста или странном поведении до того, как предлагать фикс.                                            | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Открывать, создавать, читать, анализировать, редактировать и проверять Excel/табличные файлы с малопотерным XML workflow. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
## Contributing

Приветствуются новые skills и улучшения существующих.

1. Делайте trigger conditions явными и проверяемыми.
2. Держите примеры краткими и ориентированными на выполнение.
3. Если skill зависит от внешних инструментов, документируйте эту зависимость в `SKILL.md`.
4. Обновляйте `README.md` и `README.zh-CN.md`, когда добавляете или переименовываете skill, и обновляйте остальные переведенные README, если меняется публичный skill index.

## License

Этот репозиторий распространяется по лицензии [LICENSE](LICENSE).
