# mango — Typography: a pairing with jobs, not a font list

## The rule
Every artifact demands three roles. Assign one family per role; never let a family cover two.

1. **Display/workhorse** — must have a width axis (variable `wdth`) or a condensed variant. This is the brand's voice at loud volumes: headlines, section titles, spec readouts. In the AURELIA build it was *Archivo Expanded* at 110–125 `font-stretch` with weight 800–900; the stretch axis is what makes tight-tracking uppercase feel machined rather than "bold Helvetica."
2. **Text serif** — carries body copy and italics. Must be a *real* serif with optical sizes (`opsz`) and a true italic, not a slanted roman. It is the hand that wrote the notes.
3. **Technical mono** — labels, reg keys, coordinates, captions. Small size (0.56–0.72rem), wide-ish tracking. It is the machine talking.

## How to choose (not "pick a nice font")
- Match the artifact's production process: letterpress monograph → expanded grotesque; roast log → humanist serif + tabular mono; film program → condensed display + oldstyle serif.
- If the domain has an incumbent typographic tradition (horology, gastronomy, railways), use its actual period reference — not what is popular on Google Fonts this quarter.
- Must exist as a variable font with `wdth` or `opsz` when used for display sizes. Static-weight-only grotesques are acceptable only for body/mono roles.
- Verify in the target browser: `document.fonts.check()` and measure `scrollWidth` of the longest headline at 390/768/1440px **after** fonts load, not before.

## Scale and rhythm
- Display: `clamp()` with a vw term tied to measured fit, not a round number. Example that passed: `font-size: clamp(1.95rem, 9.55vw, 10rem)` on the longer of two balanced lines, tighter clamp on the shorter line — per-line sizing prevents 2–3px clip disasters.
- Body: 16–19px, line-height 1.35–1.55, max-width 46–68ch, `text-wrap: pretty` or `balance` on headings.
- Mono captions: 0.56–0.72rem with 0.06–0.2em tracking; use tabular numerals (`font-variant-numeric: tabular-nums`) for specs and ledgers.

## Loading
- One Google Fonts `css2` URL per family with `display=swap`; preconnect to `fonts.gstatic.com` crossorigin.
- Never load a family you do not assign a role to. In the AURELIA build, unused families caused both bloat and temptation errors.

## Failures this prevents
- Two sans-serifs with no display contrast (the default).
- Gradient-clipped headline (hides a weak pairing behind an effect).
- Headline overflow at 390px because nobody measured with `scrollWidth` after font load.
