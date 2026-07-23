# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw 等工具的 AI Coding Agent Skills 與 AGENTS.md 工作流技能集

[English](README.md) | [简体中文](README.zh-CN.md) | 繁體中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

這是一個面向 Codex、Claude Code、Cursor、OpenClaw、Trae 以及其他相容 `SKILL.md` / `CLAUDE.md` / `AGENTS.md` 工作流工具的 AI coding agent skills 倉庫。

目前倉庫共收錄 **15 個可重用技能**，全部作為頂層技能目錄由本倉直接維護。將它 clone 到 `~/.agents/skills/ok-skills` 即可，倉庫內部目錄已符合 `AGENTS.md` 所需的 skills 佈局，[`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) 則提供面向 Claude Code 的 agent playbook。

如果你正在找 **Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、可重用的 **CLAUDE.md / AGENTS.md** 範本，或一套能直接落地的 **SKILL.md** 範例倉庫，這個專案就是為了搜尋可發現性與開箱即用而整理的。


## 適合誰

- 你正在使用 Codex、Claude Code、Cursor、OpenClaw、Trae 或其他 AI coding agent，希望重用技能，而不是每次臨時撰寫 prompt。
- 你正在維護 `CLAUDE.md` / `AGENTS.md` / `SKILL.md` 體系，希望同一套工作流能在不同專案之間攜帶與復用。

## 建議先安裝這幾個

如果你第一次使用這個倉庫，優先從下面幾個技能開始：

- [planning-with-files](planning-with-files/SKILL.md)：適合複雜任務、調研任務與多輪推進任務的檔案式規劃。
- [find-docs](find-docs/SKILL.md)：查詢最新函式庫文件、API 參考與 Context7 範例。
- [agent-browser](agent-browser/SKILL.md)：瀏覽器自動化、截圖、抓取、表單填寫與 Web QA。

## 1 分鐘快速開始

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 後，倉庫會位於 `~/.agents/skills/ok-skills`，其內部目錄已符合預期佈局：

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

Claude Code 或 Codex 的全域指令可以從 [`CLAUDE_AGENTS.md`](CLAUDE_AGENTS.md) 開始，然後複製或合併到 Claude Code 的 `CLAUDE.md` 或 Codex 的 `AGENTS.md`。它內建中文優先、KISS、最新文件/原始碼檢查、多 agent 優先、預設啟用 `caveman` / `planning-with-files` / `karpathy-guidelines`、嚴格 TypeScript 約束和 context-mode 路由規則。復用前請按專案編輯 `语言要求` 小節；`其他注意项` 是專案本地設定，可按需編輯。

接著在 `AGENTS.md` 裡加入最小觸發規則，或把同樣的 skill 觸發規則合併進 `CLAUDE.md` / `AGENTS.md`：

```md
## Skills

- planning-with-files: 用於複雜任務、調研任務，或預計會有 5 次以上工具呼叫的工作。
- find-docs: 需要最新函式庫文件、API 參考或 Context7 範例時使用。
- agent-browser: 需要瀏覽器自動化、截圖、抓取、網頁測試或表單填寫時使用。
```

之後就可以自然觸發：

- `在重構這個模組之前先用 planning-with-files。`
- `用 find-docs 查一下這個 SDK 的最新文件。`
- `用 agent-browser 重現這個 UI 問題。`

## 按場景瀏覽技能

### 調研與文件

- [find-docs](find-docs/SKILL.md)：專注於最新文件查詢的 Context7 CLI 工作流。
- [exa-search](exa-search/SKILL.md)：使用 Exa 進行網頁、程式碼與公司調研。
- [find-skills](find-skills/SKILL.md)：當使用者提出能力需求時，先檢查是否已有現成 skill 可用。

### 規劃與提示工程

- [planning-with-files](planning-with-files/SKILL.md)：透過 `task_plan.md`、`findings.md`、`progress.md` 管理複雜任務。
- [autoresearch](autoresearch/SKILL.md)：以明確目標、度量、驗證迴圈和保留/丟棄門禁驅動自主迭代。
- [diagnosing-bugs](diagnosing-bugs/SKILL.md)：面向疑難 bug 與效能回歸的嚴格診斷迴圈。
- [grilling](grilling/SKILL.md)：用於直接 grill 會話 的一次一題訪談循環。
- [teach](teach/SKILL.md): 透過 mission、resources、lessons 與 learning records 維護持續教學 workspace。
- [domain-modeling](domain-modeling/SKILL.md): build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.
- [karpathy-guidelines](karpathy-guidelines/SKILL.md)：減少過度複雜、隱藏假設與不可驗證改動的編碼行為準則。
- [tdd](tdd/SKILL.md)：功能、修復、重構或行為變更前執行 test-first red-green-refactor。

### 自動化與 QA

- [agent-browser](agent-browser/SKILL.md)：瀏覽器導覽、表單、截圖、抓取與網頁測試。
- [kimi-webbridge](kimi-webbridge/SKILL.md)：透過本機守護行程控制使用者的真實瀏覽器，用於導覽、表單填寫、截圖、頁面讀取和登入狀態工作階段。

### 前端與設計

- [better-icons](better-icons/SKILL.md)：透過 CLI 或 MCP 搜尋、瀏覽並取得 200+ Iconify 圖示庫中的 SVG 圖示。

## Vendored Skill Packs

[`planning-with-files/`](planning-with-files/) 對應的上游基線是 [`OthmanAdi/planning-with-files/.codex/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)。本倉將該上游目錄作為本地技能的規範基線；本地差異僅限相容 `skills-ref` 的 `SKILL.md` frontmatter，以及不依賴安裝位置的相對腳本路徑說明。

## 常見前置條件

- 瀏覽器類技能通常需要可用的 Chrome/CDP 環境。
- 文件查詢類技能可能依賴額外 CLI 或 MCP 工具，請以各自的 `SKILL.md` 為準。

## 完整技能索引

`Source URL` 欄位優先指向技能的 canonical upstream；如果沒有獨立上游，則指向目前倉庫內該技能目錄的 GitHub 位址。

### 頂層技能

| 技能                                                                | 說明                                                                                                                                           | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | 面向 AI agents 的瀏覽器自動化：導覽、表單、截圖、資料擷取與網頁測試。                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [autoresearch](autoresearch/SKILL.md)                               | 自主目標導向迭代引擎，覆蓋修改、驗證、保留/丟棄與重複推進工作流。                                                                          | [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch/tree/master/.agents/skills/autoresearch)                  |
| [better-icons](better-icons/SKILL.md)                               | 透過 CLI 或 MCP 工具搜尋 200+ Iconify 圖示庫並取得 SVG 圖示。                                                                                  | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [kimi-webbridge](kimi-webbridge/SKILL.md)                           | 透過本機守護行程控制使用者的真實瀏覽器，用於導覽、表單填寫、截圖、頁面讀取和登入狀態工作階段。                                                | [install.sh](https://cdn.kimi.com/webbridge/install.sh)                                                             |
| [caveman](caveman/SKILL.md)                                         | 用「穴居人」式極簡表達壓縮回覆 tokens，同時保留完整技術準確性，並支援多段強度。                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/skills/caveman)                                            |
| [diagnosing-bugs](diagnosing-bugs/SKILL.md)                                   | 面向疑難 bug 與效能回歸的嚴格診斷迴圈。                                                                                     | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)                                |
| [find-docs](find-docs/SKILL.md)                                     | 使用 Context7 CLI 查詢最新文件、API 參考與程式碼範例。                                                                                         | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [exa-search](exa-search/SKILL.md)                                   | 使用 Exa 進行網頁、程式碼與公司調研。                                                                                                          | 自製                                                                                                                           |
| [find-skills](find-skills/SKILL.md)                                 | 當使用者需要特定能力時，協助發現既有技能。                                                                                                     | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [grilling](grilling/SKILL.md)                               | 用於直接 grill 會話 的一次一題訪談循環。                                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grilling)                                |
| [teach](teach/SKILL.md) | 透過 mission、resources、lessons 與 learning records 在 workspace 中持續教學。 | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) |
| [domain-modeling](domain-modeling/SKILL.md)                   | Build and sharpen project domain terminology, `CONTEXT.md`, and ADRs.                                                                                         | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)                          |
| [karpathy-guidelines](karpathy-guidelines/SKILL.md)                 | 減少過度複雜、隱藏假設與不可驗證改動的編碼行為準則。                                                                                                           | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines)               |
| [planning-with-files](planning-with-files/SKILL.md)                 | 使用 `task_plan.md`、`findings.md`、`progress.md` 管理複雜任務。                                                                               | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.codex/skills/planning-with-files)   |
| [tdd](tdd/SKILL.md)                                                 | 功能、修復、重構或行為變更前使用；優先透過 public interface 做 integration-style 測試。                                                        | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd)                                                        |
## 貢獻

歡迎為現有技能提出改進，或新增新的技能。

1. 觸發條件要明確且可驗證。
2. 範例盡量簡潔，強調可執行性。
3. 若依賴外部工具，請在 `SKILL.md` 中明確標註依賴。
4. 新增或重新命名技能時，請同步更新主要 README 與各語言索引頁。

## 授權

本倉庫主授權條款見 [LICENSE](LICENSE)。
