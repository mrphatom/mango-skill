# Components & Tailwind

## Principles
- Tailwind (or equivalent utility system) is an implementation detail. It should not be visible as the “style” of the product.
- Prefer a small set of composed primitives over a large pre-styled component library that fights the Direction card.
- Accessibility behavior (focus management, keyboard, ARIA) is non-negotiable. Use Radix / Base UI / Ark / native elements for behavior, then style to the direction.

## Recommended practice
- Define semantic tokens early (`--surface`, `--ink`, `--muted`, `--accent`, `--border`, `--ring`).
- Map those tokens into Tailwind config or CSS variables so utilities stay consistent.
- Build or extend only the components the product actually needs. Avoid installing an entire kit “just in case.”
- When using shadcn-style CLI components, immediately restyle them to the Direction card. Do not ship the default look.

## Anti-patterns
- Utility class noise with no token layer on a long-lived project
- Accepting the default visual language of any component library
- Creating a new Button/Input/Card from scratch when the project already has accessible ones
- Mixing three different spacing scales or radius systems

## When the user provides a template or design system
Treat it as source of truth. Extend it. Do not silently replace its type, color, or component decisions unless they fail accessibility or the anti-slop audit.
