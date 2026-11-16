# Contributing assets

All additions must serve a documented RevenueFlow product use case and maintain a coherent visual language.

## Proposal checklist
- [ ] Explain the product context and user task.
- [ ] Search for an existing asset or suitable variant.
- [ ] Propose a permanent ID using the correct prefix.
- [ ] Supply editable/source SVG or documented motion implementation.
- [ ] Add name, category, aliases, keywords, status and usage guidance to the manifest.
- [ ] Include default, hover, active, disabled and focus states where relevant.
- [ ] Include accessible name/description guidance.
- [ ] Respect reduced motion and avoid colour-only meaning.
- [ ] Check light/dark surfaces and responsive sizes where relevant.
- [ ] Update catalogue previews and documentation.
- [ ] Run catalogue integrity checks before requesting review.

## SVG requirements
Use clean inline SVG with a viewBox, explicit stroke/fill behaviour, sensible stroke widths and no embedded scripts. Avoid external image references, filters that impair performance, and unnecessary path complexity. Decorative SVGs must be hidden from assistive technology; meaningful icons need an accessible label from the consuming component.

## Motion requirements
Document purpose, duration, easing, trigger, completion state, cancellation behaviour and reduced-motion alternative. Motion must not block user input or conceal errors.

## Review
A proposed entry remains `proposed` until reviewed. Approval should consider semantic clarity, visual consistency, accessibility, implementation cost, licensing/provenance and product fit.
