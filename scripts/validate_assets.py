#!/usr/bin/env python3
"""Dependency-free integrity checks for the RevenueFlow visual asset library."""
from __future__ import annotations
import json
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "assets/manifest.json").read_text(encoding="utf-8"))
assets = manifest.get("assets", [])
ids = [a.get("id") for a in assets]
assert len(ids) == len(set(ids)), "Duplicate stable asset IDs"
assert all(a.get("category") in manifest.get("categories", []) for a in assets), "Unknown asset category"
assert all(a.get("name") and a.get("source") and a.get("accessibility") for a in assets), "Asset missing required metadata"
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
match = re.search(r"window\\.RF_CATALOGUE = (\\{[\\s\\S]*\\});\\s*$", catalogue_text)
assert match, "Generated catalogue JS has invalid wrapper"
catalogue = json.loads(match.group(1))
def expected(prefix):
    return [[a["id"], a["name"], a["category"], a.get("symbol", ""),
             ", ".join(a.get("keywords", [])), a["status"], a["source"]]
            for a in assets if a["id"].startswith(prefix)]
assert catalogue["icons"] == expected("RF-ICO-"), "Website icon data is stale"
assert catalogue["motions"] == expected("RF-MOT-"), "Website motion data is stale"
assert catalogue["illustrations"] == expected("RF-ILL-"), "Website illustration data is stale"
assert set(catalogue["iconSvg"]) == {a["symbol"] for a in icons}, "Website SVG export map is incomplete"
for a in icons:
    assert catalogue["iconSvg"][a["symbol"]] == (ROOT / a["source"]).read_text(encoding="utf-8").strip(), f"Stale icon preview: {a['id']}"
illustrations = [a for a in assets if a["id"].startswith("RF-ILL-")]
for a in illustrations:
    path = ROOT / a["source"]
    assert path.is_file(), f"Missing illustration artwork: {a['source']}"
    ET.parse(path)
assert set(catalogue["illustrationSvg"]) == {a["symbol"] for a in illustrations}, "Website illustration export map is incomplete"
for a in illustrations:
    assert catalogue["illustrationSvg"][a["symbol"]] == (ROOT / a["source"]).read_text(encoding="utf-8").strip(), f"Stale illustration preview: {a['id']}"
html = (ROOT / "index.html").read_text(encoding="utf-8")
assert 'src="assets/catalogue-data.js"' in html, "Website does not load canonical catalogue data"
assert "const categories=" in html, "Website category navigation is not initialised"
node = shutil.which("node")
if node:
    scripts = re.findall(r"<script(?:\\s[^>]*)?>([\\s\\S]*?)</script>", html)
    inline_scripts = [script for script in scripts if script.strip()]
    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as handle:
        handle.write("\\n".join(inline_scripts))
        temp_path = handle.name
    try:
        subprocess.run([node, "--check", temp_path], check=True, capture_output=True, text=True)
    finally:
        Path(temp_path).unlink(missing_ok=True)
css = (ROOT / "assets/motion.css").read_text(encoding="utf-8").replace(" ", "")
assert "@media(prefers-reduced-motion:reduce)" in css, "Reduced-motion fallback is missing"
for selector in (".rf-spinner", ".rf-ai-pulse", ".rf-skeleton", ".rf-orbit", ".rf-progress", ".rf-success", ".rf-bell-ring", ".rf-soft-glow", ".rf-ecosystem-loader", ".rf-ecosystem-loader__orbit", ".rf-ecosystem-loader__module"):
    assert selector in css, f"Missing motion reference: {selector}"
assert ".rf-ecosystem-loader__core" not in css, "Ecosystem loader must keep its centre empty"
assert "rf-ecosystem-loader__core" not in html, "Ecosystem loader preview must not contain a centre logo"
assert "ecosystem-showcase__stage" in html and "rf-ecosystem-loader--showcase" in html, "Large bottom ecosystem preview is missing"
orbit_nodes = re.findall(r'rf-ecosystem-loader__orbit--[a-f](?=["\\s])', html)
module_nodes = re.findall(r'rf-ecosystem-loader__module--(brain|radar|network|memory|discovery|orchestration)(?=["\\s])', html)
assert len(orbit_nodes) == 6, "Ecosystem preview must contain six independent orbital paths"
assert len(module_nodes) == 6 and set(module_nodes) == {"brain", "radar", "network", "memory", "discovery", "orchestration"}, "Ecosystem preview capability nodes are incomplete"
for suffix in "abcdef":
    assert f"@keyframesrf-ecosystem-orbit-{suffix}" in css, f"Missing 3D orbital animation {suffix}"
assert "Brain·Radar·Network·Memory·Discovery·Orchestration" in html.replace(" ", ""), "Ecosystem capability labels are missing"
json.loads((ROOT / "tokens/design-tokens.json").read_text(encoding="utf-8"))
print(json.dumps({"valid": True, "manifest_version": manifest["schema_version"],
                  "assets": len(assets), "icons": len(icons), "svg_symbols": len(symbols),
                  "standalone_icons": len([a for a in icons if (ROOT / a["source"]).is_file()]),
                  "statuses": {s: sum(a["status"] == s for a in assets) for s in sorted(allowed)}}, indent=2))
