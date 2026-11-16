#!/usr/bin/env python3
"""Validate RevenueFlow visual asset catalogue integrity without third-party packages."""
from __future__ import annotations
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "assets/manifest.json").read_text(encoding="utf-8"))
assets = manifest.get("assets", [])
ids = [a.get("id") for a in assets]
assert len(ids) == len(set(ids)), "Duplicate asset IDs"
assert all(ids), "Asset missing stable ID"
allowed = {"approved", "proposed", "experimental", "deprecated"}
assert all(a.get("status") in allowed for a in assets), "Unknown approval status"
sprite = ET.parse(ROOT / "assets/icons.svg").getroot()
symbols = {node.attrib.get("id", "") for node in sprite if node.tag.rsplit("}", 1)[-1] == "symbol"}
icons = [a for a in assets if a["id"].startswith("RF-ICO-")]
assert len(icons) == len(symbols), "Icon count does not match SVG sprite"
for a in icons:
    symbol = "rf-" + a["symbol"]
    assert symbol in symbols, f"Missing sprite symbol: {symbol}"
    assert (ROOT / a["source"]).is_file(), f"Missing standalone SVG: {a['source']}"
    ET.parse(ROOT / a["source"])
assert (ROOT / "assets/catalogue-data.js").is_file(), "Generated catalogue data missing"
assert (ROOT / "assets/motion.css").is_file(), "Motion CSS missing"
css = (ROOT / "assets/motion.css").read_text(encoding="utf-8")
assert "@media(prefers-reduced-motion:reduce)" in css.replace(" ", ""), "Reduced-motion fallback missing"
tokens = json.loads((ROOT / "tokens/design-tokens.json").read_text(encoding="utf-8"))
assert tokens.get("version"), "Design token version missing"
assert (ROOT / "index.html").is_file(), "Reference site missing"
html = (ROOT / "index.html").read_text(encoding="utf-8")
assert 'src="assets/catalogue-data.js"' in html, "Site must load generated canonical catalogue data"
print(json.dumps({"valid": True, "manifest_version": manifest["schema_version"],
                  "assets": len(assets), "icons": len(icons), "svg_symbols": len(symbols),
                  "statuses": {s: sum(a["status"] == s for a in assets) for s in sorted(allowed)},
                  "standalone_icons": sum((ROOT / a["source"]).is_file() for a in icons)}, indent=2))
