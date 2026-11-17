# Motion and interaction

## Principles
- One coherent motion metaphor when motion is used.
- Prefer purposeful micro-interactions and scroll-linked moments over decorative animation.
- Every interactive element needs clear hover, focus, active, disabled, and loading states.
- Honor `prefers-reduced-motion`. Keep functional state changes; drop parallax and purely decorative motion.

## Quality bar
- Interaction details should feel designed, not default.
- Motion should support hierarchy and feedback, not compete with content.
- On mobile, prefer simple, reliable feedback over complex gesture theatre unless the product requires it.

## Anti-patterns
- Autoplaying decorative loops
- Multiple competing animation systems on one page
- Motion that traps scroll or causes layout shift
- Ignoring reduced-motion preferences
