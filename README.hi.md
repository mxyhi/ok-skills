# OK Skills: Codex, Claude Code, Cursor, OpenClaw और अन्य टूल्स के लिए AI Coding Agent Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | हिन्दी

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

Codex, Claude Code, Cursor, OpenClaw, Trae और अन्य `SKILL.md`-compatible टूल्स के लिए चुनी हुई AI coding agent skills और `CLAUDE.md` / `AGENTS.md` playbooks का यह curated repository है।

इस repo में अभी **32 reusable skills** शामिल हैं, और सभी इस repo में top-level skill directories के रूप में सीधे maintain की जाती हैं। इसे `~/.agents/skills/ok-skills` में clone करें; अंदर की directories पहले से ही `AGENTS.md`-driven workflows के अपेक्षित layout के अनुसार हैं, और [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) Claude Code-oriented agent playbook देता है。

अगर आप **Codex skills**, **Claude Code skills**, **Cursor skills**, **OpenClaw skills**, reusable **CLAUDE.md / AGENTS.md** playbooks, या practical **SKILL.md** examples खोज रहे हैं, तो यह repository खोजने में आसान और clone करते ही उपयोग योग्य होने के लिए व्यवस्थित की गई है।

**लोकप्रिय उपयोग परिदृश्य:** docs lookup, browser automation, prompt engineering, planning workflows, frontend design, और PDF / Word / PPTX / XLSX authoring.

## यह Repo किनके लिए है

- आप Codex, Claude Code, Cursor, OpenClaw, Trae या किसी अन्य AI coding agent का उपयोग करते हैं और ad-hoc prompts की जगह reusable skills चाहते हैं।
- आप `CLAUDE.md` / `AGENTS.md` / `SKILL.md` workflows maintain करते हैं और ऐसी portable instructions चाहते हैं जो कई projects में काम करें।
- आपको docs lookup, browser automation, planning, prompt engineering, frontend design, PDFs, Office documents, slide decks और spreadsheets के लिए battle-tested skills चाहिए।

## शुरुआत यहां से करें

अगर आप शुरुआत में केवल कुछ skills install करना चाहते हैं, तो इनसे शुरू करें:

- [planning-with-files](planning-with-files/SKILL.md): complex tasks, research, और long-running work के लिए file-based planning.
- [find-docs](find-docs/SKILL.md): current library docs, API references, और Context7-backed examples fetch करने के लिए।
- [agent-browser](agent-browser/SKILL.md): screenshots, forms, scraping, और web QA के लिए browser automation.

## 1-मिनट Quick Start

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

Clone करने के बाद repo `~/.agents/skills/ok-skills` पर रहेगा, और अंदर की directories पहले से अपेक्षित layout का पालन करती हैं:

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

Claude Code या Codex की global instructions के लिए [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) से शुरू करें, फिर इसे Claude Code के `CLAUDE.md` या Codex के `AGENTS.md` में copy या merge करें। इसमें Chinese-first, KISS-oriented workflow, latest docs/source checks, multi-agent preference, default `caveman` / `planning-with-files` / `karpathy-guidelines`, strict TypeScript expectations और context-mode routing rules शामिल हैं। Reuse करने से पहले `语言要求` section को अपने project के लिए edit करें। `其他注意项` section intentionally project-local है और जरूरत के अनुसार edit किया जा सकता है।

अपने `AGENTS.md` में simple trigger rules जोड़ें, या वही skill triggers `CLAUDE.md` / `AGENTS.md` में merge करें:

```md
## Skills

- planning-with-files: Use for complex tasks, research, or anything that will take 5+ tool calls.
- find-docs: Use when you need current library docs, API references, or Context7-backed examples.
- agent-browser: Use for browser automation, screenshots, scraping, web testing, or form filling.
```

फिर इसे natural language में trigger करें:

- `Use planning-with-files before refactoring this module.`
- `Use find-docs to fetch the latest docs for this SDK.`
- `Use agent-browser to reproduce this UI bug.`

## उपयोग-परिदृश्य के अनुसार Skills ब्राउज़ करें

### Research & Docs

- [find-docs](find-docs/SKILL.md): current docs lookup के लिए focused Context7 CLI workflow.
- [exa-search](exa-search/SKILL.md): Exa search tools के साथ web, code, और company research.
- [get-api-docs](get-api-docs/SKILL.md): coding शुरू करने से पहले current third-party API और SDK documentation fetch करें।
- [find-skills](find-skills/SKILL.md): जब user किसी capability की मांग करे, तब existing skills खोजें।

### Planning & Prompting

- [planning-with-files](planning-with-files/SKILL.md): `task_plan.md`, `findings.md`, और `progress.md` के साथ persistent markdown planning.
- [autoresearch](autoresearch/SKILL.md): clear goals, metrics, verify loops, और keep/discard gates के साथ autonomous goal-directed iteration.
- [diagnosing-bugs](diagnosing-bugs/SKILL.md): कठिन bugs और performance regressions के लिए disciplined diagnosis loop.
- [grill-with-docs](grill-with-docs/SKILL.md): plan को domain language, `CONTEXT.md`, और ADRs के खिलाफ जांचते हुए docs inline update करना.
- [grilling](grilling/SKILL.md): direct grill sessions और `grill-with-docs` के लिए reusable one-question-at-a-time interview loop.
- [handoff](handoff/SKILL.md): current work को fresh agent के लिए redacted handoff document में compact करें.
- [teach](teach/SKILL.md): missions, resources, lessons, और learning records के साथ stateful teaching workspace चलाएं.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md): locality, leverage, testability, और AI navigation सुधारने वाली architecture deepening opportunities खोजें।
- [prototype](prototype/SKILL.md): design questions का जल्दी जवाब देने के लिए throwaway logic या UI prototypes बनाएं.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md): overcomplication, छिपी assumptions, और unverifiable changes घटाने वाली coding behavior guidelines।
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md): tests में `as` type assertions को `@total-typescript/shoehorn` में migrate करें।
- [tdd](tdd/SKILL.md): feature, bugfix, refactor, या behavior change से पहले test-first red-green-refactor लागू करता है।
- [systematic-debugging](systematic-debugging/SKILL.md): bug, test failure, ya unexpected behavior में fix propose करने से पहले root cause को systematically जांचें।

### Automation & QA

- [agent-browser](agent-browser/SKILL.md): navigation, forms, screenshots, और scraping के लिए browser automation.
- [kimi-webbridge](kimi-webbridge/SKILL.md): local daemon के जरिए user के real browser को navigation, forms, screenshots, page reading और authenticated sessions के लिए control करें।
- [browser-trace](browser-trace/SKILL.md): browser automation debugging के लिए CDP traces, screenshots, और DOM dumps capture करें।
- [opencli](opencli/opencli-usage/SKILL.md): browser login session reuse, public APIs, और AI-generated adapters के साथ websites को CLI commands में बदलें।
- [xquik-twitter](xquik-twitter/SKILL.md): Xquik API से X/Twitter data खोजें और confirmed account actions चलाएं।

### Frontend & Design

- [ai-elements](ai-elements/SKILL.md): `ai-elements` library के लिए AI chat UI components बनाएं।
- [huashu-design](huashu-design/SKILL.md): high-fidelity HTML prototypes, interactive demos, slide decks, motion design, variants, video exports, aur design critiques banayein.
- [better-icons](better-icons/SKILL.md): CLI या MCP के जरिए 200+ Iconify libraries में icons खोजें, browse करें, और SVG प्राप्त करें।

### Utilities & Authoring

- [minimax-docx](minimax-docx/SKILL.md): OpenXML SDK (.NET) ke saath professional DOCX creation, editing, aur formatting.
- [minimax-pdf](minimax-pdf/SKILL.md): token-based design system ke saath PDF documents generate, fill, aur reformat karein.
- [pptx-generator](pptx-generator/SKILL.md): PptxGenJS, XML workflows, ya markitdown ke saath PowerPoint presentations generate, edit, aur read karein.
- [huashu-design](huashu-design/SKILL.md): HTML decks, editable PPTX, MP4/GIF motion pieces, aur narrated design videos banayein.
- [minimax-xlsx](minimax-xlsx/SKILL.md): low-loss XML workflow ke saath Excel/spreadsheet files open, create, read, analyze, edit, aur validate karein.

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) का upstream baseline [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files) है। यह repository local skill के लिए उसी upstream directory को canonical baseline मानती है। Local differences सिर्फ `skills-ref`-compatible `SKILL.md` frontmatter और install-location-independent relative script path docs तक सीमित हैं।

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
| [autoresearch](autoresearch/SKILL.md)                               | Modify, verify, keep/discard, aur repeat workflows ke liye autonomous goal-directed iteration engine.                                                                                      | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | CLI या MCP tools के जरिए 200+ Iconify libraries खोजें और SVG icons प्राप्त करें।                                                                                                             | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | local daemon के जरिए user के real browser को navigation, forms, screenshots, page reading और authenticated sessions के लिए control करें।                                                       | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | browser automation debugging के लिए CDP traces, screenshots, और DOM dumps capture करें।                                                                                  | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | Ultra-compressed communication mode jo caveman style me bolkar response tokens kam karta hai aur technical accuracy banaye rakhta hai.                                                       | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | कठिन bugs और performance regressions के लिए disciplined diagnosis loop.                                                                             | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | current documentation, API references, और code examples के लिए Context7 CLI का उपयोग करें।                                                                                                   | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | OpenXML SDK (.NET) ke saath professional DOCX creation, editing, aur formatting. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | web, code, और company research के लिए Exa का उपयोग करें।                                                                                                                                     | Custom                                                                                                                         |
| [find-skills](find-skills/SKILL.md)                                 | जब users को specialized capabilities चाहिए हों, तब existing skills खोजें।                                                                                                                    | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | High-fidelity HTML prototypes, interactive demos, slide decks, motion design, variants, video exports, aur design critiques banayein.                                                       | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | code लिखने से पहले current third-party API या SDK docs fetch करें।                                                                                                                           | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | domain language, `CONTEXT.md`, और ADRs के against plan को stress-test करके docs inline update करना.                                                 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [grilling](grilling/SKILL.md)                               | Direct grill sessions और `grill-with-docs` के लिए reusable one-question-at-a-time interview loop.                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [handoff](handoff/SKILL.md) | Current conversation को दूसरे agent के लिए redacted handoff document में compact करता है. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) |
| [teach](teach/SKILL.md) | missions, resources, lessons, और learning records वाले workspace में skill या concept सिखाता है. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | locality, leverage, testability, और AI navigation सुधारने वाली architecture deepening opportunities खोजें।                                                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [prototype](prototype/SKILL.md) | Design questions का जल्दी जवाब देने के लिए throwaway logic या UI prototypes बनाता है. | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | Overcomplication, छिपी assumptions, और unverifiable changes घटाने वाली coding behavior guidelines।                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | test files को `as` type assertions से `@total-typescript/shoehorn` में migrate करें।                                                                                                          | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | Browser login session reuse, public APIs, और AI-generated adapters के साथ websites को CLI commands में बदलने की skill.                                                                       | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [xquik-twitter](xquik-twitter/SKILL.md)                         | Xquik API से X/Twitter data खोजें और confirmed account actions चलाएं।                                                                                                                       | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)             |
| [minimax-pdf](minimax-pdf/SKILL.md) | Token-based design system ke saath PDF documents generate, fill, aur reformat karein. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | `task_plan.md`, `findings.md`, और `progress.md` का उपयोग करके complex tasks के लिए file-based planning.                                                                                      | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | PptxGenJS, XML workflows, ya markitdown ke saath PowerPoint presentations generate, edit, aur read karein. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | किसी भी feature, bugfix, refactor, या behavior change से पहले उपयोग करें; public interface integration-style tests को प्राथमिकता देता है।                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | किसी भी bug, test failure, या unexpected behavior में fix propose करने से पहले उपयोग करें।                                                  | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | Low-loss XML workflow ke saath Excel/spreadsheet files open, create, read, analyze, edit, aur validate karein. | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
## Contributing

नई skills या existing skills में improvements के लिए contributions का स्वागत है।

1. Trigger conditions स्पष्ट और testable रखें।
2. Examples concise और execution-oriented रखें।
3. अगर कोई skill external tools पर निर्भर है, तो उस dependency को `SKILL.md` में document करें।
4. जब आप किसी skill को add या rename करें, तो `README.md` और `README.zh-CN.md` अपडेट करें, और public-facing skill index बदलने पर बाकी translated READMEs भी refresh करें।

## License

यह repository [LICENSE](LICENSE) के अंतर्गत licensed है।
