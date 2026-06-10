# Query Battery

Edit freely — this file is the harness's search brain. `scripts/plan_run.py` parses block IDs from `## Block X:` headers; keep that format. `{year}`, `{month}` are filled in by the agent at run time.

**Per run:** Block F always (pick 4) + the two emphasized blocks from `plan_run.py` (pick 5 each) + 2 wildcard queries the agent invents based on recent findings + the status sweep. ~22 searches total. Full block coverage every 3 runs.

**Tuning log (append lessons here):**
- 2026-06-10: "Glean alternative" class queries = highest yield (every entrant writes a vs-Glean page). Generic "AI work assistant funding {year}" = noise. Architectural-primitive queries (context graph, memory layer) catch what category queries miss (found Interloom, Cognee). Named-company status queries are the only way to catch acquisitions (Sana, Unleash) and Tanderrum-class invisibles. Product Hunt "AI chief of staff" category page = goldmine. YC: query named-concept ("YC {batch} company brain"), not batch listings.

## Block A: self-vocabulary (work-tool language)

- enterprise search startup {year}
- AI work assistant for companies new startup
- context layer for company tools startup
- work graph startup
- "connect Slack Notion Linear" AI assistant
- company knowledge AI startup {year}

## Block B: data-vocabulary (Tanderrum's cluster)

- conversational BI startup {year}
- agentic analytics platform new
- enterprise data intelligence platform startup
- natural language data governance lineage AI
- "chat with your data" enterprise startup
- AI data analyst startup {year}

## Block C: chief-of-staff / memory vocabulary

- AI chief of staff startup {year}
- AI executive assistant team startup funding
- AI meeting memory startup
- decision tracking AI tool teams
- AI tracks commitments across Slack email
- proactive AI work assistant startup

## Block D: agent-vocabulary (Dust/Coworker cluster)

- enterprise AI agent platform company context startup
- AI agents company knowledge graph
- multiplayer AI agents enterprise
- organizational memory AI agents startup
- AI agent platform "all your tools" startup

## Block E: architectural primitives

- "context graph" startup
- "organizational memory" AI startup
- "company brain" startup
- tacit knowledge AI enterprise
- "AI memory layer" enterprise startup funding

## Block F: lookalikes + listicles (ALWAYS RUN)

- Glean alternatives {year}
- Glean competitors {year}
- Dropbox Dash alternative
- Astell alternative   ← ego search; anyone comparing against us
- best enterprise search tools {year}
- "vs Glean"

## Block G: funding + launch venues

- enterprise search seed round {month} {year}
- "context layer" OR "context graph" funding {year}
- AI knowledge management raised {year} techcrunch
- YC {current batch} company brain OR knowledge graph OR enterprise search
- Product Hunt AI chief of staff new launches
- Show HN enterprise search {year}

## Status sweep (every run)

For each of the ~8 round-robin targets from `plan_run.py`:
- `"{name}" funding OR acquired OR acquisition OR shutdown OR pivot {year}`

Material changes (new round, acquisition, death, repositioning toward Astell's lane) go in `status_updates.json`.
