# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw 等工具的 AI Agent Skills 集合

[English](README.md) | 简体中文 | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

这是一个面向 Codex、Claude Code、Cursor、OpenClaw、Trae 以及其他兼容 `SKILL.md` / `AGENTS.md` 工作流工具的技能仓库。

当前仓库共收录 **57 个可复用技能**：其中 **31 个顶层技能** 由本仓直接维护，另有 **18 个前端设计技能** 以 vendored bundle 形式放在 [`impeccable/`](impeccable/README.md) 下，另有 **8 个 GSAP 动画技能** 以 vendored bundle 形式放在 [`gsap-skills/`](gsap-skills/) 下。把它 clone 到 `~/.agents/skills/ok-skills` 即可，仓库内部目录已经符合 `AGENTS.md` 所需的 skills 规范。

如果你在找 **Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、可复用的 **AGENTS.md** 模板，或者一套能直接落地的 **SKILL.md** 示例仓库，这个项目就是为搜索可发现性和开箱即用而整理的。

**高频使用场景：** 最新文档查询、浏览器自动化、GitHub Actions 排障、提示工程、复杂任务规划、前端设计，以及 PDF / Word / PPTX / XLSX 内容处理。

## 适合谁

- 你在用 Codex、Claude Code、Cursor、OpenClaw、Trae 或其他 AI coding agent，希望复用技能而不是每次临时写 prompt。
- 你在维护 `AGENTS.md` / `SKILL.md` 体系，希望不同项目之间可以迁移同一套工作流。
- 你需要现成的文档查询、浏览器自动化、GitHub 工作流、规划、提示工程、前端设计、PDF、Office 文档、演示文稿和表格类技能。

## 建议先装这几个

如果你第一次用这个仓库，优先从下面几个技能开始：

- [planning-with-files](planning-with-files/SKILL.md)：复杂任务、调研任务、多轮推进任务的文件化规划。
- [context7-cli](context7-cli/SKILL.md)：查询最新库文档、Context7 资料和 MCP 相关内容。
- [agent-browser](agent-browser/SKILL.md)：浏览器自动化、截图、抓取、表单填写、Web QA。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：读取 GitHub Actions 失败日志并产出修复方案。
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md)：更稳定、可控的生产级提示工程模式。
- [impeccable](impeccable/impeccable/SKILL.md)：核心 impeccable 设计技能，以及一整套配套设计命令。

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
  context7-cli/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

然后在 `AGENTS.md` 里加最小触发规则：

```md
## Skills

- planning-with-files: 复杂任务、调研任务、或者预计会有 5 次以上工具调用时使用。
- context7-cli: 需要最新库文档、API 参考或 Context7 示例时使用。
- agent-browser: 需要浏览器自动化、截图、抓取、网页测试或表单填写时使用。
```

之后就可以自然触发：

- `在重构这个模块之前先用 planning-with-files。`
- `用 context7-cli 查一下这个 SDK 的最新文档。`
- `用 agent-browser 复现这个 UI 问题。`

## 按场景浏览技能

### 调研与文档

- [context7-cli](context7-cli/SKILL.md)：官方 Context7 CLI 的文档查询、skill 管理与 MCP 配置工作流。
- [exa-search](exa-search/SKILL.md)：用 Exa 做网页、代码、公司调研。
- [get-api-docs](get-api-docs/SKILL.md)：写第三方 API / SDK 代码前先拉当前文档。
- [find-skills](find-skills/SKILL.md)：当用户提出能力诉求时，先查有没有现成 skill 可用。

### 规划与提示工程

- [planning-with-files](planning-with-files/SKILL.md)：通过 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md)：生产环境可用的高级提示工程模式。
- [subagent-driven-development](subagent-driven-development/SKILL.md)：在当前会话内执行彼此独立的实现任务，用全新 subagent 和分阶段评审推进计划。
- [test-driven-development](test-driven-development/SKILL.md)：任何功能或修复先写测试。

### GitHub 工作流

- [gh-address-comments](gh-address-comments/SKILL.md)：用 `gh` 处理当前分支 PR 的 review / issue 评论。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：读取 GitHub Actions 失败日志并制定修复计划。
- [yeet](yeet/SKILL.md)：仅在用户明确要求用 `gh` 一次性完成 stage、commit、push 并创建 GitHub PR 时使用。

### 自动化与 QA

- [agent-browser](agent-browser/SKILL.md)：浏览器导航、表单、截图、抓取和网页测试。
- [browser-use](browser-use/SKILL.md)：持续式浏览器自动化 CLI，用于导航、页面状态检查、表单填写、截图和信息提取。
- [bb-browser](bb-browser/SKILL.md)：通过用户真实浏览器和登录态进行信息获取与浏览器自动化。
- [pinchtab](pinchtab/SKILL.md)：通过 Pinchtab 本地 HTTP API 控制 Chrome，使用稳定的 accessibility refs 做自动化与提取。
- [electron](electron/SKILL.md)：通过 Chrome DevTools Protocol 自动化 Electron 桌面应用。
- [opencli](opencli/opencli-usage/SKILL.md)：将网站变成 CLI，复用浏览器登录态，支持公共 API 访问和 AI 生成适配器。
- [dogfood](dogfood/SKILL.md)：系统化探索测试，并输出可复现证据。

### 前端与设计

- [ai-elements](ai-elements/SKILL.md)：为 `ai-elements` 组件库创建 AI 聊天界面组件。
- [frontend-skill](frontend-skill/SKILL.md)：适用于需要强视觉表现的落地页、网站、应用、原型、演示或游戏 UI。
- [shader-dev](shader-dev/SKILL.md)：覆盖 GLSL 着色器的系统化技巧，用于构建兼容 ShaderToy 的实时视觉效果。
- [better-icons](better-icons/SKILL.md)：通过 CLI 或 MCP 搜索、浏览并获取 200+ Iconify 图标库中的 SVG 图标。
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md)：来自 Vercel Engineering 的 React / Next.js 性能实践。
- [remotion-best-practices](remotion-best-practices/SKILL.md)：基于 React 的 Remotion 视频开发实践。
- [`gsap-skills/`](gsap-skills/)：8 个官方 GSAP 动画技能包，覆盖 core、timeline、ScrollTrigger、plugins、utils、React、performance、frameworks。
- [`impeccable/`](impeccable/README.md)：18 个 vendored 前端设计技能，包含 `impeccable`、`adapt`、`audit`、`polish` 等。

### 工具与内容生产

- [minimax-docx](minimax-docx/SKILL.md)：基于 OpenXML SDK（.NET）的专业 DOCX 创建、编辑与格式编排。
- [minimax-pdf](minimax-pdf/SKILL.md)：使用 token 化设计系统生成、填写和重排 PDF 文档。
- [pptx-generator](pptx-generator/SKILL.md)：使用 PptxGenJS、XML 工作流或 markitdown 生成、编辑和读取 PowerPoint 演示文稿。
- [minimax-xlsx](minimax-xlsx/SKILL.md)：以低损 XML 工作流打开、创建、读取、分析、编辑和校验 Excel / 表格文件。
- [skill-creator](skill-creator/SKILL.md)：创建或更新技能，补齐结构、文档和工具集成。

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) 目录收录了来自 [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) 的前端设计技能包，当前同步基于提交 `00d485659af82982aef0328d0419c49a2716d123`。

其中包括：

- `impeccable` 主技能
- `adapt`、`animate`、`audit`、`bolder`、`clarify`、`colorize`、`critique`、`delight`、`distill`
- `harden`, `layout`, `optimize`, `overdrive`, `polish`, `quieter`, `shape`, `typeset`

归属和法律文件保存在 [`impeccable/NOTICE.md`](impeccable/NOTICE.md) 与 [`impeccable/LICENSE`](impeccable/LICENSE)。

[`gsap-skills/`](gsap-skills/) 目录收录了来自 [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) 的 GSAP 动画技能包，当前同步基于提交 `4300e310513b0ddc0b121a5c0e0bd2e5c2325ff2`。

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
| [bb-browser](bb-browser/SKILL.md)                                   | 通过用户真实浏览器和登录态完成信息获取与浏览器自动化，覆盖公开页面、内部系统和登录后流程。                                                     | [epiral/bb-browser](https://github.com/epiral/bb-browser/tree/main/skills/bb-browser)                                          |
| [better-icons](better-icons/SKILL.md)                               | 通过 CLI 或 MCP 工具搜索 200+ Iconify 图标库并获取 SVG 图标。                                                                                  | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [browser-use](browser-use/SKILL.md)                                 | 持续式浏览器自动化 CLI，用于导航、页面状态检查、表单填写、截图和信息提取。                                                                     | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | 用“洞穴人”式极简表达压缩回复 tokens，同时保留完整技术准确性，并支持多档强度。                                                                  | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [context7-cli](context7-cli/SKILL.md)                               | 使用 Context7 CLI 完成文档查询、skill 管理和 MCP 配置。                                                                                        | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli)                                        |
| [minimax-docx](minimax-docx/SKILL.md) | 基于 OpenXML SDK（.NET）的专业 DOCX 创建、编辑与格式编排。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [dogfood](dogfood/SKILL.md)                                         | 系统化测试 Web 应用，并产出附截图和录屏的问题报告。                                                                                            | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood)                             |
| [electron](electron/SKILL.md)                                       | 通过 agent-browser 和 Chrome DevTools Protocol 自动化 Electron 桌面应用。                                                                      | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron)                            |
| [exa-search](exa-search/SKILL.md)                                   | 使用 Exa 做网页、代码和公司调研。                                                                                                              | 自制                                                                                                                           |
| [find-skills](find-skills/SKILL.md)                                 | 当用户需要特定能力时，发现已有技能。                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | 构建具有强视觉表现的落地页、网站、应用、原型、演示或游戏 UI。                                                                                  | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | 覆盖 GLSL 着色器的系统化技巧，用于构建兼容 ShaderToy 的实时视觉效果。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | 在写第三方 API / SDK 代码前先抓当前文档。                                                                                                      | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | 用 `gh` 处理当前分支 PR 的评审和 issue 评论。                                                                                                  | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | 检查 GitHub Actions 失败项、提取日志并制定修复方案。                                                                                           | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [opensrc](opensrc/SKILL.md)                                         | 抓取依赖源码，给 AI agents 提供更深的实现上下文。                                                                                              | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | 将网站变成 CLI，复用浏览器登录态，支持公共 API 访问和 AI 生成适配器。                                                                          | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [minimax-pdf](minimax-pdf/SKILL.md) | 使用 token 化设计系统生成、填写和重排 PDF 文档。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [pinchtab](pinchtab/SKILL.md)                                       | 通过 Pinchtab 的 HTTP API 控制 headless 或 headed Chrome，用于网页自动化、抓取、表单填写、导航、截图和基于稳定 accessibility refs 的内容提取。 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skills/pinchtab)                                            |
| [planning-with-files](planning-with-files/SKILL.md)                 | 用 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。                                                                                 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/skills/planning-with-files)       |
| [pptx-generator](pptx-generator/SKILL.md) | 使用 PptxGenJS、XML 工作流或 markitdown 生成、编辑和读取 PowerPoint 演示文稿。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | 面向生产环境的高级提示工程模式。                                                                                                               | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md)         | 用于 React + Remotion 视频开发的最佳实践。                                                                                                     | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion)                                        |
| [skill-creator](skill-creator/SKILL.md)                             | 创建或更新技能，补齐专业知识、工作流与工具集成。                                                                                               | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator)                                       |
| [subagent-driven-development](subagent-driven-development/SKILL.md) | 在当前会话内执行包含独立任务的实现计划，使用全新 subagent 和分阶段评审。                                                                       | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development)                           |
| [test-driven-development](test-driven-development/SKILL.md)         | 实现任何功能或修复前先使用。                                                                                                                   | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development)                               |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | 来自 Vercel Engineering 的 React / Next.js 性能优化实践。                                                                                      | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 以低损 XML 工作流打开、创建、读取、分析、编辑和校验 Excel / 表格文件。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | 仅在用户明确要求用 `gh` 一次性完成 stage、commit、push 并创建 GitHub PR 时使用。                                                               | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

### Vendored `impeccable/` 技能

| 技能                                                     | 说明                                         | Source URL                                                  |
| -------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| [impeccable](impeccable/impeccable/SKILL.md)   | 创建有辨识度、生产级的高质量前端界面。       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md)                       | 让设计适配不同屏幕尺寸、设备和上下文。       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md)                   | 用有目的的动画和微交互增强界面。             | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md)                       | 审计界面的可访问性、性能、主题与响应式表现。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md)                     | 让过于保守或平淡的设计更有张力。             | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md)                   | 改善不清晰的 UX 文案与说明。                 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md)                 | 为过于单色的界面加入策略性色彩。             | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md)                 | 从 UX 视角评估设计效果。                     | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md)                   | 为界面加入个性和让人记住的细节。             | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md)                   | 把设计提炼到本质，去掉多余复杂度。           | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md)                     | 提升错误处理、i18n、溢出和边界情况的韧性。   | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [layout](impeccable/layout/SKILL.md)                       | 改善布局、间距与视觉节奏。                                                                              | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md)                 | 优化加载、渲染、动画、图片和包体积。         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [overdrive](impeccable/overdrive/SKILL.md)                 | 通过更激进的技术实现把界面推到常规上限之外。                                                                     | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md)                     | 上线前打磨对齐、间距、一致性和细节。         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md)                   | 降低过强的视觉攻击性，同时保持质量。         | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [shape](impeccable/shape/SKILL.md)                         | 在写代码前先规划功能的 UX / UI。                                                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [typeset](impeccable/typeset/SKILL.md)                     | 优化字体选择、层级、字号、字重与可读性。                                                                       | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

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

部分技能目录包含额外许可证或归属说明文件，包括 [`caveman/`](caveman/)、[`minimax-docx/`](minimax-docx/)、[`impeccable/`](impeccable/README.md)、[`gsap-skills/`](gsap-skills/) 和 [`skill-creator/`](skill-creator/)。
