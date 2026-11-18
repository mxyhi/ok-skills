# Chromium and Electron Trees

Chromium-based apps (Electron or browser) are the most common source of a false
"the tree is empty" conclusion on Windows. The tree is real. The renderer builds
it after the first UIA client connects.

## Exposure Needs No Flag on Modern Chromium

Chromium 138 and later exposes a full UIA tree to any UIA client with no
`--force-renderer-accessibility` flag. The settled tree is the same with and
without the flag. Do not relaunch a running app to add accessibility flags.
Connect to what is there.

## First Contact Is Thin; Wait for Settle

The first read after connecting starts the renderer's accessibility build, so it
returns about a thirteenth of the settled tree. On a cold launch the settle
takes 10 to 25 seconds.

- Pass `--timeout-ms` to `snapshot` so its budget covers the settle. The
  adapter connects, lets the tree settle and re-walks within that budget.
- A grown tree is visible to a **fresh** read. The client that started the
  build can keep serving the shell it saw first. If one command still reports
  a thin tree after the settle, run a new snapshot instead of retrying in the
  same process.
- The renderer flag does not remove the need to settle. With it, first contact
  is a race that returns anything from a fraction of the tree to nearly all of it.

## A Thin Tree With Boundary Groups Is a Depth Effect, Not Settling

Chromium nests its controls under a long chain of unnamed pass-through groups,
so a settled tree can show no buttons, textfields or links at the default
`--max-depth 10`. The groups at the depth boundary carry `children_count` and
refs, so you can drill into them.

When a settled snapshot has refs but no operable controls, and its boundary
nodes carry `children_count`, do not wait longer or raise `--timeout-ms`. Raise
`--max-depth`, or drill into a boundary ref with `snapshot --root <ref>`.

## Covered Windows Hold First-Contact Counts Indefinitely

A Chromium window that other windows fully cover can keep its first-contact
node count through the whole settle. Do not park another window over the target
during launch and settle. If the count looks frozen at a small number, bring the
target to the foreground or minimize the covering windows, then snapshot again.

## WPF: Reading Too Early Binds the Wrong Provider

A UIA client that reads a WPF window before its automation peer exists binds the
generic HWND provider **permanently**. The window then reports
`ClassName HwndWrapper[...]` with zero children, and no in-process retry
recovers it. A read a few seconds after launch gets the real tree.

Take a new snapshot, so the adapter resolves from a new handle. Retrying the same
read cannot fix it. After you launch a WPF application, use
`wait --event window-opened` or a short `wait` before the first snapshot.

## Unnamed Web Content

A ref to web content with **no accessible name** is identified by its role plus
any AutomationId or description it carries, and resolves only if that
combination was unique in the window when you took it and still is. Bounds are
never identity. A ref to one of several unnamed elements that share role,
AutomationId and description returns `AMBIGUOUS_TARGET`; use headed coordinate
input from a parent's bounds, or a CDP client (`launch --cdp`).
