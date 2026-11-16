# mango — Art direction: the artifact-native method

Goal: produce a site that **could not have been produced for a different brand or industry**, instead of a dressed-up template. Follow this sequence every time; never skip Step 1.

## Step 1 — Name the artifact (before any code)
Write one line: **"This page is a ___."** Fill it with a physical or editorial object the *actual domain* already produces. The artifact must feel native to the industry.

| Product/domain           | Artifact the page IS                              |
|--------------------------|---------------------------------------------------|
| Real-estate developer    | A property brochure / sales catalogue with floor plans and site plans |
| Logistics / haulage      | A route book / consignment ledger / fleet status board |
| Construction firm        | A site progress report / bill of quantities / technical drawing set |
| Restaurant / hospitality | A tasting menu / reservation ledger / wine list |
| Compliance SaaS          | An audit working paper with stamped sign-offs |
| Camera lens manufactory  | A printed technical monograph (plates, figures, reg keys) |
| Coffee roastery          | A roast log / cupping sheet with graph paper |
| Ski film festival        | A film program booklet with showtimes in condensed type |
| Classical music venue    | A concert program with drop caps and seat rows |

If the domain is real-estate and the artifact is still "printed technical monograph", the direction has failed. Re-derive.

The artifact determines: layout skeleton, type system, information hierarchy, section grammar, and motion language. If the page cannot be described as a single real artifact that belongs to this industry, the direction is not resolved — stop and resolve it.

## Step 2 — Derive constraints from the artifact (10 min max)
From the *domain-native* artifact, extract 8–12 constraints. Example for a property sales catalogue:

- Large photography of the actual buildings / sites as primary evidence.
- Floor-plan plates and site diagrams treated as information, not decoration.
- Clear hierarchy: location → unit type → price / status.
- One restrained accent (often a deep green, terracotta, or navy depending on the brand), never a random vermilion.
- Type that feels institutional or residential, not technical-instrument.
- Generous margins and clear section breaks that feel like a printed brochure.

Every reference generalizes this way. The constraint list becomes the CSS/JS token spec. If a component does not obey a constraint that came from *this* domain's artifact, it is slop — cut or rework it.

## Step 3 — One hero object, one story
Pick the single object the scroll follows that actually belongs to the domain (a key building massing, a route map, a warehouse volume, a signature dish, a certificate). Build it procedurally (three.js/canvas/SVG) or photographically. The hero is a stage for that object, not a text wall with a background image. Budget: 60% of first-viewport visual mass = the object.

Rules: the hero object is interactive (drag, hover, tap toggles one state change), reacts to scroll (rotation/dolly), and has a second still life in the story below to pay off the hero promise.

## Step 4 — Composition contract
- The headline must fit its line box: measure `scrollWidth` vs parent width at 3 breakpoints (1440 / 1024 / 390). If it overflows, reduce the size or change `font-stretch`/tracking — never `overflow: hidden` on the page.
- Elements overlap deliberately (layered collage) only when each layer has a z-index job and a drop shadow that says paper or material thickness.
- Ghost numerals / figure keys / plate frames: allowed only when they carry information that belongs to the domain's artifact language. Banned when they are borrowed from a previous brief.

## Step 5 — Reject the default three + the previous mango look
Before finishing, ask whether the build contains any of these and, if so, replace:

1. Full-bleed blurred video with centered white headline.
2. Purple→blue gradient with glassmorphism cards and vague glow orbs.
3. Three equal feature columns with rounded-2xl icons and a "Get Started" CTA.
4. Any visual DNA from the AURELIA worked example (vermilion + paper, Archivo Expanded, FIG. labels, technical monograph grammar, camera-lens hero) when the domain is not a precision-instrument brand.

## Output of this step (must exist before coding)
A five-line "Direction card" committed to a scratch file or PR description:

1. Artifact: … (must be native to this domain)
2. Constraints (5+): …
3. Hero object: … (must belong to the domain)
4. Type system: …
5. One accent color: …
