#!/usr/bin/env python3
"""Dependency-free integrity checks for the RevenueFlow visual asset library."""
from __future__ import annotations
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "assets/manifest.json").read_text(encoding="utf-8"))
assets = manifest.get("assets", [])
ids = [a.get("id") for a in assets]
assert len(ids) == len(set(ids)), "Duplicate stable asset IDs"
assert all(ids), "An asset is missing its ID"
allowed = {"approved", "proposed", "experimental", "deprecated"}
assert all(a.get("status") in allowed for a in assets), "Unknown approval status"
sprite = ET.parse(ROOT / "assets/icons.svg").getroot()
symbols = {n.attrib.get("id", "") for n in sprite if n.tag.rsplit("}", 1)[-1] == "symbol"}
icons = [a for a in assets if a["id"].startswith("RF-ICO-")]
assert len(icons) == len(symbols), "Manifest icon count differs from SVG sprite"
for a in icons:
    assert "rf-" + a["symbol"] in symbols, f"Missing sprite symbol for {a['id']}"
    path = ROOT / a["source"]
    assert path.is_file(), f"Missing standalone SVG: {a['source']}"
    ET.parse(path)
catalogue_text = (ROOT / "assets/catalogue-data.js").read_text(encoding="utf-8")
match = re.search(r"window\.RF_CATALOGUE = (\{[\s\S]*\});\s*$", catalogue_text)
assert match, "Generated catalogue JS has invalid wrapper"
catalogue = json.loads(match.group(1))
def expected(prefix):
    return [[a["id"], a["name"], a["category"], a.get("symbol", ""),
             ", ".join(a.get("keywords", [])), a["status"]]
            for a in assets if a["id"].startswith(prefix)]
assert catalogue["icons"] == expected("RF-ICO-"), "Website icon data is stale"
assert catalogue["motions"] == expected("RF-MOT-"), "Website motion data is stale"
assert catalogue["illustrations"] == expected("RF-ILL-"), "Website illustration data is stale"
assert set(catalogue["iconSvg"]) == {a["symbol"] for a in icons}, "Website SVG export map is incomplete"
html = (ROOT / "index.html").read_text(encoding="utf-8")
assert 'src="assets/catalogue-data.js"' in html, "Website does not load canonical catalogue data"
css = (ROOT / "assets/motion.css").read_text(encoding="utf-8").replace(" ", "")
assert "@media(prefers-reduced-motion:reduce)" in css, "Reduced-motion fallback is missing"
json.loads((ROOT / "tokens/design-tokens.json").read_text(encoding="utf-8"))
print(json.dumps({"valid": True, "manifest_version": manifest["schema_version"],
                  "assets": len(assets), "icons": len(icons), "svg_symbols": len(symbols),
                  "standalone_icons": len([a for a in icons if (ROOT / a["source"]).is_file()]),
                  "statuses": {s: sum(a["status"] == s for a in assets) for s in sorted(allowed)}}, indent=2))
