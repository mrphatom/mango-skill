# mango — The fixed-canvas three.js stage (procedural hero object)

Use when the brief's artifact has a hero object that can be built from primitives (product, instrument, package, vessel). Skip when photography is the story — then build a depth-stack collage instead.

## Architecture
- One `<canvas id="webgl">` fixed to the viewport, `z-index: 0`, `pointer-events: none`. All page content sits in `z-index: 1`.
- Renderer: `WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' })`, `setPixelRatio(min(dpr, 1.75))`, ACES tonemapping, `outputColorSpace = SRGBColorSpace`.
- Environment: `PMREMGenerator` + `RoomEnvironment`; dispose the generator after. Never HDRIs from random URLs.
- Camera path keyed to scroll progress `p ∈ [0,1]`: define 4–7 `cameraAt(p, aspect)` keys with pos/look triples, ease with smoothstep between keys, clamp `wide = clamp((aspect-0.7)/0.9)` so phones get a tighter crop.
- One procedural object with 3–5 material jobs (anodized metal, glass, accent emissive, dark steel). No loaded glTF for hero builds; procedural = flexible and self-contained.
- Fog: `FogExp2` tinted to the paper/background color at low density (0.04–0.06) so distant elements desaturate into the page.
- Lighting: key warm hard light; cool fill; one accent-colored rim at low intensity. Ambient at ≤1.2 for tonemap headroom.

## Composition rules for the hero
- The object's bounding sphere must fit inside the FOV at its first scroll key at every aspect; re-frame with `aspect`-aware keys, not a single fixed position.
- On mobile, shift object toward empty side of the collage or enlarge camera distance; never let the object sit on top of body copy.
- Scroll-linked rotation: `object.rotation.y = base + p * PI * 1.2`; iris/aperture contraction `scale` keyed off the same p curve.

## Failure modes and fixes (from real builds)
| Symptom | Cause | Fix |
|---|---|---|
| Object invisible against paper | Tone mapping crushed mids / camera look-target pushed off-frame | Raise key light ≥3 and rim, move look target toward object, verify pixel stats |
| Black void on load | unlit materials, no env map | RoomEnvironment + `envMapIntensity ≥ 1.2` |
| Page jank on scroll | per-frame vector allocations | Reuse scratch vectors; lerp camPos at 0.05–0.07 |
| Mobile overflow | canvas `position: fixed` with 100vw + body padding | canvas `inset: 0; width: 100%; height: 100%` and body `overflow-x: hidden` |
| Glass looks like plastic | opaque black MeshPhysicalMaterial | `transparent: true, opacity ~0.6–0.9, roughness < 0.1, clearcoat` |
| Chromium headless black | missing `--ignore-gpu-blocklist` | always pass in CI/verify scripts |

## Verification
- `verify.sh <url>` prints `PAGE {…}` — require `webgl: true`.
- Capture hero screenshot; compute right/left half average luminance; if the object's half is >30% darker than page bg on average, relight.
- Check `requestfailed` — RoomEnvironment is bundled with the three CDN import (no extra requests); any other texture request is suspicious.
