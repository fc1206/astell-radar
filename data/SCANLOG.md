# Scan Log

Append-only. Every run writes an entry, including zero-find runs — written by `scripts/validate_merge.py`, never by hand.

## 2026-06-10 (baseline)
- Four-cluster parallel sweep (direct, data-intel, chief-of-staff, incumbents + funding radar), ~60 searches total.
- Candidates evaluated: ~90; registered: 73 (27 T1 incl. 6 exited, 32 T2, 14 T3).
- Escalations: n/a (baseline).
- Notes: trigger company tanderrum.ai registered as T2/data-intel with full post-mortem in LANDSCAPE.md. Flagged for re-verification: cerenovus.com (YC listing only), rekap.com (site fetch empty), jared.so (PH-sourced), martin.app / cora.so / howie.com (domains uncertain), watolabs.com (thin source). Coworker.ai homepage-verified.

## 2026-06-10 (github)
- Queries run: 24 (blocks: A, B + F + wildcards)
- Candidates evaluated: 21; net-new added: 5; status updates: 0
- Escalations: 0
- Notes: Net-new added (5): Town (T2 chief-of-staff, $55M Series A a16z/Forerunner), Dot (T2 data-intel), Querio (T2 data-intel), Carly (T2 agent platform), Pancake (T2 agent platform, by Basalt). Evaluated but EXCLUDED: Docket (docket.io) = outward-facing sales/marketing AQL agent → T3 CX; Starburst Enterprise Intelligence Platform = lakehouse/Trino data-federation infra, no work-SaaS ingest → out of lane (infra); Entropy Data = data-contract/MCP infra → T3; Cleo/Mina = meeting/standup point tools → T3; Orchid = iMessage personal assistant → T3; Menza = consumer-brand vertical analyst → T3; Mito = data-science IDE → T3 infra; Milestone = AI-agent ROI/observability → out of lane; Sierra = CX agents → T3. Status sweep: registry already current on all 8 targets (Glean SF/$7.2B, Dust $40M Series B, Granola $125M Series C, Interloom $16.5M seed, Coworker $13M seed, Onyx $10M seed, GoSearch). Only net-new fact: Glean acquired Aryn (11-Mar-2026) — minor tuck-in, not logged as material. Cerenovus confirmed real (YC S26, Harvard founders, SF) — thin-source caveat now corroborated but no material change.

## 2026-06-10 (github)
- Queries run: 17 (blocks: C, D + F + wildcards)
- Candidates evaluated: 21; net-new added: 4; status updates: 1
- Escalations: 0
- Notes: Third cycle of 2026-06-10 (blocks C/D; prior same-day run covered A/B). Net-new added (4): Claryti (T2 chief-of-staff, cross-tool commitment tracking), Zep/Mem0/Supermemory (T2 infra, graph-memory pillar a la carte, calibrated against Cognee). watch-unconfirmed: Hapax - proactive 'world model' platform observing team work to build AI coworkers across shared context, but vertical-bounded to financial services/banks; confirmed real via ChannelInsider (HumanX 2026, CEO Hank Seale) yet live homepage/domain not verified within fetch budget; verify next run, likely T2/vertical. Evaluated but EXCLUDED as T3/out-of-lane: Docket (docket.io, outward-facing AI sales/marketing 'AQL' agent), TwinMind (twinmind.com, consumer meeting+voice memory app, 400k users), Alfred (get-alfred.ai, individual email/calendar/task assistant), plus Cleo/Mina/Orchid/Poppy/Soff (individual or consumer chief-of-staff point tools) and Potpie/Cala/Lovelace/CopilotKit (code/dev-agent infra, not Astell's lane). NOTE: xembly.com now resolves to an unrelated betting site - Xembly (not tracked) appears defunct/lapsed at that domain. Status sweep: no material change on Ambient ($4.6M Series A Apr-2025), Bond ($3M seed), Rekap, AskElephant ($6M seed May-2025 / $13.7M total), Thunai, Jared (all active); Google Gemini Enterprise Agent Platform consolidation already captured in registry row; only material delta = Microsoft Work IQ APIs reaching GA 2026-06-16 -> status_updates.json.

## 2026-06-15 (github)
- Queries run: 24 (blocks: E, G + F + wildcards)
- Candidates evaluated: 16; net-new added: 4; status updates: 2
- Escalations: 3
- Notes: Net-new added: Sentra (T1/direct, closest Astell-mechanics find this run), PipesHub (T1/direct, OSS enterprise search), Jedify (T2/data-intel, $24M Series A), Doti (T1/direct, acquired by Salesforce — 4th category consolidation). watch-unconfirmed: Lovelace/Elemental (KG infra, ex-Google Cloud AI head Andrew Moore; intel+finance focus; no homepage/domain or funding confirmed); XTrace (private portable memory infra, no verified homepage); xmemory (London £3m pre-seed memory layer, unverified); company-brain.ai (manual MCP context store, Tier 3, unfunded/early-access — below registry bar); Context.dev and Glen (YC S26 agent-context infra, unverified). Interloom (already in registry) confirmed current — $16.5M seed already reflected, no update. Cerenovus already tracked (recurring YC 'company brain' RFS exemplar). 16 discovery searches (cap) + 8 status searches; 7 WebFetch verifications.

## 2026-06-16 (recovery)
- Queries run: 0 (blocks:  + F + wildcards)
- Candidates evaluated: 5; net-new added: 5; status updates: 0
- Escalations: 1
- Notes: Not a scan — a data-recovery merge. Reconciled a divergent local scan lineage (478c482) against the canonical CI line (c5187eb): two parallel 2026-06-15 scans found different companies. Canonical kept doti.ai/pipeshub.com/sentra.app; this merge recovers the 5 the local line found (hyperspell.com [T1], heyhyper.ai, soliddata.io, atomicwork.com, xmemory.ai) so the union is preserved. Hyperspell re-escalates as Tier-1 (correct).

## 2026-06-18 (github)
- Queries run: 17 (blocks: B, C + F + wildcards)
- Candidates evaluated: 24; net-new added: 3; status updates: 0
- Escalations: 0
- Notes: Registered 3: WisdomAI (T2 data-intel, $73M), Knowi (T2 data-intel, agentic BI), Knowlee (T2 direct, EU cross-tool agent platform). Status sweep: NO material changes — registry already current on all 8 targets (Kore.ai Jan-2026 Series D, Box Agent Apr-2026, Qatalog->ClickUp acquisition, Zoom 3.0 MCP, Aisera acquisition all recorded); confirms tuning-log lesson that the sweep is low-yield when last_checked is recent. watch-unconfirmed: Tanka (tanka.ai) — homepage JS-empty/loading placeholders, search snippets describe cross-tool team memory across Slack/Gmail/Notion but unverifiable; Hapax (domain unconfirmed) — proactive AI that observes team work and auto-builds automations, banking origin now broader enterprise, no funding/domain verified; Letta (letta.com) — MemGPT-lineage agent-memory infra, well-known funded peer of Zep/Mem0 but no live URL fetched this run. Skipped: Docket (docket.io, sales/marketing-bounded 'agentic marketing' -> T3 vertical), Samta.ai (AI product-engineering services/consultancy + vertical products -> out of lane), Menza/Mito (vertical/dev T3). Consolidation signal: Nerve (AI chief-of-staff that took action across tools) acqui-hired by OpenAI Feb 2026 — dead/absorbed, no live site, noted not registered.

## 2026-06-22 (github)
- Queries run: 16 (blocks: D, E + F + wildcards)
- Candidates evaluated: 14; net-new added: 3; status updates: 0
- Escalations: 1
- Notes: Registered: Adapt (T1/direct), Relevance AI (T2/direct, AU), eesel AI (T2/employee-assist, AU). Verified-out-of-lane (not registered): Tacit AI/tacitx.ai (Tier 3 industrial/manufacturing decision engine, vertical); Docket/docket.io (outward sales-CX website agent); Catalect/catalect.io (AI consultancy, no product); Engramme (Large Memory Models, Harvard spinout chasing $1B — consumer/model-infra cognition, out of lane); Sierra (outward CX agents, not in-lane). watch-unconfirmed: Foundation Capital is pushing a 'context graph' thesis and names portfolio cos building them (Maximor, PlayerZero, Tessera, Tonkean, Regie) — these read as vertical/point agents per the article, unverified against primary sources this run; revisit if any positions as a horizontal cross-tool context layer. Status sweep: zero material changes — Omni (Series C $120M/$1.5B + Explo acq) and TextQL (Series A $17M) were already current in the registry; Spinach/Fellow/Cognee/Credal/ThoughtSpot/Range unchanged. Re-confirms last_checked==recent -> low-yield rule. Note: a separate 'Range' (AI wealth management, McLean VA, $60M Series C) is NOT range.co the productivity tool — do not conflate.

## 2026-06-23 (local)
- Queries run: 1 (blocks: F + F + wildcards)
- Candidates evaluated: 6; net-new added: 3; status updates: 3
- Escalations: 1
- Notes: Recovery of the 2026-06-18/06-22 cowork-bridge lineage that diverged from canonical GitHub main. Unions 3 stranded companies (agent.nexus, tacnode.io, zaro.ai incl. a Tier-1) + enriches 3 (adapt.com, knowlee.ai, wisdom.ai) with richer cowork-run detail. Per the Hyperspell precedent: validated union, never a reset.

## 2026-06-25 (github)
- Queries run: 24 (blocks: H, I + F + wildcards)
- Candidates evaluated: 24; net-new added: 3; status updates: 1
- Escalations: 2
- Notes: 3 net-new registered: Atolio (T1, private/self-hosted enterprise search), Squirro (T1, Swiss enterprise GenAI search+KG), Blockbrain (T2, German expertise-capture+knowledge bots, EUR17.5M Series A). watch-unconfirmed: ChapsVision (FR enterprise search/data-intelligence group, surfaced in listicle, not primary-verified). OUT-OF-LANE/skipped: BAND (IL, $17M, agent-to-agent interop infra, not company-brain); Moveworks (employee-assist, acquired into ServiceNow 2025 — already covered by servicenow.com); Capacity/Sharpr/Bloomfire/AddSearch (Tier-3 KM/site-search, not registered for precision); Trusst AI, Marqo, Searchspring (AU CX/commerce search); CORE (IN consumer assistant); Stellar AI / Frontdesk AI (PH OKR/COO SMB tools); Perplexity Brain (feature of tracked Perplexity). DIGEST-FLAG (not registered, secondary-source only): Snowflake reportedly rebranded 'Snowflake Intelligence' -> 'Snowflake CoWork' (Cortex Code -> CoCo) at Summit 2026 + $200M OpenAI partnership + deepened Anthropic; agentic-control-plane positioning already in registry, rename needs primary confirmation. Status sweep low-yield: AlphaSense $350M/$7.5B round already captured in registry (only new = SuperAnalyst agent, no tier change); Coveo/Lucidworks/Vanna/Atlan/Alation no 2026 material change.
