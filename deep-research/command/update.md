---
description: 从 GitHub 拉取 deep-research skill 最新代码
---

<command-instruction>
你是一个自动更新工具。你的任务是从 GitHub 拉取 deep-research skill 的最新代码，不需要版本检查，不需要用户确认。

## 执行流程

### Step 1 — 定位 skill 目录

通过以下方式查找 skill 目录（不同工具的 skill 安装位置不同，现场探测即可）：
- 检查当前工作目录是否就是 skill 根目录（存在 VERSION 文件）
- 或在常见位置查找 deep-research 的 VERSION 文件（如 `~/.opencode/skills`、`~/.claude/skills`、`.cursor/skills` 等）

如果找不到 → 提示"找不到 deep-research skill 目录"，给出手动克隆命令后退出。

### Step 2 — 检查 git 仓库

确认目录是 git 仓库（存在 `.git` 目录）。如果不是 → 用 `git clone` 克隆到临时目录再复制过来。

### Step 3 — 直接拉取最新代码

**不需要读取 VERSION，不需要比较版本，不需要用户确认。** 直接执行：

```
git pull origin main
```

如果 pull 失败（网络、冲突等）→ 提示"更新失败: {具体原因}"后退出。

### Step 4 — 完成

提示已更新到最新版本。

### 输出示例

```
[✓] 已从 main 分支拉取最新代码
```
</command-instruction>

<user-request>
$ARGUMENTS
</user-request>

---
```
deep-research by hoolulu · github.com/hoolulu/deep-research
```
