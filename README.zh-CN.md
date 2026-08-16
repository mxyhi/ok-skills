# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw、Autohand Code 等工具的 AI Agent Skills 集合

[English](README.md) | 简体中文 | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

> 维护者专用的全局安装分支。外部贡献请面向 `main`，详见 [MAINTAINER_GLOBAL.md](MAINTAINER_GLOBAL.md)。

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

这是一个面向 Codex、Claude Code、Cursor、OpenClaw、Autohand Code、Trae 以及其他兼容 `SKILL.md` / `CLAUDE.md` / `AGENTS.md` 工作流工具的技能仓库。

当前仓库共收录 **18 个可复用技能**，全部作为顶层技能目录由本仓直接维护。把它 clone 到 `~/.agents/skills/ok-skills` 即可，仓库内部目录已经符合 `AGENTS.md` 所需的 skills 规范，[`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) 则提供面向 Claude Code 的 agent playbook。

如果你在找 **Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、可复用的 **CLAUDE.md / AGENTS.md** 模板，或者一套能直接落地的 **SKILL.md** 示例仓库，这个项目就是为搜索可发现性和开箱即用而整理的。


## 适合谁

- 你在用 Codex、Claude Code、Cursor、OpenClaw、Autohand Code、Trae 或其他 AI coding agent，希望复用技能而不是每次临时写 prompt。
- 你在维护 `CLAUDE.md` / `AGENTS.md` / `SKILL.md` 体系，希望不同项目之间可以迁移同一套工作流。

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

如果使用 Autohand Code，可以把仓库 clone 到用户级或项目级 skills 目录：

```bash
# 用户级 skills
mkdir -p ~/.autohand/skills
git clone https://github.com/mxyhi/ok-skills.git ~/.autohand/skills/ok-skills

# 项目级 skills
mkdir -p .autohand/skills
git clone https://github.com/mxyhi/ok-skills.git .autohand/skills/ok-skills
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

- [ax](ax/SKILL.md)：AI 时代的 curl：抓取、发现页面结构、提取结构化数据，替代临时解析脚本。
- [find-docs](find-docs/SKILL.md)：专注于最新文档查询的 Context7 CLI 工作流。
- [exa-search](exa-search/SKILL.md)：用 Exa 做网页、代码、公司调研。
- [get-api-docs](get-api-docs/SKILL.md)：写第三方 API / SDK 代码前先拉当前文档。
- [find-skills](find-skills/SKILL.md)：当用户提出能力诉求时，先查有没有现成 skill 可用。

### 规划与提示工程

- [planning-with-files](planning-with-files/SKILL.md)：通过 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。
- [autoresearch](autoresearch/SKILL.md)：以明确目标、度量、验证循环和保留/丢弃门禁驱动自主迭代。
- [diagnosing-bugs](diagnosing-bugs/SKILL.md)：面向疑难 bug 与性能回归的严格诊断循环。
- [grilling](grilling/SKILL.md)：用于直接 grill 会话 的一次一个问题访谈循环。
- [teach](teach/SKILL.md): 通过 mission、resources、lessons 和 learning records 维护持续教学 workspace。
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md)：减少过度复杂、隐藏假设和不可验证改动的编码行为准则。
- [tdd](tdd/SKILL.md)：功能、修复、重构或行为变更前执行 test-first red-green-refactor。

### 自动化与 QA

- [agent-browser](agent-browser/SKILL.md)：浏览器导航、表单、截图、抓取和网页测试。
- [kimi-webbridge](kimi-webbridge/SKILL.md)：通过本地守护进程控制用户真实浏览器，用于导航、表单填写、截图、页面读取和登录态会话。

### 前端与设计

- [better-icons](better-icons/SKILL.md)：通过 CLI 或 MCP 搜索、浏览并获取 200+ Iconify 图标库中的 SVG 图标。
- [diagram-design](diagram-design/SKILL.md)：27 种编辑级 HTML/SVG 图，支持品牌 token 和 draw.io/Mermaid 重绘。

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) 对应的上游基线是 [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)。本仓将该上游目录作为本地技能的规范基线；本地差异仅限兼容 `skills-ref` 的 `SKILL.md` frontmatter，以及不依赖安装位置的相对脚本路径说明。

## 常见前置条件

- `ax` 技能依赖 `ax` CLI（`curl -fsSL https://ax.yusuke.run/install | sh`）。
- `diagram-design` 技能的导入抽取和自检脚本依赖 Python 3。
- 浏览器类技能通常需要可用的 Chrome/CDP 环境。
- 文档查询类技能可能依赖额外 CLI 或 MCP 工具，请以各自的 `SKILL.md` 为准。

## 完整技能索引

`Source URL` 列优先指向技能的 canonical upstream；如果没有单独上游，则指向当前仓库内该技能目录的 GitHub 地址。

### 顶层技能

| 技能                                                                | 说明                                                                                                                                           | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [ax](ax/SKILL.md)                                                   | AI 时代的 curl：抓取 URL、发现页面结构、提取结构化数据，替代临时解析脚本。                                                                                                        | [yusukebe/ax](https://github.com/yusukebe/ax/tree/main/skills/ax)                                                              |
| [agent-browser](agent-browser/SKILL.md)                             | 面向 AI agents 的浏览器自动化：导航、表单、截图、数据提取、网页测试。                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [autoresearch](autoresearch/SKILL.md)                               | 自主目标导向迭代引擎，覆盖修改、验证、保留/丢弃与重复推进工作流。                                                                          | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | 通过 CLI 或 MCP 工具搜索 200+ Iconify 图标库并获取 SVG 图标。                                                                                  | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | 通过本地守护进程控制用户真实浏览器，用于导航、表单填写、截图、页面读取和登录态会话。                                                          | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [caveman](caveman/SKILL.md)                                         | 用“洞穴人”式极简表达压缩回复 tokens，同时保留完整技术准确性，并支持多档强度。                                                                  | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | 面向疑难 bug 与性能回归的严格诊断循环。                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [diagram-design](diagram-design/SKILL.md)                             | 27 种编辑级 HTML/SVG/PNG 图；可接入品牌 token；可重绘 draw.io 或 Mermaid 源。                                                                                                | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design/tree/main/skills/diagram-design) |
| [find-docs](find-docs/SKILL.md)                                     | 使用 Context7 CLI 查询最新文档、API 参考和代码示例。                                                                                           | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | 使用 Exa 做网页、代码和公司调研。                                                                                                              | 自制                                                                                                                           |
| [find-skills](find-skills/SKILL.md)                                 | 当用户需要特定能力时，发现已有技能。                                                                                                           | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [get-api-docs](get-api-docs/SKILL.md)                               | 在写第三方 API / SDK 代码前先抓当前文档。                                                                                                      | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [grilling](grilling/SKILL.md)                               | 用于直接 grill 会话 的一次一个问题访谈循环。                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | 通过 mission、resources、lessons 和 learning records 在 workspace 中持续教学。 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | 减少过度复杂、隐藏假设和不可验证改动的编码行为准则。                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [planning-with-files](planning-with-files/SKILL.md)                 | 用 `task_plan.md`、`findings.md`、`progress.md` 管理复杂任务。                                                                                 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [tdd](tdd/SKILL.md)                                                 | 功能、修复、重构或行为变更前使用；优先通过 public interface 做 integration-style 测试。                                                        | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## 贡献

欢迎为现有技能改进或新增技能。

1. 触发条件要明确且可验证。
2. 示例尽量简洁，强调可执行性。
3. 若依赖外部工具，请在 `SKILL.md` 中明确标注依赖。
4. 新增或重命名技能时，请同步更新 `README.md` 与 `README.zh-CN.md`；如果公开技能索引发生变化，也请一并刷新其他翻译版 README。

## 许可证

本仓库主许可证见 [LICENSE](LICENSE)。
