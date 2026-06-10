# astell-radar

Competitive-landscape radar for Astell (astell.space). Runs `/scan` twice a week to catch every new or repositioning competitor. Built to be executed by ANY Claude model — all judgment is narrowly scoped, all plumbing is deterministic.

## Hard rules (non-negotiable, any model)

1. **Never hand-edit** `data/registry.csv`, `data/SCANLOG.md`, `data/state.json`, `data/DIGEST.md`, or the changelog in `data/LANDSCAPE.md`. The only writers are `scripts/validate_merge.py` (registry/scanlog/state/changelog) and `scripts/validate_digest.py` (digest). You write `runs/<date>/*` files; the scripts do the rest.
2. **Every company needs a live evidence URL.** No URL, no entry. If a company looks real but you can't verify (site empty/JS-only), note it in `run_meta.json` notes as `watch-unconfirmed: <name> <domain>` instead of adding it.
3. **Every run logs**, even with zero findings. Zero is signal.
4. **When torn between tiers, pick the higher.** A false positive costs a minute; a miss costs what Tanderrum cost (see `config/rubric.md`).
5. **Do not message anyone or call external services** beyond WebSearch/WebFetch. Delivery is files + git only.
6. If `validate_merge.py` fails, fix your JSON per its error messages and re-run it. Max 2 retries; if still failing, write the errors to `runs/<date>/FAILED.md` and stop.

## Output schemas

`runs/<date>/candidates.json` — array of:
```json
{"name": "", "domain": "", "tier": "1|2|3", "cluster": "direct|chief-of-staff|data-intel|incumbent|employee-assist|infra|vertical", "status": "active|acquired|dead|feature", "stage": "stealth|bootstrapped|seed|series-a|series-b|series-c|late-stage|public|acquired|dead", "hq": "City, CC", "founded": "YYYY|unknown", "what": "one factual line", "why_tier": "one line vs rubric", "evidence_url": "https://...", "notes": "optional; verification caveats"}
```

`runs/<date>/status_updates.json` — array of (only for MATERIAL changes to existing registry rows — funding round, acquisition, shutdown, pivot toward/away from Astell's lane):
```json
{"domain": "existing.com", "fields_changed": {"stage": "...", "status": "...", "tier": "...", "what": "...", "notes": "..."}, "change_summary": "one line", "evidence_url": "https://..."}
```

`runs/<date>/run_meta.json`:
```json
{"runner": "github|cowork|local", "emphasized_blocks": ["A", "B"], "queries_run": ["..."], "candidates_evaluated": 0, "notes": "optional"}
```

`runs/<date>/digest.md` — markdown per `config/digest-spec.md` (0–5 cited, actionable items derived against `config/astell-context.md`, or the NO ACTIONABLE SIGNAL sentinel). Validated and prepended to `data/DIGEST.md` by `scripts/validate_digest.py`.

## Key files

- `config/queries.md` — query battery (edit to tune; append lessons to its tuning log)
- `config/rubric.md` — tier definitions + calibration examples (Tanderrum is canonical)
- `config/astell-context.md` — strategy frame the digest is judged against (Frank-editable)
- `config/digest-spec.md` — the anti-slop digest contract
- `data/registry.csv` — system of record, append-mostly
- `data/LANDSCAPE.md` — narrative map + changelog
- `.claude/commands/scan.md` — the run procedure
