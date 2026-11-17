# 04 - Technique: Scene background + layered content

**Cures:** Flat screen, sterile cards-on-solid, no atmosphere.

## Core idea
Replace a solid/flat background with a full-bleed scene. Stack content on top with clear layers and a scrim for legibility.

## Layer model
1. Scene (full-bleed image / illustration / rich gradient)
2. Atmosphere / scrim (soft gradient for contrast)
3. Primary content (hero number, title)
4. Secondary panels (frosted / glass cards)
5. Chrome (nav, status)

## Key values
- Scrim opacity typically 0.25–0.45 over the busiest region
- Verify contrast with `scripts/contrast_check.py`
- Prefer CSS backdrop-filter with solid fallback
- Respect `prefers-reduced-transparency` and `prefers-reduced-motion`

See `assets/templates/immersive-scene.html`.
