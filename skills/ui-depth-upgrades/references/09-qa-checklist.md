# 09 - QA Checklist

Use this as the final pass before delivering a redesign, spec, or code. Mark each item; fix or call out exceptions explicitly.

## Contents
- Diagnosis and scope
- Move 1 checks
- Move 2 checks
- Move 3 checks
- Cross-cutting checks
- Squint and swap tests
- Delivery checklist

## Diagnosis and scope

- [ ] The dominant problem (boring / flat / generic) is named, with the evidence.
- [ ] One primary move is applied at full strength; supporting moves are lighter.
- [ ] Information architecture is unchanged unless the user asked otherwise.
- [ ] Every change has a one-line reason.

## Move 1 checks (oversized subject + overlap)

- [ ] Subject is cut out (no box) with clean edges on light and dark backgrounds.
- [ ] Subject width is 110-180% of its container and bleeds off at least one edge deliberately.
- [ ] Headline is large (>= 2-3x body), tight leading, left-aligned, in a display face with robust letterforms.
- [ ] Overlap covers roughly 10-30% of the headline; all words still readable.
- [ ] Z-order: background < headline < subject < info/CTA < system UI.
- [ ] Subject never covers controls or small text; `pointer-events: none` / hit-testing disabled on the subject.
- [ ] Contact/ambient shadow present and consistent with light direction.
- [ ] Works at 320 px width and at 200% font scale.

## Move 2 checks (scene + layers)

- [ ] Background is a scene that means something (tied to content or state).
- [ ] Layers are named (scene, atmosphere, content, chrome) and each has one job.
- [ ] Scrim/tint ensures text >= 4.5:1 (3:1 large) on the worst region (verified with `contrast_check.py`).
- [ ] Hero numeral/title is oversized and light; supporting text is small and calm.
- [ ] Glass panels: blur, tint, border, radius defined; solid fallback for no-blur/reduced transparency.
- [ ] Scene responds to data states (or a neutral default is defined).
- [ ] Number of blurred layers is limited; no blur on long lists.
- [ ] Status bar and home indicator areas are legible over the scene.

## Move 3 checks (cohesive style)

- [ ] Motif is named in one sentence.
- [ ] Palette extracted from hero artwork (3-5 colours) and recorded as tokens.
- [ ] Motif appears on all four surfaces: crop, lettering, controls, palette.
- [ ] Framework-default blue (or other default primary) is gone.
- [ ] Custom controls keep affordances, 44/48 minimum hit areas, and visible pressed/focus states.
- [ ] Curved text is gentle and readable; real text with accessible label.
- [ ] Tokens (colours, radii, stroke, fonts, motion) defined once; `audit_style_tokens.py` shows reduced sprawl.
- [ ] Style carries to at least one other screen without new one-off values.

## Cross-cutting checks

- [ ] Accessibility: contrast, text scaling, screen-reader labels and order, focus visibility, reduced motion/transparency/high contrast variants.
- [ ] Performance: asset sizes within budget, hero preloaded, no layout shift, no animated blur.
- [ ] Resilience: fallbacks for missing images/fonts, small screens, landscape, dark mode.
- [ ] Licensing: images, fonts, illustrations cleared; no copied third-party artwork or trade dress.
- [ ] Platform conventions respected where they matter (back gesture, safe areas, system sheets).

## Squint and swap tests

- **Squint test:** blur your eyes or the screenshot. You should see one dominant shape (the subject, the numeral, the artwork) and a calm secondary structure.
- **Greyscale test:** convert to greyscale; hierarchy and legibility must hold without colour.
- **Swap test:** replace the app name and imagery with another app's. If the screen would still "fit", the style is still generic.
- **Squeeze test:** narrow to 320 px and enlarge text to 200%; nothing critical is hidden or overlapped.
- **Thumb test (mobile):** can the main action be reached and hit with one thumb without precision?

## Delivery checklist

- [ ] Output follows the format in `SKILL.md` (diagnosis, primary move, changes with values, layer order, assets, accessibility, code/prompt as relevant).
- [ ] Code runs (open the HTML; build the component) or is clearly marked as a snippet needing integration.
- [ ] Assumptions stated in a line.
- [ ] Next iteration offered only if useful (e.g. "apply the same tokens to the settings screen").
