# Impeccable Skills Bundle

Vendored from `pbakaus/impeccable` at commit `00d485659af82982aef0328d0419c49a2716d123`.

## Source

- Website: `https://impeccable.style`
- Repository: `https://github.com/pbakaus/impeccable`
- Vendored bundle source: `.agents/skills/`

## Contents

- `impeccable/`: the flagship design skill, with built-in `craft`, `teach`, and `extract` flows plus `reference/` docs and `scripts/cleanup-deprecated.mjs`
- `adapt/`, `animate/`, `audit/`, `bolder/`, `clarify/`, `colorize/`, `critique/`, `delight/`, `distill/`, `harden/`, `layout/`, `optimize/`, `overdrive/`, `polish/`, `quieter/`, `shape/`, `typeset/`: command-style design skills synced from upstream

## Legal

- `LICENSE`: upstream Apache 2.0 license
- `NOTICE.md`: upstream attribution notice for the `impeccable` skill bundle

## Notes

- This directory is kept as a single upstream bundle to avoid expanding the repository root with many related skills.
- Skill contents are intentionally kept close to upstream for easier future syncs.
- The only local adaptation is the cleanup script path in `impeccable/SKILL.md`, so it resolves inside this repository's installed layout at `~/.agents/skills/ok-skills/`.
