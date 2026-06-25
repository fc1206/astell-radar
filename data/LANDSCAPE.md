# Astell Competitive Landscape

**System of record:** `registry.csv` (count on the Last-scan line below, auto-updated). This file is the narrative read; the CSV is the data. Updated by every `/scan` run — newest changelog entry first.

**Last full baseline:** 2026-06-10 · **Last scan:** 2026-06-24 (local) · **Tracked:** 106 companies

---

## How to read this

Tier 1 = same lane (cross-SaaS context/intelligence for knowledge work) — watch every run. Tier 2 = adjacent lane, one pivot away — watch for repositioning. Tier 3 = context only. Tanderrum was missed because it lives in Tier 2 vocabulary ("data intelligence / conversational BI") while selling a Tier 1 promise; the scan harness exists to catch exactly that.

## Threat assessment (top 5, 2026-06-10)

1. **Glean** — $300M ARR, $7.2B, openly using "context graph" language, now competing on cost-of-AI too. The incumbent startup in the lane.
2. **The incumbent bundle wave** — M365 Copilot Work IQ, Gemini Enterprise, Slackbot/Agentforce, Rovo, Notion Enterprise Search, Dash. Permission-mirrored cross-SaaS search is becoming a *bundled feature*. Astell's wire is the proactive graph (open loops, decisions, drift), not retrieval — retrieval is commoditizing fast.
3. **Granola** — $1.5B, pivoting from meeting notes to "enterprise context layer" with APIs + MCP. Converging on Astell from the meeting wedge, with beloved-product distribution. (We use it internally — know thy enemy.)
4. **OpenAI Workspace Agents** — always-on agents over 60+ work apps with write actions. The "continuous, not one-shot" framing is a direct move toward open-loop detection.
5. **Coworker.ai (Village Platforms)** — OM2 org knowledge graph, 50+ read-write connectors, aggressive pricing story, vs-Glean/vs-Granola/vs-Dust SEO pages, real customer logos. The most complete seed-stage clone of the full Astell thesis. (Homepage verified 2026-06-10.)

## Tier 1 — direct lane

| Company | Stage | The short version |
|---|---|---|
| Glean | Series F, $7.2B | Category leader; 100+ connectors; $300M ARR |
| Dust | Series B (Sequoia) | Multiplayer agents on shared cross-tool context; $20M ARR |
| Coworker.ai | Seed, $13M | OM2 org graph + 50+ RW connectors + model routing |
| Granola | Series C, $1.5B | Meetings → enterprise context layer pivot |
| Interloom | Seed, $16.5M | Context graphs from operational records; Commerzbank/VW live |
| Cerenovus | YC S26 | "Company brain" knowledge graph — near-exact analog, formation stage |
| Onyx | Seed, $10M | Open-source flank; self-hostable; 40+ connectors |
| GoSearch | Seed | 100+ connector Glean-alternative |
| Ambient | Seed | AI CoS: org intelligence newsfeed from Zoom/Slack/Jira/HubSpot |
| Bond | YC X25 | AI CoS for CEOs — "your highest-leverage move" |
| Rekap | Seed (unverified) | Decision/commitment capture across Slack/meetings/email |
| AskElephant | Seed | Cross-tool workspace search (meetings+CRM+docs) |
| Jared | Seed (unverified) | Slack-native CoS, open-loop follow-through |
| Thunai | Series A | Knowledge→agents platform; APAC; PH #1 Jun 2025 |
| + incumbents | — | M365 Copilot/Work IQ, Gemini Enterprise, Slackbot/Agentforce, Rovo, Dash, Notion ES, OpenAI Workspace Agents |

Already exited (signal, not threat): Dashworks→HubSpot, Unleash→Zendesk, Akooda→Tulip, Qatalog→ClickUp, Sana→Workday ($1.1B), Moveworks→ServiceNow ($2.85B).

## Tier 2 — adjacent, one pivot away

**Data-intelligence cluster (Tanderrum's vocabulary):** Tanderrum, ThoughtSpot ($4.2B), Omni ($1.5B, rising fast), TextQL, Zenlytic, Tellius, MindsDB/Anton, GoodData, Wren, AnswerRocket, Promethium (dormant), Seek→IBM, Snowflake Intelligence, Databricks Genie. DataGPT died late 2025. These sell "unify your data, ask in plain English, governed answers" — Astell's promise in warehouse vocabulary. Watch for any of them adding Slack/email/PM connectors: that's the pivot tell.

**Work-memory / chief-of-staff cluster:** Read AI (meetings+email+Slack personal graph — closest to a pivot), Spinach, Fellow, Range. Individual-level EAs in Tier 3 (Lindy, Martin, Fyxer, Cora, Shortwave, Howie).

**Employee-assistant platforms:** Cohere North/Compass (sovereignty angle), Writer, Kore.ai, Leena; Aisera→Automation Anywhere. ServiceNow+Moveworks anchors the ITSM frame.

**Infra selling Astell's pillars à la carte:** Credal (permission-mirroring as a product), Cognee (graph memory for agents), Wato (YC W26 team memory), Cube. Partner-or-rival ambiguity — track product motion.

## Tier 3 — context

Coveo, Lucidworks, AlphaSense, Vanna, Atlan, Alation, Select Star→Snowflake, Secoda→Atlassian, Kinetica, Asana AI, Anthropic MCP ecosystem, Limitless→Meta. Full detail in the CSV.

## Structural reads (2026-06-10)

**1. The consolidation window is real and short.** Eleven category acquisitions in ~14 months: Dashworks (HubSpot), Qatalog (ClickUp), Seek (IBM), Moveworks (ServiceNow, $2.85B), Sana (Workday, $1.1B), Unleash (Zendesk), Akooda (Tulip), Aisera (Automation Anywhere), Limitless (Meta), Select Star (Snowflake), Secoda (Atlassian). Every suite is buying its context layer. Implication for Astell: the independent window is narrowing; differentiation has to be something suites can't bundle — the cross-suite graph itself.

**2. Retrieval is commoditizing; the proactive graph isn't.** Permission-mirrored cross-SaaS *search* now ships free inside Notion, Atlassian, Dropbox, Microsoft, Google. Nobody bundled has cracked decisions/owners/drift/open-loops. That's the defensible half of Astell's four pillars.

**3. The same promise is sold in at least four vocabularies.** Work-tool vocabulary (Glean, Astell), data vocabulary (Tanderrum, Omni), agent vocabulary (Dust, Coworker), memory vocabulary (Cognee, Granola post-pivot). Any scan keyed to one vocabulary misses the other three — this is the Tanderrum lesson, encoded in `config/queries.yaml`.

**4. Permission-mirroring became table stakes.** Credal sells it standalone; Notion/Dash/Copilot advertise it. Pillar 4 is no longer a differentiator on its own.

## Tanderrum post-mortem (why we missed it)

Melbourne, ~2020, 2–6 people, no disclosed funding, no Crunchbase, no G2, no press. "Launched globally" mid-2025 via a LinkedIn post. Found only by direct-vocabulary search — generic cluster queries never surface it. Assessment: low execution threat (tiny team, no capital), nonzero shortlist/positioning nuisance in APAC verticals. Monitoring: founders Roshan Edirisinghe ("Chief Enabler") and Rizvi Amith (CMO, Toronto) on LinkedIn. Lesson encoded in harness: every run includes lookalike/listicle/"alternative-to" sweeps and rotating direct-vocabulary blocks, because Tanderrum-class companies are invisible to funding-news scans.

---

## Changelog

### 2026-06-24 — scan (local)
Updated: Hyperspell — Correct stage (seed->pre-seed, per Crunchbase pre-seed round hyperspell-pre-seed led by pre-seed specialist Afore Capital + Pioneer Fund + Y Combinator) and founded (2025->2024, per YC company page; the 2025 came from conflating the YC F25 batch label with the founding year)

### 2026-06-23 — scan (local)
**⚠ NEW TIER 1:** Zaro (zaro.ai)
Added: Nexus (T2, direct); Tacnode (T2, infra); Zaro (T1, direct)
Updated: Adapt — reconcile richer detail from the parallel 2026-06-18/06-22 cowork run (no-loss union); Knowlee — reconcile richer detail from the parallel 2026-06-18/06-22 cowork run (no-loss union); WisdomAI — reconcile richer detail from the parallel 2026-06-18/06-22 cowork run (no-loss union)

### 2026-06-22 — scan (github)
**⚠ NEW TIER 1:** Adapt (adapt.com)
Added: Adapt (T1, direct); Relevance AI (T2, direct); eesel AI (T2, employee-assist)

### 2026-06-18 — scan (github)
Added: WisdomAI (T2, data-intel); Knowi (T2, data-intel); Knowlee (T2, direct)

### 2026-06-16 — scan (recovery)
**⚠ NEW TIER 1:** Hyperspell (hyperspell.com)
Added: Hyperspell (T1, direct); Hyper (T2, direct); Solid (T2, data-intel); Atomicwork (T2, employee-assist); xmemory (T2, infra)

### 2026-06-15 — scan (github)
**⚠ NEW TIER 1:** Sentra (sentra.app), PipesHub (pipeshub.com), Doti (doti.ai)
Added: Sentra (T1, direct); PipesHub (T1, direct); Jedify (T2, data-intel); Doti (T1, direct)
Updated: Atlassian Rovo — Team '26 (May 2026): opened Teamwork Graph (150B+ connections) + Rovo agentic execution; 5M MAU; OpenAI Workspace Agents (ChatGPT Enterprise) — Confirmed canonical Workspace Agents announcement; free until Jul 6 2026 then credit-priced

### 2026-06-10 — scan (github)
Added: Claryti (T2, chief-of-staff); Zep (T2, infra); Mem0 (T2, infra); Supermemory (T2, infra)
Updated: Microsoft 365 Copilot + Work IQ — Work IQ opened as APIs (GA Jun 16 2026) - the context layer becomes a programmable platform third parties build agents on.

### 2026-06-10 — scan (github)
Added: Town (T2, chief-of-staff); Dot (T2, data-intel); Querio (T2, data-intel); Carly (T2, direct); Pancake (T2, direct)

### 2026-06-10 — Baseline established
Full four-cluster sweep (direct, data-intel, chief-of-staff, incumbents+funding). 73 companies registered: 27 Tier 1 (incl. 6 exited), 32 Tier 2, 14 Tier 3. Trigger: missed tanderrum.ai. Five entries flagged for verification on next status sweep: Cerenovus, Rekap, Jared, Martin/Cora/Howie domains, Wato.
