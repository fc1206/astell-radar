# Scoring Rubric

Astell (astell.space) = an intelligence layer over a company's tools. Ingests connected SaaS (Slack, Gmail, Notion, Linear, GitHub, Salesforce, HubSpot, Zendesk, +25 more), builds a cross-tool graph, surfaces open loops: decisions, owners, outcomes, drift. Pillars: (1) ingest not retrieve, (2) graph not snapshot, (3) cite not hallucinate, (4) mirror source permissions.

## Tiers

**Tier 1 — same lane.** Core product is AI search / context / answers / proactive intelligence across MULTIPLE work SaaS tools for knowledge workers or teams. Includes incumbent features that ground across many tools (M365 Copilot, Gemini Enterprise, Notion ES). Test: could a prospect plausibly say "we're choosing between this and Astell"?

**Tier 2 — adjacent, one pivot away.** Same promise in a different vocabulary or perimeter: structured-data/BI/warehouse focus; meeting-only or email-only memory; individual-level chief-of-staff; employee IT/HR helpdesk assistants; infra selling one Astell pillar à la carte (permissions, graph memory). Test: would adding 2–3 connectors or one positioning change put them in Tier 1?

**Tier 3 — context only.** Single-feature point tools (scheduling, email triage), pure infra (semantic layers, catalogs, protocols), vertical-bounded intelligence (finance docs, market intel), outward-facing search (commerce/CX).

**When torn between two tiers, pick the higher (more threatening) one.** A false positive costs a minute of reading; a miss costs what Tanderrum cost.

## Clusters

`direct` | `chief-of-staff` | `data-intel` | `incumbent` | `employee-assist` | `infra` | `vertical`

The machine source of truth is `config/clusters.json` — `validate_merge.py` reads it to accept/reject rows. Keep this list in step with that file (edit config, never the Python).

## Calibration examples

- **Glean** → Tier 1 / direct. Cross-SaaS search + agents is the whole product.
- **Tanderrum** → Tier 2 / data-intel. Sells "unify enterprise data, ask in plain English, governed" — Astell's promise in warehouse vocabulary, claims unstructured docs + enterprise search too. Canonical Tier 2: wrong vocabulary, same customer promise. (This is the company we missed; if the pipeline wouldn't flag it, the pipeline is broken.)
- **Coworker.ai** → Tier 1 / direct. Org knowledge graph + 50+ work-SaaS connectors, despite "agent platform" vocabulary. Vocabulary never overrides mechanics.
- **Zenlytic** → Tier 2 / data-intel. AI analyst bounded to the warehouse.
- **Howie** → Tier 3 / chief-of-staff. Scheduling only.
- **Cube** → Tier 3 / infra. Semantic-layer plumbing.
- **Granola** → Tier 1 / chief-of-staff. Meeting wedge, but explicit "enterprise context layer" pivot + APIs. Trajectory counts, not just today's perimeter.

## Source quality & evidence

Precision is about what gets *registered*, never about what gets *considered* — a low-footprint, non-US, or wrong-vocabulary company is exactly what we exist to catch, so breadth of consideration stays wide (Tanderrum). Once considered, hold registered entries to higher evidence:

- **Prefer primary evidence:** the company's own site, its YC / Crunchbase / LinkedIn company page, or a named funding announcement. Listicles, "top 10" roundups, and SEO content farms are **lead generation only** — use them to find names, then verify against a primary source before registering.
- **Lift the exact domain** from the funding-DB / press page rather than guessing a homepage (WebFetch can't open a URL that didn't appear in search results).
- **Founding year ≠ batch / funding / launch year.** Record `founded` only from an explicit founding-year source (about page, Crunchbase / LinkedIn "Founded", incorporation record). Never infer it from a YC batch label (**F25 ≠ founded 2025**), a first-funding date, an OSS-project launch, or a rebrand year. This conflation is the single most common error in the registry — a 2026-06-24 audit found ≈half of stated founding years wrong from exactly this. No primary founding-year source → record `unknown` (honest beats wrong).
- **Thin / unverifiable but plausible → `watch-unconfirmed`** in `run_meta.json` notes, not a registry row. No live evidence URL, no entry.
- **Region is not a tier signal.** Non-US / non-English origin does not lower a tier — score on mechanics only. If anything, an overseas company that hits the lane deserves *extra* scrutiny, because that's the class we've missed before.

## What does NOT belong in the registry

Pure model providers, RAG tutorials, agencies/consultancies, open-source libraries without a company, products with no working website AND no funding/launch evidence (note them in SCANLOG as "watch-unconfirmed" instead).
