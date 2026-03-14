# OK Skills: skills de agentes de programacion con IA para Codex, Claude Code, Cursor, OpenClaw y mas

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | Español | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

Coleccion curada de skills para agentes de programacion con IA y playbooks de `AGENTS.md` para Codex, Claude Code, Cursor, OpenClaw, Trae y otras herramientas compatibles con `SKILL.md`.

Este repositorio incluye actualmente **41 skills reutilizables**: **23 skills de nivel superior** mantenidos directamente aqui, ademas de **18 skills de diseno** integradas como paquete vendorizado en [`impeccable/`](impeccable/README.md). Clonalo en `~/.agents/skills/ok-skills`; los directorios internos ya siguen la estructura esperada por los flujos basados en `AGENTS.md`.

Si estas buscando **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, playbooks reutilizables de **AGENTS.md** o ejemplos practicos de **SKILL.md**, este repositorio esta organizado para ser facil de encontrar y facil de usar desde el primer clon.

**Casos de uso frecuentes:** consulta de documentacion actual, automatizacion de navegador, depuracion de GitHub Actions, prompt engineering, planificacion de tareas complejas, diseno frontend y trabajo con PDF / Word / PPTX / XLSX.

## Para Quien Es Este Repositorio

- Usas Codex, Claude Code, Cursor, OpenClaw, Trae u otro agente de programacion con IA y quieres reutilizar skills en lugar de depender de prompts improvisados.
- Mantienes flujos con `AGENTS.md` / `SKILL.md` y quieres instrucciones portables que funcionen entre distintos proyectos.
- Necesitas skills probadas para busqueda de documentacion, automatizacion de navegador, flujo de GitHub, planificacion, prompt engineering, frontend, PDF, documentos de Office, presentaciones y hojas de calculo.

## Empieza Por Aqui

Si al principio solo vas a instalar unas pocas skills, empieza por estas:

- [planning-with-files](planning-with-files/SKILL.md): planificacion basada en archivos para tareas complejas, investigacion y trabajo de larga duracion.
- [context7-cli](context7-cli/SKILL.md): consulta documentacion actual de librerias y referencias respaldadas por Context7.
- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para capturas, formularios, scraping y QA web.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspecciona fallos de GitHub Actions y convierte los logs en un plan de correccion.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): patrones de prompt orientados a produccion para flujos con LLM mas fiables.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): skill de frontend de alta calidad junto con un paquete completo de comandos de diseno complementarios.

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

- [brainstorming](brainstorming/SKILL.md): aclara la intencion, los requisitos y el diseno antes de implementar.
- [planning-with-files](planning-with-files/SKILL.md): planificacion persistente en Markdown con `task_plan.md`, `findings.md` y `progress.md`.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): patrones avanzados de prompt para sistemas LLM en produccion.
- [test-driven-development](test-driven-development/SKILL.md): obliga a escribir pruebas antes de implementar.

### Flujo De Trabajo En GitHub

- [gh-address-comments](gh-address-comments/SKILL.md): gestiona comentarios de revision e incidencias en la PR actual usando `gh`.
- [gh-fix-ci](gh-fix-ci/SKILL.md): inspecciona checks fallidos de GitHub Actions, resume logs y planifica la solucion.
- [yeet](yeet/SKILL.md): usala solo cuando el usuario pida explicitamente hacer stage, commit, push y abrir una pull request en un unico flujo con `gh`.

### Automatizacion y QA

- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para navegacion, formularios, capturas y scraping.
- [pinchtab](pinchtab/SKILL.md): controla Chrome mediante la API HTTP local de Pinchtab usando referencias de accesibilidad estables.
- [electron](electron/SKILL.md): automatiza aplicaciones Electron mediante Chrome DevTools Protocol.
- [dogfood](dogfood/SKILL.md): pruebas exploratorias estructuradas con evidencia reproducible.

### Frontend y Diseno

- [ai-elements](ai-elements/SKILL.md): crea componentes de interfaz conversacional para la libreria `ai-elements`.
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): recomendaciones de rendimiento para React y Next.js de Vercel Engineering.
- [remotion-best-practices](remotion-best-practices/SKILL.md): guia de Remotion para trabajo de video basado en React.
- [`impeccable/`](impeccable/README.md): 18 skills de diseno frontend vendorizadas, incluidas `frontend-design`, `adapt`, `audit`, `polish` y mas.

### Utilidades y Creacion De Contenido

- [docx](docx/SKILL.md): crea, lee, edita y manipula documentos de Word con formato, comentarios y control de cambios.
- [pdf](pdf/SKILL.md): lee, crea y revisa PDF con validaciones conscientes del renderizado.
- [pptx](pptx/SKILL.md): crea, lee, edita y manipula presentaciones, plantillas y contenido de diapositivas.
- [xlsx](xlsx/SKILL.md): creacion, edicion, formulas y analisis de hojas de calculo.
- [skill-creator](skill-creator/SKILL.md): crea o actualiza skills con mejor estructura e integraciones de herramientas.

## Paquetes De Skills Vendorizados

[`impeccable/`](impeccable/README.md) contiene un paquete centrado en diseno, vendorizado desde [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) en el commit `0df1ba59dc80b8b1891ee42eed0ef4e03d7ef165`.

Incluye:

- `frontend-design`: la skill principal de diseno frontend
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

La atribucion y los archivos legales se conservan en [`impeccable/NOTICE.md`](impeccable/NOTICE.md) y [`impeccable/LICENSE`](impeccable/LICENSE).

## Requisitos Habituales

- Algunas skills asumen que `gh` esta instalado y autenticado.
- Las skills centradas en navegador pueden requerir un entorno compatible con Chrome/CDP.
- Las skills de consulta de documentacion de terceros pueden depender de CLI externas o herramientas MCP; revisa cada `SKILL.md` para los detalles.

## Indice Completo De Skills

`Source URL` apunta al upstream canonico cuando una skill fue importada o vendorizada; en caso contrario, apunta al directorio de la skill dentro de este repositorio.

### Skills De Nivel Superior

| Skill | Descripcion | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | CLI de automatizacion de navegador para agentes de IA: navegacion, formularios, capturas, extraccion y pruebas web. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | Crea nuevos componentes de chat con IA para la libreria ai-elements con patrones componibles y convenciones de shadcn/ui. | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [brainstorming](brainstorming/SKILL.md) | Aclara la intencion, los requisitos y el diseno antes de implementar. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [context7-cli](context7-cli/SKILL.md) | Usa Context7 CLI para buscar documentacion, gestionar skills y configurar MCP. | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | Crea, lee, edita y manipula documentos de Word con formato, comentarios, control de cambios y actualizacion de imagenes. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | Prueba aplicaciones web de forma sistematica y produce reportes de incidencias reproducibles con capturas y videos. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | Automatiza aplicaciones Electron mediante agent-browser y Chrome DevTools Protocol. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | Usa Exa para investigacion web, de codigo y de empresas. | Custom |
| [find-skills](find-skills/SKILL.md) | Descubre skills existentes cuando los usuarios necesitan capacidades especializadas. | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | Obtiene la documentacion actual de APIs o SDK de terceros antes de escribir codigo. | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | Responde a comentarios de revision y de issues en la rama actual con `gh`. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | Inspecciona fallos de GitHub Actions, descarga logs y prepara un plan de correccion. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [pdf](pdf/SKILL.md) | Lee, crea y revisa archivos PDF con comprobaciones de renderizado y herramientas en Python. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | Controla Chrome en modo headless o con interfaz mediante la API HTTP de Pinchtab para automatizacion web, scraping, formularios, navegacion, capturas y extraccion basada en referencias de accesibilidad estables. | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skill/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | Planificacion basada en archivos para tareas complejas mediante `task_plan.md`, `findings.md` y `progress.md`. | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.agent/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | Crea, lee, edita y manipula presentaciones de PowerPoint, plantillas, layouts, notas y contenido de diapositivas. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | Patrones avanzados de prompt engineering para flujos LLM fiables y orientados a produccion. | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | Buenas practicas para crear videos en React con Remotion. | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | Guia para crear o actualizar skills con conocimiento especializado e integraciones de herramientas. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [test-driven-development](test-driven-development/SKILL.md) | Usala antes de implementar cualquier funcionalidad o correccion. | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | Guia de optimizacion de rendimiento para React y Next.js desde Vercel Engineering. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | Creacion, edicion, formulas, formato y analisis de hojas de calculo. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | Usala solo cuando el usuario pida explicitamente hacer stage, commit, push y abrir una pull request en un unico flujo con `gh`. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### Skills Vendorizadas De `impeccable/`

| Skill | Descripcion | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | Crea interfaces frontend distintivas y listas para produccion con alta calidad de diseno. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | Adapta disenos a distintos tamanos de pantalla, dispositivos y contextos. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | Anade movimiento intencional y microinteracciones. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | Audita la calidad de interfaces en accesibilidad, rendimiento, tematizacion y diseno responsive. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | Hace que disenos demasiado seguros o planos resulten mas interesantes visualmente. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | Mejora textos e instrucciones UX poco claros. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | Anade color estrategico a interfaces demasiado monocromaticas. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | Evalua la efectividad del diseno desde una perspectiva UX. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | Anade personalidad y momentos memorables a las interfaces. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | Reduce los disenos a su forma esencial. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | Consolida componentes, tokens y patrones reutilizables en un sistema de diseno. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | Refuerza la resiliencia ante errores, i18n, desbordes y casos limite. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | Normaliza una funcionalidad para alinearla con un sistema de diseno. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | Disena o mejora la incorporacion, los estados vacios y la primera experiencia de uso. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | Mejora rendimiento frontend, renderizado, movimiento y eficiencia del bundle. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | Hace el pulido final de alineacion, espaciado, consistencia y detalle. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | Reduce la agresividad visual sin perder calidad de diseno. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | Reune contexto de diseno y lo guarda como guia persistente para el trabajo futuro. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## Contribuir

Se aceptan contribuciones para nuevas skills o para mejorar las existentes.

1. Mantén las condiciones de activacion explicitas y comprobables.
2. Mantén los ejemplos concisos y orientados a la ejecucion.
3. Si una skill depende de herramientas externas, documenta esa dependencia en `SKILL.md`.
4. Actualiza `README.md` y `README.zh-CN.md` cuando anadas o renombres una skill, y refresca las demas READMEs traducidas cuando cambie el indice publico de skills.

## Licencia

Este repositorio esta licenciado bajo [LICENSE](LICENSE).

Algunas skills incluyen archivos adicionales de licencia o avisos de atribucion para activos especificos, incluidos [`docx/`](docx/), [`pptx/`](pptx/), [`impeccable/`](impeccable/README.md), [`skill-creator/`](skill-creator/) y [`xlsx/`](xlsx/).
