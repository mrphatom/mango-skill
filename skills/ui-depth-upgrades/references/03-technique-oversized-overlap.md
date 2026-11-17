# 03 - Technique: Oversized subject + headline overlap

**Cures:** Boring layout, weak hierarchy, everything the same size.

## Core idea
Pull the main subject out of its photo box as a cutout, scale it large (often 1.4–2×), let it bleed off an edge, and overlap the headline.

## Key values
- Subject scale: 110–180% of original slot
- Overlap: 10–30% of the headline area
- Headline: display face, 2–3× body size, tight leading
- Z-order: background < headline < subject < secondary content
- Subject: `pointer-events: none` so it does not block taps

## Implementation notes
See `assets/templates/oversized-overlap.html` for a live before/after.
Use `scripts/cutout_subject.py` for simple cutouts.
Full recipes for Web / RN / SwiftUI / Compose in `06-implementation-recipes.md`.
