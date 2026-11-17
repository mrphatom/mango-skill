# Motion and interaction

## Principles
- One coherent motion metaphor when motion is used.
- Prefer purposeful micro-interactions and scroll-linked moments over decorative animation.
- Every interactive element needs clear hover, focus, active, disabled, and loading states.
- Honor `prefers-reduced-motion`. Keep functional state changes; drop parallax and purely decorative motion.

## Quality bar (high-budget)
- Interaction details should feel designed, not default.
- Motion should support hierarchy and feedback, not compete with content.
- Scroll-linked and scrubbed animation is often stronger than autoplay loops.
- A single well-executed 3D or interactive scene (orbit, cursor reaction, scroll progress) can carry more premium feel than many small effects.
- Advanced interactions (hover states that reveal structure, staggered entrances, layout morphs) are welcome when they clarify or delight — not when they only decorate.
- On mobile, prefer simple, reliable feedback over complex gesture theatre unless the product requires it.

## When using 3D / interactive embeds
- Treat the 3D object as the rich moment, not background noise.
- Prefer one hero scene over multiple competing models.
- Ensure the embed does not destroy performance, accessibility, or reduced-motion paths.
- The surrounding page must still feel domain-native; a generic robot or abstract shape rarely helps a real-estate or logistics product.

## Anti-patterns
- Autoplaying decorative loops
- Multiple competing animation systems on one page
- Motion that traps scroll or causes layout shift
- Ignoring reduced-motion preferences
- Using 3D or shaders as default “premium sauce” regardless of domain
