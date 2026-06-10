#!/usr/bin/env python3
"""Emit this run's plan as JSON: emphasized query blocks, status-sweep targets,
and the set of known domains. Pure function of state.json + queries.md + registry.csv.
Does NOT mutate state — validate_merge.py advances cursors only after a successful merge,
so a failed run safely repeats the same plan.

Usage: python scripts/plan_run.py [--root .]
"""
import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

ALWAYS_BLOCK = "F"


def load_blocks(queries_md: Path):
    """Parse block IDs from '## Block X:' headers, in file order."""
    ids = re.findall(r"^## Block ([A-Z]):", queries_md.read_text(encoding="utf-8"), re.M)
    if not ids:
        sys.exit("ERROR: no '## Block X:' headers found in config/queries.md")
    return ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="repo root")
    args = ap.parse_args()
    root = Path(args.root)

    state = json.loads((root / "data/state.json").read_text(encoding="utf-8"))
    blocks = load_blocks(root / "config/queries.md")
    rotating = [b for b in blocks if b != ALWAYS_BLOCK]

    n = state.get("emphasis_per_run", 2)
    cur = state.get("block_cursor", 0) % len(rotating)
    emphasized = [rotating[(cur + i) % len(rotating)] for i in range(n)]

    with (root / "data/registry.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    known_domains = sorted({r["domain"].strip().lower() for r in rows if r.get("domain")})

    # Status sweep: round-robin over registry rows, skipping dead companies.
    sweepable = [r for r in rows if r.get("status") != "dead"]
    batch = state.get("status_batch", 8)
    scur = state.get("status_cursor", 0) % max(len(sweepable), 1)
    targets = [
        {
            "domain": sweepable[(scur + i) % len(sweepable)]["domain"],
            "name": sweepable[(scur + i) % len(sweepable)]["name"],
            "tier": sweepable[(scur + i) % len(sweepable)]["tier"],
        }
        for i in range(min(batch, len(sweepable)))
    ]

    print(json.dumps({
        "run_date": date.today().isoformat(),
        "always_block": ALWAYS_BLOCK,
        "emphasized_blocks": emphasized,
        "status_targets": targets,
        "registry_size": len(rows),
        "known_domains": known_domains,
    }, indent=2))


if __name__ == "__main__":
    main()
