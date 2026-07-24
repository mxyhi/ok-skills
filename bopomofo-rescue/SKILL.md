---
name: bopomofo-rescue
description: >-
  Detect and recover text that was accidentally typed with the Taiwanese
  Bopomofo / Zhuyin (注音) keyboard while the input method (IME) was stuck in
  English/ASCII mode — what Taiwanese users call 注音亂碼 or 注音文 —
  producing meaningless-looking letter+digit sequences such as
  "su3cl3a8", "cl3", "g4", "2k7", "vu,4", or such garbled runs embedded in an
  otherwise normal request (e.g. "help me fix su3cl3a8", "看看這個 PR qk4ru.6",
  "幫我改 su3cl3a8xk7"). Use this skill whenever a user message contains short
  ASCII tokens that look like keyboard gibberish, do not form real English
  words, and cannot be understood normally — especially tokens with digits
  interspersed among letters (tone keys 3/4/6/7 or vowel keys 8/9/0), which are
  a strong sign of Mandarin phonetic keystrokes typed in the wrong input mode.
  Run scripts/decode_bopomofo.py to deterministically map the keystrokes back
  to 注音 symbols with a confidence score, then interpret the intended
  Traditional Chinese in context and continue the user's original request
  without making them retype. Do NOT trigger on genuine technical strings —
  code, file paths, URLs, git hashes, CLI flags, package names, version numbers
  — the script's exclusion rules and confidence tiers already filter these out.
  Especially valuable for Taiwanese developers who forget to switch input
  methods when prompting AI coding agents.
allowed-tools: Bash(python "${CLAUDE_SKILL_DIR}/scripts/decode_bopomofo.py" *)
---

# 注音鍵盤誤打還原 (Bopomofo Input Recovery)

## 安裝前提 (Prerequisite)

這個 skill 需要**上游 repo 內附的解碼腳本與注音詞典**（約 5 MB）才能運作；本目錄
只收錄 `SKILL.md` 與參考資料。請直接從來源安裝：

```bash
git clone https://github.com/Oliviaiii/bopomofo-rescue.git ~/.claude/skills/bopomofo-rescue
```

安裝後會一併掛上 `UserPromptSubmit` hook，訊息送出當下就自動解碼，不需任何前綴指令。
需要 Python 3，且 `python` 在 PATH 上。

**This skill requires the decoder script and Bopomofo dictionary (~5 MB) bundled in the
upstream repository** — only `SKILL.md` and `references/` are vendored here. Install from
source with the command above. Requires Python 3 on PATH.

## 這個 skill 在解決什麼

台灣工程師常用注音輸入法。忘記把輸入法從英文切回中文時，本來想打的中文會
變成一串按鍵序列 —— 例如想打「你好嗎」卻打出 `su3cl3a8`。這串不是英文、也
不是亂碼，而是**注音鍵盤的實體按鍵**。這個 skill 把它還原回中文，讓你不必
重打就能繼續原本的請求。

## 核心原則

**還原這一步一定要用 `scripts/decode_bopomofo.py`，不要自己心算。**
LLM 自己硬猜按鍵映射經常出錯（例如會把 `dj94` 說成「是的」，實際是「快」）。
這支程式是純查表 + 音節切分 + 詞典斷詞（IME 式最大機率），會直接給你**注音**與
**中文猜測**。你的工作是**用上下文確認或修正**它的猜測 —— 這是你的強項，因為
同音字要靠前後文消歧（`ㄕˋ` = 是/事/世/市…），而標準 IME 沒有上下文、你有。

## 工作流程

當使用者訊息可能含注音誤打時：

1. **執行腳本**（把整段原始訊息交給它，它會自己挑出候選、跳過技術字串）：

   ```bash
   python "${CLAUDE_SKILL_DIR}/scripts/decode_bopomofo.py" --brief "使用者的原始訊息"
   ```

   **預設用 `--brief`**：只回傳判讀所需欄位，約為完整 JSON 的 10%，省下大量
   context。需要同音字候選或除錯時再拿掉 `--brief`（完整輸出含
   `chinese_alternatives`、`confidence` 等；`--full` 另外附上所有 token 的 `segments`）。

   輸出 JSON 的重點欄位：
   - `has_candidates`：是否偵測到疑似誤打中文。
   - `candidates[]`：每個候選的 `bopomofo`（注音）、`chinese`（詞典最佳中文猜測）、
     `tier`（信心分級）、以及可能出現的 `repair`（打字手誤補救建議，見下）。
   - `reconstructed`：把候選換成**中文**（詞典可用時）或 `[注音]` 的整句版本，直接可讀。

2. **依 `tier` 決定行為**（見下）。

3. **用上下文確認 `chinese` 猜測**，代回原句，然後**照還原後的意思繼續做事**。

## 依信心分級的行為

腳本已經把 `confidence` 轉成三級。請照這個原則反應，重點是**不要打斷開發節奏**：

| tier | 信心 | 建議行為 |
|------|------|----------|
| `high` | ≥ 0.90 | **靜默還原**，直接照還原後的意思繼續。不用大張旗鼓宣告。 |
| `medium` | 0.65–0.89 | 用**一句話**標註你的推測（例：「`su3cl3a8` 我理解為『你好嗎』」）再繼續。 |
| `low` | < 0.65 | **預設不動**。只有在上下文讓意思非常明顯時才採用，否則照原文理解。 |

`low` 多半是純字母、能硬切成音節但其實可能是英文的 token（如 `npm`、`git`、
`html`）。這類**寧可放過**，除非整句語境明顯是中文而這個 token 格格不入。

## 確認中文猜測（你的工作）

腳本已用詞頻詞典給出 `chinese` 最佳猜測（常見句多半直接正確）。你負責**用上下文
把關**：

- **預設採用 `chinese`**。像 `su3cl3a8` → 你好嗎、`g42k7` → 是的，通常直接對。
- **語境不合時，改看 `chinese_alternatives`**。詞典只看頻率、不看上下文；若最佳
  猜測在句中不通，從同音候選裡挑合理的（`ㄕˋ` 的候選：是/試/時/十/事…）。
- **若怎麼拼都不成合理中文**，就**退回原文**照字面理解，別硬湊。這個 fallback
  很重要 —— 誤把 `npm run dev` 當中文會造成實際傷害。
- 詞典缺席時（未安裝資料檔）`chinese` 會是空的、只有 `bopomofo`，這時就由你依
  注音在上下文中判讀。

## `repair`：打字手誤的補救建議

有時 tier 是 `high`、注音也切得出來，但 `chinese` 是空的 —— 這通常代表**相鄰兩鍵
打反**了。例如「說」= ㄕㄨㄛ 應打 `gji`，快打成 `jgi`，切出來變 ㄨ + ㄕㄛ：音節合法，
但國語沒有這個詞，詞典自然查無。

這時腳本會附上 `repair` 陣列（最多 3 個建議）：

```json
"repair": [{"kind": "transpose", "from": "jgi", "to": "gji",
            "chinese": "說", "note": "相鄰兩鍵對調後詞典可完整還原"}]
```

怎麼用：

- **看到 `repair` 就優先採用它的 `chinese`**，因為原本的解讀根本還不出中文，
  而這個建議能被詞典完整還原 —— 它幾乎一定比原解讀接近使用者的本意。
- **但仍要用上下文確認**。轉置只是最常見的手誤之一，不保證就是使用者的原意。
- **若 `repair` 建議在語境中不通，就退回原解讀**（原本的 `bopomofo` 一直都保留著），
  依注音自行判讀，或直接照原文處理。
- 有多個建議時，挑語境最合理的，不必然是第一個。
- `repair` 只是建議：腳本**不會**因此改寫 `bopomofo`，也**不會**提高 `confidence`。
  最終判斷是你的工作。

## 安全界線（重要）

- 腳本已排除程式碼區塊、行內 code、URL、路徑、git hash、CLI flag、版本號、
  含大寫的識別字。你仍應**再判斷一次**：如果某個「候選」其實在語境中是檔名、
  變數、指令，就不要還原它。
- 這個 skill 只**解讀**輸入、不改變請求的意圖。還原後請照使用者**本來**的意思做事。

## 範例

**範例 1（high，靜默）**
輸入：`su3cl3a8 幫我看一下這個 function`
腳本：`chinese=你好嗎` tier=high，`reconstructed=你好嗎 幫我看一下這個 function`
你的理解：直接照「你好嗎，幫我看一下這個 function」回應請求，不用特別解釋還原過程。

**範例 2（用 alternatives 修正）**
輸入：`ej94k6 這個字怎麼念`（假設 `chinese` 猜測在語境中不通）
腳本：給 `chinese` 與各音節的 `chinese_alternatives`
你的行為：從候選裡挑語境合理的字；若仍拼不出合理中文，就退回原文。

**範例 3（技術字串，不觸發）**
輸入：`run npm install then git commit -m fix in ./src/app.py`
腳本：`has_candidates=false`
你的行為：完全照原文處理，不做任何還原。

## 參考資料

需要人工核對、或腳本不可用時，可查：
- `references/keyboard-layout.md` —— 大千式注音鍵盤完整對照表與合法韻母清單。
- `references/exclusion-rules.md` —— 哪些字串該跳過、為什麼。

但正常情況下**一律以腳本輸出為準**，不要用參考表自己重算按鍵映射。
