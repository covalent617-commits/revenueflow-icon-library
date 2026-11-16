# Icon library repository instructions

This repository is the single canonical source for RevenueFlow visual assets.

- Keep `assets/manifest.json` as the metadata and approval source of truth.
- Keep `assets/icons.svg` as canonical icon geometry.
- Generate standalone SVGs and website data with `python scripts/build_assets.py`.
- Run `python scripts/validate_assets.py` after every asset change.
- Never introduce arbitrary icon packs, remote CDNs, emoji, glyphs or unreviewed one-off SVGs.
- Only `approved` entries may be used in production; proposed illustrations/motion need explicit review.
- When adding an icon, update the sprite, manifest, generated files, site catalogue and any consuming app mirrors in the same change set.
- Do not mark an asset approved merely because its SVG exists.
- Keep accessible naming, contrast, responsive sizing and reduced-motion behaviour intact.
