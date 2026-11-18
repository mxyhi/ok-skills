# Go CLI layout

Use the existing project's conventions when available. For a standalone CLI, keep daemon transport separate from site-specific operations:

```text
{platform}-cli/
├── go.mod
├── main.go                     # run command; exit non-zero on error
├── browser/client.go           # daemon transport and tab selection
├── output/output.go            # JSON result/error envelopes
├── {platform}/                 # site operations derived from exploration
├── cmd/                        # command registration and argument validation
└── skill/{platform}-cli/SKILL.md
```

## Daemon client

- Store the base URL, fixed CLI session name and an HTTP client with a timeout long enough for browser navigation (for example, 90 seconds).
- POST `{"action": action, "session": session, "args": args}` to `/command`. Handle JSON encoding, transport and decoding errors. Decode the daemon's error envelope even on a non-2xx HTTP status; an unexpected response must remain an error.
- Decode `ok`, `data` and `error.code` / `error.message`. Return `data` only when `ok:true`; propagate failures rather than treating an empty result as success.
- Reuse the session's tab with `find_tab`. Open a new tab only for a no-match result; propagate connection and other errors. Matching is by host, so explicitly navigate when the operation requires a particular path.
- Wrap page-side JavaScript in an IIFE. Keep authenticated requests inside the browser and derive them from the exploration findings.

## Commands and output

Follow the [CLI contract](workflow.md#phase-3-implement): root `--daemon-url`, help on each command, JSON success/error output and non-zero error exits. Keep diagnostic logs on stderr so stdout remains parseable. Validate arguments before making a browser request.

Build with `go build`, check command help, and verify reads against the explored data. Follow the workflow's write-test restrictions; do not generate live writes merely to demonstrate the scaffold.
