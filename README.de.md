# OK Skills: AI Coding Agent Skills für Codex, Claude Code, Cursor, OpenClaw und mehr

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Deutsch | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

Kuratiertes Repository für AI Coding Agent Skills und `AGENTS.md`-Playbooks für Codex, Claude Code, Cursor, OpenClaw, Trae und andere Tools, die mit `SKILL.md`-Workflows kompatibel sind.

Dieses Repository bündelt aktuell **45 wiederverwendbare Skills**: **27 Top-Level-Skills**, die direkt hier gepflegt werden, plus **18 vendorte Design-Skills** unter [`impeccable/`](impeccable/README.md). Klone es nach `~/.agents/skills/ok-skills`; die enthaltenen Verzeichnisse entsprechen bereits dem Layout, das `AGENTS.md`-gesteuerte Workflows erwarten.

Wenn du nach **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, wiederverwendbaren **AGENTS.md**-Playbooks oder praxistauglichen **SKILL.md**-Beispielen suchst, ist dieses Repository bewusst auf Auffindbarkeit und sofortige Nutzbarkeit ausgelegt.

**Häufige Einsatzfälle:** aktuelle Dokumentation nachschlagen, Browser-Automatisierung, GitHub-Actions-Debugging, Prompt Engineering, Planung komplexer Aufgaben, Frontend-Design sowie PDF / Word / PPTX / XLSX Authoring.

## Für wen dieses Repository gedacht ist

- Du nutzt Codex, Claude Code, Cursor, OpenClaw, Trae oder einen anderen AI Coding Agent und möchtest wiederverwendbare Skills statt ad-hoc Prompts.
- Du pflegst Workflows auf Basis von `AGENTS.md` und `SKILL.md` und willst portable Anleitungen, die projektübergreifend funktionieren.
- Du brauchst erprobte Skills für Dokumentationsrecherche, Browser-Automatisierung, GitHub-Workflows, Planung, Prompt Engineering, Frontend-Design, PDFs, Office-Dokumente, Foliensätze und Tabellen.

## Einstieg

Wenn du zuerst nur wenige Skills installieren willst, beginne mit diesen:

- [planning-with-files](planning-with-files/SKILL.md): dateibasierte Planung für komplexe Aufgaben, Recherche und länger laufende Arbeit.
- [context7-cli](context7-cli/SKILL.md): aktuelle Bibliotheksdokumentation und Context7-basierte Referenzen abrufen.
- [agent-browser](agent-browser/SKILL.md): Browser-Automatisierung für Screenshots, Formulare, Scraping und Web-QA.
- [gh-fix-ci](gh-fix-ci/SKILL.md): fehlgeschlagene GitHub-Actions-Checks untersuchen und aus Logs einen Fixplan ableiten.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): produktionsorientierte Prompt-Muster für verlässlichere LLM-Workflows.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): hochwertiger Frontend-Design-Skill plus ein vollständiges Bundle ergänzender Design-Kommandos.

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

- [brainstorming](brainstorming/SKILL.md): Absicht, Anforderungen und Design vor der Implementierung klären.
- [planning-with-files](planning-with-files/SKILL.md): persistente Markdown-Planung mit `task_plan.md`, `findings.md` und `progress.md`.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): fortgeschrittene Prompt-Design-Muster für produktive LLM-Systeme.
- [test-driven-development](test-driven-development/SKILL.md): Tests vor der Implementierungsarbeit durchsetzen.

### GitHub-Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): Review- und Issue-Kommentare im aktuellen PR mit `gh` bearbeiten.
- [gh-fix-ci](gh-fix-ci/SKILL.md): fehlgeschlagene GitHub-Actions-Checks untersuchen, Logs zusammenfassen und Fixes planen.
- [yeet](yeet/SKILL.md): nur verwenden, wenn der Benutzer explizit darum bittet, Stage, Commit, Push und das Öffnen eines GitHub-PR in einem einzigen `gh`-basierten Ablauf zu erledigen.

### Automatisierung und QA

- [agent-browser](agent-browser/SKILL.md): Browser-Automatisierung für Navigation, Formulare, Screenshots und Scraping.
- [chrome-cdp](chrome-cdp/SKILL.md): Verbindung zu einer bereits laufenden lokalen Chrome-Sitzung per CDP für leichte Seiteninspektion und Interaktion.
- [bb-browser](bb-browser/SKILL.md): Informationsgewinnung und Browser-Automatisierung über den echten Browser und den Login-Status des Nutzers.
- [pinchtab](pinchtab/SKILL.md): Chrome über Pinchtabs lokale HTTP-API mit stabilen Accessibility-Referenzen steuern.
- [electron](electron/SKILL.md): Electron-Desktop-Apps über das Chrome DevTools Protocol automatisieren.
- [opencli](opencli/SKILL.md): Websites mit wiederverwendeter Browser-Session, Public APIs und KI-generierten Adaptern als CLI nutzen.
- [dogfood](dogfood/SKILL.md): strukturierte explorative Tests mit reproduzierbaren Belegen.

### Frontend und Design

- [ai-elements](ai-elements/SKILL.md): AI-Chat-UI-Komponenten für die Bibliothek `ai-elements` erstellen.
- [better-icons](better-icons/SKILL.md): SVG-Icons aus mehr als 200 Iconify-Bibliotheken per CLI oder MCP suchen, durchsuchen und abrufen.
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): React- und Next.js-Performanceleitlinien von Vercel Engineering.
- [remotion-best-practices](remotion-best-practices/SKILL.md): Remotion-Leitfaden für videobasierte Arbeit mit React.
- [`impeccable/`](impeccable/README.md): 18 vendorte Frontend-Design-Skills, darunter `frontend-design`, `adapt`, `audit`, `polish` und mehr.

### Utilities und Content-Erstellung

- [docx](docx/SKILL.md): Word-Dokumente mit Formatierung, Kommentaren und Änderungsverfolgung erstellen, lesen, bearbeiten und manipulieren.
- [pdf](pdf/SKILL.md): PDFs mit renderbewussten Prüfungen lesen, erstellen und überprüfen.
- [pptx](pptx/SKILL.md): Foliensätze, Vorlagen und Präsentationsinhalte erstellen, lesen, bearbeiten und manipulieren.
- [xlsx](xlsx/SKILL.md): Tabellenkalkulationen erstellen, bearbeiten, mit Formeln versehen und analysieren.
- [skill-creator](skill-creator/SKILL.md): Skills mit stärkerer Struktur und besseren Tool-Integrationen erstellen oder aktualisieren.

## Vendorte Skill-Pakete

[`impeccable/`](impeccable/README.md) enthält ein vendortes, designfokussiertes Bundle aus [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) auf Basis des Commits `b5af865d84bc1ba1b8bc7104488bc7db50977029`.

Enthalten sind:

- `frontend-design`: der zentrale Frontend-Design-Skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

Attributionen und rechtliche Dateien bleiben in [`impeccable/NOTICE.md`](impeccable/NOTICE.md) und [`impeccable/LICENSE`](impeccable/LICENSE) erhalten.

## Häufige Voraussetzungen

- Einige Skills setzen voraus, dass `gh` installiert und authentifiziert ist.
- Browser-orientierte Skills können eine Chrome/CDP-fähige Umgebung erfordern.
- Skills für Dokumentationsrecherche können von externen CLIs oder MCP-Tools abhängen; Details stehen jeweils in `SKILL.md`.

## Vollständiger Skill-Index

`Source URL` verweist auf das kanonische Upstream, wenn ein Skill vendort oder importiert wurde; andernfalls zeigt sie auf das Skill-Verzeichnis in diesem Repository.

### Top-Level-Skills

| Skill | Beschreibung | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | Browser-Automatisierungs-CLI für AI Agents: Navigation, Formularausfüllung, Screenshots, Extraktion und Web-Tests. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | Neue AI-Chat-Oberflächenkomponenten für die ai-elements-Bibliothek mit komponierbaren Mustern und shadcn/ui-Konventionen erstellen. | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [bb-browser](bb-browser/SKILL.md) | Skill für Informationsgewinnung und Browser-Automatisierung über den echten Browser und den Login-Status des Nutzers, inklusive öffentlicher Seiten, interner Systeme und eingeloggter Abläufe. | [epiral/bb-browser](https://github.com/epiral/bb-browser/tree/main/skills/bb-browser) |
| [better-icons](better-icons/SKILL.md) | Durchsuche über 200 Iconify-Bibliotheken und hole SVG-Icons per CLI oder MCP-Tools. | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills) |
| [brainstorming](brainstorming/SKILL.md) | Absicht, Anforderungen und Design vor der Implementierungsarbeit klären. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [chrome-cdp](chrome-cdp/SKILL.md) | Verbindet sich per CDP mit einer bereits laufenden lokalen Chrome-Sitzung für leichte Tab-Inspektion, Screenshots, DOM-Zugriff, Eingaben und Navigation. | [pasky/chrome-cdp-skill](https://github.com/pasky/chrome-cdp-skill/tree/main/skills/chrome-cdp) |
| [context7-cli](context7-cli/SKILL.md) | Die Context7 CLI für Dokumentationssuche, Skill-Management und MCP-Setup verwenden. | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | Word-Dokumente mit Formatierung, Kommentaren, Änderungsverfolgung und Bildaktualisierungen erstellen, lesen, bearbeiten und manipulieren. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | Web-Apps systematisch testen und reproduzierbare Fehlerberichte mit Screenshots und Videos erstellen. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | Electron-Desktop-Apps über agent-browser und das Chrome DevTools Protocol automatisieren. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | Exa für Web-, Code- und Unternehmensrecherche verwenden. | Custom |
| [find-skills](find-skills/SKILL.md) | Vorhandene Skills entdecken, wenn Benutzer spezialisierte Fähigkeiten benötigen. | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | Aktuelle Dokumentation zu APIs oder SDKs von Drittanbietern abrufen, bevor Code geschrieben wird. | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | PR-Review- und Issue-Kommentare im aktuellen Branch mit `gh` bearbeiten. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | Fehlgeschlagene GitHub-Actions-Checks untersuchen, Logs abrufen und Fixes planen. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [opencli](opencli/SKILL.md) | Websites mit wiederverwendeter Browser-Session, Public APIs und KI-generierten Adaptern in CLI-Befehle verwandeln. | [jackwener/opencli](https://github.com/jackwener/opencli) |
| [pdf](pdf/SKILL.md) | PDF-Dateien mit Rendering-Prüfungen und Python-Werkzeugen lesen, erstellen und überprüfen. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | Einen headless oder sichtbaren Chrome-Browser über Pinchtabs HTTP-API für Web-Automatisierung, Scraping, Formularausfüllung, Navigation, Screenshots und Extraktion mit stabilen Accessibility-Referenzen steuern. | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skill/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | Dateibasierte Planung für komplexe Aufgaben mit `task_plan.md`, `findings.md` und `progress.md`. | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.agent/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | PowerPoint-Präsentationen, Vorlagen, Layouts, Notizen und Foliensinhalte erstellen, lesen, bearbeiten und manipulieren. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Fortgeschrittene Prompt-Engineering-Muster für verlässliche, produktive LLM-Workflows. | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | Best Practices für das Erstellen von Videos in React mit Remotion. | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | Leitfaden zum Erstellen oder Aktualisieren von Skills mit spezialisiertem Wissen und Tool-Integrationen. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [test-driven-development](test-driven-development/SKILL.md) | Vor jeder neuen Funktion oder Fehlerbehebung verwenden. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | React- und Next.js-Leitlinien zur Performance-Optimierung von Vercel Engineering. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | Erstellung, Bearbeitung, Formeln, Formatierung und Analyse von Tabellenkalkulationen. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | Nur verwenden, wenn der Benutzer explizit verlangt, Staging, Commit, Push und das Öffnen eines GitHub-PR in einem Ablauf mit `gh` zu erledigen. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### Vendorte `impeccable/`-Skills

| Skill | Beschreibung | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | Unverwechselbare, produktionsreife Frontends mit hoher Designqualität erstellen. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | Designs auf unterschiedliche Bildschirmgrößen, Geräte und Kontexte anpassen. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | Zweckgerichtete Motion und Mikrointeraktionen ergänzen. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | Interface-Qualität in Bezug auf Accessibility, Performance, Theming und Responsive Design auditieren. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | Sichere oder langweilige Designs visuell interessanter machen. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | Unklare UX-Texte und Anweisungen verbessern. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | Strategische Farbe zu übermäßig monochromen Oberflächen hinzufügen. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | Designwirksamkeit aus UX-Sicht bewerten. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | Interfaces Persönlichkeit und erinnerungswürdige Momente geben. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | Designs auf ihre wesentliche Form reduzieren. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | Wiederverwendbare Komponenten, Tokens und Muster in ein Designsystem überführen. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | Resilienz bei Fehlern, i18n, Overflow und Randfällen verbessern. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | Ein Feature auf ein Designsystem angleichen und konsistent machen. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | Onboarding, Empty States und das erste Nutzungserlebnis verbessern. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | Frontend-Performance, Rendering, Motion und Bundle-Effizienz verbessern. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | Letzter Qualitätsschliff für Ausrichtung, Abstände, Konsistenz und Details. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | Visuelle Aggressivität reduzieren und die Qualität beibehalten. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | Designkontext erfassen und als dauerhafte Leitlinie für spätere Arbeit speichern. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## Mitwirken

Beiträge für neue Skills oder Verbesserungen an bestehenden Skills sind willkommen.

1. Halte Trigger-Bedingungen explizit und testbar.
2. Halte Beispiele knapp und ausführungsorientiert.
3. Wenn ein Skill von externen Tools abhängt, dokumentiere diese Abhängigkeit in `SKILL.md`.
4. Aktualisiere `README.md` und `README.zh-CN.md`, wenn du einen Skill hinzufügst oder umbenennst, und aktualisiere die übrigen übersetzten READMEs, sobald sich der öffentliche Skill-Index ändert.

## Lizenz

Dieses Repository steht unter der Lizenz aus [LICENSE](LICENSE).

Einige Skills enthalten zusätzliche Lizenzdateien oder Hinweise zu skill-spezifischen Assets und Attributionen, darunter [`docx/`](docx/), [`pptx/`](pptx/), [`impeccable/`](impeccable/README.md), [`skill-creator/`](skill-creator/) und [`xlsx/`](xlsx/).
