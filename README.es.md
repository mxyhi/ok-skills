# OK Skills: skills de agentes de programacion con IA para Codex, Claude Code, Cursor, OpenClaw y mas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | Español | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Coleccion curada de skills para agentes de programacion con IA y playbooks de `AGENTS.md` para Codex, Claude Code, Cursor, OpenClaw, Trae y otras herramientas compatibles con `SKILL.md`.

Este repositorio incluye actualmente **36 skills reutilizables**: **28 skills de nivel superior** mantenidos directamente aqui, ademas de **8 skills de animacion GSAP** integradas como paquete vendorizado en [`gsap-skills/`](gsap-skills/). Clonalo en `~/.agents/skills/ok-skills`; los directorios internos ya siguen la estructura esperada por los flujos basados en `AGENTS.md`.

Si estas buscando **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, playbooks reutilizables de **AGENTS.md** o ejemplos practicos de **SKILL.md**, este repositorio esta organizado para ser facil de encontrar y facil de usar desde el primer clon.

**Casos de uso frecuentes:** consulta de documentacion actual, automatizacion de navegador, depuracion de GitHub Actions, prompt engineering, planificacion de tareas complejas, diseno frontend y trabajo con PDF / Word / PPTX / XLSX.

## Para Quien Es Este Repositorio

- Usas Codex, Claude Code, Cursor, OpenClaw, Trae u otro agente de programacion con IA y quieres reutilizar skills en lugar de depender de prompts improvisados.
- Mantienes flujos con `AGENTS.md` / `SKILL.md` y quieres instrucciones portables que funcionen entre distintos proyectos.
- Necesitas skills probadas para busqueda de documentacion, automatizacion de navegador, flujo de GitHub, planificacion, prompt engineering, frontend, PDF, documentos de Office, presentaciones y hojas de calculo.

## Empieza Por Aqui

Si al principio solo vas a instalar unas pocas skills, empieza por estas:

- [brainstorming](brainstorming/SKILL.md): aclara ideas, requisitos y diseno antes de empezar la implementacion.
- [planning-with-files](planning-with-files/SKILL.md): planificacion basada en archivos para tareas complejas, investigacion y trabajo de larga duracion.
- [find-docs](find-docs/SKILL.md): consulta documentacion actual de librerias, referencias de API y ejemplos de Context7.
- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para capturas, formularios, scraping y QA web.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspecciona fallos de GitHub Actions y convierte los logs en un plan de correccion.

## Inicio Rapido En 1 Minuto

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Despues de clonar, el repositorio quedara en `~/.agents/skills/ok-skills`, y los directorios internos ya siguen la estructura esperada:

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

Anade reglas de activacion simples a tu `AGENTS.md`:

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

### Planificacion y Prompting

- [brainstorming](brainstorming/SKILL.md): aclara ideas, requisitos y diseno antes de empezar la implementacion.
- [planning-with-files](planning-with-files/SKILL.md): planificacion persistente en Markdown con `task_plan.md`, `findings.md` y `progress.md`.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): encuentra oportunidades de deepening que mejoran locality, leverage, testabilidad y navegacion por IA.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): migra assertions de tipo `as` en tests a `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): red-green-refactor test-first para funcionalidades, correcciones, refactors y cambios de comportamiento.
- [systematic-debugging](systematic-debugging/SKILL.md): investiga la causa raiz de bugs, tests fallidos o comportamientos inesperados antes de proponer arreglos.

### Flujo De Trabajo En GitHub

- [gh-address-comments](gh-address-comments/SKILL.md): gestiona comentarios de revision e incidencias en la PR actual usando `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspecciona checks fallidos de GitHub Actions, resume logs y planifica la solucion.
- [yeet](yeet/SKILL.md): usala solo cuando el usuario pida explicitamente hacer stage, commit, push y abrir una pull request en un unico flujo con `gh`.

### Automatizacion y QA

- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para navegacion, formularios, capturas y scraping.
- [browser-use](browser-use/SKILL.md): CLI de automatizacion persistente del navegador para navegacion, inspeccion del estado de la pagina, formularios, capturas y extraccion.
- [opencli](opencli/opencli-usage/SKILL.md): convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.
- [dogfood](dogfood/SKILL.md): pruebas exploratorias estructuradas con evidencia reproducible.
- [electron](electron/SKILL.md): automatiza aplicaciones Electron mediante Chrome DevTools Protocol.

`dogfood/` y `electron/` siguen vendorizados desde `vercel-labs/agent-browser`, pero upstream los movio de `skills/` a `skill-data/` en el commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` para que la deteccion del instalador solo exponga el skill bootstrap `agent-browser`. Este repositorio mantiene esos skills especializados como directorios de nivel superior porque upstream todavia los mantiene y siguen siendo utiles de forma directa.


### Frontend y Diseno

- [ai-elements](ai-elements/SKILL.md): crea componentes de interfaz conversacional para la libreria `ai-elements`.
- [frontend-skill](frontend-skill/SKILL.md): usalo cuando necesites una landing page, sitio web, app, prototipo, demo o UI de juego con gran impacto visual.
- [shader-dev](shader-dev/SKILL.md): tecnicas GLSL completas para efectos visuales en tiempo real compatibles con ShaderToy.
- [better-icons](better-icons/SKILL.md): busca, explora y obtiene iconos SVG de mas de 200 bibliotecas de Iconify mediante CLI o MCP.
- [`gsap-skills/`](gsap-skills/): 8 skills oficiales de animacion GSAP (core, timelines, ScrollTrigger, plugins, utils, React, rendimiento, frameworks).

### Utilidades y Creacion De Contenido

- [minimax-docx](minimax-docx/SKILL.md): creacion, edicion y formateo profesional de DOCX con OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): genera, rellena y remaqueta documentos PDF con un sistema de diseno basado en tokens.
- [pptx-generator](pptx-generator/SKILL.md): genera, edita y lee presentaciones PowerPoint con PptxGenJS, flujos XML o markitdown.
- [minimax-xlsx](minimax-xlsx/SKILL.md): abre, crea, lee, analiza, edita y valida archivos Excel/hojas de calculo con un flujo XML de baja perdida.

## Paquetes De Skills Vendorizados

[`gsap-skills/`](gsap-skills/) contiene un paquete centrado en animacion, vendorizado desde [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) en el commit `aed9cfd3277740755f6bfc1155c7aa645403b760`.

Incluye:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

La atribucion y los archivos legales se conservan en [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) y [`gsap-skills/LICENSE`](gsap-skills/LICENSE).

[`planning-with-files/`](planning-with-files/) usa [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files) como baseline upstream. Este repositorio conserva el nombre generico `planning-with-files` y elimina metadatos de paquete especificos de Pi para mantener compatibilidad con flujos `SKILL.md` estandar.

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
| [ai-elements](ai-elements/SKILL.md)                                 | Crea nuevos componentes de chat con IA para la libreria ai-elements con patrones componibles y convenciones de shadcn/ui.                                                                                           | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | Busca en mas de 200 bibliotecas de Iconify y obtiene iconos SVG mediante CLI o herramientas MCP.                                                                                                                    | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | Convierte ideas en disenos y especificaciones validadas mediante dialogo colaborativo antes de implementar.                                                                               | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | CLI de automatizacion persistente del navegador para navegacion, inspeccion del estado de la pagina, formularios, capturas y extraccion.                                                                            | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | Modo de comunicacion ultra comprimido que reduce tokens de respuesta hablando como cavernicola sin perder precision tecnica.                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [find-docs](find-docs/SKILL.md)                                     | Usa Context7 CLI para consultar documentacion actual, referencias de API y ejemplos de codigo.                                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | Creacion, edicion y formateo profesional de DOCX con OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Usa Exa para investigacion web, de codigo y de empresas.                                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Descubre skills existentes cuando los usuarios necesitan capacidades especializadas.                                                                                                                                | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Crea landing pages, sitios web, apps, prototipos, demos o UIs de juego con gran impacto visual.                                                                                                                     | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Tecnicas GLSL completas para efectos visuales en tiempo real compatibles con ShaderToy. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Obtiene la documentacion actual de APIs o SDK de terceros antes de escribir codigo.                                                                                                                                 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Responde a comentarios de revision y de issues en la rama actual con `gh`.                                                                                                                                          | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspecciona fallos de GitHub Actions, descarga logs y prepara un plan de correccion.                                                                                                                                | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Encuentra oportunidades de deepening que mejoran locality, leverage, testabilidad y navegacion por IA.                                                                                                            | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture)                              |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migra archivos de test desde assertions de tipo `as` a `@total-typescript/shoehorn`.                                                                                                                            | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/migrate-to-shoehorn)                                        |
| [opensrc](opensrc/SKILL.md)                                         | Obtiene el codigo fuente de dependencias para dar a los agentes de IA un contexto de implementacion mas profundo.                                                                                                  | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.                                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | Prueba aplicaciones web de forma sistematica y produce reportes de incidencias reproducibles con capturas y videos.                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | Automatiza aplicaciones Electron mediante agent-browser y Chrome DevTools Protocol.                                                                                                                                 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | Genera, rellena y remaqueta documentos PDF con un sistema de diseno basado en tokens. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | Planificacion basada en archivos para tareas complejas mediante `task_plan.md`, `findings.md` y `progress.md`.                                                                                                      | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | Genera, edita y lee presentaciones PowerPoint con PptxGenJS, flujos XML o markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | Usala antes de funcionalidades, correcciones, refactors o cambios de comportamiento; prefiere pruebas de integracion via interfaces publicas.                                                                       | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Usala cuando encuentres cualquier bug, test fallido o comportamiento inesperado, antes de proponer arreglos.                                                                              | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Abre, crea, lee, analiza, edita y valida archivos Excel/hojas de calculo con un flujo XML de baja perdida. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Usala solo cuando el usuario pida explicitamente hacer stage, commit, push y abrir una pull request en un unico flujo con `gh`.                                                                                     | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

Notas:
- `dogfood` y `electron` vienen del `skill-data/` de upstream, no del `skills/`.
- Upstream movio estos skills especializados en el commit `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` para que la deteccion del instalador solo encuentre el skill bootstrap `agent-browser`.
- Este repositorio los conserva a proposito como skills vendorizados de nivel superior porque upstream sigue manteniendolos y siguen siendo utiles directamente.

### Skills Vendorizadas De `gsap-skills/`

| Skill                                                         | Descripcion                                                                                     | Source URL                                                                                            |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | API core: `gsap.to()` / `from()` / `fromTo()`, easing, duration, stagger, defaults, matchMedia. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timelines: secuenciacion, parametro position, labels, anidacion, control de reproduccion.       | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: animacion ligada al scroll, pinning, scrub, triggers, refresh, cleanup.          | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | Plugins: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase y mas.                         | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | Helpers de gsap.utils: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe.           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React: useGSAP, refs, `gsap.context()`, cleanup, SSR.                                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | Rendimiento: transforms, will-change, batching, tips de ScrollTrigger.                          | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue, Svelte, etc.: lifecycle, scope de selectores, cleanup al desmontar.                        | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## Contribuir

Se aceptan contribuciones para nuevas skills o para mejorar las existentes.

1. Mantén las condiciones de activacion explicitas y comprobables.
2. Mantén los ejemplos concisos y orientados a la ejecucion.
3. Si una skill depende de herramientas externas, documenta esa dependencia en `SKILL.md`.
4. Actualiza `README.md` y `README.zh-CN.md` cuando anadas o renombres una skill, y refresca las demas READMEs traducidas cuando cambie el indice publico de skills.

## Licencia

Este repositorio esta licenciado bajo [LICENSE](LICENSE).

Algunas skills incluyen archivos adicionales de licencia o avisos de atribucion para activos especificos, incluidos [`improve-codebase-architecture/`](improve-codebase-architecture/), [`migrate-to-shoehorn/`](migrate-to-shoehorn/), [`minimax-docx/`](minimax-docx/) y [`gsap-skills/`](gsap-skills/).
