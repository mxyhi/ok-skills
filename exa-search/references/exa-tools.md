# Exa MCP Tools And Parameters

Snapshot checked against:

- Hosted endpoint: `https://mcp.exa.ai/mcp`
- Official repo: `exa-labs/exa-mcp-server@253322139071596121f8ef35532443dba8b67017`
- npm package: `exa-mcp-server@3.2.1`
- Date checked: 2026-06-23

## Base URL

- Base: `https://mcp.exa.ai/mcp`
- Select tools: `?tools=tool_a,tool_b,...`
- API key: `?exaApiKey=YOUR_EXA_API_KEY`, `Authorization: Bearer ...`, or `EXA_API_KEY` for local npm.
- Anonymous hosted use works but has rate limits and may not register API-key-only tools.
- Streamable HTTP flow: `initialize`, `notifications/initialized`, then `tools/list` or `tools/call` with the returned `Mcp-Session-Id`.
- Hosted responses usually use `text/event-stream`; extract JSON from `data:` lines before parsing.
- Use `curl` through small shell helpers. Repeating raw header/body plumbing at every call site is noisy.

## Enabled By Default

| Tool | Purpose | Parameters |
| --- | --- | --- |
| `web_search_exa` | General web search with clean highlights/text | `query` required; `numResults` optional, default `10` |
| `web_fetch_exa` | Fetch full content for known URLs | `urls` required; `maxCharacters` optional, default `3000` |

## Off By Default

| Tool | Purpose | Parameters |
| --- | --- | --- |
| `web_search_advanced_exa` | Advanced search with filters and content controls | See detailed schema below |

## Deprecated Tools

| Tool | Use Instead | Current Parameters |
| --- | --- | --- |
| `get_code_context_exa` | `web_search_exa` | `query`, `numResults` |
| `company_research_exa` | `web_search_advanced_exa` with `category:"company"` | `companyName`, `numResults`; default `3` |
| `people_search_exa` | `web_search_advanced_exa` with `category:"people"` | `query`, `numResults`; default `5` |
| `crawling_exa` | `web_fetch_exa` | `urls`, `maxCharacters` |
| `linkedin_search_exa` | `web_search_advanced_exa` with `category:"people"` | `query`, `numResults` |
| `deep_search_exa` | `web_search_advanced_exa` | May require user-provided API key; not always registered anonymously |
| `deep_researcher_start` | Exa Research API | `instructions`, `model`, `outputSchema` |
| `deep_researcher_check` | Exa Research API | `researchId` |

## `web_search_advanced_exa` Schema

Required:

- `query`: string

Optional:

- Search tuning: `numResults`, `type` (`auto` | `fast` | `instant`)
- Category: `company`, `research paper`, `news`, `pdf`, `github`, `personal site`, `people`, `financial report`
- Domain filters: `includeDomains`, `excludeDomains`
- Date filters: `startPublishedDate`, `endPublishedDate`, `startCrawlDate`, `endCrawlDate`
- Text filters: `includeText`, `excludeText`
- Geo/safety: `userLocation`, `moderation`
- Query expansion: `additionalQueries`
- Content: `textMaxCharacters`, `contextMaxCharacters`, `enableSummary`, `summaryQuery`, `enableHighlights`, `highlightsMaxCharacters`, `highlightsNumSentences`, `highlightsPerUrl`, `highlightsQuery`
- Freshness/fetch: `maxAgeHours`, `livecrawlTimeout`
- Subpages: `subpages`, `subpageTarget`

Deprecated/compat details:

- `highlightsNumSentences` and `highlightsPerUrl` are deprecated in official source comments; prefer `highlightsMaxCharacters`.
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

## Direct HTTP Smoke Result

No-proxy direct HTTP passed on 2026-06-23:

- `initialize`: protocol `2025-06-18`, server `exa-search-server`, version `3.2.1`
- `tools/list`: returned `web_search_exa`, `web_search_advanced_exa`, `web_fetch_exa`
- `tools/call web_search_exa`: returned `isError=false` and formatted search text
- `tools/call web_search_advanced_exa`: returned `isError=false` and JSON text
- `tools/call web_fetch_exa`: returned `isError=false` and fetched page text
