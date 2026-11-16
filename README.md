# RevenueFlow Official Visual Asset Library

The central reference catalogue for RevenueFlow icons, loading states, motion references, illustrations and design tokens.

**Purpose:** prevent inconsistent, ad-hoc visual asset selection across RevenueFlow. Developers and Cline must consult this library before introducing visual assets.

## Contents
- `index.html` — searchable interactive catalogue and SVG preview/export.
- `assets/manifest.json` — canonical asset metadata and approval states.
- `tokens/design-tokens.json` — semantic visual tokens.
- `GOVERNANCE.md` — mandatory asset selection and approval rules.
- `docs/MOTION-SPEC.md` — loading and motion behaviour.
- `CONTRIBUTING.md` — asset proposal and review process.

## Use
1. Search by name, category, keyword or asset ID.
2. Open an asset to inspect its ID, category, status and SVG.
3. Copy or download the SVG for local implementation.
4. Preserve the semantic meaning, accessible label and state.
5. If a needed asset is absent, propose it; do not silently substitute an external pack.

## Important status distinction
The catalogue currently contains a mix of approved icon references and proposed illustration concepts. The status is visible in the manifest. A catalogue entry is not automatically a production approval. The website is a reference/demo and does not itself migrate or enforce assets in the RevenueFlow application.

## Local preview
Open `index.html` directly in a modern browser. No build step or external runtime dependency is required.

## GitHub Pages
The repository includes a Pages deployment workflow. Enable GitHub Pages in repository Settings → Pages and select **GitHub Actions** as the build/deployment source if it is not already enabled.

## Version
Initial comprehensive catalogue build: **1.0.0**.
