# OK Skills: skills de agentes de programacion con IA para Codex, Claude Code, Cursor, OpenClaw y mas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | Español | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Coleccion curada de skills para agentes de programacion con IA y playbooks de `CLAUDE.md` / `AGENTS.md` para Codex, Claude Code, Cursor, OpenClaw, Trae y otras herramientas compatibles con `SKILL.md`.

Este repositorio incluye actualmente **15 skills reutilizables**, todas mantenidas directamente como directorios de skill de nivel superior en este repo. Clonalo en `~/.agents/skills/ok-skills`; los directorios internos ya siguen la estructura esperada por los flujos basados en `AGENTS.md`, y [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) aporta un agent playbook orientado a Claude Code.

Si estas buscando **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, playbooks reutilizables de **CLAUDE.md / AGENTS.md** o ejemplos practicos de **SKILL.md**, este repositorio esta organizado para ser facil de encontrar y facil de usar desde el primer clon.


## Para Quien Es Este Repositorio

- Usas Codex, Claude Code, Cursor, OpenClaw, Trae u otro agente de programacion con IA y quieres reutilizar skills en lugar de depender de prompts improvisados.
- Mantienes flujos con `CLAUDE.md` / `AGENTS.md` / `SKILL.md` y quieres instrucciones portables que funcionen entre distintos proyectos.

## Empieza Por Aqui

Si al principio solo vas a instalar unas pocas skills, empieza por estas:

- [planning-with-files](planning-with-files/SKILL.md): planificacion basada en archivos para tareas complejas, investigacion y trabajo de larga duracion.
- [find-docs](find-docs/SKILL.md): consulta documentacion actual de librerias, referencias de API y ejemplos de Context7.
- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para capturas, formularios, scraping y QA web.

## Inicio Rapido En 1 Minuto

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Despues de clonar, el repositorio quedara en `~/.agents/skills/ok-skills`, y los directorios internos ya siguen la estructura esperada:

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

Para instrucciones globales de Claude Code o Codex, empieza por [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) y copialo o fusionarlo en el `CLAUDE.md` de Claude Code o el `AGENTS.md` de Codex. Incluye un workflow Chinese-first y orientado a KISS, checks de documentacion/source actual, preferencia por multi-agent, `caveman` / `planning-with-files` / `karpathy-guidelines` activados por defecto, expectativas estrictas de TypeScript y reglas de enrutamiento de context-mode. Antes de reutilizarlo, edita la seccion `语言要求` para tu proyecto. La seccion `其他注意项` es intencionalmente local al proyecto y puede editarse segun sea necesario.

Anade reglas de activacion simples a tu `AGENTS.md`, o fusiona los mismos triggers de skills en `CLAUDE.md` / `AGENTS.md`:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- find-docs: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Despues puedes pedirlo de forma natural:

- `Use planning-with-files before refactoring this module.`
- `Use find-docs to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Explora Skills Por Caso De Uso

### Investigacion y Documentacion

- [find-docs](find-docs/SKILL.md): flujo de Context7 CLI centrado en buscar documentacion actual.
- [exa-search](exa-search/SKILL.md): investigacion web, de codigo y de empresas con herramientas de Exa.
- [find-skills](find-skills/SKILL.md): descubre skills existentes cuando un usuario pide una capacidad concreta.

### Planificacion y Prompting

- [planning-with-files](planning-with-files/SKILL.md): planificacion persistente en Markdown con `task_plan.md`, `findings.md` y `progress.md`.
- [autoresearch](autoresearch/SKILL.md): iteracion autonoma orientada a objetivos con metas, metricas, ciclos de verificacion y compuertas keep/discard.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): bucle disciplinado de diagnostico para bugs dificiles y regresiones de rendimiento.
- [grilling](grilling/SKILL.md): bucle reutilizable de entrevista pregunta por pregunta para sesiones grill directas.
- [teach](teach/SKILL.md): mantiene un workspace de ensenanza con mission, resources, lessons y learning records.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): pautas de conducta al programar para reducir sobrecomplicacion, supuestos ocultos y cambios no verificables.
- [tdd](tdd/SKILL.md): red-green-refactor test-first para funcionalidades, correcciones, refactors y cambios de comportamiento.

### Automatizacion y QA

- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para navegacion, formularios, capturas y scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): controla el navegador real del usuario mediante un daemon local para navegacion, formularios, capturas, lectura de paginas y sesiones autenticadas.

### Frontend y Diseno

- [better-icons](better-icons/SKILL.md): busca, explora y obtiene iconos SVG de mas de 200 bibliotecas de Iconify mediante CLI o MCP.

## Paquetes De Skills Vendorizados

[`planning-with-files/`](planning-with-files/) usa [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) como baseline upstream. Este repositorio usa ese directorio upstream como baseline canonica para la skill local. Las diferencias locales se limitan al frontmatter de `SKILL.md` compatible con `skills-ref` y a rutas relativas de scripts independientes de la ubicacion de instalacion en la documentacion.

## Requisitos Habituales

- Algunas skills asumen que `gh` esta instalado y autenticado.
- Las skills centradas en navegador pueden requerir un entorno compatible con Chrome/CDP.
- Las skills de consulta de documentacion de terceros pueden depender de CLI externas o herramientas MCP; revisa cada `SKILL.md` para los detalles.

## Indice Completo De Skills

`Source URL` apunta al upstream canonico cuando una skill fue importada o vendorizada; en caso contrario, apunta al directorio de la skill dentro de este repositorio.

### Skills De Nivel Superior

| Skill                                                               | Descripcion                                                                                                                                                                                                         | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | CLI de automatizacion de navegador para agentes de IA: navegacion, formularios, capturas, extraccion y pruebas web.                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [autoresearch](autoresearch/SKILL.md)                               | Motor de iteracion autonoma orientada a objetivos para flujos de modificar, verificar, conservar/descartar y repetir.                                                                    | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | Busca en mas de 200 bibliotecas de Iconify y obtiene iconos SVG mediante CLI o herramientas MCP.                                                                                                                    | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Controla el navegador real del usuario mediante un daemon local para navegacion, formularios, capturas, lectura de paginas y sesiones autenticadas.                                                                 | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [caveman](caveman/SKILL.md)                                         | Modo de comunicacion ultra comprimido que reduce tokens de respuesta hablando como cavernicola sin perder precision tecnica.                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Bucle disciplinado de diagnostico para bugs dificiles y regresiones de rendimiento.                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | Usa Context7 CLI para consultar documentacion actual, referencias de API y ejemplos de codigo.                                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | Usa Exa para investigacion web, de codigo y de empresas.                                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Descubre skills existentes cuando los usuarios necesitan capacidades especializadas.                                                                                                                                | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [grilling](grilling/SKILL.md)                               | Bucle reutilizable de entrevista pregunta por pregunta para sesiones grill directas.                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | Ensena una skill o concepto en un workspace con mission, resources, lessons y learning records. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Pautas de conducta al programar para reducir sobrecomplicacion, supuestos ocultos y cambios no verificables.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [planning-with-files](planning-with-files/SKILL.md)                 | Planificacion basada en archivos para tareas complejas mediante `task_plan.md`, `findings.md` y `progress.md`.                                                                                                      | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [tdd](tdd/SKILL.md)                                                 | Usala antes de funcionalidades, correcciones, refactors o cambios de comportamiento; prefiere pruebas de integracion via interfaces publicas.                                                                       | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## Contribuir

Se aceptan contribuciones para nuevas skills o para mejorar las existentes.

1. Mantén las condiciones de activacion explicitas y comprobables.
2. Mantén los ejemplos concisos y orientados a la ejecucion.
3. Si una skill depende de herramientas externas, documenta esa dependencia en `SKILL.md`.
4. Actualiza `README.md` y `README.zh-CN.md` cuando anadas o renombres una skill, y refresca las demas READMEs traducidas cuando cambie el indice publico de skills.

## Licencia

Este repositorio esta licenciado bajo [LICENSE](LICENSE).
