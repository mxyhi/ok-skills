# Global Essentials 分支维护说明

`global-essentials` 分支仅供本仓库作者 mxyhi 进行全局安装与维护。

- 本分支不接受外部直接修改，也不接受以本分支为目标分支的 Pull Request。
- 公共贡献请统一面向 `main` 分支提交。
- 全局安装与后续更新应持续跟踪 `global-essentials` 分支。
- 本分支可根据作者的全局使用需求主动偏离 `main`，不保证与 `main` 保持相同的 skill 集合。

安装：

```bash
git clone --branch global-essentials --single-branch https://github.com/mxyhi/ok-skills.git ~/.agents/skills/ok-skills
```

更新：

```bash
git -C ~/.agents/skills/ok-skills pull --ff-only origin global-essentials
```
