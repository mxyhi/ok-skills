# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw 等工具的 AI Agent Skills 集合

[English](README.md) | 简体中文 | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

这是一个面向 Codex、Claude Code、Cursor、OpenClaw、Trae 以及其他兼容 `SKILL.md` / `AGENTS.md` 工作流工具的技能仓库。

当前仓库共收录 **36 个可复用技能**：其中 **28 个顶层技能** 由本仓直接维护，另有 **8 个 GSAP 动画技能** 以 vendored bundle 形式放在 [`gsap-skills/`](gsap-skills/) 下。把它 clone 到 `~/.agents/skills/ok-skills` 即可，仓库内部目录已经符合 `AGENTS.md` 所需的 skills 规范。

如果你在找 **Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、可复用的 **AGENTS.md** 模板，或者一套能直接落地的 **SKILL.md** 示例仓库，这个项目就是为搜索可发现性和开箱即用而整理的。

**高频使用场景：** 最新文档查询、浏览器自动化、GitHub Actions 排障、提示工程、复杂任务规划、前端设计，以及 PDF / Word / PPTX / XLSX 内容处理。

## 适合谁

- 你在用 Codex、Claude Code、Cursor、OpenClaw、Trae 或其他 AI coding agent，希望复用技能而不是每次临时写 prompt。
- 你在维护 `AGENTS.md` / `SKILL.md` 体系，希望不同项目之间可以迁移同一套工作流。
- 你需要现成的文档查询、浏览器自动化、GitHub 工作流、规划、提示工程、前端设计、PDF、Office 文档、演示文稿和表格类技能。

## 建议先装这几个

如果你第一次用这个仓库，优先从下面几个技能开始：

- [brainstorming](brainstorming/SKILL.md)：在进入实现前先梳理想法、需求和设计。
- [planning-with-files](planning-with-files/SKILL.md)：复杂任务、调研任务、多轮推进任务的文件化规划。
- [find-docs](find-docs/SKILL.md)：查询最新库文档、API 参考和 Context7 示例。
- [agent-browser](agent-browser/SKILL.md)：浏览器自动化、截图、抓取、表单填写、Web QA。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：读取 GitHub Actions 失败日志并产出修复方案。

## 1 分钟快速开始

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 后仓库位于 `~/.agents/skills/ok-skills`，其内部目录已经符合预期布局：

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

然后在 `AGENTS.md` 里加最小触发规则：

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

- [brainstorming](brainstorming/SKILL.md)：在进入实现前先梳理想法、需求和设计。
- [planning-with-files](planning-with-files/SKILL.md)：通过 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md)：发现能提升 locality、leverage、可测试性和 AI 可导航性的架构 deepening 机会。
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)：把测试里的 `as` 类型断言迁移到 `@total-typescript/shoehorn`。
- [test-driven-development](test-driven-development/SKILL.md)：任何功能或修复先写测试。
- [systematic-debugging](systematic-debugging/SKILL.md)：遇到 bug、测试失败或异常行为时，先系统化追根因，再提出修复。

### GitHub 工作流

- [gh-address-comments](gh-address-comments/SKILL.md)：用 `gh` 处理当前分支 PR 的 review / issue 评论。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：读取 GitHub Actions 失败日志并制定修复计划。
- [yeet](yeet/SKILL.md)：仅在用户明确要求用 `gh` 一次性完成 stage、commit、push 并创建 GitHub PR 时使用。

### 自动化与 QA

- [agent-browser](agent-browser/SKILL.md)：浏览器导航、表单、截图、抓取和网页测试。
- [browser-use](browser-use/SKILL.md)：持续式浏览器自动化 CLI，用于导航、页面状态检查、表单填写、截图和信息提取。
- [opencli](opencli/opencli-usage/SKILL.md)：将网站变成 CLI，复用浏览器登录态，支持公共 API 访问和 AI 生成适配器。
- [dogfood](dogfood/SKILL.md)：系统化探索测试，并输出可复现证据。
- [electron](electron/SKILL.md)：通过 Chrome DevTools Protocol 自动化 Electron 桌面应用。

`dogfood/` 和 `electron/` 仍然 vendored 自 `vercel-labs/agent-browser`，但 upstream 在提交 `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` 中把它们从 `skills/` 挪到了 `skill-data/`，这样 installer 的发现逻辑只会暴露引导用的 `agent-browser` skill。本仓仍把这两个 specialized skills 保留为顶层目录，因为它们依然由 upstream 维护，并且可以直接使用。

### 前端与设计

- [ai-elements](ai-elements/SKILL.md)：为 `ai-elements` 组件库创建 AI 聊天界面组件。
- [frontend-skill](frontend-skill/SKILL.md)：适用于需要强视觉表现的落地页、网站、应用、原型、演示或游戏 UI。
- [shader-dev](shader-dev/SKILL.md)：覆盖 GLSL 着色器的系统化技巧，用于构建兼容 ShaderToy 的实时视觉效果。
- [better-icons](better-icons/SKILL.md)：通过 CLI 或 MCP 搜索、浏览并获取 200+ Iconify 图标库中的 SVG 图标。
- [`gsap-skills/`](gsap-skills/)：8 个官方 GSAP 动画技能包，覆盖 core、timeline、ScrollTrigger、plugins、utils、React、performance、frameworks。

### 工具与内容生产

- [minimax-docx](minimax-docx/SKILL.md)：基于 OpenXML SDK（.NET）的专业 DOCX 创建、编辑与格式编排。
- [minimax-pdf](minimax-pdf/SKILL.md)：使用 token 化设计系统生成、填写和重排 PDF 文档。
- [pptx-generator](pptx-generator/SKILL.md)：使用 PptxGenJS、XML 工作流或 markitdown 生成、编辑和读取 PowerPoint 演示文稿。
- [minimax-xlsx](minimax-xlsx/SKILL.md)：以低损 XML 工作流打开、创建、读取、分析、编辑和校验 Excel / 表格文件。

## Vendored Skill Packs

[`gsap-skills/`](gsap-skills/) 目录收录了来自 [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) 的 GSAP 动画技能包，当前同步基于提交 `aed9cfd3277740755f6bfc1155c7aa645403b760`。

其中包括：

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

归属和法律文件保存在 [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) 与 [`gsap-skills/LICENSE`](gsap-skills/LICENSE)。

[`planning-with-files/`](planning-with-files/) 对应的上游基线是 [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)。本仓保留通用的 `planning-with-files` 名称，并移除 Pi 专属包元数据，使其继续兼容标准 `SKILL.md` 工作流。

## 常见前置条件

- 部分 GitHub 相关技能默认你已经安装并登录 `gh`。
- 浏览器类技能通常需要可用的 Chrome/CDP 环境。
- 文档查询类技能可能依赖额外 CLI 或 MCP 工具，请以各自的 `SKILL.md` 为准。

## 完整技能索引

`Source URL` 列优先指向技能的 canonical upstream；如果没有单独上游，则指向当前仓库内该技能目录的 GitHub 地址。

### 顶层技能

| 技能                                                                | 说明                                                                                                                                           | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | 面向 AI agents 的浏览器自动化：导航、表单、截图、数据提取、网页测试。                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | 为 ai-elements 组件库创建新的 AI 聊天界面组件，遵循可组合模式与 shadcn/ui 约定。                                                               | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | 通过 CLI 或 MCP 工具搜索 200+ Iconify 图标库并获取 SVG 图标。                                                                                  | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | 通过协作式对话把想法整理成经确认的设计与规格，再进入实现。                                                                                                       | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | 持续式浏览器自动化 CLI，用于导航、页面状态检查、表单填写、截图和信息提取。                                                                     | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | 用“洞穴人”式极简表达压缩回复 tokens，同时保留完整技术准确性，并支持多档强度。                                                                  | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [find-docs](find-docs/SKILL.md)                                     | 使用 Context7 CLI 查询最新文档、API 参考和代码示例。                                                                                           | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | 基于 OpenXML SDK（.NET）的专业 DOCX 创建、编辑与格式编排。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | 使用 Exa 做网页、代码和公司调研。                                                                                                              | 自制                                                                                                                           |
| [find-skills](find-skills/SKILL.md)                                 | 当用户需要特定能力时，发现已有技能。                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | 构建具有强视觉表现的落地页、网站、应用、原型、演示或游戏 UI。                                                                                  | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | 覆盖 GLSL 着色器的系统化技巧，用于构建兼容 ShaderToy 的实时视觉效果。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | 在写第三方 API / SDK 代码前先抓当前文档。                                                                                                      | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | 用 `gh` 处理当前分支 PR 的评审和 issue 评论。                                                                                                  | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | 检查 GitHub Actions 失败项、提取日志并制定修复方案。                                                                                           | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | 发现能提升 locality、leverage、可测试性和 AI 可导航性的架构 deepening 机会。                                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture)                              |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | 把测试文件中的 `as` 类型断言迁移到 `@total-typescript/shoehorn`。                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/migrate-to-shoehorn)                                        |
| [opensrc](opensrc/SKILL.md)                                         | 抓取依赖源码，给 AI agents 提供更深的实现上下文。                                                                                              | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | 将网站变成 CLI，复用浏览器登录态，支持公共 API 访问和 AI 生成适配器。                                                                          | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | 系统化测试 Web 应用，并产出附截图和录屏的问题报告。                                                                                            | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | 通过 agent-browser 和 Chrome DevTools Protocol 自动化 Electron 桌面应用。                                                                      | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | 使用 token 化设计系统生成、填写和重排 PDF 文档。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | 用 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。                                                                                 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | 使用 PptxGenJS、XML 工作流或 markitdown 生成、编辑和读取 PowerPoint 演示文稿。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [test-driven-development](test-driven-development/SKILL.md)         | 实现任何功能或修复前先使用。                                                                                                                   | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [systematic-debugging](systematic-debugging/SKILL.md)             | 遇到任何 bug、测试失败或异常行为时，在提出修复前先使用。                                                                                     | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 以低损 XML 工作流打开、创建、读取、分析、编辑和校验 Excel / 表格文件。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | 仅在用户明确要求用 `gh` 一次性完成 stage、commit、push 并创建 GitHub PR 时使用。                                                               | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

说明：
- `dogfood` 和 `electron` 的上游路径在 `skill-data/`，不在 upstream 的 `skills/`。
- upstream 在提交 `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` 中迁移了这些 specialized skills，以便 installer 发现逻辑只找到引导 skill `agent-browser`。
- 本仓有意继续把它们作为顶层 vendored skills 保留，因为它们仍在 upstream 持续维护，且具备直接使用价值。

### Vendored `gsap-skills/` 技能

| 技能                                                          | 说明                                                                                           | Source URL                                                                                            |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | 核心 API：`gsap.to()` / `from()` / `fromTo()`，缓动、duration、stagger、defaults、matchMedia。 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timeline：时序编排、position 参数、labels、嵌套与播放控制。                                    | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger：滚动驱动动画、pin、scrub、触发器、refresh、清理。                               | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | 插件：Flip、Draggable、MotionPath、ScrollToPlugin、CustomEase 等。                             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils：clamp、mapRange、normalize、random、snap、toArray、wrap、pipe。                    | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React：useGSAP、refs、`gsap.context()`、清理、SSR。                                            | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | 性能：transform 优先、will-change、批处理、ScrollTrigger 性能建议。                            | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue、Svelte 等：生命周期、选择器作用域、卸载清理。                                             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## 贡献

欢迎为现有技能改进或新增技能。

1. 触发条件要明确且可验证。
2. 示例尽量简洁，强调可执行性。
3. 若依赖外部工具，请在 `SKILL.md` 中明确标注依赖。
4. 新增或重命名技能时，请同步更新 `README.md` 与 `README.zh-CN.md`；如果公开技能索引发生变化，也请一并刷新其他翻译版 README。

## 许可证

本仓库主许可证见 [LICENSE](LICENSE)。

部分技能目录包含额外许可证或归属说明文件，包括 [`caveman/`](caveman/)、[`improve-codebase-architecture/`](improve-codebase-architecture/)、[`migrate-to-shoehorn/`](migrate-to-shoehorn/)、[`minimax-docx/`](minimax-docx/) 和 [`gsap-skills/`](gsap-skills/)。
