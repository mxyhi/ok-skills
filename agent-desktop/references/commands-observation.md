# Observation Commands

Commands that read UI state and never change it. Run `agent-desktop <command> --help` for flags.

## snapshot

Captures the accessibility tree as JSON. Interactive elements get qualified refs (`@s8f3k2p9:e1`) that embed the snapshot id. A bare `@eN` fails with `INVALID_ARGS`.

```bash
agent-desktop snapshot --app "System Settings" -i --compact
agent-desktop snapshot --app "App" --skeleton -i --compact
agent-desktop snapshot --root @s8f3k2p9:e3 -i --compact
agent-desktop snapshot --app "App" --surface menu -i
agent-desktop snapshot --app "App" --window-id w-1234 -i
```

Output shape:

```json
{ "ok": true, "command": "snapshot",
  "data": { "app": "System Settings", "window": { "id": "w-4521", "title": "General" },
    "ref_count": 14, "snapshot_id": "s8f3k2p9", "complete": true,
    "tree": { "role": "window", "name": "General", "children": [
      { "ref_id": "@s8f3k2p9:e1", "role": "button", "name": "About", "states": ["focused"] } ] } } }
```

On macOS, `menu` and `menubar` snapshots are application-owned. They need no document window, include `data.app`, and omit `data.window`. A process-owned snapshot of a background app with no window also omits `data.window`. If you pass `--window-id` for an application-owned menu, it selects the app that owns the surface.

Each ref names the snapshot that owns it, so a ref keeps resolving against its own snapshot when you interleave several apps or windows.

Choose the scope:

- `-i --compact` keeps interactive elements only and drops empty wrappers. Use both by default.
- `-i` keeps interactive nodes and cut containers, so a row's static-text label is dropped. To tie a repeated button to its row, drill that row's container with `--root` and leave out `-i`. On Windows and Linux this identifies the row but a button repeated across rows stays a twin, so its ref is refused.
- `--skeleton` clamps depth to 3 and adds `children_count` to cut containers. Each cut branch exposes its deepest safely resolvable drill target, or its nearest resolvable ancestor when the boundary has no stable identity.
- `--root <REF>` starts from a ref found earlier. Re-drilling a root replaces the refs from that root's previous drill, and those of any drill made under it. Refs outside the drilled subtree keep working, skeleton refs inside it are replaced, and the new refs join the same snapshot id. A drill inherits the whole-window identity count of its snapshot, so its refs resolve like the skeleton's. `--root` cannot combine with `--surface` or `--wait-for`.
- `--max-depth` (default 10) limits depth. Reach deeper subtrees with `--root`.
- Use `--include-bounds` only when you need coordinates.
- With `--app` and no `--window-id`, `snapshot` and `find` take the app's only visible window, else its only focused window, and answer `AMBIGUOUS_TARGET` with the candidates when neither settles it. Pass `--window-id` when an app has several windows.
- On macOS, `menu` and `menubar` are application-owned and skip window selection. If you pass `--window-id`, it selects the owning app for that surface.

### Partial trees

`data.complete` is on every snapshot. When the observation budget runs out, the command still succeeds with `"complete": false`, `"truncated": true`, `"nodes_observed"`, and the tree it saw. Each node with cut descendants carries `"subtree_truncated": true`. Read `complete`; do not wait for a `TIMEOUT`. Raise `--timeout-ms` (default 3000) or drill with `--root` to finish the tree. A `--root` drill is all or nothing: an incomplete read returns `TIMEOUT`.

`"identity_unproven": true` means the snapshot could not read the whole window in time to prove its refs. On Windows and Linux, and on macOS for an element with no address, those refs fail with `identity_not_unique`, so retake the snapshot with a larger `--timeout-ms` before acting.

A cold Chromium or Electron app can take 10 to 25 seconds to expose its web tree. If a fresh snapshot comes back thin, raise `--timeout-ms` and snapshot again.

### Which refs exist

An element gets a ref when its role is interactive or it advertises a primary action. `scrollarea` and `disclosure` get refs because `scroll`, `expand` and `collapse` need them. Static text and inert containers stay in the tree without refs. Web content advertises focus, right-click and scroll-to on almost every node, so those alone do not earn a ref. `find` returns `bounds` for such matches. Drive them with `--xy` (right-click, hover, drag) or scroll the container.

### Ref re-identification

A command re-identifies the element from the ref before it acts. On macOS, a ref carries the element's native address when available, so identical twins each keep their ref. On Windows and Linux, and on macOS when an element has no address, a ref resolves only when a complete read proved it was the only element in the window with its role, native id, name and description, and exactly one live element still matches. A skeleton, depth-limited or drilled capture counts against the whole window, so a shallow tree proves the same thing a full one does. Values and bounds never count as identity.

- `STALE_REF`, `details.kind: saved_ref_absent`: no live element matches the stored identity. Take a fresh snapshot. On macOS `retained_object_stale` means the recorded address is dead or no longer matches.
- `AMBIGUOUS_TARGET`, `details.kind: saved_ref_ambiguous`: an identical element appeared, so two live elements match. `identity_not_unique`: the ref was not proven unique at capture, so nothing was searched. That is an identical twin, which every snapshot refuses again, or a window the snapshot could not read whole in time, which a new snapshot with a larger `--timeout-ms` fixes.
- `TIMEOUT`, `details.kind: resolution_identity_unknown`: a live read did not answer, so identity is unproven. Nothing was sent; retry.

Off macOS, identical twins have no ref path: only `--headed mouse-click --xy X,Y` can choose one. It takes the foreground, and a Linux Wayland session refuses it.

### Surfaces

Surfaces include `menu`, `menubar`, `sheet`, `popover`, `alert`, `focused`, and OS shell kinds supported on each platform. On macOS, `menu` and `menubar` are application-owned. A kind this OS does not have returns `INVALID_ARGS` with the supported list in `details`; an adapter with no supported surfaces returns `PLATFORM_NOT_SUPPORTED`. A shell surface needs no `--app`, except that macOS `menu-bar-extras` with `--app` reads that app's own status item. A closed shell surface returns `WINDOW_NOT_FOUND`; a complete lookup of an absent macOS menu returns `ELEMENT_NOT_FOUND` with `details.kind: "surface_absent"`. Raise a shell surface with `open-system-surface`.

Use a surface snapshot for dialogs and menus, not a window snapshot. To reach one item inside an overlay, use `find --surface` instead of a full dump.

## find

Searches by role, name, value, text, description or native id. Use it first when you know the target.

```bash
agent-desktop find --app "App" --role button --name "OK" --exact
agent-desktop find --root @s8f3k2p9:e4 --role textfield --first
agent-desktop find --app "App" --surface menubar --name "Save" --exact --first
agent-desktop find --app "App" --role button --count
```

- Scope before you widen. `--root` searches one ref's subtree. `--surface` searches an overlay. Both cost a few hundred bytes instead of a full dump. They cannot combine.
- `--name` and `--text` match fuzzily. Add `--exact` for case-insensitive equality. Use `--limit 2` before a mutation when you need to know the match is unique.
- `--text` also matches ancestors whose subtree text contains the text. Use `--name` to match the node itself.
- `--role` is case-insensitive; `textarea`, `textbox` and `searchfield` fold to `textfield`. When a role filter matches nothing, `data.roles_present` lists the roles in the searched tree. Use it to tell a wrong role name from an empty screen.
- Unnamed elements omit `name`. Their content is in `value`, so search it with `--value`.
- A large tree, such as a file dialog, can pass the 5000 ms default `--timeout-ms`. Raise it or narrow the search. A timeout here does not mean the app hangs.

Every non-count response returns the `snapshot_id` that owns its refs:

```json
{ "data": { "snapshot_id": "s8f3k2p9",
  "matches": [ { "ref_id": "@s8f3k2p9:e5", "role": "button", "name": "OK", "states": ["enabled"] } ] } }
```

A match without `ref_id` is a context match: readable text with no action target. It carries `bounds` when the platform reports them. A match with a `ref_id` never carries `bounds`; read them with `get --property bounds`.

## get

Reads one property of a ref: `text` (default), `value`, `title`, `bounds`, `role`, `states`.

- `title` is the accessible name. It answers "what does this button say".
- `text` is what a person reads. It is the content for `textfield`, `combobox`, `listbox`, `datefield` and `timefield`, and the name everywhere else. If the preferred half is empty, the other half answers. A checkbox answers its label, not `1`.
- `value` is the raw value regardless of role (text, slider position).
- `text`, `value`, `bounds` and `states` read live state when the adapter can. A missing live value or bounds returns `null`. When an optional live read is unavailable, `get` can fall back to the saved ref entry's value, name, bounds or states.
- Only `bounds` reports whether it is live, in `data.live`. When it is `false`, the rectangle came from the snapshot and may be out of date. Check it before you pass bounds to `mouse-click`.

## is

Checks one boolean: `visible` (default), `enabled`, `checked`, `focused`, `expanded`, `selected`. Output: `{ "ref", "property", "result" }`. For `enabled`, an unknown native value returns `result: false` with `applicable: false`. That means unknown, not disabled.

## screenshot

```bash
agent-desktop screenshot --app "Finder" out.png
agent-desktop screenshot --screen 0 display.png
```

With no path, the PNG returns as base64 in `data`. `--screen` takes a display index from `list-displays`; `0` is the primary display. A screenshot is evidence for you, not proof that an action worked. Permission denial returns `PERM_DENIED` (see the platform skill).

## list-displays

Lists displays as `{ id, bounds, is_primary, scale }`, primary first. Use the array index, not `id`, with `screenshot --screen`.

## list-surfaces

```bash
agent-desktop list-surfaces --app "Finder"
```

Lists the overlay surfaces an app presents now, the values `snapshot --surface` accepts. Shell surfaces belong to the OS and never appear here. If a window entry carries `"unclassified": ["sheet"]` or `["menu"]`, the check could not read that window (often a busy app). Treat the missing entry as unknown, not absent.

## open-system-surface

```bash
agent-desktop --headed open-system-surface --surface action-center
```

Raises an OS shell surface. On Windows and Linux it returns the window it presents, in the `w-<id>` form that `list-windows` uses; on macOS `data` is only `{"surface": "dock"}` and `window` is left out, because no window owns these surfaces. It takes the foreground, so on Windows and Linux strict headless is refused with `POLICY_DENIED`; pass `--headed`. On macOS, `dock` and `menu-bar-extras` are always on screen, so they return headless with no `--headed`. An already-present surface returns without being raised again. A kind the OS does not expose returns `INVALID_ARGS` naming the kinds to use instead. `start-menu` is a Windows kind and `action-center` exists on Windows and Linux (GNOME); neither is a macOS kind. On macOS use `dock` or `menu-bar-extras`, and open Control Center or Notification Center by clicking its `menu-bar-extras` item. See the platform skill for the kinds.

## Chromium and Electron apps

The accessibility path is the default. It is the only path for an app that is already running and for native menus, dialogs and windows. For the web contents of an app you can launch fresh, `launch --cdp` plus a CDP client is faster than a skeleton walk. See `commands-system.md`.
