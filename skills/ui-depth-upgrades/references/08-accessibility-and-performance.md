# 08 - Accessibility and Performance

## Contrast
Always verify text over imagery with `scripts/contrast_check.py`. Target AA (4.5:1 normal / 3:1 large).

## Motion & transparency
Respect `prefers-reduced-motion` and `prefers-reduced-transparency`. Provide solid fallbacks for glass panels.

## Hit targets
Minimum 44×44 pt (iOS) / 48×48 dp (Android). Decorative subjects must not intercept taps (`pointer-events: none`).

## Performance
- Prefer SVG / CSS for motifs over large rasters.
- Lazy-load scene images; preload the hero.
- Limit simultaneous backdrop-filters.
- Avoid layout shift when images load (reserve space or use aspect-ratio).

## Screen readers
Decorative depth gets aria-hidden. Real text stays real text (not baked into images) with proper labels.
