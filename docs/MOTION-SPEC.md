# Loading and motion reference

Motion communicates a real state. It must never imply progress, intelligence or completion that has not happened.

## Catalogue patterns and implementation state

| Pattern | Catalogue ID | State | Production guidance |
|---|---|---|---|
| Indeterminate spinner | RF-MOT-001 | Approved | Use for short operations with unknown duration; pair with text for longer waits |
| AI activity pulse | RF-MOT-002 | Approved | Show only while an assistant/agent is actively processing; pair with explicit wording |
| Skeleton shimmer | RF-MOT-003 | Approved | Use only when final content geometry is known; never leave indefinitely |
| Intelligence orbit | RF-MOT-004 | Proposed | Preview concept only; no approved reusable production CSS component |
| Determinate progress | RF-MOT-005 | Proposed | Must be tied to measured progress, not estimated visual theatre |
| Success confirmation | RF-MOT-006 | Proposed | Must represent a confirmed successful outcome |
| Notification bell ring | RF-MOT-007 | Approved | Brief notification-arrival cue; avoid repeated disruptive motion |
| Soft glow emphasis | RF-MOT-008 | Approved | Secondary emphasis only; never the sole indicator of state |

The exact approval state lives in `assets/manifest.json`. The website preview is not a production integration.

## Current CSS references

`assets/motion.css` currently provides:
- `.rf-spinner`
- `.rf-ai-pulse`
- `.rf-skeleton`
- `.rf-bell-ring`
- `.rf-soft-glow`

The catalogue also previews proposed concepts. A preview does not imply that production-ready CSS or a reusable component exists.

## Accessibility and behaviour
- Respect `prefers-reduced-motion: reduce`; every non-essential animation needs a static alternative.
- Avoid rapid flashing, large parallax and continuous motion that competes with reading.
- Stop activity motion when the underlying operation ends.
- Use `aria-live` for meaningful status text, not decorative animation.
- Do not announce animation frames to assistive technology.
- Never imply an operation succeeded until the backend confirms success.
