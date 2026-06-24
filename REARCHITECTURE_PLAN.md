# Astell Radar — Re-architecture Plan (v2)

**Goal:** keep evolving the radar from a curated ~100-company watchlist into a deeper, more trustworthy internal competitive-intelligence database — **without** regressing the working system underneath it.

**North Star (revised):** the measure of success is **zero Tanderrum-class misses + real depth on the companies that matter**, *not* a raw count. "500+" is a side effect of better recall, never the objective. Volume on its own dilutes the digest and multiplies the staleness burden.

**Decided (Frank, 2026-06-22):** internal intel use · fix data quality + recall + add per-company depth.

> **v2 changes (2026-06-23, after a first-principles review + independent codex review + a 16-agent verification pass):**
> - **Re-sequenced.** Recall and reliability come *first* — they're the mission and they don't depend on the data-model migration. The migration moves to its own track, pulled forward only by *depth* (which genuinely needs it).
> - **Corrected several premises that didn't survive contact with the code/data** (see "Reality check" below). The system is already a clean staged pipeline, dedupe-on-write already exists, Tier-1 is the *largest* tier, the `tacnode.com vs .io` dupe doesn't exist, and the parallel-run divergence is a *process* problem, not a storage-format one.
> - **Split the losslessness gate** into a provable format-only step and a separate reviewed dedupe step.
> - **A live incident was found during review** (see "Incident 2026-06-23"): the cowork bridge is still running and has re-created the exact divergence this project fears. That moves reliability to the top.

---

## Reality check — premises corrected against the actual repo

The v1 plan argued against an older, messier system than the one that actually exists. Verified against the code and all 103 rows:

| v1 said | Reality |
|---|---|
| Stages are "tangled in one LLM pass." | **False.** The pipeline is already staged: `plan_run.py` (deterministic) → discover (LLM) → verify+score (LLM) → `validate_merge.py` (deterministic, sole writer) → digest (LLM) → `render_report.py` (deterministic). The LLM does only *find + score*. The one true gap is there's no **depth/enrich** stage yet. |
| "Enforce canonical-domain dedupe on every write." | **Already done** for exact domains (`validate_merge.py` normalizes + rejects dupes, with a test). The only new work is **cross-TLD / same-company** merging — which has **zero instances** in the current data. |
| Enrich "Tier-1 (highest value, fewest)." | **Backwards.** Tier-1 = 32 (the largest single tier), Tier-2 = 51, Tier-3 = 20. Enriching Tier-1 = enriching ~31% of the registry. ("Highest value" is fair; "fewest" is wrong.) |
| Dedupe motivated by "tacnode.com vs .io." | **No such dupe exists.** Only `tacnode.io` is in the registry. Use a synthetic fixture to test dedupe, not this example. |
| Per-entity files "eliminate parallel-run merge divergence." | **Divergence is a process problem, not a format one.** It is caused by two runners both writing (see Incident 2026-06-23). CI already serializes its own runs (`concurrency:` in `scan.yml`). Per-file JSON would not fix the live cause; a single canonical writer does. |
| Runtime can take a JSON-Schema dependency freely. | The runtime is **stdlib-only** by design (the scheduled scan runs on bare `python3`). There is **no `requirements.txt`**; a fresh clone has neither `pytest` nor `jsonschema`. Any dependency must be pinned and installed in both workflows, or the live scan breaks. |

None of these are fatal — but they mean v1's Phase 2 was largely redundant, Phase 4's scoping was wrong, and the migration's headline risk (dupes) isn't present today.

## Principles (hold these every phase)
1. **Verify premises against the code and data before building for them.** (New — this is why v2 exists.)
2. **Incremental, never big-bang.** Each phase ships a working, tested system and is independently revertible. The radar stays live throughout.
3. **Schema-first** — the entity contract is written and reviewed before any code reads/writes entities. **One source of truth** for validation: do not run a JSON-Schema validator *and* the hand-rolled `validate_merge.py` checks in parallel; pick one and generate or test the other from it.
4. **Prove losslessness as a *format-only* step** (byte-identical, no dedupe), then dedupe separately with a reviewed diff. (See Track D, D1.)
5. **Tests are the safety net for an LLM-driven refactor.** Every phase extends `tests/`. CI green is the gate to merge — which first requires a reproducible test env (a pinned `requirements.txt`, installed in both workflows).
6. **Preserve what's good:** deterministic rendering (`render_report.py`), per-run audit trails (`runs/`), the sole-writer guarantee, merge validation, the rubric, the two-lane query battery + coverage ledger.
7. **Don't over-build.** ~500 entities need JSON-files-in-git or SQLite, not Postgres. Model depth at the altitude the render + digest actually consume (flat scalars first); add nested structures only when something reads them.

---

## Two tracks (the key structural change)

v1 ran one linear chain `0→1→2→3→4→5` that gated the mission (recall) behind a storage refactor. v2 splits the work into two tracks that run **in parallel**, because they have no real dependency on each other:

- **Track M — Mission (recall + reliability + trust).** Delivers competitive-intel value against **today's** CSV pipeline. Needs no schema and no migration. **Start here.**
- **Track D — Data model (schema → migration → depth).** The only track that genuinely needs entities, because depth fields (funding-round histories, customer lists) are nested/multi-valued and cannot live in a CSV cell. Pulled forward by depth, not by recall.

The single rule connecting them: **recall does not wait for the migration; depth does.**

---

## Incident 2026-06-23 — the divergence is live again (do this first)

During the review, comparing the local clone to GitHub `main` showed the **exact failure this project exists to prevent**, recurring:

- Local `main` and `origin/main` have **diverged** (2 commits each side from a common ancestor).
- The **cowork bridge is still running** (despite `TRANSITION.md` saying it was disabled): local commits `scan: 2026-06-18 (cowork bridge)` and `scan: 2026-06-22 (cowork bridge)` exist only locally; CI ran its own `(github)` scans the same days.
- **6 companies are split across the two lineages** (a count check would miss it — both are 103 rows):
  - local-only: `agent.nexus`, `tacnode.io`, `zaro.ai`
  - origin-only: `eesel.ai`, `knowi.com`, `relevanceai.com`
- A naive `git reset --hard origin/main` (the move that dropped Hyperspell on 2026-06-16) would silently delete the first three.

**Immediate actions (M0, before anything else):**
1. **Reconcile via validated union, never a reset** — feed the 3 local-only companies through `validate_merge.py` into the canonical (github) lineage so all 6 survive; mirror the divergent `config/queries.md` tuning-log entries by hand-merge (config is not registry). Push the union to `main`.
2. **Actually disable the cowork bridge** — find and remove the scheduled task on the local machine. The guardrail in `TRANSITION.md` was decorative; make it real. One canonical writer (CI), full stop.
3. Only then start M1/M2.

This incident is the argument for putting reliability first: the radar was silently running two divergent lineages for ~8 days and nothing flagged it.

---

## Track M — Mission (do first)

### M1 — Reliability you can't fake (cheap, depends on nothing)
**Goal:** a radar that stops, stalls, or silently degrades is *loud*. Today `scan.yml` already opens an issue on an in-job crash (`if: failure()`) and on a new Tier-1 — so the gap is **not** "no alerting." The real, unmet gaps:

- **The run never fires.** GitHub auto-disables a `schedule` after ~60 days of repo inactivity, and the repo's only activity is its own scans — a quiet stretch can kill the cron. A job that never starts can't alert on itself. → **external dead-man switch**: ping a monitor (e.g. Healthchecks.io) on every success; the monitor alarms when a ping is overdue. (`scripts/heartbeat.py`, env-gated like the email path.)
- **The run exits 0 but did nothing** (e.g. wrote `FAILED.md`, or zero candidates evaluated). Indistinguishable from a legitimately quiet week. → **deterministic post-run health check**: assert today's run dir exists, `state.last_run == today`, `queries_run` non-empty, no `FAILED.md`. Fail the workflow loudly otherwise. (`scripts/check_run_health.py`.)
- **Two writers diverge** (Incident above). → enforce single-writer; add a CI step that refuses to commit a scan if local `main` is behind `origin/main`.

**Done when:** a skipped run, a degraded exit-0 run, and a divergence each produce a visible alert; both new scripts have tests; CI runs the health check as a gate.

### M2 — Recall (break the keyword ceiling — the founding mission)
**Goal:** stop missing companies that don't use the searched vocabulary (the Tanderrum class). This feeds the **existing** `candidates.json → validate_merge.py` path — **no schema or migration required.**

The battery already has strong recall channels (Block F vs/alternatives + ego; Block H geographic; the coverage ledger). What's genuinely missing is **edge-expansion harvesting**:
- **Compare-list directories** (G2 / Capterra / SourceForge "compare" and "alternatives to X" pages) enumerate competitor *sets*, not one-vs-one. New channel.
- **Systematic per-Tier-1 `/alternatives` and `/vs` page harvest** — formalize the ad-hoc technique the tuning log already discovered (Knowlee, Nexus came off their own `/blog/X-alternatives` pages) so it runs every cycle, not by luck.
- Later, if needed: accelerator batch lists (beyond the YC query already in Block G) and named investor-portfolio feeds.

**Recall regression — be honest about what's testable:**
- *Deterministic (CI):* guard that the recall-critical channels still exist in the battery and are rotated — Block F (always-on, alternatives/vs), Block H (non-US), Block B (data-intelligence vocab, the Tanderrum class), and the new edge-expansion block. Removing any silently re-opens a known miss class. (`tests/test_recall.py`.)
- *Live (periodic, not CI):* the true "remove a known hard case and prove discovery re-finds it" test requires live web search; run it as a documented periodic integration check, not a unit test. State this plainly — a green CI does not by itself prove recall.

**Done when:** a scan ingests candidates from the edge-expansion channel; `test_recall.py` guards the channel set; the live recall check is documented and run once.

### M3 — Trust the count (fold in; most of it already exists)
**Goal:** official counts are trustworthy and stale data is visible.
- Exact-domain dedupe on write is **already enforced + tested** — keep it; the only new work is **cross-TLD / same-company** merge (drive it with a synthetic fixture, since the live data has none).
- Lifecycle/quarantine: the evidence-URL hard rule already keeps unverifiable companies *out* of the registry, so counts are already clean. If a quarantine state is still wanted, add it as a **separate axis from `status`** and name it to avoid overlap — call it `confidence` / `verification` (`verified | candidate | unconfirmed`), not `state` (which collides with `status`'s `acquired`/`dead`).
- **Staleness:** `scripts/check_staleness.py` flags entities whose `last_checked` exceeds a threshold (e.g. 90 days) → a re-verify queue. Reads today's CSV; needs no migration.

**Done when:** staleness report runs in CI; cross-TLD dedupe has a fixture test; (optional) a `confidence` axis is added without colliding with `status`.

---

## Track D — Data model (parallel; pulled by depth, not recall)

### D0 — The entity contract + a reproducible test env
- Write `schema/company.schema.json`. Model the existing 14 fields **plus flat depth scalars first** (`latest_funding_stage`, `total_raised`, `headcount`, `top_customers` as text, `key_integrations` as text) and per-field `verified_at` only where freshness matters. Defer nested funding-round arrays / per-element provenance until a consumer (render or digest) actually reads them.
- **One source of truth:** either keep the hand-rolled checks (extend them for the new fields) *or* adopt JSON Schema and generate/replace the hand-rolled checks from it — not both by hand. If JSON Schema is chosen: add a **pinned `requirements.txt`** (`jsonschema==<exact>`) and install it in **both** `scan.yml` and `test.yml`, or the live scan breaks.
- **Add a `render_report.py` test now** (it currently has zero coverage and is about to become a load-bearing render target): render the seed fixtures and assert tier counts in the stat cards, the NEW badge, and digest rendering.

**Done when:** schema reviewed by Frank/Kevin; one validator path; `requirements.txt` exists and both workflows install it; `render_report.py` has a smoke test; `pytest` green.

### D1 — Migrate to entities, prove losslessness (split into two provable steps)
- **D1a — format only, byte-identical.** Explode `registry.csv` 1:1 into one validated JSON per domain (no dedupe), render back to CSV, and assert **true byte-identity** against the pre-migration file. Pin the CSV dialect first (line terminator, `QUOTE_MINIMAL`, exact `FIELDNAMES` order, UTF-8, trailing newline) — byte-identity depends on these and ~96/103 rows contain embedded commas/quotes.
- **D1b — dedupe, separate + reviewed.** Run cross-TLD/same-company resolution as its own pass that **prints every proposed merge for human review** and expects a *changed* row count. Never fold this into D1a's gate ("byte-identical modulo dedupe" is self-contradictory).
- **Migrate the `notes` field, don't drop it** — it already holds informal provenance ("unverified", "watch-unconfirmed"); parse it into the new fields.
- Point `render_report.py` at the regenerated CSV first (minimal diff), then at entities.
- **Rollback:** keep regenerating + round-trip-asserting `registry.csv` from entities for N runs (a dual-write bake) so the CSV stays a continuously-validated fallback before the old path is retired.

**Done when:** D1a byte-identity holds in CI; D1b merges reviewed; round-trip test in CI; dual-write bake running.

### D2 — Depth (enrichment) — cheap source first
- **Source decision (corrected):** the default should be the **already-connected Apollo enrichment** (`apollo_organizations_bulk_enrich`) — it returns funding/headcount/revenue/location with provenance for ~cents/company (~32 credits for all of Tier-1, one-time). Reserve Crunchbase/PitchBook (thousands/yr) only if a field Apollo lacks proves essential. This is an internal $10–15/month tool; match the source to that.
- `scripts/enrich.py`: populate the **flat** depth fields per entity with `source` + `verified_at`, Tier-1 first (note: that's 32 companies, not a handful — batch accordingly), then outward.

**Done when:** Tier-1 carries flat funding/headcount/customers/integrations with stamped provenance, sourced from Apollo.

---

## Suggested order
1. **M0** — reconcile the live divergence (validated union) + actually disable the cowork bridge. *(now)*
2. **M1** — heartbeat + post-run health check + single-writer guard. *(now; protects everything that follows)*
3. **M2** — edge-expansion recall channel + recall-channel guard test. *(the founding mission)*
4. **D0/D1a** in parallel on the data-model track — schema, `requirements.txt`, `render_report` test, byte-identical format migration. *(while the registry is small)*
5. **M3** staleness + **D1b** reviewed dedupe + **D2** Apollo depth. *(value + cleanup)*

Tracks M and D run concurrently; M is never blocked by D.

## How to run this via Claude Code
- **One phase = one Claude Code session = one PR.** Paste the phase goal; let it implement + test; review the diff; merge when CI is green.
- **Update `CLAUDE.md` as structure changes** so future runs have correct context.
- **The byte-identity gate in D1a is non-negotiable** — do not retire the old CSV until the format round-trip is byte-identical and the dual-write bake has run clean.
- **Never reconcile divergent lineages with a reset** — always union through `validate_merge.py` (the Hyperspell lesson, reconfirmed 2026-06-23).
