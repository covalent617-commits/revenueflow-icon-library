# Loading and motion reference

Motion communicates state; it must never be decoration at the expense of clarity.

| Pattern | Use | Guidance |
|---|---|---|
| Indeterminate spinner | Short operation with unknown duration | Keep small; pair with a textual status for longer waits |
| Determinate progress | Known measurable work | Show percentage or meaningful stage when reliable |
| Skeleton | Content is loading and layout is known | Match final content geometry; do not use as an indefinite placeholder |
| AI activity pulse | Assistant/agent is actively processing | Pair with explicit wording such as “Analysing”; never imply completion |
| Intelligence orbit | Subtle non-blocking ambient state | Decorative only; hide from screen readers |
| Success confirmation | A task completed successfully | Brief, non-blocking; preserve persistent status in the UI |
| Notification ring | A new notification arrives | Avoid repeated disruptive movement; respect reduced motion |
| Glow emphasis | Draw attention to a relevant control | Maintain contrast; never use glow as the only state indicator |

## Accessibility and behaviour
- Respect `prefers-reduced-motion: reduce`.
- Provide a static alternative for every non-essential animation.
- Avoid rapid flashing, large parallax and continuous motion that competes with reading.
- Do not animate status indefinitely after the operation has completed.
- Use `aria-live` for meaningful status text, not decorative animation.
- Do not announce every animation frame to assistive technology.

## Current demo
The catalogue demonstrates spinner, pulse, skeleton and orbit CSS patterns. These are reference behaviours, not yet a versioned production motion package. Product teams should extract and test reusable components before production use.
