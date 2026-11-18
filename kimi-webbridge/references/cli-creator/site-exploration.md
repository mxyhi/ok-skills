# Site Exploration Protocol

For each feature, establish the API request or DOM interaction before implementing its command. Verify reads in the browser; verify writes only within an explicitly authorized disposable test scope.

Every step uses [SKILL.md's call format](../../SKILL.md#call-format). Use one task session for this exploration; the generated CLI uses its own fixed platform session as described in the workflow.

## Steps

1. **`navigate`** `{url: "<target-url>", newTab: true}` — open the page the feature lives on.

2. **`snapshot`** — read the page structure. If the feature is purely DOM-based (the text is already on the page, or the action is one visible button), note the `@e` refs and go to step 7.

3. **`network`** `{cmd: "start"}` — begin capturing.

4. **Trigger the feature** so the page makes its API call — reload the same tab, scroll, or click. Capture stays on that tab; opening a new one will not capture its traffic. For writes (posting, liking), capture an already-authorized action or an explicitly authorized test. The request to build a CLI alone does not authorize real posts or messages.

5. **`network`** `{cmd: "list", filter: "<url-substring>"}` — find the XHR/GraphQL/REST call behind the feature; skip static assets. Then, **while capture is still on**:
   - **`network`** `{cmd: "detail", requestId: "<id>"}` — full URL with query params, method, status, `requestHeaders`, `requestBody`, and the response `body`. Note the response's field names, nesting, and any pagination cursor. In `requestHeaders`, note the ones the page set itself — `authorization`, a CSRF token, a language header, other `x-…` headers: the replay in step 7 has to send them.

   The response body can only be fetched while capture is on.

6. **`network`** `{cmd: "stop"}`

7. **Verify the read** with `evaluate` inside the page. For a captured write, record its request and observed result; do not replay it unless another execution is explicitly within the authorized test scope. Same-origin fetch attaches cookies; a cross-origin API may need `credentials: "include"` and must allow credentialed CORS:

   ```js
   (async () => {
     const r = await fetch("<api-path>", {
       method: "POST",
       headers: {"Content-Type": "application/json", <headers the page set, from step 5>},
       body: JSON.stringify(<request-body>),
     });
     return JSON.stringify({status: r.status, body: await r.text()});
   })()
   ```

   `evaluate` runs the code as a plain script, so `await` needs the async wrapper.

   For a DOM-based feature from step 2, verify the content or interaction against the snapshot. Use current refs at runtime rather than hardcoding exploration-time refs. The same write-test boundary applies to clicks.

   **Compare the result with the response body captured in step 5** — same items, same count. A replay can return 200 with different data (another language, a shorter list) when it lacks a header the page sends, so "looks plausible" is not the test.

   If a read fails or differs, compare status, payload, query, headers and login state before retrying; do not assume a missing header. The browser manages `cookie`, `user-agent`, `accept-encoding` and `sec-…`. Read any required token from its observed page-side source inside the same `evaluate` call; do not hardcode it in the CLI or copy its value into findings.

## Exploration summary

Write the findings down in the CLI project before writing code:

```
Feature: [home feed / search / post / ...]
Request: [GET/POST] <full URL>   (or "DOM read")
Auth: [cookies only / token header from <where>]
Request params: [query, cursor, limit]
Response shape: {data: [{id, text, author: {name}, created_at}], next_cursor}
Implementation: [verified read JS or observed write request/DOM interaction]
Verification: [observed result, or unverified write + proposed test scope]
```
