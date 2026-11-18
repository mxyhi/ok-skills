# Build a CLI for a website

Read this when the user asks for a reusable CLI tool or script that automates a specific website. The CLI drives the user's real browser through the same daemon as the tools in SKILL.md, so it works with the sessions the user is already logged in to.

Work through the phases in order. `{platform}` below is a short name for the site — one lowercase word, no hyphens: it names the binary (`{platform}-cli`), the CLI's `session`, and in Go a package.

## Phase 1: Requirements

Establish the target URL and first features from the request. Ask only for missing scope you cannot infer. Follow the project's language; otherwise choose an available toolchain unless the user specified one. Inspect the site to determine login requirements. Add later features by repeating Phases 2–3.

## Phase 2: Site exploration

Before implementing a feature, follow [Site exploration](site-exploration.md) to establish its API request or DOM interaction in the user's browser session.

Proceed when reads are verified and each write has an observed request/interaction with a verification plan. A write that cannot be tested within the user's authorized scope must be reported as unverified, not executed merely to finish exploration.

## Phase 3: Implement

Build in this order:

1. **Project scaffold** — [Go layout](go-layout.md) for Go. In any other language use the HTTP request/reply contract in [SKILL.md](../../SKILL.md#call-format).
2. **`login-status` command** — if the site requires login; see [Login handling](login-handling.md)
3. **Read commands** — no side effects
4. **Write commands** — after the reads work

Verify each command's help, then run read commands against observed data:

```bash
{platform}-cli {command} --help          # must work
{platform}-cli {read-command} [args]     # must print {"ok": true, "data": ...}
```

Test writes only on disposable fixtures within explicitly authorized test scope, and verify their effects. Use mocks or local argument validation for write error paths; an arbitrary wrong ID on a live site is not a safe test fixture. Check an unreachable `--daemon-url` too: errors must print `{"ok": false, ...}` and exit non-zero.

**CLI contract (every language):**

- `--help` / `-h` works on every command
- All output is `{"ok": true, "data": ...}` or `{"ok": false, "error": {"code": "...", "message": "..."}}`
- Non-zero exit code on error
- A `--daemon-url` flag on the root command, defaulting to `http://127.0.0.1:10086`. The daemon can listen elsewhere (see "If a tool call fails" in SKILL.md), so the caller must be able to say where.
- One fixed `session` name for the whole CLI, sent on every daemon request. A CLI outlives any single task, so the name is `{platform}`, not a task name.
- Each command reuses the CLI's tab, so runs don't pile up tabs: `find_tab` with the site's URL first, and `navigate` with `newTab: true` only when no tab matches; propagate connection and other errors. `find_tab` matches by host, so when a command needs a specific page, `navigate` the found tab there (without `newTab`).

## Phase 4: Companion skill

Once the CLI works, use the [companion skill template](companion-skill-template.md) to write `skill/{platform}-cli/SKILL.md` in the CLI project. Document any unverified commands explicitly.

Install it into the host's skill directory if the user requested installation; otherwise offer installation after delivering the CLI.
