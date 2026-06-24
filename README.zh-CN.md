# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw 等工具的 AI Agent Skills 集合

[English](README.md) | 简体中文 | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

这是一个面向 Codex、Claude Code、Cursor、OpenClaw、Trae 以及其他兼容 `SKILL.md` / `CLAUDE.md` / `AGENTS.md` 工作流工具的技能仓库。

当前仓库共收录 **30 个可复用技能**，全部作为顶层技能目录由本仓直接维护。把它 clone 到 `~/.agents/skills/ok-skills` 即可，仓库内部目录已经符合 `AGENTS.md` 所需的 skills 规范，[`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) 则提供面向 Claude Code 的 agent playbook。

如果你在找 **Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、可复用的 **CLAUDE.md / AGENTS.md** 模板，或者一套能直接落地的 **SKILL.md** 示例仓库，这个项目就是为搜索可发现性和开箱即用而整理的。

**高频使用场景：** 最新文档查询、浏览器自动化、提示工程、复杂任务规划、前端设计，以及 PDF / Word / PPTX / XLSX 内容处理。

## 适合谁

- 你在用 Codex、Claude Code、Cursor、OpenClaw、Trae 或其他 AI coding agent，希望复用技能而不是每次临时写 prompt。
- 你在维护 `CLAUDE.md` / `AGENTS.md` / `SKILL.md` 体系，希望不同项目之间可以迁移同一套工作流。
- 你需要现成的文档查询、浏览器自动化、规划、提示工程、前端设计、PDF、Office 文档、演示文稿和表格类技能。

## 建议先装这几个

如果你第一次用这个仓库，优先从下面几个技能开始：

- [planning-with-files](planning-with-files/SKILL.md)：复杂任务、调研任务、多轮推进任务的文件化规划。
- [find-docs](find-docs/SKILL.md)：查询最新库文档、API 参考和 Context7 示例。
- [agent-browser](agent-browser/SKILL.md)：浏览器自动化、截图、抓取、表单填写、Web QA。

## 1 分钟快速开始

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 后仓库位于 `~/.agents/skills/ok-skills`，其内部目录已经符合预期布局：

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

Claude Code 或 Codex 的全局指令可以从 [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) 开始，然后复制或合并到 Claude Code 的 `CLAUDE.md` 或 Codex 的 `AGENTS.md`。它内置中文优先、KISS、最新文档/源码检查、多 agent 优先、默认启用 `caveman` / `planning-with-files` / `karpathy-guidelines`、严格 TypeScript 约束和 context-mode 路由规则。复用前请按项目编辑 `语言要求` 小节；`其他注意项` 是项目本地配置，可按需编辑。

然后在 `AGENTS.md` 里加最小触发规则，或把同样的 skill 触发规则合并进 `CLAUDE.md` / `AGENTS.md`：

```md
## Skills

- planning-with-files: 复杂任务、调研任务、或者预计会有 5 次以上工具调用时使用。
- find-docs: 需要最新库文档、API 参考或 Context7 示例时使用。
- agent-browser: 需要浏览器自动化、截图、抓取、网页测试或表单填写时使用。
```

之后就可以自然触发：

- `在重构这个模块之前先用 planning-with-files。`
- `用 find-docs 查一下这个 SDK 的最新文档。`
- `用 agent-browser 复现这个 UI 问题。`

## 按场景浏览技能

### 调研与文档

- [find-docs](find-docs/SKILL.md)：专注于最新文档查询的 Context7 CLI 工作流。
- [exa-search](exa-search/SKILL.md)：用 Exa 做网页、代码、公司调研。
- [get-api-docs](get-api-docs/SKILL.md)：写第三方 API / SDK 代码前先拉当前文档。
- [find-skills](find-skills/SKILL.md)：当用户提出能力诉求时，先查有没有现成 skill 可用。

### 规划与提示工程

- [planning-with-files](planning-with-files/SKILL.md)：通过 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。
- [autoresearch](autoresearch/SKILL.md)：以明确目标、度量、验证循环和保留/丢弃门禁驱动自主迭代。
- [diagnosing-bugs](diagnosing-bugs/SKILL.md)：面向疑难 bug 与性能回归的严格诊断循环。
- [grill-me](grill-me/SKILL.md)：通过一次一个问题的追问，压力测试计划或设计直到达成共识。
- [grill-with-docs](grill-with-docs/SKILL.md)：用领域语言、`CONTEXT.md` 与 ADR 压测计划，并在决策明确时同步更新文档。
- [grilling](grilling/SKILL.md): reusable one-question-at-a-time interview loop behind `grill-me` and `grill-with-docs`.
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [codebase-design](codebase-design/SKILL.md): shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md)：发现能提升 locality、leverage、可测试性和 AI 可导航性的架构 deepening 机会。
- [karpathy-guidelines](karpathy-guidelines/SKILL.md)：减少过度复杂、隐藏假设和不可验证改动的编码行为准则。
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)：把测试里的 `as` 类型断言迁移到 `@total-typescript/shoehorn`。
- [tdd](tdd/SKILL.md)：功能、修复、重构或行为变更前执行 test-first red-green-refactor。
- [systematic-debugging](systematic-debugging/SKILL.md)：遇到 bug、测试失败或异常行为时，先系统化追根因，再提出修复。

### 自动化与 QA

- [agent-browser](agent-browser/SKILL.md)：浏览器导航、表单、截图、抓取和网页测试。
- [kimi-webbridge](kimi-webbridge/SKILL.md)：通过本地守护进程控制用户真实浏览器，用于导航、表单填写、截图、页面读取和登录态会话。
- [browser-trace](browser-trace/SKILL.md)：采集浏览器自动化运行的 CDP trace、截图和 DOM dump，并按页面拆分以便调试。
- [opencli](opencli/opencli-usage/SKILL.md)：将网站变成 CLI，复用浏览器登录态，支持公共 API 访问和 AI 生成适配器。
- [xquik-twitter](xquik-twitter/SKILL.md)：通过 Xquik API 搜索 X/Twitter 数据，并执行需确认的账号操作。

### 前端与设计

- [ai-elements](ai-elements/SKILL.md)：为 `ai-elements` 组件库创建 AI 聊天界面组件。
- [huashu-design](huashu-design/SKILL.md)：用 HTML 交付高保真原型、交互 Demo、幻灯片、动画、设计变体、视频导出和设计评审。
- [better-icons](better-icons/SKILL.md)：通过 CLI 或 MCP 搜索、浏览并获取 200+ Iconify 图标库中的 SVG 图标。

### 工具与内容生产

- [minimax-docx](minimax-docx/SKILL.md)：基于 OpenXML SDK（.NET）的专业 DOCX 创建、编辑与格式编排。
- [minimax-pdf](minimax-pdf/SKILL.md)：使用 token 化设计系统生成、填写和重排 PDF 文档。
- [pptx-generator](pptx-generator/SKILL.md)：使用 PptxGenJS、XML 工作流或 markitdown 生成、编辑和读取 PowerPoint 演示文稿。
- [huashu-design](huashu-design/SKILL.md)：制作 HTML deck、可编辑 PPTX、MP4/GIF 动画和带解说的设计视频。
- [minimax-xlsx](minimax-xlsx/SKILL.md)：以低损 XML 工作流打开、创建、读取、分析、编辑和校验 Excel / 表格文件。

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) 对应的上游基线是 [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)。本仓将该上游目录作为本地技能的规范基线；本地差异仅限兼容 `skills-ref` 的 `SKILL.md` frontmatter，以及不依赖安装位置的相对脚本路径说明。

## 常见前置条件

- 浏览器类技能通常需要可用的 Chrome/CDP 环境。
- 文档查询类技能可能依赖额外 CLI 或 MCP 工具，请以各自的 `SKILL.md` 为准。

## 完整技能索引

`Source URL` 列优先指向技能的 canonical upstream；如果没有单独上游，则指向当前仓库内该技能目录的 GitHub 地址。

### 顶层技能

| 技能                                                                | 说明                                                                                                                                           | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | 面向 AI agents 的浏览器自动化：导航、表单、截图、数据提取、网页测试。                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | 为 ai-elements 组件库创建新的 AI 聊天界面组件，遵循可组合模式与 shadcn/ui 约定。                                                               | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [autoresearch](autoresearch/SKILL.md)                               | 自主目标导向迭代引擎，覆盖修改、验证、保留/丢弃与重复推进工作流。                                                                          | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | 通过 CLI 或 MCP 工具搜索 200+ Iconify 图标库并获取 SVG 图标。                                                                                  | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | 通过本地守护进程控制用户真实浏览器，用于导航、表单填写、截图、页面读取和登录态会话。                                                          | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [browser-trace](browser-trace/SKILL.md)                             | 采集浏览器自动化调试所需的 CDP trace、截图和 DOM dump。                                                                                     | [browserbase/skills](https://github.com/browserbase/skills/tree/main/skills/browser-trace)                                     |
| [caveman](caveman/SKILL.md)                                         | 用“洞穴人”式极简表达压缩回复 tokens，同时保留完整技术准确性，并支持多档强度。                                                                  | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | 面向疑难 bug 与性能回归的严格诊断循环。                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | 使用 Context7 CLI 查询最新文档、API 参考和代码示例。                                                                                           | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | 基于 OpenXML SDK（.NET）的专业 DOCX 创建、编辑与格式编排。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | 使用 Exa 做网页、代码和公司调研。                                                                                                              | 自制                                                                                                                           |
| [find-skills](find-skills/SKILL.md)                                 | 当用户需要特定能力时，发现已有技能。                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [huashu-design](huashu-design/SKILL.md)                           | 用 HTML 创建高保真原型、交互演示、幻灯片、动画、设计变体、视频导出和设计评审。                                                                | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)                                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | 在写第三方 API / SDK 代码前先抓当前文档。                                                                                                      | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grill-me](grill-me/SKILL.md)                                 | 通过持续追问计划或设计，直到达成共同理解。                                                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)                                |
| [grill-with-docs](grill-with-docs/SKILL.md)                   | 用领域语言、`CONTEXT.md` 与 ADR 压测计划，并内联更新文档。                                                                  | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)                          |
| [grilling](grilling/SKILL.md)                               | Reusable one-question-at-a-time interview loop behind `grill-me` and `grill-with-docs`.                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [codebase-design](codebase-design/SKILL.md)                   | Shared deep-module vocabulary for seams, interfaces, leverage, locality, and testability.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | 发现能提升 locality、leverage、可测试性和 AI 可导航性的架构 deepening 机会。                                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture)                              |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | 减少过度复杂、隐藏假设和不可验证改动的编码行为准则。                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | 把测试文件中的 `as` 类型断言迁移到 `@total-typescript/shoehorn`。                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/misc/migrate-to-shoehorn)                                        |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | 将网站变成 CLI，复用浏览器登录态，支持公共 API 访问和 AI 生成适配器。                                                                          | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [xquik-twitter](xquik-twitter/SKILL.md)                         | 通过 Xquik API 搜索 X/Twitter 数据，并执行需确认的账号操作。                                                                                  | [Xquik-dev/x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper/tree/master/skills/x-twitter-scraper)             |
| [minimax-pdf](minimax-pdf/SKILL.md) | 使用 token 化设计系统生成、填写和重排 PDF 文档。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | 用 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。                                                                                 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | 使用 PptxGenJS、XML 工作流或 markitdown 生成、编辑和读取 PowerPoint 演示文稿。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | 功能、修复、重构或行为变更前使用；优先通过 public interface 做 integration-style 测试。                                                        | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | 遇到任何 bug、测试失败或异常行为时，在提出修复前先使用。                                                                                     | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 以低损 XML 工作流打开、创建、读取、分析、编辑和校验 Excel / 表格文件。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
## 贡献

欢迎为现有技能改进或新增技能。

1. 触发条件要明确且可验证。
2. 示例尽量简洁，强调可执行性。
3. 若依赖外部工具，请在 `SKILL.md` 中明确标注依赖。
4. 新增或重命名技能时，请同步更新 `README.md` 与 `README.zh-CN.md`；如果公开技能索引发生变化，也请一并刷新其他翻译版 README。

## 许可证

本仓库主许可证见 [LICENSE](LICENSE)。
