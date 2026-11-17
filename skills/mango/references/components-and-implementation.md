# Components and implementation

## Principles
- Styling systems and component libraries are implementation details. They must not become the visual identity.
- Prefer a small set of composed primitives over a large pre-styled kit that fights the Direction card.
- Accessibility behavior (focus, keyboard, ARIA) is non-negotiable.
- Honor the user’s stated preference or the project’s existing approach. Do not force a stack.

## Practice
- Define semantic tokens early (`--surface`, `--ink`, `--muted`, `--accent`, `--border`, `--ring`) regardless of tooling.
- Map tokens into whatever system is in use so spacing, type, and color stay consistent.
- Build or extend only the components the product actually needs.
- When using any pre-built components, restyle them to the Direction card. Never ship the library’s default look as the brand.

## Anti-patterns
- Forcing a stack the user did not ask for
- Utility/class noise with no token layer on longer-lived work
- Accepting a component library’s default visual language
- Re-creating Button/Input/Card when the project already has accessible ones
- Mixing multiple spacing scales or radius systems

## When the user provides a template, design system, or stack preference
Treat it as source of truth. Extend it. Do not silently replace its decisions unless they fail accessibility or the anti-slop audit.
