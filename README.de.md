# OK Skills: AI Coding Agent Skills für Codex, Claude Code, Cursor, OpenClaw und mehr

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Deutsch | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Kuratiertes Repository für AI Coding Agent Skills und `CLAUDE.md` / `AGENTS.md`-Playbooks für Codex, Claude Code, Cursor, OpenClaw, Trae und andere Tools, die mit `SKILL.md`-Workflows kompatibel sind.

Dieses Repository bündelt aktuell **18 wiederverwendbare Skills**, alle als Top-Level-Skill-Verzeichnisse direkt in diesem Repository gepflegt. Klone es nach `~/.agents/skills/ok-skills`; die enthaltenen Verzeichnisse entsprechen bereits dem Layout, das `AGENTS.md`-gesteuerte Workflows erwarten, und [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) bietet ein auf Claude Code ausgerichtetes Agent-Playbook.

Wenn du nach **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, wiederverwendbaren **CLAUDE.md / AGENTS.md**-Playbooks oder praxistauglichen **SKILL.md**-Beispielen suchst, ist dieses Repository bewusst auf Auffindbarkeit und sofortige Nutzbarkeit ausgelegt.


## Für wen dieses Repository gedacht ist

- Du nutzt Codex, Claude Code, Cursor, OpenClaw, Trae oder einen anderen AI Coding Agent und möchtest wiederverwendbare Skills statt ad-hoc Prompts.
- Du pflegst Workflows auf Basis von `CLAUDE.md` / `AGENTS.md` / `SKILL.md` und willst portable Anleitungen, die projektübergreifend funktionieren.

## Einstieg

Wenn du zuerst nur wenige Skills installieren willst, beginne mit diesen:

- [planning-with-files](planning-with-files/SKILL.md): dateibasierte Planung für komplexe Aufgaben, Recherche und länger laufende Arbeit.
- [find-docs](find-docs/SKILL.md): aktuelle Bibliotheksdokumentation, API-Referenzen und Context7-Beispiele abrufen.
- [agent-browser](agent-browser/SKILL.md): Browser-Automatisierung für Screenshots, Formulare, Scraping und Web-QA.

## 1-Minuten-Schnellstart

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Nach dem Klonen liegt das Repository unter `~/.agents/skills/ok-skills`, und die enthaltenen Verzeichnisse entsprechen bereits dem erwarteten Layout:

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

Für globale Claude-Code- oder Codex-Anweisungen kannst du mit [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) starten und es in Claude Codes `CLAUDE.md` oder Codex' `AGENTS.md` kopieren oder mergen. Es bündelt einen Chinese-first, KISS-orientierten Workflow mit aktuellen Dokumentations-/Source-Checks, Multi-Agent-Präferenz, standardmäßig aktivierten `caveman` / `planning-with-files` / `karpathy-guidelines`, strikten TypeScript-Erwartungen und context-mode Routing-Regeln. Passe vor der Wiederverwendung den Abschnitt `语言要求` an dein Projekt an. Der Abschnitt `其他注意项` ist bewusst projektlokal und kann nach Bedarf bearbeitet werden.

Füge deinem `AGENTS.md` einfache Trigger-Regeln hinzu oder übernimm dieselben Skill-Trigger in `CLAUDE.md` / `AGENTS.md`:

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

- [ax](ax/SKILL.md): curl für das AI-Zeitalter — URLs holen, Seitenstruktur entdecken, strukturierte Daten extrahieren ohne Wegwerf-Parser.
- [find-docs](find-docs/SKILL.md): fokussierter Context7-CLI-Workflow für aktuelle Dokumentationssuche.
- [exa-search](exa-search/SKILL.md): Web-, Code- und Unternehmensrecherche mit Exa-Suchwerkzeugen.
- [get-api-docs](get-api-docs/SKILL.md): aktuelle Third-Party-API- und SDK-Dokumentation vor dem Coden abrufen.
- [find-skills](find-skills/SKILL.md): vorhandene Skills finden, wenn ein Benutzer nach einer Fähigkeit fragt.

### Planung und Prompting

- [planning-with-files](planning-with-files/SKILL.md): persistente Markdown-Planung mit `task_plan.md`, `findings.md` und `progress.md`.
- [autoresearch](autoresearch/SKILL.md): autonome zielgerichtete Iteration mit expliziten Zielen, Metriken, Verifikationsschleifen und Keep/Discard-Gates.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): disziplinierte Diagnose-Schleife fuer schwierige Bugs und Performance-Regressionen.
- [grilling](grilling/SKILL.md): wiederverwendbare One-question-at-a-time Interview-Schleife fuer direkte Grill-Sessions.
- [teach](teach/SKILL.md): ein stateful Teaching-Workspace mit Mission, Ressourcen, Lessons und Learning Records fuehren.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): Coding-Verhaltensregeln gegen Overengineering, versteckte Annahmen und nicht verifizierbare Änderungen.
- [tdd](tdd/SKILL.md): test-first red-green-refactor fur Features, Bugfixes, Refactorings und Verhaltensaenderungen.

### Automatisierung und QA

- [agent-browser](agent-browser/SKILL.md): Browser-Automatisierung für Navigation, Formulare, Screenshots und Scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): Steuert den echten Browser des Nutzers über einen lokalen Daemon für Navigation, Formulare, Screenshots, Seitenlesen und angemeldete Sessions.

### Frontend und Design

- [better-icons](better-icons/SKILL.md): SVG-Icons aus mehr als 200 Iconify-Bibliotheken per CLI oder MCP suchen, durchsuchen und abrufen.
- [diagram-design](diagram-design/SKILL.md): editorische HTML/SVG-Diagramme in 27 Typen, mit Brand-Tokens und draw.io/Mermaid-Redraw.

## Vendorte Skill-Pakete

[`planning-with-files/`](planning-with-files/) verwendet [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) als Upstream-Basis. Dieses Repository nutzt dieses Upstream-Verzeichnis als kanonische Basis für den lokalen Skill. Lokale Unterschiede sind auf `skills-ref`-kompatibles `SKILL.md`-Frontmatter und install-location-unabhaengige relative Skriptpfade in der Dokumentation beschraenkt.

## Häufige Voraussetzungen

- Der `ax`-Skill benötigt die `ax`-CLI (`curl -fsSL https://ax.yusuke.run/install | sh`).
- Der `diagram-design`-Skill nutzt Python 3 fuer Import-Extraktion und den mitgelieferten Self-Check.
- Einige Skills setzen voraus, dass `gh` installiert und authentifiziert ist.
- Browser-orientierte Skills können eine Chrome/CDP-fähige Umgebung erfordern.
- Skills für Dokumentationsrecherche können von externen CLIs oder MCP-Tools abhängen; Details stehen jeweils in `SKILL.md`.

## Vollständiger Skill-Index

`Source URL` verweist auf das kanonische Upstream, wenn ein Skill vendort oder importiert wurde; andernfalls zeigt sie auf das Skill-Verzeichnis in diesem Repository.

### Top-Level-Skills

| Skill                                                               | Beschreibung                                                                                                                                                                                                       | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [ax](ax/SKILL.md)                                                   | curl für das AI-Zeitalter: URLs holen, Seitenstruktur entdecken, strukturierte Daten extrahieren ohne Wegwerf-Parser.                                                               | [yusukebe/ax](https://github.com/yusukebe/ax/tree/main/skills/ax)                                                              |
| [agent-browser](agent-browser/SKILL.md)                             | Browser-Automatisierungs-CLI für AI Agents: Navigation, Formularausfüllung, Screenshots, Extraktion und Web-Tests.                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [autoresearch](autoresearch/SKILL.md)                               | Autonome zielgerichtete Iterations-Engine für Modify-, Verify-, Keep/Discard- und Repeat-Workflows.                                                                                     | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | Durchsuche über 200 Iconify-Bibliotheken und hole SVG-Icons per CLI oder MCP-Tools.                                                                                                                                | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Steuert den echten Browser des Nutzers über einen lokalen Daemon für Navigation, Formulare, Screenshots, Seitenlesen und angemeldete Sessions.                                                                       | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [caveman](caveman/SKILL.md)                                         | Ultrasparsamer Kommunikationsmodus, der Antwort-Tokens im Hoehlenmenschenstil reduziert, ohne technische Genauigkeit zu verlieren.                                                         | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Disziplinierte Diagnose-Schleife fuer schwierige Bugs und Performance-Regressionen.                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [diagram-design](diagram-design/SKILL.md)                             | Editorische HTML/SVG/PNG-Diagramme in 27 Typen; Brand-Tokens; draw.io- oder Mermaid-Quellen neu zeichnen.                                                                                                | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design/tree/main/skills/diagram-design) |
| [find-docs](find-docs/SKILL.md)                                     | Die Context7 CLI für aktuelle Dokumentation, API-Referenzen und Codebeispiele verwenden.                                                                                                                          | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | Exa für Web-, Code- und Unternehmensrecherche verwenden.                                                                                                                                                           | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Vorhandene Skills entdecken, wenn Benutzer spezialisierte Fähigkeiten benötigen.                                                                                                                                   | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | Aktuelle Dokumentation zu APIs oder SDKs von Drittanbietern abrufen, bevor Code geschrieben wird.                                                                                                                  | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grilling](grilling/SKILL.md)                               | Wiederverwendbare One-question-at-a-time Interview-Schleife fuer direkte Grill-Sessions.                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | Vermittelt Skills oder Konzepte in einem stateful Workspace mit Mission, Ressourcen, Lessons und Learning Records. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Coding-Verhaltensregeln gegen Overengineering, versteckte Annahmen und nicht verifizierbare Änderungen.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [planning-with-files](planning-with-files/SKILL.md)                 | Dateibasierte Planung für komplexe Aufgaben mit `task_plan.md`, `findings.md` und `progress.md`.                                                                                                                   | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [tdd](tdd/SKILL.md)                                                 | Vor Features, Bugfixes, Refactorings oder Verhaltensaenderungen verwenden; bevorzugt Integrationstests ueber public interfaces.                                                                                    | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## Mitwirken

Beiträge für neue Skills oder Verbesserungen an bestehenden Skills sind willkommen.

1. Halte Trigger-Bedingungen explizit und testbar.
2. Halte Beispiele knapp und ausführungsorientiert.
3. Wenn ein Skill von externen Tools abhängt, dokumentiere diese Abhängigkeit in `SKILL.md`.
4. Aktualisiere `README.md` und `README.zh-CN.md`, wenn du einen Skill hinzufügst oder umbenennst, und aktualisiere die übrigen übersetzten READMEs, sobald sich der öffentliche Skill-Index ändert.

## Lizenz

Dieses Repository steht unter der Lizenz aus [LICENSE](LICENSE).
