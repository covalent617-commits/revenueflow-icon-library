# RevenueFlow Visual Asset Governance

## Authority
This repository is the authoritative visual reference for RevenueFlow icons, loading states, motion, illustrations and design tokens. It is the first place developers and Cline must consult before adding a visual asset.

## Mandatory rules
1. Search this catalogue and manifest before creating or importing an asset.
2. Use stable asset IDs in implementation notes, pull requests and design reviews.
3. Use local, reviewed asset source. Do not add runtime dependencies on remote icon CDNs.
4. Do not silently substitute emoji, arbitrary Unicode glyphs, random SVGs, unrelated icon packs, stock illustrations or unreviewed animations.
5. Do not reinterpret an icon in a way that changes its semantic meaning.
6. Preserve accessible names, keyboard behaviour, focus visibility and non-colour status cues.
7. Respect `prefers-reduced-motion`; never make essential information depend on animation.
8. Keep asset source and manifest metadata together. Update both in the same change.
9. Use semantic design tokens rather than scattering hard-coded visual values.
10. Do not describe proposed assets as approved or production-ready.

## Missing asset process
When an asset is missing:
- Search aliases and related categories first.
- Record the missing use case, context, desired size, states and accessibility needs.
- Propose an asset with a suggested ID and source file.
- Add it as `proposed`; do not use it in production until reviewed and approved.
- If urgent delivery requires a temporary solution, explicitly document the exception, owner and removal/replacement plan. Never silently bypass governance.

## Status definitions
- `approved`: reviewed for inclusion in the official library. Product teams must still verify fit and accessibility in context.
- `proposed`: concept or candidate; not approved for production use.
- `deprecated`: retained for traceability but must not be used in new work.
- `experimental`: exploratory; not a stable product contract.

## Naming and IDs
- Icons: `RF-ICO-NNN`
- Motion: `RF-MOT-NNN`
- Illustrations: `RF-ILL-NNN`
- Tokens: semantic names such as `color.accent.primary`, not component-specific aliases.
IDs are permanent. Do not recycle IDs after deprecation.

## Cline implementation contract
Before changing frontend visuals, Cline should:
1. Inspect this repository's README and governance.
2. Search `assets/manifest.json` for the closest matching approved asset.
3. Use the matching local source and preserve the asset ID in code comments or component metadata where practical.
4. Report missing assets instead of choosing an unrelated substitute.
5. Update the manifest and source together when an approved new asset is added.

## Scope and enforcement
This repository documents and demonstrates the standard. It does not technically prevent a separate application repository from importing unapproved assets. Enforcement in application CI, lint rules and component packages must be implemented and tested in the consuming RevenueFlow codebase. Do not claim that enforcement exists until that integration is verified.
