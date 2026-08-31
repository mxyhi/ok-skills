# OK Skills: skills de agentes de programacion con IA para Codex, Claude Code, Cursor, OpenClaw y mas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | Español | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Coleccion curada de skills para agentes de programacion con IA y playbooks de `CLAUDE.md` / `AGENTS.md` para Codex, Claude Code, Cursor, OpenClaw, Trae y otras herramientas compatibles con `SKILL.md`.

Este repositorio incluye actualmente **29 skills reutilizables**, todas mantenidas directamente como directorios de skill de nivel superior en este repo. Clonalo en `~/.agents/skills/ok-skills`; los directorios internos ya siguen la estructura esperada por los flujos basados en `AGENTS.md`, y [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) aporta un agent playbook orientado a Claude Code.

Si estas buscando **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, playbooks reutilizables de **CLAUDE.md / AGENTS.md** o ejemplos practicos de **SKILL.md**, este repositorio esta organizado para ser facil de encontrar y facil de usar desde el primer clon.

**Casos de uso frecuentes:** consulta de documentacion actual, automatizacion de navegador, prompt engineering, planificacion de tareas complejas, diseno frontend y trabajo con PDF / Word / PPTX / XLSX.

## Para Quien Es Este Repositorio

- Usas Codex, Claude Code, Cursor, OpenClaw, Trae u otro agente de programacion con IA y quieres reutilizar skills en lugar de depender de prompts improvisados.
- Mantienes flujos con `CLAUDE.md` / `AGENTS.md` / `SKILL.md` y quieres instrucciones portables que funcionen entre distintos proyectos.
- Necesitas skills probadas para busqueda de documentacion, automatizacion de navegador, planificacion, prompt engineering, frontend, PDF, documentos de Office, presentaciones y hojas de calculo.

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
- [get-api-docs](get-api-docs/SKILL.md): recupera la documentacion actual de APIs y SDK de terceros antes de programar.
- [find-skills](find-skills/SKILL.md): descubre skills existentes cuando un usuario pide una capacidad concreta.
- [ax](ax/SKILL.md): curl de la era de la IA — fetch de paginas, descubrir estructura y extraer datos estructurados sin scripts de parseo desechables.

### Planificacion y Prompting

- [planning-with-files](planning-with-files/SKILL.md): planificacion persistente en Markdown con `task_plan.md`, `findings.md` y `progress.md`.
- [product-decision-agent](product-decision-agent/SKILL.md): agente de decisión de producto centrado en chino para diagnosticar cuellos de botella, priorización, crecimiento, métricas, operaciones y coordinación entre equipos.
- [autoresearch](autoresearch/SKILL.md): iteracion autonoma orientada a objetivos con metas, metricas, ciclos de verificacion y compuertas keep/discard.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): bucle disciplinado de diagnostico para bugs dificiles y regresiones de rendimiento.
- [grilling](grilling/SKILL.md): bucle reutilizable de entrevista en árbol de diseño para sesiones grill directas.
- [teach](teach/SKILL.md): mantiene un workspace de ensenanza con mission, resources, lessons y learning records.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): encuentra oportunidades de deepening que mejoran locality, leverage, testabilidad y navegacion por IA.
- [prototype](prototype/SKILL.md): crea prototipos descartables de logica o UI para responder preguntas de diseno rapido.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): pautas de conducta al programar para reducir sobrecomplicacion, supuestos ocultos y cambios no verificables.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): migra assertions de tipo `as` en tests a `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): red-green-refactor test-first para funcionalidades, correcciones, refactors y cambios de comportamiento.

### Automatizacion y QA

- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para navegacion, formularios, capturas y scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): controla el navegador real del usuario mediante un daemon local para navegacion, formularios, capturas, lectura de paginas y sesiones autenticadas.
- [browser-trace](browser-trace/SKILL.md): captura trazas CDP, capturas de pantalla y dumps DOM para depurar automatizacion del navegador.
- [opencli](opencli/opencli-usage/SKILL.md): convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.

### Frontend y Diseno

- [ai-elements](ai-elements/SKILL.md): crea componentes de interfaz conversacional para la libreria `ai-elements`.
- [huashu-design](huashu-design/SKILL.md): crea prototipos HTML de alta fidelidad, demos interactivas, decks, motion design, variantes, exportes de video y criticas de diseno.
- [imagegen-frontend-web](imagegen-frontend-web/SKILL.md): genera referencias visuales premium para frontend, una imagen horizontal por seccion.
- [gpt-taste](gpt-taste/SKILL.md): crea paginas frontend con estructura AIDA, layouts aleatorios y patrones GSAP.
- [better-icons](better-icons/SKILL.md): busca, explora y obtiene iconos SVG de mas de 200 bibliotecas de Iconify mediante CLI o MCP.
- [diagram-design](diagram-design/SKILL.md): crea diagramas editoriales con marca como HTML/SVG/PNG autonomos — arquitectura, flowchart, secuencia y 36 tipos mas. Redibuja draw.io o Mermaid.

### Utilidades y Creacion De Contenido

- [huashu-design](huashu-design/SKILL.md): produce HTML decks, PPTX editables, piezas MP4/GIF y videos de diseno narrados.

## Paquetes De Skills Vendorizados

[`planning-with-files/`](planning-with-files/) usa [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) como baseline upstream. Este repositorio usa ese directorio upstream como baseline canonica para la skill local. Las diferencias locales se limitan al frontmatter de `SKILL.md` compatible con `skills-ref` y a rutas relativas de scripts independientes de la ubicacion de instalacion en la documentacion.

## Requisitos Habituales

- Algunas skills asumen que `gh` esta instalado y autenticado.
- Las skills centradas en navegador pueden requerir un entorno compatible con Chrome/CDP.
- Las skills de consulta de documentacion de terceros pueden depender de CLI externas o herramientas MCP; revisa cada `SKILL.md` para los detalles.
- La exportacion PNG de diagram-design necesita Playwright y Chromium: `pip install playwright && playwright install chromium`.

## Indice Completo De Skills

`Source URL` apunta al upstream canonico cuando una skill fue importada o vendorizada; en caso contrario, apunta al directorio de la skill dentro de este repositorio.

### Skills De Nivel Superior

| Skill                                                               | Descripcion                                                                                                                                                                                                         | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | CLI de automatizacion de navegador para agentes de IA: navegacion, formularios, capturas, extraccion y pruebas web.                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | Crea nuevos componentes de chat con IA para la libreria ai-elements con patrones componibles y convenciones de shadcn/ui.                                                                                           | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [autoresearch](autoresearch/SKILL.md)                               | Motor de iteracion autonoma orientada a objetivos para flujos de modificar, verificar, conservar/descartar y repetir.                                                                    | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [ax](ax/SKILL.md)                                                   | curl de la era de la IA: obtener URLs, descubrir estructura de pagina y extraer datos estructurados de HTML sin scripts de parseo desechables.                              | [yusukebe/ax](https://github.com/yusukebe/ax/tree/main/skills/ax)                                                             |

| [better-icons](better-icons/SKILL.md)                               | Busca en mas de 200 bibliotecas de Iconify y obtiene iconos SVG mediante CLI o herramientas MCP.                                                                                                                    | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Controla el navegador real del usuario mediante un daemon local para navegacion, formularios, capturas, lectura de paginas y sesiones autenticadas.                                                                 | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | Captura trazas CDP, capturas de pantalla y dumps DOM para depurar automatizacion del navegador.                                                                    | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | Modo de comunicacion ultra comprimido que reduce tokens de respuesta hablando como cavernicola sin perder precision tecnica.                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Bucle disciplinado de diagnostico para bugs dificiles y regresiones de rendimiento.                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [diagram-design](diagram-design/SKILL.md)                           | Crea diagramas editoriales HTML/SVG/PNG (39 tipos). Redibuja fuentes draw.io o Mermaid.                                                               | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design/tree/main/skills/diagram-design)                 |
| [find-docs](find-docs/SKILL.md)                                     | Usa Context7 CLI para consultar documentacion actual, referencias de API y ejemplos de codigo.                                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | Usa Exa para investigacion web, de codigo y de empresas.                                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Descubre skills existentes cuando los usuarios necesitan capacidades especializadas.                                                                                                                                | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | Crea prototipos HTML de alta fidelidad, demos interactivas, decks, motion design, variantes, exportes de video y criticas de diseno.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [imagegen-frontend-web](imagegen-frontend-web/SKILL.md) | Genera referencias visuales premium para frontend, una imagen horizontal por seccion. | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/imagegen-frontend-web) |
| [gpt-taste](gpt-taste/SKILL.md) | Crea paginas frontend con estructura AIDA, layouts aleatorios y patrones GSAP. | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/gpt-tasteskill) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Obtiene la documentacion actual de APIs o SDK de terceros antes de escribir codigo.                                                                                                                                 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grilling](grilling/SKILL.md)                               | Bucle reutilizable de entrevista en árbol de diseño para sesiones grill directas.                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | Ensena una skill o concepto en un workspace con mission, resources, lessons y learning records. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Encuentra oportunidades de deepening que mejoran locality, leverage, testabilidad y navegacion por IA.                                                                                                            | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [prototype](prototype/SKILL.md) | Crea prototipos descartables de logica o UI para responder preguntas de diseno rapido. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Pautas de conducta al programar para reducir sobrecomplicacion, supuestos ocultos y cambios no verificables.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migra archivos de test desde assertions de tipo `as` a `@total-typescript/shoehorn`.                                                                                                                            | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.                                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [planning-with-files](planning-with-files/SKILL.md)                 | Planificacion basada en archivos para tareas complejas mediante `task_plan.md`, `findings.md` y `progress.md`.                                                                                                      | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [product-decision-agent](product-decision-agent/SKILL.md)           | Agente de decisión de producto centrado en chino para diagnosticar cuellos de botella, priorización, crecimiento, métricas, operaciones y coordinación entre equipos.                                           | [atdy/maoxuan-product-agent](https://github.com/atdy/maoxuan-product-agent/tree/main/product-decision-agent)                      |
| [tdd](tdd/SKILL.md)                                                 | Usala antes de funcionalidades, correcciones, refactors o cambios de comportamiento; prefiere pruebas de integracion via interfaces publicas.                                                                       | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## Contribuir

Se aceptan contribuciones para nuevas skills o para mejorar las existentes.

1. Mantén las condiciones de activacion explicitas y comprobables.
2. Mantén los ejemplos concisos y orientados a la ejecucion.
3. Si una skill depende de herramientas externas, documenta esa dependencia en `SKILL.md`.
4. Actualiza `README.md` y `README.zh-CN.md` cuando anadas o renombres una skill, y refresca las demas READMEs traducidas cuando cambie el indice publico de skills.

## Licencia

Este repositorio esta licenciado bajo [LICENSE](LICENSE).
