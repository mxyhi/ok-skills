# deep-research Skill

<p align="center"><b>English</b> · <a href="#chinese">中文</a></p>

---

**Deep Research Report Generation Skill — One command, ten minutes, institutional-grade deep research report**

Multi-agent autonomous search, scrape, write, and QA — feed it a topic, get a citable, browsable, exportable research report in Chinese or 19 other languages.

Benchmarked against institutional research structure: conclusions-first, traceable sources, counter-arguments, scenario forecasting. Supports quick / standard / deep tiers, with automatic language detection across 19 languages.

Built for industry research, trend foresight, competitive scanning, policy analysis, technology deep-dives, and investment memos — not a handful of search summaries, but a report you can actually use.

> **Current version:** [View updates](https://github.com/hoolulu/deep-research/commits/main)
>
> 📂 **Browse all sample reports →** [H33研报· 深度调研报告集](https://www.h33.top)
> — filter, sort, and browse by language and depth.

---

### ✨ At a Glance

<table width="100%">
<tr><td style="white-space: nowrap; width: 1%;"><b>🎯 One command</b></td><td><code>/research &lt;topic&gt;</code> → fully automated research, zero manual intervention</td></tr>
<tr><td style="white-space: nowrap;"><b>⏱ Report in ~10 min</b></td><td>quick mode ~8–12 min, standard ~10–15 min</td></tr>
<tr><td style="white-space: nowrap;"><b>🌍 19 languages</b></td><td>Auto-detects topic language, generates report in the same language</td></tr>
<tr><td style="white-space: nowrap;"><b>🔧 All platforms</b></td><td>Works with any AI coding tool (Claude Code, Codex CLI, Cursor, DSH, Windsurf, Cline and more)</td></tr>
<tr><td style="white-space: nowrap;"><b>📁 Local file research</b></td><td>Also supports PDF/DOCX/TXT/MD, no internet needed, auto-parsed</td></tr>
<tr><td style="white-space: nowrap;"><b>🖥️ Local report browser</b></td><td>Auto-refreshed as a local browser page after each run<br><code>reports-browser/index.html</code> — search, filter, sort, preview</td></tr>
<tr><td style="white-space: nowrap;"><b>📄 PDF/DOCX export</b></td><td>Export reports as PDF or DOCX from the preview modal — fully client-side, no server required</td></tr>
</table>

<table width="100%">
<tr><th>Command</th><th>Result</th></tr>
<tr><td style="white-space: nowrap;"><code>/research 中国新能源汽车产业发展现状</code></td><td>中文报告</td></tr>
<tr><td><code>/research Competitive landscape of AI cloud computing</code></td><td>English report</td></tr>
<tr><td><code>/research Анализ рынка нефти и газа в России</code></td><td>Отчёт на русском</td></tr>
<tr><td><code>/research 日本のアニメ産業のグローバル市場戦略</code></td><td>日本語レポート</td></tr>
<tr><td><code>/research 한국 반도체 산업의 글로벌 경쟁력 분석</code></td><td>한국어 보고서</td></tr>
<tr><td><code>local file research, see FAQ for prompts</code></td><td>offline mode, read local files</td></tr>
</table>

> It interacts with you entirely in the language you set and searches for materials in that target language — not a simple translation pipeline.

---

## 1. Why You Need This

If you've ever asked AI to do research, you've likely hit these walls:

- Search + summarize → too shallow, just a few bullet points
- Industry reports at $50–500+ each → too expensive for individuals
- Overseas tools → can't search Chinese sources like Baidu Baike, Zhihu, 199IT, iResearch
- AI fabricates numbers → looks reasonable but has no traceable source

This skill follows a **4-stage pipeline** before delivering a report. Not search-and-dump — it's analyze → search+verify → write → verify.

## 2. Who It's For

**Indie developers**, **independent researchers**, **small teams**.
People who need professional-grade research capabilities without relying on paid databases or research institutions.

## 3. Typical Output (Standard Mode)

| Metric | Data (standard mode example) |
|--------|------------------------------|
| Report length | 500-700 lines / ~12,000-20,000 chars (varies by language) |
| Data tables | 15-25, covering market size, competitive landscape, technical specs |
| Analysis paragraphs | 80-120 (each with conclusion + data + causation + judgment) |
| Unique sources cited | 15-25 (Chinese and international institutions) |
| Opposing viewpoints | 3-8, at least one controversy per chapter |
| Data collection | ~1-3 min |
| Report generation | ~8-15 min |
| Total time | ~10-20 min |

> Above ranges for standard mode. Actual times vary by topic complexity and data availability.

### 📖 Featured Reports

> All sample reports have moved to [H33研报· 深度调研报告集](https://www.h33.top) — filter, sort, and browse by language and type. Some featured topics:

| Report | Tags |
|--------|------|
| <a href="https://www.h33.top" target="_blank">Global AI Chip Market Landscape and Competitive Dynamics 2026</a> | AI · Semiconductors |
| <a href="https://www.h33.top" target="_blank">The Feasibility of Mars Colonization</a> | Space · Technology |
| <a href="https://www.h33.top" target="_blank">Electric Vehicle Battery Supply Chain and Raw Material Geopolitics 2026</a> | Energy · Geopolitics |
| <a href="https://www.h33.top" target="_blank">GenAI Enterprise Adoption Trends & ROI Measurement in 2026</a> | AI · Enterprise |
| <a href="https://www.h33.top" target="_blank">Cross-border E-commerce Logistics Trends in Southeast Asia 2026</a> | E-commerce · Logistics |

Click a report title to jump to the H33 report collection and search for the topic.

## 4. Cost

| Component | Cost |
|-----------|------|
| **LLM (already using)** | **DeepSeek v4 Flash** baseline: quick ~100–150k tokens / < $0.03, standard ~150–300k / < $0.06, deep ~300–500k / < $0.10 |
| **Scrapling fetching** | Runs locally, zero cost |
| **Domestic sources** | Direct connection, zero cost, no proxy needed |
| **AI tool runtime** | MIT open source, zero cost |

> Estimates based on DeepSeek v4 Flash ($0.14/1M input, $0.28/1M output, source: `https://api-docs.deepseek.com/quick_start/pricing`). Actual costs vary by cache hit rate and topic complexity.

## 5. How It Works

The pipeline runs in 4 automated stages:

```
① Analyze outline — Analyze topic, generate research framework and search plan
         ↓
② Collect data — ╭─ Online: four-layer parallel search (tool built-in engine → suggested sources → sources.json → free fallback) → Scrapling batch fetch → data pool
                  ╰─ Offline: read local files directly (PDF/DOCX/TXT/MD) → data pool
         ↓
③ Parallel writing — All chapters in parallel (auto-sequential without multi-agent), facts embedded directly in prompts, no tool calls
         ↓
④ Validate & assemble — Batch validate → assemble-report → convert-citations → escape-currency → qa-report
```


## 6. Search Pipeline & Built-in Resources

Search uses a **four-layer priority** strategy, all issued in parallel:

```
Layer 0 — Tool built-in engine (auto-detected at runtime, e.g., `websearch` / `web_search`)
Layer 1 — Outline-suggested sources (topic-targeted recommendations, e.g., arctic-council.org)
Layer 2 — sources.json (30+ curated quality sources, health-checked on startup)
Layer 3 — Free source reinforcement (A/B class search fallback)
```

All layers are merged and deduplicated, then batch-fetched by Scrapling. Free source reinforcement is triggered only when Layer 0-2 fail the per-sub-question quality gate (URL < 3 / outdated year / no authoritative source for high-priority sub-questions).

`sources.json` covers academic (Semantic Scholar / arXiv / PubMed / Nature), data (World Bank / IMF / Our World in Data), news (Reuters / BBC / Guardian), and Chinese sources (Baidu Baike / Zhihu / 36Kr / The Paper / iResearch / East Money / CSDN) — 30+ sources, auto health-checked on startup with dead sources skipped.

## 7. Report Highlights

| Dimension | Description |
|-----------|-------------|
| **Multilingual native writing** | Auto-detects topic language, writes directly in 19 languages, no translation pipeline |
| **Every number has a source** | `(N)` clickable citations in text, full reference list at end. No source = no number |
| **Pros and cons coexist** | Every chapter presents controversies and opposing views |
| **Confidence grading** | Final summary table (high/medium/low) shows what's reliable vs. disputed |
| **Data anti-pitfall** | Auto-detects common data errors — wrong units, fabricated trends, misattributed sources |
| **Paragraphs over padding** | 8-12 substantive paragraphs per chapter as core, tables can't pad the length |

## 8. Three Depth Modes

| Command | Purpose | Min chapters | Min paragraphs/chapter | Target chars | Est. time |
|---------|---------|-------------|----------------------|--------------|-----------|
| `/research <topic>` | standard (default) | 8 | ≥ 5 | ≈ 25,000 | ~10–15 min |
| `/research <topic> -quick` | Quick insight | 5 | ≥ 4 | ≈ 15,000 | ~8–12 min |
| `/research <topic> -deep` | Maximum depth | 10 | ≥ 6 | ≈ 45,000 | ~15–25 min |

> Parameters in `profiles.json`, restart to apply. Char count excludes whitespace and Markdown syntax.

## 9. Installation

deep-research is an **all-platform** skill: one codebase, drop it into any AI tool that supports skill/command mechanisms — no per-tool rewrite needed.

### 🧠 Method 1: AI Auto-Install (Recommended)

Copy this prompt into your AI tool's chat, the AI will do everything automatically:

```text
Please read the https://github.com/hoolulu/deep-research project and follow the documentation to:
1. Install prerequisites (determine method based on Scrapling docs and your OS)
2. Register the Scrapling MCP Server, verify it works after restart
3. Register the /research and /research-update entry points for your current tool
Confirm each step, then read VERSION and summarize the installation status.
```

The AI reads the docs → understands your system → installs step by step → verifies. No manual commands needed.

### 📋 Method 2: Manual Entry Registration

Each tool registers skills/commands differently — drop the whole project into the right directory (common tools below):

| Tool | skill/entry location | Command form |
|------|----------------------|--------------|
| OpenCode | `~/.opencode/skills/deep-research/` | `/research`, `/research-update` (included in `command/`) |
| Codex CLI | skill directory, `command/` files included | `/research`, `/research-update` |
| Claude Code | `~/.claude/skills/deep-research/` | Use SKILL.md as an Agent Skill |
| Cursor | `.cursor/skills/` or custom commands | Custom command pointing at SKILL.md |
| DSH / others | Any directory that supports skill loading | Load SKILL.md, then enter a topic |

> This skill's SKILL.md is already written as **all-platform** instructions: no dependency on any tool-specific `task()` multi-agent syntax. Chapter writing is parallel by default (when a multi-agent tool is detected); tools without multi-agent support automatically fall back to sequential writing — same output, slightly slower. Search and scraping logic (Scrapling) is reused unchanged across platforms.

### Prerequisites

| Component | Online mode | Offline mode | How to get |
|-----------|:-----------:|:------------:|------------|
| **AI tool runtime** (Claude Code / Codex CLI / Cursor / DSH / OpenCode etc.) | ✅ Required | ✅ Required | Pick your preferred tool |
| **Scrapling** | ✅ Required | ❌ Not needed | For web scraping; offline mode doesn't need it |

> **Platform note**: Multi-agent-capable tools (OpenCode, Claude Code, Codex, DSH, etc.) naturally write chapters in parallel; tools without multi-agent support automatically write sequentially. Offline mode only needs the LLM's file-reading capability — no search/scraping components required.

## 10. Usage

After installation and restart, type in the chat:

| Command | Description | Est. time |
|---------|-------------|-----------|
| `/research <topic>` | standard mode (online search) | ~10-15 min |
| `/research <topic> -quick` | quick mode (online search) | ~8-12 min |
| `/research <topic> -deep` | deep mode (online search) | ~15-25 min |
| `local file research` | offline mode (local files) | depends on file size |
| `/research-update` | Check for updates | — |

> Local file research: see FAQ §2 "How to use local materials for report generation?" for exact prompts.

### What Happens After You Send It

The entire pipeline runs automatically — you don't need to do anything:

```
① Analyze outline — Analyze topic, generate framework and search plan
② Collect data — tool built-in engine + sources.json parallel search → quality-triggered reinforcement → Scrapling batch fetch → data pool → quality check
③ Parallel writing — All chapters simultaneously, facts embedded in prompts
④ Validate & assemble — Batch validate → assemble → citations → QA
```

> Total ~10-20 minutes. Complex topics may take longer, simple ones may be faster.

### Output Files

Reports are saved as Markdown files in the skill's `reports/` directory, with date-timestamped filenames:

```
<your skill install dir>/deep-research/reports/
```

Open with any Markdown reader (Typora / Obsidian / VS Code etc.).

You can also specify a custom output path — ask AI to configure it.

**Local report browser page**: After each research run, AI auto-refreshes `reports-browser/index.html`. Open it directly in your browser (file:// protocol works) — all reports displayed in a searchable, filterable table with click-to-preview modal.

## 11. FAQ

**1. Search quotas? How to ensure uninterrupted searching?**

The system uses a **four-layer priority search** architecture (tool built-in engine → outline-suggested sources → sources.json → free source fallback), all issued in parallel, each layer auto-degrades on failure:

- **Layer 0 — Tool built-in engine**: Auto-detects the tool's built-in search engine at runtime (e.g., `websearch` / `web_search`). If available, used as primary, runs in parallel with subsequent layers. No additional configuration needed.
- **Layer 1 — Outline-suggested sources**: Task 1 recommends authoritative domains per topic (e.g., arctic-council.org, stats.gov.cn), searched first.
- **Layer 2 — sources.json quality sources**: 30+ curated sources (Semantic Scholar / arXiv / Nature / World Bank / IMF / Reuters / BBC / Baidu Baike / Zhihu / 36Kr / iResearch / East Money etc.). Auto health check on startup, dead sources skipped.
- **Layer 3 — Free source reinforcement (final fallback)**: triggered only when Layer 0-2 fail the per-sub-question quality gate (URL < 3 / outdated / no authoritative source for high-priority). DuckDuckGo / Bing / Brave / Mojeek / Semantic Scholar / GDELT / arXiv + 20+ Chinese sources. No API keys required, always available.

**2. How to use local materials for report generation?**

The skill has a built-in offline mode that generates fully-formatted reports (TOC, citations, metadata) from local files. Supported formats: **MD / TXT** (native read), **PDF** (AI auto-installs pypdf for text extraction), **DOCX** (AI auto-installs python-docx).

Choose your scenario:

**Scenario 1: Local materials + online supplement** (recommended for most complete research)
```
Use the deep-research skill with my local files in D:\notes\projectA to generate a research report on XX (quick mode). Prioritize local content, search online for anything missing.
```

**Scenario 2: Local materials only, no internet** (when you have sufficient data and don't want online distractions)
```
Use the deep-research skill with my local files in D:\notes\projectA to generate a research report on XX (quick mode). Use only local materials, do not search online.
```
The system skips the search/scraping pipeline and reads local files directly. Task 3 (chapter writing) and Task 4 (assembly/QA) run normally. The final output includes metadata, `[N]` citations, and TOC.

**Scenario 3: Pure local, no skill** (lightweight, no professional format needed)
```
Help me organize the materials in D:\notes\projectA into a structured research report with table of contents and chapter headings.
```

> **Scenario guide**: Incomplete materials → Scenario 1 (online supplement); Sufficient materials + need professional format → Scenario 2 (offline mode); Quick summary only → Scenario 3 (lightweight).

**3. How to update to the latest version?**

**Version strategy**: `main` branch always has the latest code. GitHub Releases are only for milestone markers.

All tools:

- **Auto**: Type `/research-update`, AI auto-runs `git pull`
- **Manual**: `cd <skill install dir>/deep-research && git pull`

Check version: `cat <skill install dir>/deep-research/VERSION`

**4. Can other tools auto-update?**

Yes. All tools share the same all-platform codebase — just `git pull` in the install directory (or ask your AI to do it). There are no platform-specific changes to preserve, so updates never conflict.

**5. Is my data safe?**

All processing is done locally. No data is collected or uploaded.

**6. How do I view my generated reports?**

After each research run, the AI outputs both the report file path and the local report browser page path.

- **Report file**: `{SKILLDIR}/reports/{LANG}/xxx.md` — open with any Markdown reader
- **Local report browser page**: `{SKILLDIR}/reports-browser/index.html` — **open directly in your browser** (works with file:// protocol). All reports are displayed in a table with search, language/depth filtering, sorting, and click-to-preview in a modal

You can also manually refresh the browser page anytime by running `python tools/generate_pages.py --local` in the skill directory.

## 12. Screenshot

<img width="1532" height="836" alt="Screenshot 2026-06-09 at 11-28-17" src="https://github.com/user-attachments/assets/736b0113-f054-4dba-b018-e656a51a9fb4" />

<img width="1532" height="932" alt="Screenshot 2026-06-09 at 11-30-13" src="https://github.com/user-attachments/assets/a88cbf27-7b6c-4ea3-8b51-424f48bf9906" />

<img width="1524" height="846" alt="Screenshot 2026-06-09 at 11-30-55" src="https://github.com/user-attachments/assets/ef10865d-3a72-4658-ac9c-28b2221e77f5" />

<img width="1528" height="840" alt="Screenshot 2026-06-09 at 11-32-13" src="https://github.com/user-attachments/assets/506e91eb-1d5d-4312-aceb-9280d357e264" />

<img width="1438" height="842" alt="Screenshot 2026-06-09 at 11-35-03" src="https://github.com/user-attachments/assets/75acd450-9349-4024-923d-f9b14ea601dd" />

---

<a id="chinese"></a>

**深度调研报告生成 Skill — 一条命令，十分钟出券商级深度调研报告**

多 Agent 自动搜索、抓取、撰写、质检——输入主题，输出可引用、可浏览、可导出的中文/多语言调研报告。

对标券商/第三方研究机构结构：结论先行、来源可追溯、反方视角、情景预测。支持 quick / standard / deep 三档模式，19 种语言随主题自动切换。

适合行业研究、趋势前瞻、竞品扫描、政策解读、技术专题、投研备忘——不是搜几条摘要，是交付一份能拿去用的报告。

> **当前版本：** [查看更新](https://github.com/hoolulu/deep-research/commits/main)
>
> 📂 **浏览所有示例报告 →** [H33研报· 深度调研报告集](https://www.h33.top)
> 可筛选、排序、按语言和类型浏览所有示例报告。

---

### ✨ 一分钟看懂


<table width="100%">
<tr><td style="white-space: nowrap; width: 1%;"><b>🎯 一个命令</b></td><td><code>/research 你的主题</code> → 全自动调研，无需人工干预</td></tr>
<tr><td style="white-space: nowrap;"><b>⏱ 十分钟出报告</b></td><td>quick 模式约 8–12 分钟，standard 约 10–15 分钟</td></tr>
<tr><td style="white-space: nowrap;"><b>🌍 19 种语言</b></td><td>主题用什么语言写，报告就用什么语言出，自动检测</td></tr>
<tr><td style="white-space: nowrap;"><b>🔧 所有平台通用</b></td><td>任何 AI 编程工具均可使用（Claude Code、Codex CLI、Cursor、DSH、Windsurf、Cline 等）</td></tr>
<tr><td style="white-space: nowrap;"><b>📁 本地文件调研</b></td><td>也可支持本地 PDF/DOCX/TXT/MD，不联网，AI 自动解析</td></tr>
<tr><td style="white-space: nowrap;"><b>🖥️ 本地报告浏览页</b></td><td>每次报告生成后自动刷新为本地浏览器页面<br><code>reports-browser/index.html</code>，支持搜索/筛选/排序/弹窗预览</td></tr>
<tr><td style="white-space: nowrap;"><b>📄 PDF/DOCX 导出</b></td><td>本地浏览页弹窗中可导出 PDF、DOCX 格式，浏览器端直接转换下载</td></tr>
</table>



<table width="100%">
<tr><th>命令</th><th>说明</th></tr>
<tr><td style="white-space: nowrap;"><code>/research 中国新能源汽车产业发展现状</code></td><td>中文报告</td></tr>
<tr><td><code>/research Competitive landscape of AI cloud computing</code></td><td>English report</td></tr>
<tr><td><code>/research Анализ рынка нефти и газа в России</code></td><td>Отчёт на русском</td></tr>
<tr><td><code>/research 日本のアニメ産業のグローバル市場戦略</code></td><td>日本語レポート</td></tr>
<tr><td><code>/research 한국 반도체 산업의 글로벌 경쟁력 분석</code></td><td>한국어 보고서</td></tr>
<tr><td><code>本地资料调研，详细命令见 FAQ</code></td><td>离线模式，读本地文件</td></tr>
</table>

> 是全程以设定语言与你交互，并搜索目标语言的资料，不是简单的翻译输出。

---

## 一、为什么你需要这个

让 AI 帮你做调研，你大概率碰过这些坑：

- 搜索 + 总结 → 太浅，出来几条摘要，没有纵深
- 行业报告按份收费 $50–500+ → 太贵，个人用不起
- 海外工具 → 搜不到国内资源如：百度百科、知乎、199IT、艾瑞
- AI 编数字 → 看起来合理，但找不到来源

这个 skill 走完 **4 层流程**才交报告。不是搜完就出，是析→搜验→写→验。

## 二、谁适合用

**独立开发者**、**独立研究者**、**小团队**。
需要专业级调研能力，但不想依赖付费数据库或研究机构的人。

## 三、一次标准模式调研的输出


| 指标      | 数据（standard 模式示例）                           |
| ------- | ------------------------------------------- |
| 报告长度    | 500-700 行 / 约 12,000-20,000 字（视语言浮动）     |
| 数据表     | 15-25 张，覆盖市场规模、竞争格局、技术参数等多个维度               |
| 分析段落    | 80-120 段（每段含结论 + 数据 + 因果 + 判断）              |
| 引用的独立机构 | 15-25 家（中国信通院、艾瑞咨询、国家统计局、百度百科、知乎、36氪、澎湃新闻等） |
| 反方观点    | 3-8 处，每章至少呈现一个争议或反对角度                       |
| 数据收集    | ~1-3 分钟                                     |
| 报告生成    | ~8-15 分钟                                    |
| 总耗时     | ~10-20 分钟                                   |


> 以上为 standard 模式典型范围，实际因主题复杂度、数据可获取性、搜索引擎响应等因素有所浮动。|

### 📖 精选报告展示

> 所有示例报告已迁移至 [H33研报· 深度调研报告集](https://www.h33.top)，可筛选、排序、按语言和类型浏览。以下为部分精选主题：

| 报告主题 | 话题标签 |
|---------|---------|
| <a href="https://www.h33.top" target="_blank">长江三角洲与珠江三角洲：中国两大经济引擎的地理比较</a> | 地理 · 经济 |
| <a href="https://www.h33.top" target="_blank">郑和下西洋：为什么中国在 15 世纪放弃了海洋？</a> | 历史 · 航海 |
| <a href="https://www.h33.top" target="_blank">玛雅文明崩溃之谜：干旱、战争还是生态超载？</a> | 历史 · 文明 |
| <a href="https://www.h33.top" target="_blank">2026年中国新能源汽车行业展望</a> | 汽车 · 产业 |
| <a href="https://www.h33.top" target="_blank">火星移民的工程现实：从 SpaceX 到 ISRU 到辐射防护</a> | 航天 · 科技 |

点击报告标题跳转到 H33 研报集，在站内搜索对应主题即可阅读。

## 四、成本


| 组件                                              | 费用                                                                                                              |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **LLM（你已经在用的）**                                 | **DeepSeek v4 Flash** 基准：quick 约 10–15 万 token / < 0.2 元，standard 约 15–30 万 / < 0.4 元，deep 约 30–50 万 / < 0.7 元 |
| **Scrapling 抓取**                                | 纯本地运行，零费用                                                                                                       |
| **国内源（百度百科/维基百科/知乎/36氪/澎湃/199IT/艾瑞/东方财富/国统局等）** | 直连零费用，不要代理                                                                                                      |
| **AI 工具运行时**                                | 开源免费，零费用                                                                                                      |


> 以上估算基于 DeepSeek v4 Flash（$0.14/百万输入、$0.28/百万输出，来源：`https://api-docs.deepseek.com/quick_start/pricing`）。实际因缓存命中率与主题复杂度浮动。

## 五、工作逻辑

整个流程分 4 个阶段，按顺序自动执行：

```
① 分析大纲 — 分析主题，生成调研框架和搜索计划
         ↓
② 采集数据 — ╭─ 在线模式：四层搜索并行（工具内置引擎 → 建议源 → sources.json → 免费源）→ Scrapling 批量抓取 → 数据池
               ╰─ 离线模式：直接读取本地文件（PDF/DOCX/TXT/MD）→ 数据池
         ↓
③ 并行撰写 — 所有章节同时撰写，事实直接嵌入 prompt，不做工具调用
           ↓
④ 验收装配 — 批量 validate → assemble-report → convert-citations → escape-currency → qa-report
```


## 六、搜索链路与内置资源

搜索采用 **四层优先级** 策略，全部并行发出：

```
Layer 0 — 工具内置引擎（如 `websearch` / `web_search`，运行时自适应）
Layer 1 — 大纲建议源（按主题定向推荐，如 arctic-council.org）
Layer 2 — sources.json（skill 内置 30+ 优质源，启动时健康检测）
Layer 3 — 免费源补强（A/B 类搜索兜底）
```

所有层的结果合并去重，由 Scrapling 统一抓取全文。免费源补强仅在 Layer 0-2 结果未通过逐子问题质量门时触发（子问题可用 URL < 3 / 结果年份过旧 / high 优先级子问题无权威来源）。

`sources.json` 覆盖学术（Semantic Scholar / arXiv / PubMed / Nature）、数据（World Bank / IMF / Our World in Data）、新闻（Reuters / BBC / Guardian）、中文（百度百科 / 知乎 / 36氪 / 澎湃 / 艾瑞 / 东方财富 / CSDN 等）30+ 个源，启动时自动健康检测，死源跳过。

## 七、报告独特亮点


| 维度          | 说明                                      |
| ----------- | --------------------------------------- |
| **多语言专业行文** | 自动检测主题语言，以 19 种语言直接撰写报告，非翻译模式           |
| **每个数字有来源** | 正文标注 `(N)` 可点击引用，文末附参考来源列表。找不到来源的数字不写   |
| **正反观点并存**  | 每章呈现争议和反对观点，不回避矛盾                       |
| **置信度分级**   | 末章汇总表（高/中/低），什么可靠什么有争议一目了然              |
| **数据防坑机制**  | 自动识别常见数据错误——单位搞混、数据造假、张冠李戴，不让有问题的数据混进报告 |
| **段落重于行数**  | 每章 8-12 段正文为核心，表格和空行灌不了水                |


## 八、三种深度


| 命令                    | 用途          | 最少章数 | 最少段落/章 | 参考字数（字符） | 参考耗时       |
| --------------------- | ----------- | ---- | ------ | -------- | ---------- |
| `/research 主题`        | standard 默认 | 8    | ≥ 5    | ≈ 25,000 | ~10–15 min |
| `/research 主题 -quick` | 快速洞察        | 5    | ≥ 4    | ≈ 15,000 | ~8–12 min  |
| `/research 主题 -deep`  | 极致深度        | 10   | ≥ 6    | ≈ 45,000 | ~15–25 min |


> 参数见 `profiles.json`，修改后重启生效。字数为去空格和 Markdown 语法的纯字符数。

## 九、安装

deep-research 是**所有平台通用**的 skill：一套文件，放入任意支持 skill/命令机制的 AI 工具即可使用，无需按工具改写流程。

### 🧠 方式一：AI 傻瓜安装（推荐）

把下面这段提示词复制到你的 AI 工具聊天框发送，AI 会自动完成一切：

```text
请调研 https://github.com/hoolulu/deep-research 项目，按照文档要求依次完成：

1. 安装前置依赖（根据 Scrapling 官方文档和你的操作系统确定安装方式）
2. 注册 Scrapling MCP Server，确保重启工具后正常使用
3. 把本 skill 注册为当前工具的 skill / 命令入口（/research 和 /research-update）

每完成一步都确认结果，完成后读取 VERSION 确认版本号，并总结安装状态。
```

AI 会读取项目文档→理解系统类型→逐项安装→验证可用性。不需要手动执行任何命令。

### 📋 方式二：手动注册命令入口

各工具的 skill/命令注册方式不同，把整个项目放进对应目录即可（以下为常见工具）：

| 工具 | skill/入口位置 | 命令形式 |
|------|--------------|---------|
| OpenCode | `~/.opencode/skills/deep-research/` | `/research`、`/research-update`（`command/` 已含） |
| Codex CLI | skill 目录，`command/` 已含命令文件 | `/research`、`/research-update` |
| Claude Code | `~/.claude/skills/deep-research/` | 用 SKILL.md 作为 Agent Skill |
| Cursor | `.cursor/skills/` 或自定义命令 | 自定义命令指向 SKILL.md |
| DSH / 其他 | 任意支持 skill 加载的目录 | 加载 SKILL.md 后输入主题 |

> 本 skill 的 SKILL.md 已写成**所有平台通用**指令：不再依赖任何工具专属的 `task()` 等多 agent 语法。章节撰写默认并行（探测到多 agent 工具时），没有多 agent 能力的工具会自动降级为串行撰写，产物一致，仅耗时略增。搜索与抓取逻辑（Scrapling）各平台原样复用。

### 前置依赖


| 组件 | 在线模式 | 离线模式 | 获取方式 |
|:----|:--------|:--------|:--------|
| **AI 工具运行时**（Claude Code / Codex CLI / Cursor / DSH / OpenCode 等） | ✅ 必须 | ✅ 必须 | 选择你习惯的工具即可 |
| **Scrapling** | ✅ 必须 | ❌ 不需要 | 网页抓取用，离线模式不涉及 |

> **平台说明**：支持多 agent 的工具（OpenCode、Claude Code、Codex、DSH 等）天然并行撰写章节；不支持多 agent 的工具自动串行撰写。离线模式下仅依赖 LLM 的文件读取能力，无需搜索/抓取组件。

## 十、使用方法

安装并重启你的 AI 工具后，在聊天框输入：


| 命令                                                         | 说明          | 参考耗时       |
| ---------------------------------------------------------- | ----------- | ---------- |
| `/research 你的主题`                                           | standard 模式（在线搜索） | ~10-15 min |
| `/research 你的主题 -quick`                                    | quick 模式（在线搜索）   | ~8-12 min  |
| `/research 你的主题 -deep`                                     | deep 模式（在线搜索）    | ~15-25 min |
| `本地资料调研`                                              | 离线模式（读本地文件）     | 取决于文件大小   |
| `/research-update`                                         | 检查更新        | —          |

> 本地资料调研：具体指令词见 FAQ 第 2 节《如何使用本地资料生成报告？》。

### 发送后会发生什么

整个流程自动运行，你不需要做任何操作：

```
① 分析大纲 — 分析主题，生成调研框架和搜索计划（含 source_suggestions 定向源推荐）
② 采集数据 — 四层搜索并行（工具内置引擎→建议源→sources.json→免费源）→ Scrapling 批量抓取 → 数据池提取 → 数据质检
③ 并行撰写 — 所有章节同时撰写，事实直接嵌入 prompt，不做额外工具调用
④ 装配验收 — 批量 validate → assemble-report → convert-citations → escape-currency → qa-report
```

> 以上累计 ~10-20 分钟。复杂主题可能延长，简单主题可能缩短。

### 输出文件

报告以 Markdown 格式保存到 skill 目录下的 `reports/` 文件夹，文件名包含日期时间戳：

```
<你的 skill 安装目录>/deep-research/reports/
```

可以用任何 Markdown 阅读器（Typora / Obsidian / VS Code 等）打开。

你也可以指定报告的存放路径，让 AI 帮你修改。

**本地报告列表页**：每次调研完成后，AI 自动刷新 `reports-browser/index.html`。直接用浏览器打开（支持 file:// 协议），所有报告以表格展示，支持搜索、按语言/深度筛选、排序，点击标题在弹窗中预览。

## 十一、FAQ

**1. 搜索额度？怎么保证搜索不中断？**

系统采用 **四层搜索 + 质量触发补强** 架构：

- **Layer 0 — 工具内置引擎（新增）**：运行时自动探测当前工具的内置搜索引擎（如 `websearch` / `web_search`）。如果可用，以此为主力搜索引擎，与后续层并行发出。无需额外配置。
- **Layer 1 — 大纲建议源**：阶段1 根据主题定向推荐权威域名（如 moe.gov.cn、stats.gov.cn），用内置引擎做 `site:` 定向搜索。
- **Layer 2 — sources.json 优质源**：skill 内置 30+ 精选源（Semantic Scholar / arXiv / Nature / World Bank / IMF / Reuters / BBC / 百度百科 / 知乎 / 36氪 / 艾瑞 / 东方财富 等）。启动时自动健康检测，死源跳过。
- **Layer 3 — 免费源补强（兜底）**：当 Layers 0-2 合计结果质量不足（URL < 3 / 年份过旧 / 来源过少）时触发。DuckDuckGo / Bing / Brave / Mojeek / Semantic Scholar / GDELT / arXiv + 百度百科 / 知乎 / 199IT / 艾瑞 / 36氪 / 澎湃 / 东方财富 / 微博 / CSDN / 虎嗅 / 豆瓣 等 20+ 源。不依赖任何 API Key，永远可用。

**2. 如何使用本地资料生成报告？**

Skill 内置了离线模式，可以根据本地文件直接生成带有完整格式（目录/引用/元数据）的调研报告。支持的文件格式：**MD / TXT**（原生读取）、**PDF**（AI 自动安装 pypdf 提取文本）、**DOCX**（AI 自动安装 python-docx 解析）。

根据你的需要选择以下场景：

**场景 1：本地资料 + 联网补充**（推荐，调研最完整）
```
请使用 deep-research 这个 skill，根据 D:\我的笔记\项目A 的本地资料，生成一份关于 XX 的研究报告（quick 模式）。本地资料里的内容优先作为素材，不够的你在网上搜索补充。
```

**场景 2：只用本地资料，不联网**（适合资料足够、担心联网干扰主题的情况）
```
请使用 deep-research 这个 skill，根据 D:\我的笔记\项目A 的本地资料，生成一份关于 XX 的研究报告（quick 模式）。只看本地资料，不要联网搜索。
```
系统会跳过搜索/抓取流程，直接从指定文件提取数据，后续的章节撰写和装配 QA 正常执行。最终输出带有元数据、`[N]` 引用、目录的标准报告。

**场景 3：纯本地，不用 skill**（最轻量，适合不需要专业报告格式的快速总结）
```
根据 D:\我的笔记\项目A 的资料，帮我整理成一份结构化的研究报告，要有目录和章节标题。
```

> **场景选择建议**：资料不够全 → 场景 1（联网补充）；资料足够且需要专业报告格式 → 场景 2（离线模式）；只需快速总结 → 场景 3（最轻量）。

**3. 如何更新到最新版本？**

**版本策略**：`main` 分支始终是最新代码，日常小修改直接推送。GitHub Releases 仅用于里程碑版本标记（如 v2.1.0 → v2.2.0），不必等到新 Release 才更新。

任意工具的用户：

- **自动**：输入 `/research-update`，AI 自动执行 `git pull` 获取最新
- **手动**：`cd <skill 安装目录>/deep-research && git pull`

版本号可通过 `cat <skill 安装目录>/deep-research/VERSION` 查看。

**4. 其他工具能自动更新吗？**

可以。所有工具共用同一套所有平台通用代码，直接在安装目录 `git pull` 即可（或让 AI 帮你执行）。没有平台特定的适配改动需要保留，因此更新不会产生冲突。

**5. 数据安全吗？**

所有处理在本地完成。不收集、不上传任何用户数据。

## 十二、运行截图

<img width="1532" height="836" alt="Screenshot 2026-06-09 at 11-28-17" src="https://github.com/user-attachments/assets/736b0113-f054-4dba-b018-e656a51a9fb4" />

<img width="1532" height="932" alt="Screenshot 2026-06-09 at 11-30-13" src="https://github.com/user-attachments/assets/a88cbf27-7b6c-4ea3-8b51-424f48bf9906" />

<img width="1524" height="846" alt="Screenshot 2026-06-09 at 11-30-55" src="https://github.com/user-attachments/assets/ef10865d-3a72-4658-ac9c-28b2221e77f5" />

<img width="1528" height="840" alt="Screenshot 2026-06-09 at 11-32-13" src="https://github.com/user-attachments/assets/506e91eb-1d5d-4312-aceb-9280d357e264" />

<img width="1438" height="842" alt="Screenshot 2026-06-09 at 11-35-03" src="https://github.com/user-attachments/assets/75acd450-9349-4024-923d-f9b14ea601dd" />

---

## License / 协议

MIT

This project uses MIT instead of GPL/CC because its core value is a portable methodology and pipeline design, not a copyrighted product. MIT maximizes reuse and adaptation across different platforms and toolchains, consistent with the "all-platform" positioning.

本项目采用 MIT 协议。选择 MIT 而非 GPL/CC 等更严格的协议，是因为本项目的核心是一套可移植的方法论和管道设计，而非需要保护版权的成品库。MIT 能让它在不同平台和工具链中被最大化地复用和改造，与"所有平台通用"的定位一致。

---

## Star History / 星标历史

<a href="https://www.star-history.com/?repos=hoolulu%2Fdeep-research">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=hoolulu/deep-research&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=hoolulu/deep-research&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=hoolulu/deep-research&type=date&legend=top-left" />
  </picture>
</a>

---

**Created by [hoolulu](https://github.com/hoolulu)** · [github.com/hoolulu/deep-research](https://github.com/hoolulu/deep-research)

> Community discussion · 社区讨论：[LINUX DO](https://linux.do/t/topic/2312664)
