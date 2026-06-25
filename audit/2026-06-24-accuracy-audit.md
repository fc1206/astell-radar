# Radar accuracy audit — 2026-06-24

**Question (Frank):** how accurate is the information the radar has actually pulled?
**Method:** live, per-field re-verification against primary sources by an independent agent fleet (76 agents, two-pass adversarial: verify → independent recheck). Plus a code/process review of the ingest + validation + re-verification mechanism.
**Coverage:** 66 of 106 rows verified against live sources — the **56 active-startup rows** (the volatile cohort where errors live) + **10** from the earlier demo-facts pass. The unaudited 40 are incumbents / acquired / public-mega (static facts, low risk).

---

## Headline

**The engine guarantees well-formed data, not true data.** It is reliable at the job it was built for — *finding* competitors, *describing* what they do, and *tiering* the threat — and unreliable at the structured metadata nobody re-checks after capture (founding year, stage label, funding round, HQ).

- **0% of audited companies were fake or unverifiable.** Every row is a real company in the lane. Recall/identity is sound (one wrong-entity case: Cora).
- **But only 21% of audited rows are fully clean.** 36% have a *material* (load-bearing) error; an independent recheck confirmed 19 of those 20.

## Scorecard

| Row-level (n=56) | Count | % |
|---|---|---|
| Fully accurate | 12 | 21% |
| Minor drift (cosmetic) | 24 | 43% |
| **Material drift (a load-bearing fact wrong)** | **20** | **36%** |
| Unverifiable / fake | 0 | 0% |

| Field accuracy (among rows that stated a value) | Correct | **Wrong** |
|---|---|---|
| **Founded year** | 49% | **47%** ← nearly a coin flip |
| Funding round/amount | 54% | 27% |
| Stage label | 63% | 24% |
| HQ | 79% | 21% |
| **What it does (description)** | 86% ok | **0% wrong** (14% overstated) |

| Evidence quality | Count |
|---|---|
| primary-strong | 44 (79%) |
| secondary-ok | 5 |
| weak (aggregator/comparison/category page) | 6 |
| invalid (does not identify the company) | 1 (Cora) |

## Root cause — two distinct error classes

**1. Founded-year conflation (the dominant defect — 47% wrong).**
The engine records the *most salient year it encounters* — YC batch year, first-funding year, OSS-launch year, or rebrand year — as the founding year, because homepages rarely state it. Confirmed pattern:

| Company | Recorded | Actual | What the recorded year really was |
|---|---|---|---|
| GoSearch | 2022 | 2016 | Series A year |
| Kinetica | 2013 | 2009 | (founded as GIS Federal) |
| Cube | 2019 | 2016 | Cube.js OSS launch |
| Wren AI | 2023 | 2018 | (parent Canner) |
| Hyperspell | 2025 | 2024 | YC **F25** batch label |
| Mem0 | 2024 | 2023 | rebrand/launch year |
| Granola | 2022 | 2023 | pre-launch guess |
| Shortwave | 2021 | 2020 | between founding & funding |
| Range | 2018 | 2017 | — |
| Ambient | 2022 | 2023 | post-pivot entity |

The team already half-knew this — `validate_merge.py` was patched to make `founded` correctable "for conflating a YC batch label like F25 with the founding year." The audit shows it's not an edge case; it's ~half the field.

**2. Staleness drift (correct at ingest, now stale).**
Fast-movers raised again after capture: **Fyxer** seed→Series B ($30M, Sep 2025), **Mem0** seed→Series A, **Lindy** Series A→Series B, **Ambient** seed→Series A, **Relevance** funding figure one round behind. Different fix than (1): this is the re-verification gap, not a capture error.

## The systemic gap that lets both persist

The status sweep re-checks **8 rows/run × 2 runs/week = 16/week** (~6.6 weeks for a full cycle) — and it only looks for **material *events*** (new funding, acquisition, pivot). It **does not re-audit already-recorded fields.** So a wrong founding year captured at ingest is *never* caught by the normal loop. **The engine has no periodic correctness re-audit. This is the first one.**

Separately, the coverage ledger shows discovery blocks **A, G, H, I are stale** — a *recall* gap (possible missed entrants), distinct from data correctness.

## What is NOT broken (don't over-correct)

- **Structural integrity is code-enforced and clean:** 0 duplicate domains/names/URLs, 0 missing evidence URLs, every row checked ≤14 days. `validate_merge.py` does its job.
- **The qualitative signal is trustworthy:** descriptions are 0% fabricated (14% overstate scope), evidence is 79% primary, tiering is sound and *intentionally* over-inclusive ("when torn, pick higher"). For the radar's actual purpose — "who's the threat and what do they do" — the engine is dependable. The map's wobble is cosmetic; the metadata underneath it is the real issue.

---

## Remediation (prioritized)

### A. Engine process fixes (highest leverage — fixes the cause, not the symptom)
1. **Harden founded-year capture** in `.claude/commands/scan.md` step 3 and `config/rubric.md`: *never* record a founding year inferred from a YC batch / first-funding / OSS-launch / rebrand year. Require an explicit incorporation/about-page/Crunchbase-"founded" source; otherwise record `unknown`. `unknown` is honest; a wrong year is not.
2. **Add a correctness re-audit pass** distinct from the event-based status sweep: each run, re-verify the *N oldest-checked* rows' core fields (founded/stage/hq) against a primary source. This is the missing loop.

### B. Data corrections (ready to apply)
- **18 confirmed updatable corrections** drafted in `audit/2026-06-24-corrections.status_updates.json` (stage/founded/hq/evidence_url). Apply via the canonical writer (`validate_merge.py` status_updates) — **not** a hand-edit (rule #1).
- **Domain/identity fixes (need manual re-key — `domain` isn't updatable):** Cora `cora.so → cora.computer`; Martin `martin.app → trymartin.com`.
- **Watch:** Martin pivoted/rebranded to **Letterbook** (customer-support, away from our lane) — reconsider tier/cluster. Thunai's "Series A" is unverified (Tracxn shows no confirmed round) — consider downgrading stage to `unknown`. Rekap was the one flagged row the recheck *disputed* — leave as-is pending a third look.

### C. Evidence hygiene
7 rows have weak/invalid evidence URLs (Rekap, Jared, Leena AI, Cognee, Martin, Cora, Atomicwork) — stronger primary sources are in the audit output and folded into the corrections draft where the field was updatable.

---
*Full per-row results: workflow `w8xf67mx3` output. This audit verified 66/106 rows; the remaining 40 (incumbents/acquired/public) were treated as low-risk and not re-verified.*
