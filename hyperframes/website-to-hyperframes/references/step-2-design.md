# Step 2: Write DESIGN.md

DESIGN.md is a **brand cheat sheet** for the captured website. It encodes the visual identity so you can reference exact colors, fonts, and patterns while writing the storyboard and compositions.

DESIGN.md is NOT the creative plan. The STORYBOARD (Step 4) drives creative direction. DESIGN.md is a reference you consult, not a document you follow slavishly.

## The 6 Sections

### `## Overview`

3-4 sentences. Describe the visual identity factually: layout patterns (bento grid, logo wall, hero section), color strategy, typography tone, overall feel. Be precise, not poetic.

### `## Colors`

5-10 key colors with HEX values from tokens.json and their roles:

```
- **Primary Surface**: `#020204` — deep black background
- **Primary Content**: `#FFFFFF` — high-purity white for text and borders
- **Accent Warm**: `#FB923C` — orange for CTAs and highlights
```

Include semantic colors if the site uses color to differentiate product areas.

### `## Typography`

Font families with weights, roles, and any distinctive usage:

```
- **Serif**: Cormorant Garamond (Italic). Major headings, brand identity.
- **Monospace**: Geist Mono. Subheaders, labels, terminal readouts. High tracking (0.1-0.3em), all-caps.
- **Sans-Serif**: Inter. Body copy, interface elements. Small sizes (9-14px).
```

Include sizing hierarchy if notable (hero: 64px, section: 32px, body: 16px).

### `## Elevation`

One paragraph on depth strategy: Does the site use borders, shadows, glassmorphism, or flat color shifts? Reference specific patterns (e.g., "1px borders at white/10 opacity" or "layered backdrop-blur with thin borders").

### `## Components`

Name every notable UI component you see in the screenshot. Be specific:

- "Cinematic Accordion" not "Cards"
- "Logo Marquee" not "Scrolling section"
- "Glass Cards with grain overlay" not "Content containers"

For each, note the distinctive visual treatment (border-radius, spacing, hover behavior).

### `## Do's and Don'ts`

3-5 rules each, derived from what the site actually does and doesn't do:

```
### Do's
- Use thin subtle borders (white/10) to separate sections
- Keep imagery desaturated with dark gradients for text readability

### Don'ts
- Do not use bright solid background colors — stay in "The Void"
- Do not use standard drop shadows — use radial glow or bloom effects
- Do not use sharp high-speed animations — all motion should be fluid
```

## Rules

- Use **exact HEX values** from tokens.json. Do not approximate.
- Name components by what you see in the screenshot, not generic terms.
- Keep it under 100 lines. This is a cheat sheet, not a design system document.
- No "Style Prompt" section — the storyboard handles creative direction.
- No "Assets" section — `asset-descriptions.md` already covers this.
- No "Motion" section — the storyboard specifies motion per-beat.

## Example

This is a real DESIGN.md from a production capture (Soulscape 2026):

```markdown
# Design System

## Overview

Soulscape 2026 is a cinematic, "high-signal" digital experience that positions itself as the vanguard of AI filmmaking. The visual personality is dark, technical, and premium, characterized by high-contrast "Flare" on "Void" (white on black) aesthetics. The layout is dense but organized, utilizing heavy horizontal layering and border-defined sections to evoke a wide-screen cinematic feel. Motion is a core tenet, with atmospheric grain overlays, shifting light leaks, and slow-moving marquees creating constant, breathing texture.

## Colors

- **Primary Surface**: `#020204` (Void) - Deep black for the entire background.
- **Primary Content**: `#FFFFFF` (Flare) - High-purity white for typography and primary borders.
- **Accent 1 (Warm)**: `#FB923C` - Orange for industry/executive tiers and primary CTAs.
- **Accent 2 (Cool)**: `#60A5FA` - Blue for creative voices and summit-focused components.
- **Subtle Overlays**: `rgba(255, 255, 255, 0.02)` to `0.08` for glass backgrounds.

## Typography

- **Serif**: Cormorant Garamond (Italic). Major headings and "Soul" brand identity. Classical cinematic contrast.
- **Monospace**: Geist Mono. Subheaders, labels, terminal readouts. High tracking (0.1-0.3em), all-caps.
- **Sans-Serif**: Inter. Body copy and interface elements. Small sizes (9-14px).

## Elevation

- **Glassmorphism**: Components use backdrop-filter blur(10px) with thin borders (1px solid rgba(255, 255, 255, 0.08)).
- **Layering**: Depth via fixed global grain-overlay and localized light-leak gradients rather than box-shadows.
- **Interaction**: Hover triggers subtle translateY(-5px) and increased border opacity.

## Components

- **Cinematic Accordion**: Expanding horizontal/vertical card system where panels expand from compressed state to reveal full-bleed imagery and large serif typography.
- **HUD Explorer**: Floating mobile navigation trigger styled as a "Lens" with pulsing glow and terminal readouts.
- **Slow Marquees**: Continuous horizontal tickers for partner logos and veteran listings.
- **Glass Cards**: Content containers with subtle gradients, rounded corners (2.5rem), and high-contrast iconography.
- **Grain & Flicker**: Global CSS noise filters and holographic flicker animations on UI labels.

## Do's and Don'ts

### Do's

- Use thin subtle borders (white/10) to separate sections rather than solid color changes.
- Maintain high letter-spacing on all Geist Mono labels.
- Use serif italics for emotional or visionary statements.
- Keep imagery desaturated or stylized with dark gradients for readability.

### Don'ts

- Do not use bright solid background colors — the page must remain in "The Void."
- Do not use standard drop shadows — use radial glow or bloom effects instead.
- Do not use sharp high-speed animations — all motion should be fluid and breathing.
```
