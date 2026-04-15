# OK Skills: AI Coding Agent Skills für Codex, Claude Code, Cursor, OpenClaw und mehr

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Deutsch | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Kuratiertes Repository für AI Coding Agent Skills und `AGENTS.md`-Playbooks für Codex, Claude Code, Cursor, OpenClaw, Trae und andere Tools, die mit `SKILL.md`-Workflows kompatibel sind.

Dieses Repository bündelt aktuell **53 wiederverwendbare Skills**: **27 Top-Level-Skills**, die direkt hier gepflegt werden, plus **18 vendorte Design-Skills** unter [`impeccable/`](impeccable/README.md), plus **8 vendorte GSAP-Animations-Skills** unter [`gsap-skills/`](gsap-skills/). Klone es nach `~/.agents/skills/ok-skills`; die enthaltenen Verzeichnisse entsprechen bereits dem Layout, das `AGENTS.md`-gesteuerte Workflows erwarten.

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
- [context7-cli](context7-cli/SKILL.md): aktuelle Bibliotheksdokumentation und Context7-basierte Referenzen abrufen.
- [agent-browser](agent-browser/SKILL.md): Browser-Automatisierung für Screenshots, Formulare, Scraping und Web-QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): fehlgeschlagene GitHub-Actions-Checks untersuchen und aus Logs einen Fixplan ableiten.
- [impeccable](impeccable/impeccable/SKILL.md): zentraler impeccable Design-Skill plus ein vollstandiges Bundle erganzender Design-Kommandos.

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
  context7-cli/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

Füge deinem `AGENTS.md` einfache Trigger-Regeln hinzu:

```md
## Skills

- planning-with-files: Für komplexe Aufgaben, Recherche oder alles verwenden, was mehr als 5 Tool-Aufrufe benötigt.
- context7-cli: Verwenden, wenn aktuelle Bibliotheksdokumentation, API-Referenzen oder Context7-Beispiele benötigt werden.
- agent-browser: Für Browser-Automatisierung, Screenshots, Scraping, Web-Tests oder Formularausfüllung verwenden.
```

Danach kannst du natürlich formulieren:

- `Use planning-with-files before refactoring this module.`
- `Use context7-cli to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Skills nach Anwendungsfall durchsuchen

### Recherche und Dokumentation

- [context7-cli](context7-cli/SKILL.md): offizieller Context7-CLI-Workflow für Dokumentationssuche, Skill-Management und MCP-Einrichtung.
- [exa-search](exa-search/SKILL.md): Web-, Code- und Unternehmensrecherche mit Exa-Suchwerkzeugen.
- [get-api-docs](get-api-docs/SKILL.md): aktuelle Third-Party-API- und SDK-Dokumentation vor dem Coden abrufen.
- [find-skills](find-skills/SKILL.md): vorhandene Skills finden, wenn ein Benutzer nach einer Fähigkeit fragt.

### Planung und Prompting

- [brainstorming](brainstorming/SKILL.md): Ideen, Anforderungen und Design klären, bevor die Implementierung beginnt.
- [planning-with-files](planning-with-files/SKILL.md): persistente Markdown-Planung mit `task_plan.md`, `findings.md` und `progress.md`.
- [test-driven-development](test-driven-development/SKILL.md): Tests vor der Implementierungsarbeit durchsetzen.

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
- [remotion-best-practices](remotion-best-practices/SKILL.md): Remotion-Leitfaden für videobasierte Arbeit mit React.
- [`gsap-skills/`](gsap-skills/): 8 offizielle GSAP-Animations-Skills (Core, Timelines, ScrollTrigger, Plugins, Utils, React, Performance, Frameworks).
- [`impeccable/`](impeccable/README.md): 18 vendorte Frontend-Design-Skills, darunter `impeccable`, `adapt`, `audit`, `polish` und mehr.

### Utilities und Content-Erstellung

- [minimax-docx](minimax-docx/SKILL.md): Professionelle DOCX-Erstellung, Bearbeitung und Formatierung mit OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): PDF-Dokumente mit einem tokenbasierten Designsystem erzeugen, ausfüllen und neu formatieren.
- [pptx-generator](pptx-generator/SKILL.md): PowerPoint-Präsentationen mit PptxGenJS, XML-Workflows oder markitdown erzeugen, bearbeiten und lesen.
- [minimax-xlsx](minimax-xlsx/SKILL.md): Excel-/Spreadsheet-Dateien mit verlustarmem XML-Workflow öffnen, erstellen, analysieren, bearbeiten und validieren.
- [skill-creator](skill-creator/SKILL.md): Skills mit stärkerer Struktur und besseren Tool-Integrationen erstellen oder aktualisieren.

## Vendorte Skill-Pakete

[`impeccable/`](impeccable/README.md) enthält ein vendortes, designfokussiertes Bundle aus [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) auf Basis des Commits `00d485659af82982aef0328d0419c49a2716d123`.

Enthalten sind:

- `impeccable`: der zentrale Frontend-Design-Skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `harden`, `layout`, `optimize`, `overdrive`, `polish`, `quieter`, `shape`, `typeset`

Attributionen und rechtliche Dateien bleiben in [`impeccable/NOTICE.md`](impeccable/NOTICE.md) und [`impeccable/LICENSE`](impeccable/LICENSE) erhalten.

[`gsap-skills/`](gsap-skills/) enthält ein animationsfokussiertes Bundle, vendort aus [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) auf Basis des Commits `03d9f0c3dbf91e0b60582b64ed040c8911ca0174`.

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
| [context7-cli](context7-cli/SKILL.md)                               | Die Context7 CLI für Dokumentationssuche, Skill-Management und MCP-Setup verwenden.                                                                                                                                | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | Professionelle DOCX-Erstellung, Bearbeitung und Formatierung mit OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Exa für Web-, Code- und Unternehmensrecherche verwenden.                                                                                                                                                           | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Vorhandene Skills entdecken, wenn Benutzer spezialisierte Fähigkeiten benötigen.                                                                                                                                   | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Visuell starke Landingpages, Websites, Apps, Prototypen, Demos oder Game-UIs erstellen.                                                                                                                            | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Umfassende GLSL-Shader-Techniken für ShaderToy-kompatible Echtzeit-Visuals. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Aktuelle Dokumentation zu APIs oder SDKs von Drittanbietern abrufen, bevor Code geschrieben wird.                                                                                                                  | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | PR-Review- und Issue-Kommentare im aktuellen Branch mit `gh` bearbeiten.                                                                                                                                           | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Fehlgeschlagene GitHub-Actions-Checks untersuchen, Logs abrufen und Fixes planen.                                                                                                                                  | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | Abhängige Quelltexte abrufen, um AI-Agents tieferen Implementierungskontext zu geben.                                                                                                                              | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Websites mit wiederverwendeter Browser-Session, Public APIs und KI-generierten Adaptern in CLI-Befehle verwandeln.                                                                                                 | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Web-Apps systematisch testen und reproduzierbare Fehlerberichte mit Screenshots und Videos erstellen.                                                                                                              | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Electron-Desktop-Apps über agent-browser und das Chrome DevTools Protocol automatisieren.                                                                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | PDF-Dokumente mit einem tokenbasierten Designsystem erzeugen, ausfüllen und neu formatieren. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | Dateibasierte Planung für komplexe Aufgaben mit `task_plan.md`, `findings.md` und `progress.md`.                                                                                                                   | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | PowerPoint-Präsentationen mit PptxGenJS, XML-Workflows oder markitdown erzeugen, bearbeiten und lesen. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | Best Practices für das Erstellen von Videos in React mit Remotion.                                                                                                                                                 | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | Leitfaden zum Erstellen oder Aktualisieren von Skills mit spezialisiertem Wissen und Tool-Integrationen.                                                                                                           | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [test-driven-development](test-driven-development/SKILL.md)         | Vor jeder neuen Funktion oder Fehlerbehebung verwenden.                                                                                                                                                            | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Excel-/Spreadsheet-Dateien mit verlustarmem XML-Workflow öffnen, erstellen, analysieren, bearbeiten und validieren. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Nur verwenden, wenn der Benutzer explizit verlangt, Staging, Commit, Push und das Öffnen eines GitHub-PR in einem Ablauf mit `gh` zu erledigen.                                                                    | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

Hinweise:
- `dogfood` und `electron` kommen upstream aus `skill-data/`, nicht aus `skills/`.
- Upstream hat diese spezialisierten Skills in Commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` verschoben, damit die Installer-Erkennung nur das Bootstrap-Skill `agent-browser` findet.
- Dieses Repository behält sie bewusst als vendorte Top-Level-Skills, weil sie upstream weiter gepflegt werden und direkt nützlich bleiben.

### Vendorte `impeccable/`-Skills

| Skill                                                    | Beschreibung                                                                                          | Source URL                                                  |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [impeccable](impeccable/impeccable/SKILL.md)   | Unverwechselbare, produktionsreife Frontends mit hoher Designqualität erstellen.                      | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md)                       | Designs auf unterschiedliche Bildschirmgrößen, Geräte und Kontexte anpassen.                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md)                   | Zweckgerichtete Motion und Mikrointeraktionen ergänzen.                                               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md)                       | Interface-Qualität in Bezug auf Accessibility, Performance, Theming und Responsive Design auditieren. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md)                     | Sichere oder langweilige Designs visuell interessanter machen.                                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md)                   | Unklare UX-Texte und Anweisungen verbessern.                                                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md)                 | Strategische Farbe zu übermäßig monochromen Oberflächen hinzufügen.                                   | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md)                 | Designwirksamkeit aus UX-Sicht bewerten.                                                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md)                   | Interfaces Persönlichkeit und erinnerungswürdige Momente geben.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md)                   | Designs auf ihre wesentliche Form reduzieren.                                                         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md)                     | Resilienz bei Fehlern, i18n, Overflow und Randfällen verbessern.                                      | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [layout](impeccable/layout/SKILL.md)                       | Layout, Abstande und visuellen Rhythmus verbessern.                                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | Frontend-Performance, Rendering, Motion und Bundle-Effizienz verbessern.                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [overdrive](impeccable/overdrive/SKILL.md)                 | Interfaces mit technisch ambitionierten Umsetzungen uber herkommliche Grenzen hinausschieben. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | Letzter Qualitätsschliff für Ausrichtung, Abstände, Konsistenz und Details.                           | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | Visuelle Aggressivität reduzieren und die Qualität beibehalten.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [shape](impeccable/shape/SKILL.md)                         | UX und UI eines Features planen, bevor Code geschrieben wird.                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [typeset](impeccable/typeset/SKILL.md)                     | Typografie verbessern, indem Schriftwahl, Hierarchie, Grossen, Gewichtung und Lesbarkeit optimiert werden. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

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

Einige Skills enthalten zusätzliche Lizenzdateien oder Hinweise zu skill-spezifischen Assets und Attributionen, darunter [`minimax-docx/`](minimax-docx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), und [`skill-creator/`](skill-creator/).
