# astell-radar

Autonomous competitive-landscape radar for [Astell](https://astell.space). Scans the market twice a week (Mon + Thu), maintains a registry of every company in or near Astell's lane, and opens a GitHub Issue the moment a new Tier-1 competitor appears. Born 2026-06-10, the day we found out about tanderrum.ai from a cofounder call instead of from our own tooling.

## How it works

A scan = the `/scan` slash command executed by Claude Code. The LLM does exactly two judgment tasks — extract candidate companies from web searches, and score them against `config/rubric.md`. Everything else is deterministic Python (`scripts/`): query-block rotation, status-sweep round-robin, schema validation, domain-normalized dedupe, registry merge, changelog, escalation. The model writes `runs/<date>/*.json`; `validate_merge.py` is the only writer of the system of record and rejects anything malformed. That separation is what makes the harness model-agnostic: run it on Sonnet for pennies, the registry can't be corrupted either way.

- `data/registry.csv` — system of record (seeded with a 73-company baseline)
- `data/LANDSCAPE.md` — narrative map, threat assessment, changelog
- `data/SCANLOG.md` — append-only audit trail; zero-find runs log too
- `config/queries.md` — the query battery, multi-vocabulary by design (the Tanderrum lesson); has its own tuning log
- `config/rubric.md` — tier definitions with calibration examples
- `tests/` — plumbing tests + the **Tanderrum regression fixture**: a low-footprint, adjacent-vocabulary company must merge cleanly. Changing models or prompts? `pytest` first.

## Setup (one time, ~2 minutes)

Lives at `fc1206/astell-radar` (personal account, deliberately: the labtwofour org/enterprise requires non-author PR approvals, which breaks autonomous merging — moving the repo back means accepting a human click per scan). Secrets: `ANTHROPIC_API_KEY`; model via repo variable `SCAN_MODEL`. The publish step pushes straight to main and automatically falls back to a PR if branch rules ever block direct pushes.

Then watch the repo (Watch → All activity) so Tier-1 escalation issues hit your inbox.

**Org-rule compatibility:** the labtwofour org requires changes via pull request, so each scan pushes a `scan/<date>` branch and opens a PR, then squash-merges it automatically if the ruleset allows (no required reviews) — otherwise the PR waits for your one-click merge; merge promptly to keep scans linear. This requires the repo Actions setting "Allow GitHub Actions to create and approve pull requests":

```bash
gh api -X PUT repos/labtwofour/astell-radar/actions/permissions/workflow -f default_workflow_permissions=write -F can_approve_pull_request_reviews=true
```

## Schedule + model

`.github/workflows/scan.yml` runs Mon/Thu 14:00 UTC (adjust the cron to taste). Model defaults to **Sonnet** — set a repo variable `SCAN_MODEL` (e.g. `claude-opus-4-8`) to change it without touching code. If the action's input names drift, check the [claude-code-action docs](https://github.com/anthropics/claude-code-action).

Manual run anytime: Actions → scan → Run workflow. Locally: `claude` in this directory, then `/scan`.

## Bridge mode

Until this repo is pushed + the secret is set, a Cowork scheduled task runs `/scan` locally on the same cadence and commits to the local git history. It checks `data/state.json` first and stands down automatically once it sees a `github` run within the last 4 days — no dual-writer drift. Delete the Cowork task once Actions is confirmed running.

## Changing the methodology

Queries → `config/queries.md`. Scoring → `config/rubric.md`. Procedure → `.claude/commands/scan.md`. Plumbing → `scripts/` (run `pytest` after). Every scan is a commit, so `git log -- data/registry.csv` answers "when did we learn about X?"
