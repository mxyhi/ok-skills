# Step 7: Validate & Deliver

## Lint + Validate

Run in sequence. Fix all errors before proceeding to the next command.

```bash
npx hyperframes lint
npx hyperframes validate
```

`lint` checks HTML structure statically — missing attributes, timeline registration, tween conflicts, CSS transform + GSAP conflicts (including inline styles).
`validate` loads the composition in headless Chrome and catches runtime JS errors, missing assets, and failed network requests.

## Visual Verification (snapshot)

After lint and validate pass, capture snapshot frames to SEE your own output:

```bash
npx hyperframes snapshot <project-dir> --at <beat-midpoints>
```

If the snapshot command isn't available, fall back to:

```bash
npx tsx packages/cli/src/cli.ts snapshot <project-dir> --at <beat-midpoints>
```

Calculate the midpoint of each beat from your STORYBOARD.md timings. For a 4-beat video with beats at 0-5.8s, 5.8-15.0s, 15.0-22.5s, 22.5-25.3s:

```bash
npx hyperframes snapshot <project-dir> --at 2.9,10.4,18.7,23.9
```

This renders one frame per beat at the moment when content is most visible. Use timestamps where the most content is on screen — usually 60-70% into each beat, after entrances finish but before exits start.

**View every snapshot image carefully.** Don't glance and move on. For each frame, check:

**Visibility:**

- Is there visible content? All-white or all-black frames mean compositions aren't rendering.
- Can you read ALL text? White text on white/light background is invisible. Dark text on dark background is invisible. Every text element needs contrast against what's directly behind it.
- Are images and assets showing? Empty space where an image should be means a path issue or missing file.

**Positioning and layout:**

- Do background images fill the entire frame? If an image only covers half the screen, the `object-fit`, `width`, `height`, or position values are wrong.
- Are elements where the storyboard says they should be? Compare the snapshot to the beat description.
- Is there too much empty/dead space? If more than 40% of the frame is a flat solid color with nothing on it, the composition is sparse.
- Are elements overlapping incorrectly? Text over text, or content bleeding off the edges?

**Visual quality:**

- Are overlays too heavy? If a background image is barely visible through a dark overlay, reduce the overlay opacity.
- Is the visual hierarchy clear? One dominant element per frame, supporting elements secondary.
- Do the colors match DESIGN.md? Check actual rendered colors against what was planned.

**Code vs. rendered verification:**

- For each beat, check: does the snapshot show the assets you referenced in the HTML? If a composition has `<img src="...wave.png">` but the snapshot shows no wave — the image isn't loading, the path is wrong, or it's hidden behind another element.
- If a snapshot shows nothing at a timestamp, try a slightly different time (1-2 seconds later). Compositions may still be in entrance animations.
- The snapshot command is fast — run it multiple times at different timestamps if needed.

If any frame has issues, go back to Step 6 and fix that composition before proceeding.

## Preview

```bash
npx hyperframes preview
```

Open the studio in a browser. Scrub through every beat.

## Create HANDOFF.md

Write a `HANDOFF.md` for multi-session continuity:

```markdown
# Handoff — [Project Name]

**Date:** [today]
**Preview:** `npx hyperframes preview`

## What's Built

| Beat | File                 | Dur  | Status | Notes |
| ---- | -------------------- | ---- | ------ | ----- |
| 1    | beat-1-hook.html     | 5.2s | Built  | ...   |
| 2    | beat-2-features.html | 6.8s | Built  | ...   |

## Audio

| Asset           | Status | Notes                                |
| --------------- | ------ | ------------------------------------ |
| narration.wav   | Done   | [provider], [voice name], [duration] |
| transcript.json | Done   | [word count] words, [duration]       |

## What Needs Work

- [any known issues, polish requests, missing SFX]

## Commands

npx hyperframes preview
npx hyperframes lint
npx hyperframes validate
npx hyperframes snapshot <project-dir> --at <beat-midpoints>
npx hyperframes render --output renders/final.mp4
```
