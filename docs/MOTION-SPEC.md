# Loading and motion reference

Motion communicates a real state. It must never imply progress, intelligence or completion that has not happened.

## Catalogue patterns and implementation state

| Pattern | Catalogue ID | State | Production guidance |
|---|---|---|---|
| Indeterminate spinner | RF-MOT-001 | Approved | Use for short operations with unknown duration; pair with text for longer waits |
| AI activity pulse | RF-MOT-002 | Approved | Show only while an assistant/agent is actively processing; pair with explicit wording |
| Skeleton shimmer | RF-MOT-003 | Approved | Use only when final content geometry is known; never leave indefinitely |
| Intelligence orbit | RF-MOT-004 | Proposed | Concept is implemented in reference CSS; requires product/design approval |
| Determinate progress | RF-MOT-005 | Proposed | Set from measured progress; never animate a fabricated percentage |
| Success confirmation | RF-MOT-006 | Proposed | Use only after the backend confirms successful completion |
| Notification bell ring | RF-MOT-007 | Approved | Brief notification-arrival cue; avoid repeated disruptive motion |
| Soft glow emphasis | RF-MOT-008 | Approved | Secondary emphasis only; never the sole indicator of state |
| Ecosystem synchronisation loader | RF-MOT-009 | Approved | Preferred RevenueFlow loading icon; use in existing loading positions, not as a full-screen illustration |

The exact approval state lives in `assets/manifest.json`. The website preview is not proof of production integration.

## CSS references

`assets/motion.css` provides:
- `.rf-spinner`
- `.rf-ai-pulse`
- `.rf-skeleton`
- `.rf-orbit`
- `.rf-progress` (set `--rf-progress-value` from a measured value)
- `.rf-success`
- `.rf-bell-ring`
- `.rf-soft-glow`
- `.rf-ecosystem-loader`

## Signature loading icon: Ecosystem synchronisation (RF-MOT-009)

The loader is a compact, self-contained icon for the existing places where RevenueFlow is waiting for work to complete. It is not a splash screen, dashboard illustration, security graphic, background image or new loading page.

Its visual grammar is deliberately simple:
1. A central RevenueFlow mark anchors the identity.
2. Three thin orbital paths express connected systems working together.
3. Three small module nodes represent ecosystem capabilities: partnership, communication and configuration.
4. The orbits move at different, restrained speeds to communicate synchronisation without suggesting a percentage or measured completion.

Use the icon at compact sizes beside existing loading/status text. Do not add dashboard panels, locks, security imagery, large background artwork or decorative containers around it. The loader must not replace useful loading text on longer operations.

### Accessibility and runtime rules
- Give meaningful instances an accessible name such as “RevenueFlow ecosystem synchronising”; hide decorative instances from assistive technology.
- Respect `prefers-reduced-motion: reduce`; freeze orbital movement and retain a clear static icon.
- Start motion only while the associated operation is active and stop it when the operation ends or the component leaves the active state.
- Do not use it as a percentage/progress indicator.
- Do not announce animation frames to assistive technology.
- Never imply an operation succeeded until the backend confirms success.
