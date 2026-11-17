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

## High-craft libraries as reference (not costume)
Modern component libraries (Magic UI, Unlumen UI, Smooth UI, Retro UI, and similar) are useful sources of:
- polished motion and interaction patterns
- shader / background / text-effect techniques
- neo-brutalist or maximalist energy when the Direction card calls for it
- ready-made accessible primitives that can be restyled

They are **not** the visual system. Extract the craft quality (timing, state design, material feel, type energy) and map it onto the domain-native Direction card. A real-estate site that looks like a Magic UI demo is a failure. A real-estate site that uses Magic-UI-level motion discipline while feeling like a property sales catalogue is a success.

## Anti-patterns
- Forcing a stack the user did not ask for
- Utility/class noise with no token layer on longer-lived work
- Accepting a component library’s default visual language
- Re-creating Button/Input/Card when the project already has accessible ones
- Mixing multiple spacing scales or radius systems
- Letting a library’s aesthetic override the industry recognition test

## When the user provides a template, design system, or stack preference
Treat it as source of truth. Extend it. Do not silently replace its decisions unless they fail accessibility or the anti-slop audit.
