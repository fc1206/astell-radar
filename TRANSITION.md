# Astell Radar — Transition / Handoff

_Last updated 2026-06-16. This is the pick-it-up-cold doc: what exists, how it runs, what to touch, what's pending. Pair it with `README.md` (setup) and `CLAUDE.md` (the rules any model running a scan must follow)._

## TL;DR status

| | |
|---|---|
| **State** | Live and autonomous on GitHub Actions |
| **Repo** | `github.com/fc1206/astell-radar` (private, personal account — see Decision log for why not the org) |
| **Model** | **Claude Opus 4.8** via repo variable `SCAN_MODEL` (workflow falls back to Sonnet 4.6 if the var is ever unset) |
| **Schedule** | Mon + Thu 14:00 UTC, `.github/workflows/scan.yml` (+ manual `gh workflow run scan.yml`) |
| **Tracking** | 97 companies as of 2026-06-16 |
| **Delivery** | commit to repo → `data/report.html` (dashboard) + `data/DIGEST.md` (decisions) + Slack digest; GitHub Issue on any new Tier-1 or failed run |
| **Cost** | ~$1–1.50 model + ~$0.25 web-search per run → ~$10–15/month on Opus |
| **Tests** | 15, `pytest` — incl. the Tanderrum regression, digest slop-lint, coverage ledger |

## Why this exists

Built 2026-06-10 after we learned about a competitor (tanderrum.ai) from a cofounder call instead of our own tooling. Goal: never miss a company in or near Astell's lane again. The radar sweeps the market twice a week, maintains a tiered registry, and tells us **what each finding means and what to do** — not just that it exists.

## How a run works

A scan is the `/scan` command (`.claude/commands/scan.md`) run by Claude Code in CI. The design principle throughout: **the model does only narrow judgment; deterministic Python does everything else.** That's what lets it run cheaply and safely on any model.

1. `scripts/plan_run.py` — picks which query blocks to emphasize (rotates so all vocabularies get swept), which companies to re-check, stamps a coverage ledger. Deterministic.
2. **Model: discovery** — ~16 web searches across the rotating + always-on query blocks, pulls out candidate companies.
3. **Model: verify + score** — fetches each candidate's site, scores it against `config/rubric.md` (Tier 1 same lane / 2 adjacent / 3 context).
4. **Model: status sweep** — re-checks ~8 existing companies for funding/acquisition/pivot.
5. `scripts/validate_merge.py` — **sole writer** of `registry.csv`, `SCANLOG.md`, `state.json`, and the `LANDSCAPE.md` changelog. Schema-validates, dedupes by domain, rejects malformed input, fires `ESCALATION.md` on new Tier-1. The model literally cannot corrupt the registry.
6. **Model: digest** — derives `runs/<date>/digest.md` against `config/astell-context.md` under the contract in `config/digest-spec.md`.
7. `scripts/validate_digest.py` — **sole writer** of `data/DIGEST.md`. Slop-linter: rejects uncited claims, banned phrases, and lazy actions ("monitor closely" bounces).
8. `scripts/render_report.py` — regenerates `data/report.html`.
9. Workflow publishes (commit + push), then `scripts/notify_slack.py` posts the digest, then opens a GitHub Issue if a Tier-1 escalated.

## Repo map

- `data/registry.csv` — system of record (the 97 companies).
- `data/LANDSCAPE.md` — narrative map + threat assessment + changelog.
- `data/DIGEST.md` — decisions: what changed, why it matters, what to do. Newest first.
- `data/report.html` — self-contained dashboard (open in a browser; forwardable).
- `data/SCANLOG.md` — append-only audit; every run logs, including zero-find runs.
- `config/queries.md` — the query battery (two lanes: precision + recall safety-net) and its tuning log.
- `config/rubric.md` — tier definitions + calibration examples (Tanderrum is canonical).
- `config/astell-context.md` — **the strategy frame the digest is judged against.**
- `config/digest-spec.md` — the anti-slop digest contract.
- `scripts/` — `plan_run`, `validate_merge`, `validate_digest`, `render_report`, `notify_slack`, `send_report` (email, dormant).
- `tests/` — run `pytest` before changing any script.

## The levers (what to edit to tune)

- **Strategy moved? Edit `config/astell-context.md`.** This is the digest's brain — pillars, standing reads, the five "actionable" lanes. Stale context = stale judgment. Highest-leverage file in the repo.
- **Scoring feels off?** `config/rubric.md`.
- **Queries noisy / missing a cluster?** `config/queries.md` (append a dated line to its tuning log).
- **Model?** `gh variable set SCAN_MODEL --body "..."` — no code change, run `pytest` after.

## Secrets & access (GitHub repo settings)

- `ANTHROPIC_API_KEY` ✓ set — required.
- `SLACK_WEBHOOK_URL` ✓ set — the Slack digest. Webhook points at the channel chosen in api.slack.com/apps.
- `MAIL_USER` set, **`MAIL_PASSWORD` not set** → email delivery (`send_report.py`) is dormant by design. To enable: set a Gmail app password as `MAIL_PASSWORD`.
- `RADAR_TOKEN` not set → CI uses the default token; direct push to `main` works because the personal repo has no branch rules. (If the repo ever moves somewhere with PR rules, set a PAT here and the workflow auto-falls-back to a PR flow.)
- Add cofounder: `gh api -X PUT repos/fc1206/astell-radar/collaborators/USERNAME -f permission=push`.

## Guardrails (do not break)

- **Never hand-edit** `registry.csv`, `SCANLOG.md`, `state.json`, `DIGEST.md`, or the `LANDSCAPE.md` changelog. Only `validate_merge.py` and `validate_digest.py` write them. Hand-edits will be clobbered and break the audit trail.
- **Run `pytest` before pushing any script change.** The Tanderrum regression is the canary — if it fails, a real competitor could be silently dropped.
- **GitHub Actions is the single canonical runner.** See the warning below.

## ⚠ Multi-runner divergence (the 2026-06-16 lesson)

For a while, Cowork "bridge" scheduled tasks ran scans locally in parallel with CI. On 2026-06-15 that produced **two different scans the same day that found different companies** — and a naive "reset to GitHub" reconciliation silently dropped 5 of them, including **Hyperspell, a Tier-1 all-four-pillars clone**. The exact failure this project exists to prevent.

Resolution applied: recovered the union through `validate_merge.py` (not a hand-edit) — registry went 92 → 97, Hyperspell re-escalated. Going forward:

- The two Cowork bridge tasks (`astell-radar-bridge`, `astell-radar-bridge-thu`) are **disabled** — safe to delete. Leave them off so only CI writes.
- If you ever run `/scan` locally, **`git pull` first** and let `validate_merge.py` dedupe; never force a reset that discards a lineage without checking `comm` on the registry domains first.

## Open items

- Email path dormant (`MAIL_PASSWORD` unset) — enable if you want inbox delivery alongside Slack.
- Coverage gap noted in SCANLOG: old-guard enterprise-search incumbents (Mindbreeze, Sinequa) not yet registered — likely Tier-3; add on a dedicated pass.
- A few `watch-unconfirmed` entries await verification on the next scan (e.g. Atolio, Curiosity) — see latest SCANLOG note.
- Workflow uses `actions/checkout@v4` etc. on Node 20 (GitHub deprecation warning) — cosmetic, bump to v5 when convenient.

## Decision log

- **Born** from missing tanderrum.ai (2026-06-10). Tanderrum is the canonical rubric example: same promise, different vocabulary ("data intelligence"), zero press footprint.
- **Repo home: personal, not the org.** The labtwofour enterprise (a) disables workflow-token writes and (b) requires non-author PR approval on every PR — together that makes org-hosted CI unable to self-merge. Transferred to `fc1206` so the radar is autonomous. Moving back means accepting a human merge-click per scan.
- **Runner: bare `claude` CLI, not the GitHub App.** The `claude-code-action` GitHub App wasn't installable on the repo; the workflow installs `@anthropic-ai/claude-code` and runs `claude -p "/scan"` directly.
- **Model: Opus 4.8.** Sonnet is the safe floor and the workflow default; we run Opus because the judgment steps (extraction recall, borderline tier calls, digest sharpness) are where a weak model silently under-delivers, and the cost delta is a few dollars a month.
- **Queries: two-lane battery + coverage ledger** (2026-06-16) — Lane 1 precision (site-targeted, sharpened), Lane 2 recall safety-net (always-on + geographic). The ledger flags any block unswept >18 days so breadth is provable, not assumed.
