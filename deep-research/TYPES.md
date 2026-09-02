# 主题类型与章节结构 — deep-research

基于 IDC 文档类型体系、Gartner 研究方法、券商行业深度报告标准、Forrester Tech Tide、IEEE 技术报告规范整理。

---

## 类型一：行业研究

| 项目 | 说明 |
|:----|:-----|
| 对标标准 | 券商行业深度报告 / IDC Market Forecast / 艾瑞咨询行业报告 |
| 适用场景 | 分析一个行业的规模、竞争、趋势 |
| 典型章序 | 定义 → 规模 → 竞争格局 → 产业链 → 政策 → 趋势 → 风险 |
| 受众侧重 | 投资者、决策层 |
| 参考来源 | IDC: Market Forecast, Market Share, Spending Guide ([idc.com/help/doctypes](https://www.idc.com/help/doctypes/)) |

## 类型二：公司/产品研究

| 项目 | 说明 |
|:----|:-----|
| 对标标准 | 券商公司深度报告 / Gartner Vendor Assessment / CB Insights Company Profile |
| 适用场景 | 深入分析一家公司或产品 |
| 典型章序 | 定位 → 产品/技术 → 商业模式 → 竞争 → 风险 → 展望 |
| 受众侧重 | 投资者、技术决策者 |
| 参考来源 | Gartner: Magic Quadrant, Critical Capabilities ([gartner.com](https://www.gartner.com/en/research/magic-quadrant)) |

## 类型三：技术专题研究

| 项目 | 说明 |
|:----|:-----|
| 对标标准 | IEEE 技术报告 / Gartner Hype Cycle / 技术白皮书 |
| 适用场景 | 调研一项技术的原理、现状与前景 |
| 典型章序 | 背景 → 架构原理 → 发展现状 → 技术评估 → 应用 → 趋势 |
| 受众侧重 | 技术决策者、学习者 |
| 参考来源 | Gartner: Hype Cycle, Tech Trend ([gartner.com](https://www.gartner.com/en/research/methodologies/magic-quadrants-research)) |

## 类型四：趋势/市场前瞻

| 项目 | 说明 |
|:----|:-----|
| 对标标准 | Forrester Tech Tide / Gartner FutureScape / 36Kr 行业趋势 |
| 适用场景 | 分析新兴趋势的驱动力与影响 |
| 典型章序 | 现状 → 驱动因素 → 演进脉络 → 影响评估 → 行动建议 |
| 受众侧重 | 决策层、投资者 |
| 参考来源 | IDC: FutureScape, PlanScape ([idc.com/help/doctypes](https://www.idc.com/help/doctypes/)) |

## 类型五：指南/教程

| 项目 | 说明 |
|:----|:-----|
| 对标标准 | IEEE 技术白皮书"方法"模版 / 实操文档标准 / GB/T 指南标准 |
| 适用场景 | 提供可执行的选型或实施指南 |
| 典型章序 | 前置准备 → 核心概念 → 分步指南 → 常见错误 → 进阶路径 |
| 受众侧重 | 学习者、技术实践者 |
| 参考来源 | GB/T 1.1-2020 指南标准 ([openstd.samr.gov.cn](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C4BFD981E993C417EF475F2A19B681F1)) |

---

## 受众分类（参考Gartner/IDC体系）

| 受众层 | 角色 | 侧重点 |
|:-------|:-----|:--------|
| **决策层** | CEO/CIO/CTO | 战略方向、ROI、风险、竞争格局 |
| **投资层** | 基金经理、分析师 | 市场规模、估值、盈利预测 |
| **技术层** | 技术负责人、架构师 | 架构、技术栈、部署、安全 |
| **业务层** | 业务总监、产品经理 | 应用场景、实践案例、ROI |
| **学习者** | 从业者、学生、媒体 | 概念理解、趋势、全景认知 |

> 来源：Gartner 受众模型 ([portersfiveforce.com](https://portersfiveforce.com/blogs/target-market/gartner)), 证券业协会研究报告受众分类 ([sac.net.cn](https://www.sac.net.cn/zlgl/zlgz/202512/t20251231_69839.html))

---

## 报告输出编号体系

报告正文使用三级编号体系，章与子节采用不同编号格式以避免层级冲突：

| 层级 | Markdown | 编号格式 | 示例 | 备注 |
|------|----------|----------|------|------|
| **章（一级）** | `##` | 汉字数字 + 顿号：一、二、三… | `## 一、市场规模` | 装配阶段自动分配，每章独占一个汉字编号 |
| **子节（二级）** | `###` | 阿拉伯数字 x.x：1.1, 1.2… | `### 1.1 全球出货量` | 各章从头编号（每章均从 .1 开始） |
| **子子节（三级）** | `####` | 括号阿拉伯数字：(1), (2)… | `#### (1) 按地区拆分` | 子节内部可选细化 |

### 核心约束

1. **同层统一**：同一层级全报告使用相同的编号格式，不得混用
2. **不可跳级**：一级 → 二级 → 三级递进，不得出现一级后直接三级
3. **体系分离**：子节编号体系与章编号体系必须不同（章用汉字数字 → 子节用阿拉伯数字）
4. **每章重置**：子节编号在每章内从 1.1 重新开始，不跨章连续

来源：CY/T 35-2001《科技文献的章节编号方法》([xxmu.edu.cn](https://www.xxmu.edu.cn/qks/CY_T35-2001.pdf)), GB/T 1.1-2020《标准化工作导则》([openstd.samr.gov.cn](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C4BFD981E993C417EF475F2A19B681F1)), 公文层次序号规范 ([book118.com](https://m.book118.com/html/2024/1014/7012141001006162.shtm))

---
```
deep-research by hoolulu · github.com/hoolulu/deep-research
```
