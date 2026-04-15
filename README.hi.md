# OK Skills: Codex, Claude Code, Cursor, OpenClaw और अन्य टूल्स के लिए AI Coding Agent Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | हिन्दी

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Codex, Claude Code, Cursor, OpenClaw, Trae और अन्य `SKILL.md`-compatible टूल्स के लिए चुनी हुई AI coding agent skills और `AGENTS.md` playbooks का यह curated repository है।

इस repo में अभी **51 reusable skills** शामिल हैं: **25 top-level skills** सीधे इसी repo में maintain की जाती हैं, [`impeccable/`](impeccable/README.md) के अंतर्गत **18 vendored design skills** शामिल हैं, और [`gsap-skills/`](gsap-skills/) के अंतर्गत **8 vendored GSAP animation skills** शामिल हैं। इसे `~/.agents/skills/ok-skills` में clone करें; अंदर की directories पहले से ही `AGENTS.md`-driven workflows के अपेक्षित layout के अनुसार हैं।

अगर आप **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **AGENTS.md** playbooks, या practical **SKILL.md** examples खोज रहे हैं, तो यह repository खोजने में आसान और clone करते ही उपयोग योग्य होने के लिए व्यवस्थित की गई है।

**लोकप्रिय उपयोग परिदृश्य:** docs lookup, browser automation, GitHub Actions debugging, prompt engineering, planning workflows, frontend design, और PDF / Word / PPTX / XLSX authoring.

## यह Repo किनके लिए है

- आप Codex, Claude Code, Cursor, OpenClaw, Trae या किसी अन्य AI coding agent का उपयोग करते हैं और ad-hoc prompts की जगह reusable skills चाहते हैं।
- आप `AGENTS.md` / `SKILL.md` workflows maintain करते हैं और ऐसी portable instructions चाहते हैं जो कई projects में काम करें।
- आपको docs lookup, browser automation, GitHub workflow, planning, prompt engineering, frontend design, PDFs, Office documents, slide decks और spreadsheets के लिए battle-tested skills चाहिए।

## शुरुआत यहां से करें

अगर आप शुरुआत में केवल कुछ skills install करना चाहते हैं, तो इनसे शुरू करें:

- [brainstorming](brainstorming/SKILL.md): implementation शुरू होने से पहले ideas, requirements, aur design को clarify करें।
- [planning-with-files](planning-with-files/SKILL.md): complex tasks, research, और long-running work के लिए file-based planning.
- [context7-cli](context7-cli/SKILL.md): current library docs और Context7-backed references fetch करने के लिए।
- [agent-browser](agent-browser/SKILL.md): screenshots, forms, scraping, और web QA के लिए browser automation.
- [gh-fix-ci](gh-fix-ci/SKILL.md): failing GitHub Actions checks inspect करके logs को fix plan में बदलता है।
- [impeccable](impeccable/impeccable/SKILL.md): core impeccable design skill और companion design commands का पूरा bundle.

## 1-मिनट Quick Start

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Clone करने के बाद repo `~/.agents/skills/ok-skills` पर रहेगा, और अंदर की directories पहले से अपेक्षित layout का पालन करती हैं:

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

अपने `AGENTS.md` में simple trigger rules जोड़ें:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- context7-cli: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

फिर इसे natural language में trigger करें:

- `Use planning-with-files before refactoring this module.`
- `Use context7-cli to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## उपयोग-परिदृश्य के अनुसार Skills ब्राउज़ करें

### Research & Docs

- [context7-cli](context7-cli/SKILL.md): docs lookup, skill management, और MCP setup के लिए official Context7 CLI workflow.
- [exa-search](exa-search/SKILL.md): Exa search tools के साथ web, code, और company research.
- [get-api-docs](get-api-docs/SKILL.md): coding शुरू करने से पहले current third-party API और SDK documentation fetch करें।
- [find-skills](find-skills/SKILL.md): जब user किसी capability की मांग करे, तब existing skills खोजें।

### Planning & Prompting

- [brainstorming](brainstorming/SKILL.md): implementation शुरू होने से पहले ideas, requirements, aur design को clarify करें।
- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`, `findings.md`, और `progress.md` के साथ persistent markdown planning.
- [test-driven-development](test-driven-development/SKILL.md): implementation work से पहले tests लिखने को enforce करता है।

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): `gh` के साथ current PR पर review और issue comments address करें।
- [gh-fix-ci](gh-fix-ci/SKILL.md): failing GitHub Actions checks inspect करें, logs summarize करें, और fixes plan करें।
- [yeet](yeet/SKILL.md): केवल तब उपयोग करें जब user explicitly stage, commit, push, और GitHub pull request खोलने के लिए कहे।

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): navigation, forms, screenshots, और scraping के लिए browser automation.
- [browser-use](browser-use/SKILL.md): navigation, page state inspection, form filling, screenshots, और extraction के लिए persistent browser automation CLI.
- [opencli](opencli/opencli-usage/SKILL.md): browser login session reuse, public APIs, और AI-generated adapters के साथ websites को CLI commands में बदलें।

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): `ai-elements` library के लिए AI chat UI components बनाएं।
- [frontend-skill](frontend-skill/SKILL.md): जब आपको दृश्य रूप से मजबूत landing page, website, app, prototype, demo या game UI चाहिए तब उपयोग करें।
- [shader-dev](shader-dev/SKILL.md): ShaderToy-compatible real-time visuals ke liye comprehensive GLSL shader techniques.
- [better-icons](better-icons/SKILL.md): CLI या MCP के जरिए 200+ Iconify libraries में icons खोजें, browse करें, और SVG प्राप्त करें।
- [remotion-best-practices](remotion-best-practices/SKILL.md): React-based video work के लिए Remotion guidance.
- [`gsap-skills/`](gsap-skills/): core, timelines, ScrollTrigger, plugins, utils, React, performance, frameworks सहित 8 official GSAP animation skills.
- [`impeccable/`](impeccable/README.md): `impeccable`, `adapt`, `audit`, `polish` आदि सहित 18 vendored frontend design skills.

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): OpenXML SDK (.NET) ke saath professional DOCX creation, editing, aur formatting.
- [minimax-pdf](minimax-pdf/SKILL.md): token-based design system ke saath PDF documents generate, fill, aur reformat karein.
- [pptx-generator](pptx-generator/SKILL.md): PptxGenJS, XML workflows, ya markitdown ke saath PowerPoint presentations generate, edit, aur read karein.
- [minimax-xlsx](minimax-xlsx/SKILL.md): low-loss XML workflow ke saath Excel/spreadsheet files open, create, read, analyze, edit, aur validate karein.
- [skill-creator](skill-creator/SKILL.md): बेहतर structure और tool integrations के साथ skills create या update करें।

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) में [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) से लिया गया design-focused vendored bundle शामिल है, commit `00d485659af82982aef0328d0419c49a2716d123` पर आधारित।

इसमें शामिल हैं:

- `impeccable`: flagship frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `harden`, `layout`, `optimize`, `overdrive`, `polish`, `quieter`, `shape`, `typeset`

Attribution और legal files [`impeccable/NOTICE.md`](impeccable/NOTICE.md) और [`impeccable/LICENSE`](impeccable/LICENSE) में सुरक्षित रखे गए हैं।

[`gsap-skills/`](gsap-skills/) में [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) से लिया गया animation-focused vendored bundle शामिल है, commit `03d9f0c3dbf91e0b60582b64ed040c8911ca0174` पर आधारित।

इसमें शामिल हैं:

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

Attribution और legal files [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) और [`gsap-skills/LICENSE`](gsap-skills/LICENSE) में सुरक्षित रखे गए हैं।

## सामान्य prerequisites

- कुछ skills मानकर चलती हैं कि `gh` installed और authenticated है।
- Browser-focused skills के लिए Chrome/CDP-capable environment की आवश्यकता हो सकती है।
- Third-party doc lookup skills external CLIs या MCP tools पर निर्भर हो सकती हैं; विवरण के लिए संबंधित `SKILL.md` देखें।

## पूरा Skill Index

`Source URL` उस skill के canonical upstream को point करता है जब skill vendored/imported हो; अन्यथा यह इस repository के skill directory को point करता है।

### Top-Level Skills

| Skill                                                               | विवरण                                                                                                                                                                                        | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | AI agents के लिए browser automation CLI: navigation, form filling, screenshots, extraction, और web testing.                                                                                  | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | composable patterns और shadcn/ui conventions के साथ ai-elements library के लिए नए AI chat interface components बनाएं।                                                                        | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | CLI या MCP tools के जरिए 200+ Iconify libraries खोजें और SVG icons प्राप्त करें।                                                                                                             | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | Collaborative dialogue ke through implementation se pehle ideas ko validated design aur spec mein badalta hai.                                                                          | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | navigation, page state inspection, form filling, screenshots, और extraction के लिए persistent browser automation CLI.                                                                        | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | Ultra-compressed communication mode jo caveman style me bolkar response tokens kam karta hai aur technical accuracy banaye rakhta hai.                                                       | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [context7-cli](context7-cli/SKILL.md)                               | docs lookup, skill management, और MCP setup के लिए Context7 CLI का उपयोग करें।                                                                                                               | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | OpenXML SDK (.NET) ke saath professional DOCX creation, editing, aur formatting. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | web, code, और company research के लिए Exa का उपयोग करें।                                                                                                                                     | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | जब users को specialized capabilities चाहिए हों, तब existing skills खोजें।                                                                                                                    | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | दृश्य रूप से मजबूत landing page, website, app, prototype, demo या game UI बनाएं।                                                                                                             | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | ShaderToy-compatible real-time visuals ke liye comprehensive GLSL shader techniques. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | code लिखने से पहले current third-party API या SDK docs fetch करें।                                                                                                                           | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | current branch पर PR review और issue comments को `gh` के साथ address करें।                                                                                                                   | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | failing GitHub Actions checks inspect करें, logs pull करें, और fixes plan करें।                                                                                                              | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | Dependency source code fetch karke AI agents ko deeper implementation context dena.                                                                                                          | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Browser login session reuse, public APIs, और AI-generated adapters के साथ websites को CLI commands में बदलने की skill.                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [minimax-pdf](minimax-pdf/SKILL.md) | Token-based design system ke saath PDF documents generate, fill, aur reformat karein. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | `task_plan.md`, `findings.md`, और `progress.md` का उपयोग करके complex tasks के लिए file-based planning.                                                                                      | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | PptxGenJS, XML workflows, ya markitdown ke saath PowerPoint presentations generate, edit, aur read karein. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | React के साथ videos बनाने के लिए Remotion best practices.                                                                                                                                    | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | specialized knowledge और tool integrations के साथ skills create या update करने की guide.                                                                                                     | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [test-driven-development](test-driven-development/SKILL.md)         | किसी भी feature या bugfix को implement करने से पहले उपयोग करें।                                                                                                                              | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Low-loss XML workflow ke saath Excel/spreadsheet files open, create, read, analyze, edit, aur validate karein. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | केवल तब उपयोग करें जब user explicitly `gh` के साथ stage, commit, push, और GitHub pull request खोलने को कहे।                                                                                  | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

### Vendored `impeccable/` Skills

| Skill                                                    | विवरण                                                                                          | Source URL                                                  |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [impeccable](impeccable/impeccable/SKILL.md)   | उच्च पहचान और production-grade quality के साथ frontend interfaces बनाएं।                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md)                       | designs को अलग-अलग screen sizes, devices, और contexts के लिए adapt करें।                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md)                   | purposeful motion और micro-interactions जोड़ें।                                                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md)                       | accessibility, performance, theming, और responsive design के पार interface quality audit करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md)                     | safe या boring designs को और अधिक visually interesting बनाएं।                                  | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md)                   | अस्पष्ट UX copy और instructions को बेहतर बनाएं।                                                | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md)                 | बहुत अधिक monochrome features में strategic color जोड़ें।                                      | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md)                 | UX perspective से design effectiveness evaluate करें।                                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md)                   | interfaces में personality और memorable touches जोड़ें।                                        | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md)                   | designs को उनकी essential form तक simplify करें।                                               | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md)                     | errors, i18n, overflow, और edge cases के आसपास resilience बढ़ाएं।                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [layout](impeccable/layout/SKILL.md)                       | लेआउट, स्पेसिंग और विजुअल रिद्म को बेहतर बनाएं।                                            | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | frontend performance, rendering, motion, और bundle efficiency सुधारें।                         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [overdrive](impeccable/overdrive/SKILL.md)                 | तकनीकी रूप से महत्वाकांक्षी इम्प्लीमेंटेशन के साथ इंटरफेस को पारंपरिक सीमाओं से आगे ले जाएं। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | alignment, spacing, consistency, और detail के लिए final quality pass.                          | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | quality बरकरार रखते हुए visual aggression कम करें।                                             | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [shape](impeccable/shape/SKILL.md)                         | कोड लिखने से पहले किसी फीचर की UX और UI योजना बनाएं।                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [typeset](impeccable/typeset/SKILL.md)                     | फ़ॉन्ट चयन, hierarchy, sizing, weight और readability को सुधारकर typography बेहतर बनाएं।    | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

### Vendored `gsap-skills/` Skills

| Skill                                                         | विवरण                                                                                           | Source URL                                                                                            |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | Core API: `gsap.to()` / `from()` / `fromTo()`, easing, duration, stagger, defaults, matchMedia. | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timelines: sequencing, position parameter, labels, nesting, playback.                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger: scroll-linked animation, pinning, scrub, triggers, refresh, cleanup.             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | Plugins: Flip, Draggable, MotionPath, ScrollToPlugin, CustomEase, और अधिक.                      | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils helpers: clamp, mapRange, normalize, random, snap, toArray, wrap, pipe.              | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React: useGSAP, refs, `gsap.context()`, cleanup, SSR.                                           | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | Performance tips: transforms, will-change, batching, ScrollTrigger tips.                        | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue, Svelte, और अन्य frameworks: lifecycle, selector scoping, unmount cleanup.                  | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## Contributing

नई skills या existing skills में improvements के लिए contributions का स्वागत है।

1. Trigger conditions स्पष्ट और testable रखें।
2. Examples concise और execution-oriented रखें।
3. अगर कोई skill external tools पर निर्भर है, तो उस dependency को `SKILL.md` में document करें।
4. जब आप किसी skill को add या rename करें, तो `README.md` और `README.zh-CN.md` अपडेट करें, और public-facing skill index बदलने पर बाकी translated READMEs भी refresh करें।

## License

यह repository [LICENSE](LICENSE) के अंतर्गत licensed है।

कुछ skills में skill-specific assets और attribution के लिए अतिरिक्त license files या notices शामिल हैं, जिनमें [`minimax-docx/`](minimax-docx/), [`impeccable/`](impeccable/README.md), [`gsap-skills/`](gsap-skills/), और [`skill-creator/`](skill-creator/) शामिल हैं।
