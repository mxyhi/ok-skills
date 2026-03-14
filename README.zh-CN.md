# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw 等工具的 AI Agent Skills 集合

[English](README.md) | 简体中文 | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

这是一个面向 Codex、Claude Code、Cursor、OpenClaw、Trae 以及其他兼容 `SKILL.md` / `AGENTS.md` 工作流工具的技能仓库。

当前仓库共收录 **41 个可复用技能**：其中 **23 个顶层技能** 由本仓直接维护，另有 **18 个前端设计技能** 以 vendored bundle 形式放在 [`impeccable/`](impeccable/README.md) 下。把它 clone 到 `~/.agents/skills/ok-skills` 即可，仓库内部目录已经符合 `AGENTS.md` 所需的 skills 规范。

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
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md)：高质量前端界面设计技能，以及一整套配套设计命令。

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

- [brainstorming](brainstorming/SKILL.md)：在实现前澄清意图、需求和设计。
- [planning-with-files](planning-with-files/SKILL.md)：通过 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md)：生产环境可用的高级提示工程模式。
- [test-driven-development](test-driven-development/SKILL.md)：任何功能或修复先写测试。

### GitHub 工作流

- [gh-address-comments](gh-address-comments/SKILL.md)：用 `gh` 处理当前分支 PR 的 review / issue 评论。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：读取 GitHub Actions 失败日志并制定修复计划。
- [yeet](yeet/SKILL.md)：仅在用户明确要求用 `gh` 一次性完成 stage、commit、push 并创建 GitHub PR 时使用。

### 自动化与 QA

- [agent-browser](agent-browser/SKILL.md)：浏览器导航、表单、截图、抓取和网页测试。
- [pinchtab](pinchtab/SKILL.md)：通过 Pinchtab 本地 HTTP API 控制 Chrome，使用稳定的 accessibility refs 做自动化与提取。
- [electron](electron/SKILL.md)：通过 Chrome DevTools Protocol 自动化 Electron 桌面应用。
- [dogfood](dogfood/SKILL.md)：系统化探索测试，并输出可复现证据。

### 前端与设计

- [ai-elements](ai-elements/SKILL.md)：为 `ai-elements` 组件库创建 AI 聊天界面组件。
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md)：来自 Vercel Engineering 的 React / Next.js 性能实践。
- [remotion-best-practices](remotion-best-practices/SKILL.md)：基于 React 的 Remotion 视频开发实践。
- [`impeccable/`](impeccable/README.md)：18 个 vendored 前端设计技能，包含 `frontend-design`、`adapt`、`audit`、`polish` 等。

### 工具与内容生产

- [docx](docx/SKILL.md)：创建、读取、编辑和处理 Word 文档，覆盖格式、批注与修订。
- [pdf](pdf/SKILL.md)：读取、生成、审查 PDF，强调渲染后的视觉检查。
- [pptx](pptx/SKILL.md)：创建、读取、编辑和处理演示文稿、模板与幻灯片内容。
- [xlsx](xlsx/SKILL.md)：表格创建、编辑、公式、格式和分析。
- [skill-creator](skill-creator/SKILL.md)：创建或更新技能，补齐结构、文档和工具集成。

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) 目录收录了来自 [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) 的前端设计技能包，当前同步基于提交 `0df1ba59dc80b8b1891ee42eed0ef4e03d7ef165`。

其中包括：

- `frontend-design` 主技能
- `adapt`、`animate`、`audit`、`bolder`、`clarify`、`colorize`、`critique`、`delight`、`distill`
- `extract`、`harden`、`normalize`、`onboard`、`optimize`、`polish`、`quieter`、`teach-impeccable`

归属和法律文件保存在 [`impeccable/NOTICE.md`](impeccable/NOTICE.md) 与 [`impeccable/LICENSE`](impeccable/LICENSE)。

## 常见前置条件

- 部分 GitHub 相关技能默认你已经安装并登录 `gh`。
- 浏览器类技能通常需要可用的 Chrome/CDP 环境。
- 文档查询类技能可能依赖额外 CLI 或 MCP 工具，请以各自的 `SKILL.md` 为准。

## 完整技能索引

`Source URL` 列优先指向技能的 canonical upstream；如果没有单独上游，则指向当前仓库内该技能目录的 GitHub 地址。

### 顶层技能

| 技能 | 说明 | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | 面向 AI agents 的浏览器自动化：导航、表单、截图、数据提取、网页测试。 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | 为 ai-elements 组件库创建新的 AI 聊天界面组件，遵循可组合模式与 shadcn/ui 约定。 | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [brainstorming](brainstorming/SKILL.md) | 在任何实现前先澄清意图、需求与设计。 | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [context7-cli](context7-cli/SKILL.md) | 使用 Context7 CLI 完成文档查询、skill 管理和 MCP 配置。 | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | 创建、读取、编辑和处理 Word 文档，覆盖格式、批注、修订和图片替换。 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | 系统化测试 Web 应用，并产出附截图和录屏的问题报告。 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | 通过 agent-browser 和 Chrome DevTools Protocol 自动化 Electron 桌面应用。 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | 使用 Exa 做网页、代码和公司调研。 | 自制 |
| [find-skills](find-skills/SKILL.md) | 当用户需要特定能力时，发现已有技能。 | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | 在写第三方 API / SDK 代码前先抓当前文档。 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | 用 `gh` 处理当前分支 PR 的评审和 issue 评论。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | 检查 GitHub Actions 失败项、提取日志并制定修复方案。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [pdf](pdf/SKILL.md) | 处理 PDF 的读取、生成与审查，强调渲染后的视觉检查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | 通过 Pinchtab 的 HTTP API 控制 headless 或 headed Chrome，用于网页自动化、抓取、表单填写、导航、截图和基于稳定 accessibility refs 的内容提取。 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skill/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | 用 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.agent/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | 创建、读取、编辑和处理 PowerPoint 演示文稿，覆盖模板、布局、备注和幻灯片内容。 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | 面向生产环境的高级提示工程模式。 | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | 用于 React + Remotion 视频开发的最佳实践。 | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | 创建或更新技能，补齐专业知识、工作流与工具集成。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [test-driven-development](test-driven-development/SKILL.md) | 实现任何功能或修复前先使用。 | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | 来自 Vercel Engineering 的 React / Next.js 性能优化实践。 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | 覆盖表格创建、编辑、公式、格式和分析。 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | 仅在用户明确要求用 `gh` 一次性完成 stage、commit、push 并创建 GitHub PR 时使用。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### Vendored `impeccable/` 技能

| 技能 | 说明 | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | 创建有辨识度、生产级的高质量前端界面。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | 让设计适配不同屏幕尺寸、设备和上下文。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | 用有目的的动画和微交互增强界面。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | 审计界面的可访问性、性能、主题与响应式表现。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | 让过于保守或平淡的设计更有张力。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | 改善不清晰的 UX 文案与说明。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | 为过于单色的界面加入策略性色彩。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | 从 UX 视角评估设计效果。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | 为界面加入个性和让人记住的细节。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | 把设计提炼到本质，去掉多余复杂度。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | 抽取并整合可复用组件、tokens 和模式。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | 提升错误处理、i18n、溢出和边界情况的韧性。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | 让功能对齐到设计系统并保持一致性。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | 改进引导流程、空状态和首次使用体验。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | 优化加载、渲染、动画、图片和包体积。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | 上线前打磨对齐、间距、一致性和细节。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | 降低过强的视觉攻击性，同时保持质量。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | 收集设计上下文并保存为后续工作的长期指导。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## 贡献

欢迎为现有技能改进或新增技能。

1. 触发条件要明确且可验证。
2. 示例尽量简洁，强调可执行性。
3. 若依赖外部工具，请在 `SKILL.md` 中明确标注依赖。
4. 新增或重命名技能时，请同步更新 `README.md` 与 `README.zh-CN.md`；如果公开技能索引发生变化，也请一并刷新其他翻译版 README。

## 许可证

本仓库主许可证见 [LICENSE](LICENSE)。

部分技能目录包含额外许可证或归属说明文件，包括 [`docx/`](docx/)、[`pptx/`](pptx/)、[`impeccable/`](impeccable/README.md)、[`skill-creator/`](skill-creator/) 和 [`xlsx/`](xlsx/)。
