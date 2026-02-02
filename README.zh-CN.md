# OK Skills

简体中文 | [English](README.md)

面向 pi coding agent / Codex / Claude Code 等 agents 的技能集合。

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
| [test-driven-development](test-driven-development/SKILL.md)         | TDD 流程指引：任何功能或修复先写测试。                              |
| [xlsx](xlsx/SKILL.md)                                               | 覆盖表格创建、编辑与分析，支持公式、格式和可视化图表。              |

## 结构

```
skill-name/
  SKILL.md
  scripts/       # 可选
  references/    # 可选
  assets/        # 可选
```

## 使用方式

1. 选择一个技能目录。
2. 阅读 `SKILL.md` 了解触发条件与流程。
3. 通过你的 agent/skill 管理器加载该技能。
