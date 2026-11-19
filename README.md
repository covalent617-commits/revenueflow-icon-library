# RevenueFlow Official Visual Asset Library

The central source of truth for RevenueFlow icons, motion, loading states, illustration concepts and design tokens.

## Repository map
- `index.html` — searchable catalogue with category filters, favourites, preview, copy and download.
- `assets/manifest.json` — canonical metadata, keywords, stable IDs, source paths and approval states.
- `assets/icons.svg` — canonical reusable SVG sprite.
- `assets/icons/` — individually consumable SVGs generated from the sprite.
- `assets/brand/revenueflow-mark.svg` — 
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
Run `python -m http.server 8080` from the repository root, then open `http://localhost:8080`. This avoids local-file clipboard restrictions. The site uses local scripts and assets; no external icon CDN or runtime build system is required.

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
79 icon references, 9 motion references, including the approved ecosystem synchronisation loader with a dedicated large preview at the bottom of the catalogue, and 5 illustration concepts. The manifest is the exact source of status and metadata.


## GitHub Pages deployment

The published site is served from the repository root at `https://covalent617-commits.github.io/revenueflow-icon-library/`. The `.github/workflows/pages.yml` workflow deploys the root directory on every push to `main` and can also be run manually from the Actions tab. If the URL returns 404 before the first successful deployment, check that GitHub Pages is enabled for this repository with **Build and deployment → Source: GitHub Actions**.
