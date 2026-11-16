# Cline integration contract

This is mandatory for every RevenueFlow UI implementation.

1. Read `README.md` and `GOVERNANCE.md` before selecting or adding visual assets.
2. Search `assets/manifest.json` by stable ID, semantic name, keywords and category.
3. Use only `approved` entries in production. Proposed/experimental assets require explicit approval; deprecated assets are forbidden for new work.
4. Use the manifest's standalone SVG `source` path or matching symbol from `assets/icons.svg`; retain the asset ID in implementation records.
5. Treat `tokens/design-tokens.json` as a reference candidate. Do not wholesale-import or override the product's existing design tokens without an explicit design-system review. Map only approved semantics into the consuming app's existing token layer.
6. Follow `docs/MOTION-SPEC.md` and `assets/motion.css`; support `prefers-reduced-motion`.
7. If a suitable approved asset is missing, report the gap and propose an addition. Never silently use emoji, arbitrary glyphs, external icon packs, random SVGs or stock art.
8. Run `python scripts/build_assets.py` and `python scripts/validate_assets.py` after library changes.
9. Report separately what is referenced, integrated, tested and browser-verified.

Standalone icon:
```html
<img src="/assets/icons/grid.svg" alt="" aria-hidden="true">
```

Sprite:
```html
<svg aria-hidden="true" focusable="false"><use href="/assets/icons.svg#rf-grid"></use></svg>
```

For icon-only controls, put the accessible name on the button itself.
