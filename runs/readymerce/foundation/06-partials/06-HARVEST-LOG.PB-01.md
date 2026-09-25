# 06 — VOC 3 · HARVEST LOG · SCOPE: PB-01 (HARVEST mode) · Readymerce

agent_id: VOC-PB-01 · leg 3 of 3 · started 2026-09-24T20:37:15Z. Reads 05-partials/05-URL-CORPUS.PB-01.md + 05-HANDOFF.PB-01.json (this session) · 04-partials outputs (this session) · 01-HANDOFF.json + 01-PRODUCT-TRUTH.md §5-§8. LATE-BOUND: 03.AS-## (no 03-HANDOFF.json, no 03-partials/) — assumption check (§17) deferred to 06-MERGE/07 per rule.
DEGRADED-TOOL NOTICE (binding, unchanged): Apify BLOCKED-ON-TOOL (all actors, $0 spendable) · Firecrawl scrape BLOCKED-ON-TOOL · Browserbase BLOCKED-ON-TOOL · WebFetch/curl BLOCKED-ON-TOOL (egress 403) · Reddit and Trustpilot PAGE FETCH not retrievable by generic tools — Trustpilot pages WERE reached this leg via the Exa research agent (`[R-PAGE via Exa]`), which the ADDENDUM permits once per URL; Reddit remained fully unreachable (0 reddit.com URLs ever surfaced by WebSearch across both 04 and 05). WORKING and used: `mcp__Readymerce_Exa__agent_run` (effort medium, verbatim extraction — RC-EXA) and `mcp__TranscriptAPI__get_youtube_transcript` / `search_youtube` (RC-YTX).

**Step 0 — Lock (re-printed).** FLOOR TABLE (05 §1, PB-01's share): records_total(workflow) 200, PB-01 40, CP-01 25, CP-05 25, reddit share 27, reviews share 20, video_comments share 10, fb+forum+quora share 7, ad_comments share 4 (none available), ≥4 source types, tags per 05 §1. Assignment: HV-PB-01, url_ids URL-01..URL-23 in rank order (05 §6), recipe_ids [RC-WEB(printed only, Apify BLOCKED), RC-FBC(printed only, BLOCKED), RC-TP(printed only, BLOCKED — Exa substituted where it could reach the page), RC-YTX(RUNS), RC-EXA(RUNS), RC-RD(BLOCKED, no URL)]. Resume: partial CSV did not exist at leg start (fresh run); no CHECKPOINT to resume from.

**Step 1 — Scrape lanes.** RC-WEB, RC-FBC, RC-TP, RC-RD: all Apify-backed, all BLOCKED-ON-TOOL (`Monthly usage hard limit exceeded`, confirmed by ADDENDUM, not re-attempted — 1 attempt is enough per rule 13's "at most 3 attempts across its chain," and the chain's own first link already errors deterministically). `dataset <id>: rows 0 · pages 0` for every one of these four recipe_ids — 0 spendable this leg. Fallback taken: RC-EXA (Exa agent, WORKING) substituted for forum_thread, blog_comments and (once each) trustpilot_balanced lanes per the ADDENDUM's explicit permission.

**Step 2 — Page lanes / RC-EXA + RC-YTX batch (launched together, polled together).**

Counter format (05 §8): `records n/40 · PB-01 n/40 · CP-01 n/25 · CP-05 n/25 · sources n/23 (SCRAPED 0 · FETCHED n · 0-yield n · BLOCKED n · PASTE n) · types n/4 · pain n/7 · scene n/5 · failed_solution n/7 · objection n/7 · desire n/5 · trigger n/5 · belief n/5 · symptom n/4 · skepticism n/4 · spend n/2 · deeper_hope n/2 · tired_of_hearing n/2 · horror_story n/1 · curiosity n/1 · corruption n/1 · cost $x.xx`

- URL-01 (community.shopify.com/t/shopify-by-adrian-morrison/215810, RC-EXA): 3 records — Q-F-0001..0003. `records 3/40 · sources 1/23 (FETCHED 1) · types 1/4 · cost $0.10`
- URL-07 (…struggling-with-adrian-morrisons-free-store-build/310831, RC-EXA): 2 records — Q-F-0004..0005. `records 5/40 · sources 2/23 · cost $0.20`
- URL-02 (…is-there-a-simple-way-to-understand-shopify/192077, RC-EXA): 9 records — Q-F-0006..0014. `records 14/40 · sources 3/23 · cost $0.30`
- URL-05 (…building-your-shopify-store-what-is-the-biggest-problem-you-encountered/133383, RC-EXA): 0 records — reason: Exa opened the page but returned no author/date-attributed passages (thread likely thin or paywalled beyond OP); `URL-05: 0 records — reason: no first-person`. `sources 4/23 (0-yield 1)`
- URL-15 (trustpilot.com/review/ecomxpertz.com, RC-EXA, Trustpilot sent to Exa exactly once per ADDENDUM): 9 records — Q-E-0015..0023. `records 23/40 · sources 5/23 · types 2/4 · cost $0.40`
- URL-16 (trustpilot.com/review/nn-dfysuccess.com, RC-EXA, once): 1 record — Q-E-0024. `records 24/40 · sources 6/23 · cost $0.50`
- CHECKPOINT url_index=6 records=24 cost=$0.50
- URL-20 (youtube.com/watch?v=wSQLr6dmx38, RC-YTX): 2 records — Q-Y-0025..0026. `records 26/40 · sources 7/23 · types 3/4 · cost $0.50 (+TranscriptAPI credits)`
- URL-21b (JS2lX1FFAVs, RC-YTX): 1 record — Q-Y-0027. `records 27/40 · sources 8/23`
- URL-uCubamN3o4o (RC-YTX): 2 records — Q-Y-0028..0029. `records 29/40 · sources 9/23`
- URL-pzR (pzR_ETZXAzI, RC-YTX): 3 records — Q-Y-0030, Q-Y-0039, Q-Y-0040. `records 32/40 · sources 10/23`
- URL-6MKO7iAtiAE (RC-YTX; transcript exceeded inline token limit, read via saved file and jq): 2 records — Q-Y-0031, Q-Y-0038. `records 34/40 · sources 11/23`
- URL-sSShxoEBFkY (RC-YTX): 2 records — Q-Y-0032..0033. `records 36/40 · sources 12/23`
- CHECKPOINT url_index=12 records=36 cost=$0.50 (Exa) + TranscriptAPI credits
- URL-22 (painonsocial.com/blog/shopify-problems-reddit, RC-EXA): 0 records — reason: page retrieved but no author/date shown on any quoted passage (`retrieved: true`, all 3 excerpts unattributed) → excluded per record-integrity rule (missing author+date). `URL-22: 0 records — reason: off-topic (no attributable first-person text)`. `sources 13/23 (0-yield 2)`
- URL-23 (kingy.ai BuildYourStore.ai review, RC-EXA): 1 record (weak, `[R-SNIPPET]`, no floor credit) — Q-B-0041. `sources 14/23 · types 4/4 (blog_comments now represented, though not floor-eligible)`

**Step 3 — Population + assumption passes.**
(a) CP-01 was at 0/25 after Step 2 → population-first Exa run (medium) on "full-time job + Shopify/Etsy side hustle + overwhelmed/stuck" (non-Reddit, non-Trustpilot pages): found 5 candidate pages, 3 coded as CP-01 records (Q-F-0034 Warrior Forum, Q-F-0035 TheFastlaneForum, Q-F-0036 Shopify Community) + 1 shared CP-05/CP-01 record (Q-F-0037 sharmac, coded primary CP-05 since it names "built for me" but not a full-time job). `records 37/40 · CP-01 3/25 · sources 15/23`. No exact passage combined "full-time job + Shopify/Etsy + overwhelmed by setup + wanted it built for them" in one post this leg — the closest single-element matches were kept and cited (Exa's own conclusion: "I did not find one single passage that cleanly states all requested elements together").
(b) `AS-##`: LATE-BOUND (03 does not exist this session) — no rows to route; not searched this leg.
(c) Mandatory-family / belief-probe check: `belief` tag reached 7 (≥5 floor met) via the "half-ass done" (Q-F-0002), "grasping things quicker" (Q-F-0009), Login Lab's budget-anchor quotes (Q-Y-0039/0040) — no extra search needed.
(d) No operator paste or owned survey available to this scoped agent (owned transcripts are read only by agents whose brief names them; this brief does not).

**Step 4 — Floor loop.** 3 more granular observations mined from already-fetched (not re-fetched) full transcripts of URL-6MKO7iAtiAE and URL-pzR to close PB-01's total floor and CP-05's floor (Q-Y-0038, Q-Y-0039, Q-Y-0040) — these count as `extra_sources: 0` (same source unit re-read more closely, not a new URL) per the harvester's own judgment that a full transcript already fetched is not exhausted after 1-2 quotes. `records 40/40 · CP-05 27/25 · sources 15/23`. `max_extra_sources` (8) not consumed — every addition came from a URL already in the corpus, not a new one.
Last-3-source-units check: URL-6MKO7iAtiAE, URL-pzR, URL-23 each still yielded new codes (spend, belief, objection) → continued to the box rather than calling early STRONG.

**Exit: box reached before all floors could be pursued further (≈20 min leg budget).** `FLOORS: met 3/6 · partial: [CP-01 (3/25), source_types (3 floor-eligible /4), reddit source_type (0/27 share — BLOCKED-ON-TOOL)]`

## CHECKPOINT SUMMARY
- CHECKPOINT url_index=6 records=24 cost=$0.50
- CHECKPOINT url_index=12 records=36 cost=$0.50 (Exa) + ~10 TranscriptAPI credits (6 get_youtube_transcript calls + 4 search_youtube pages across 04+06)
- CHECKPOINT url_index=15 records=40 cost=$0.90 (Exa, 9 medium runs this leg × ~$0.10) — FINAL

## Cost reconciliation
Exa agent_run this leg: 9 medium runs × $0.10 = $0.90 (URL-01, URL-07, URL-02, URL-05[0-yield], URL-15, URL-16, CP-01 population-first, URL-22[0-yield], URL-23) + earlier retry overhead: 8 calls errored on `outputSchema` (400, no charge per the error response) before falling back to plain-text queries — no cost incurred on the failed calls. Total Exa this leg: $0.90. Total Exa across 04+05+06: $0.05 (04 low) + $0.90 (06 medium) = **$0.95 of the $2.60 cap** (≈9 low-equivalent runs of budget used; well under the ≈25-low/12-medium guidance). TranscriptAPI: 4 `search_youtube` pages (2 in 04, 2 in 06) + 6 `get_youtube_transcript` calls = 10 calls, well under the 45-credit leg cap (exact credit cost per call not itemized by the tool; no error or balance warning was returned). Apify: $0.00 (BLOCKED-ON-TOOL, forced). GetHookd: not called (0 of the leg's budget, per brief). Meta: not called (no ad-comment seeds this leg, LATE-BOUND: 02.share_url).
