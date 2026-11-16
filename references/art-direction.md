# mango — Art direction: the artifact-native method

Goal: produce a site that **could not have been produced for a different brand**, instead of a dressed-up template. Follow this sequence every time; never skip Step 1.

## Step 1 — Name the artifact (before any code)
Write one line: **"This page is a ___."** Fill it with a physical or editorial object the domain already produces. Examples:

| Product/domain           | Artifact the page IS                              |
|--------------------------|---------------------------------------------------|
| Camera lens manufactory  | A printed technical monograph (plates, figures, reg keys) |
| Coffee roastery          | A roast log / cupping sheet with graph paper      |
| Ski film festival        | A film program booklet with showtimes in condensed type |
| Compliance SaaS          | An audit working paper with stamped sign-offs     |
| Classical music venue    | A concert program with drop caps and seat rows    |

The artifact determines: layout skeleton, type system, information hierarchy, section grammar, and motion language. If the page cannot be described as a single real artifact, the direction is not resolved — stop and resolve it.

## Step 2 — Derive constraints from the artifact (10 min max)
From the artifact, extract 8–12 constraints. For *printed technical monograph*:

- Hairline rules and generous internal margins (print), never cards-in-cards.
- Numbered figures with a `FIG. n` or figure-key motif; every visual is evidence, not decoration.
- A dark "instrument readout" element against light paper for signal contrast.
- One spot accent (vermilion class), never a gradient rainbow.
- Type pairing: one workhorse display face with real width axis, one text serif, one technical mono.
- Ink-soft body text at ~70% opacity of the paper-ink pair, not gray.
- Section headers behave like plate captions, not marketing slogans.

Every reference generalizes this way. The constraint list becomes the CSS/JS token spec. If a component does not obey a constraint, it is slop — cut or rework it.

## Step 3 — One hero object, one story
Pick the single object the scroll follows (camera objective, roast curve, waveform, certificate). Build it procedurally (three.js/canvas/SVG). The hero is a stage for that object, not a text wall with a background image. Budget: 60% of first-viewport visual mass = the object.

Rules: the hero object is interactive (drag, hover, tap toggles one state change), reacts to scroll (rotation/dolly), and has a second still life in the story below (close-up plate) to pay off the hero promise.

## Step 4 — Composition contract
- The headline must fit its line box: measure `scrollWidth` vs parent width at 3 breakpoints (1440 / 1024 / 390). If it overflows, reduce the size or change `font-stretch`/tracking — never `overflow: hidden` on the page.
- Elements overlap deliberately (layered collage) only when each layer has a z-index job and a drop shadow that says paper thickness.
- Ghost numerals/figure keys/plate frames: allowed when they carry information (figure number, section index). Banned when they are meaningless texture.

## Step 5 — Reject the default three
Before finishing, ask whether the build contains any of these and, if so, replace:

1. Full-bleed blurred video with centered white headline.
2. Purple→blue gradient with glassmorphism cards and vague glow orbs.
3. Three equal feature columns with rounded-2xl icons and a "Get Started" CTA.

## Output of this step (must exist before coding)
A five-line "Direction card" committed to a scratch file or PR description:

1. Artifact: …
2. Constraints (5+): …
3. Hero object: …
4. Type system: …
5. One accent color: …
