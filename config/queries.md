# Query Battery

Edit freely — this file is the harness's search brain. `scripts/plan_run.py` parses block IDs from `## Block X:` headers; keep that format (one capital letter, then a colon — extra text after the colon is fine). `{year}`, `{month}`, `{current batch}` are filled in by the agent at run time.

**Two lanes, tuned independently so precision never costs breadth:**

- **Lane 1 — precision (Blocks A–E, G):** source-targeted queries that reliably surface real companies. Favor `site:` and named venues; lift exact domains from the result pages. Sharpen these freely.
- **Lane 2 — recall safety-net (Block F always-on + Block H regional + Block I edge-expansion):** the wide net that exists to catch low-footprint, wrong-vocabulary, non-US entrants — the Tanderrum class. This lane is *allowed* to be noisy; that's its job. **Never trim it for cleanliness.**

**Per run:** Block F always (pick 4) + the two emphasized blocks from `plan_run.py` (pick ~5 each) + 2 wildcards the agent invents from recent findings + the status sweep. ~22 searches total. Full block coverage every 4 runs. `plan_run.py` emits a **coverage ledger** and flags any block gone stale (default >18 days) — if it reports `stale_coverage`, fold the stalest block/region into your wildcards that run. Breadth is guaranteed by cadence + this ledger, not by per-run volume.

**Tuning log (append lessons here):**
- 2026-06-10: "Glean alternative" class queries = highest yield (every entrant writes a vs-Glean page). Generic "AI work assistant funding {year}" = noise. Architectural-primitive queries (context graph, memory layer) catch what category queries miss (found Interloom, Cognee). Named-company status queries are the only way to catch acquisitions (Sana, Unleash) and Tanderrum-class invisibles. Product Hunt "AI chief of staff" category page = goldmine. YC: query named-concept ("YC {batch} company brain"), not batch listings.
- 2026-06-10 (run 3, blocks C/D): Block C commitment/brief vocabulary earns its keep — "AI tracks commitments across Slack email" surfaced Claryti (cross-tool decision tracking, the cleanest C hit). Block D agent-vocabulary queries ("AI agents knowledge graph", "organizational memory AI agents") now mostly route to the memory-INFRA cluster (Zep, Mem0, Supermemory, Cognee) rather than application-layer rivals — treat D as an infra-radar, tier against Cognee. "multiplayer AI agents" = pure Dust echo (already tracked). Consumer chief-of-staff (TwinMind/Poppy/Orchid) and code-agent infra (Potpie/CopilotKit) are recurring D/C noise — skip fast.
- 2026-06-10 (run 2): Block A self-vocabulary now nearly pure noise — "Glean alternatives/competitors" and "enterprise search startup" surface only listicles + already-tracked rows; the lane's obvious names are saturated. Block B data-vocabulary still earns its keep (found Dot, Querio via "conversational BI" / "AI data analyst funding"). Best ROI this run was the Product Hunt "AI chief of staff" wildcard — caught Town ($55M Series A, same day) and Pancake. Lean wildcards toward PH/launch venues + funding-news; trim generic Block A category queries. Status sweep added nothing: registry was already current on all 8 targets — when registry last_checked == today, status sweep is low-yield.
- 2026-06-15 (blocks E/G): Architectural-primitive + funding/launch was the high-yield combo. Block E ("company brain"/"context graph") and the YC RFS query surfaced the whole Summer-2026 "Company Brain" cluster (Hyperspell → T1, Hyper, Cerenovus, Savant) plus funded context-graph plays (Jedify $24M Series A w/ Snowflake Ventures, Solid $20M seed w/ Team8/SignalFire). "Context graph" is now the cross-vocabulary category term — worth a standing wildcard. Plumbing lesson: WebFetch only retrieves URLs that appeared in WebSearch results — can't fetch a guessed homepage; verify candidates via the press/listicle URLs the search returns, and lift exact domains from funding-DB pages (thesaasnews → soliddata.io, startupmag → xmemory.ai). Status sweep paid off this run (registry was 5 days stale): TDX 2026 Slackbot default-provisioning, Atlassian Team '26 Teamwork Graph/Rovo Max, and OpenAI Workspace Agents all landed since baseline — re-confirms the sweep is only low-yield when last_checked == today.
- 2026-06-15 (refactor): split the battery into Lane 1 (precision) / Lane 2 (recall safety-net); added **Block H (geographic / non-US)** — the actual Tanderrum gap (Melbourne, no US press) — and a **coverage ledger** in `state.json` that `plan_run.py` uses to flag any block unswept >18d. Source-targeted the funding/launch block with `site:` venue queries (PH/HN/YC/funding DBs) and generalized the vs-Glean winner into a per-Tier-1 "vs X" query in Block F. Added the noise-skip list below — stop re-litigating confirmed out-of-lane tools each run.
- 2026-06-18 (bridge, blocks B/C): Block B (data-vocab) delivered the headline catch — "AI data analyst startup" / "enterprise data intelligence natural language" surfaced **WisdomAI** (ex-Rubrik, $73M Kleiner/NVIDIA, T2 data-intel) that pre-dated the baseline yet sat un-tracked: the Tanderrum/data lane is still where the costly misses hide, keep Block B emphasized often. Block F vs-X pages yielded two agent platforms (**Knowlee** via its own Dust-alternatives blog; **Nexus**/agent.nexus likewise) — when a startup's homepage is JS-empty/unfetchable, its own `/blog/<competitor>-alternatives` page is a usable primary-ish source. Plumbing reconfirmed: WebFetch only opens URLs that appeared in search results — bare homepages (knowlee.ai/, agent.nexus/) failed provenance; lift the domain from a press / VC-perspective page (wisdom.ai came off the Kleiner Series-A post). Status sweep low-yield despite an 8-day-stale registry — every target's 2026 event was already captured 2026-06-10, and Kore.ai funding totals conflicted across Tracxn/PitchBook ($224M vs $296M); verify named-company status against primary (kore.ai/news), not aggregators.
- 2026-06-22 (bridge, blocks D/E): Block E ("company brain"/"context graph") + a Product Hunt launch-venue wildcard surfaced the cleanest direct clone yet — **Adapt** (adapt.com): an in-market, team-facing "company brain" across all work tools that answers+acts+cites and attacks Glean by name (T1, NEW escalation). PH "company brain" stays a goldmine (Town lesson holds). Block D agent-vocab still routes mostly to memory-infra (Cognee/Mem0/Supermemory) + out-of-lane agent platforms (Sierra/Relevance/DevRev) — tier against the infra cluster, don't re-litigate. New cross-vocabulary signal worth a standing wildcard: **data ownership / context portability** ("own your context, take it elsewhere" — Zaro, ex-Agentforce team). Out-of-lane reconfirmed: Lovelace/Elemental (mission-critical OUTWARD intel — YottaGraph over public/licensed sources; already on the noise list, no trajectory shift) and Graphon (pre-model multimodal representation infra, not work-tool context). Plumbing: WebFetch/web_fetch only opens URLs already in the search-result/provenance set — the Zaro/Tacnode evidence URLs carried in from a memory note failed provenance until re-surfaced via a WebSearch; run a quick confirming search to pull a known prior-miss URL into provenance before fetching. Status sweep zero-yield again: all 8 targets (incl. Omni $120M Series C @ $1.5B, TextQL $17M Series A) were already current from the 2026-06-10 baseline — sweep only pays when last_checked is stale.

- 2026-06-23 (re-architecture v2): added **Block I (edge-expansion)** — G2/Capterra/SourceForge compare lists + per-Tier-1 `/alternatives` page harvest. Formalizes the ad-hoc win the 06-18/06-22 entries stumbled on (Knowlee, Nexus came off their own `/blog/X-alternatives` pages): read the competitor sets others already publish instead of re-guessing vocabulary. Lane 2 / recall; rotates with the ledger. `tests/test_recall.py` guards that F, H, I, and the data-vocab block (B) stay present — removing any silently re-opens a known miss class.

- 2026-06-18 (blocks B/C): Block B data-vocabulary still the most productive lane — "AI data analyst funding" + the structured/unstructured framing surfaced WisdomAI ($73M, Kleiner/Nvidia, markets an "enterprise context layer") and Knowi (agentic BI). Block C is decaying into consumer/individual noise: "AI chief of staff / proactive assistant" now route almost entirely to individual desktop/inbox tools (Poppy, IrisGo, Logical, Supafax — skip-list material) and the only team-facing C hits (Tanka, Hapax) had JS-empty or domainless sites → watch-unconfirmed, not registrable. Both standing wildcards saturated this run: "memory API/layer" returned only tracked infra (Mem0, Cognee, Interloom, Letta) and "context graph/company brain" returned only tracked rows (Interloom, Jedify, Cerenovus) — rotate wildcards toward funding-DB/launch venues next time. Status sweep added nothing: registry was current on all 8 (last_checked 8 days) — re-confirms the last_checked==recent → low-yield rule.
- 2026-06-22 (blocks D/E): Both stale-coverage wildcards earned their keep — the AU regional sweep (Block H) caught **two** net-new Australian players the prior US-centric runs missed (Relevance AI, well-established Series B agent platform; eesel AI, CX+internal-knowledge), confirming the Tanderrum-gap thesis that region rotation surfaces invisibles. The PH "company brain" wildcard (Block G) surfaced **Adapt (adapt.com) → Tier 1** — an app-facing, Slack-native "company brain" that answers *and* acts (Skills/workflows), distinct from the recent API-for-agents T1s (Hyperspell/Sentra). Block E "company brain"/"context graph" is now also a VC-narrative radar: Foundation Capital's "context graph = trillion-dollar opportunity" thesis dominated the E results (mostly essays, not companies) — useful for fundraise-narrative digest items, low yield for new registry rows. Block D again routed almost entirely to infra/incumbents (Cognee, Mem0, Interloom, Oracle/Cloudflare memory) + code-agent noise (Potpie, Lovelace) — treat D as infra-radar as noted. Status sweep added nothing: Omni (Series C) and TextQL (Series A) were already current in registry — re-confirms last_checked==recent → low-yield. Caution logged: a separate "Range" (AI wealth mgmt, McLean VA) is not range.co — don't conflate on status sweeps.
## Standing wildcards (keep one in rotation every run)

- `"context graph" OR "company brain"` + (funding OR launch OR startup) {year} — now the cross-vocabulary category term
- whatever the last 1–2 changelog entries flag as moving (a pivot, a fresh raise, a new vocabulary)
- the stalest block/region from `plan_run.py`'s `stale_coverage`, if any

## Block A: self-vocabulary (work-tool language) — Lane 1

- enterprise search startup {year}
- AI work assistant for companies new startup
- context layer for company tools startup
- work graph startup
- "connect Slack Notion Linear" AI assistant
- company knowledge AI startup {year}

## Block B: data-vocabulary (Tanderrum's cluster) — Lane 1

- conversational BI startup {year}
- agentic analytics platform new
- enterprise data intelligence platform startup
- natural language data governance lineage AI
- "chat with your data" enterprise startup
- AI data analyst startup {year}

## Block C: chief-of-staff / memory vocabulary — Lane 1

- AI chief of staff startup {year}
- AI executive assistant team startup funding
- AI meeting memory startup
- decision tracking AI tool teams
- AI tracks commitments across Slack email
- proactive AI work assistant startup

## Block D: agent-vocabulary (Dust/Coworker cluster) — Lane 1

- enterprise AI agent platform company context startup
- AI agents company knowledge graph
- multiplayer AI agents enterprise
- organizational memory AI agents startup
- AI agent platform "all your tools" startup

## Block E: architectural primitives — Lane 1

- "context graph" startup
- "organizational memory" AI startup
- "company brain" startup
- tacit knowledge AI enterprise
- "AI memory layer" enterprise startup funding

## Block F: lookalikes + listicles + ego (Lane 2 — ALWAYS RUN)

- Glean alternatives {year}
- Glean competitors {year}
- Dropbox Dash alternative
- Astell alternative   ← ego search; anyone comparing against us
- "vs Glean" OR "vs Dust" OR "vs Coworker" OR "vs Granola"   ← per-Tier-1 comparison pages; every real entrant writes one
- best enterprise search OR "AI work assistant" tools {year}
- AI "company brain" OR enterprise search startup (Europe OR India OR Australia OR Israel)   ← light regional touch every run

## Block G: funding + launch venues — Lane 1 (source-targeted)

- site:producthunt.com AI chief of staff OR enterprise search OR "company brain"
- site:news.ycombinator.com Show HN enterprise search OR knowledge OR "context graph"
- YC {current batch} company brain OR knowledge graph OR enterprise search
- "context layer" OR "context graph" funding {year} (techcrunch OR theinformation OR thesaasnews)
- enterprise search OR "AI knowledge" seed OR "series A" raised {month} {year}
- AI work assistant OR enterprise search acquisition OR acquired {year}

## Block H: geographic / non-US (Lane 2 — recall; rotate one region per run)

The Tanderrum gap: a wrong-vocabulary, no-funding, non-US company is invisible to generic + US-funding search. Rotate the region across runs so each gets covered.

- AI enterprise search OR "company brain" startup Australia OR New Zealand {year}
- enterprise AI assistant OR knowledge graph startup India OR Singapore {year}
- AI "context" OR "knowledge" enterprise startup Europe OR UK OR Germany {year}
- AI enterprise knowledge OR agent startup Israel {year} (Team8 OR funding)
- LinkedIn "launched globally" OR "now live" AI company knowledge OR context (no funding/press)   ← catches Tanderrum-style social-only launches
- (non-English) when a region surfaces a hit, re-run one query in that region's language

## Block I: edge-expansion (Lane 2 — recall; harvest the competitor sets others publish)

The insight: every player in this market maps its own rivals. Compare-list directories and competitors' own `/alternatives` and `/vs` pages name companies our keyword queries never reach — the cheapest way to find the next Tanderrum is to read who Glean/Dust/Coworker already consider rivals. Run 2–3 of these per cycle; lift exact domains from the listed entries and verify each against a primary source before registering (the source-quality rule still applies).

- site:g2.com Glean OR Dust OR "enterprise search" alternatives OR compare
- site:capterra.com OR site:sourceforge.net enterprise search OR "AI knowledge" alternatives {year}
- "alternatives to" Glean OR Dust OR Coworker OR Granola (-site:g2.com)   ← roundups that enumerate a competitor set
- {pick a Tier-1 from the registry}/alternatives OR /vs — fetch the company's own comparison page and harvest every rival it names
- "compare" AI "enterprise search" OR "company brain" OR "work assistant" {year}
- crunchbase OR tracxn "similar companies" enterprise search OR knowledge graph

## Status sweep (every run)

For each of the ~8 round-robin targets from `plan_run.py`:
- `"{name}" funding OR acquired OR acquisition OR shutdown OR pivot {year}`

Material changes (new round, acquisition, death, repositioning toward Astell's lane) go in `status_updates.json`.

## Known noise — skip fast (NOT a block; do not re-evaluate unless trajectory changes)

Confirmed out-of-lane in prior runs — recognize and move on, don't spend fetch budget. Re-check ONLY if one pivots toward cross-tool team intelligence (the Granola lesson: trajectory counts):

- **Consumer / individual chief-of-staff & memory:** TwinMind, Poppy, Orchid, Cleo, Mina, Soff, Alfred, Curiosity (individual cross-tool search)
- **Code / dev-agent infra:** Potpie, CopilotKit, Cala, Lovelace, Tabnine
- **Pure echoes of tracked players:** "multiplayer AI agents" → Dust; generic "AI work assistant funding {year}" → noise
- **Out-of-lane infra / observability:** Milestone (agent ROI), Starburst/Trino (data-federation), Entropy Data (data-contract infra)
