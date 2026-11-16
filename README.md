# RevenueFlow Official Visual Asset Library

The central source of truth for RevenueFlow icons, motion, loading states, illustration concepts and design tokens.

## Repository map
- `index.html` — searchable catalogue with category filters, favourites, preview, copy and download.
- `assets/manifest.json` — canonical metadata, keywords, stable IDs, source paths and approval states.
- `assets/icons.svg` — canonical reusable SVG sprite.
- `assets/icons/` — individually consumable SVGs generated from the sprite.
- `assets/catalogue-data.js` — generated website catalogue derived from the manifest.
- `assets/motion.css` — reduced-motion-aware CSS references.
- `tokens/design-tokens.json` — semantic design tokens.
- `GOVERNANCE.md` — mandatory selection and approval rules.
- `docs/CLINE-INTEGRATION.md` — exact implementation contract for Cline.
- `scripts/build_assets.py` — deterministic asset generator.
- `scripts/validate_assets.py` — dependency-free integrity checks.

## Use
Search by name, category, keyword or ID. Confirm the entry is marked `approved` before production use. Use the manifest's source path or matching sprite symbol. Preserve meaning and accessible labelling. If the right approved asset does not exist, propose it instead of substituting a random asset.

## Local preview
Open `index.html` in a modern browser. The site uses local scripts and assets; no external icon CDN or runtime build system is required.

## Validate after changes
```bash
python scripts/build_assets.py
python scripts/validate_assets.py
```
Commit generated files with their source changes.

## Status meanings
- `approved`: approved catalogue reference; validate contextual fit.
- `proposed`: awaiting explicit approval.
- `experimental`: trial asset not cleared for general use.
- `deprecated`: retained for migration/history; do not use in new work.

The website remains a reference library, not proof of production integration. The main RevenueFlow application now mirrors the manifest and sprite, uses a canonical icon adapter, and has an `AGENTS.md` policy plus tests to prevent arbitrary icon substitutions. Other consuming repositories must adopt the same contract.

## Current scope
79 icon references, 8 motion references with mixed approval states, and 5 illustration concepts. The manifest is the exact source of status and metadata.
