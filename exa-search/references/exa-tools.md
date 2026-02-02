# Exa MCP Tools and Parameters

## Base URL
- Base: `https://mcp.exa.ai/mcp`
- Select tools: `?tools=tool_a,tool_b,...`
- Pass API key: `?exaApiKey=YOUR_EXA_API_KEY` (takes precedence over server env var)

## Default enabled tools
- `web_search_exa`
- `get_code_context_exa`
- `company_research_exa`

## Full tool list
- `web_search_exa`
- `web_search_advanced_exa`
- `get_code_context_exa`
- `deep_search_exa`
- `crawling_exa`
- `company_research_exa`
- `people_search_exa`
- `deep_researcher_start`
- `deep_researcher_check`

## Notes
- You can use it without an API key, but free rate limits apply.
- Pass `exaApiKey` as a request parameter.
- Field names use camelCase (e.g., `numResults`, `contextMaxCharacters`).
