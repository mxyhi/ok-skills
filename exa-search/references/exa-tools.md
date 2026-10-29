# Exa MCP Tools And Parameters

Snapshot checked against:

- Hosted endpoint: `https://mcp.exa.ai/mcp`
- Official repo: `exa-labs/exa-mcp-server@55cc85c7305117aea538ea0b9dc7d19523be0c6a`
- npm package: `exa-mcp-server@3.4.2`
- npm tarball SHA-256: `a7d76442a45d809393eae6ec439ac4ebbbfa9f89e30789008069f8c5236b3f97`
- npm package `gitHead`: `f2bdda713e9368a8db8854929faf4fd277e5a1c9`
- Hosted MCP `serverInfo.version`: `3.5.0` (hosted `web_search_exa` adds required `objective`, not yet in official source or npm)
- Date checked: 2026-10-29

## Base URL

- Base: `https://mcp.exa.ai/mcp`
- Select tools: `?tools=tool_a,tool_b,...`
- API key: `?exaApiKey=YOUR_EXA_API_KEY`, `Authorization: Bearer ...`, or `EXA_API_KEY` for local npm.
- Anonymous hosted use works but has rate limits and may not register API-key-only tools.
- Streamable HTTP flow: `initialize`, `notifications/initialized`, then `tools/list` or `tools/call`. Include `Mcp-Session-Id` if initialization returned one; the hosted service may operate without it.
- Hosted responses usually use `text/event-stream`; extract JSON from `data:` lines before parsing.
- Use `curl` through small shell helpers. Repeating raw header/body plumbing at every call site is noisy.

## Enabled By Default

| Tool | Purpose | Parameters |
| --- | --- | --- |
| `web_search_exa` | General web search with clean highlights/text | `query` and `objective` required; `numResults` optional, default `10` |
| `web_fetch_exa` | Fetch full content for known URLs | `urls` required; `maxCharacters` optional, default `3000` |

## Off By Default

| Tool | Purpose | Parameters |
| --- | --- | --- |
| `web_search_advanced_exa` | Advanced search with filters and content controls | See detailed schema below |

Official source also registers `agent_run` for research-agent runs. Selecting it on the hosted endpoint requires OAuth or a user-provided API key; anonymous `tools/list` returned HTTP 401 on 2026-10-29. Fetch its authenticated schema before constructing a request. This snapshot did not execute an agent run.

## Deprecated Tools

| Tool | Use Instead | Current Parameters |
| --- | --- | --- |
| `get_code_context_exa` | `web_search_exa` | `query`, `numResults` |
| `company_research_exa` | `web_search_advanced_exa` with `category:"company"` | `companyName`, `numResults`; default `3` |
| `people_search_exa` | `web_search_advanced_exa` with `category:"people"` | `query`, `numResults`; default `5` |
| `crawling_exa` | `web_fetch_exa` | `urls`, `maxCharacters` |
| `linkedin_search_exa` | `web_search_advanced_exa` with `category:"people"` | `query`, `numResults` |
| `deep_search_exa` | `web_search_advanced_exa` | Requires OAuth or a user-provided API key on current hosted MCP when requested |
| `deep_researcher_start` | Exa Research API | `instructions`, `model`, `outputSchema` |
| `deep_researcher_check` | Exa Research API | `researchId` |

## `web_search_advanced_exa` Schema

Required:

- `query`: string

Optional:

- Search tuning: `numResults`, `type` (`auto` | `lite` | `fast` | `instant`)
- Category: `company`, `publication`, `news`, `pdf`, `github`, `personal site`, `people`, `financial report`
- Domain filters: `includeDomains`, `excludeDomains`
- Date filters: `startPublishedDate`, `endPublishedDate`, `startCrawlDate`, `endCrawlDate`
- Text filters: `includeText`, `excludeText`
- Geo/safety: `userLocation`, `moderation`
- Query expansion: `additionalQueries`
- Content: `textMaxCharacters`, `contextMaxCharacters`, `enableSummary`, `summaryQuery`, `enableHighlights`, `highlightsMaxCharacters`, `highlightsNumSentences`, `highlightsPerUrl`, `highlightsQuery`
- Freshness/fetch: `maxAgeHours`, `livecrawlTimeout`
- Subpages: `subpages`, `subpageTarget`

Deprecated/compat details:

- `auto` is the recommended default and accepts every parameter. `lite` serves cached content and supports only `query`, `numResults`, `category`, `includeDomains`, `excludeDomains`, `startPublishedDate`, `endPublishedDate`, `userLocation`, `moderation`, `textMaxCharacters`, and highlights parameters. Use `auto` for other controls, including summaries, crawl-date/text filters, additional queries, context output, freshness and subpages. `fast` and `instant` are legacy types; prefer `lite`, or `auto` when the required parameters exceed `lite` support.
- `highlightsNumSentences` and `highlightsPerUrl` are deprecated; the hosted schema explicitly says `highlightsPerUrl` is ignored. Prefer `highlightsMaxCharacters`.
- `livecrawl` is not a direct exposed parameter on current hosted `web_search_exa`; use advanced freshness controls (`maxAgeHours`, `livecrawlTimeout`) when needed.
- Old local docs mentioning `tokensNum` for `get_code_context_exa` are obsolete.

## Minimal MCP Schema Check

```bash
EXA_URL="https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,web_fetch_exa,get_code_context_exa,company_research_exa,people_search_exa"
EXA_SESSION_ID=""

exa_rpc() {
  local payload="$1"
  local session_header=()
  local response

  if [ -n "$EXA_SESSION_ID" ]; then
    session_header=(-H "Mcp-Session-Id: $EXA_SESSION_ID")
  fi

  response="$(curl -isS "$EXA_URL" \
    -H 'Content-Type: application/json' \
    -H 'Accept: application/json, text/event-stream' \
    "${session_header[@]}" \
    --data "$payload")"

  if [ -z "$EXA_SESSION_ID" ]; then
    EXA_SESSION_ID="$(printf '%s\n' "$response" | awk 'tolower($0) ~ /^mcp-session-id:/ { sub(/^[^:]+:[[:space:]]*/, ""); gsub(/\r/, ""); print; exit }')"
  fi

  printf '%s\n' "$response" | sed -n 's/^data: //p'
}

exa_rpc '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"exa-schema-check","version":"0.1.0"}}}' >/dev/null
exa_rpc '{"jsonrpc":"2.0","method":"notifications/initialized"}' >/dev/null
exa_rpc '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
```

Expected hosted anonymous tools from that request on 2026-06-23:

- `web_search_exa`
- `web_search_advanced_exa`
- `company_research_exa`
- `web_fetch_exa`
- `people_search_exa`
- `get_code_context_exa`

`deep_search_exa` was requested separately but did not register anonymously, matching official source behavior that requires a user-provided API key.

Rechecked on 2026-06-28 with `deep_search_exa` included in `tools=`:

- Returned HTTP 401 with `Authentication required. Use OAuth or provide an API key.`
- Without `deep_search_exa`, anonymous hosted MCP still returns `web_search_exa`, `web_search_advanced_exa`, `web_fetch_exa`, and requested deprecated tools.
- npm package `exa-mcp-server@3.2.1` confirms `deep_search_exa` only registers when a user-provided API key is present.
- `web_search_advanced_exa` still exposes deprecated `highlightsNumSentences` and `highlightsPerUrl`; prefer `highlightsMaxCharacters`.

Rechecked on 2026-07-06:

- Official repo `main` is `8823cbea80b6ec5999c6217cccd91660fe953b97`.
- npm latest remains `exa-mcp-server@3.2.1`, package `gitHead` remains `74438bc48ea9853e2e3e56f72535edc4f5c34bf6`, and tarball SHA-256 remains `675688dffcd746b8bb6ac7f077b64b7382c4a305f948d44ba526e67be50396df`.
- Anonymous hosted schema still returns `web_search_exa`, `web_search_advanced_exa`, `company_research_exa`, `web_fetch_exa`, `people_search_exa`, and `get_code_context_exa` with the same parameter surface.
- Requesting only `deep_search_exa` still returns HTTP 401 `Authentication required. Use OAuth or provide an API key.`

## Direct HTTP Smoke Result

No-proxy direct HTTP passed on 2026-06-23:

- `initialize`: protocol `2025-06-18`, server `exa-search-server`, version `3.2.1`
- `tools/list`: returned `web_search_exa`, `web_search_advanced_exa`, `web_fetch_exa`
- `tools/call web_search_exa`: returned `isError=false` and formatted search text
- `tools/call web_search_advanced_exa`: returned `isError=false` and JSON text
- `tools/call web_fetch_exa`: returned `isError=false` and fetched page text

Rechecked on 2026-07-15:
- Official repo `main` advanced to `8823cbea80b6ec5999c6217cccd91660fe953b97`.
- npm latest remains `exa-mcp-server@3.2.1`, package `gitHead` remains `74438bc48ea9853e2e3e56f72535edc4f5c34bf6`, and tarball SHA-256 remains `675688dffcd746b8bb6ac7f077b64b7382c4a305f948d44ba526e67be50396df`.
- Hosted `initialize` still returns `serverInfo.version=3.2.1`.
- No skill body/tool-choice change required beyond source SHA refresh.

Rechecked on 2026-07-23:
- Official repo `main` advanced to `0de23f94b7e8539192bdc2008c16592156ada870`.
- npm latest remains `exa-mcp-server@3.2.1`; package `gitHead` and tarball SHA-256 remain unchanged.
- Hosted advanced schema now uses category `publication` instead of `research paper` and exposes deprecated `highlightsNumSentences` / `highlightsPerUrl` compatibility fields.

Rechecked on 2026-08-15:
- Official repo `main` advanced to `e64c11f2d3b4400ffbda8ccdd9658a450cc9d270`.
- npm latest is `exa-mcp-server@3.4.0`; package `gitHead` is `a664592b5dd7c5598b70158c771dcc5c2a4fb2c1`; tarball SHA-256 is `cbc24567086756cde087eee8d8f617b7c423b1761e068e2b52e167b013e63f19`.
- Hosted `initialize` still returns `serverInfo.version=3.2.1`.
- Anonymous hosted `tools/list` still returns `web_search_exa`, `web_search_advanced_exa`, `company_research_exa`, `web_fetch_exa`, `people_search_exa`, and `get_code_context_exa` with the same parameter surface, including category `publication` and deprecated highlight compatibility fields.
- No skill body/tool-choice change required beyond source SHA and npm metadata refresh.

Rechecked on 2026-09-04:
- Official repo `main` is `15ffb50519e719dc791cdc750ce5ed1934c0a1ed`; npm latest is `exa-mcp-server@3.4.1` with the package metadata above.
- Hosted `initialize` still reports `serverInfo.version=3.2.1`.
- Anonymous `tools/list` returns all seven explicitly requested tools, including `crawling_exa`, with the same parameters, category `publication`, and deprecated highlight fields.
- No tool-choice or parameter change was needed.

Rechecked on 2026-10-09:
- Official repo `main` is `e9c3b0126a3373eb1aeaca162e84d0791ff4c7f7`; npm latest is `exa-mcp-server@3.4.2` with the package metadata above.
- Hosted `initialize` now reports `serverInfo.version=3.4.2`.
- Anonymous `tools/list` returns the same seven requested tools. Only `web_search_exa` changed: it adds `objective` (string, 1-4096 chars) and lists it as required. Official source `src/tools/webSearch.ts` and npm 3.4.2 still define only `query` and `numResults`.
- Anonymous `tools/call web_search_exa` succeeded both with and without `objective`; send it anyway because the hosted schema requires it.
- Requesting `deep_search_exa` still returns HTTP 401 `Authentication required. Use OAuth or provide an API key.`

Rechecked on 2026-10-18:
- Official repo `main` remains `e9c3b0126a3373eb1aeaca162e84d0791ff4c7f7`; npm latest remains `exa-mcp-server@3.4.2`, with the same `gitHead` and package integrity.
- Hosted `initialize` reports `serverInfo.version=3.5.0`. It returns no session header; anonymous `notifications/initialized` and `tools/list` succeed without one.
- All eight explicitly requested tools register, including `linkedin_search_exa`. The parameter names, types, and required fields of the seven previously checked tools are unchanged. Advanced highlight descriptions now mark `highlightsPerUrl` as ignored and remove the old character conversion claim for `highlightsNumSentences`.
- This check covers initialization and schema discovery; search, fetch, and authenticated research calls were not repeated.
