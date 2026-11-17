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

The exact approval state lives in `assets/manifest.json`. The website preview is not a production integration.

## Current CSS references

`assets/motion.css` provides all eight reference patterns:
- `.rf-spinner`
- `.rf-ai-pulse`
- `.rf-skeleton`
- `.rf-orbit`
- `.rf-progress` (set `--rf-progress-value` from a measured value)
- `.rf-success`
- `.rf-bell-ring`
- `.rf-soft-glow`

All eight patterns have reference CSS and catalogue previews. Proposed patterns remain gated from production use until explicitly approved.

## Accessibility and behaviour
- Respect `prefers-reduced-motion: reduce`; every non-essential animation needs a static alternative.
- Avoid rapid flashing, large parallax and continuous motion that competes with reading.
- Stop activity motion when the underlying operation ends.
- Use `aria-live` for meaningful status text, not decorative animation.
- Do not announce animation frames to assistive technology.
- Never imply an operation succeeded until the backend confirms success.

## Signature motion: Master Compass Loader (RF-MOT-009)

**Status: Proposed — visible in the library preview, not production-approved.**

This is a signature RevenueFlow loading/activity motif, not a generic compass glyph. It must show two simultaneous, independent movements:

1. **Axial rotation:** the compass rose spins around its own centre.
2. **Orbital revolution:** the compass assembly travels around a separate, fixed central orbital axis.

The centre hub and orbital track establish the fixed reference axis. The orbiting compass satellite follows the circular path while its rose independently spins. The two animations must remain independently controllable; do not combine them into one rotation or fake the orbital movement with a simple spinner.

### Reference implementation

`assets/motion.css` provides `.rf-master-compass`, `.rf-master-compass__orbit`, `.rf-master-compass__rose`, `.rf-master-compass__hub` and `.rf-master-compass__track`.

The catalogue preview uses a metallic silver/blue treatment on the library's dark navy surface. Keep the silhouette crisp at compact sizes and do not let the animation imply measured task progress or successful completion.

### Accessibility and runtime rules
- Respect `prefers-reduced-motion: reduce`; freeze both moving layers while retaining a legible static compass.
- Give meaningful instances an accessible name such as “RevenueFlow compass activity”; hide purely decorative instances from assistive technology.
- Stop both animations when the associated operation ends or the component leaves the active state.
- Do not use as a percentage/progress indicator.
- Keep axial speed and orbital speed as separate CSS animation controls.
- Status remains **proposed** until explicitly approved through the library's asset governance process.
