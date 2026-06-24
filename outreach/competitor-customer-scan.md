# Competitor customer scan — seed + spec

**Purpose:** turn the radar's competitor list into a prospecting input by finding the **competitors' customers**. A company already buying an in-category product is the cleanest Astell ICP. **Build the list only — contact no one.**

**Where to run this:** Cowork (orangeslice). BuiltWith-backed discovery (who runs a competitor's tech) + PredictLeads are purpose-built for "who are company X's customers." Claude Code generated this seed from `data/registry.csv`; load the Astell Spine for full context (rubric, what each competitor does, the threat map).

**Handoff:** Claude Code (repo + radar) → this file (committed) + the Spine → Cowork (orangeslice) runs the scan → Frank reviews. Single-writer note: the radar registry is only ever written by GitHub Actions; this file is a one-off seed, safe to hand-edit.

## Seed — direct-lane Tier-1 startups (their customers = purest ICP)

Filter: `tier == 1`, `cluster == direct`, `status == active`, stage not public. Excluded acquired companies (Dashworks, Unleash, Akooda, Qatalog, Sana, Doti — their customer base is now noise) and mega-incumbents (whose "customers" are everyone). Expand to Tier-2 `data-intel` (the Tanderrum class) later for more volume.

| Competitor | Domain | Stage |
|---|---|---|
| Glean | glean.com | series-f |
| Dust | dust.tt | series-b |
| Thunai | thunai.ai | series-a |
| Adapt | adapt.com | seed |
| AskElephant | askelephant.ai | seed |
| Cerenovus | cerenovus.com | seed |
| Coworker (Village Platforms) | coworker.ai | seed |
| GoSearch | gosearch.ai | seed |
| Hyperspell | hyperspell.com | seed |
| Interloom | interloom.com | seed |
| Onyx (fmr Danswer) | onyx.app | seed |
| Sentra | sentra.app | seed |
| PipesHub | pipeshub.com | bootstrapped |
| Zaro | zaro.ai | pre-seed |

## Task spec (for the Cowork / orangeslice run)

For each competitor in the seed, find its customers/clients:

- **Sources:** orangeslice BuiltWith-backed discovery (sites running the competitor's tech/SDK), PredictLeads signals, the competitor's own `/customers` / case-study / logo-wall pages, and G2 / Capterra reviewers (reviewers are usually customers).
- **Output per customer:** `company`, `domain`, `competitor_used`, `signal` (the evidence), `source_url`.
- **Dedupe** across competitors (a company using two competitors is a stronger signal — keep both, note it).
- **Flag ICP matches** against Astell's ICP.
- **List only — no outreach, no messages, no sends.**

## ICP reference

Astell sells an intelligence layer over a company's work tools (ingest not retrieve, graph not snapshot, cite not hallucinate, mirror permissions — see `config/rubric.md`). A competitor's customer that is a mid-to-large company running many SaaS tools is a strong ICP match. Full competitor detail is in `data/registry.csv`; the synthesized company picture is in the Astell Spine.
