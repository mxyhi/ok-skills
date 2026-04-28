# OK Skills: AI Coding Agent Skills für Codex, Claude Code, Cursor, OpenClaw und mehr

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Deutsch | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Kuratiertes Repository für AI Coding Agent Skills und `AGENTS.md`-Playbooks für Codex, Claude Code, Cursor, OpenClaw, Trae und andere Tools, die mit `SKILL.md`-Workflows kompatibel sind.

Dieses Repository bündelt aktuell **36 wiederverwendbare Skills**: **28 Top-Level-Skills**, die direkt hier gepflegt werden, plus **8 vendorte GSAP-Animations-Skills** unter [`gsap-skills/`](gsap-skills/). Klone es nach `~/.agents/skills/ok-skills`; die enthaltenen Verzeichnisse entsprechen bereits dem Layout, das `AGENTS.md`-gesteuerte Workflows erwarten.

Wenn du nach **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, wiederverwendbaren **AGENTS.md**-Playbooks oder praxistauglichen **SKILL.md**-Beispielen suchst, ist dieses Repository bewusst auf Auffindbarkeit und sofortige Nutzbarkeit ausgelegt.

**Häufige Einsatzfälle:** aktuelle Dokumentation nachschlagen, Browser-Automatisierung, GitHub-Actions-Debugging, Prompt Engineering, Planung komplexer Aufgaben, Frontend-Design sowie PDF / Word / PPTX / XLSX Authoring.

## Für wen dieses Repository gedacht ist

- Du nutzt Codex, Claude Code, Cursor, OpenClaw, Trae oder einen anderen AI Coding Agent und möchtest wiederverwendbare Skills statt ad-hoc Prompts.
- Du pflegst Workflows auf Basis von `AGENTS.md` und `SKILL.md` und willst portable Anleitungen, die projektübergreifend funktionieren.
- Du brauchst erprobte Skills für Dokumentationsrecherche, Browser-Automatisierung, GitHub-Workflows, Planung, Prompt Engineering, Frontend-Design, PDFs, Office-Dokumente, Foliensätze und Tabellen.

## Einstieg

Wenn du zuerst nur wenige Skills installieren willst, beginne mit diesen:

- [brainstorming](brainstorming/SKILL.md): Ideen, Anforderungen und Design klären, bevor die Implementierung beginnt.
- [planning-with-files](planning-with-files/SKILL.md): dateibasierte Planung für komplexe Aufgaben, Recherche und länger laufende Arbeit.
- [find-docs](find-docs/SKILL.md): aktuelle Bibliotheksdokumentation, API-Referenzen und Context7-Beispiele abrufen.
- [agent-browser](agent-browser/SKILL.md): Browser-Automatisierung für Screenshots, Formulare, Scraping und Web-QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): fehlgeschlagene GitHub-Actions-Checks untersuchen und aus Logs einen Fixplan ableiten.

## 1-Minuten-Schnellstart

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Nach dem Klonen liegt das Repository unter `~/.agents/skills/ok-skills`, und die enthaltenen Verzeichnisse entsprechen bereits dem erwarteten Layout:

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

Füge deinem `AGENTS.md` einfache Trigger-Regeln hinzu:

```md
## Skills

- planning-with-files: Für komplexe Aufgaben, Recherche oder alles verwenden, was mehr als 5 Tool-Aufrufe benötigt.
- find-docs: Verwenden, wenn aktuelle Bibliotheksdokumentation, API-Referenzen oder Context7-Beispiele benötigt werden.
- agent-browser: Für Browser-Automatisierung, Screenshots, Scraping, Web-Tests oder Formularausfüllung verwenden.
```

Danach kannst du natürlich formulieren:

- `Use planning-with-files before refactoring this module.`
- `Use find-docs to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Skills nach Anwendungsfall durchsuchen

### Recherche und Dokumentation

- [find-docs](find-docs/SKILL.md): fokussierter Context7-CLI-Workflow für aktuelle Dokumentationssuche.
- [exa-search](exa-search/SKILL.md): Web-, Code- und Unternehmensrecherche mit Exa-Suchwerkzeugen.
- [get-api-docs](get-api-docs/SKILL.md): aktuelle Third-Party-API- und SDK-Dokumentation vor dem Coden abrufen.
- [find-skills](find-skills/SKILL.md): vorhandene Skills finden, wenn ein Benutzer nach einer Fähigkeit fragt.

### Planung und Prompting

- [brainstorming](brainstorming/SKILL.md): Ideen, Anforderungen und Design klären, bevor die Implementierung beginnt.
- [planning-with-files](planning-with-files/SKILL.md): persistente Markdown-Planung mit `task_plan.md`, `findings.md` und `progress.md`.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): Architektur-Deepening-Chancen finden, die Locality, Leverage, Testbarkeit und AI-Navigation verbessern.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): `as`-Type-Assertions in Tests nach `@total-typescript/shoehorn` migrieren.
- [tdd](tdd/SKILL.md): test-first red-green-refactor fur Features, Bugfixes, Refactorings und Verhaltensaenderungen.
- [systematic-debugging](systematic-debugging/SKILL.md): Bei Bugs, Testfehlern oder unerwartetem Verhalten die Ursache systematisch untersuchen, bevor Fixes vorgeschlagen werden.

### GitHub-Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): Review- und Issue-Kommentare im aktuellen PR mit `gh` bearbeiten.
- [gh-fix-ci](gh-fix-ci/SKILL.md): fehlgeschlagene GitHub-Actions-Checks untersuchen, Logs zusammenfassen und Fixes planen.
- [yeet](yeet/SKILL.md): nur verwenden, wenn der Benutzer explizit darum bittet, Stage, Commit, Push und das Öffnen eines GitHub-PR in einem einzigen `gh`-basierten Ablauf zu erledigen.

### Automatisierung und QA

- [agent-browser](agent-browser/SKILL.md): Browser-Automatisierung für Navigation, Formulare, Screenshots und Scraping.
- [browser-use](browser-use/SKILL.md): Persistente Browser-Automatisierungs-CLI für Navigation, Statusprüfung, Formularausfüllung, Screenshots und Extraktion.
- [opencli](opencli/opencli-usage/SKILL.md): Websites mit wiederverwendeter Browser-Session, Public APIs und KI-generierten Adaptern als CLI nutzen.
- [dogfood](dogfood/SKILL.md): strukturierte explorative Tests mit reproduzierbaren Belegen.
- [electron](electron/SKILL.md): Electron-Desktop-Apps über das Chrome DevTools Protocol automatisieren.

`dogfood/` und `electron/` werden weiterhin aus `vercel-labs/agent-browser` vendort, aber upstream hat sie in Commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` von `skills/` nach `skill-data/` verschoben, damit die Installer-Erkennung nur das Bootstrap-Skill `agent-browser` findet. Dieses Repo behält diese spezialisierten Skills als Top-Level-Verzeichnisse, weil sie upstream weiterhin gepflegt werden und direkt nutzbar bleiben.


### Frontend und Design

- [ai-elements](ai-elements/SKILL.md): AI-Chat-UI-Komponenten für die Bibliothek `ai-elements` erstellen.
- [frontend-skill](frontend-skill/SKILL.md): Verwenden, wenn eine visuell starke Landingpage, Website, App, ein Prototyp, eine Demo oder ein Game-UI benötigt wird.
- [shader-dev](shader-dev/SKILL.md): Umfassende GLSL-Shader-Techniken für ShaderToy-kompatible Echtzeit-Visuals.
- [better-icons](better-icons/SKILL.md): SVG-Icons aus mehr als 200 Iconify-Bibliotheken per CLI oder MCP suchen, durchsuchen und abrufen.
- [`gsap-skills/`](gsap-skills/): 8 offizielle GSAP-Animations-Skills (Core, Timelines, ScrollTrigger, Plugins, Utils, React, Performance, Frameworks).

### Utilities und Content-Erstellung

- [minimax-docx](minimax-docx/SKILL.md): Professionelle DOCX-Erstellung, Bearbeitung und Formatierung mit OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): PDF-Dokumente mit einem tokenbasierten Designsystem erzeugen, ausfüllen und neu formatieren.
- [pptx-generator](pptx-generator/SKILL.md): PowerPoint-Präsentationen mit PptxGenJS, XML-Workflows oder markitdown erzeugen, bearbeiten und lesen.
- [minimax-xlsx](minimax-xlsx/SKILL.md): Excel-/Spreadsheet-Dateien mit verlustarmem XML-Workflow öffnen, erstellen, analysieren, bearbeiten und validieren.

## Vendorte Skill-Pakete

[`gsap-skills/`](gsap-skills/) enthält ein animationsfokussiertes Bundle, vendort aus [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) auf Basis des Commits `aed9cfd3277740755f6bfc1155c7aa645403b760`.

Enthalten sind:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

Attributionen und rechtliche Dateien bleiben in [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) und [`gsap-skills/LICENSE`](gsap-skills/LICENSE) erhalten.

[`planning-with-files/`](planning-with-files/) verwendet [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files) als Upstream-Basis. Dieses Repository behält den generischen Namen `planning-with-files` und entfernt Pi-spezifische Paketmetadaten, damit der Skill mit standardmäßigen `SKILL.md`-Workflows kompatibel bleibt.

## Häufige Voraussetzungen

- Einige Skills setzen voraus, dass `gh` installiert und authentifiziert ist.
- Browser-orientierte Skills können eine Chrome/CDP-fähige Umgebung erfordern.
- Skills für Dokumentationsrecherche können von externen CLIs oder MCP-Tools abhängen; Details stehen jeweils in `SKILL.md`.

## Vollständiger Skill-Index

`Source URL` verweist auf das kanonische Upstream, wenn ein Skill vendort oder importiert wurde; andernfalls zeigt sie auf das Skill-Verzeichnis in diesem Repository.

### Top-Level-Skills

| Skill                                                               | Beschreibung                                                                                                                                                                                                       | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | Browser-Automatisierungs-CLI für AI Agents: Navigation, Formularausfüllung, Screenshots, Extraktion und Web-Tests.                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | Neue AI-Chat-Oberflächenkomponenten für die ai-elements-Bibliothek mit komponierbaren Mustern und shadcn/ui-Konventionen erstellen.                                                                                | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | Durchsuche über 200 Iconify-Bibliotheken und hole SVG-Icons per CLI oder MCP-Tools.                                                                                                                                | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | Ideen vor der Implementierung in einem kollaborativen Dialog zu validierten Designs und Spezifikationen ausarbeiten.                                                                      | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | Persistente Browser-Automatisierungs-CLI für Navigation, Statusprüfung, Formularausfüllung, Screenshots und Extraktion.                                                                                            | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | Ultrasparsamer Kommunikationsmodus, der Antwort-Tokens im Hoehlenmenschenstil reduziert, ohne technische Genauigkeit zu verlieren.                                                         | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [find-docs](find-docs/SKILL.md)                                     | Die Context7 CLI für aktuelle Dokumentation, API-Referenzen und Codebeispiele verwenden.                                                                                                                          | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | Professionelle DOCX-Erstellung, Bearbeitung und Formatierung mit OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Exa für Web-, Code- und Unternehmensrecherche verwenden.                                                                                                                                                           | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Vorhandene Skills entdecken, wenn Benutzer spezialisierte Fähigkeiten benötigen.                                                                                                                                   | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Visuell starke Landingpages, Websites, Apps, Prototypen, Demos oder Game-UIs erstellen.                                                                                                                            | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Umfassende GLSL-Shader-Techniken für ShaderToy-kompatible Echtzeit-Visuals. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Aktuelle Dokumentation zu APIs oder SDKs von Drittanbietern abrufen, bevor Code geschrieben wird.                                                                                                                  | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | PR-Review- und Issue-Kommentare im aktuellen Branch mit `gh` bearbeiten.                                                                                                                                           | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Fehlgeschlagene GitHub-Actions-Checks untersuchen, Logs abrufen und Fixes planen.                                                                                                                                  | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Architektur-Deepening-Chancen finden, die Locality, Leverage, Testbarkeit und AI-Navigation verbessern.                                                                                                           | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture)                              |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Testdateien von `as`-Type-Assertions zu `@total-typescript/shoehorn` migrieren.                                                                                                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/migrate-to-shoehorn)                                        |
| [opensrc](opensrc/SKILL.md)                                         | Abhängige Quelltexte abrufen, um AI-Agents tieferen Implementierungskontext zu geben.                                                                                                                              | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Websites mit wiederverwendeter Browser-Session, Public APIs und KI-generierten Adaptern in CLI-Befehle verwandeln.                                                                                                 | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Web-Apps systematisch testen und reproduzierbare Fehlerberichte mit Screenshots und Videos erstellen.                                                                                                              | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Electron-Desktop-Apps über agent-browser und das Chrome DevTools Protocol automatisieren.                                                                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | PDF-Dokumente mit einem tokenbasierten Designsystem erzeugen, ausfüllen und neu formatieren. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | Dateibasierte Planung für komplexe Aufgaben mit `task_plan.md`, `findings.md` und `progress.md`.                                                                                                                   | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | PowerPoint-Präsentationen mit PptxGenJS, XML-Workflows oder markitdown erzeugen, bearbeiten und lesen. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | Vor Features, Bugfixes, Refactorings oder Verhaltensaenderungen verwenden; bevorzugt Integrationstests ueber public interfaces.                                                                                    | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Verwenden, wenn ein Bug, Testfehler oder unerwartetes Verhalten auftritt, bevor Fixes vorgeschlagen werden.                                                                              | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Excel-/Spreadsheet-Dateien mit verlustarmem XML-Workflow öffnen, erstellen, analysieren, bearbeiten und validieren. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Nur verwenden, wenn der Benutzer explizit verlangt, Staging, Commit, Push und das Öffnen eines GitHub-PR in einem Ablauf mit `gh` zu erledigen.                                                                    | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

Hinweise:
- `dogfood` und `electron` kommen upstream aus `skill-data/`, nicht aus `skills/`.
- Upstream hat diese spezialisierten Skills in Commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` verschoben, damit die Installer-Erkennung nur das Bootstrap-Skill `agent-browser` findet.
- Dieses Repository behält sie bewusst als vendorte Top-Level-Skills, weil sie upstream weiter gepflegt werden und direkt nützlich bleiben.

### Vendorte `gsap-skills/`-Skills

| Skill                                                         | Beschreibung                                                                             | Source URL                                                                                            |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | Core API: gsap.to()/from()/fromTo(), Easing, Duration, Stagger, Defaults, MatchMedia.    | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timelines: Sequencing, Position Parameter, Labels, Nesting, Playback.                    | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: Scroll-gebundene Animationen, Pinning, Scrub, Triggers, Refresh, Cleanup. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | Plugins: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase u.v.m.                  | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils Helpers: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe.       | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React: useGSAP, Refs, gsap.context(), Cleanup, SSR.                                      | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | Performance: Transforms, will-change, Batching, ScrollTrigger Tips.                      | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue, Svelte u.a.: Lifecycle, Selector-Scoping, Cleanup beim Unmount.                     | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## Mitwirken

Beiträge für neue Skills oder Verbesserungen an bestehenden Skills sind willkommen.

1. Halte Trigger-Bedingungen explizit und testbar.
2. Halte Beispiele knapp und ausführungsorientiert.
3. Wenn ein Skill von externen Tools abhängt, dokumentiere diese Abhängigkeit in `SKILL.md`.
4. Aktualisiere `README.md` und `README.zh-CN.md`, wenn du einen Skill hinzufügst oder umbenennst, und aktualisiere die übrigen übersetzten READMEs, sobald sich der öffentliche Skill-Index ändert.

## Lizenz

Dieses Repository steht unter der Lizenz aus [LICENSE](LICENSE).

Einige Skills enthalten zusätzliche Lizenzdateien oder Hinweise zu skill-spezifischen Assets und Attributionen, darunter [`improve-codebase-architecture/`](improve-codebase-architecture/), [`migrate-to-shoehorn/`](migrate-to-shoehorn/), [`minimax-docx/`](minimax-docx/) und [`gsap-skills/`](gsap-skills/).
