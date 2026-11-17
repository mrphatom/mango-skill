# Security and hardening (when it becomes an application)

Activate this thinking automatically when the work involves auth, user data, permissions, money, PII, file uploads, or external integrations.

## Quick threat model
1. Map trust boundaries (HTTP, forms, uploads, webhooks, third-party APIs, LLM output).
2. Name the assets worth protecting.
3. For each boundary ask: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege.
4. Write abuse cases next to use cases.

## Always do
- Validate and constrain all untrusted input
- Authorize every sensitive action (not just authenticate)
- Use safe defaults for forms, uploads, and API responses
- Avoid leaking internal details in errors
- Treat secrets as sacred

## Frontend-relevant
- Never trust client-only checks for authorization
- Sanitize or carefully handle any user-generated content that will be rendered
- Be deliberate with third-party scripts and tokens in the browser
- Prefer httpOnly / secure cookie patterns when auth is involved (coordinate with backend)

Security is a constraint on every line that touches untrusted data, not a phase at the end.
