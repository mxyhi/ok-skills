# OK Skills

简体中文 | [English](README.md)

面向 pi coding agent / Codex / Claude Code 等 agents 的技能集合。

## 仓库包含内容

- 按目录组织的可复用技能（`<skill-name>/SKILL.md`）。
- 技能所需的可选参考资料、脚本、许可证文件。
- 中英文双语概览文档（`README.md` + `README.zh-CN.md`）。

## 快速开始

1. 克隆本仓库。
2. 将需要的技能目录复制到本地技能目录（例如：`~/.codex/skills` 或 `~/.agents/skills`）。
3. 在项目说明文件（如 `AGENTS.md`）中定义技能触发条件。
4. 通过技能名显式调用，或自然描述需求让 agent 自动匹配技能。

本仓库无需构建即可使用。

## 技能列表

| 技能                                                                | 说明                                                                |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [agent-browser](agent-browser/SKILL.md)                             | 自动化浏览器操作，用于网页测试、表单填写、截图与数据提取。          |
| [brainstorming](brainstorming/SKILL.md)                             | 在任何创造性工作前使用，用于澄清意图、需求与设计。                  |
| [context7](context7/SKILL.md)                                       | 通过 Context7 获取最新库/框架文档，用于 API、示例与正确用法。       |
| [exa-search](exa-search/SKILL.md)                                   | 使用 Exa 进行网页/代码/公司调研，含参数与示例；需要联网搜索时使用。 |
| [find-skills](find-skills/SKILL.md)                                 | 当用户需要特定能力时，用于发现和安装现成技能。                      |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | 使用 gh CLI 处理当前分支 PR 的评审/issue 评论，并先验证登录状态。   |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | 检查 GitHub Actions 失败项，提取日志并制定修复方案。                |
| [planning-with-files](planning-with-files/SKILL.md)                 | 面向复杂任务的文件化规划（task_plan/findings/progress）。           |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | 高级提示工程方法，提升生产环境的可靠性与可控性。                    |
| [skill-creator](skill-creator/SKILL.md)                             | 创建或更新技能，聚焦专业知识、工作流与工具集成。                    |
| [taste-skill](taste-skill/SKILL.md)                                 | 面向高质量前端界面设计的 UI/UX 工程技能，强调有意图的视觉与实现。   |
| [test-driven-development](test-driven-development/SKILL.md)         | TDD 流程指引：任何功能或修复先写测试。                              |
| [xlsx](xlsx/SKILL.md)                                               | 覆盖表格创建、编辑与分析，支持公式、格式和可视化图表。              |

## 目录结构

```text
ok-skills/
  README.md
  README.zh-CN.md
  <skill-name>/
    SKILL.md
    references / scripts / examples（可选）
```

## 贡献指南

欢迎为现有技能改进或新增技能。

1. 触发条件要明确且可验证。
2. 示例尽量简洁，强调可执行性。
3. 若依赖外部工具，请在 `SKILL.md` 中明确标注依赖。

## 许可证

本仓库主许可证见 [LICENSE](LICENSE)。
部分技能目录可能包含额外许可证文件（例如 `xlsx/`、`skill-creator/`）。
