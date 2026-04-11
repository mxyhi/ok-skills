# Task Plan: 根层 skills 上游同步

## Goal
基于 `README.zh-CN.md` 中列出的 source repo，逐个比对根层技能目录（不含 `impeccable/` 与 `gsap-skills/`）与各自上游主线，合并有价值更新，保持本仓中文化与既有目录结构，并完成自测与未同步项说明。

## Current Phase
Phase 21

## Phases

### Phase 1: 范围确认与清单整理
- [x] 理解用户目标、约束与输出要求
- [x] 识别受影响的根层技能目录
- [x] 提炼 source repo 与不适用项
- **Status:** complete

### Phase 2: 规划与分组
- [x] 建立分来源仓库的并行比对策略
- [x] 创建 `task_plan.md`、`findings.md`、`progress.md`
- [ ] 为各批次准备可执行的比对上下文
- **Status:** in_progress

### Phase 3: 上游比对与差异筛选
- [ ] 拉取各 source repo 当前主线对应目录
- [ ] 逐技能比对 `SKILL.md`、脚本、模板、说明与引用文件
- [ ] 记录值得同步的内容与应跳过的差异
- **Status:** pending

### Phase 4: 合并与本地化
- [ ] 合并筛选后的上游更新
- [ ] 保持中文化、结构约定与本仓定制说明
- [ ] 必要时同步依赖说明、示例与引用文件
- **Status:** pending

### Phase 5: 验证与交付
- [ ] 运行自测/一致性检查
- [ ] 汇总变更、验证结果与未同步项
- [ ] 检查工作区状态并准备交付
- **Status:** pending

## Key Questions
1. 哪些顶层技能存在可追踪的外部上游，哪些应视为自制/本仓维护而跳过？
2. 上游更新中哪些属于“有价值更新”，哪些会破坏本仓中文化、结构或定制约束而不应直接引入？
3. 哪些附属文件需要与 `SKILL.md` 一并同步，才能保持技能可执行性？

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| 使用 `planning-with-files` 记录全过程 | 任务跨越多来源仓库、工具调用多，需把研究与决策持久化 |
| 使用分来源仓库的并行调查策略 | 多个技能目录彼此独立，适合并行拉取与比对，减少总耗时 |
| 排除 `impeccable/` 与 `gsap-skills/` | 用户明确要求仅处理根层技能目录 |
| `caveman-compress` 仅 vendoring 运行必需文件 | 上游 `README.md` 和 `SECURITY.md` 仅用于人类说明，不参与 skill 执行，保留会增加仓库噪音 |
| 将 upstream 的 `compress` frontmatter 名称改为 `caveman-compress` | 对齐目录名、README 索引和本仓 discoverability，同时在正文里保留 `/caveman:compress` 触发方式 |
| `opensrc` 保持 upstream `SKILL.md` 原文，仅补最小元数据与许可证 | upstream 内容已足够清晰，避免不必要本地改写，同时对齐本仓收录规范 |

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
|       | 1       |            |

## Notes
- 只同步“有价值更新”，不机械覆盖本仓中文化与定制内容
- 允许破坏旧格式，不做向后兼容
- 每完成一批来源仓库比对后更新 `findings.md` 与 `progress.md`
- 2026-04-10 follow-up：新增 `caveman` / `caveman-compress`，上游基线为 `JuliusBrussee/caveman@92f892f2b99744a4501f35bce9a2e384878e4877`
- 2026-04-10 follow-up 2：按用户要求删除 `caveman-compress`，仅保留 `caveman`

## Follow-up Goal (2026-04-10)

将 `JuliusBrussee/caveman` 仓库中的 `caveman` 与 `caveman-compress` 接入为新的根层 skills，补齐必需脚本、license、agents 元数据，并同步更新多语言 README 的顶层索引与计数。

### Phase 6: 上游调研与接入范围确认
- [x] 读取 `caveman` 与 `caveman-compress` 当前主线内容
- [x] 区分运行必需文件与可省略的人类说明文件
- [x] 确认 README 计数、索引和命名策略
- **Status:** complete

### Phase 7: 落地 skill 目录与索引
- [x] 新增 `caveman/` 的 `SKILL.md`、`agents/openai.yaml`、`LICENSE.txt`
- [x] 新增 `caveman-compress/` 的 `SKILL.md`、`scripts/`、`agents/openai.yaml`、`LICENSE.txt`
- [x] 更新 10 份顶层 README 的技能总数与顶层技能索引
- **Status:** complete

### Phase 8: 验证与交付
- [x] 运行 Python 语法检查与模块入口检查
- [x] 校验 README 计数与索引命中
- [x] 更新 `task_plan.md`、`findings.md`、`progress.md`
- **Status:** complete

### Phase 9: 回退 caveman-compress
- [x] 删除 `caveman-compress/` 目录
- [x] 将 README 计数与索引回退为仅新增 `caveman`
- [x] 更新 planning 记录并复查工作区
- **Status:** complete

## Follow-up Goal (2026-04-11)

将 `vercel-labs/opensrc` 仓库中的 `skills/opensrc` 接入为新的根层 skill，补齐必要元数据与许可证文件，并同步更新多语言 README 的技能总数与顶层索引。

### Phase 10: 上游调研与接入边界
- [x] 读取 upstream `skills/opensrc` 目录与 `SKILL.md`
- [x] 确认是否存在脚本、模板与额外资源
- [x] 确认许可证类型与本仓落地范围
- **Status:** complete

### Phase 11: 落地 skill 与索引
- [x] 新增 `opensrc/` 的 `SKILL.md`
- [x] 补齐 `agents/openai.yaml` 与 `LICENSE.txt`
- [x] 更新多语言 README 的计数与顶层索引
- **Status:** complete

### Phase 12: 校验与交付
- [x] 校验文件结构、README 命中与工作区状态
- [x] 更新 `findings.md`、`progress.md`
- [x] 汇总结果并交付
- **Status:** complete

## Follow-up Goal (2026-04-11, upstream sync refresh)

基于 `README.md` / `README.zh-CN.md` 当前的 `Source URL`，重新拉取对应 upstream 最新主线，筛选并同步本仓中有直接对应关系且存在实质更新的 skills，同时保留本仓聚合/本地增强部分。

### Phase 13: 重新建立 upstream 基线
- [x] 拉取所有唯一 upstream 仓库当前主线
- [x] 重新解析顶层与 vendored skills 的 `Source URL`
- [x] 识别直接映射、聚合映射与不适合机械同步的目录
- **Status:** complete

### Phase 14: 差异筛选与范围决策
- [x] 比对直接映射 skills 与 upstream 最新内容
- [x] 标记高价值可同步项与应跳过项
- [x] 将筛选结论写入 `findings.md`
- **Status:** complete

### Phase 15: 同步明确可落地的 skills
- [x] 同步 `agent-browser`、`better-icons`、`browser-use`
- [x] 同步 `pinchtab`、`planning-with-files`、`yeet`
- [x] 同步 `remotion-best-practices`、`vercel-react-best-practices`
- **Status:** complete

### Phase 16: 处理新增引用文件与目录
- [x] 补充新增 `references/` 或 `rules/` 文件
- [x] 复查本地增强文件（如 `LICENSE.txt`、`agents/openai.yaml`）未被误删
- [x] 记录本轮跳过项与原因
- **Status:** complete

### Phase 17: 校验与交付
- [x] 运行目录/差异检查
- [x] 更新 `task_plan.md`、`findings.md`、`progress.md`
- [x] 汇总同步结果、验证结果与跳过项
- **Status:** complete

## Follow-up Goal (2026-04-11, opencli 对齐)

将本仓 `opencli/` 调整为 upstream `jackwener/opencli/skills/` 的镜像目录，保持目录层级、文件命名与文件内容一致；README 中的 `opencli` 入口指向 `opencli/opencli-usage/SKILL.md`。

### Phase 18: opencli 映射与结构设计
- [x] 读取本地 `opencli/` 与 upstream `skills/` 完整结构
- [x] 确定采用“镜像 upstream skills 子树”的落地方案
- [x] 确认 README 计数与顶层 skill 索引无需变更
- **Status:** complete

### Phase 19: 同步 opencli usage 主入口
- [x] 用 upstream `skills/opencli-usage/` 原样同步 `opencli/opencli-usage/`
- [x] 保留 `SKILL.md`、`commands.md`、`desktop.md`、`plugins.md` 原始层级
- [x] 避免对内容做本地改写
- **Status:** complete

### Phase 20: 收拢相关 opencli 子文档
- [x] 将 upstream `opencli-browser`、`opencli-explorer`、`opencli-oneshot`、`opencli-autofix`、`smart-search` 全部纳入 `opencli/`
- [x] 保持子目录名与 upstream 一致
- [x] 保持本仓“独立 opencli 目录”与 upstream `skills/` 同构
- **Status:** complete

### Phase 21: 校验与交付
- [x] 校验 `opencli/` 与 upstream `skills/` 目录级无 diff
- [x] 更新 `task_plan.md`、`findings.md`、`progress.md`
- [x] 汇总本轮 opencli 改造结果
- **Status:** complete

## Follow-up Goal (2026-04-11, impeccable 同步)

将本仓 `impeccable/` 从旧版派生 bundle 切换到 upstream `pbakaus/impeccable/.agents/skills/` 当前结构，保留根目录 `LICENSE` / `NOTICE.md` / `README.md`，并同步更新多语言 README 中的 vendored skill 索引与提交号。

### Phase 22: upstream 结构确认与映射决策
- [x] 比对本地 `impeccable/` 与 upstream `source/skills`、`.agents/skills` 的差异
- [x] 确认应以 `.agents/skills` 为 vendoring 基线，避免同步模板变量
- [x] 确认旧的 `frontend-design`、`extract`、`normalize`、`onboard`、`teach-impeccable` 已被 upstream 新结构替代
- **Status:** complete

### Phase 23: bundle 同步与索引更新
- [x] 用 upstream `.agents/skills` 覆盖共享 skill，并新增 `impeccable`、`layout`、`overdrive`、`shape`、`typeset`
- [x] 删除已被 upstream 合并或重命名的旧目录
- [x] 更新 `impeccable/README.md`、`NOTICE.md` 与 10 份顶层 `README*` 的索引、说明和 commit
- **Status:** complete

### Phase 24: 校验与交付
- [x] 校验本地 `impeccable/` 结构与 upstream `.agents/skills` 差异仅剩预期本地文件
- [x] 校验多语言 `README*` 不再引用旧 impeccable skill 名称或旧 commit
- [x] 更新 `task_plan.md`、`findings.md`、`progress.md`
- **Status:** complete
