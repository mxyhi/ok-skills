# OK Skills: AI coding agent skills для Codex, Claude Code, Cursor, OpenClaw и других инструментов

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | Русский | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Кураторская коллекция AI coding agent skills и playbook-файлов `CLAUDE.md` / `AGENTS.md` для Codex, Claude Code, Cursor, OpenClaw, Trae и других инструментов, совместимых с `SKILL.md`.

Сейчас в этом репозитории собрано **15 переиспользуемых skills**, все они поддерживаются прямо здесь как каталоги skills верхнего уровня. Достаточно клонировать репозиторий в `~/.agents/skills/ok-skills`; внутренняя структура уже соответствует layout, который ожидают workflows на базе `AGENTS.md`, а [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) содержит agent playbook для Claude Code.

Если вы ищете **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, переиспользуемые playbook-файлы **CLAUDE.md / AGENTS.md** или практичные примеры **SKILL.md**, этот репозиторий специально оформлен так, чтобы его было легко найти и сразу использовать.


## Для кого этот репозиторий

- Вы используете Codex, Claude Code, Cursor, OpenClaw, Trae или другого AI coding agent и хотите опираться на переиспользуемые skills, а не на одноразовые prompts.
- Вы поддерживаете workflows на базе `CLAUDE.md` / `AGENTS.md` / `SKILL.md` и хотите переносимые инструкции, которые работают в разных проектах.

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
- [find-skills](find-skills/SKILL.md): поиск существующих skills, когда пользователю нужна определенная capability.

### Planning & Prompting

- [planning-with-files](planning-with-files/SKILL.md): persistent markdown planning с `task_plan.md`, `findings.md` и `progress.md`.
- [autoresearch](autoresearch/SKILL.md): автономная goal-directed iteration с явными целями, метриками, verify loops и keep/discard gates.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): disciplined diagnosis loop для сложных bugs и performance regressions.
- [grilling](grilling/SKILL.md): reusable one-question-at-a-time interview loop для прямых grill sessions.
- [teach](teach/SKILL.md): вести stateful teaching workspace с mission, resources, lessons и learning records.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): coding guidelines, снижающие overcomplication, скрытые assumptions и неверифицируемые изменения.
- [tdd](tdd/SKILL.md): test-first red-green-refactor для функций, исправлений, рефакторинга и изменений поведения.

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): browser automation для навигации, форм, скриншотов и scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): Управляет реальным браузером пользователя через локальный daemon для навигации, форм, скриншотов, чтения страниц и авторизованных сессий.

### Frontend & Design

- [better-icons](better-icons/SKILL.md): искать, просматривать и получать SVG-иконки из более чем 200 библиотек Iconify через CLI или MCP.

### Utilities & Authoring


## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) использует [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) как upstream baseline. В этом репозитории этот upstream-каталог используется как canonical baseline для локального skill. Локальные отличия ограничены совместимым со `skills-ref` frontmatter в `SKILL.md` и не зависящими от места установки относительными путями к scripts в документации.

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
| [autoresearch](autoresearch/SKILL.md)                               | Автономный goal-directed iteration engine для workflows modify, verify, keep/discard и repeat.                                                                                         | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | Search 200+ Iconify libraries and retrieve SVG icons via CLI or MCP tools.                                                                                                                   | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Управляет реальным браузером пользователя через локальный daemon для навигации, форм, скриншотов, чтения страниц и авторизованных сессий.                                                    | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [caveman](caveman/SKILL.md)                                         | Sverkhzhatyi rezhim obshcheniya, kotoryi sokrashchaet tokeny otveta stilem peshchernogo cheloveka bez poteri tekhnicheskoi tochnosti.                                                      | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Disciplined diagnosis loop для сложных bugs и performance regressions.                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | Use the Context7 CLI for current documentation lookup, API references, and code examples.                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | Use Exa for web, code, and company research.                                                                                                                                                 | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Discover existing skills when users need specialized capabilities.                                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [grilling](grilling/SKILL.md)                               | Reusable one-question-at-a-time interview loop для прямых grill sessions.                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | Обучает skill или concept внутри workspace с mission, resources, lessons и learning records. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Coding guidelines, снижающие overcomplication, скрытые assumptions и неверифицируемые изменения.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [planning-with-files](planning-with-files/SKILL.md)                 | File-based planning for complex tasks using `task_plan.md`, `findings.md`, and `progress.md`.                                                                                                | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [tdd](tdd/SKILL.md)                                                 | Use before any feature, bugfix, refactor, or behavior change; prefers public-interface integration tests.                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## Contributing

Приветствуются новые skills и улучшения существующих.

1. Делайте trigger conditions явными и проверяемыми.
2. Держите примеры краткими и ориентированными на выполнение.
3. Если skill зависит от внешних инструментов, документируйте эту зависимость в `SKILL.md`.
4. Обновляйте `README.md` и `README.zh-CN.md`, когда добавляете или переименовываете skill, и обновляйте остальные переведенные README, если меняется публичный skill index.

## License

Этот репозиторий распространяется по лицензии [LICENSE](LICENSE).
