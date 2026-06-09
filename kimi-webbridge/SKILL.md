---
name: kimi-webbridge
description: |
  Kimi WebBridge lets AI control the user's real browser — navigate, click, type, read, screenshot, and interact with any website using the user's actual login sessions. Use this skill whenever the user wants to interact with websites, automate browser tasks, scrape web content, or perform any action requiring a real browser. Also use when the user mentions "browser", "webpage", "open URL", "screenshot", or asks to read/interact with any website. Use even for simple-sounding browser requests — the daemon handles all complexity.
---

# Kimi WebBridge

Control the user's real browser (with their login sessions) via a local daemon at `http://127.0.0.1:10086`.

## Health check (always do this first)

```bash
~/.kimi-webbridge/bin/kimi-webbridge status
```

Then act on the result:

- **`running: true` and `extension_connected: true`** — healthy. Proceed with the tool calls below.
- **Anything else** (command not found, `running: false`, `extension_connected: false`, errors) — **Read `references/operations.md`** in this skill directory. It has the install / start / diagnose routing table.

Don't guess fixes here — every non-healthy state is handled in `references/operations.md`.

## Tools

| Tool | Args | Returns | Note |
|------|------|---------|------|
| `navigate` | `url`, `newTab`(bool), `group_title` | `{success, url, tabId}` | First call opens a tab — see [Tabs](#tabs-and-the-current-tab). `group_title` sets the group's visible label |
| `find_tab` | `url`, `active`(bool) | `{success, url, tabId}` | Select an already-open tab as the current one — see [Tabs](#tabs-and-the-current-tab) |
| `snapshot` | — | `{url, title, tree}` with `@e` refs | **Accessibility tree** (text) — use this to read page content and locate elements |
| `click` | `selector` (@e ref or CSS) | `{success, tag, text}` | Synthetic `el.click()` |
| `fill` | `selector`, `value` | `{success, tag, mode}` | Works on `<input>`/`<textarea>` AND `[contenteditable]` (ProseMirror/Lexical/Slate). `mode` is `"value"` or `"contenteditable"` |
| `evaluate` | `code` (supports async/await) | `{type, value}` | |
| `screenshot` | `format`(png\|jpeg), `quality`(0-100), optional `selector` (@e/CSS), optional `path` | `{format, path, sizeBytes, mimeType}` | Returns a file path, not base64 — see [Screenshots](#screenshots) |
| `network` | `cmd`(start\|stop\|list\|detail), `filter`, `requestId` | request/response data | |
| `upload` | `selector`, `files`(string[]) | `{success, fileCount}` | |
| `save_as_pdf` | `paper_format`, `landscape`, `scale`, `print_background`, optional `path` | `{path, sizeBytes, mimeType, pageTitle}` | Render current page → PDF, returns a file path — see [Save as PDF](#save-the-current-page-as-pdf) |
| `list_tabs` | — | `{success, tabs:[{tabId, url, title, active, groupTitle}]}` | Inspect tabs in the current session |
| `close_tab` | — | `{success, closed: bool}` | Close the current tab in the session |
| `close_session` | — | `{success, closed: int}` | Close all tabs in the session — `closed` is the count. See [Sessions](#sessions) for when to call |

### Tabs and the current tab

Single-tab tools (`snapshot`, `click`, `fill`, `screenshot`, `save_as_pdf`) act on the **current tab** — the one you most recently opened with `navigate` or selected with `find_tab`.

- **Opening pages**: use `newTab:true` when pages should coexist (comparing, cross-referencing); omit it to send the current tab to a new URL.
- **Going back to an earlier tab**: call `find_tab` to make a tab you already opened the current one again. Pass the tab's **full URL** — take it from `list_tabs` or the earlier `navigate` result. A bare root domain (`zhihu.com`) may miss a `www.zhihu.com` tab, so prefer the exact URL. `active:true` picks the tab the user is currently viewing — use it when they say "用我打开的 X" / "在我当前的 X 页面上"; otherwise the leftmost match wins.
- If `find_tab` returns "no open tab found", the page isn't open — `navigate` with `newTab:true` instead.

```bash
curl -s -X POST http://127.0.0.1:10086/command \
  -d '{"action":"find_tab","args":{"url":"https://www.zhihu.com","active":true},"session":"camping-research"}'
```

### Call Format

Every command carries a top-level `session` naming the current task — see [Sessions](#sessions) below. The examples in later sections omit it only for brevity; in real calls always include it.

```bash
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"navigate","args":{"url":"https://example.com","newTab":true,"group_title":"My task"},"session":"my-task"}'
```

## Sessions

**One task = one session = one tab group.** A `session` collects every tab this task opens into a single tab group, so the user sees one group representing "what the agent is doing right now". Pass it as a **top-level field** of the request body (not inside `args`).

Rules:

1. **Pick one session name when the task starts, put it on _every_ command, and never change it mid-task.**
2. **One task uses one session — even across multiple sites.** Searching on Google and then opening results on three different domains all share the same session and land in the same group. **Do not switch session names per site** — that is the #1 cause of fragmented tab groups.
3. Name the session after the **task**, not the site or domain — e.g. `camping-research`, `phone-compare`.
4. `group_title` is the human-readable label shown on the group in the browser. Write it in the user's language (match the conversation — Chinese or English). Pass it on the **first** `navigate`; later calls in the same session don't need it.
5. Use multiple sessions **only when the user asks for several unrelated tasks at once** — one session per task.

```bash
# First tab of the task: set session + human-readable label (in the user's language)
curl -s -X POST http://127.0.0.1:10086/command \
  -d '{"action":"navigate","args":{"url":"https://www.google.com/search?q=tents","newTab":true,"group_title":"Camping gear research"},"session":"camping-research"}'

# Another SITE, SAME task → same session → joins the same group automatically
curl -s -X POST http://127.0.0.1:10086/command \
  -d '{"action":"navigate","args":{"url":"https://www.zhihu.com/search?q=tents","newTab":true},"session":"camping-research"}'

# Every later command carries the same session
curl -s -X POST http://127.0.0.1:10086/command \
  -d '{"action":"snapshot","args":{},"session":"camping-research"}'
```

When the task is finished and the user no longer needs these pages, `close_session` clears the whole group. If they might want to look further (a follow-up question, inspecting a result), deliver your answer first and leave the tabs open — closing too eagerly throws away the work the user can still see.

## Screenshots

The daemon writes the image to disk and returns `{format, path, sizeBytes, mimeType}` — never base64, since the model can't read raw image bytes. Take the `.path` and open it with the `Read` tool to actually see it.

```bash
# Default: PNG of the visible viewport, daemon picks a temp path
curl ... -d '{"action":"screenshot","args":{}}'
# Options (each independent): JPEG quality, element-only via @e/CSS selector, custom output path
curl ... -d '{"action":"screenshot","args":{"format":"jpeg","quality":60}}'
curl ... -d '{"action":"screenshot","args":{"selector":"@e123"}}'
```

A caller-supplied `path` is honored verbatim (parent dirs created, existing file overwritten) — use a unique name to avoid clobbering. `save_as_pdf` follows the same rule.

## Prefer snapshot over CSS/JS selectors

`snapshot` returns interactive elements with `@e` refs based on semantic role/name. Use them directly with click/fill — they survive CSS class hash changes that break manually-written selectors.

Fall back to `evaluate` (JS) only when:
- The target has no `@e` ref in the snapshot
- You need attributes not in the snapshot (e.g., `href`)
- You need to dispatch complex event sequences, or scroll

## Evaluate Tips

- Always use compact `JSON.stringify(data)` — never add `null, 2` formatting. Indentation and newlines can inflate the response several times over, causing truncation during transmission.
- `evaluate` calls share the page's JS realm — re-declaring the same `const`/`let` across two calls throws `SyntaxError`. Wrap in an IIFE for a fresh scope: `(() => { const x = ...; return x; })()`.

## Text input — use `fill`

`fill` handles all three text input shapes. Pass selector (CSS or `@e` ref) + value:

| Target | What `fill` does | Returned `mode` |
|--------|------|------|
| `<input>` / `<textarea>` | Sets `.value` via native setter, fires `input`/`change`. | `"value"` |
| `[contenteditable]` (ProseMirror / TipTap / Lexical / Slate / Quill etc.) | Focuses, selects all existing content, calls `document.execCommand('insertText', ...)` which fires `beforeinput`/`input` with `inputType:'insertText'` and `data:value`. | `"contenteditable"` |
| Other element | Best-effort `.value` + events. | `"value"` |

`fill` is **clear-and-insert**: existing content is replaced. For "append to existing text", read the current value via `evaluate`, concatenate, then `fill` with the result.

## Form submit / special keys

There's no separate "press Enter" tool. To submit a form, click the submit button directly (`click` on the @e ref or selector). To dispatch a key event programmatically (e.g. Escape to close a modal):

```bash
{"action":"evaluate","args":{"code":"document.activeElement.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}))"}}
```

## Save the current page as PDF

`save_as_pdf` renders the current page to PDF and returns the file path. All args optional:
- `paper_format`: `letter` (default) \| `a4` \| `legal` \| `a3` \| `tabloid`
- `landscape`: `false` (default)
- `scale`: `1.0` (default), range `[0.1, 2.0]`
- `print_background`: `true` (default) — keep background colors
- `path`: caller-supplied output path; if absent, daemon picks a default under OS temp dir using the page title as the filename

`path` semantics match `screenshot`: written verbatim, parent dirs auto-created, existing files overwritten.

Decoded PDF cap is 100 MB. Above that the daemon refuses; reduce `scale` or split the page.

## Known limitations

- **Sites that strictly check `event.isTrusted`** (some banking portals, captcha challenges) reject `fill` and `click` because both go through DOM-level synthetic events (`isTrusted=false`). This is a product boundary, not a bug — no automation primitive that runs on the user's machine without stealing OS focus can produce trusted events on these sites.
- **Cross-origin iframes**: `fill`, `click`, `evaluate`, and `snapshot` operate on the top frame. If a target element lives in a same-page iframe from a different origin (e.g. embedded sandbox demos), navigate to the iframe's URL directly instead.

## Versions

Daemon, extension, and this skill share a 1:1 version string. Read both via:

```bash
~/.kimi-webbridge/bin/kimi-webbridge status
# {"version":"<daemon>", "extension_version":"<extension>"}
```

If a tool returns an error containing **"Please update the Kimi WebBridge extension"**, the user's extension is older than this skill. Tell the user:

> 请更新 Kimi WebBridge 浏览器扩展后重试：https://kimi.com/features/webbridge

Don't retry the failed tool. Don't auto-switch skill versions based on `extension_version` — the pairing protocol isn't finalized.
