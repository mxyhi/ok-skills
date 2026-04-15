# OK Skills: skills de agentes de programacion con IA para Codex, Claude Code, Cursor, OpenClaw y mas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | Español | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Coleccion curada de skills para agentes de programacion con IA y playbooks de `AGENTS.md` para Codex, Claude Code, Cursor, OpenClaw, Trae y otras herramientas compatibles con `SKILL.md`.

Este repositorio incluye actualmente **53 skills reutilizables**: **27 skills de nivel superior** mantenidos directamente aqui, ademas de **18 skills de diseno** integradas como paquete vendorizado en [`impeccable/`](impeccable/README.md), y **8 skills de animacion GSAP** integradas como paquete vendorizado en [`gsap-skills/`](gsap-skills/). Clonalo en `~/.agents/skills/ok-skills`; los directorios internos ya siguen la estructura esperada por los flujos basados en `AGENTS.md`.

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
- [context7-cli](context7-cli/SKILL.md): consulta documentacion actual de librerias y referencias respaldadas por Context7.
- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para capturas, formularios, scraping y QA web.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspecciona fallos de GitHub Actions y convierte los logs en un plan de correccion.
- [impeccable](impeccable/impeccable/SKILL.md): skill central de impeccable junto con un paquete completo de comandos de diseno complementarios.

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
  context7-cli/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

Anade reglas de activacion simples a tu `AGENTS.md`:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- context7-cli: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

Despues puedes pedirlo de forma natural:

- `Use planning-with-files before refactoring this module.`
- `Use context7-cli to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## Explora Skills Por Caso De Uso

### Investigacion y Documentacion

- [context7-cli](context7-cli/SKILL.md): flujo oficial de Context7 CLI para buscar documentacion, gestionar skills y configurar MCP.
- [exa-search](exa-search/SKILL.md): investigacion web, de codigo y de empresas con herramientas de Exa.
- [get-api-docs](get-api-docs/SKILL.md): recupera la documentacion actual de APIs y SDK de terceros antes de programar.
- [find-skills](find-skills/SKILL.md): descubre skills existentes cuando un usuario pide una capacidad concreta.

### Planificacion y Prompting

- [brainstorming](brainstorming/SKILL.md): aclara ideas, requisitos y diseno antes de empezar la implementacion.
- [planning-with-files](planning-with-files/SKILL.md): planificacion persistente en Markdown con `task_plan.md`, `findings.md` y `progress.md`.
- [test-driven-development](test-driven-development/SKILL.md): obliga a escribir pruebas antes de implementar.

### Flujo De Trabajo En GitHub

- [gh-address-comments](gh-address-comments/SKILL.md): gestiona comentarios de revision e incidencias en la PR actual usando `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspecciona checks fallidos de GitHub Actions, resume logs y planifica la solucion.
- [yeet](yeet/SKILL.md): usala solo cuando el usuario pida explicitamente hacer stage, commit, push y abrir una pull request en un unico flujo con `gh`.

### Automatizacion y QA

- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para navegacion, formularios, capturas y scraping.
- [browser-use](browser-use/SKILL.md): CLI de automatizacion persistente del navegador para navegacion, inspeccion del estado de la pagina, formularios, capturas y extraccion.
- [opencli](opencli/opencli-usage/SKILL.md): convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.

### Frontend y Diseno

- [ai-elements](ai-elements/SKILL.md): crea componentes de interfaz conversacional para la libreria `ai-elements`.
- [frontend-skill](frontend-skill/SKILL.md): usalo cuando necesites una landing page, sitio web, app, prototipo, demo o UI de juego con gran impacto visual.
- [shader-dev](shader-dev/SKILL.md): tecnicas GLSL completas para efectos visuales en tiempo real compatibles con ShaderToy.
- [better-icons](better-icons/SKILL.md): busca, explora y obtiene iconos SVG de mas de 200 bibliotecas de Iconify mediante CLI o MCP.
- [remotion-best-practices](remotion-best-practices/SKILL.md): guia de Remotion para trabajo de video basado en React.
- [`gsap-skills/`](gsap-skills/): 8 skills oficiales de animacion GSAP (core, timelines, ScrollTrigger, plugins, utils, React, rendimiento, frameworks).
- [`impeccable/`](impeccable/README.md): 18 skills de diseno frontend vendorizadas, incluidas `impeccable`, `adapt`, `audit`, `polish` y mas.

### Utilidades y Creacion De Contenido

- [minimax-docx](minimax-docx/SKILL.md): creacion, edicion y formateo profesional de DOCX con OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): genera, rellena y remaqueta documentos PDF con un sistema de diseno basado en tokens.
- [pptx-generator](pptx-generator/SKILL.md): genera, edita y lee presentaciones PowerPoint con PptxGenJS, flujos XML o markitdown.
- [minimax-xlsx](minimax-xlsx/SKILL.md): abre, crea, lee, analiza, edita y valida archivos Excel/hojas de calculo con un flujo XML de baja perdida.
- [skill-creator](skill-creator/SKILL.md): crea o actualiza skills con mejor estructura e integraciones de herramientas.

## Paquetes De Skills Vendorizados

[`impeccable/`](impeccable/README.md) contiene un paquete centrado en diseno, vendorizado desde [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) en el commit `00d485659af82982aef0328d0419c49a2716d123`.

Incluye:

- `impeccable`: la skill principal de diseno frontend
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `harden`, `layout`, `optimize`, `overdrive`, `polish`, `quieter`, `shape`, `typeset`

La atribucion y los archivos legales se conservan en [`impeccable/NOTICE.md`](impeccable/NOTICE.md) y [`impeccable/LICENSE`](impeccable/LICENSE).

[`gsap-skills/`](gsap-skills/) contiene un paquete centrado en animacion, vendorizado desde [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) en el commit `03d9f0c3dbf91e0b60582b64ed040c8911ca0174`.

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
| [context7-cli](context7-cli/SKILL.md)                               | Usa Context7 CLI para buscar documentacion, gestionar skills y configurar MCP.                                                                                                                                      | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | Creacion, edicion y formateo profesional de DOCX con OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Usa Exa para investigacion web, de codigo y de empresas.                                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Descubre skills existentes cuando los usuarios necesitan capacidades especializadas.                                                                                                                                | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | Crea landing pages, sitios web, apps, prototipos, demos o UIs de juego con gran impacto visual.                                                                                                                     | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | Tecnicas GLSL completas para efectos visuales en tiempo real compatibles con ShaderToy. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | Obtiene la documentacion actual de APIs o SDK de terceros antes de escribir codigo.                                                                                                                                 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | Responde a comentarios de revision y de issues en la rama actual con `gh`.                                                                                                                                          | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | Inspecciona fallos de GitHub Actions, descarga logs y prepara un plan de correccion.                                                                                                                                | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | Obtiene el codigo fuente de dependencias para dar a los agentes de IA un contexto de implementacion mas profundo.                                                                                                  | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.                                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [minimax-pdf](minimax-pdf/SKILL.md) | Genera, rellena y remaqueta documentos PDF con un sistema de diseno basado en tokens. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | Planificacion basada en archivos para tareas complejas mediante `task_plan.md`, `findings.md` y `progress.md`.                                                                                                      | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | Genera, edita y lee presentaciones PowerPoint con PptxGenJS, flujos XML o markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | Buenas practicas para crear videos en React con Remotion.                                                                                                                                                           | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | Guia para crear o actualizar skills con conocimiento especializado e integraciones de herramientas.                                                                                                                 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [test-driven-development](test-driven-development/SKILL.md)         | Usala antes de implementar cualquier funcionalidad o correccion.                                                                                                                                                    | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Abre, crea, lee, analiza, edita y valida archivos Excel/hojas de calculo con un flujo XML de baja perdida. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | Usala solo cuando el usuario pida explicitamente hacer stage, commit, push y abrir una pull request en un unico flujo con `gh`.                                                                                     | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

### Skills Vendorizadas De `impeccable/`

| Skill                                                    | Descripcion                                                                                      | Source URL                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| [impeccable](impeccable/impeccable/SKILL.md)   | Crea interfaces frontend distintivas y listas para produccion con alta calidad de diseno.        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md)                       | Adapta disenos a distintos tamanos de pantalla, dispositivos y contextos.                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md)                   | Anade movimiento intencional y microinteracciones.                                               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md)                       | Audita la calidad de interfaces en accesibilidad, rendimiento, tematizacion y diseno responsive. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md)                     | Hace que disenos demasiado seguros o planos resulten mas interesantes visualmente.               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md)                   | Mejora textos e instrucciones UX poco claros.                                                    | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md)                 | Anade color estrategico a interfaces demasiado monocromaticas.                                   | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md)                 | Evalua la efectividad del diseno desde una perspectiva UX.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md)                   | Anade personalidad y momentos memorables a las interfaces.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md)                   | Reduce los disenos a su forma esencial.                                                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md)                     | Refuerza la resiliencia ante errores, i18n, desbordes y casos limite.                            | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [layout](impeccable/layout/SKILL.md)                       | Mejora el layout, el espaciado y el ritmo visual.                                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | Mejora rendimiento frontend, renderizado, movimiento y eficiencia del bundle.                    | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [overdrive](impeccable/overdrive/SKILL.md)                 | Lleva las interfaces mas alla de los limites convencionales con implementaciones tecnicamente ambiciosas. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | Hace el pulido final de alineacion, espaciado, consistencia y detalle.                           | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | Reduce la agresividad visual sin perder calidad de diseno.                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [shape](impeccable/shape/SKILL.md)                         | Planifica la UX y la UI de una funcionalidad antes de escribir codigo.                     | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [typeset](impeccable/typeset/SKILL.md)                     | Mejora la tipografia corrigiendo fuentes, jerarquia, tamanos, peso y legibilidad.          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

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

Algunas skills incluyen archivos adicionales de licencia o avisos de atribucion para activos especificos, incluidos [`minimax-docx/`](minimax-docx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), y [`skill-creator/`](skill-creator/).
