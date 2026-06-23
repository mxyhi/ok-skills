---
name: exa-search
description: Use Exa MCP for current web, code/docs, company, people, and page-fetch research. Prefer current hosted tool schemas and note deprecated tools.
---

# Exa MCP Search

Use this skill when online search, page fetch, code/docs lookup, company research, people research, or Exa MCP parameter checks are needed.

## Current Source Of Truth

- Hosted MCP endpoint: `https://mcp.exa.ai/mcp`
- Official source: `exa-labs/exa-mcp-server@253322139071596121f8ef35532443dba8b67017`
- Current npm package checked: `exa-mcp-server@3.2.1`; verified tarball SHA-256 `675688dffcd746b8bb6ac7f077b64b7382c4a305f948d44ba526e67be50396df`
- Tool schemas can change. Before adding new parameters, verify with `tools/list` through a normal HTTP client.

Direct MCP HTTP is the required invocation model for this skill. `curl` is fine, but keep the session and SSE parsing in small shell helpers instead of repeating low-level flags at every call site.

## Tool Choice

| Need | Prefer | Notes |
| --- | --- | --- |
| General current web search | `web_search_exa` | Simple search. Only `query` and `numResults`. |
| Filtered search, dates, domains, categories, summaries, highlights, subpages | `web_search_advanced_exa` | Enable explicitly in `tools=`. Use this for company/people/papers/news filters. |
| Read known URLs fully | `web_fetch_exa` | Use after search when highlights are insufficient. |
| Code examples/docs | `web_search_exa` | `get_code_context_exa` still exists but is deprecated. |
| Company research | `web_search_advanced_exa` with `category:"company"` | `company_research_exa` still exists but is deprecated. |
| People/profiles | `web_search_advanced_exa` with `category:"people"` | `people_search_exa` still exists but is deprecated. |

## Core Parameters

### `web_search_exa`

- `query` required: semantically rich natural-language query. Can include `category:company` or `category:people`.
- `numResults` optional: default `10`.
- No `type`, `livecrawl`, `contextMaxCharacters`, or `tokensNum` on current hosted schema.

```json
{"query":"latest AI safety research June 2026","numResults":10}
```

### `web_search_advanced_exa`

- `query` required.
- Common optional filters: `numResults`, `type` (`auto` | `fast` | `instant`), `category`, `includeDomains`, `excludeDomains`, `startPublishedDate`, `endPublishedDate`, `startCrawlDate`, `endCrawlDate`, `includeText`, `excludeText`, `userLocation`, `moderation`, `additionalQueries`.
- Content controls: `textMaxCharacters`, `contextMaxCharacters`, `enableSummary`, `summaryQuery`, `enableHighlights`, `highlightsMaxCharacters`, `highlightsQuery`, `maxAgeHours`, `livecrawlTimeout`, `subpages`, `subpageTarget`.
- Categories include `company`, `research paper`, `news`, `pdf`, `github`, `personal site`, `people`, `financial report`.

```json
{
  "query":"Anthropic funding valuation 2026",
  "category":"news",
  "includeDomains":["techcrunch.com","bloomberg.com"],
  "startPublishedDate":"2026-01-01",
  "numResults":10,
  "type":"auto",
  "enableHighlights":true
}
```

### `web_fetch_exa`

- `urls` required: array of URLs. Batch multiple URLs in one call.
- `maxCharacters` optional: default `3000`.

```json
{"urls":["https://docs.exa.ai/reference"],"maxCharacters":5000}
```

### Deprecated But Still Available

- `get_code_context_exa`: use `web_search_exa` instead. Current schema is `query`, `numResults`; old `tokensNum` is obsolete.
- `company_research_exa`: use `web_search_advanced_exa` with `category:"company"` instead. Schema is `companyName`, `numResults`; default `3`.
- `people_search_exa`: use `web_search_advanced_exa` with `category:"people"` instead.
- `crawling_exa`: use `web_fetch_exa` instead.
- `deep_search_exa`: use `web_search_advanced_exa` instead; may require user-provided Exa API key and may not register on anonymous hosted MCP.
- `deep_researcher_start` / `deep_researcher_check`: deprecated; use Exa Research API directly when needed.

## Curl Pattern

1. POST `initialize`; keep returned `Mcp-Session-Id` response header.
2. POST `notifications/initialized` with that header.
3. POST `tools/list` or `tools/call` with that header.
4. If response is `text/event-stream`, parse JSON from `data:` lines.

### Minimal Curl Helper

```bash
EXA_URL="https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,web_fetch_exa"
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

exa_init() {
  exa_rpc '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"exa-curl","version":"0.1.0"}}}' >/dev/null
  exa_rpc '{"jsonrpc":"2.0","method":"notifications/initialized"}' >/dev/null
}

exa_call() {
  local tool_name="$1"
  local arguments_json="$2"
  jq -nc --arg name "$tool_name" --argjson arguments "$arguments_json" \
    '{jsonrpc:"2.0",id:2,method:"tools/call",params:{name:$name,arguments:$arguments}}' |
    while IFS= read -r payload; do exa_rpc "$payload"; done
}

exa_init
exa_call web_search_exa '{"query":"latest AI safety research","numResults":5}'
```

Tool output format differs: `web_search_exa` returns formatted text, `web_search_advanced_exa` returns JSON text, and `web_fetch_exa` returns fetched page text.

## Research Practice

- For simple lookup, run one targeted `web_search_exa` call.
- For dated/current questions, calculate exact date ranges first and pass `startPublishedDate` / `endPublishedDate` through `web_search_advanced_exa`.
- For source-heavy tasks, fetch only the best URLs with `web_fetch_exa`; do not dump raw results into the final answer.
- For company/people/paper/news workflows, prefer `web_search_advanced_exa` categories rather than deprecated specialized tools.
- Mention source uncertainty when Exa returns sparse, conflicting, or old results.

## References

- Tool fields: `references/exa-tools.md`
