# mango — Composition: layout from the artifact

Layout is not chosen from a pattern library; it is read off the artifact named in the direction card. Map the artifact's grammar onto page regions before writing HTML.

## Region grammar (universal slots, artifact-specific content)
| Slot | Monograph fill | Roast-log fill | Film-program fill |
|---|---|---|---|
| Masthead / header | Edition line + live bench clock (tabular) | Roastery mark + cup score ledger | Venue + season + ticket CTA |
| Hero | Object + headline + registration caption | Cupping scorecard + roast curve SVG | Condensed title + showtime grid |
| Section 1 | "Specification plate" (readout + figure) | "Roast curve" interactive | "Program" listing with page-turn hover |
| Interlude | Full-bleed figure with caption | Parchment pull-quote on kraft | Projection-room still with grain |
| Section 2 | Process contact sheet (horizontal) | Sourcing map + altitude stats | Filmmaker bios as program entries |
| Social proof | Colophon with real bench facts | Cupping notes ledger | Press wall (quotes, not logos) |
| CTA | Order slip (form as artifact) | Reserve-a-bag slip | Box office manifest |
| Footer | Fine-print colophon (type/paper notes) | Shelf-life seal | Accessibility + venue credits |

## Grid rules
- Asymmetric two-column with an 8–15% off-grid rail for plates/labels; avoid 12-column symmetry.
- Sticky technical rail allowed (spec plate, cup score) while story scrolls past; `position: sticky; top: ≤5rem`.
- Full-bleed dark band used exactly once (ledger or order slip); single accent equals single ask.
- Horizontal strips: always `overflow-x: auto` below 760px; above, pin + scrub.

## Section geometry — stop designing boring sections
High-budget work rarely lives in a stack of equal-height rectangular cards with identical padding.

When the domain and craft target support elevated presence, reject static, predictable section stacks. Prefer living geometries that create hierarchy, movement, and ownership:

- **Overlapping / staggered cards** — cards or media panels that overlap, cascade, or sit at slight angles rather than aligning to a rigid grid.
- **Organic side panels** — curved or wavy flanking panels that frame a central card or media object instead of straight columns.
- **Diagonal or circular arrangements** — content cards or images arranged along a diagonal, arc, or loose orbit rather than rows and columns.
- **Floating / layered compositions** — elements that feel placed in space (depth, scale contrast, soft shadows) instead of locked to a baseline grid.
- **Asymmetric focal layouts** — one dominant media or title moment with supporting elements orbiting it, rather than three equal feature cards.
- **Tunnel / perspective sequences** — content cards that recede or advance in depth (useful for product showcases, portfolios, or narrative sequences).

These are not decorative tricks. They are tools for hierarchy and energy. Use them only when they serve the content model and pass the industry recognition test. A logistics operations dashboard should stay disciplined; a brand, product, or portfolio site can afford (and often needs) more compositional ambition.

Never default to the generic three-column feature grid or centered hero + dual CTA stack. Derive the geometry from the artifact and the craft ceiling of the brief.

## Type composition
- Headline set to measured fit; per-line `clamp()` when line lengths differ > 15% (see typography.md).
- Section titles: one line of display + one line of italic optical-serif continuation (`em`). The italic is not decoration — it is the second voice of the artifact.
- Caption columns: mono, left-aligned, never centered; centered captions read as generic marketing.

## Imagery placement
- Photo direction: single light source, consistent grade (desaturate 10–25% and warm 5% for paper artifacts; higher-contrast/desat for editorial dark).
- Alt text must describe subject + light ("ridgeline at first light, valley filled with low cloud"), not keywords.
- One image may bleed the collage boundary (drop-shadowed print plate) — that is the pattern's signature; more than one breaks it.
