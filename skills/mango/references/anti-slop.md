# mango — Anti-slop: the reject list and the replacement rule

Slop is not "bad taste." Slop is any element that exists because it is common, not because the artifact calls for it. Use these two lists at the end of every build, not the beginning.

## Reject on sight (delete or redesign)
- Default Inter/Roboto/system-ui unmodified, when the artifact demands a real pairing.
- Purple-blue or teal-lime gradients; glow orbs; noise textures with no ink job.
- `backdrop-filter: blur()` glass cards floating over stock photos.
- Three-up feature grid with identical round-icon + title + blurb cards.
- Gradient-clipped headline text for its own sake.
- Emoji bullets, `🚀`, decorative dividers of dots/waves/stars.
- Rounded-2xl on everything; pill buttons everywhere.
- Stock "diverse team smiling at laptop" imagery with no relation to the artifact.
- Centered everything. Left-aligned asymmetric grids usually signal a real opinion.
- Fake stats (99% uptime of a "made in 3 days" page) presented without measurement.
- CTA repetition: more than two asks on one page is anxiety, not conversion.

## Replacement rule of thumb
For every rejected element, replace with an artifact-derived equivalent:
| Rejected                        | Replace with                                               |
|---------------------------------|-------------------------------------------------------------|
| Icon feature grid               | Numbered plates/figures that are *evidence* of the story    |
| Testimonial carousel            | One quoted line in the artifact's own voice, with provenance|
| Gradient hero                   | Layered collage: object + caption + hairline rule           |
| Badge "trusted by X"            | Countable ledger rows (units, years, audits)                |
| Newsletter signup footer        | Order slip / manifest / working paper form                  |

## Replacement constraint
A replacement must be *measurably different* from the rejected thing: different geometry, different hierarchy, different role in the story. A swapped color is not a replacement.

## Self-audit questions (answer all before shipping)
1. If this brand's domain vanished tomorrow, would any element still make sense? → It doesn't belong.
2. Which elements carry information? Are there fewer decorative elements than informative ones?
3. Does anything exist because "the reference site did it"? Name the artifact constraint it obeys.
4. Would removing any animation make the story harder to follow? Animations that only decorate must go.
5. Does the page still work with WebGL off, JS off, reduced-motion on? (Minimum: content and hierarchy intact.)

## The non-negotiable floor
Taste can be argued. The floor cannot: semantic landmarks, focus-visible styles, alt text on every informational image, no horizontal shell overflow on mobile, no console errors on load, honest measurement of any claim.
