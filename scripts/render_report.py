#!/usr/bin/env python3
"""Render data/report.html from the system of record. Deterministic, stdlib-only.

Reads registry.csv, state.json, SCANLOG.md, LANDSCAPE.md. Never written by the
model — this script is the only producer of report.html.

Usage: python3 scripts/render_report.py [--root .] [--out data/report.html]
"""
import argparse
import csv
import html
import json
import re
from datetime import date
from pathlib import Path

import score_axes  # sibling in scripts/; computes the map's breadth × action coordinates

TIER_META = {
    "1": ("T1 · direct lane", "#ff5d5d"),
    "2": ("T2 · adjacent", "#5da9ff"),
    "3": ("T3 · context", "#9aa3ad"),
}
STATUS_BADGE = {"acquired": "#b08cff", "dead": "#6b7280", "feature": "#46c28e"}


def esc(s):
    return html.escape(str(s or ""), quote=True)


def load(root: Path):
    with (root / "data/registry.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    state = json.loads((root / "data/state.json").read_text(encoding="utf-8"))
    scanlog = (root / "data/SCANLOG.md").read_text(encoding="utf-8")
    landscape = (root / "data/LANDSCAPE.md").read_text(encoding="utf-8")
    digest_p = root / "data/DIGEST.md"
    digest = digest_p.read_text(encoding="utf-8") if digest_p.exists() else ""
    return rows, state, scanlog, landscape, digest


def latest_scan_notes(scanlog: str) -> str:
    """Last '## ...' section of the scan log."""
    parts = re.split(r"^## ", scanlog, flags=re.M)
    return ("## " + parts[-1]).strip() if len(parts) > 1 else ""


def threat_top5(landscape: str):
    m = re.search(r"## Threat assessment.*?\n(.*?)\n## ", landscape, re.S)
    if not m:
        return []
    items = re.findall(r"^\d+\.\s+(.*)$", m.group(1), re.M)
    return [re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", esc_keep_strong(i)) for i in items[:5]]


def esc_keep_strong(s: str) -> str:
    """Escape, but allow the ** -> <strong> conversion afterwards."""
    return html.escape(s, quote=False)


def competitive_map_html(rows, root: Path) -> str:
    """Dark-themed 2x2 competitive map: every active Tier-1/2 plotted at its computed
    (breadth x action) position from config/axes.json. Dots are fixed; Tier-1 labels
    offset on leader lines (right-gutter for the dense corner) so nothing drifts. Optional
    — returns '' on any failure rather than breaking the report."""
    try:
        cfg = score_axes.load_config(root, None)
        on = [r for r in rows if r.get("status") == "active" and r.get("tier") in ("1", "2")]
        data = []
        for r in on:
            b, a = score_axes.score_row(r, cfg)
            meta = " · ".join(p for p in [r.get("stage", ""), r.get("hq", ""),
                              (("est. " + r["founded"]) if r.get("founded") not in ("", "unknown") else "")]
                              if p and p != "unknown")
            data.append({"n": esc(r["name"]), "x": b, "y": a, "t": int(r["tier"]),
                         "labeled": r["tier"] == "1", "m": esc(meta), "w": esc((r.get("what", "") or "")[:150])})
        if not data:
            return ""
        data.sort(key=lambda c: c["labeled"])  # labeled paint on top
        xa, ya = cfg["x_axis"], cfg["y_axis"]
    except Exception as e:  # never let the map break the system-of-record report
        return f"<!-- competitive map skipped: {esc(str(e))} -->"

    tmpl = r"""<h2>Competitive map — __XL__ × __YL__</h2>
<style>
.cm{position:relative;height:480px;background:#0d1117;border:1px solid #21262d;border-radius:10px;overflow:hidden;}
.cmq{position:absolute;background:#1b212a;}.cmv{left:50%;top:5%;bottom:9%;width:1px;}.cmh{top:50%;left:6%;right:4%;height:1px;}
.cmax{position:absolute;font-size:9px;letter-spacing:.08em;text-transform:uppercase;color:#6b7280;}
.cmx{left:84px;right:16px;bottom:10px;text-align:center;}.cmy{left:4px;top:50%;transform:translateY(-50%) rotate(-90deg);white-space:nowrap;}
.cmlead{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;}
.cmdot{position:absolute;border-radius:50%;transform:translate(-50%,-50%);cursor:default;}
.cmdot.t1{width:11px;height:11px;background:#ff5d5d;box-shadow:0 0 0 3px rgba(255,93,93,.13);}
.cmdot.t2{width:9px;height:9px;background:#5da9ff;opacity:.85;}
.cmlbl{position:absolute;transform:translate(-50%,-50%);font-size:11px;font-weight:600;white-space:nowrap;color:#e6edf3;background:rgba(13,17,23,.66);padding:1px 4px;border-radius:4px;cursor:default;}
.cmtip{display:none;position:absolute;left:0;top:0;width:194px;background:#161b22;border:1px solid #30363d;border-radius:10px;padding:10px 12px;box-shadow:0 14px 32px -12px rgba(0,0,0,.6);z-index:40;transform:translate(-50%,12px);text-align:left;white-space:normal;}
.cmdot:hover{z-index:30;}.cmdot:hover .cmtip{display:block;}
.cmtn{font-weight:600;font-size:13px;display:flex;align-items:center;gap:6px;}
.cmtc{font-size:10px;font-weight:600;padding:1px 6px;border-radius:5px;}.cmtc.t1{background:#ff5d5d22;color:#ff5d5d;}.cmtc.t2{background:#5da9ff22;color:#5da9ff;}
.cmtm{color:#9aa3ad;font-size:11px;margin:3px 0 5px;}.cmtw{color:#bac3cc;font-size:11.5px;line-height:1.4;}
.cmcap{color:#6b7280;font-size:12px;margin-top:8px;}
</style>
<div class="cm" id="cmap"><div class="cmq cmv"></div><div class="cmq cmh"></div>
<div class="cmax cmx">__XLO__&nbsp;───→&nbsp;__XHI__</div><div class="cmax cmy">__YLO__&nbsp;───→&nbsp;__YHI__</div>
<svg class="cmlead" id="cmlead"></svg></div>
<div class="cmcap">__N__ active Tier-1/2 plotted by <strong>computed</strong> breadth × action (from <code>config/axes.json</code>, never hand-placed). Tier-1 labelled; hover any dot.</div>
<script>(function(){
var DATA=__DATA__,m=document.getElementById('cmap'),svg=document.getElementById('cmlead');
function build(){var W=m.clientWidth,H=m.clientHeight;if(!W)return setTimeout(build,60);var PADX=86,PADY=40;
 var ns=DATA.map(function(d){return {d:d,px:PADX+d.x/100*(W-PADX-20),py:H-PADY-d.y/100*(H-2*PADY)};});
 ns.forEach(function(n){var dot=document.createElement('div');dot.className='cmdot t'+n.d.t;
  dot.style.left=n.px+'px';dot.style.top=n.py+'px';
  dot.innerHTML='<div class="cmtip"><div class="cmtn">'+n.d.n+' <span class="cmtc t'+n.d.t+'">T'+n.d.t+'</span></div><div class="cmtm">'+n.d.m+'</div><div class="cmtw">'+n.d.w+'</div></div>';
  m.appendChild(dot);n.dot=dot;});
 var L=ns.filter(function(n){return n.d.labeled;});
 L.forEach(function(n){var el=document.createElement('div');el.className='cmlbl';el.textContent=n.d.n;m.appendChild(el);n.el=el;n.w=el.offsetWidth;n.h=el.offsetHeight;});
 var GUT=L.filter(function(n){return n.d.x>=78;});       // dense corner -> right gutter
 GUT.forEach(function(g){g.dir=1;g.lx=W-12-g.w/2;g.ly=g.py;});  // anchor at dot height (short lines)
 var NEAR=L.filter(function(n){return n.d.x<78;});
 NEAR.forEach(function(n){n.dir=n.px<W*0.5?-1:1;n.lx=n.px+n.dir*(n.w/2+14);n.ly=n.py;});
 [GUT,NEAR].forEach(function(G){for(var it=0;it<240;it++){     // declutter each group vertically
   for(var i=0;i<G.length;i++)for(var j=i+1;j<G.length;j++){
     var a=G[i],b=G[j],dy=b.ly-a.ly,oy=(a.h/2+b.h/2+7)-Math.abs(dy);
     if(oy>0&&Math.abs(b.lx-a.lx)<(a.w/2+b.w/2+12)){var s=oy/2*(dy<0?-1:1)||oy/2;a.ly-=s;b.ly+=s;}}
   G.forEach(function(n){n.ly=Math.max(n.h/2+6,Math.min(H-n.h/2-26,n.ly));});}});
 var SN='http://www.w3.org/2000/svg';
 L.forEach(function(n){n.el.style.left=n.lx+'px';n.el.style.top=n.ly+'px';
  var ex=n.lx-n.dir*(n.w/2+2),ln=document.createElementNS(SN,'line');
  ln.setAttribute('x1',n.px);ln.setAttribute('y1',n.py);ln.setAttribute('x2',ex);ln.setAttribute('y2',n.ly);
  ln.setAttribute('stroke',n.d.t===1?'rgba(255,93,93,.42)':'rgba(93,169,255,.42)');ln.setAttribute('stroke-width','1');svg.appendChild(ln);
  n.el.addEventListener('mouseenter',function(){var t=n.dot.querySelector('.cmtip');if(t)t.style.display='block';});
  n.el.addEventListener('mouseleave',function(){var t=n.dot.querySelector('.cmtip');if(t)t.style.display='none';});});}
build();})();</script>
"""
    return (tmpl.replace("__DATA__", json.dumps(data, ensure_ascii=False))
            .replace("__XL__", esc(xa["label"])).replace("__YL__", esc(ya["label"]))
            .replace("__XLO__", esc(xa["low"])).replace("__XHI__", esc(xa["high"]))
            .replace("__YLO__", esc(ya["low"])).replace("__YHI__", esc(ya["high"]))
            .replace("__N__", str(len(data))))


def render(root: Path, out: Path):
    rows, state, scanlog, landscape, digest = load(root)
    run_date = state.get("last_run", date.today().isoformat())
    runner = state.get("last_runner", "?")
    tiers = {t: [r for r in rows if r["tier"] == t] for t in ("1", "2", "3")}
    new_rows = [r for r in rows if r.get("first_seen") == run_date]
    if len(new_rows) >= len(rows):  # baseline day: dates can't distinguish — use the changelog's Added list
        m = re.search(r"^### .*? — scan.*?\nAdded: (.*?)$", landscape, re.M | re.S)
        names = set()
        if m:
            names = {n.strip() for n in re.findall(r"([^;]+?) \(T\d", m.group(1))}
        new_rows = [r for r in rows if r["name"] in names]
    new_domains = {r["domain"] for r in new_rows}
    threats = threat_top5(landscape)
    notes = latest_scan_notes(scanlog)
    map_html = competitive_map_html(rows, root)

    digest_html = ""
    dm = re.search(r"^## (\d{4}-\d{2}-\d{2}) — digest.*?(?=^## \d{4}|\Z)", digest, re.M | re.S)
    if dm:
        d = esc(dm.group(0).strip())
        d = re.sub(r"^## (.*)$", r'<div class="dghead">\1</div>', d, count=1, flags=re.M)
        d = re.sub(r"^### (.*)$", r'<div class="dgitem">\1</div>', d, flags=re.M)
        d = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", d)
        d = re.sub(r"(https?://[^\s<)]+)", r'<a href="\1" target="_blank" rel="noopener">\1</a>', d)
        digest_html = d.replace("\n", "<br>")

    def row_html(r):
        label, color = TIER_META.get(r["tier"], ("T?", "#888"))
        status = r.get("status", "")
        sbadge = ""
        if status in STATUS_BADGE:
            sbadge = f'<span class="badge" style="background:{STATUS_BADGE[status]}22;color:{STATUS_BADGE[status]}">{esc(status)}</span>'
        is_new = ' data-new="1"' if r["domain"] in new_domains else ""
        newtag = '<span class="badge new">NEW</span>' if is_new else ""
        ev = esc(r.get("evidence_url", ""))
        return (
            f'<tr data-tier="{esc(r["tier"])}"{is_new}>'
            f'<td><div class="nm">{esc(r["name"])} {newtag}</div>'
            f'<a class="dom" href="https://{esc(r["domain"])}" target="_blank" rel="noopener">{esc(r["domain"])}</a></td>'
            f'<td><span class="badge" style="background:{color}22;color:{color}">{label.split(" ")[0]}</span> {sbadge}</td>'
            f'<td>{esc(r.get("cluster", ""))}</td>'
            f'<td>{esc(r.get("stage", ""))}</td>'
            f'<td>{esc(r.get("hq", ""))}</td>'
            f'<td class="dt">{esc(r.get("first_seen", ""))}</td>'
            f'<td class="what">{esc(r.get("what", ""))}'
            f'<div class="why">{esc(r.get("why_tier", ""))}'
            + (f' · <a href="{ev}" target="_blank" rel="noopener">evidence</a>' if ev.startswith("http") else "")
            + (f'<div class="note">⚠ {esc(r["notes"])}</div>' if r.get("notes") else "")
            + "</div></td></tr>"
        )

    body_rows = "\n".join(row_html(r) for r in sorted(rows, key=lambda r: (r["tier"], r["name"].lower())))

    new_cards = "".join(
        f'<div class="card"><div class="nm">{esc(r["name"])} '
        f'<span class="badge" style="background:{TIER_META[r["tier"]][1]}22;color:{TIER_META[r["tier"]][1]}">T{esc(r["tier"])}</span></div>'
        f'<div class="cl">{esc(r["cluster"])} · {esc(r["stage"])} · {esc(r["hq"])}</div>'
        f'<div class="wt">{esc(r["what"])}</div>'
        f'<div class="why">{esc(r["why_tier"])}</div></div>'
        for r in new_rows
    ) or '<div class="quiet">No net-new companies this run — and that is a verified zero, not an unchecked one.</div>'

    threat_html = "".join(f"<li>{t}</li>" for t in threats)
    notes_html = esc(notes).replace("\n", "<br>")

    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Astell Radar — {esc(run_date)}</title>
<style>
:root {{ color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:#0d1117; color:#e6edf3; font:14px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif; }}
.wrap {{ max-width:1180px; margin:0 auto; padding:32px 20px 80px; }}
h1 {{ font-size:22px; margin:0; letter-spacing:.04em; }}
h1 .accent {{ color:#5da9ff; }}
h2 {{ font-size:15px; text-transform:uppercase; letter-spacing:.08em; color:#9aa3ad; margin:36px 0 12px; }}
.meta {{ color:#9aa3ad; margin-top:6px; }}
.stats {{ display:flex; gap:12px; flex-wrap:wrap; margin-top:18px; }}
.stat {{ background:#161b22; border:1px solid #21262d; border-radius:10px; padding:12px 18px; min-width:110px; }}
.stat b {{ display:block; font-size:22px; }}
.stat span {{ color:#9aa3ad; font-size:12px; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(330px,1fr)); gap:12px; }}
.card {{ background:#161b22; border:1px solid #21262d; border-left:3px solid #5da9ff; border-radius:10px; padding:14px 16px; }}
.card .nm {{ font-weight:600; }}
.card .cl {{ color:#9aa3ad; font-size:12px; margin:4px 0 8px; }}
.card .wt {{ margin-bottom:6px; }}
.card .why {{ color:#9aa3ad; font-size:12.5px; }}
.quiet {{ color:#9aa3ad; background:#161b22; border:1px dashed #21262d; border-radius:10px; padding:16px; }}
ol.threats {{ padding-left:20px; }} ol.threats li {{ margin-bottom:8px; }}
.controls {{ display:flex; gap:10px; flex-wrap:wrap; margin-bottom:12px; }}
input[type=search] {{ flex:1; min-width:220px; background:#161b22; border:1px solid #30363d; border-radius:8px; color:#e6edf3; padding:8px 12px; font-size:14px; }}
button.f {{ background:#161b22; border:1px solid #30363d; border-radius:8px; color:#9aa3ad; padding:7px 14px; cursor:pointer; font-size:13px; }}
button.f.on {{ color:#e6edf3; border-color:#5da9ff; }}
table {{ width:100%; border-collapse:collapse; }}
th {{ text-align:left; color:#9aa3ad; font-size:12px; text-transform:uppercase; letter-spacing:.05em; padding:8px 10px; border-bottom:1px solid #30363d; cursor:pointer; white-space:nowrap; }}
td {{ padding:10px; border-bottom:1px solid #21262d; vertical-align:top; }}
td .nm {{ font-weight:600; }}
a.dom {{ color:#5da9ff; font-size:12px; text-decoration:none; }}
td.what {{ max-width:430px; }}
.why {{ color:#9aa3ad; font-size:12px; margin-top:4px; }}
.why a {{ color:#5da9ff; }}
.note {{ color:#d29922; font-size:12px; margin-top:3px; }}
.dt {{ white-space:nowrap; color:#9aa3ad; font-size:12.5px; }}
.badge {{ display:inline-block; border-radius:20px; padding:2px 9px; font-size:11.5px; font-weight:600; }}
.badge.new {{ background:#23863622; color:#3fb950; border:1px solid #3fb95055; }}
.lognotes {{ background:#161b22; border:1px solid #21262d; border-radius:10px; padding:14px 16px; color:#bac3cc; font-size:13px; }}
.foot {{ margin-top:40px; color:#6b7280; font-size:12px; }}
.foot a {{ color:#5da9ff; }}
@media print {{ body {{ background:#fff; color:#111; }} }}
</style></head><body><div class="wrap">

<h1>ASTELL <span class="accent">RADAR</span></h1>
<div class="meta">Competitive landscape · scan of <b>{esc(run_date)}</b> ({esc(runner)}) · system of record: <code>data/registry.csv</code></div>

<div class="stats">
  <div class="stat"><b>{len(rows)}</b><span>companies tracked</span></div>
  <div class="stat"><b style="color:#ff5d5d">{len(tiers['1'])}</b><span>Tier 1 · direct lane</span></div>
  <div class="stat"><b style="color:#5da9ff">{len(tiers['2'])}</b><span>Tier 2 · adjacent</span></div>
  <div class="stat"><b style="color:#9aa3ad">{len(tiers['3'])}</b><span>Tier 3 · context</span></div>
  <div class="stat"><b style="color:#3fb950">{len(new_rows)}</b><span>new this run</span></div>
</div>

<h2>Decision digest — what it means, what to do</h2>
<div class="lognotes" style="border-left:3px solid #3fb950">{digest_html if digest_html else 'No digest entry for this scan yet — see <code>data/DIGEST.md</code>.'}</div>

<h2>New this run</h2>
<div class="cards">{new_cards}</div>

<h2>Current threat assessment — top 5</h2>
<ol class="threats">{threat_html}</ol>

{map_html}

<h2>Full registry</h2>
<div class="controls">
  <input type="search" id="q" placeholder="Search name, domain, description, cluster…">
  <button class="f on" data-t="all">All</button>
  <button class="f" data-t="1">Tier 1</button>
  <button class="f" data-t="2">Tier 2</button>
  <button class="f" data-t="3">Tier 3</button>
  <button class="f" data-t="new">New</button>
</div>
<table id="reg"><thead><tr>
<th>Company</th><th>Tier</th><th>Cluster</th><th>Stage</th><th>HQ</th><th>First seen</th><th>What / why it matters</th>
</tr></thead><tbody>
{body_rows}
</tbody></table>

<h2>Latest scan log</h2>
<div class="lognotes">{notes_html}</div>

<div class="foot">Generated by <code>scripts/render_report.py</code> — deterministic render of the registry; the model never writes this file.
Repo: <a href="https://github.com/fc1206/astell-radar">fc1206/astell-radar</a> · Narrative map: <code>data/LANDSCAPE.md</code> · Audit: <code>data/SCANLOG.md</code></div>

</div>
<script>
(function() {{
  var q = document.getElementById('q'), rows = Array.prototype.slice.call(document.querySelectorAll('#reg tbody tr'));
  var mode = 'all';
  function apply() {{
    var t = (q.value || '').toLowerCase();
    rows.forEach(function(r) {{
      var okMode = mode === 'all' || (mode === 'new' ? r.hasAttribute('data-new') : r.getAttribute('data-tier') === mode);
      var okText = !t || r.textContent.toLowerCase().indexOf(t) !== -1;
      r.style.display = (okMode && okText) ? '' : 'none';
    }});
  }}
  q.addEventListener('input', apply);
  document.querySelectorAll('button.f').forEach(function(b) {{
    b.addEventListener('click', function() {{
      document.querySelectorAll('button.f').forEach(function(x) {{ x.classList.remove('on'); }});
      b.classList.add('on'); mode = b.getAttribute('data-t'); apply();
    }});
  }});
}})();
</script>
</body></html>"""
    out.write_text(doc, encoding="utf-8")
    print(f"report.html: {len(rows)} rows, {len(new_rows)} new, {len(threats)} threats → {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    root = Path(a.root)
    out = Path(a.out) if a.out else root / "data/report.html"
    render(root, out)


if __name__ == "__main__":
    main()
