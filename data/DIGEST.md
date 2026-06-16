# Astell Radar — Decision Digest

What changed, why it matters to Astell, what to do about it. Derived against `config/astell-context.md`, written under the contract in `config/digest-spec.md`, structurally enforced by `scripts/validate_digest.py` — the only writer of this file. Newest first. "NO ACTIONABLE SIGNAL" is a valid, respected outcome; forced items are not.

<!-- entries below -->

## 2026-06-16 — digest (recovery)

### 1. Hyperspell is the closest single-product Astell clone yet — and it forces the API-vs-app decision now
**Signal:** Hyperspell (hyperspell.com, YC F25) connects 50+ work tools into one permission-aware, self-correcting context graph with supersession/drift tracking and citations, served to agents — hitting all four Astell pillars including pillar 2 (open-loop/drift). Surfaced by the 2026-06-15 scan, recovered into the registry 2026-06-16 and re-escalated as Tier 1.
**Why it matters to Astell:** First product to match all four pillars at once, including the supposedly defensible pillar 2 — but sold as an API to agent builders, not a team-facing surface. That gap (memory-for-agents vs open-loops-for-humans) is simultaneously the threat and the differentiation.
**Action:** Write the Astell-vs-Hyperspell teardown this week and use it to force the deferred call — does Astell expose its graph as an API or stay application-only? Ship the one-page recommendation by 2026-06-26.

### 2. Two independent scans hit the same pattern — the open-loop wedge is being cloned in "memory" vocabulary by multiple funded teams at once
**Signal:** The canonical 2026-06-15 CI scan flagged Sentra (sentra.app — "what's true / what's owed / what was meant," bi-temporal graph); the parallel scan flagged Hyperspell and xmemory (xmemory.ai) making the same drift/precision claims in memory-layer framing — three funded hits on one pattern in a single day.
**Why it matters to Astell:** The standing read predicted pillar 2 (open-loop/drift) would get cloned cross-vocabulary; it now has, specifically from the memory/agent-infra camp, by several teams simultaneously. Whoever names the human-facing open-loop category first owns it before "memory API" hardens into the default frame.
**Action:** Lock Astell's open-loop positioning in one sentence that separates "open-loop intelligence for the team" from "memory API for agents" by 2026-06-26, and put it on the astell.space hero and the deck category slide before the next investor update.

## 2026-06-15 — digest (github)

### 1. Sentra is a seed-funded clone of Astell's open-loop wedge — dressed as a "memory API"
**Signal:** Sentra (sentra.app), backed by a16z Speedrun + Together Fund, ships a bi-temporal context graph over 200+ work tools that tracks "what's true, what's owed, what was meant" with source citations, exposed as an MCP/REST memory API.
**Why it matters to Astell:** Pillar 2 (graph, not snapshot) is the defensible bet, and the context file calls Astell's wire open-loop/drift detection, not search. Sentra claims exactly that — "what's owed" is open loops, temporal validity is drift — making it a sharper wedge-competitor than Coworker.ai, just in memory vocabulary (the cross-vocabulary pivot the standing read warned to expect).
**Action:** Benchmark Sentra against the in-house graph on one connector's real data within two weeks (does its "what's owed" surfacing actually find open loops?), and draft an Astell-vs-Sentra battlecard separating "memory API for agents" from "open-loop intelligence for teams."

### 2. Salesforce buying Doti makes it 4-for-4: every independent direct-search startup is now suite-owned
**Signal:** Salesforce acquired Doti (doti.ai), an agentic enterprise-search startup, to power agentic search in Slack/Agentforce (https://www.salesforceben.com/salesforce-buys-agentic-search-company-doti-its-eighth-acquisition-this-year/). With Dashworks→HubSpot, Unleash→Zendesk, and Akooda→Tulip, that is four direct-lane search startups absorbed into suites.
**Why it matters to Astell:** The standing read says the consolidation window is short and independence requires the cross-suite graph suites can't bundle. Doti is a fresh, nameable proof point — and it specifically arms Slack, the "front door," with agentic cross-tool search.
**Action:** Build the four-acquisition table (target → acquirer → date) into the fundraise deck and the "why not just buy the bundled one" battlecard this week, anchored on the line that none of the four can span rival suites post-acquisition.

### 3. A second incumbent graph just opened — extend the Work IQ memo to cover consumable incumbent graphs
**Signal:** At Team '26 (May 2026) Atlassian opened its Teamwork Graph (150B+ connections) to third-party tools and pushed Rovo into autonomous multistep execution, at 5M MAU (atlassian.com, https://siliconangle.com/2026/05/06/atlassian-opens-teamwork-graph-pushes-rovo-agentic-execution-team-26/).
**Why it matters to Astell:** New evidence since the 2026-06-10 Work IQ build-on/compete memo — Microsoft is no longer the only incumbent exposing a cross-tool graph Astell could consume or must out-position. Two now exist, both adding agentic execution: a pillar-2 collision plus a move into open-loop action.
**Action:** Extend the Work IQ memo (already due from the prior digest) with one added page by 2026-06-26 treating Teamwork Graph as a second consumable graph source, with a consume-vs-compete call for each so the M365 decision isn't made in isolation.

## 2026-06-10 — digest (cowork)

### 1. Microsoft Work IQ APIs go GA in six days — decide build-on vs compete before they frame the category
**Signal:** Status sweep caught Work IQ APIs (Microsoft's persistent cross-app context layer) reaching GA on 2026-06-16 (microsoft.com, https://techcommunity.microsoft.com/blog/microsoft365copilotblog/).
**Why it matters to Astell:** Direct collision with pillar 2 (graph, not snapshot) carried by default M365 distribution — and within weeks "context layer" becomes Microsoft marketing vocabulary, which raises the cost of Astell's own positioning language.
**Action:** Assign one engineer to read the Work IQ API docs on GA day and ship a one-page memo by 2026-06-19: build-on (consume Work IQ as a graph source in our M365 connector), compete, or ignore — with the positioning-language implication called out either way.

### 2. Coworker.ai already owns the comparison-page battleground Astell will launch into
**Signal:** coworker.ai (seed, $13M) ships live vs-Glean, vs-Granola, vs-Dust, vs-Notion-AI SEO pages plus named customer logos (https://coworker.ai/).
**Why it matters to Astell:** Positioning lane — when Astell exits waitlist, buyers searching the category will land on Coworker's framing of it; SEO lead time means whoever publishes comparison pages 8+ weeks before our GA owns those SERPs at launch.
**Action:** Write the Astell-vs-Coworker battlecard this week and make the publish/no-publish call on astell.space comparison pages this month, working back from the launch date.

### 3. Town's same-day $55M Series A is the fundraise reference point investors will quote at you
**Signal:** a16z + Forerunner led a $55M Series A into Town (town.com), an individual-level AI work assistant, announced 2026-06-10 — caught by the radar the day it broke.
**Why it matters to Astell:** Fundraise-narrative lane — top-tier funds just priced the individual wedge of this market; every Astell pitch meeting from here will get a "how are you not Town?" question, and the honest answer (org-level graph vs personal assistant) is also our sharpest differentiation.
**Action:** Add a Town slide to the fundraise deck this week: "Town validates the demand at the individual level; Astell is the org-level graph" — with the team-vs-individual capability table to back it.

### 4. The graph-memory layer is now purchasable à la carte — settle build-vs-buy with a benchmark, not a debate
**Signal:** This run registered Zep (getzep.com), Mem0 (mem0.ai), and Supermemory (supermemory.ai) alongside the already-tracked Cognee — four funded vendors selling agent-graph memory as infrastructure.
**Why it matters to Astell:** Product-bet lane, double-edged: competitors can now assemble pillar-2 lookalikes from parts, and Astell could potentially accelerate its own graph build the same way — either way the moat story in the deck needs to survive this cluster's existence.
**Action:** Run a two-day eng spike benchmarking Mem0/Zep/Cognee against the in-house graph on one connector's real data; output an adopt/ignore memo plus the updated moat paragraph for the deck.
