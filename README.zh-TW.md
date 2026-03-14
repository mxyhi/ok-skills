# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw 等工具的 AI Coding Agent Skills 與 AGENTS.md 工作流技能集

[English](README.md) | [简体中文](README.zh-CN.md) | 繁體中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

這是一個面向 Codex、Claude Code、Cursor、OpenClaw、Trae 以及其他相容 `SKILL.md` / `AGENTS.md` 工作流工具的 AI coding agent skills 倉庫。

目前倉庫共收錄 **41 個可重用技能**：其中 **23 個頂層技能** 由本倉直接維護，另有 **18 個前端設計技能** 以 vendored bundle 形式放在 [`impeccable/`](impeccable/README.md) 目錄下。將它 clone 到 `~/.agents/skills/ok-skills` 即可，倉庫內部目錄已符合 `AGENTS.md` 所需的 skills 佈局。

如果你正在找 **Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、可重用的 **AGENTS.md** 範本，或一套能直接落地的 **SKILL.md** 範例倉庫，這個專案就是為了搜尋可發現性與開箱即用而整理的。

**高頻使用場景：** 最新文件查詢、瀏覽器自動化、GitHub Actions 排障、提示工程、複雜任務規劃、前端設計，以及 PDF / Word / PPTX / XLSX 內容處理。

## 適合誰

- 你正在使用 Codex、Claude Code、Cursor、OpenClaw、Trae 或其他 AI coding agent，希望重用技能，而不是每次臨時撰寫 prompt。
- 你正在維護 `AGENTS.md` / `SKILL.md` 體系，希望同一套工作流能在不同專案之間攜帶與復用。
- 你需要現成可用的文件查詢、瀏覽器自動化、GitHub 工作流、規劃、提示工程、前端設計、PDF、Office 文件、簡報與試算表技能。

## 建議先安裝這幾個

如果你第一次使用這個倉庫，優先從下面幾個技能開始：

- [planning-with-files](planning-with-files/SKILL.md)：適合複雜任務、調研任務與多輪推進任務的檔案式規劃。
- [context7-cli](context7-cli/SKILL.md)：查詢最新函式庫文件、Context7 參考資料與 MCP 相關內容。
- [agent-browser](agent-browser/SKILL.md)：瀏覽器自動化、截圖、抓取、表單填寫與 Web QA。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：讀取 GitHub Actions 失敗日誌並輸出修復方案。
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md)：更穩定、可控、面向生產的提示工程模式。
- [impeccable/frontend-design](impeccable/frontend-design/SKILL.md)：高品質前端介面設計技能，以及一整套配套設計指令。

## 1 分鐘快速開始

```bash
mkdir -p ~/.agents/skills
cd ~/.agents/skills
git clone https://github.com/mxyhi/ok-skills.git ok-skills
```

clone 後，倉庫會位於 `~/.agents/skills/ok-skills`，其內部目錄已符合預期佈局：

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

接著在 `AGENTS.md` 裡加入最小觸發規則：

```md
## Skills
- planning-with-files: 用於複雜任務、調研任務，或預計會有 5 次以上工具呼叫的工作。
- context7-cli: 需要最新函式庫文件、API 參考或 Context7 範例時使用。
- agent-browser: 需要瀏覽器自動化、截圖、抓取、網頁測試或表單填寫時使用。
```

之後就可以自然觸發：

- `在重構這個模組之前先用 planning-with-files。`
- `用 context7-cli 查一下這個 SDK 的最新文件。`
- `用 agent-browser 重現這個 UI 問題。`

## 按場景瀏覽技能

### 調研與文件

- [context7-cli](context7-cli/SKILL.md)：官方 Context7 CLI 的文件查詢、skill 管理與 MCP 設定工作流。
- [exa-search](exa-search/SKILL.md)：使用 Exa 進行網頁、程式碼與公司調研。
- [get-api-docs](get-api-docs/SKILL.md)：撰寫第三方 API / SDK 程式碼前先抓取當前文件。
- [find-skills](find-skills/SKILL.md)：當使用者提出能力需求時，先檢查是否已有現成 skill 可用。

### 規劃與提示工程

- [brainstorming](brainstorming/SKILL.md)：在實作前先釐清意圖、需求與設計。
- [planning-with-files](planning-with-files/SKILL.md)：透過 `task_plan.md`、`findings.md`、`progress.md` 管理複雜任務。
- [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md)：面向生產環境的進階提示工程模式。
- [test-driven-development](test-driven-development/SKILL.md)：任何功能或修復都先寫測試。

### GitHub 工作流

- [gh-address-comments](gh-address-comments/SKILL.md)：使用 `gh` 處理目前分支 PR 的 review / issue 留言。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：讀取 GitHub Actions 失敗日誌並制定修復計畫。
- [yeet](yeet/SKILL.md)：僅在使用者明確要求用 `gh` 一次完成 stage、commit、push 與建立 GitHub PR 時使用。

### 自動化與 QA

- [agent-browser](agent-browser/SKILL.md)：瀏覽器導覽、表單、截圖、抓取與網頁測試。
- [pinchtab](pinchtab/SKILL.md)：透過 Pinchtab 的本地 HTTP API 控制 Chrome，利用穩定的 accessibility refs 進行自動化與擷取。
- [electron](electron/SKILL.md)：透過 Chrome DevTools Protocol 自動化 Electron 桌面應用。
- [dogfood](dogfood/SKILL.md)：系統化探索測試，並輸出可重現的證據。

### 前端與設計

- [ai-elements](ai-elements/SKILL.md)：為 `ai-elements` 元件庫建立 AI 對話介面元件。
- [vercel-react-best-practices](vercel-react-best-practices/SKILL.md)：來自 Vercel Engineering 的 React / Next.js 效能實踐。
- [remotion-best-practices](remotion-best-practices/SKILL.md)：基於 React 的 Remotion 影片開發最佳實踐。
- [`impeccable/`](impeccable/README.md)：18 個 vendored 前端設計技能，包含 `frontend-design`、`adapt`、`audit`、`polish` 等。

### 工具與內容製作

- [docx](docx/SKILL.md)：建立、讀取、編輯與處理 Word 文件，涵蓋格式、批註與修訂。
- [pdf](pdf/SKILL.md)：讀取、產生與審查 PDF，強調渲染後的視覺檢查。
- [pptx](pptx/SKILL.md)：建立、讀取、編輯與處理簡報、模板與投影片內容。
- [xlsx](xlsx/SKILL.md)：試算表建立、編輯、公式、格式與分析。
- [skill-creator](skill-creator/SKILL.md)：建立或更新技能，補齊結構、文件與工具整合。

## Vendored Skill Packs

[`impeccable/`](impeccable/README.md) 目錄收錄了來自 [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) 的前端設計技能包，目前同步基於提交 `0df1ba59dc80b8b1891ee42eed0ef4e03d7ef165`。

其中包括：

- `frontend-design` 主技能
- `adapt`、`animate`、`audit`、`bolder`、`clarify`、`colorize`、`critique`、`delight`、`distill`
- `extract`、`harden`、`normalize`、`onboard`、`optimize`、`polish`、`quieter`、`teach-impeccable`

歸屬與法律文件保存在 [`impeccable/NOTICE.md`](impeccable/NOTICE.md) 與 [`impeccable/LICENSE`](impeccable/LICENSE)。

## 常見前置條件

- 部分 GitHub 相關技能預設你已安裝並登入 `gh`。
- 瀏覽器類技能通常需要可用的 Chrome/CDP 環境。
- 文件查詢類技能可能依賴額外 CLI 或 MCP 工具，請以各自的 `SKILL.md` 為準。

## 完整技能索引

`Source URL` 欄位優先指向技能的 canonical upstream；如果沒有獨立上游，則指向目前倉庫內該技能目錄的 GitHub 位址。

### 頂層技能

| 技能 | 說明 | Source URL |
| --- | --- | --- |
| [agent-browser](agent-browser/SKILL.md) | 面向 AI agents 的瀏覽器自動化：導覽、表單、截圖、資料擷取與網頁測試。 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser) |
| [ai-elements](ai-elements/SKILL.md) | 為 ai-elements 元件庫建立新的 AI 對話介面元件，遵循可組合模式與 shadcn/ui 慣例。 | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements) |
| [brainstorming](brainstorming/SKILL.md) | 在任何實作前先釐清意圖、需求與設計。 | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| [context7-cli](context7-cli/SKILL.md) | 使用 Context7 CLI 完成文件查詢、skill 管理與 MCP 設定。 | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/context7-cli) |
| [docx](docx/SKILL.md) | 建立、讀取、編輯與處理 Word 文件，涵蓋格式、批註、修訂與圖片替換。 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/docx) |
| [dogfood](dogfood/SKILL.md) | 系統化測試 Web 應用，並產出附帶截圖與錄影的可重現問題報告。 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/dogfood) |
| [electron](electron/SKILL.md) | 透過 agent-browser 與 Chrome DevTools Protocol 自動化 Electron 桌面應用。 | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/electron) |
| [exa-search](exa-search/SKILL.md) | 使用 Exa 進行網頁、程式碼與公司調研。 | 自製 |
| [find-skills](find-skills/SKILL.md) | 當使用者需要特定能力時，協助發現既有技能。 | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| [get-api-docs](get-api-docs/SKILL.md) | 在撰寫第三方 API / SDK 程式碼前先抓取當前文件。 | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs) |
| [gh-address-comments](gh-address-comments/SKILL.md) | 使用 `gh` 處理目前分支 PR 的評審與 issue 留言。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments) |
| [gh-fix-ci](gh-fix-ci/SKILL.md) | 檢查 GitHub Actions 失敗項、提取日誌並制定修復計畫。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci) |
| [pdf](pdf/SKILL.md) | 處理 PDF 的讀取、產生與審查，強調渲染後的視覺檢查。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/pdf) |
| [pinchtab](pinchtab/SKILL.md) | 透過 Pinchtab 的 HTTP API 控制 headless 或 headed Chrome，用於網頁自動化、抓取、表單填寫、導覽、截圖與基於穩定 accessibility refs 的內容擷取。 | [pinchtab/pinchtab](https://github.com/pinchtab/pinchtab/tree/main/skill/pinchtab) |
| [planning-with-files](planning-with-files/SKILL.md) | 使用 `task_plan.md`、`findings.md`、`progress.md` 管理複雜任務。 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.agent/skills/planning-with-files) |
| [pptx](pptx/SKILL.md) | 建立、讀取、編輯與處理 PowerPoint 簡報，涵蓋模板、版面、備註與投影片內容。 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| [prompt-engineering-patterns](prompt-engineering-patterns/SKILL.md) | 面向生產環境的進階提示工程模式。 | [wshobson/agents](https://github.com/wshobson/agents/tree/main/plugins/llm-application-dev/skills/prompt-engineering-patterns) |
| [remotion-best-practices](remotion-best-practices/SKILL.md) | 用於 React + Remotion 影片開發的最佳實踐。 | [remotion-dev/skills](https://github.com/remotion-dev/skills/tree/main/skills/remotion) |
| [skill-creator](skill-creator/SKILL.md) | 建立或更新技能，補齊專業知識、工作流與工具整合。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.system/skill-creator) |
| [test-driven-development](test-driven-development/SKILL.md) | 實作任何功能或修復前先使用。 | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) |
| [vercel-react-best-practices](vercel-react-best-practices/SKILL.md) | 來自 Vercel Engineering 的 React / Next.js 效能最佳實踐。 | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| [xlsx](xlsx/SKILL.md) | 涵蓋試算表建立、編輯、公式、格式與分析。 | [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| [yeet](yeet/SKILL.md) | 僅在使用者明確要求用 `gh` 一次完成 stage、commit、push 與建立 GitHub PR 時使用。 | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet) |

### Vendored `impeccable/` 技能

| 技能 | 說明 | Source URL |
| --- | --- | --- |
| [frontend-design](impeccable/frontend-design/SKILL.md) | 建立有辨識度、可用於生產環境的高品質前端介面。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [adapt](impeccable/adapt/SKILL.md) | 讓設計適配不同螢幕尺寸、裝置與上下文。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [animate](impeccable/animate/SKILL.md) | 以有目的的動畫與微互動強化介面。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [audit](impeccable/audit/SKILL.md) | 稽核介面的可存取性、效能、主題與響應式表現。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [bolder](impeccable/bolder/SKILL.md) | 讓過於保守或平淡的設計更有張力。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [clarify](impeccable/clarify/SKILL.md) | 改善不清楚的 UX 文案與說明。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [colorize](impeccable/colorize/SKILL.md) | 為過於單色的介面加入策略性色彩。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [critique](impeccable/critique/SKILL.md) | 從 UX 視角評估設計效果。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [delight](impeccable/delight/SKILL.md) | 為介面加入個性與令人記住的細節。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [distill](impeccable/distill/SKILL.md) | 將設計提煉到本質，去除多餘複雜度。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [extract](impeccable/extract/SKILL.md) | 抽取並整合可重用元件、tokens 與模式。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [harden](impeccable/harden/SKILL.md) | 提升錯誤處理、i18n、溢出與邊界情況的韌性。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [normalize](impeccable/normalize/SKILL.md) | 讓功能對齊設計系統並保持一致性。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [onboard](impeccable/onboard/SKILL.md) | 改善導覽流程、空狀態與首次使用體驗。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [optimize](impeccable/optimize/SKILL.md) | 優化載入、渲染、動畫、圖片與包體積。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [polish](impeccable/polish/SKILL.md) | 上線前打磨對齊、間距、一致性與細節。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [quieter](impeccable/quieter/SKILL.md) | 降低過強的視覺侵略性，同時保留設計品質。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| [teach-impeccable](impeccable/teach-impeccable/SKILL.md) | 收集設計上下文並保存為後續工作的長期指引。 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |

## 貢獻

歡迎為現有技能提出改進，或新增新的技能。

1. 觸發條件要明確且可驗證。
2. 範例盡量簡潔，強調可執行性。
3. 若依賴外部工具，請在 `SKILL.md` 中明確標註依賴。
4. 新增或重新命名技能時，請同步更新主要 README 與各語言索引頁。

## 授權

本倉庫主授權條款見 [LICENSE](LICENSE)。

部分技能目錄包含額外授權或歸屬說明文件，包括 [`docx/`](docx/)、[`pptx/`](pptx/)、[`impeccable/`](impeccable/README.md)、[`skill-creator/`](skill-creator/) 與 [`xlsx/`](xlsx/)。
