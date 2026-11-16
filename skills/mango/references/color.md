# mango — Color: OKLCH rampling, tinted neutrals, spot accent

## Rules
1. Define 11 brand steps in OKLCH (L from 0.985 → 0.15). Use `scripts/palette.py <hue> <chroma>` to seed, then hand-tune — generated ramps are starting points, not finished systems.
2. **Neutrals carry the hue.** Never `#ffffff`/`#000000` raw. Paper: L≈0.96, C≈0.01. Ink: L≈0.15, C≈0.015. Warm-cool bias is a brand decision: state it in the direction card.
3. Exactly **one spot accent**, reserved for action and signal (CTA, fault, active state). Never two competing accents; never vermilion for both CTA and "error."
4. Contrast: body text ≥ 4.5:1 on paper; large display ≥ 3:1; accent on paper for ≥ 19px bold only. Measure, don't eyeball (`color-contrast.com` or `npx @primer/contrast-check`).
5. Dark sections are not `#111` defaults. They are the ink token or a desaturated sibling of the accent's complement. Semi-gradients (radial/linear washes at 5–12% accent alpha, or warm→cool paper tints) create depth without glow.
6. Forbid: purple→blue gradients, teal→lime gradients, 100% saturated backgrounds behind body copy.

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
