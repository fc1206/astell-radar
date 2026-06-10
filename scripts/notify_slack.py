#!/usr/bin/env python3
"""Post the scan digest to Slack via incoming webhook. Stdlib-only.

Env: SLACK_WEBHOOK_URL (required to send; exits 0 quietly if unset).
Usage: python3 scripts/notify_slack.py [--dry-run]
"""
import csv
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

REPORT_URL = "https://github.com/fc1206/astell-radar/blob/main/data/report.html"
LANDSCAPE_URL = "https://github.com/fc1206/astell-radar/blob/main/data/LANDSCAPE.md"


def build_message(root: Path) -> str:
    state = json.loads((root / "data/state.json").read_text(encoding="utf-8"))
    run_date = state.get("last_run", "?")
    with (root / "data/registry.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    new = [r for r in rows if r.get("first_seen") == run_date]
    if len(new) >= len(rows):  # baseline-day ambiguity: derive from latest changelog Added list
        land = (root / "data/LANDSCAPE.md").read_text(encoding="utf-8")
        m = re.search(r"^### .*? — scan.*?\nAdded: (.*?)$", land, re.M | re.S)
        names = {n.strip() for n in re.findall(r"([^;]+?) \(T\d", m.group(1))} if m else set()
        new = [r for r in rows if r["name"] in names]
    esc_file = root / "runs" / run_date / "ESCALATION.md"

    lines = [f":satellite_antenna: *Astell Radar — scan {run_date}*"]
    lines.append(f"+{len(new)} new · {len(rows)} tracked")
    if esc_file.exists():
        lines.insert(0, ":rotating_light: *NEW TIER-1 COMPETITOR DETECTED*")
        for ln in esc_file.read_text(encoding="utf-8").splitlines():
            if ln.startswith("## "):
                lines.append("> " + ln[3:])
    for r in new[:8]:
        what = r.get("what", "")
        what = what if len(what) <= 140 else what[:137] + "…"
        lines.append(f"• *{r['name']}* (T{r['tier']}, {r['cluster']}, {r.get('stage', '?')}) — {what}")
    if len(new) > 8:
        lines.append(f"…and {len(new) - 8} more.")
    if not new and not esc_file.exists():
        lines.append("No net-new companies — verified zero (see scan log for queries run).")
    lines.append(f"<{REPORT_URL}|Full HTML report> · <{LANDSCAPE_URL}|Landscape map>")
    return "\n".join(lines)


def main():
    dry = "--dry-run" in sys.argv
    hook = os.environ.get("SLACK_WEBHOOK_URL", "")
    text = build_message(Path("."))
    if dry:
        print(text)
        return
    if not hook:
        print("SLACK_WEBHOOK_URL not set — skipping Slack notify.")
        return
    req = urllib.request.Request(
        hook,
        data=json.dumps({"text": text}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        print(f"Slack notify: HTTP {resp.status}")


if __name__ == "__main__":
    main()
