# Cline integration contract

When implementing or modifying RevenueFlow UI:

1. Read the Visual Asset Library README and GOVERNANCE.md.
2. Search assets/manifest.json by semantic name, keywords and category.
3. For an approved icon, use its SVG symbol from assets/icons.svg or copy its SVG markup into the consuming application with provenance retained.
4. Import tokens from tokens/design-tokens.json into the consuming design-token layer; do not independently invent competing values.
5. For loading states, follow docs/MOTION-SPEC.md and use assets/motion.css as the reference implementation.
6. If no appropriate approved asset exists, report the gap and propose a new asset. Do not select a random external asset.
7. In implementation reports, distinguish a reference available in this repository from an asset actually integrated and tested in the product application.

Example SVG symbol use (adjust the asset path for the consuming application's public/static asset configuration):

```html
<svg role="img" aria-label="Dashboard">
  <use href="/assets/icons.svg#rf-grid"></use>
</svg>
```

For decorative icons use `aria-hidden="true"`. For icon-only controls, provide an accessible name on the button itself.
