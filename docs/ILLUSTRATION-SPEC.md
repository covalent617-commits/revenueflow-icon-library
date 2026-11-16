# Illustration system

## Purpose
Small, original vector illustrations for empty, onboarding, permission and recoverable error states. Illustrations support the message; they never replace explanatory text or an actionable next step.

## Visual language
- Canvas: `240 × 160` viewBox for the current illustration family.
- Style: restrained line-art, rounded joins/caps, generous negative space.
- Palette: RevenueFlow dark surfaces with limited indigo, cyan and amber accents; inherit `currentColor` for neutral outlines where possible.
- Complexity: one primary metaphor, no decorative clutter, no tiny detail that disappears at small sizes.
- No stock art, emoji, arbitrary glyphs or external illustration libraries.
- Keep the artwork independent of user data; never embed customer names, values or sensitive records.

## Accessibility
- Every illustration must have adjacent explanatory text in the consuming interface.
- Decorative inline use should set `aria-hidden="true"`; do not duplicate the same message in an image label and adjacent heading.
- Meaningful standalone use requires a concise accessible name.
- Never use colour alone to communicate the state.

## Current artwork
The five initial SVG concepts are present in `assets/illustrations/` and marked `proposed` in the manifest. Their existence is not approval for production use. Review each in the actual consuming screen at desktop and mobile sizes before changing its status.
