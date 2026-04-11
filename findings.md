# Findings & Decisions

## Requirements
- 依据 `README.zh-CN.md` 的顶层技能 `Source URL` 清单逐项比对。
- 处理范围仅限根层技能目录，不含 `impeccable/` 与 `gsap-skills/`。
- 比对对象包括 `SKILL.md`、附属脚本、模板、说明文件，以及必要的引用依赖说明与示例。
- 允许破坏旧格式，不做向后兼容，但要保留本仓中文化与现有结构约定。
- 任务完成后需要自测，并总结已同步变更与未同步项。

## Research Findings
- 根层技能目录共 29 个，其中部分条目上游为外部 GitHub 仓库，部分为自制或指向本仓目录。
- `README.zh-CN.md` 已为每个顶层技能给出 `Source URL`，可直接作为逐项比对的 canonical mapping。
- `git status --short` 当前为空，工作区干净，便于识别本轮改动。
- 仓库内只有 `vercel-react-best-practices/AGENTS.md` 额外生效；当前尚未触及该目录下文件，但若后续修改该目录需补读其约束。
- 已按 `Source URL` 拉取各唯一来源仓库的当前主线到 `/tmp/ok-skills-upstreams/`，并以 `diff -ru` 对比本地目录。
- 第一轮结果显示：除 `pinchtab/` 外，其余存在外部上游的根层技能均与上游目录一致。
- `browser-use/` 仅比上游多出 `LICENSE.txt`，`planning-with-files/` 仅比上游多出 `scripts/__pycache__/`；两者都不是上游更新缺失。
- `exa-search` 为自制技能，`frontend-skill` 的 source 指向本仓自身路径，均不适用外部上游同步。
- `pinchtab/` 与上游当前主线存在内容差异，集中在 `references/` 下的文档文件，需要进一步筛选哪些更新应同步。
- GitHub issue `#2`（`https://github.com/mxyhi/ok-skills/issues/2`）是一个收录通知，不涉及功能缺陷；issue 正文建议在 README 添加 `Awesome Codex CLI` badge，仓库 owner 评论为 `ok`，说明该建议已被接受。
- 仓库顶层 10 份多语言 `README*` 在修改前均未包含 `awesome.re` badge；为了避免仅英文首页可见，适合统一在所有顶层 README 标题区同步展示同一 badge。
- `JuliusBrussee/caveman@92f892f2b99744a4501f35bce9a2e384878e4877` 的 `caveman/` 目录只有 `SKILL.md`，而 `caveman-compress/` 的运行核心是 `SKILL.md + scripts/`；同目录下的 `README.md` 与 `SECURITY.md` 属于说明文档，不参与执行。
- `caveman-compress/scripts/` 依赖 `python3`；压缩阶段优先走 `ANTHROPIC_API_KEY` + Anthropic Python SDK，缺省时回退到本地 `claude --print`，因此这些依赖需要在 vendored `SKILL.md` 中显式写明。
- upstream `caveman-compress/SKILL.md` 的 frontmatter `name` 为 `compress`，但在本仓作为独立根层 skill 收录时会与目录名、README 索引和触发发现产生歧义，因此更适合改为 `caveman-compress`，同时保留 `/caveman:compress` 触发描述。
- README 贡献规则明确要求新增 skill 时至少同步 `README.md` 与 `README.zh-CN.md`，若公开技能索引变化则也应刷新其余翻译版 README；因此这次需要把 10 份顶层 README 的技能总数从 55/29 改为 57/31，并新增两条顶层 skill 索引。
- 本地验证结果：`python3 -m compileall caveman-compress/scripts` 通过；`cd caveman-compress && python3 -m scripts` 正常输出 usage；`rg` 校验显示 10 份顶层 README 都已命中新的总数与两条 skill 索引。
- 用户随后要求删除 `caveman-compress`；因此最终保留方案应为仅保留 `caveman`，并把 10 份 README 的技能总数回退为 56/30，同时移除所有 `caveman-compress` 公开入口与许可证说明。
- `vercel-labs/opensrc` 的 upstream 目录 `skills/opensrc` 当前只有一个 `SKILL.md`，没有脚本、模板或引用文件。
- upstream `SKILL.md` 通过 `allowed-tools: Bash(opensrc:*)` 约束工具面，核心命令是 `opensrc path ...`，缓存目录为 `~/.opensrc/`。
- upstream 仓库顶层许可证为 Apache-2.0；本仓接入时适合附带许可证文本到 `opensrc/LICENSE.txt`。
- 本仓已有若干根层 skill 补 `agents/openai.yaml` 做 UI 发现增强；即便 upstream 没有该文件，`opensrc/` 也适合补一个最小 metadata 文件。
- 2026-04-11 重新拉取 live upstream 后，存在直接映射且有实质更新的目录主要有：`agent-browser`、`better-icons`、`browser-use`、`pinchtab`、`planning-with-files`、`remotion-best-practices`、`vercel-react-best-practices`、`yeet`。
- `agent-browser` upstream 新增了 Chrome/Brave/Playwright/Puppeteer 自动探测说明、`batch` 强化用法、tab 管理、dialog 自动处理与 `chat` 命令示例；`references/commands.md` 也补了 `dialog status`。
- `browser-use` upstream 明确了 `connect` / `cloud connect` 模式、tab 子命令、配置管理，并新增 `references/cdp-python.md` 与 `references/multi-session.md`。
- `better-icons` upstream 在 `SKILL.md` 中新增了全局安装与 `npx` / `bunx` 的使用方式，更适合 agent 初次运行时自举。
- `pinchtab` upstream 新增了 agent identity/session token、tab-scoped HTTP API、下拉值发现等操作约定，并扩充了 `TRUST.md` 的安全公告列表。
- `planning-with-files` upstream 从 `2.26.1` 升到 `2.33.0`，`scripts/session-catchup.py` 新增了 Codex session 解析与可选 `orjson` 加速，属于本仓当前运行环境下的高价值修复。
- `remotion-best-practices` upstream 新增了新项目脚手架、Studio 启动、单帧渲染检查、静音检测入口，并补了一份 `rules/silence-detection.md`；若同步应连带更新相关 rule 文档。
- `vercel-react-best-practices` upstream 从 65 条规则增加到 69 条，新增 `advanced-effect-event-deps`、`async-cheap-condition-before-await`、`server-no-shared-module-state` 三条规则，并在 `SKILL.md` 与既有 rule 间加了交叉引用。
- `yeet` upstream 改了默认分支与 PR 命名约定：去掉 `codex/` 分支前缀和 `[codex]` PR title 前缀。
- `caveman` 当前 upstream 差异仅是排版符号（ASCII `->` 改成 Unicode 箭头、破折号样式），不属于高价值功能更新。
- `opencli` 的 `Source URL` 原先指向整个 repo；如果要严格对齐，最合理的方式不是扁平化改写，而是直接让本仓 `opencli/` 镜像 upstream `skills/` 子树。
- `impeccable/` bundle 在 upstream 已迁移到新结构；真正可直接 vendoring 的基线不是 `source/skills/*`，而是已展开模板变量的 `.agents/skills/*`。
- 实际同步后，重新做目录 diff，所有“直接映射且选中同步”的目标目录都已对齐；剩余差异只来自预期跳过项：`caveman`、`opensrc`、`opencli`、`impeccable/`。
- 本轮新增文件为：`browser-use/references/cdp-python.md`、`browser-use/references/multi-session.md`、`remotion-best-practices/rules/silence-detection.md`、`vercel-react-best-practices/rules/advanced-effect-event-deps.md`、`vercel-react-best-practices/rules/async-cheap-condition-before-await.md`、`vercel-react-best-practices/rules/server-no-shared-module-state.md`。
- 用户随后明确要求把 `opencli` 对齐，并收敛为一个独立 `opencli/` 目录，因此上一轮“跳过 opencli”结论失效，需要单独执行结构化同步。
- `opencli` 的最终落地方式是：
  - 顶层仍只有一个 `opencli/` 目录
  - 目录内容直接镜像 upstream `jackwener/opencli/skills/`
  - 不再把多个 skill 扁平化成 `CLI-*.md`
- 这样可以同时满足：
  - 顶层技能索引仍只暴露一个 `opencli`
  - 目录内容与 upstream `skills/` 完全同构
  - 本仓无需修改 README 技能总数与顶层 skill 数量
- 实际落地后，`opencli/` 目录已直接镜像 upstream `skills/`，包含：
  - `opencli-usage/`
  - `opencli-browser/`
  - `opencli-explorer/`
  - `opencli-oneshot/`
  - `opencli-autofix/`
  - `smart-search/`
- 目录级校验通过：`diff -ru /tmp/ok-skills-upstreams-live/jackwener__opencli/skills opencli` 无输出，说明本地 `opencli/` 与 upstream `skills/` 当前完全一致。
- `README*` 中的本地入口已改为 `opencli/opencli-usage/SKILL.md`，`Source URL` 改为 `https://github.com/jackwener/opencli/tree/main/skills`，与镜像结构一致。

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| 先按来源仓库分组，再在组内逐技能比对 | 同一来源仓库可复用一次拉取结果，提高效率 |
| 将“自制”与“本仓自引用”技能标为无外部上游 | 这些技能不存在可同步的独立主线，应作为未同步但非遗漏记录 |
| 需要时采用多 subagent 并行做差异调查 | 目录写入可按技能分片，且用户明确偏好优先多 agent |
| issue #2 采用文档展示修复而非代码层处理 | issue 内容只是收录通知，目标是补 README badge |
| badge 同步到所有顶层多语言 README | 保持入口展示一致，避免不同语言落地页信息不对齐 |
| vendoring `caveman-compress` 时省略 upstream `README.md` 与 `SECURITY.md` | 这两个文件不影响 skill 运行，且本仓已有 README 体系承接公开说明 |
| 为 `caveman` 与 `caveman-compress` 新增 `agents/openai.yaml` | 与本仓已有可发现性较强的 skills 保持一致，便于 UI 展示与默认提示语生成 |
| `opensrc` 保持 upstream `SKILL.md` 原文，仅补最小元数据与许可证 | upstream 内容已足够清晰，避免不必要本地改写，同时对齐本仓收录规范 |
| 本轮只同步“直接映射且高价值”的 upstream 更新 | 避免把聚合版、本仓增强版或非 1:1 vendored skill 机械覆盖掉 |
| `opencli` 与 `impeccable/` 本轮先记为跳过项 | 两者都已在后续 follow-up 中完成结构化同步 |

## Follow-up Findings: impeccable

- upstream `pbakaus/impeccable` 当前提交为 `00d485659af82982aef0328d0419c49a2716d123`。
- `source/skills/*` 中仍包含 `{{command_prefix}}`、`{{scripts_path}}` 等模板变量，不适合直接 vendoring；`.agents/skills/*` 已经展开为可直接使用的 agent 版本。
- 本地旧 bundle 与 upstream 新 bundle 的核心结构差异是：
  - 旧：`frontend-design`、`extract`、`normalize`、`onboard`、`teach-impeccable`
  - 新：`impeccable`、`layout`、`overdrive`、`shape`、`typeset`
- 共享 skill 也存在内容更新，不能只做目录重命名；例如 `adapt` 等 skill 已从依赖 `/frontend-design` / `/teach-impeccable` 改为依赖 `/impeccable` / `/impeccable teach`。
- 实际同步后，本地 `impeccable/` 已包含：
  - `impeccable/`
  - `adapt/`
  - `animate/`
  - `audit/`
  - `bolder/`
  - `clarify/`
  - `colorize/`
  - `critique/`
  - `delight/`
  - `distill/`
  - `harden/`
  - `layout/`
  - `optimize/`
  - `overdrive/`
  - `polish/`
  - `quieter/`
  - `shape/`
  - `typeset/`
- 本地与 upstream `.agents/skills` 的差异只剩预期项：
  - 根目录额外保留 `LICENSE`、`NOTICE.md`、`README.md`
  - `impeccable/impeccable/SKILL.md` 已按 upstream 自身说明移除一次性的 `<post-update-cleanup>` 段落，因为本轮同步已经手工完成了对应清理
- 10 份顶层 `README*` 已完成同步：
  - `frontend-design` 入口改为 `impeccable`
  - vendored impeccable skill 索引改为新 18 项集合
  - `Source` 说明中的 commit 已更新到 `00d485659af82982aef0328d0419c49a2716d123`
| `caveman` 保持本地版本不动 | 差异仅为排版符号，不值得引入 Unicode 变更 |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| 暂无 | 持续记录 |

## Resources
- `README.zh-CN.md`
- `task_plan.md`
- `subagent-driven-development/SKILL.md`
- `/Users/langhuam/.codex/memories/MEMORY.md`
- `/tmp/ok-skills-upstreams/`
- `/tmp/ok-skills-caveman/`
- `https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc`

## Visual/Browser Findings
- 当前阶段未使用浏览器/图像类工具。
