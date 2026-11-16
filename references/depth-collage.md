# mango — Depth without heavy 3D: the collage layer stack

When the artifact is editorial (monograph, lookbook, program, almanac) rather than product-hero, depth comes from layered flat graphics, not WebGL. This is a complete system on its own; the AURELIA build shipped both.

## The four layers (bottom → top)
1. **Ghost numeral / plate rule** — oversized `-webkit-text-stroke` numeral at 10–24rem, `z-index: 0`, `position: absolute`, pointer-events none. Must carry information (section index). One per major section, never adjacent.
2. **Illustration SVG** — technical cross-section, registration marks, exploded diagram. `drop-shadow()` for paper-thickness; width `clamp(11rem, 30vw, 19.5rem)`; `z-index: 4`.
3. **Rotating reticle / badge** — circular "EST · location · edition" textPath or aperture/crosshair reticle; `animation: rotor 34–40s linear infinite`; `z-index: 5–6`.
4. **Display type** — the headline sits at `z-index: 2` but `line__inner` at normal flow; collage layers may overlap the type's box as long as `pointer-events: none` and legibility holds (contrast ≥ 3:1 on the overlap region).

## Layer coefficients for pointer parallax
- Diagram: −14px/−10px (furthest visual, least movement)
- Reticle: +22/+18 (nearest)
- Badge: −26/−20 with slight rotate (nearest, largest swing)
Lerp factor 0.08; disable on `pointer: coarse` and reduced-motion.

## Scroll coupling
Scrub `rotate`/`y` on the same three layers with opposite directions (diagram down, badge up, reticle still) via ScrollTrigger `scrub: 0.7`. The type stays fixed to the document; only the collage drifts.

## SVG illustration craft rules
- viewBox around 340×190 for plates; stroke `#131310` at 1.2–2.2px; one accent stroke (vermilion class) for datum lines; fills ≤ 30% alpha so the paper reads through.
- Always include a hairline dashed frame inset by 6–8px; the dashed frame is the "registration" cue that separates illustration from decoration.
- Callout labels in mono at 8.5–9.5px with leader lines; never floating labels without a line.
- Dimension lines with arrowheads and centered caption (e.g., `124 mm · SECTION A–A`) — these carry *information*, satisfying the information-density rule.

## Failure modes
| Symptom | Fix |
|---|---|
| Collage covers body text on mobile | Media query: shrink widths, move badge above the fold line, set `display: none` on hint text |
| Rotating badge causes horizontal scroll | Parent `overflow: clip`; badge `position: absolute` with `right` offset, never `vw` bleed |
| Text unreadable where diagram overlaps | Raise fill alpha of diagram plate to 0.78–0.85; drop headline weight to 850–900 |
| SVG looks like clip-art | Double-stroke paths (outer dark, inner light); dashed inner frame; dimension arrows |
