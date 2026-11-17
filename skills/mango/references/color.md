# mango — Color: OKLCH ramps, tinted neutrals, spot accent

## Rules
1. Define 11 brand steps in OKLCH (L from 0.985 → 0.15). Use `scripts/palette.py <hue> <chroma>` to seed, then hand-tune — generated ramps are starting points, not finished systems.
2. **Neutrals carry the hue.** Never `#ffffff`/`#000000` raw. Paper: L≈0.96, C≈0.01. Ink: L≈0.15, C≈0.015. Warm-cool bias is a brand decision: state it in the direction card.
3. Exactly **one spot accent**, reserved for action and signal (CTA, fault, active state). Never two competing accents; never vermilion for both CTA and "error."
4. Contrast: body text ≥ 4.5:1 on paper; large display ≥ 3:1; accent on paper for ≥ 19px bold only. Measure, don't eyeball (`color-contrast.com` or `npx @primer/contrast-check`).
5. Dark sections are not `#111` defaults. They are the ink token or a desaturated sibling of the accent's complement. Semi-gradients (radial/linear washes at 5–12% accent alpha, or warm→cool paper tints) create depth without glow.
6. Forbid: purple→blue gradients, teal→lime gradients, 100% saturated backgrounds behind body copy.

## Mood pair + memorable accent (core energy rule)
The first two colors set the mood. The accent gives the viewer something to remember.

Build the base as a coherent pair (deep + light, or dominant neutral + supporting surface). Then introduce **one** accent that injects energy, hierarchy, or character. Without that third note the system often stays cold, soft, or inert even when the individual colors are correct.

Examples of the *method* (derive fresh values for the current domain — do not copy hexes):
- Obsidian black + ice gray (clean, cold) → racing red → suddenly the brand has energy and direction
- Deep charcoal + electric violet (already strong) → acid lime → the system becomes impossible to scroll past
- Raspberry pink + pale pink (soft, playful) → butter yellow → packaging and product surfaces demand attention

This is not "use three colors." It is a deliberate hierarchy: mood-setting pair first, then a single high-signal accent that lives on the opposite side of the temperature or hue wheel from the base.

## Complementary / energy accent (the lever)
A strong way to create hierarchy and life is to place the single accent on the **opposite side of the color wheel** (or temperature axis) from the dominant neutrals / base.

When the base feels cold, washed, or inert, a complementary or high-chroma touch often wakes the whole surface up without needing more color.

Illustrative patterns (derive fresh values):
- Cool glacier blue + deep navy base → one lemon / chartreuse accent → eyes know where to look
- Deep teal + cream base → one orange accent → turns "cold beans" into "hot out the roaster"
- Cream + near-black ink base → one orchid / magenta accent → turns washed out into a flower show
- Black + cool gray → racing red or acid lime → performance / tech energy without neon chaos

Principle, not recipe: the accent should feel like a deliberate signal, not decoration. If the page still looks cold after the accent is placed, the accent is either too weak, too similar in temperature, or competing with itself.

## Working tokens (shape, not values — values come from the build)
```css
:root{
  --paper: …; --paper-2: …; --card: …;         /* tinted light surfaces */
  --ink: …; --ink-soft: …;                      /* tinted dark text */
  --brand-x00: …;                               /* 11-step seed ramp */
  --accent: …; --accent-deep: …;                /* one spot color */
  --rule: …; --hairline: …;                     /* rules are ink at alpha, not gray solids */
}
```

## Gradient budget
At most two gradient expressions on the whole page: one "wash" behind a key section (radial at 8–12% accent or brand), one on a ledger/dark band. Everything else is flat tinted paper + ink rules. If a third appears, delete the weakest.
