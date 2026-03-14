# OK Skills: Codex, Claude Code, Cursor, OpenClaw और अन्य टूल्स के लिए AI Coding Agent Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | हिन्दी

Codex, Claude Code, Cursor, OpenClaw, Trae और अन्य `SKILL.md`-compatible टूल्स के लिए चुनी हुई AI coding agent skills और `AGENTS.md` playbooks का यह curated repository है।

इस repo में अभी **42 reusable skills** शामिल हैं: **24 top-level skills** सीधे इसी repo में maintain की जाती हैं, और [`impeccable/`](impeccable/README.md) के अंतर्गत **18 vendored design skills** शामिल हैं। इसे `~/.agents/skills/ok-skills` में clone करें; अंदर की directories पहले से ही `AGENTS.md`-driven workflows के अपेक्षित layout के अनुसार हैं।

अगर आप **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **AGENTS.md** playbooks, या practical **SKILL.md** examples खोज रहे हैं, तो यह repository खोजने में आसान और clone करते ही उपयोग योग्य होने के लिए व्यवस्थित की गई है।

**लोकप्रिय उपयोग परिदृश्य:** docs lookup, browser automation, GitHub Actions debugging, prompt engineering, planning workflows, frontend design, और PDF / Word / PPTX / XLSX authoring.

## यह Repo किनके लिए है

- आप Codex, Claude Code, Cursor, OpenClaw, Trae या किसी अन्य AI coding agent का उपयोग करते हैं और ad-hoc prompts की जगह reusable skills चाहते हैं।
- आप `AGENTS.md` / `SKILL.md` workflows maintain करते हैं और ऐसी portable instructions चाहते हैं जो कई projects में काम करें।
- आपको docs lookup, browser automation, GitHub workflow, planning, prompt engineering, frontend design, PDFs, Office documents, slide decks और spreadsheets के लिए battle-tested skills चाहिए।

## शुरुआत यहां से करें

अगर आप शुरुआत में केवल कुछ skills install करना चाहते हैं, तो इनसे शुरू करें:

- [planning-with-files](planning-with-files/SKILL.md): complex tasks, research, और long-running work के लिए file-based planning.
- [context7-cli](context7-cli/SKILL.md): current library docs और Context7-backed references fetch करने के लिए।
- [agent-browser](agent-browser/SKILL.md): screenshots, forms, scraping, और web QA के लिए browser automation.
- [gh-fix-ci](gh-fix-ci/SKILL.md): failing GitHub Actions checks inspect करके logs को fix plan में बदलता है।
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): अधिक reliable LLM workflows के लिए production-oriented prompt patterns.
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md): high-quality frontend design skill और companion design commands का पूरा bundle.

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

- [brainstorming](brainstorming/SKILL.md): implementation से पहले intent, requirements, और design स्पष्ट करें।
- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`, `findings.md`, और `progress.md` के साथ persistent markdown planning.
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md): production LLM systems के लिए advanced prompt design patterns.
- [test-driven-development](test-driven-development/SKILL.md): implementation work से पहले tests लिखने को enforce करता है।

### GitHub Workflow

- [gh-address-comments](gh-address-comments/SKILL.md): `gh` के साथ current PR पर review और issue comments address करें।
- [gh-fix-ci](gh-fix-ci/SKILL.md): failing GitHub Actions checks inspect करें, logs summarize करें, और fixes plan करें।
- [yeet](yeet/SKILL.md): केवल तब उपयोग करें जब user explicitly stage, commit, push, और GitHub pull request खोलने के लिए कहे।

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): navigation, forms, screenshots, और scraping के लिए browser automation.
- [pinchtab](pinchtab/SKILL.md): stable accessibility refs के साथ Pinchtab के local HTTP API द्वारा Chrome control करें।
- [electron](electron/SKILL.md): Chrome DevTools Protocol के माध्यम से Electron desktop apps automate करें।
- [dogfood](dogfood/SKILL.md): reproducible evidence के साथ structured exploratory testing.

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): `ai-elements` library के लिए AI chat UI components बनाएं।
- [better-icons](better-icons/SKILL.md): CLI या MCP के जरिए 200+ Iconify libraries में icons खोजें, browse करें, और SVG प्राप्त करें।
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md): Vercel Engineering से React और Next.js performance guidance.
- [remotion-best-practices](remotion-best-practices/SKILL.md): React-based video work के लिए Remotion guidance.
- [`impeccable/`](impeccable/README.md): `frontend-design`, `adapt`, `audit`, `polish` आदि सहित 18 vendored frontend design skills.

### Utilities & Authoring

- [docx](docx/SKILL.md): formatting, comments, और tracked changes के साथ Word documents create, read, edit, और manipulate करें।
- [pdf](pdf/SKILL.md): rendering-aware checks के साथ PDFs पढ़ें, बनाएं, और review करें।
- [pptx](pptx/SKILL.md): slide decks, templates, और presentation content create, read, edit, और manipulate करें।
- [xlsx](xlsx/SKILL.md): spreadsheet creation, editing, formulas, और analysis.
- [skill-creator](skill-creator/SKILL.md): बेहतर structure और tool integrations के साथ skills create या update करें।

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) में [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) से लिया गया design-focused vendored bundle शामिल है, commit `15332dd293986e0a310fa54c103025d21142c3dd` पर आधारित।

इसमें शामिल हैं:

- `frontend-design`: flagship frontend design skill
- `adapt`, `animate`, `audit`, `bolder`, `clarify`, `colorize`, `critique`, `delight`, `distill`
- `extract`, `harden`, `normalize`, `onboard`, `optimize`, `polish`, `quieter`, `teach-impeccable`

Attribution और legal files [`impeccable/NOTICE.md`](impeccable/NOTICE.md) और [`impeccable/LICENSE`](impeccable/LICENSE) में सुरक्षित रखे गए हैं।

## सामान्य prerequisites

- कुछ skills मानकर चलती हैं कि `gh` installed और authenticated है।
- Browser-focused skills के लिए Chrome/CDP-capable environment की आवश्यकता हो सकती है।
- Third-party doc lookup skills external CLIs या MCP tools पर निर्भर हो सकती हैं; विवरण के लिए संबंधित `SKILL.md` देखें।

## पूरा Skill Index

`Source URL` उस skill के canonical upstream को point करता है जब skill vendored/imported हो; अन्यथा यह इस repository के skill directory को point करता है।

### Top-Level Skills

| Skill | विवरण | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | AI agents के लिए browser automation CLI: navigation, form filling, screenshots, extraction, और web testing. | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | composable patterns और shadcn/ui conventions के साथ ai-elements library के लिए नए AI chat interface components बनाएं। | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [better-icons](better-icons/SKILL.md) | CLI या MCP tools के जरिए 200+ Iconify libraries खोजें और SVG icons प्राप्त करें। | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills) |
| [brainstorming](brainstorming/SKILL.md) | implementation work से पहले intent, requirements, और design स्पष्ट करें। | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [context7-cli](context7-cli/SKILL.md) | docs lookup, skill management, और MCP setup के लिए Context7 CLI का उपयोग करें। | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | formatting, comments, tracked changes, और image updates के साथ Word documents create, read, edit, और manipulate करें। | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | screenshots और videos के साथ reproducible issue reports तैयार करने के लिए web apps का systematic परीक्षण करें। | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | agent-browser और Chrome DevTools Protocol के माध्यम से Electron desktop apps automate करें। | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | web, code, और company research के लिए Exa का उपयोग करें। | Custom |
| [find-skills](find-skills/SKILL.md) | जब users को specialized capabilities चाहिए हों, तब existing skills खोजें। | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | code लिखने से पहले current third-party API या SDK docs fetch करें। | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | current branch पर PR review और issue comments को `gh` के साथ address करें। | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | failing GitHub Actions checks inspect करें, logs pull करें, और fixes plan करें। | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [pdf](pdf/SKILL.md) | rendering checks और Python tooling के साथ PDF files पढ़ें, बनाएं, और review करें। | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | Pinchtab के HTTP API के जरिए headless या headed Chrome control करें, web automation, scraping, form filling, navigation, screenshots, और stable accessibility refs के साथ extraction के लिए। | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skill/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | `task_plan.md`, `findings.md`, और `progress.md` का उपयोग करके complex tasks के लिए file-based planning. | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.agent/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | PowerPoint presentations, templates, layouts, notes, और slide content create, read, edit, और manipulate करें। | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | reliable, production LLM workflows के लिए advanced prompt engineering patterns. | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | React के साथ videos बनाने के लिए Remotion best practices. | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | specialized knowledge और tool integrations के साथ skills create या update करने की guide. | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [test-driven-development](test-driven-development/SKILL.md) | किसी भी feature या bugfix को implement करने से पहले उपयोग करें। | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | Vercel Engineering से React और Next.js performance optimization guidance. | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | spreadsheet creation, editing, formulas, formatting, और analysis. | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | केवल तब उपयोग करें जब user explicitly `gh` के साथ stage, commit, push, और GitHub pull request खोलने को कहे। | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### Vendored `impeccable/` Skills

| Skill | विवरण | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | उच्च पहचान और production-grade quality के साथ frontend interfaces बनाएं। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | designs को अलग-अलग screen sizes, devices, और contexts के लिए adapt करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | purposeful motion और micro-interactions जोड़ें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | accessibility, performance, theming, और responsive design के पार interface quality audit करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | safe या boring designs को और अधिक visually interesting बनाएं। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | अस्पष्ट UX copy और instructions को बेहतर बनाएं। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | बहुत अधिक monochrome features में strategic color जोड़ें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | UX perspective से design effectiveness evaluate करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | interfaces में personality और memorable touches जोड़ें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | designs को उनकी essential form तक simplify करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | reusable components, tokens, और patterns को design system में consolidate करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | errors, i18n, overflow, और edge cases के आसपास resilience बढ़ाएं। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | किसी feature को design system के अनुरूप normalize करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | onboarding और first-time user experience को design या improve करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | frontend performance, rendering, motion, और bundle efficiency सुधारें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | alignment, spacing, consistency, और detail के लिए final quality pass. | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | quality बरकरार रखते हुए visual aggression कम करें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | future work के लिए design context एकत्र करके persistent guidance के रूप में सहेजें। | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## Contributing

नई skills या existing skills में improvements के लिए contributions का स्वागत है।

1. Trigger conditions स्पष्ट और testable रखें।
2. Examples concise और execution-oriented रखें।
3. अगर कोई skill external tools पर निर्भर है, तो उस dependency को `SKILL.md` में document करें।
4. जब आप किसी skill को add या rename करें, तो `README.md` और `README.zh-CN.md` अपडेट करें, और public-facing skill index बदलने पर बाकी translated READMEs भी refresh करें।

## License

यह repository [LICENSE](LICENSE) के अंतर्गत licensed है।

कुछ skills में skill-specific assets और attribution के लिए अतिरिक्त license files या notices शामिल हैं, जिनमें [`docx/`](docx/), [`pptx/`](pptx/), [`impeccable/`](impeccable/README.md), [`skill-creator/`](skill-creator/), और [`xlsx/`](xlsx/) शामिल हैं।
