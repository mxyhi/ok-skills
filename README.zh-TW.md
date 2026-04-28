# OK Skills：面向 Codex、Claude Code、Cursor、OpenClaw 等工具的 AI Coding Agent Skills 與 AGENTS.md 工作流技能集

[English](README.md) | [简体中文](README.zh-CN.md) | 繁體中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Русский](README.ru.md) | [हिन्दी](README.hi.md)

[![Mentioned in Awesome Codex CLI](https://awesome.re/mentioned-badge.svg)](https://github.com/RoggeOhta/awesome-codex-cli)

這是一個面向 Codex、Claude Code、Cursor、OpenClaw、Trae 以及其他相容 `SKILL.md` / `AGENTS.md` 工作流工具的 AI coding agent skills 倉庫。

目前倉庫共收錄 **36 個可重用技能**：其中 **28 個頂層技能** 由本倉直接維護，另有 **8 個 GSAP 動畫技能** 以 vendored bundle 形式放在 [`gsap-skills/`](gsap-skills/) 目錄下。將它 clone 到 `~/.agents/skills/ok-skills` 即可，倉庫內部目錄已符合 `AGENTS.md` 所需的 skills 佈局。

如果你正在找 **Codex skills**、**Claude Code skills**、**Cursor skills**、**OpenClaw skills**、可重用的 **AGENTS.md** 範本，或一套能直接落地的 **SKILL.md** 範例倉庫，這個專案就是為了搜尋可發現性與開箱即用而整理的。

**高頻使用場景：** 最新文件查詢、瀏覽器自動化、GitHub Actions 排障、提示工程、複雜任務規劃、前端設計，以及 PDF / Word / PPTX / XLSX 內容處理。

## 適合誰

- 你正在使用 Codex、Claude Code、Cursor、OpenClaw、Trae 或其他 AI coding agent，希望重用技能，而不是每次臨時撰寫 prompt。
- 你正在維護 `AGENTS.md` / `SKILL.md` 體系，希望同一套工作流能在不同專案之間攜帶與復用。
- 你需要現成可用的文件查詢、瀏覽器自動化、GitHub 工作流、規劃、提示工程、前端設計、PDF、Office 文件、簡報與試算表技能。

## 建議先安裝這幾個

如果你第一次使用這個倉庫，優先從下面幾個技能開始：

- [brainstorming](brainstorming/SKILL.md)：在進入實作前先梳理想法、需求與設計。
- [planning-with-files](planning-with-files/SKILL.md)：適合複雜任務、調研任務與多輪推進任務的檔案式規劃。
- [find-docs](find-docs/SKILL.md)：查詢最新函式庫文件、API 參考與 Context7 範例。
- [agent-browser](agent-browser/SKILL.md)：瀏覽器自動化、截圖、抓取、表單填寫與 Web QA。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：讀取 GitHub Actions 失敗日誌並輸出修復方案。

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
  find-docs/
    SKILL.md
  agent-browser/
    SKILL.md
  ...
```

接著在 `AGENTS.md` 裡加入最小觸發規則：

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
- [get-api-docs](get-api-docs/SKILL.md)：撰寫第三方 API / SDK 程式碼前先抓取當前文件。
- [find-skills](find-skills/SKILL.md)：當使用者提出能力需求時，先檢查是否已有現成 skill 可用。

### 規劃與提示工程

- [brainstorming](brainstorming/SKILL.md)：在進入實作前先梳理想法、需求與設計。
- [planning-with-files](planning-with-files/SKILL.md)：透過 `task_plan.md`、`findings.md`、`progress.md` 管理複雜任務。
- [improve-codebase-architecture](improve-codebase-architecture/SKILL.md)：找出能提升 locality、leverage、可測試性與 AI 可導覽性的架構 deepening 機會。
- [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)：將測試中的 `as` 型別斷言遷移到 `@total-typescript/shoehorn`。
- [tdd](tdd/SKILL.md)：功能、修復、重構或行為變更前執行 test-first red-green-refactor。
- [systematic-debugging](systematic-debugging/SKILL.md)：遇到 bug、測試失敗或異常行為時，先系統化追查根因，再提出修復。

### GitHub 工作流

- [gh-address-comments](gh-address-comments/SKILL.md)：使用 `gh` 處理目前分支 PR 的 review / issue 留言。
- [gh-fix-ci](gh-fix-ci/SKILL.md)：讀取 GitHub Actions 失敗日誌並制定修復計畫。
- [yeet](yeet/SKILL.md)：僅在使用者明確要求用 `gh` 一次完成 stage、commit、push 與建立 GitHub PR 時使用。

### 自動化與 QA

- [agent-browser](agent-browser/SKILL.md)：瀏覽器導覽、表單、截圖、抓取與網頁測試。
- [browser-use](browser-use/SKILL.md)：持久化瀏覽器自動化 CLI，用於導覽、頁面狀態檢查、表單填寫、截圖和資訊擷取。
- [opencli](opencli/opencli-usage/SKILL.md)：將網站變成 CLI，重用瀏覽器登入狀態，支援公開 API 存取與 AI 生成適配器。

- [dogfood](dogfood/SKILL.md)：系統化探索測試，並輸出可重現的證據。
- [electron](electron/SKILL.md)：透過 Chrome DevTools Protocol 自動化 Electron 桌面應用。

`dogfood/` 和 `electron/` 仍然 vendored 自 `vercel-labs/agent-browser`，但 upstream 在提交 `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` 中把它們從 `skills/` 挪到了 `skill-data/`，讓 installer 的發現邏輯只暴露引導用的 `agent-browser` skill。本倉仍把這兩個 specialized skills 保留為頂層目錄，因為它們依然由 upstream 維護，且可以直接使用。

### 前端與設計

- [ai-elements](ai-elements/SKILL.md)：為 `ai-elements` 元件庫建立 AI 對話介面元件。
- [frontend-skill](frontend-skill/SKILL.md)：適用於需要強視覺表現的著陸頁、網站、應用、原型、示範或遊戲 UI。
- [shader-dev](shader-dev/SKILL.md)：提供系統化的 GLSL 著色器技巧，用於打造相容 ShaderToy 的即時視覺效果。
- [better-icons](better-icons/SKILL.md)：透過 CLI 或 MCP 搜尋、瀏覽並取得 200+ Iconify 圖示庫中的 SVG 圖示。
- [`gsap-skills/`](gsap-skills/)：8 個官方 GSAP 動畫技能包，涵蓋 core、timeline、ScrollTrigger、plugins、utils、React、performance、frameworks。

### 工具與內容製作

- [minimax-docx](minimax-docx/SKILL.md)：基於 OpenXML SDK（.NET）的專業 DOCX 建立、編輯與格式編排。
- [minimax-pdf](minimax-pdf/SKILL.md)：使用 token 化設計系統生成、填寫與重排 PDF 文件。
- [pptx-generator](pptx-generator/SKILL.md)：使用 PptxGenJS、XML 工作流或 markitdown 來建立、編輯與讀取 PowerPoint 簡報。
- [minimax-xlsx](minimax-xlsx/SKILL.md)：以低損 XML 工作流開啟、建立、讀取、分析、編輯與驗證 Excel／試算表檔案。

## Vendored Skill Packs

[`gsap-skills/`](gsap-skills/) 目錄收錄了來自 [`greensock/gsap-skills`](https://github.com/greensock/gsap-skills) 的 GSAP 動畫技能包，目前同步基於提交 `aed9cfd3277740755f6bfc1155c7aa645403b760`。

其中包括：

- `gsap-core`
- `gsap-timeline`
- `gsap-scrolltrigger`
- `gsap-plugins`
- `gsap-utils`
- `gsap-react`
- `gsap-performance`
- `gsap-frameworks`

歸屬與法律文件保存在 [`gsap-skills/NOTICE.md`](gsap-skills/NOTICE.md) 與 [`gsap-skills/LICENSE`](gsap-skills/LICENSE)。

[`planning-with-files/`](planning-with-files/) 對應的上游基線是 [`OthmanAdi/planning-with-files/.pi/skills/planning-with-files`](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)。本倉保留通用的 `planning-with-files` 名稱，並移除 Pi 專屬套件中繼資料，使其繼續相容標準 `SKILL.md` 工作流。

## 常見前置條件

- 部分 GitHub 相關技能預設你已安裝並登入 `gh`。
- 瀏覽器類技能通常需要可用的 Chrome/CDP 環境。
- 文件查詢類技能可能依賴額外 CLI 或 MCP 工具，請以各自的 `SKILL.md` 為準。

## 完整技能索引

`Source URL` 欄位優先指向技能的 canonical upstream；如果沒有獨立上游，則指向目前倉庫內該技能目錄的 GitHub 位址。

### 頂層技能

| 技能                                                                | 說明                                                                                                                                           | Source URL                                                                                                                     |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [agent-browser](agent-browser/SKILL.md)                             | 面向 AI agents 的瀏覽器自動化：導覽、表單、截圖、資料擷取與網頁測試。                                                                          | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skills/agent-browser)                       |
| [ai-elements](ai-elements/SKILL.md)                                 | 為 ai-elements 元件庫建立新的 AI 對話介面元件，遵循可組合模式與 shadcn/ui 慣例。                                                               | [vercel/ai-elements](https://github.com/vercel/ai-elements/tree/main/skills/ai-elements)                                       |
| [better-icons](better-icons/SKILL.md)                               | 透過 CLI 或 MCP 工具搜尋 200+ Iconify 圖示庫並取得 SVG 圖示。                                                                                  | [better-auth/better-icons](https://github.com/better-auth/better-icons/tree/main/skills)                                       |
| [brainstorming](brainstorming/SKILL.md)                               | 透過協作式對話把想法整理成已確認的設計與規格，再進入實作。                                                                                                       | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/brainstorming)                                        |
| [browser-use](browser-use/SKILL.md)                                 | 持久化瀏覽器自動化 CLI，用於導覽、頁面狀態檢查、表單填寫、截圖和資訊擷取。                                                                     | [browser-use/browser-use](https://github.com/browser-use/browser-use/tree/main/skills/browser-use)                             |
| [caveman](caveman/SKILL.md)                                         | 用「穴居人」式極簡表達壓縮回覆 tokens，同時保留完整技術準確性，並支援多段強度。                                                                | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/main/caveman)                                            |
| [find-docs](find-docs/SKILL.md)                                     | 使用 Context7 CLI 查詢最新文件、API 參考與程式碼範例。                                                                                         | [upstash/context7](https://github.com/upstash/context7/tree/master/skills/find-docs)                                           |
| [minimax-docx](minimax-docx/SKILL.md) | 基於 OpenXML SDK（.NET）的專業 DOCX 建立、編輯與格式編排。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-docx) |
| [exa-search](exa-search/SKILL.md)                                   | 使用 Exa 進行網頁、程式碼與公司調研。                                                                                                          | 自製                                                                                                                           |
| [find-skills](find-skills/SKILL.md)                                 | 當使用者需要特定能力時，協助發現既有技能。                                                                                                     | [vercel-labs/skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills)                                       |
| [frontend-skill](frontend-skill/SKILL.md)                           | 建立具有強視覺表現的著陸頁、網站、應用、原型、示範或遊戲 UI。                                                                                  | [ok-skills/frontend-skill](frontend-skill/SKILL.md)                                                                            |
| [shader-dev](shader-dev/SKILL.md) | 提供系統化的 GLSL 著色器技巧，用於打造相容 ShaderToy 的即時視覺效果。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/shader-dev) |
| [get-api-docs](get-api-docs/SKILL.md)                               | 在撰寫第三方 API / SDK 程式碼前先抓取當前文件。                                                                                                | [andrewyng/context-hub](https://github.com/andrewyng/context-hub/tree/main/cli/skills/get-api-docs)                            |
| [gh-address-comments](gh-address-comments/SKILL.md)                 | 使用 `gh` 處理目前分支 PR 的評審與 issue 留言。                                                                                                | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-address-comments)                                |
| [gh-fix-ci](gh-fix-ci/SKILL.md)                                     | 檢查 GitHub Actions 失敗項、提取日誌並制定修復計畫。                                                                                           | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)                                          |
| [improve-codebase-architecture](improve-codebase-architecture/SKILL.md) | 找出能提升 locality、leverage、可測試性與 AI 可導覽性的架構 deepening 機會。                                                                   | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture)                              |
| [migrate-to-shoehorn](migrate-to-shoehorn/SKILL.md)                 | 將測試檔案中的 `as` 型別斷言遷移到 `@total-typescript/shoehorn`。                                                                              | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/migrate-to-shoehorn)                                        |
| [opensrc](opensrc/SKILL.md)                                         | 抓取依賴原始碼，為 AI agents 提供更深的實作上下文。                                                                                            | [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc/tree/main/skills/opensrc)                                         |
| [opencli](opencli/opencli-usage/SKILL.md)                                         | 將網站變成 CLI，重用瀏覽器登入狀態，支援公開 API 存取與 AI 生成適配器。                                                                        | [jackwener/opencli](https://github.com/jackwener/opencli/tree/main/skills)                                                                      |
| [dogfood](dogfood/SKILL.md)                                         | 系統化測試 Web 應用，並產出附帶截圖與錄影的可重現問題報告。                                                                                    | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/dogfood)                                         |
| [electron](electron/SKILL.md)                                       | 透過 agent-browser 與 Chrome DevTools Protocol 自動化 Electron 桌面應用。                                                                      | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser/tree/main/skill-data/electron)                                        |
| [minimax-pdf](minimax-pdf/SKILL.md) | 使用 token 化設計系統生成、填寫與重排 PDF 文件。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-pdf) |
| [planning-with-files](planning-with-files/SKILL.md)                 | 使用 `task_plan.md`、`findings.md`、`progress.md` 管理複雜任務。                                                                               | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files/tree/master/.pi/skills/planning-with-files)   |
| [pptx-generator](pptx-generator/SKILL.md) | 使用 PptxGenJS、XML 工作流或 markitdown 來建立、編輯與讀取 PowerPoint 簡報。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/pptx-generator) |
| [tdd](tdd/SKILL.md)                                                 | 功能、修復、重構或行為變更前使用；優先透過 public interface 做 integration-style 測試。                                                        | [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/tdd)                                                        |
| [systematic-debugging](systematic-debugging/SKILL.md)             | 遇到任何 bug、測試失敗或異常行為時，在提出修復前先使用。                                                                                     | [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging)                                  |
| [minimax-xlsx](minimax-xlsx/SKILL.md) | 以低損 XML 工作流開啟、建立、讀取、分析、編輯與驗證 Excel／試算表檔案。 | [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills/tree/main/skills/minimax-xlsx) |
| [yeet](yeet/SKILL.md)                                               | 僅在使用者明確要求用 `gh` 一次完成 stage、commit、push 與建立 GitHub PR 時使用。                                                               | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/yeet)                                               |

說明：
- `dogfood` 和 `electron` 的上游路徑在 `skill-data/`，不在 upstream 的 `skills/`。
- upstream 在提交 `7c2ff0a2a624e86cec0bcc9cc0835aeff6a2edf0` 中遷移了這些 specialized skills，以便 installer 的發現邏輯只找到引導 skill `agent-browser`。
- 本倉有意繼續把它們作為頂層 vendored skills 保留，因為它們仍在 upstream 持續維護，且具備直接使用價值。

### Vendored `gsap-skills/` 技能

| 技能                                                          | 說明                                                                                           | Source URL                                                                                            |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [gsap-core](gsap-skills/gsap-core/SKILL.md)                   | 核心 API：`gsap.to()` / `from()` / `fromTo()`，緩動、duration、stagger、defaults、matchMedia。 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-core)          |
| [gsap-timeline](gsap-skills/gsap-timeline/SKILL.md)           | Timeline：時序編排、position 參數、labels、巢狀與播放控制。                                    | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-timeline)      |
| [gsap-scrolltrigger](gsap-skills/gsap-scrolltrigger/SKILL.md) | ScrollTrigger：滾動驅動動畫、pin、scrub、觸發器、refresh、清理。                               | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-scrolltrigger) |
| [gsap-plugins](gsap-skills/gsap-plugins/SKILL.md)             | 外掛：Flip、Draggable、MotionPath、ScrollToPlugin、CustomEase 等。                             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-plugins)       |
| [gsap-utils](gsap-skills/gsap-utils/SKILL.md)                 | gsap.utils：clamp、mapRange、normalize、random、snap、toArray、wrap、pipe。                    | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-utils)         |
| [gsap-react](gsap-skills/gsap-react/SKILL.md)                 | React：useGSAP、refs、`gsap.context()`、清理、SSR。                                            | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-react)         |
| [gsap-performance](gsap-skills/gsap-performance/SKILL.md)     | 效能：transform 優先、will-change、批次處理、ScrollTrigger 效能建議。                          | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-performance)   |
| [gsap-frameworks](gsap-skills/gsap-frameworks/SKILL.md)       | Vue、Svelte 等：生命週期、選擇器作用域、卸載清理。                                             | [greensock/gsap-skills](https://github.com/greensock/gsap-skills/tree/main/skills/gsap-frameworks)    |

## 貢獻

歡迎為現有技能提出改進，或新增新的技能。

1. 觸發條件要明確且可驗證。
2. 範例盡量簡潔，強調可執行性。
3. 若依賴外部工具，請在 `SKILL.md` 中明確標註依賴。
4. 新增或重新命名技能時，請同步更新主要 README 與各語言索引頁。

## 授權

本倉庫主授權條款見 [LICENSE](LICENSE)。

部分技能目錄包含額外授權或歸屬說明文件，包括 [`improve-codebase-architecture/`](improve-codebase-architecture/)、[`migrate-to-shoehorn/`](migrate-to-shoehorn/)、[`minimax-docx/`](minimax-docx/) 與 [`gsap-skills/`](gsap-skills/)。
