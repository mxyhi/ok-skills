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

### Planificacion y Prompting

- [planning-with-files](planning-with-files/SKILL.md): planificacion persistente en Markdown con `task_plan.md`, `findings.md` y `progress.md`.
- [autoresearch](autoresearch/SKILL.md): iteracion autonoma orientada a objetivos con metas, metricas, ciclos de verificacion y compuertas keep/discard.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): bucle disciplinado de diagnostico para bugs dificiles y regresiones de rendimiento.
- [grill-with-docs](grill-with-docs/SKILL.md): valida planes contra lenguaje de dominio, `CONTEXT.md` y ADRs, actualizando docs inline.
- [grilling](grilling/SKILL.md): bucle reutilizable de entrevista pregunta por pregunta para sesiones grill directas y `grill-with-docs`.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): encuentra oportunidades de deepening que mejoran locality, leverage, testabilidad y navegacion por IA.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): pautas de conducta al programar para reducir sobrecomplicacion, supuestos ocultos y cambios no verificables.
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): migra assertions de tipo `as` en tests a `@total-typescript/shoehorn`.
- [tdd](tdd/SKILL.md): red-green-refactor test-first para funcionalidades, correcciones, refactors y cambios de comportamiento.
- [systematic-debugging](systematic-debugging/SKILL.md): investiga la causa raiz de bugs, tests fallidos o comportamientos inesperados antes de proponer arreglos.

### Automatizacion y QA

- [agent-browser](agent-browser/SKILL.md): automatizacion de navegador para navegacion, formularios, capturas y scraping.
- [kimi-webbridge](kimi-webbridge/SKILL.md): controla el navegador real del usuario mediante un daemon local para navegacion, formularios, capturas, lectura de paginas y sesiones autenticadas.
- [browser-trace](browser-trace/SKILL.md): captura trazas CDP, capturas de pantalla y dumps DOM para depurar automatizacion del navegador.
- [opencli](opencli/opencli-usage/SKILL.md): convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.
- [xquik-twitter](xquik-twitter/SKILL.md): busca datos de X/Twitter y ejecuta acciones de cuenta confirmadas mediante la API de Xquik.

### Frontend y Diseno

- [ai-elements](ai-elements/SKILL.md): crea componentes de interfaz conversacional para la libreria `ai-elements`.
- [huashu-design](huashu-design/SKILL.md): crea prototipos HTML de alta fidelidad, demos interactivas, decks, motion design, variantes, exportes de video y criticas de diseno.
- [better-icons](better-icons/SKILL.md): busca, explora y obtiene iconos SVG de mas de 200 bibliotecas de Iconify mediante CLI o MCP.

### Utilidades y Creacion De Contenido

- [minimax-docx](minimax-docx/SKILL.md): creacion, edicion y formateo profesional de DOCX con OpenXML SDK (.NET).
- [minimax-pdf](minimax-pdf/SKILL.md): genera, rellena y remaqueta documentos PDF con un sistema de diseno basado en tokens.
- [pptx-generator](pptx-generator/SKILL.md): genera, edita y lee presentaciones PowerPoint con PptxGenJS, flujos XML o markitdown.
- [huashu-design](huashu-design/SKILL.md): produce HTML decks, PPTX editables, piezas MP4/GIF y videos de diseno narrados.
- [minimax-xlsx](minimax-xlsx/SKILL.md): abre, crea, lee, analiza, edita y valida archivos Excel/hojas de calculo con un flujo XML de baja perdida.

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
| [ai-elements](ai-elements/SKILL.md)                                 | Crea nuevos componentes de chat con IA para la libreria ai-elements con patrones componibles y convenciones de shadcn/ui.                                                                                           | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [autoresearch](autoresearch/SKILL.md)                               | Motor de iteracion autonoma orientada a objetivos para flujos de modificar, verificar, conservar/descartar y repetir.                                                                    | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | Busca en mas de 200 bibliotecas de Iconify y obtiene iconos SVG mediante CLI o herramientas MCP.                                                                                                                    | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | Controla el navegador real del usuario mediante un daemon local para navegacion, formularios, capturas, lectura de paginas y sesiones autenticadas.                                                                 | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | Captura trazas CDP, capturas de pantalla y dumps DOM para depurar automatizacion del navegador.                                                                    | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | Modo de comunicacion ultra comprimido que reduce tokens de respuesta hablando como cavernicola sin perder precision tecnica.                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | Bucle disciplinado de diagnostico para bugs dificiles y regresiones de rendimiento.                                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | Usa Context7 CLI para consultar documentacion actual, referencias de API y ejemplos de codigo.                                                                                                                     | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | Creacion, edicion y formateo profesional de DOCX con OpenXML SDK (.NET). | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | Usa Exa para investigacion web, de codigo y de empresas.                                                                                                                                                            | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | Descubre skills existentes cuando los usuarios necesitan capacidades especializadas.                                                                                                                                | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | Crea prototipos HTML de alta fidelidad, demos interactivas, decks, motion design, variantes, exportes de video y criticas de diseno.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | Obtiene la documentacion actual de APIs o SDK de terceros antes de escribir codigo.                                                                                                                                 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | Stress-test de planes contra lenguaje de dominio, `CONTEXT.md` y ADRs, con actualizacion inline de docs.                                             | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [grilling](grilling/SKILL.md)                               | Bucle reutilizable de entrevista pregunta por pregunta para sesiones grill directas y `grill-with-docs`.                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | Encuentra oportunidades de deepening que mejoran locality, leverage, testabilidad y navegacion por IA.                                                                                                            | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Pautas de conducta al programar para reducir sobrecomplicacion, supuestos ocultos y cambios no verificables.                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | Migra archivos de test desde assertions de tipo `as` a `@total-typescript/shoehorn`.                                                                                                                            | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Convierte sitios web en comandos CLI con reutilizacion de sesion del navegador, APIs publicas y adaptadores generados por IA.                                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [xquik-twitter](xquik-twitter/SKILL.md)                         | Busca datos de X/Twitter y ejecuta acciones de cuenta confirmadas mediante la API de Xquik.                                                                                               | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)             |
| [minimax-pdf](minimax-pdf/SKILL.md) | Genera, rellena y remaqueta documentos PDF con un sistema de diseno basado en tokens. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | Planificacion basada en archivos para tareas complejas mediante `task_plan.md`, `findings.md` y `progress.md`.                                                                                                      | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | Genera, edita y lee presentaciones PowerPoint con PptxGenJS, flujos XML o markitdown. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | Usala antes de funcionalidades, correcciones, refactors o cambios de comportamiento; prefiere pruebas de integracion via interfaces publicas.                                                                       | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | Usala cuando encuentres cualquier bug, test fallido o comportamiento inesperado, antes de proponer arreglos.                                                                              | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Abre, crea, lee, analiza, edita y valida archivos Excel/hojas de calculo con un flujo XML de baja perdida. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
## Contribuir

Se aceptan contribuciones para nuevas skills o para mejorar las existentes.

1. Mantén las condiciones de activacion explicitas y comprobables.
2. Mantén los ejemplos concisos y orientados a la ejecucion.
3. Si una skill depende de herramientas externas, documenta esa dependencia en `SKILL.md`.
4. Actualiza `README.md` y `README.zh-CN.md` cuando anadas o renombres una skill, y refresca las demas READMEs traducidas cuando cambie el indice publico de skills.

## Licencia

Este repositorio esta licenciado bajo [LICENSE](LICENSE).
