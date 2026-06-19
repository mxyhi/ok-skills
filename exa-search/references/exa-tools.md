# Exa MCP Tools And Parameters

Snapshot checked against:

- Hosted endpoint: `https://mcp.exa.ai/mcp`
- Official repo: `exa-labs/exa-mcp-server@9ea4ba3e67f87c462c3e06b192470e837ed9009e`
- npm package: `exa-mcp-server@3.2.1`
- Date checked: 2026-06-19

## Base URL

- Base: `https://mcp.exa.ai/mcp`
- Select tools: `?tools=tool_a,tool_b,...`
- API key: `?exaApiKey=YOUR_EXA_API_KEY`, `Authorization: Bearer ...`, or `EXA_API_KEY` for local npm.
- Anonymous hosted use works but has rate limits and may not register API-key-only tools.

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
mcporter list 'https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,web_fetch_exa,get_code_context_exa,company_research_exa,people_search_exa' --schema --json
```

Expected hosted anonymous tools from that request on 2026-06-19:

- `web_search_exa`
- `web_search_advanced_exa`
- `company_research_exa`
- `web_fetch_exa`
- `people_search_exa`
- `get_code_context_exa`

`deep_search_exa` was requested separately but did not register anonymously, matching official source behavior that requires a user-provided API key.
