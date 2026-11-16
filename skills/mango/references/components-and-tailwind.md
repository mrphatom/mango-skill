# Components & implementation

## Principles
- Styling systems and component libraries are implementation details. They should not become the visual identity of the product.
- Prefer a small set of composed primitives over a large pre-styled kit that fights the Direction card.
- Accessibility behavior (focus management, keyboard, ARIA) is non-negotiable. Use solid primitives (Radix, Base UI, Ark, native elements, or the project’s existing ones) for behavior, then style to the direction.
- Honor the user’s stated preference or the project’s existing approach. Do not force Tailwind, CSS Modules, or any other system.

## Recommended practice
- Define semantic tokens early (`--surface`, `--ink`, `--muted`, `--accent`, `--border`, `--ring`) regardless of the styling approach.
- Map those tokens into whatever system is in use so spacing, type, and color stay consistent.
- Build or extend only the components the product actually needs. Avoid installing an entire kit “just in case.”
- When using any pre-built components (shadcn-style or otherwise), restyle them to the Direction card. Do not ship the default look.

## Anti-patterns
- Forcing a stack the user did not ask for
- Utility or class noise with no token layer on a long-lived project
- Accepting the default visual language of any component library
- Creating a new Button/Input/Card from scratch when the project already has accessible ones
- Mixing three different spacing scales or radius systems

## When the user provides a template, design system, or stack preference
Treat it as source of truth. Extend it. Do not silently replace its type, color, component, or tooling decisions unless they fail accessibility or the anti-slop audit.
