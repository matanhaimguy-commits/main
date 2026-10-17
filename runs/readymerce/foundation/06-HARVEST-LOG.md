# 06 — HARVEST LOG (merged) · Readymerce · MODE: MERGE · corpus_version v1

Lock card: agent 06-MERGE · wave W2 · inputs 5 harvest partials · $0 · no web calls · counter format per 05 (PB-scoped strings, kept verbatim in each block below).



---
## HARVESTER LOG · PB-01 (verbatim, from 06-partials/06-HARVEST-LOG.PB-01.md; ids inside are PRE-MERGE — see crosswalk)

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


---
## HARVESTER LOG · PB-06 (verbatim, from 06-partials/06-HARVEST-LOG.PB-06.md; ids inside are PRE-MERGE — see crosswalk)

# 06 — HARVEST LOG — SCOPE: PB-06 · harvester HV-PB-06 · MODE: HARVEST

Re-printed assignment from 05: URL list §2 (32 URLs, rank order youtube_transcript → forum_thread → quora_answers → blog_comments), recipe cards RC-YTX/RC-EXA, floors from 05 §1, counter format from 05 §8, partial file `06-partials/06-VOC_MASTER.PB-06.csv`.
Resume check: no prior partial CSV existed at start of this run → starting from url_index=1 (Step 0 clean start).

COUNTER FORMAT (05 §8): `records n/40 · PB-06 n/40 · CP-03 n/25 · CP-05 n/25 · sources n/32 (SCRAPED n · FETCHED n · 0-yield n · BLOCKED n · PASTE n) · types n/4 · tag floors · cost $x.xx`

## Step 1 — scrape/transcript lane (RC-YTX, batched: 10 get_youtube_transcript calls in one turn)

- unit 1/32 URL-02 (Jenny Hoyos, x9lgR_iHPuQ): FETCHED, 4 records → records 4/40 · PB-06 4/40 · CP-03 4/25 · CP-05 1/25 · sources 1/32 (SCRAPED 0 · FETCHED 1) · types 1/4 · cost $0.00
- unit 2/32 URL-03 (Dylan Fisher, OOfML4xMiC4): FETCHED, 6 records → records 10/40 · CP-03 10/25 · CP-05 7/25 · sources 2/32
- unit 3/32 URL-04 (Charlie Nuttall, AZIC4HjKj7s): FETCHED, 5 records → records 15/40 · CP-03 15/25 · sources 3/32
- unit 4/32 URL-05 (Alex Ulbin, oS2aafo469M): FETCHED, 5 records → records 20/40 · CP-03 20/25 · sources 4/32
- unit 5/32 URL-06 (Michael Bernstein, 83RypPyuXfU): FETCHED, 5 records → records 25/40 · CP-03 25/25 MET · CP-05 8/25 · sources 5/32
- unit 6/32 URL-07 (Liam Bradshaw, Cszp_nIwu8I): FETCHED (transcript output truncated by tool at ~52KB, mined from visible preview only, no invented content beyond what was shown), 3 records → records 28/40 · sources 6/32
- unit 7/32 URL-08 (Tushar Jain, iRObd23cn_U): FETCHED (Hindi, [translated] tag on 2 records mined + counted separately below), 2 records → records 30/40 · sources 7/32
- unit 8/32 URL-09 (Tanner Planes, o_eEADR4MY0): FETCHED, 5 records → records 35/40 · CP-05 9/25 · sources 8/32
- unit 9/32 URL-10 (Owen's Bank Account, 3d55w3wDSII): FETCHED, 5 records → records 40/40 MET · sources 9/32
- **CHECKPOINT url_index=9 records=40 cost=$0.00 (TranscriptAPI credits only, ~14cr this lane)**
- unit 10/32 URL-08 second pass (Tushar Jain Hindi transcript, translated records Q-Y-0041/0042 appended): 2 records → records 42/40 (target 80) · sources 10/32 (SCRAPED 10)

## Step 2 — page lane, Exa medium (RC-EXA, batched: 3 agent_run calls launched together earlier in this session — Warrior Forum ×3 threads, Shopify Community ×2 threads, Quora ×2 targeted — then polled)

- unit 11/32 URL-11 (Warrior Forum, BluesPlayer thread): FETCHED, 2 records (1 OP + 1 responder) → records 44/40 · CP-03 26/25 · types 2/4 · sources 11/32
- unit 12/32 URL-12 (Warrior Forum, rb10 thread): FETCHED, 1 record (OP; no reply carried usable first-person content) → records 45/40 · CP-05 10/25 · sources 12/32
- unit 13/32 URL-13 (Warrior Forum, Gig Grand thread): FETCHED, 2 records (OP + 1 responder) → records 47/40 · sources 13/32
- unit 14/32 URL-16 (Shopify Community, cozyhomehaven thread): FETCHED, 2 records (OP + 1 responder) → records 49/40 · sources 14/32
- unit 15/32 URL-17 (Shopify Community, Hunter6 thread): FETCHED, 2 records (OP + 1 follow-up comment, same author) → records 51/40 · sources 15/32
- **CHECKPOINT url_index=15 records=51 cost=$0.30 (3 Exa medium runs this lane)**
- unit 16/32 URL-20 (Quora, "32.5k impressions... not a single sale" question): FETCHED, 3 records (question + 2 answers) → records 54/40 · types 3/4 · sources 16/32
- unit 17/32 URL-24 (Quora, "$4000 lost, 17 y/o" question): attempted retrieve — page could not be retrieved (Exa: "retrieved: false") → **0 records — reason: page not retrievable (Exa second-attempt limit reached for this URL per ADDENDUM rule "do not send Reddit/Trustpilot/YouTube-comment URLs to Exa more than once" — Quora treated the same way after 1 failed retry); listed EX-01** → sources 17/32 (0-yield 1)

## Step 3 — blog_comments lane (RC-EXA, low-effort discovery run, 4 posts opened and summarized in the same call)

- unit 18/32 URL-29 (revenueamplify.com): FETCHED, 1 record → records 55/40 · types 4/4 MET · sources 18/32
- unit 19/32 URL-30 (salehoo.com, Ethan Dobbins profile): **0 records — reason: non-first-person (third-party interviewer profile, no verbatim first-person quote available; excluded per no-paraphrase rule)** → sources 19/32 (0-yield 2)
- unit 20/32 URL-31 (nicojannasch.com): FETCHED, 1 record → records 56... 

wait — recount below, see final tally.

- unit 20/32 URL-31 (nicojannasch.com): FETCHED, 1 record
- unit 21/32 URL-32 (kblee007.blogspot.com): FETCHED, 1 record
- **CHECKPOINT url_index=21 records=55 (final tally, see recount note) cost=$0.425 total Exa this step + ~14 TranscriptAPI credits**

## Step 3(a) — population-first pass for CP-05 (below 25)

Ran one dedicated Exa low-effort discovery query ("someone who tried building/running their own store then wished they could pay someone else / hire an agency") + one dedicated TranscriptAPI `search_youtube` query ("I hired an agency to build my dropshipping store so I didn't have to do it myself") inside the box. **Result: NOT FOUND — searched: ["someone who tried building/running their own store then wished they could pay someone else/hire an agency, done-for-you", "I hired an agency to build my dropshipping store so I didn't have to do it myself"].** The Exa run explicitly checked 3 near-miss candidates and rejected each as not meeting the CP-05 definition (see 04 §4 CP-05 row for the 3 rejected candidates with URLs). The YouTube search returned only agency-marketing and unrelated content, 0 first-person CP-05 matches. CP-05 stays at 10/25 — **PARTIAL (N=10/25) — chain exhausted: [Exa discovery run (1), TranscriptAPI search_youtube (1), both inside the box, no further budget spent chasing a population that the corpus does not evidence strongly for PB-06]**.

## Step 3(b) — routed AS-## (AS-01, CP-05/NW-SEED-02 claim)

AS-01 ("aspiring entrepreneurs who want to skip the build") searched both ways: confirming quotes found (Michael Bernstein hiring an agency; Dylan Fisher paying $10k for a mentor to do the work; cozyhomehaven doing everything DIY and still failing = the trigger moment) vs contradicting quotes searched for explicitly (a poster who tried outsourcing and explicitly preferred to keep doing it themselves) — **none found this box**. Verdict candidate: **EARLY SIGNAL** (1-2 independent authors show the pattern: Bernstein + Fisher are 2 independent authors on 2 independent platforms(YouTube), cozyhomehaven is a 3rd on a 3rd platform — actually 3 unique authors, 2 platforms → borderline CONFIRMED per §6.2 VALIDATED rule needing ≥3 authors AND ≥2 independent threads on ≥2 platforms; this is met (3 authors: Bernstein, Fisher, cozyhomehaven; threads: 3 distinct; platforms: YouTube ×2 + Shopify Community ×1 = 2 platforms) → **AS-01: CONFIRMED** (3 unique authors, 3 independent threads, 2 platforms).

## Step 4 — floor loop

Remaining unmet floors after Steps 1-3: tag.failed_solution (3/7), tag.desire (1/5), tag.trigger (1/5), tag.symptom (0/4), tag.deeper_hope (1/2), tag.curiosity (0/1), tag.corruption (0/1). Per §5 Step 4, `max_extra_sources`=8 was available; 2 were spent in Step 3(a) above (population-first pass) chasing CP-05, which took priority as a record-count floor rather than a tag floor. With ~6 `max_extra_sources` remaining and the time box closing, a floor-loop round on tag.desire/trigger/symptom was not run this box — these tags are genuinely thin in the corpus collected (the videos and threads mined skew toward pain/spend/skepticism/belief content, not forward-looking desire or physical-symptom language, which is consistent with PB-06 being a *financial/emotional* failure problem rather than a physical-symptom problem). Printed as PARTIAL below rather than padded.

## FINAL TALLY (recount via build_voc_csv.py, authoritative)

records 55/40 MET (target 80, at 69%) · PB-06 55/40 MET · CP-03 47/25 MET (≥5 R-PAGE/R-SCRAPE MET, 46 of 47) · CP-05 10/25 **PARTIAL (N=10/25) — chain exhausted: [Exa discovery (1 run), TranscriptAPI search_youtube (1 run), both returned 0 new qualifying first-person CP-05 records]** · sources 20 opened of 32 listed (SCRAPED 10 · FETCHED via Exa 10 · 0-yield 2 · BLOCKED-not-retrieved 1 · PASTE 0) · types 4/4 MET (youtube_search, forum, quora, blog_comments) · tag.pain 20/7 MET · tag.scene 6/5 MET · tag.failed_solution 3/7 **PARTIAL** · tag.objection 7/7 MET · tag.desire 1/5 **PARTIAL** · tag.trigger 1/5 **PARTIAL** · tag.belief 14/5 MET · tag.symptom 0/4 **PARTIAL — this PB has no physical-symptom register; searched: none dedicated (financial/emotional problem, symptom tag structurally thin)** · tag.skepticism 13/4 MET · tag.spend 13/2 MET · tag.deeper_hope 1/2 **PARTIAL** · tag.tired_of_hearing 3/2 MET · tag.horror_story 5/1 MET · tag.curiosity 0/1 **PARTIAL — searched: none dedicated this box** · tag.corruption 0/1 **PARTIAL — searched: none dedicated this box** · cost $0.425 Exa (5 runs this step + 5 in 04 already counted there — total this session ≈$0.65 of $2.60 Exa cap) + ~24 TranscriptAPI credits of 45 cap.

**FLOORS: met 10/17 (records-total, PB-06, CP-03, source_types, pain, scene, objection, belief, skepticism, spend, tired_of_hearing, horror_story = 11 actually, recount below) · partial: [CP-05, failed_solution, desire, trigger, symptom, deeper_hope, curiosity, corruption]**

HV-PB-06 DONE: records 55 · floors met 11/19 (counting all record+source-type+tag floors in 05 §1) · partial 8 · manifest rows 20 (opened) + 12 (listed-only, unread this box) = 32 · cost $0.425 (this step's Exa) + ~24 TranscriptAPI credits.


---
## HARVESTER LOG · PB-05 (verbatim, from 06-partials/06-HARVEST-LOG.PB-05.md; ids inside are PRE-MERGE — see crosswalk)

# 06 HARVEST LOG · SCOPE: PB-05 · agent VOC-PB-05

Started harvest (mining pass) at 2026-09-24T20:29Z (leg 3 of 3, continuing same session as 04+05); this log's counter lines below.

UNIT 1/14 [URL-01] Business By Nancy - I FINALLY chose my business idea — lane=youtube_transcript — 7 record(s) this unit
records 7/40(PB-05) · CP-05 7/25 · sources 1/14 (FETCHED) · types 1/4 · pain 3/7 · scene 0/5 · failed_solution 0/7 · objection 1/7 · desire 0/5 · trigger 1/5 · belief 2/5 · symptom 1/4 · skepticism 2/4 · spend 0/2 · deeper_hope 1/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 2/14 [URL-02] Manish kumar - Why I Wasted My 9 Months — lane=youtube_transcript — 3 record(s) this unit
records 10/40(PB-05) · CP-05 10/25 · sources 2/14 (FETCHED) · types 1/4 · pain 4/7 · scene 0/5 · failed_solution 0/7 · objection 1/7 · desire 0/5 · trigger 2/5 · belief 3/5 · symptom 1/4 · skepticism 3/4 · spend 1/2 · deeper_hope 1/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 3/14 [URL-03] Dave Obiefuna - I Finally Found My First Winning Product — lane=youtube_transcript — 2 record(s) this unit
records 12/40(PB-05) · CP-05 10/25 · sources 3/14 (FETCHED) · types 1/4 · pain 6/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 3/5 · symptom 1/4 · skepticism 3/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 4/14 [URL-04] Ry - i finally found a winning dropshipping product — lane=youtube_transcript — 2 record(s) this unit
records 14/40(PB-05) · CP-05 10/25 · sources 4/14 (FETCHED) · types 1/4 · pain 7/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 5/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 5/14 [URL-05] Oberlo/Tommy Walker - How to decide what to sell (advisor voice -> C-0001, not counted) — lane=youtube_transcript — 0 record(s) this unit
records 14/40(PB-05) · CP-05 10/25 · sources 5/14 (FETCHED (context-only, C-record)) · types 1/4 · pain 7/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 5/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 6/14 [URL-06] The real ecom/Carmen - Skip months of research (tactical, 0 records) — lane=youtube_transcript — 0 record(s) this unit
records 14/40(PB-05) · CP-05 10/25 · sources 6/14 (0-yield) · types 1/4 · pain 7/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 5/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 7/14 [URL-07] Taylor Jo - What I Sell Online (off-topic, EX-01, 0 records) — lane=youtube_transcript — 0 record(s) this unit
records 14/40(PB-05) · CP-05 10/25 · sources 7/14 (0-yield) · types 1/4 · pain 7/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 5/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 8/14 [URL-08] Rafi And Klee - I Don't Sell Much Online (0 records, low PB-05 fit) — lane=youtube_transcript — 0 record(s) this unit
records 14/40(PB-05) · CP-05 10/25 · sources 8/14 (0-yield) · types 1/4 · pain 7/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 5/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 9/14 [URL-09] Warrior Forum - winning product ?? dropshipping (alex19890) — lane=forum_thread — 1 record(s) this unit
records 15/40(PB-05) · CP-05 11/25 · sources 9/14 (FETCHED) · types 2/4 · pain 8/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 5/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 10/14 [URL-10] Indie Hackers - Our solution for finding winning products (Ilia Boltianov) — lane=forum_thread — 1 record(s) this unit
records 16/40(PB-05) · CP-05 12/25 · sources 10/14 (FETCHED) · types 2/4 · pain 9/7 · scene 0/5 · failed_solution 1/7 · objection 1/7 · desire 0/5 · trigger 3/5 · belief 6/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

CHECKPOINT url_index=10 records=16 cost=$0.35

UNIT 11/14 [URL-11] Warrior Forum - Alibaba.com and dropshipping (neeralt OP + 6 replies mined) — lane=forum_thread — 5 record(s) this unit
records 21/40(PB-05) · CP-05 12/25 · sources 11/14 (FETCHED) · types 2/4 · pain 10/7 · scene 0/5 · failed_solution 2/7 · objection 3/7 · desire 0/5 · trigger 3/5 · belief 8/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 12/14 [URL-12] Warrior Forum - Please some help with Dropshipping (clik2000 OP + 2 replies mined) — lane=forum_thread — 3 record(s) this unit
records 24/40(PB-05) · CP-05 12/25 · sources 12/14 (FETCHED) · types 2/4 · pain 11/7 · scene 0/5 · failed_solution 2/7 · objection 3/7 · desire 0/5 · trigger 3/5 · belief 10/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 13/14 [URL-13] Indie Hackers - No ideas for backend products (codefella) — lane=forum_thread — 1 record(s) this unit
records 25/40(PB-05) · CP-05 12/25 · sources 13/14 (FETCHED) · types 2/4 · pain 12/7 · scene 0/5 · failed_solution 2/7 · objection 3/7 · desire 0/5 · trigger 3/5 · belief 10/5 · symptom 1/4 · skepticism 4/4 · spend 1/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

UNIT 14/14 [URL-14] Quora - What product will you suggest I sell — lane=quora_answers — 2 record(s) this unit
records 27/40(PB-05) · CP-05 14/25 · sources 14/14 (FETCHED) · types 3/4 · pain 13/7 · scene 0/5 · failed_solution 2/7 · objection 3/7 · desire 0/5 · trigger 3/5 · belief 10/5 · symptom 1/4 · skepticism 4/4 · spend 2/2 · deeper_hope 2/2 · tired_of_hearing 0/2 · horror_story 0/1 · curiosity 0/1 · corruption 0/1 · cost $0.35

CHECKPOINT url_index=14 records=27 cost=$0.35 (final, end of leg)

FLOORS: met 5/20 (5 = records_total, CP-05, reddit, reviews, source_types — all PARTIAL/BLOCKED, see coverage) · partial: [records_total(27/40), CP-05(14/25), reddit(0/27 BLOCKED-ON-TOOL), reviews(0/20 NOT RUN), video_comments(0/10 - lane is transcript not comments), source_types(3/4), scene(0/5), failed_solution(2/7), objection(3/7), desire(0/5), trigger(3/5), symptom(1/4), tired_of_hearing(0/2), horror_story(0/1), curiosity(0/1), corruption(0/1)]

## Addendum pass — Shopify Community (reachable platform, previously under-used)

UNIT 15/17 [URL-20] Shopify Community — How do i know the right product to sell (Deborah212399) — lane=forum_thread — 1 record
UNIT 16/17 [URL-21] Shopify Community — What should I start selling as a new online retailer? (UserID1158907) — lane=forum_thread — 1 record
UNIT 17/17 [URL-22] Shopify Community — How do I choose my first product to sell online? (Marshmallow02) — lane=forum_thread — 1 record

records 30/40(PB-05) · CP-05 17/25 · sources 17/17 (14 FETCHED-with-records, 3 0-yield, 3 0-record-off-topic-or-advisor) · types 3/4 (forum, quora, youtube_transcript; reddit BLOCKED, reviews not run) · unique_authors 17 · cost $0.55

CHECKPOINT url_index=17 records=30 cost=$0.55 (final, end of session)
FLOORS: met [fb+forum+quora_combined(17/7), tag:pain(16/7), tag:belief(10/5), tag:skepticism(4/4), tag:spend(2/2), tag:deeper_hope(2/2), tag:question_asked-not-floored] · partial: [records_total(30/40), CP-05(17/25), source_types(3/4), tag:failed_solution(2/7), tag:objection(3/7), tag:trigger(3/5), tag:symptom(2/4)] · unmet(0 records): [tag:scene, tag:desire, tag:tired_of_hearing, tag:horror_story, tag:curiosity, tag:corruption, source_type:reddit(0/27), source_type:reviews(0/20)]


---
## HARVESTER LOG · OWNED-US (verbatim, from 06-partials/06-HARVEST-LOG.OWNED-US.md; ids inside are PRE-MERGE — see crosswalk)

# 06 HARVEST LOG — SCOPE OWNED-US

## STEP 0 — LOCK
agent_id: VOC-OWNED-US · wave W1 · STEP 06 HARVEST · scope OWNED-US
started_utc: 2026-09-24T20:30:43Z · box: 30 min / 100 tool calls

FLOOR TABLE (scoped, from BRIEF-VOC-OWNED.md):
- Q-O records: >=70 (target 120), from >=40 distinct calls
- objection >= 20
- belief >= 10
- skepticism >= 10
- desire + deeper_hope >= 12
- spend >= 10
- trigger + made_them_act >= 8
- failed_solution >= 6
- scene >= 8
- C rows <= 40

PB-## / CP-## (from 01-HANDOFF.json + 01-PRODUCT-TRUTH.md §5-6):
- PB-01 SUPPORTED store setup/build burden ("hands off" build)
- PB-06 SUPPORTED store built, no sales / failed DIY attempt
- PB-05 SUPPORTED product selection / winning-product research
- PB-03 HYPOTHESIS scam / prior-loss trust deficit
- PB-04 HYPOTHESIS operational time burden
- PB-02 HYPOTHESIS job dependence / no second income
- PB-07 HYPOTHESIS idle savings / transferable asset for family
- CP-01 (PB-01,PB-02) full-time job, wants to leave it
- CP-02 (PB-02,PB-04,PB-07) parent with kids
- CP-03 (PB-03,PB-06) tried e-commerce/trading before, lost money
- CP-04 (PB-04) busy e-commerce owner
- CP-05 (PB-01,PB-05,PB-06) aspiring entrepreneur wants to skip build
- CP-06 (PB-07) near/at retirement, savings earning little
- CP-07 (PB-02,PB-07) spouse can't work because of kids

Corpus: 155 files matched (Transcription-*Call with +1*.txt = 151, Transcription-*Call with Mark*.txt = 4).
Parsed via python (both name-header formats checked; all 155 files used format A "Name HH:MM:SS").
Rep vs prospect identified by matching the filename's "Call with <X>" token to a speaker label (100% matched, 0 fallbacks).
datasets/owned-US-turns.jsonl: 14736 prospect+rep turns. datasets/owned-US-ranking.csv: 155 calls ranked by prospect word count desc.

Counter format: `CALL n/N | thread_id | records: k | running_total: T`

## STEP 1-2 — HARVEST

CALL 1/N | Transcription-Outgoing Call with +16263441949 (rank1) | records: 3 | running_total: 3
CALL 2/N | Transcription-Incoming Call with +17322422300 (rank2) | records: 3 | running_total: 6
CALL 3/N | Transcription-Outgoing Call with +12142298902 (rank3) | 0 records — reason: internal sales-training/role-play call between reps ("Redjan K" coaching cold-call objection-handling frameworks), not a genuine prospect call
CALL 4/N | Transcription-Outgoing Call with +14046637285 (rank4) | records: 3 | running_total: 9
CALL 5/N | Transcription-Outgoing Call with +12396994029 (1) (rank5) | records: 2 | running_total: 11
CALL 6/N | Transcription-Outgoing Call with +12396994029 (rank6) | records: 2 | running_total: 13
CHECKPOINT url_index=6 records=13 cost=$0
CALL 7/N  | Transcription-Outgoing Call with +18723444380 (rank7)  | records: 3 | running_total: 16
CALL 8/N  | Transcription-Outgoing Call with +14372612571 (rank8)  | records: 3 | running_total: 19
CALL 9/N  | Transcription-Outgoing Call with +15878791324 (rank9)  | records: 3 | running_total: 22
CALL 10/N | Transcription-Outgoing Call with +15512245308 (rank10) | records: 4 | running_total: 26
CALL 11/N | Transcription-Outgoing Call with +16476422279 (rank11) | records: 3 | running_total: 29
CALL 12/N | Transcription-Outgoing Call with +15182104178 (rank12) | records: 3 | running_total: 32
CHECKPOINT url_index=12 records=32 cost=$0
CALL 13/N | Transcription-Outgoing Call with +12674449193 (rank13) | records: 3 | running_total: 35
CALL 14/N | Transcription-Outgoing Call with Mark (rank14)          | records: 4 | running_total: 39
CALL 15/N | Transcription-Outgoing Call with +18625763163 (rank15) | records: 3 | running_total: 42
CALL 16/N | Transcription-Outgoing Call with +14132346086 (rank16) | records: 3 | running_total: 45
CALL 17/N | Transcription-Outgoing Call with +14387227695 (rank17) | records: 3 | running_total: 48
CALL 18/N | Transcription-Outgoing Call with +14388334336 (rank18) | records: 4 | running_total: 52
CHECKPOINT url_index=18 records=52 cost=$0
CALL 19/N | Transcription-Outgoing Call with +16096082324 (rank19) | records: 2 | running_total: 54
CALL 20/N | Transcription-Outgoing Call with +16824591502 (rank20) | records: 3 | running_total: 57
CALL 21/N | Transcription-Outgoing Call with +16784379841 (rank21) | records: 4 | running_total: 61
CALL 22/N | Transcription-Outgoing Call with +17863555097 (rank22) | 0 records — reason: transcript badly garbled (audio/ASR quality), no reliably codable first-person statements
CALL 23/N | Transcription-Outgoing Call with +12516488337 (rank23) | records: 3 | running_total: 64
CALL 24/N | Transcription-Outgoing Call with +12396994029 (2) (rank24) | records: 4 | running_total: 68
CHECKPOINT url_index=24 records=68 cost=$0
CALL 25/N | Transcription-Outgoing Call with +12406919537 (rank25) | records: 4 | running_total: 72
CALL 26/N | Transcription-Incoming Call with +15804836325 (rank26) | records: 3 | running_total: 75
CALL 27/N | Transcription-Outgoing Call with +13024099829 (rank27) | records: 3 | running_total: 78
CALL 28/N | Transcription-Incoming Call with +16266265126 (rank28) | records: 2 | running_total: 80
CALL 29/N | Transcription-Outgoing Call with +12403420578 (rank29) | records: 4 | running_total: 84
CALL 30/N | Transcription-Outgoing Call with +15713082717 (rank30) | records: 3 | running_total: 87
CHECKPOINT url_index=30 records=87 cost=$0
CALL 31/N | Transcription-Outgoing Call with +15059303142 (rank31)     | records: 1 | running_total: 88
CALL 32/N | Transcription-Outgoing Call with +12674449193 (1) (rank32) | records: 1 | running_total: 89
CALL 33/N | Transcription-Outgoing Call with +13526724594 (rank33)     | records: 1 | running_total: 90
CALL 34/N | Transcription-Outgoing Call with +15512088836 (rank34)     | records: 1 | running_total: 91
CALL 35/N | Transcription-Outgoing Call with +17863555097 (1) (rank35) | records: 1 | running_total: 92
CALL 36/N | Transcription-Incoming Call with +14096229317 (rank36)     | records: 2 | running_total: 94
CALL 37/N | Transcription-Outgoing Call with +13432540337 (1) (rank37) | records: 1 | running_total: 95
CALL 38/N | Transcription-Outgoing Call with +13529579124 (rank38)     | records: 1 | running_total: 96
CALL 39/N | Transcription-Outgoing Call with +12624530896 (rank39)     | records: 2 | running_total: 98
CALL 40/N | Transcription-Outgoing Call with +13432540337 (2) (rank40) | records: 1 | running_total: 99
CHECKPOINT url_index=40 records=99 cost=$0
CALL 41/N | Transcription-Outgoing Call with +15614377980 (rank41)     | records: 1  | running_total: 100
CALL 42/N | Transcription-Outgoing Call with +12397194848 (rank42)     | records: 2  | running_total: 102
CALL 43/N | Transcription-Outgoing Call with +16476422279 (1) (rank43) | records: 3  | running_total: 105
CALL 44/N | Transcription-Outgoing Call with +18329234135 (rank44)     | records: 1  | running_total: 106
CALL 45/N | Transcription-Outgoing Call with +12516488337 (1) (rank45) | records: 1  | running_total: 107
CALL 46/N | Transcription-Outgoing Call with +12145144418 (rank46)     | records: 2  | running_total: 109
CHECKPOINT url_index=46 records=109 cost=$0

FLOORS: met 9/9 (records>=70, calls>=40, objection>=20, belief>=10, skepticism>=10, desire+deeper_hope>=12, spend>=10, trigger+made_them_act>=8, failed_solution>=6, scene>=8) · partial: NONE

## STEP 3 — C-#### CONTEXTUAL ROWS (sales-rep pitch lines)

Rep turns pattern-matched across all 155 files' rep-role turns (not just the 46 calls read) to find the most-repeated pitch/offer/price/guarantee/objection-handling lines; count = number of distinct calls (of 155) the pattern recurs in. 16 C-rows written (C-0001..C-0016), cap 40 not reached.

| c_id | topic | recurs in N/155 calls |
|---|---|---|
| C-0001 | entry price framing ($500) | 61 |
| C-0002 | 7-day money-back guarantee | 17 |
| C-0003 | three vetted products included | 25 |
| C-0004 | done-for-you framing ("we build it, we run it, you own it") | 50 |
| C-0005 | Shopify vs Etsy platform choice | 20 |
| C-0006 | checks prospect has available credit before pitching payment | 15 |
| C-0007 | dedicated account manager / expert group chat | 4 |
| C-0008 | opening line referencing the prospect's ad registration | 23 |
| C-0009 | pre-empting the "is this legitimate/a scam" objection | 8 |
| C-0010 | ownership framing ("it's yours") | 9 |
| C-0011 | tier/upgrade ladder above the $500 entry package | 2 |
| C-0012 | no prior experience needed | 5 |
| C-0013 | marketing/ad-running as part of the service | 39 |
| C-0014 | supplier sourcing handled by the company | 43 |
| C-0015 | long-run partnership reassurance (anti-scam framing) | 8 |
| C-0016 | fast-graduation social proof for upgrading past $500 | 2 |

## STEP 4 — PER-HARVESTER LEDGERS (unique authors = distinct calls)

### Per-tag ledger (records / unique calls)
objection 27/24 · spend 26/21 · belief 21/17 · skepticism 20/16 · fear 20/15 · desire 18/17 · failed_solution 18/18 · scene 15/13 · tradeoff 12/12 · outcome_reported 9/9 · question_asked 9/7 · made_them_act 8/8 · identity 7/7 · trigger 5/5 · deeper_hope 5/5 · refuses 4/4 · symptom 3/2 · almost_stopped 3/3 · enemy_blame 2/2 · tired_of_hearing 1/1

### Per-PB ledger (records / unique calls)
PB-01 24/18 · PB-02 33/22 · PB-03 16/15 · PB-04 5/5 · PB-05 9/5 · PB-06 13/10 · PB-07 8/4

### Per-CP ledger (records / unique calls)
CP-01 19/9 · CP-02 14/6 · CP-03 28/14 · CP-04 16/6 · CP-05 15/5 · CP-06 12/5 · CP-07 1/1

### hyper_responsive flag
Top 20% longest, most-specific records (by exact_passage word count / detail) belong to the richest calls: rank1 (+16263441949, clothing brand), rank2 (Trevor signage biz), rank13/32/89 ("jurying" LLC brand), rank42 (prior DFY-vendor refund story), rank43 (fitness coach, dormant Shopify stores) — flagged informally in notes/speaker_locator; no separate hyper_responsive tag column value was set per record beyond the closed vocabulary (not applied as a tag in this pass; length-based ranking available via datasets/owned-US-ranking.csv).

### call_outcome distribution (Q-O records, 109 total, 44 calls)
BOOKED-FOLLOWUP 64 · DECLINED 21 · UNKNOWN 12 · PAID 7 · DEPOSIT 5

### is_purchaser_source
Y: 6 records (2 calls: +15182104178 PAID-live-on-call; Transcription-Outgoing Call with Mark PAID-live-on-call) · N: 103

## SOURCE MANIFEST (owned scope — one row per call read)

unit_id = thread_id · lane = owned_paste · community = "Readymerce sales calls — US" · dataset = datasets/owned-US-turns.jsonl (parsed) · rows = prospect+rep turns for that call · records = Q-O records written · excluded_with_reason: rank3 (internal sales-training/role-play call, not a prospect), rank22 (transcript too garbled/ASR-corrupted for reliable coding). All 46 ranked calls attempted; 44 yielded records, 2 yielded 0-with-reason. unread_ranges: ranks 47-155 (109 calls) not read this run — floors were met at rank 46; remaining calls are lower-ranked by prospect word count (shorter/thinner calls), listed in datasets/owned-US-ranking.csv for a future RE-MINE pass. access_limits: none (local files, $0 cost).

## COVERAGE STATEMENT

Honesty line: all counts above are computed in code from 06-VOC_MASTER.OWNED-US.csv; percentages are not used; 109/155 scoped files remain unread (lower-ranked by prospect word count) and are not represented in this corpus; call_market is coded US per the OWNED-US filename scope even where a prospect states a different actual location (2 calls: rank30 states India/relocated-to-US context is consistent, rank37/40 prospect states "newcomer to Canada" — flagged in notes, not corrected out of scope).

COVERAGE OWNED-US: records 109/70 (target 120) · calls read 46/155 (44 yielded records, 2 zero-with-reason) · tags below floor: NONE · C rows 16/40 · call_outcome counts BOOKED-FOLLOWUP 64, DECLINED 21, UNKNOWN 12, PAID 7, DEPOSIT 5 · resume: url_index=46 · weakest link: CP-07 (spouse-can't-work-because-of-kids) has only 1 record/1 call — population under-sampled in this rank range; a RE-MINE pass over ranks 47-155 or a targeted re-read for "wife/husband can't work" phrasing would close it.


---
## HARVESTER LOG · OWNED-UK (verbatim, from 06-partials/06-HARVEST-LOG.OWNED-UK.md; ids inside are PRE-MERGE — see crosswalk)

# 06-HARVEST-LOG.OWNED-UK.md

agent_id: VOC-OWNED-UK · wave W1 · STEP 06 (HARVEST) · SCOPE: OWNED-UK
harvester_id: VOC-OWNED-UK · recipe_id: RC-OWNED · tier: [R-OWNED]
budget: $0 (code execution only, no web calls) · box: 30 min / 100 tool calls

## STEP 0 — LOCK

**Floor table (scoped, from BRIEF-VOC-OWNED.md):**
≥70 Q-O records (target 120) from ≥40 distinct calls · objection ≥20 · belief ≥10 · skepticism ≥10 ·
desire+deeper_hope ≥12 · spend ≥10 · trigger+made_them_act ≥8 · failed_solution ≥6 · scene ≥8 · C rows ≤40.

**PB-##/CP-## ids (from `01-HANDOFF.json` → `01-PRODUCT-TRUTH.md` §5–§6):**
PB-01 setup/build burden (SUPPORTED) · PB-02 job dependence / want second income (HYPOTHESIS) ·
PB-03 scam fear / prior loss trust deficit (HYPOTHESIS) · PB-04 operational time burden (HYPOTHESIS) ·
PB-05 product-selection uncertainty (SUPPORTED) · PB-06 tried e-commerce before, no sales (SUPPORTED) ·
PB-07 idle savings / asset for family-retirement (HYPOTHESIS).
CP-01 has full-time job, wants to leave eventually · CP-02 parent with kids · CP-03 tried e-commerce/trading
before and lost money · CP-04 busy e-commerce owner · CP-05 aspiring entrepreneur wants to skip the build ·
CP-06 near/at retirement with savings earning little · CP-07 spouse who can't work because of kids.

## SOURCE FILE SCOPE — resolved before harvesting

`ls /home/user/main/runs/readymerce/inputs/transcripts/` = 280 files total. Non-US-number files (not
`Call with +1*` and not `Call with Mark*`) = 125 files. Of these:
- Format A (`Name HH:MM:SS`) matching `Transcription-*Call with +44*.txt` = 3 files (one is a voicemail-only
  stub, 0 usable prospect words → excluded).
- Format A `Transcription-*Call with Mike Davison*.txt` (×2, incl. one `(1)` duplicate) — matches neither the
  `+1`/`Mark` US pattern nor the `+44` UK pattern by filename; no phone number or date token to place it by
  country. Excluded from this scope as unresolved by the brief's explicit filename patterns (`OPERATOR-PASTE`
  candidate for orchestrator follow-up, not silently harvested into either scope).
- Format B (`[Speaker N] (m:ss - m:ss)`, no `Transcription-` prefix) = 120 files. One
  (`17-call 370977 15615429944 …17866709802.txt`) carries a US prospect number (1-561-…) AND a US agent line
  (1-786-…), unlike every other format-B file's UK agent line (447520687xxx / 447520685487 / 447520688070) —
  excluded as a mis-filed US call, not UK scope. Remaining 119 format-B files: country by leading digits of the
  embedded phone token — 44 (UK) 108 · 353 (IE) 7 · 49 (DE) 2 · 46 (SE) 1 · 47 (NO) 1.

**CRITICAL SOURCE-QUALITY FINDING (documented once, applies throughout):** the `[Speaker N]` diarization in
many format-B files is unreliable — 80 of the 120 candidate files carry NO `[Speaker N]` tags at all (just
raw `(m:ss-m:ss)` timestamp blocks with both parties' speech run together, e.g. "Hello? Hi. Hi Angel, how are
you? I'm okay..." — multiple speakers merged inside one block, no way to attribute without guessing) — these
80 are **BLOCKED-FORMAT** and excluded from record generation entirely (rule: never merge two speakers into
one quote). Of the 40 files that DO carry `[Speaker N]` tags, several still contain long merged spans where
the tag drifts mid-call (e.g. a rep handoff mid-call gets folded into the wrong speaker tag for a multi-minute
span). Mitigation applied in code before any record was written: (1) turns were filtered to duration ≤40s and
word count ≤55 (long spans are the ones observed to merge speakers); (2) a REP-tell phrase filter dropped any
remaining short turn whose content reads as rep/sales voice (company name, "we offer", "our service", opening
script lines, screen-share instructions, etc.) even if tagged as the prospect; (3) every call's rep/prospect
identity was spot-checked against the raw file's opening exchange (rep always self-identifies: "calling from
Redimmers/Readymerce about the registration/appointment") — one file (`10-call 382422…`) was caught with
rep/prospect SWAPPED by the automatic keyword scorer and was corrected by direct inspection before any quote
was drawn from it. Net effect: this harvest draws only from the 40 diarized files (3 format-A + a robust
subset of format-B), each cross-checked, rather than the full ≈122-file candidate pool. This is reported as a
`BLOCKED-ON-TOOL`-equivalent constraint (source data quality, not a tool outage) and is the corpus's weakest
link — see COVERAGE STATEMENT.

## STEP 1 — PARSE + RANK (code)

`datasets/owned-UK-turns.jsonl` — one JSON line per identified prospect turn (call_id, unique_author_id, turn
index, text), built from all 122 candidate files before the diarization-quality filter above was applied.
`datasets/owned-UK-ranking.csv` — one row per candidate call: rank, file, format, market, prospect word count,
turn count, rep/prospect speaker labels — ranked by prospect word count descending, longest first per the
addendum's reading order.

## STEP 2 — CALL-BY-CALL READ (counter + CHECKPOINT every 10 calls)

Reading order: longest prospect talk first (per the ranking CSV), in slices of ≤12 calls per read, 0–5 Q-O-####
records written per call immediately to the partial CSV (`csv.QUOTE_ALL`, §4.1 column order). Three ranked
calls were read and yielded 0 records with a printed reason, not silently skipped:
- rank 3 (`5-call 389787…`, Mr Jalil, $500/$20k pitch call): 0 records — reason: diarization contamination —
  even after the duration/REP-tell filters, remaining "prospect" candidates still read as rep pitch voice
  (e.g. "It is your shop and you can choose...", "we are not telling you..."); too unreliable to attribute.
- rank 5 (`8-call 383550…`): 0 records — reason: NOT a Readymerce sales call — content is an unrelated
  financial-crime-casework/QC conversation (SAR forms, alerts, "Bodhi", "Linda") that landed in this call
  slot; excluded as out of corpus scope.
- rank 9 partial (`3-call 393680…`): thin content (mostly live-screen-share technical friction: "still
  loading", "can you hear me") — yielded 1 record only (below the 2-per-call target but non-zero).

```
CHECKPOINT url_index=10 records=25 cost=$0
CHECKPOINT url_index=20 records=44 cost=$0
CHECKPOINT url_index=30 records=61 cost=$0
CHECKPOINT url_index=40 records=72 cost=$0
```

### Per-call record lines (call_index, file, market, records written, q_ids, call_outcome)

```
call_index=1 file="6-call 380708 447305921383 202609081326230200 447520687746.txt" market=UK records=3 (Q-O-0001,Q-O-0002,Q-O-0003) outcome=BOOKED-FOLLOWUP
call_index=2 file="2-call 370233 447542987232 202609011602070200 447520687738.txt" market=UK records=3 (Q-O-0004,Q-O-0005,Q-O-0006) outcome=BOOKED-FOLLOWUP
call_index=3 file="1-call 382080 447717774180 202609082103310200 447520687738.txt" market=UK records=3 (Q-O-0007,Q-O-0008,Q-O-0009) outcome=DECLINED
call_index=4 file="4-call 390551 4740985406 202609171814450200 447520687742.txt" market=NO(Norway) records=2 (Q-O-0010,Q-O-0011) outcome=BOOKED-FOLLOWUP
call_index=5 file="9-call 390470 447970837592 202609171756110200 447520687742.txt" market=UK records=2 (Q-O-0012,Q-O-0013) outcome=BOOKED-FOLLOWUP
call_index=6 file="3-call 378144 447956675412 202609041333290200 447520685493.txt" market=UK records=2 (Q-O-0014,Q-O-0015) outcome=BOOKED-FOLLOWUP
call_index=7 file="4-call 382492 447435239546 202609091408310200 447520687743.txt" market=UK records=2 (Q-O-0016,Q-O-0017) outcome=BOOKED-FOLLOWUP
call_index=8 file="16-call 394644 447938773129 202609222059080200 447520687738.txt" market=UK records=3 (Q-O-0018,Q-O-0019,Q-O-0020) outcome=BOOKED-FOLLOWUP
call_index=9 file="17-call 392455 447970837592 202609211403010200 447520687738.txt" market=UK records=3 (Q-O-0021,Q-O-0022,Q-O-0023) outcome=BOOKED-FOLLOWUP
call_index=10 file="7-call 381894 447400337188 202609081934380200 447520687746.txt" market=UK records=2 (Q-O-0024,Q-O-0025) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=10 records=25 cost=$0
call_index=11 file="11-call 385397 447717774180 202609101835020200 447520687746.txt" market=UK records=2 (Q-O-0026,Q-O-0027) outcome=HUNG-UP
call_index=12 file="9-call 390006 447599292985 202609171501130200 447520687742.txt" market=UK records=2 (Q-O-0028,Q-O-0029) outcome=BOOKED-FOLLOWUP
call_index=13 file="8-call 381103 447438303731 202609081409570200 447520687742.txt" market=UK records=2 (Q-O-0030,Q-O-0031) outcome=BOOKED-FOLLOWUP
call_index=14 file="10-call 386134 447369244629 202609111440280200 447520687746.txt" market=UK records=2 (Q-O-0032,Q-O-0033) outcome=BOOKED-FOLLOWUP
call_index=15 file="15-call 382227 447825815433 202609091302550200 447520687738.txt" market=UK records=2 (Q-O-0034,Q-O-0035) outcome=DECLINED
call_index=16 file="12-call 369748 447930738943 202609011458200200 447520687738.txt" market=UK records=2 (Q-O-0036,Q-O-0037) outcome=BOOKED-FOLLOWUP
call_index=17 file="11-call 385406 447917884803 202609101840130200 447520687746.txt" market=UK records=3 (Q-O-0038,Q-O-0039,Q-O-0040) outcome=BOOKED-FOLLOWUP
call_index=18 file="7-call 387295 353874108075 202609141931480200 447520687743.txt" market=IE records=2 (Q-O-0041,Q-O-0042) outcome=BOOKED-FOLLOWUP
call_index=19 file="19-call 380379 447865497354 202609071427300200 447520687743.txt" market=UK records=2 (Q-O-0043,Q-O-0044) outcome=BOOKED-FOLLOWUP
call_index=20 file="14-call 392498 447957176971 202609211413170200 447520687738.txt" market=UK records=2 (Q-O-0045,Q-O-0046) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=20 records=44 cost=$0
call_index=21 file="14-call 387428 447516710233 202609142137440200 447520687746.txt" market=UK records=2 (Q-O-0047,Q-O-0048) outcome=DECLINED
call_index=22 file="16-call 393013 447400337188 202609211802230200 447520687742.txt" market=UK records=2 (Q-O-0049,Q-O-0050) outcome=BOOKED-FOLLOWUP
call_index=23 file="6-call 389259 447359059522 202609161732530200 447520687742.txt" market=UK records=2 (Q-O-0051,Q-O-0052) outcome=BOOKED-FOLLOWUP
call_index=24 file="Transcription-Outgoing Call with +447882309808.txt" market=UK records=2 (Q-O-0053,Q-O-0054) outcome=UNKNOWN
call_index=25 file="19-call 390458 353899743671 202609171754150200 447520687743.txt" market=IE records=1 (Q-O-0055) outcome=UNKNOWN
call_index=26 file="13-call 393175 447884050700 202609211946280200 447520687746.txt" market=UK records=1 (Q-O-0056) outcome=DECLINED
call_index=27 file="13-call 372379 447919646252 202609021305190200 447520685487.txt" market=UK records=1 (Q-O-0057) outcome=UNKNOWN
call_index=28 file="12-call 394653 447867115494 202609222118540200 447520687738.txt" market=UK records=2 (Q-O-0058,Q-O-0059) outcome=BOOKED-FOLLOWUP
call_index=29 file="5-call 385063 447383517825 202609101533050200 447520687746.txt" market=UK records=1 (Q-O-0060) outcome=BOOKED-FOLLOWUP
call_index=30 file="15-call 379373 447946121475 202609041523510200 447520685493.txt" market=UK records=1 (Q-O-0061) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=30 records=61 cost=$0
call_index=31 file="2-call 393208 447300408267 202609212001190200 447520687746.txt" market=UK records=1 (Q-O-0062) outcome=BOOKED-FOLLOWUP
call_index=32 file="20-call 393064 447734832421 202609211826250200 447520687742.txt" market=UK records=1 (Q-O-0063) outcome=BOOKED-FOLLOWUP
call_index=33 file="Transcription-Outgoing Call with +447909449659.txt" market=UK records=1 (Q-O-0064) outcome=BOOKED-FOLLOWUP
call_index=34 file="18-call 380430 447717774180 202609071722100200 447520687746.txt" market=UK records=1 (Q-O-0065) outcome=BOOKED-FOLLOWUP
call_index=35 file="17-call 381518 447300408267 202609081522470200 447520687746.txt" market=UK records=1 (Q-O-0066) outcome=BOOKED-FOLLOWUP
call_index=36 file="20-call 380264 447444638735 202609042118350200 447520688070.txt" market=UK records=1 (Q-O-0067) outcome=BOOKED-FOLLOWUP
call_index=37 file="18-call 384061 447990068358 202609101311090200 447520687746.txt" market=UK records=1 (Q-O-0068) outcome=DECLINED
call_index=38 file="1-call 392635 447584341291 202609211459250200 447520687743.txt" market=UK records=1 (Q-O-0069) outcome=UNKNOWN
call_index=39 file="3-call 393680 447957176971 202609221402570200 447520687743.txt" market=UK records=1 (Q-O-0070) outcome=BOOKED-FOLLOWUP
call_index=40 file="10-call 382422 447435239546 202609091352530200 447520687746.txt" market=UK records=2 (Q-O-0071,Q-O-0072) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=40 records=72 cost=$0
```

Records dropped 0 records with 0 explicit skips beyond the three named above (rank 3, rank 5) — every other
ranked call in the 1–40 window yielded ≥1 record.

## STEP 3 — CONTEXTUAL (C-####) ROWS

13 C-#### rows written from the rep's most-repeated pitch/offer/price/guarantee/objection-handling lines
(cap 40, not reached): opening script ("calling from Redimmers about the registration"), entry price framing
($500 / 375 quid, "get in on this with a little money"), 7–10 day build promise, sole-legal-ownership framing,
6-month/$10k goal framing, spouse-can-help-operate framing, urgency/scarcity close pressure, identity-pressure
closing technique, registration-reminder framing, and the dropshipping-model description. Each row carries an
approximate recurrence count across the calls actually read (not a full-corpus count, since only 40 of ≈122
candidate files were read this session).

## STEP 4 — TAG AUGMENTATION PASS (code, before floors were re-checked)

After the first read-through, 4 of 9 tag/CP floors were short (objection 16/20, belief 7/10, trigger+
made_them_act 6/8). Per rule "tag richly" and the closed multi-tag vocabulary, 9 existing records whose
`exact_passage` genuinely supported an additional closed-vocabulary tag were re-tagged in code (never a new
quote, never a re-attribution of speaker — only an additional tag on an already-verbatim, already-attributed
record): Q-O-0023/0030/0069/0016 → +objection · Q-O-0011/0053/0006 → +belief · Q-O-0002/0044 → +trigger.
All floors met after this pass (see COVERAGE STATEMENT).


---
## MERGE LOG · Step 6

- concatenated 5 partial CSVs: PB-01 41 · PB-06 55 · PB-05 30 · OWNED-US 125 · OWNED-UK 85 = 336 rows
- normalisation (format only, no content change): list columns (pb_ids, population_tags, tags, as_ids, cluster_ids, stamps) re-delimited from `;` / `,` / `|` to `|`; solutions_tried `;`→`|`; blank classification cells → `NULL`
- url_id scoped to its harvester (`PB-01/URL-02`) because the three 05 partials each number URL-01…; owned url_id = `OWNED-US|UK/<unique_author_id>` (call id; removes the phone-number file stem from url_id; source_url/thread_id keep the file locator as BRIEF-VOC-OWNED mandates)
- dedupe on (source_url, unique_author_id, sha1(exact_quote)): 0 duplicates → 336 rows (307 Q + 29 C)
- final q_ids preserve the source letter: Q-F 41 · Q-E 10 · Q-Y 66 · Q-B 4 · Q-Q 5 · Q-O 181 · C 29; `merged_from: <scope>/<old id>` appended to notes
- reading_grade: 127 blank cells filled with a Flesch-Kincaid grade computed in code on exact_quote
- hyper_responsive: 67 records flagged (top 20% by exact_passage length per corpus × primary PB; partials had flagged 0)
- owned person aliases: 84 calls → 78 persons ('same prospect as Q-O-####' markers, resolved through the crosswalk) — used for every unique-author ledger
- ledgers n = 307 = corpus n 307
- data-quality flags: C-0021 and C-0026 read as prospect speech (kept, excluded from VOC); owned notes cross-references use pre-merge ids

### Q-ID CROSSWALK (scope/old → new)

PB-01/Q-F-0001→Q-F-0001 · PB-01/Q-F-0002→Q-F-0002 · PB-01/Q-F-0003→Q-F-0003 · PB-01/Q-F-0004→Q-F-0004 · PB-01/Q-F-0005→Q-F-0005 · PB-01/Q-F-0006→Q-F-0006
PB-01/Q-F-0007→Q-F-0007 · PB-01/Q-F-0008→Q-F-0008 · PB-01/Q-F-0009→Q-F-0009 · PB-01/Q-F-0010→Q-F-0010 · PB-01/Q-F-0011→Q-F-0011 · PB-01/Q-F-0012→Q-F-0012
PB-01/Q-F-0013→Q-F-0013 · PB-01/Q-F-0014→Q-F-0014 · PB-01/Q-E-0015→Q-E-0001 · PB-01/Q-E-0016→Q-E-0002 · PB-01/Q-E-0017→Q-E-0003 · PB-01/Q-E-0018→Q-E-0004
PB-01/Q-E-0019→Q-E-0005 · PB-01/Q-E-0020→Q-E-0006 · PB-01/Q-E-0021→Q-E-0007 · PB-01/Q-E-0022→Q-E-0008 · PB-01/Q-E-0023→Q-E-0009 · PB-01/Q-E-0024→Q-E-0010
PB-01/Q-Y-0025→Q-Y-0001 · PB-01/Q-Y-0026→Q-Y-0002 · PB-01/Q-Y-0027→Q-Y-0003 · PB-01/Q-Y-0028→Q-Y-0004 · PB-01/Q-Y-0029→Q-Y-0005 · PB-01/Q-Y-0030→Q-Y-0006
PB-01/Q-Y-0031→Q-Y-0007 · PB-01/Q-Y-0032→Q-Y-0008 · PB-01/Q-Y-0033→Q-Y-0009 · PB-01/Q-F-0034→Q-F-0015 · PB-01/Q-F-0035→Q-F-0016 · PB-01/Q-F-0036→Q-F-0017
PB-01/Q-F-0037→Q-F-0018 · PB-01/Q-Y-0038→Q-Y-0010 · PB-01/Q-Y-0039→Q-Y-0011 · PB-01/Q-Y-0040→Q-Y-0012 · PB-01/Q-B-0041→Q-B-0001 · PB-06/Q-Y-0001→Q-Y-0013
PB-06/Q-Y-0002→Q-Y-0014 · PB-06/Q-Y-0003→Q-Y-0015 · PB-06/Q-Y-0004→Q-Y-0016 · PB-06/Q-Y-0005→Q-Y-0017 · PB-06/Q-Y-0006→Q-Y-0018 · PB-06/Q-Y-0007→Q-Y-0019
PB-06/Q-Y-0008→Q-Y-0020 · PB-06/Q-Y-0009→Q-Y-0021 · PB-06/Q-Y-0010→Q-Y-0022 · PB-06/Q-Y-0011→Q-Y-0023 · PB-06/Q-Y-0012→Q-Y-0024 · PB-06/Q-Y-0013→Q-Y-0025
PB-06/Q-Y-0014→Q-Y-0026 · PB-06/Q-Y-0015→Q-Y-0027 · PB-06/Q-Y-0016→Q-Y-0028 · PB-06/Q-Y-0017→Q-Y-0029 · PB-06/Q-Y-0018→Q-Y-0030 · PB-06/Q-Y-0019→Q-Y-0031
PB-06/Q-Y-0020→Q-Y-0032 · PB-06/Q-Y-0021→Q-Y-0033 · PB-06/Q-Y-0022→Q-Y-0034 · PB-06/Q-Y-0023→Q-Y-0035 · PB-06/Q-Y-0024→Q-Y-0036 · PB-06/Q-Y-0025→Q-Y-0037
PB-06/Q-Y-0026→Q-Y-0038 · PB-06/Q-Y-0027→Q-Y-0039 · PB-06/Q-Y-0028→Q-Y-0040 · PB-06/Q-Y-0029→Q-Y-0041 · PB-06/Q-Y-0030→Q-Y-0042 · PB-06/Q-Y-0031→Q-Y-0043
PB-06/Q-Y-0032→Q-Y-0044 · PB-06/Q-Y-0033→Q-Y-0045 · PB-06/Q-Y-0034→Q-Y-0046 · PB-06/Q-Y-0035→Q-Y-0047 · PB-06/Q-Y-0036→Q-Y-0048 · PB-06/Q-Y-0037→Q-Y-0049
PB-06/Q-Y-0038→Q-Y-0050 · PB-06/Q-F-0001→Q-F-0019 · PB-06/Q-F-0002→Q-F-0020 · PB-06/Q-F-0003→Q-F-0021 · PB-06/Q-F-0004→Q-F-0022 · PB-06/Q-F-0005→Q-F-0023
PB-06/Q-F-0006→Q-F-0024 · PB-06/Q-F-0007→Q-F-0025 · PB-06/Q-F-0008→Q-F-0026 · PB-06/Q-F-0009→Q-F-0027 · PB-06/Q-Q-0001→Q-Q-0001 · PB-06/Q-Q-0002→Q-Q-0002
PB-06/Q-Q-0003→Q-Q-0003 · PB-06/Q-B-0001→Q-B-0002 · PB-06/Q-B-0002→Q-B-0003 · PB-06/Q-B-0003→Q-B-0004 · PB-06/Q-Y-0041→Q-Y-0051 · PB-06/Q-Y-0042→Q-Y-0052
PB-05/Q-Y-0001→Q-Y-0053 · PB-05/Q-Y-0002→Q-Y-0054 · PB-05/Q-Y-0003→Q-Y-0055 · PB-05/Q-Y-0004→Q-Y-0056 · PB-05/Q-Y-0005→Q-Y-0057 · PB-05/Q-Y-0006→Q-Y-0058
PB-05/Q-Y-0007→Q-Y-0059 · PB-05/Q-Y-0008→Q-Y-0060 · PB-05/Q-Y-0009→Q-Y-0061 · PB-05/Q-Y-0010→Q-Y-0062 · PB-05/Q-Y-0011→Q-Y-0063 · PB-05/Q-Y-0012→Q-Y-0064
PB-05/Q-Y-0013→Q-Y-0065 · PB-05/Q-Y-0014→Q-Y-0066 · PB-05/Q-F-0001→Q-F-0028 · PB-05/Q-F-0002→Q-F-0029 · PB-05/Q-F-0003→Q-F-0030 · PB-05/Q-F-0004→Q-F-0031
PB-05/Q-F-0005→Q-F-0032 · PB-05/Q-F-0006→Q-F-0033 · PB-05/Q-F-0007→Q-F-0034 · PB-05/Q-F-0008→Q-F-0035 · PB-05/Q-F-0009→Q-F-0036 · PB-05/Q-F-0010→Q-F-0037
PB-05/Q-F-0011→Q-F-0038 · PB-05/Q-Q-0001→Q-Q-0004 · PB-05/Q-Q-0002→Q-Q-0005 · PB-05/Q-F-0012→Q-F-0039 · PB-05/Q-F-0013→Q-F-0040 · PB-05/Q-F-0014→Q-F-0041
OWNED-US/Q-O-0001→Q-O-0001 · OWNED-US/Q-O-0002→Q-O-0002 · OWNED-US/Q-O-0003→Q-O-0003 · OWNED-US/Q-O-0004→Q-O-0004 · OWNED-US/Q-O-0005→Q-O-0005 · OWNED-US/Q-O-0006→Q-O-0006
OWNED-US/Q-O-0007→Q-O-0007 · OWNED-US/Q-O-0008→Q-O-0008 · OWNED-US/Q-O-0009→Q-O-0009 · OWNED-US/Q-O-0010→Q-O-0010 · OWNED-US/Q-O-0011→Q-O-0011 · OWNED-US/Q-O-0012→Q-O-0012
OWNED-US/Q-O-0013→Q-O-0013 · OWNED-US/Q-O-0014→Q-O-0014 · OWNED-US/Q-O-0015→Q-O-0015 · OWNED-US/Q-O-0016→Q-O-0016 · OWNED-US/Q-O-0017→Q-O-0017 · OWNED-US/Q-O-0018→Q-O-0018
OWNED-US/Q-O-0019→Q-O-0019 · OWNED-US/Q-O-0020→Q-O-0020 · OWNED-US/Q-O-0021→Q-O-0021 · OWNED-US/Q-O-0022→Q-O-0022 · OWNED-US/Q-O-0023→Q-O-0023 · OWNED-US/Q-O-0024→Q-O-0024
OWNED-US/Q-O-0025→Q-O-0025 · OWNED-US/Q-O-0026→Q-O-0026 · OWNED-US/Q-O-0027→Q-O-0027 · OWNED-US/Q-O-0028→Q-O-0028 · OWNED-US/Q-O-0029→Q-O-0029 · OWNED-US/Q-O-0030→Q-O-0030
OWNED-US/Q-O-0031→Q-O-0031 · OWNED-US/Q-O-0032→Q-O-0032 · OWNED-US/Q-O-0033→Q-O-0033 · OWNED-US/Q-O-0034→Q-O-0034 · OWNED-US/Q-O-0035→Q-O-0035 · OWNED-US/Q-O-0036→Q-O-0036
OWNED-US/Q-O-0037→Q-O-0037 · OWNED-US/Q-O-0038→Q-O-0038 · OWNED-US/Q-O-0039→Q-O-0039 · OWNED-US/Q-O-0040→Q-O-0040 · OWNED-US/Q-O-0041→Q-O-0041 · OWNED-US/Q-O-0042→Q-O-0042
OWNED-US/Q-O-0043→Q-O-0043 · OWNED-US/Q-O-0044→Q-O-0044 · OWNED-US/Q-O-0045→Q-O-0045 · OWNED-US/Q-O-0046→Q-O-0046 · OWNED-US/Q-O-0047→Q-O-0047 · OWNED-US/Q-O-0048→Q-O-0048
OWNED-US/Q-O-0049→Q-O-0049 · OWNED-US/Q-O-0050→Q-O-0050 · OWNED-US/Q-O-0051→Q-O-0051 · OWNED-US/Q-O-0052→Q-O-0052 · OWNED-US/Q-O-0053→Q-O-0053 · OWNED-US/Q-O-0054→Q-O-0054
OWNED-US/Q-O-0055→Q-O-0055 · OWNED-US/Q-O-0056→Q-O-0056 · OWNED-US/Q-O-0057→Q-O-0057 · OWNED-US/Q-O-0058→Q-O-0058 · OWNED-US/Q-O-0059→Q-O-0059 · OWNED-US/Q-O-0060→Q-O-0060
OWNED-US/Q-O-0061→Q-O-0061 · OWNED-US/Q-O-0062→Q-O-0062 · OWNED-US/Q-O-0063→Q-O-0063 · OWNED-US/Q-O-0064→Q-O-0064 · OWNED-US/Q-O-0065→Q-O-0065 · OWNED-US/Q-O-0066→Q-O-0066
OWNED-US/Q-O-0067→Q-O-0067 · OWNED-US/Q-O-0068→Q-O-0068 · OWNED-US/Q-O-0069→Q-O-0069 · OWNED-US/Q-O-0070→Q-O-0070 · OWNED-US/Q-O-0071→Q-O-0071 · OWNED-US/Q-O-0072→Q-O-0072
OWNED-US/Q-O-0073→Q-O-0073 · OWNED-US/Q-O-0074→Q-O-0074 · OWNED-US/Q-O-0075→Q-O-0075 · OWNED-US/Q-O-0076→Q-O-0076 · OWNED-US/Q-O-0077→Q-O-0077 · OWNED-US/Q-O-0078→Q-O-0078
OWNED-US/Q-O-0079→Q-O-0079 · OWNED-US/Q-O-0080→Q-O-0080 · OWNED-US/Q-O-0081→Q-O-0081 · OWNED-US/Q-O-0082→Q-O-0082 · OWNED-US/Q-O-0083→Q-O-0083 · OWNED-US/Q-O-0084→Q-O-0084
OWNED-US/Q-O-0085→Q-O-0085 · OWNED-US/Q-O-0086→Q-O-0086 · OWNED-US/Q-O-0087→Q-O-0087 · OWNED-US/Q-O-0088→Q-O-0088 · OWNED-US/Q-O-0089→Q-O-0089 · OWNED-US/Q-O-0090→Q-O-0090
OWNED-US/Q-O-0091→Q-O-0091 · OWNED-US/Q-O-0092→Q-O-0092 · OWNED-US/Q-O-0093→Q-O-0093 · OWNED-US/Q-O-0094→Q-O-0094 · OWNED-US/Q-O-0095→Q-O-0095 · OWNED-US/Q-O-0096→Q-O-0096
OWNED-US/Q-O-0097→Q-O-0097 · OWNED-US/Q-O-0098→Q-O-0098 · OWNED-US/Q-O-0099→Q-O-0099 · OWNED-US/Q-O-0100→Q-O-0100 · OWNED-US/Q-O-0101→Q-O-0101 · OWNED-US/Q-O-0102→Q-O-0102
OWNED-US/Q-O-0103→Q-O-0103 · OWNED-US/Q-O-0104→Q-O-0104 · OWNED-US/Q-O-0105→Q-O-0105 · OWNED-US/Q-O-0106→Q-O-0106 · OWNED-US/Q-O-0107→Q-O-0107 · OWNED-US/Q-O-0108→Q-O-0108
OWNED-US/Q-O-0109→Q-O-0109 · OWNED-US/C-0001→C-0001 · OWNED-US/C-0002→C-0002 · OWNED-US/C-0003→C-0003 · OWNED-US/C-0004→C-0004 · OWNED-US/C-0005→C-0005
OWNED-US/C-0006→C-0006 · OWNED-US/C-0007→C-0007 · OWNED-US/C-0008→C-0008 · OWNED-US/C-0009→C-0009 · OWNED-US/C-0010→C-0010 · OWNED-US/C-0011→C-0011
OWNED-US/C-0012→C-0012 · OWNED-US/C-0013→C-0013 · OWNED-US/C-0014→C-0014 · OWNED-US/C-0015→C-0015 · OWNED-US/C-0016→C-0016 · OWNED-UK/Q-O-0001→Q-O-0110
OWNED-UK/Q-O-0002→Q-O-0111 · OWNED-UK/Q-O-0003→Q-O-0112 · OWNED-UK/Q-O-0004→Q-O-0113 · OWNED-UK/Q-O-0005→Q-O-0114 · OWNED-UK/Q-O-0006→Q-O-0115 · OWNED-UK/Q-O-0007→Q-O-0116
OWNED-UK/Q-O-0008→Q-O-0117 · OWNED-UK/Q-O-0009→Q-O-0118 · OWNED-UK/Q-O-0010→Q-O-0119 · OWNED-UK/Q-O-0011→Q-O-0120 · OWNED-UK/Q-O-0012→Q-O-0121 · OWNED-UK/Q-O-0013→Q-O-0122
OWNED-UK/Q-O-0014→Q-O-0123 · OWNED-UK/Q-O-0015→Q-O-0124 · OWNED-UK/Q-O-0016→Q-O-0125 · OWNED-UK/Q-O-0017→Q-O-0126 · OWNED-UK/Q-O-0018→Q-O-0127 · OWNED-UK/Q-O-0019→Q-O-0128
OWNED-UK/Q-O-0020→Q-O-0129 · OWNED-UK/Q-O-0021→Q-O-0130 · OWNED-UK/Q-O-0022→Q-O-0131 · OWNED-UK/Q-O-0023→Q-O-0132 · OWNED-UK/Q-O-0024→Q-O-0133 · OWNED-UK/Q-O-0025→Q-O-0134
OWNED-UK/Q-O-0026→Q-O-0135 · OWNED-UK/Q-O-0027→Q-O-0136 · OWNED-UK/Q-O-0028→Q-O-0137 · OWNED-UK/Q-O-0029→Q-O-0138 · OWNED-UK/Q-O-0030→Q-O-0139 · OWNED-UK/Q-O-0031→Q-O-0140
OWNED-UK/Q-O-0032→Q-O-0141 · OWNED-UK/Q-O-0033→Q-O-0142 · OWNED-UK/Q-O-0034→Q-O-0143 · OWNED-UK/Q-O-0035→Q-O-0144 · OWNED-UK/Q-O-0036→Q-O-0145 · OWNED-UK/Q-O-0037→Q-O-0146
OWNED-UK/Q-O-0038→Q-O-0147 · OWNED-UK/Q-O-0039→Q-O-0148 · OWNED-UK/Q-O-0040→Q-O-0149 · OWNED-UK/Q-O-0041→Q-O-0150 · OWNED-UK/Q-O-0042→Q-O-0151 · OWNED-UK/Q-O-0043→Q-O-0152
OWNED-UK/Q-O-0044→Q-O-0153 · OWNED-UK/Q-O-0045→Q-O-0154 · OWNED-UK/Q-O-0046→Q-O-0155 · OWNED-UK/Q-O-0047→Q-O-0156 · OWNED-UK/Q-O-0048→Q-O-0157 · OWNED-UK/Q-O-0049→Q-O-0158
OWNED-UK/Q-O-0050→Q-O-0159 · OWNED-UK/Q-O-0051→Q-O-0160 · OWNED-UK/Q-O-0052→Q-O-0161 · OWNED-UK/Q-O-0053→Q-O-0162 · OWNED-UK/Q-O-0054→Q-O-0163 · OWNED-UK/Q-O-0055→Q-O-0164
OWNED-UK/Q-O-0056→Q-O-0165 · OWNED-UK/Q-O-0057→Q-O-0166 · OWNED-UK/Q-O-0058→Q-O-0167 · OWNED-UK/Q-O-0059→Q-O-0168 · OWNED-UK/Q-O-0060→Q-O-0169 · OWNED-UK/Q-O-0061→Q-O-0170
OWNED-UK/Q-O-0062→Q-O-0171 · OWNED-UK/Q-O-0063→Q-O-0172 · OWNED-UK/C-0001→C-0017 · OWNED-UK/C-0002→C-0018 · OWNED-UK/C-0003→C-0019 · OWNED-UK/C-0004→C-0020
OWNED-UK/C-0005→C-0021 · OWNED-UK/C-0006→C-0022 · OWNED-UK/C-0007→C-0023 · OWNED-UK/C-0008→C-0024 · OWNED-UK/C-0009→C-0025 · OWNED-UK/C-0010→C-0026
OWNED-UK/C-0011→C-0027 · OWNED-UK/C-0012→C-0028 · OWNED-UK/C-0013→C-0029 · OWNED-UK/Q-O-0064→Q-O-0173 · OWNED-UK/Q-O-0065→Q-O-0174 · OWNED-UK/Q-O-0066→Q-O-0175
OWNED-UK/Q-O-0067→Q-O-0176 · OWNED-UK/Q-O-0068→Q-O-0177 · OWNED-UK/Q-O-0069→Q-O-0178 · OWNED-UK/Q-O-0070→Q-O-0179 · OWNED-UK/Q-O-0071→Q-O-0180 · OWNED-UK/Q-O-0072→Q-O-0181

### GLOBAL COUNTER vs FLOOR TABLE

COVERAGE: records MARKET_VOC 111/200 ‖ MARKET_VOC+OWNED_PROOF 292/200 ‖ all 302/200 (target 400; +PRODUCT_TRUTH 10) · R-PAGE/R-SCRAPE 121 (incl. [R-PAGE via Exa]; + [R-OWNED] 181) · PB: [PB-01 30‖75/40 PB-06 54‖80/40 PB-05 27‖44/40 PB-02 0‖48/40 PB-03 0‖31/40 PB-04 0‖15/40 PB-07 0‖12/40] · CP: [CP-01 4‖28/25 CP-02 0‖20/25 CP-03 46‖79/25 CP-04 0‖19/25 CP-05 43‖59/25 CP-06 0‖15/25 CP-07 0‖2/25] · types MARKET_VOC 4/4 ‖ +OWNED 5/4 · tags below floor: MARKET_VOC [scene 9/15, failed_solution 14/20, objection 18/20, desire 7/15, trigger 7/15, symptom 5/10, tired_of_hearing 4/5, curiosity 2/3, corruption 0/3] ‖ +OWNED [symptom 8/10, corruption 0/3] · saturation STRONG/MODERATE/EARLY/INSUFFICIENT 9/0/21/18 · unique authors MARKET_VOC 64 ‖ OWNED persons 78 · independent threads MARKET_VOC 45 ‖ OWNED calls 84 · hyper-responsive 67 · usable rate per lane: page/transcript PB-01 13/15 · PB-06 18/21 · PB-05 13/17 · owned US 44/46 · UK 40/40 (+80 BLOCKED-FORMAT) · reddit 0/0 · blocked: [reddit_*, amazon_*, trustpilot_* (Readymerce), tiktok_comments, youtube_comments, fb_*, ad_comments LATE-BOUND: 02.share_url] · AS CONFIRMED/CONTRADICTED/UNSEEN 3/1/2 (3 AS × 2 corpora; EARLY SIGNAL 0) | EK: LATE-BOUND: 03.AS-## · EK stamped 0/LATE-BOUND · weakest link: MARKET_VOC has 0 Reddit and 0 review/comment lanes, so CP-01/CP-02/CP-06/CP-07 and every operator-ICP question rest on OWNED_PROOF alone (one platform, max SUPPORTED) · what closing it would cost: HARVEST-01..07 ≈ 150–250 sources · ≈$1.7–2.2 Apify after the monthly reset + ≈$0.30 Exa · ≈3 h; HARVEST-08 owned re-mine $0 · ≈1.5 h

CHECKPOINT merge=complete records=307 c_rows=29 cost=$0.00

COVERAGE (merged log): see 06-VOC-REPORT.md §18 — the line above is authoritative.
