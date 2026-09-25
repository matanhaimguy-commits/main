# 00-RUN-CARD · readymerce · US · standard · claude-code

## INPUTS CARD
| field | value | state |
|---|---|---|
| PRODUCT NAME | Readymerce (readymerce.com) — a done-for-you online-store / e-commerce business setup service sold by phone to inbound "I want to open an online business" registrations | GIVEN (product-name check: PRESENT → run starts) |
| PDP LINK | https://readymerce.com | GIVEN (our own site; 01 fetches it; competitors found by free search) |
| TARGET MARKET | US | ASSUMED (blank → US). The 280 owned sales-call transcripts split ≈151 US-number calls / ≈123 UK-number calls / 6 other; UK is a second run in its own folder. Owned records from UK calls are still coded (OWNED_PROOF) with `call_market: UK` in `life_context` so downstream can split. |
| category | done-for-you e-commerce store / "business in a box" (dropshipping, Shopify/Amazon/Etsy store build) | INFERRED: transcripts + readymerce.com (01 confirms) |
| components / spec | unknown | INFERRED path (01): our PDP claims → competitor PDPs → category-typical → VOC |
| price | unknown (transcripts mention deposits ≈ $500 and plan tiers) | INFERRED: 01 / 12 |
| competitor list | none given | 01 free searches → NW-SEED-## |
| budget level | standard | ASSUMED (default) |
| brand-name lock | Readymerce (existing brand) | GIVEN — 13 treats it as option 1 + 2 alternates |
| owned data | 280 sales-call transcripts (Sept 2026), `runs/readymerce/inputs/transcripts/` | GIVEN — `[R-OWNED]`, corpus OWNED_PROOF, harvested by VOC-OWNED-* in W1 |
| operator ICP hypotheses | (a) fathers of kids who want to provide a better future / more time with kids and wife; (b) adults 50+ with money who want an online business | HYPOTHESIS — entered by 01 as candidate populations with label HYPOTHESIS (operator-supplied, not validated); the run finds the validated directions |
| operator problem statement | current leads are low quality ("tire kickers"); wants narrow, accurate ICPs of buyers ready to invest, not broad | OPERATOR CONTEXT (recorded, never read as VOC) |

## RUN KNOBS
RUN_MODE fresh · PERSISTENT_RUN_DIR `/home/user/main/runs` (git repo, branch `claude/sweet-keller-g8zeli`) · BACKUP_DIR = the git remote `origin/claude/sweet-keller-g8zeli` (every checkpoint = commit + push) · BRAND_SLUG `readymerce` · RUNTIME `claude-code` (cloud container, Agent tool with sonnet/opus routing, run_in_background) · MAX_PARALLEL_AGENTS 8 · CHECKPOINT_DELIVERY both (git push + key files attached at wave ends via SendUserFile).
Run folder: `/home/user/main/runs/readymerce/foundation/` · probe PASS 2026-09-24T19:42:16Z · step prompts: `/home/user/main/runs/readymerce/prompts/STEP-nn.md` (pasted whole into every brief by path; each agent reads its prompt file in full first).

## BUDGET LEVEL + CAPS (standard)
02 ≈5–7 cr (≤3 seed networks + keywords) · 07 ≤2 cr · 09/10 ≤3 cr · 01 ≈$1.00 · 04 ≤$0.60 · 05/06 cap $8 (÷ N_PB per harvester) · 09 ≤$1. Credit guard: `start_brand_spy` NOT RUN — needs operator yes (asked once below); never unfiltered `list_shops` or `search_ads {}`.
Balances before W0: GetHookd 291.22 credits · Higgsfield 1,998.34 credits (ultra) · Apify: BRONZE tier, balance not exposed by the MCP (spend reconciled from per-run costs).

## TOOL CARD (inspected 2026-09-24T19:44Z)
| capability | status | provider / substitute | steps |
|---|---|---|---|
| Ad-intelligence source | AVAILABLE (GetHookd MCP `mcp__Gethooked__*`, 291.22 cr) + AVAILABLE (Meta Ad Library via `mcp__Facebook_Ads__ads_library_search`, free, live: 4,519 ads on a test term) | Apify `igolaizola/facebook-ad-library-scraper` as the third rung | 01·02·03·07·09·10·12·13 |
| Scraper (reviews, subreddits, threads, groups, comments, pages) | **UNAVAILABLE — verified 20:35Z:** Apify `Monthly usage hard limit exceeded`; Firecrawl scrape `Insufficient credits`; Browserbase `401 Unauthorized`; WebFetch/curl egress 403 for every research host | SUBSTITUTED → Exa research agent `mcp__Readymerce_Exa__agent_run` for ordinary pages (`[R-PAGE via Exa]`; Reddit + Trustpilot NOT retrievable) → WebSearch snippets `[R-SNIPPET]` → OPERATOR-PASTE | 01·04·05·06·09·10·11 |
| Transcript source | AVAILABLE (GetHookd `transcribe_ad`; TranscriptAPI MCP `mcp__TranscriptAPI__get_youtube_transcript` + `search_youtube` — verified 20:33Z) | Apify `johnvc/YoutubeTranscripts` UNAVAILABLE (limit) | 02·05·06·07·13 |
| Web search + fetch | SUBSTITUTED: WebSearch AVAILABLE (snippets); WebFetch UNAVAILABLE (egress policy 403 — readymerce.com, trustpilot.com, youtube.com, reddit.com all denied); page reads via `mcp__Readymerce_Exa__agent_run` (verified: read readymerce.com pricing/refund pages verbatim) | — | every step |
| Code execution | AVAILABLE (Bash, python3 3.11, node 22) | — | every step |
| Search-volume corroboration | UNAVAILABLE (no Ahrefs / SimilarWeb MCP) → `search_volume: UNSCANNED` | none | 07 |
| Audience-size read (Meta EAS) | UNAVAILABLE (drafting ad sets in the operator's ad account is an outward action not authorised for this run) → `fish: UNSIZED — method: EAS` | none | 09 |
| Image generation + consistency | AVAILABLE (Higgsfield MCP `mcp__Higgs__*`, 1,998 cr) | — | 13 |
| Delegated agents | AVAILABLE (Claude Code `Agent` tool, up to 8 in one message, `run_in_background`, model routed sonnet/opus) | — | every wave |
| TikTok Ads MCP | UNAVAILABLE (needs OAuth; not used) | — | — |

## FILE REGISTRY — see DELIVERABLES in the orchestrator prompt; files land under `foundation/` with the registry names; scoped partials under `nn-partials/`.

## WAVE PLAN
W0 SEED: `01` (MODE: SEED, opus, 10 min / 40 calls).
W1 FAN-OUT (≤8 at once; queue order: seed NW with most active ads → PB with most populations → 02-KEYWORDS → 01-DEEP → VOC-OWNED-*): `02-NW-<seed>` ×≤3 · `02-KEYWORDS` · `VOC-PB-##` ×≤5 (04→05→06 scoped) · `01-DEEP` · **orchestrator adaptation:** `VOC-OWNED-US` + `VOC-OWNED-UK` — STEP 06 HARVEST with `SCOPE: OWNED-US | OWNED-UK` over the 280 sales-call transcripts (lane `owned_paste`, corpus OWNED_PROOF, ids Q-O-####, pb_ids tagged from 01's PB map; 04's Step 9 "owned sources" COM row); they write `06-partials/06-VOC_MASTER.OWNED-US.csv` / `.OWNED-UK.csv` + logs + handoffs and merge in 06-MERGE. Rationale: the operator supplied the transcripts for objection / belief / angle analysis; the step prompts route owned data through 06 (OWNED_PROOF) and 11 (`[R-OWNED]` operator notes).
W2: `03` (MODE: MERGE then synthesis) ∥ `06-MERGE` ∥ `07-SOPH`.
W3: `07` (MODE: FULL) ∥ `08` ∥ `10`.
W4: `09`.
W5: `11-AV-##` ×≤5 ∥ `13` ∥ `12-OFFER`.
W6: `12` (MODE: ASSEMBLE).
Time boxes: 01 seed 10/40 · harvester 30/100 · network agent 25/80 · synthesis 40/150 · merge/assemble 20/60. Model routing: extraction (VOC-PB, VOC-OWNED, 02-NW, 02-KEYWORDS, 01-DEEP) → sonnet; everything else → opus.

## BRIEFS
Every brief = `prompts/AGENT-BRIEF-COMMON.md` (inputs card, tool card, MCP tool names, budget, rules pointer, label vocabulary pointer) + the step prompt file path (read whole) + the SCOPE/MODE line + inputs[] + outputs[] + max_minutes/max_tool_calls + model.

## PORTABILITY NOTE
Claude Code (cloud): one message launches a wave (Agent calls, run_in_background: true); this session polls the run folder, audits at wave end with `prompts/audit.py`, checkpoints (git commit + push), launches the next wave. Model choice honoured (sonnet / opus).

## OPERATOR QUESTIONS (asked once; the run does not wait)
1. `start_brand_spy` (8 cr per brand) on the top competitor network — yes/no? Without a yes it prints `NOT RUN — needs operator yes: start_brand_spy`.


---

## COMPLETION CHECK — written by the orchestrator at 2026-09-24T23:16:23Z (all facts from files on disk and 00-STATUS.md; no agent message trusted)

### A · WAVES 7/7
| wave | agents | result |
|---|---|---|
| W0 | 01 SEED | COMPLETE (AUDIT-PASS) |
| W1 | 02-NW-SEED-01/02/03, 02-NW-NEW-SEED-01..05, 02-KEYWORDS, 01-DEEP, VOC-PB-01/06/05, VOC-OWNED-US/UK (15 agents, ≤8 parallel) | COMPLETE 15 (two HARVEST-LOG files AUDIT-PARTIAL on the coverage-tail technicality; coverage lives in their handoffs) |
| W2 | 03 (MERGE + synthesis), 06-MERGE (override 30/80), 07-SOPH | COMPLETE 3 |
| W3 | 07 FULL, 08, 10 | COMPLETE 3 |
| W4 | 09 | COMPLETE 1 |
| W5 | 11-AV-07, 11-AV-01, 11-AV-04, 11-AV-02, 11-AV-03, 12-OFFER, 13 | COMPLETE 7 |
| W6 | 12 ASSEMBLE (override 40/120) | COMPLETE 1 |
PARTIAL agents: none. Every wave audited from disk with `prompts/audit.py` before WAVE-END.

### B · FILES 122 on disk · top-level deliverables 37/37 present and non-empty · partial-scope files 70 · datasets 15 · `.partial` remaining 0
Top-level: 00-RUN-CARD.md, 00-STATUS.md, 01-PRODUCT-TRUTH.md + 01-HANDOFF.json, 02-COMPETITOR-INTEL.md + 02-swipe.csv + 02-HANDOFF.json, 03-VALIDATED-MESSAGING.md + 03-HANDOFF.json, 04-COMMUNITY-MAP.md + 04-HANDOFF.json, 05-URL-CORPUS.md + 05-HANDOFF.json, 06-VOC_MASTER.csv (362 rows: MARKET_VOC 142 / OWNED_PROOF 210 / PRODUCT_TRUTH 10; Q rows 333, C rows 29) + 06-VOC-LEDGERS.csv + 06-HARVEST-LOG.md + 06-SOURCE-MANIFEST.md + 06-VOC-REPORT.md + 06-HANDOFF.json, 07-AWARENESS-SOPHISTICATION.md + 07-SOPH-20ADS.csv + 07-HANDOFF.json, 08-DESIRES-LF8.md + 08-DESIRES.csv + 08-HANDOFF.json, 09-AVATARS.md + 09-HANDOFF.json, 10-MECHANISMS.md + 10-HANDOFF.json, 11-BELIEFS.md (449 KB, merged by 12 ASSEMBLE) + 11-HANDOFF.json, 12-OFFER-TESTPLAN-PLAYBOOK.md + handoff.json (v2) + 12-HANDOFF.json, 13-BRAND.md + 13-HANDOFF.json + assets/readymerce-visual-identity/README.md.
Inputs: inputs/transcripts/ (280 sales-call .txt) — parsed by VOC-OWNED-US/UK as OWNED_PROOF, never mixed with MARKET_VOC.

### B2 · EVERY AGENT'S COVERAGE LINE (verbatim `coverage` field of each handoff on disk)
- `01-HANDOFF.json` (1934 B): SEED: pdp BLOCKED; reviews 5 snippet/0 full; seeds 3; PB 7; CP 7; lanes 3; lead PB-01 LOW
- `01-partials/01-HANDOFF.DEEP.json` (1902 B): DEEP: reviews 0 read of 0 retrievable (exact-SKU, every venue exhausted: BBB none, ScamAdviser 0, ScamDoc unattributable, trustedrevie.ws 0, Sitejabber 0, ProductReview none, Trustpilot BLOCKED-ON-TOOL, Reddit/forum 0); PDP 9/9 pages EXACT PRODUCT MATERIAL (new vs SEED's BLOCKED PDP); components 9 of 11 with a DEEP fact (C8 portal, C9 account-manager remain SEED-only UNKNOWN); DF 3; PB refreshed 6 (labels unchanged, evidence firmed; PB-03 gets new non-buyer trust-score context); pain score PB-05 5->6/10, others unchanged; CONFIDENCE: truth card PROXY-SKU, problem map SUPPORTED 3 / HYPOTHESIS 4 / VALIDATED 0
- `02-HANDOFF.json` (1968 B): NW 8 (AF 1, UNSIZED 7); IM 32, STRICT 0; lanes 5/7; VALIDATION-DEGRADED (3 seeds ~0 ads)
- `02-partials/02-HANDOFF.KEYWORDS.json` (3515 B): KEYWORDS: 9 lane terms + 5 avatar phrases searched GetHookd(28 charged calls)+Meta(14 free calls); 7 of 9 GetHookd cells exact, 2 marked ~/NOT MAPPED (batch-scale re-verification limit, VALIDATION-DEGRADED); every raw total SATURATED but almost no DFY-ecom-relevant advertisers in rows actually read (keyword vocabulary shared with fitness/fiction/supplement/SaaS categories); new seeds 6 queued (K01-K02 mandatory, both UNSIZED-confirmed-not-indexed; K03 reconfirms NW-SEED-03; K04-K06 net-new, UNSIZED credit-capped) + 1 logged off-topic (Joseph Lewis, store-liquidation model); list_similar_shops NOT RUN (no shop_id); credits GetHookd 2.29/3.0 (288.37->286.08, unattributed 0.00), Meta $0, Exa $0/$0.60 (not needed), Apify $0; CONFIDENCE: discovery COMPLETE, band precision PARTIAL (2/9 GetHookd cells), new-seed sizing PARTIAL (2/8 sized-as-UNSIZED, 6/8 not GetHookd-sized)
- `02-partials/02-HANDOFF.NW-NEW-SEED-01.json` (2047 B): 1 network (0 active/922 hist.); 3 concepts+1 anchor; lanes 4/7; avatar 3/3; credits GH 1.9/2.5, Exa $0.13/$0.40; ad $0/$20 -> $1/mo+$500 fee funnel
- `02-partials/02-HANDOFF.NW-NEW-SEED-02.json` (2019 B): NO coverage field
- `02-partials/02-HANDOFF.NW-NEW-SEED-03.json` (2031 B): NO coverage field
- `02-partials/02-HANDOFF.NW-NEW-SEED-04.json` (2118 B): NO coverage field
- `02-partials/02-HANDOFF.NW-NEW-SEED-05.json` (2068 B): NO coverage field
- `02-partials/02-HANDOFF.NW-SEED-01.json` (1725 B): networks 1 (ABOVE-FLOOR 0/UNSIZED 1); ads 0/0; lanes 2 of 3; components 10; credits GetHookd 0.66/2.0, Exa $0.10/$0.60; VALIDATION-DEGRADED — see .md
- `02-partials/02-HANDOFF.NW-SEED-02.json` (1909 B): NO coverage field
- `02-partials/02-HANDOFF.NW-SEED-03.json` (2037 B): NO coverage field
- `03-HANDOFF.json` (2041 B): IM32 STRICT0 NW8 AF1 ctrl SUP 540d M
- `04-HANDOFF.json` (1796 B): COM 30 (V 6 · S 13 · H 5 + owned 2) · Reddit usable 0% · walled 5 · cost $1.025 · AS checked in 06 §17 · EK LATE-BOUND: 03.AS-##
- `04-partials/04-HANDOFF.PB-01.json` (2017 B): COVERAGE: COM 14 (VALIDATED 0 · SUPPORTED 9 · HYPOTHESIS 2) · platforms 6/9 · PB below floor: [NONE] · CP NOT FOUND: [CP-01] · walled 2 · Reddit usable rate 0% · cost $0.05 · AS: LATE-BOUND: 03.AS-## · weakest link: Reddit fully BLOCKED-ON-TOOL this run; every Reddit-shaped floor filled from Shopify's own forum or snippets instead. · what closing it would cost: Apify limit reset to run harshmaur/reddit-scraper (~$0.0018/result), ≈$5-15 and one billing cycle.
- `04-partials/04-HANDOFF.PB-05.json` (2333 B): COM 7 (VALIDATED 1 · SUPPORTED 4 · HYPOTHESIS 2) · platforms 5/9 · PB below floor: [NONE on >=4-per-PB; PARTIAL on reddit>=3-subreddits] · CP NOT FOUND: [NONE] · walled 3 · Reddit usable rate 0% · cost $0.25 · AS: 1 row | LATE-BOUND: 03.AS-## · weakest link: Reddit fully BLOCKED-ON-TOOL (Apify hard limit + Exa cannot retrieve reddit.com) · what closing it would cost: Apify plan reset or alternate Reddit credential + ~$0.05-0.10/thread, or operator-pasted thread URLs
- `04-partials/04-HANDOFF.PB-06.json` (2067 B): COVERAGE: COM 7 (VALIDATED 5 · SUPPORTED 0 · HYPOTHESIS 1) · platforms 4/9 (forum x2, quora, youtube_search, blog_comments; reddit/tiktok/trustpilot/facebook/amazon blocked or n/a) · PB below floor: NONE · CP NOT FOUND: NONE · walled 0 · Reddit usable rate 0% · cost $0.425 Exa + ~14 TranscriptAPI credits · AS: 1 row (LATE-BOUND: 03.AS-## for the rest) · weakest link: Reddit is completely unopenable this run · what closing it would cost: 1 Apify harshmaur/reddit-scraper run per PB (~$0.05-0.10) once the monthly hard limit resets, or an operator-side residential-proxy fetch of old.reddit.com search.json
- `05-HANDOFF.json` (1610 B): URL 80/60 (LISTED 70 · BLOCKED 7 · OPERATOR-PASTE 4 · +6 added in 06 · +2 owned) · reddit 0 URLs · plan cost $1.025/$8
- `05-partials/05-HANDOFF.PB-01.json` (1615 B): COVERAGE: URL 23/60 (LISTED 21 · QUERY-ONLY 0 · BLOCKED 2 · OPERATOR-PASTE 2) · PB below URL floor: [NONE] · CP THIN: [CP-01] · PLAN-VALIDATED: [PB-01, CP-05] · PLAN-THIN: [CP-01] · plan cost $0.05/$2.67 · weakest link: Reddit fully BLOCKED-ON-TOOL, 0 reddit.com URLs surfaced across 22 queries. · what closing it would cost: Apify billing-cycle reset (~$5-15) or 2-3 operator-pasted Reddit URLs mined by hand in 06.
- `05-partials/05-HANDOFF.PB-05.json` (1559 B): URL 17/12 (LISTED 17 · QUERY-ONLY 0 · BLOCKED 5 · OPERATOR-PASTE 2) · PB below URL floor: [NONE total; reddit sub-floor unmet] · CP THIN: [NONE] · PLAN-VALIDATED: [NONE] · PLAN-THIN: [PB-05, CP-05] · plan cost $0.55/$2.67 · weakest link: Reddit+Facebook fully BLOCKED-ON-TOOL · what closing it would cost: Apify reset or operator-pasted Reddit thread URLs + ~$0.05-0.10/thread
- `05-partials/05-HANDOFF.PB-06.json` (1350 B): COVERAGE: URL 32/12(scoped) (LISTED 32 · QUERY-ONLY 0 · BLOCKED 0-URLs-exist(reddit) · OPERATOR-PASTE 0) · PB below URL floor: NONE · CP THIN: [CP-05] · PLAN-VALIDATED: [PB-06, CP-03] · PLAN-THIN: [CP-05] · plan cost $0.425/~$2.67 cap · weakest link: Reddit lane has zero discoverable URLs this run · what closing it would cost: 1 Apify reddit-scraper run (~$0.10) once the monthly hard limit resets
- `06-HANDOFF.json` (2038 B): {'file': '06-VOC-REPORT.md', 'section': '§18 last line'}
- `06-partials/06-HANDOFF.OWNED-UK.json` (1699 B): COVERAGE OWNED-UK: records 72/70 (target 120) · calls read 40/42 (N=122 candidate files; 80 BLOCKED-FORMAT no-diarization) · tags below floor: NONE · C rows 13 · call_outcome BOOKED-FOLLOWUP 56/DECLINED 9/HUNG-UP 2/UNKNOWN 5 · resume: url_index=42 · weakest link: 80/120 format-B files have no [Speaker N] tags at all (merged untagged speech) — corpus built from the diarization-clean minority only
- `06-partials/06-HANDOFF.OWNED-US.json` (1701 B): COVERAGE OWNED-US: records 109/70 (target 120) · calls read 46/155 (44 yielded records, 2 zero-with-reason) · tags below floor: NONE · C rows 16 · call_outcome BOOKED-FOLLOWUP 64/DECLINED 21/UNKNOWN 12/PAID 7/DEPOSIT 5 · resume: url_index=46 · weakest link: CP-07 (spouse can't work because of kids) has only 1 record/1 call — under-sampled in this rank range, a RE-MINE pass over ranks 47-155 would close it
- `06-partials/06-HANDOFF.PB-01.json` (2221 B): COVERAGE PB-01: records 40/40 · CP: [CP-01 3/25, CP-05 27/25] · types 3 floor-eligible (forum, trustpilot, youtube_search) + 1 non-floor (blog_comments [R-SNIPPET]) · tags below floor: [scene 3/5, trigger 3/5, symptom 3/4, tired_of_hearing 1/2, corruption 0/1] · blocked: [reddit_post+comments, fb_post_comments (RC-FBC), quora_answers] · cost $0.95 (Exa) + ~10 TranscriptAPI calls · resume: url_index=15 · weakest link: CP-01 (full-time-job population) stays almost entirely unfound (3/25) because Reddit — where it most likely speaks — is fully BLOCKED-ON-TOOL and no single non-Reddit page combined all of CP-01's defining traits in one passage.
- `06-partials/06-HANDOFF.PB-05.json` (2064 B): PARTIAL (N=30/floor 40) — chain exhausted: [Apify monthly hard limit (all actors), egress 403 (WebFetch/curl on all research hosts), Exa cannot retrieve reddit.com or Trustpilot] · CP-05 PARTIAL (N=17/25) · types 3/4 (forum, quora, youtube_transcript; reddit BLOCKED, reviews not run) · unique authors 17 · independent threads/videos 17 · cost $0.55 vs scoped cap $2.67 · weakest link: Reddit (the platform most likely to hold PB-05's core population) fully BLOCKED-ON-TOOL across all three legs · what closing it would cost: Apify plan reset or an alternate Reddit-capable credential, ~$0.05-0.10/thread via RC-RD once real thread URLs exist (operator paste of 5-10 r/dropshipping + r/dropship threads is the fastest unblock), plus Amazon/Trustpilot review lanes (not attempted this leg, time-boxed) for the reviews floor.
- `06-partials/06-HANDOFF.PB-06.json` (1794 B): COVERAGE PB-06: records 55/40 · CP: [CP-03 47/25 MET, CP-05 10/25 PARTIAL] · types 4/4 · tags below floor: [failed_solution, desire, trigger, symptom, deeper_hope, curiosity, corruption] · blocked: [reddit, trustpilot, tiktok, facebook, amazon(n/a)] · cost $0.425 (this step) + ~24 TranscriptAPI credits · resume: url_index=21 · weakest link: CP-05 (aspiring entrepreneur wanting to skip the build) is genuinely thin in the reachable corpus — only 10 of 25 needed records, despite a dedicated population-first search round
- `07-HANDOFF.json` (2013 B): {'file': '07-AWARENESS-SOPHISTICATION.md', 'section': '§18'}
- `07-partials/07-HANDOFF.SOPH.json` (1984 B): {'file': '07-partials/07-SOPH.md', 'section': '§18'}
- `08-HANDOFF.json` (2045 B): §19
- `09-HANDOFF.json` (1959 B): avatars 7V/0S/1E/0H; sized 0/8; OWNED1 STEAL2 UNTAP3 UNPROV2; CAM 36/488 SINGLE-NW; harvest 10; Q+22
- `10-HANDOFF.json` (2036 B): NO coverage field
- `11-HANDOFF.json` (2030 B): ALL: B 33/33 Q (V28/S4/E1); VIE 5/5; lane 5/5; OBJ 59 T1 32 unres 2; FS 20 M1 9; P 46/9/19; P0 16/17; open 5/5; domino PARTIAL
- `11-partials/11-HANDOFF.AV-01.json` (1936 B): AV-01: 7 beliefs 7 traced (VAL 7); V/I/E 1/1; OBJ 12 (T1 7, unres 1); FS 6 (M-1 4); proof 9/1/3; P0 stacks 4/4; opening 1/1; domino PARTIAL; full: 11-partials/11-BELIEFS.AV-01.md §COVERAGE
- `11-partials/11-HANDOFF.AV-02.json` (1865 B): AV-02: 7 beliefs 7 traced (V6/S1); VIE 1/1; lane 1/1; OBJ 13 (T1 8); FS 4 (M-1 2); proof 9/3/4; P0 stack 4/4; opening 1/1; domino PARTIAL
- `11-partials/11-HANDOFF.AV-03.json` (1596 B): B6 V5/S1, VIE 3/3, OBJ11 T1 6 unres0, FS4 M-1 1, P 9/1/4, P0 3/3, DOMINO PARTIAL, HARVEST-24 +4Q
- `11-partials/11-HANDOFF.AV-04.json` (1902 B): AV-04: B 7/7 Q-traced, VIE 1/1, lane 1/1, OBJ 12 (T1 7, unres 0), FS 3 (M-1 1), P E8/S2/P5, P0 stack 2/3, opening 1/1, domino PARTIAL
- `11-partials/11-HANDOFF.AV-07.json` (1857 B): AV-07: B 6/6 Q; VIE 1/1; lane 1/1; OBJ 11 T1 4 unres 1; FS 3 M1 1; P 11/2/3; P0 3/3; open 1/1; domino PARTIAL
- `12-HANDOFF.json` (1113 B): Offer ACCEPTABLE; target CPA $399.56, breakeven $217.50; 5 partials merged; 5 adsets x 18 cells (READY 18); $100/day; day 3/7; playbook 50 verbatim/36 openings/QC 13/13; contracts 26/26 x5 STRANGER PASS; handoff v2 65 keys; weakest: no outcome proof + booked-call proxy
- `12-partials/12-HANDOFF.OFFER.json` (1907 B): Offer ACCEPTABLE; BAND NULL (1 above-floor NW); $500 given, upper tiers INFERRED; valid Y; sub not preselected; urgency NONE. Target CPA $399.56, breakeven $217.50, AOV ratio 1.73.
- `13-HANDOFF.json` (1528 B): POS PASS; EN-1 VALIDATED 8 auth/0 NW; NF 4; NAR peer SUPPORTED 0 STRICT; REG 2 CR; name PROVISIONAL (USPTO not fetched); voice PASS; story POSITIONED; elements product+env, soul NULL; set 6/6; FACT v1 21/24
- `handoff.json` (141577 B, v2): Offer: ACCEPTABLE, benchmark networks 1, anchor COGS-multiple 2.06× (GIVEN $500; BAND: NULL), price given (T1) / INFERRED (T2, T3), tiers valid Y, subscription not preselected, urgency NONE. Economics: target CPA $399.56, breakeven $217.50, CM/order $399.56, AOV ratio 1.73 ACCEPTABLE, testable concepts 0 (booked-call proxy 18, OPERATOR-VALIDATES), max adsets 0 (proxy 5, OPERATOR-VALIDATES). Merge: 5 partials → 11-BELIEFS.md. Test plan: 5 adsets × 3–4 ads = 18 cells (READY 18 / FLAGGED 0), budget $100/day, decisions day 3/7. Playbook: 50 verbatim, 36 openings, 18 angles, QC 13/13. Contract: filled AV-07 26/26, AV-01 26/26, AV-04 26/26, AV-02 26/26, AV-03 26/26; STRANGER TEST PASS. Handoff: 65 keys, version 2, late-bound [none from 11/13; OPERATOR-VALIDATES: booked-call proxy, 60-day guarantee, T2/T3 + complement prices, build 7–10 days; 13.name_status PROVISIONAL], patch note present. Weakest link: zero Readymerce outcome proof plus a purchase-level test the $100/day budget cannot fund — the whole plan rides a booked-call proxy built on 4 closes in 84 seller-contacted calls; cost to close: operator confirms the proxy + publishes the post-launch window and per-stage product count ($0), one ≈1-hour demo shoot ($0), one consenting client's post-launch report (weeks after a first sale). No ROAS or profit is read from a spy score or an ad's runtime; paid testing decides.

### C · LATE-BOUND FIELDS — who filled them (grep of every deliverable .md/.json, STATUS/PROGRESS excluded; the token stays in the issuing file by design, the value lives in the later file)

| target | refs | issued by | filled by |
|---|---|---|---|
| 01.* (TRUTH CARD fields) | 12 | 01 SEED handoff, 02-NW-SEED-02, 02-NW-NEW-SEED-01/04 | 01-DEEP (W1) → 01-PRODUCT-TRUTH.md §TRUTH CARD + 01-partials/01-HANDOFF.DEEP.json |
| 02.* (share_url, top_ad_image_urls, ad_comments seeds) | 35 | 04-PB-##, 05-PB-##, 06-PB-##, 06-MERGE, 02-NW-SEED-02 | 02 MERGE (W1/W2) for network fields; `02.share_url` for ad comments stays OPEN → HARVEST-07 (Meta connector exposes no share_url/media field) |
| 03.* (PR-##, EK-##, story_structures) | 37 | 02 partials, 04 partials + merge, 06 partials + merge | 03 (W2) → 03-VALIDATED-MESSAGING.md + 03-HANDOFF.json |
| 06.* (Q-## counts, corpus tiers) | 22 | 07-SOPH (W2, parallel with 06-MERGE) | 07 FULL (W3) re-read 06-HANDOFF.json; 07-AWARENESS-SOPHISTICATION.md carries the resolved counts |
| 07.* (awareness rungs, sophistication stage, CP reads) | 66 | 08 (W3, parallel with 07 FULL), 09, 07-SOPH self-refs | 09 (W4) for the avatar rows; 12 ASSEMBLE `awareness_snapshot` in handoff.json |
| 08.* (MD-##, H-##) | 5 | 10 (W3, parallel with 08), 11-AV-04 | 11 partials (W5) + 12 ASSEMBLE `desire_leaderboard` / `mass_desires[]` |
| 11.* (OBJ-##, P-##, GO-AV#, WM-AV#.enemies, live_wire, proof) | 15 | 12-OFFER (W5), 13 (W5) | 12 ASSEMBLE (W6) inside 12-OFFER-TESTPLAN-PLAYBOOK.md + handoff.json (12-partials and 13-BRAND.md untouched — one writer per file) |
| 12.offer / 12.route (fact-sheet rows) | 6 | 13 (W5) | 12 ASSEMBLE (W6) in handoff.json `fact_sheet` + `route` |

### D · OPEN HARVEST ORDERS (issuing step · lane · closing call) — none run; all need a tool that is BLOCKED-ON-TOOL or an operator paste

| ID | issued by | lane | closing call |
|---|---|---|---|
| HARVEST-01 | 06-MERGE | reddit_post+comments, all PBs | Apify harshmaur/reddit-scraper (Apify monthly hard limit) or OPERATOR-PASTE of 5–10 top threads |
| HARVEST-02 | 06-MERGE | trustpilot_balanced (6 domains incl. readymerce.com) | Apify memo23/trustpilot-scraper-ppe |
| HARVEST-03 | 06-MERGE | amazon_* critical/3★/5★ on proxy listings | Apify junglee/Amazon-crawler (n/a for the service itself — no ASIN) |
| HARVEST-04 | 06-MERGE | tiktok_comments | Apify clockworks/tiktok-scraper (≈$0.25) |
| HARVEST-05 | 06-MERGE | youtube_comments on the 25 transcribed videos | Apify youtube-comments scraper |
| HARVEST-06 | 06-MERGE | fb_post_comments / fb_group | Apify facebook-comments-scraper / facebook-groups-scraper |
| HARVEST-07 | 06-MERGE | ad_comments | LATE-BOUND: 02.share_url → Apify facebook-comments-scraper (≈$0.10) |
| HARVEST-08 | 06-MERGE | owned_paste RE-MINE: US ranks 47–155 (109 calls) + 80 undiarized UK files | in-house re-mine, $0, ≈2 harvester boxes |
| HARVEST-09 | 06-MERGE | population-first CP-01 / CP-07 | Apify reddit-scraper on 4 queries |
| HARVEST-10 | 08 | pain scenes for the leaderboard rows | targeted re-mine (Reddit/YouTube comments) |
| HARVEST-11 | 08 | EARLY SIGNAL MD-03/05/06/08 second-context voices | MARKET_VOC re-mine |
| HARVEST-12 | 08 | MD-02 emotion- + scene-tagged records | MARKET_VOC re-mine |
| HARVEST-13 | 08 | CP-04 LB-CP depth (5 desire-tagged records) | OWNED re-mine (HARVEST-08) → Exa |
| HARVEST-14 | 09 | AV-01 pond CP-03 n=3 (<5) sophistication read | Reddit re-mine |
| HARVEST-15 | 09 | AV-02 pond CP-03 n=3 (<5) | Reddit re-mine |
| HARVEST-16 | 09 | AV-03 pond | Reddit re-mine |
| HARVEST-17 | 09 | AV-04 pond EAS UNSIZED | Meta EAS (no tool) |
| HARVEST-18 | 09 | CL-04 parent/father pond (7 minted via Exa) | Reddit/FB group re-mine |
| HARVEST-19 | 09 | CL-05 retired/pension pond (6 minted via Exa) | Reddit/forum re-mine |
| HARVEST-20 | 09 | CL-06 existing small-business owner pond (3 minted) | Quora shells + Reddit |
| HARVEST-21 | 09 | CL-09 capital holder ($15–35K) pond | competitor lens + Reddit |
| HARVEST-22 | 09 | CL-08 partner-on-speaker-phone (0 primary) | owned re-mine (HARVEST-08) |
| HARVEST-23 | 09 | proof-loop Reddit threads for the 7 defining phrases | Apify reddit-scraper one batch (≈$0.30) |
| HARVEST-24 | 11-AV-03 | B-02.AV-3 INTERNAL single-thread P0 | CLOSED by 11-AV-03 (1 Exa run, 4 rows minted, SUPPORTED→VALIDATED) |

### E · BLOCKED-ON-TOOL OBJECTS (with the call that closes each)

| object | file | closing call |
|---|---|---|
| readymerce.com PDP direct fetch (SEED) | 01 | WebFetch/curl once network policy allows readymerce.com; closed indirectly by 01-DEEP via Exa |
| Reddit lane, every PB (0 thread URLs even discoverable) | 04, 05, 06, 06-VOC-REPORT §11 | Apify reddit-scraper or OPERATOR-PASTE |
| Trustpilot pages (6 domains) | 05, 06, 01 §complaints | Apify trustpilot scraper / WebFetch |
| Amazon proxy-SKU reviews | 05, 06 | Apify junglee/Amazon-crawler |
| TikTok comments + TikTok ad lane (UNSIZED) | 04, 05, 06, 07 | Apify clockworks/tiktok-scraper; TikTok Ads MCP OAuth |
| YouTube comments lane (transcripts done via TranscriptAPI) | 05, 06 | Apify youtube-comments scraper |
| FB group facebook.com/groups/282038432287765 (PUBLIC, unread) | 04, 06 | Apify facebook-groups-scraper or Browserbase |
| Competitor ad comments (share_url) | 02, 06 | Meta share_url + Apify facebook-comments-scraper |
| Competitor page hex/fonts, top_ad_image_urls | 13 | Browserbase / WebFetch on 5 network pages |
| Render proofread + downloads (CDN 403) | 13, assets/ | egress to Higgsfield CDN or operator download in the Higgsfield workspace |
| Meta EAS sizing | 07, 09 | Meta Ads Manager estimate (no tool; UNSIZED — method: EAS) |
| search_volume | 02-KEYWORDS | keyword-volume tool (UNSCANNED) |
| GetHookd get_top_ads / narrator cls_* counts | 07, 13 | NOT RUN — needs operator yes: start_brand_spy (8 cr) |

### F · NOT RUN — needs operator yes: `start_brand_spy` (8 cr) — never called; referenced in 00-RUN-CARD, 01, 07, 07-SOPH, 13, 02-NW-NEW-SEED-03/04/05. Never called unfiltered: `list_shops` appears only as `list_shops q:'readymerce.com'` (01 SEED, filtered, 0.6 cr); `search_ads {}` appears nowhere except the run-card rule (grep of every deliverable).

### G · TOOL CARD vs USED

| tool | card | used |
|---|---|---|
| GetHookd MCP | AVAILABLE 291.22 cr | USED: 01 SEED 0.6, 02 networks ≈9.9 (incl. 5 new seeds), 07-SOPH, 10 (search_ads 0-result variants, 0 cr), 12-OFFER 0.04, 13 0.05 → 282.89 cr at close (live read) = 8.33 cr spent |
| Meta Ad Library | AVAILABLE (free) | USED: 02, 03, 07, 10, 13 (limit ≤50, client_conversation_id fixed) |
| WebSearch | AVAILABLE | USED: 01, 02-KEYWORDS, 04, 05, 09, 13 |
| TranscriptAPI | AVAILABLE | USED: 05/06 (25 YouTube transcripts → Q-Y-####), 11 ×0 |
| Exa research agent | AVAILABLE (~$0.03–0.10/run) | USED: 01-DEEP, 04, 05, 06 partials + merge ($1.055 + $0.825), 09 ($0.30+), 11-AV-03 ($0.10), 13 ($0.20) → ≈$5.30 cumulative (agent-reported, not metered) |
| Higgsfield | AVAILABLE 1,998.34 cr | USED: 13 only — 10 images 20.50 cr → 1,977.84 cr (live read) |
| Apify | UNAVAILABLE (monthly hard limit) | NOT USED — every planned actor printed `NOT RUN — Apify monthly limit` |
| Firecrawl scrape | UNAVAILABLE (insufficient credits) | NOT USED |
| Browserbase | UNAVAILABLE (401) | NOT USED |
| WebFetch / curl | UNAVAILABLE (egress 403 on every research host) | NOT USED after the W0 probe |
| TikTok Ads MCP | UNAVAILABLE (OAuth not granted) | NOT USED |
| Meta EAS / search volume | no tool | UNSIZED / UNSCANNED |
| Bash + python3 | AVAILABLE | every count |

### H · SPEND RECONCILIATION
- GetHookd: 291.22 → 282.89 (live at close) = **8.33 cr**; cap for a standard run ≈8–10 cr incl. seeds → at cap; CREDIT-NOTE on STATUS for 01 SEED (0.6 vs 0.5) and 02 (≈9.9 vs 5–7 band, reason: 3 original seeds carried no ad corpus, 5 new-seed crawls added).
- Apify: **$0.00** (blocked). Firecrawl **$0**. Browserbase **$0**.
- Exa: **≈$5.30** (sum of agent-reported runs; no meter available).
- Higgsfield: 1,998.34 → 1,977.84 = **20.50 cr** (13 only).
- Cash total this run ≈ **$5.30** + credits above.

### I · WALL-CLOCK PER WAVE (STATUS clock: WAVE-START line → WAVE-END line; run started 19:41:38Z, W0 opened 20:12:38Z after a 31-min preflight: unzip, prompt files, tool checks)

| wave | start | end | wall-clock | band | note |
|---|---|---|---|---|---|
| W0 | 20:12:38 | 20:26:22 | 0:14 | ≈0:10 | 01 SEED (PDP blocked → Exa route in DEEP) |
| W1 | 20:26:47 | 21:19:15 | 0:52 | 0:30–0:40 | OVER: 15 agents, 5 new-seed crawls added after the 3 seeds carried no ads |
| W2 | 21:19:15 | 21:46:17 | 0:27 | 0:20–0:40 | 03, 06-MERGE (override 30/80), 07-SOPH |
| W3 | 21:46:17 | 22:07:57 | 0:22 | 0:20–0:40 | 07 FULL, 08, 10 |
| W4 | 22:07:57 | 22:28:47 | 0:21 | 0:20–0:40 | 09 |
| W5 | 22:28:47 | 22:50:49 | 0:22 | 0:25–0:45 | 7 agents (5× 11-AV, 12-OFFER, 13) |
| W6 | 22:51:20 | 23:16:23 | 0:25 | short | 12 ASSEMBLE (override 40/120) |

### J · RULE BREACHES STATED (none hidden)
- 7 partial handoff JSONs exceed 2 KB (02-KEYWORDS 3,515 B; 02-NW-NEW-SEED-04 2,118; 02-NW-NEW-SEED-05 2,068; 04-PB-05 2,333; 04-PB-06 2,067; 06-PB-01 2,221; 06-PB-05 2,064). Every merged nn-HANDOFF.json is ≤2 KB.
- 13: all 10 renders exceed width+height ≤2000 px (model 1k defaults); product Element built from the uncut shot (remove_background stayed queued); no render proofread (CDN 403) — stated in 13-BRAND.md.
- 01 SEED 0.6 cr vs 0.5 cap; 02 ≈9.9 cr vs 5–7 band (CREDIT-NOTE on STATUS).
- audit.py flags the HARVEST-LOG files as lacking a coverage statement (coverage lives in the handoff) — logged AUDIT-PARTIAL with the note.
- W1 over its band (0:52 vs 0:40); W0 over (0:14 vs ≈0:10).
- The W0–W5 WAVE-END lines print agent-reported clocks ≈13–41 min ahead of the STATUS clock; a CORRECTION line was appended and this table uses STATUS timestamps only.
- MAX_PARALLEL_AGENTS 8 never exceeded (highest RUNNING count on any STATUS line: 8 of 8, during W1).


### K · GATES AND LABELS
- MAX_PARALLEL_AGENTS 8: highest RUNNING count on any STATUS line is 8 of 8 (W1); never exceeded.
- Labels used across every deliverable (grep count): 
```
21 CONTESTED
    343 EARLY SIGNAL
    305 HYPOTHESIS
     16 REJECTED
    405 SUPPORTED
    643 VALIDATED
```
- `REJECTED` occurrences (must be category errors only) — every line, for the reader to check:
```
01-PRODUCT-TRUTH.md:227:distinct_speakers counts non-owned speakers only (VOC); owned speakers print separately and never raise a label (rule 4 + brief). Operator ICP (b) 'adults 50+ with money' as wr
03-VALIDATED-MESSAGING.md:370:- Operator ICP (b) "adults 50+ with money" as a demographic — REJECTED at 01 (demographic ≠ population); the situation CP-06 is what is sold (IM-19, IM-20).
04-COMMUNITY-MAP.md:198:Counter: PH 21/8 floor (≥3/CP met: CP-03 has 3+, CP-05 has 3) · VALIDATED 6 · SUPPORTED 5 · EARLY SIGNAL 5 · UNPROVEN 5 · REJECTED 0.
06-VOC-REPORT.md:752:Notes [D]: AS-02 — Q-O-0018 excluded from both sides (speaker is a mother deferring to her husband: bears on CP-02, not on 'fathers'). 'parent with kids' is CONFIRMED as a situa
08-DESIRES-LF8.md:726:| RJ-04 | KD-b "an online business at 50+ with money" (operator) | broader outcome (+ demographic band — 01 REJECTED it as a population) | MD-06 |
10-MECHANISMS.md:299:**KEEPERS re-filed (category error = the only REJECTED in this step; 9):**
13-BRAND.md:35:Tally computed in code over 06-VOC_MASTER.csv (unique_author_id, thread_id) for the Q-## each 06 ledger (FS-02, FS-03, SK-02/03/06, worldview_map) and 10 §15 anchor names as *blaming* 
13-BRAND.md:42:| E-D · the free / $20 store with a catch (upsells and fees after you pay) | suspects | 4 of 180 authors | 4 | Q-Y-0009, Q-B-0001, Q-O-0028, Q-O-0135 | 0 (NW-04 / NW-06 SELL it) | **LK
13-BRAND.md:45:| E-G · EcomXpertz (a named competitor) | blames (vendor) | 3 of 180 authors (MARKET+OWNED only: 0 authors / 0 threads) | 1 | Q-E-0006, Q-E-0007, Q-E-0009 | n/a | n/a | n/a | REJECTED 
13-BRAND.md:46:| E-H · Shopify / the platform's support | blames (platform) | 1 of 180 authors | 1 | Q-F-0011 | n/a | n/a | contradicts PT-04 / PT-14 (Readymerce builds on Shopify/Etsy) | REJECTED (c
13-BRAND.md:49:**Pick (by author count among non-REJECTED, clean before SELF-EXPOSURE [A]):**
13-BRAND.md:51:- **EN-1 · enemy: "the build-and-leave store deal"** — you pay someone to build a store; it arrives half-done, locked, or finished-and-abandoned on launch day, and the running is lef
```
- One writer per file: 12 ASSEMBLE wrote 11-BELIEFS.md / 11-HANDOFF.json as the designated merger; 12-partials/*, 13-BRAND.md, 13-HANDOFF.json and 06-VOC_MASTER.csv unchanged in W6 (git diff). 00-STATUS.md and 00-RUN-CARD.md written only by the orchestrator.

### L · handoff.json v2 VERIFICATION (python3, not by eye)
- required top-level keys 65/65 present (67 total), `handoff_version` 2, `generated_at` present, `ready_for_P3` "OPERATOR-CLEARED", PATCH NOTE present, `coverage_statement` present.
- brand keys from 13 present: brand_name, positioning, narrator_archetype, photographic_register, identity, tribe_aesthetic, congruence_spec, fact_sheet, name_options (9/9); `fact_sheet` rows 27, 13's three `LATE-BOUND: 11.* / 12.*` rows filled with `filled_by: "12 ASSEMBLE"` and 13's original text kept beside as `value_13`.
- `late_bound[]` = ["OPERATOR-VALIDATES: booked-call proxy economics (close 4.76% SAMPLE(84))", "OPERATOR-VALIDATES: 60-day deliverables guarantee (replaces PT-15) + legal", "OPERATOR-VALIDATES: T2/T3 prices, bump/OTO prices", "OPERATOR-VALIDATES: build 7\u201310 days before print", "13.name_status PROVISIONAL (USPTO NOT FETCHED)"]
- `avatar_portfolio` = {"primary": "AV-07", "launch": ["AV-07", "AV-01", "AV-04", "AV-02", "AV-03"], "reserve": ["AV-06 (UNPROVEN, operator hypothesis b)", "AV-05 (UNPROVEN, operator hypothesis a)", "CL-09 (RESERVE)"], "testing_sequence": ["AV-07", "AV-01", "AV-04", "AV-02", "AV-03"], "expansion_queue": ["AV-08"]}
- `test_cells` 18 · `writer_handoff` for AV-07, AV-01, AV-04, AV-02, AV-03 (26/26 each) · `voc_corpus.q_count` 333 (method: python3 csv count).
- 11-HANDOFF.json 2,030 B and 12-HANDOFF.json 1,113 B (≤2,048 B rule met; the 7 over-size partial handoffs are listed in §J).

### M · WEAKEST LINK (named by the agents themselves, converging) + COST TO CLOSE
- 12 ASSEMBLE: "zero Readymerce outcome proof plus a purchase-level test the $100/day budget cannot fund — the whole plan rides a booked-call proxy built on 4 closes in 84 seller-contacted calls."
- 13: "proof congruence (actor-testimonial disclosure + disputed access complaint PT-10 vs a peer-owner, keys-in-your-name brand) and unfetched name clearance."
- 06-MERGE / 09: the Reddit lane (the largest expected MARKET_VOC population) is fully BLOCKED-ON-TOOL; every Reddit-shaped floor was filled from Shopify's own forum, YouTube transcripts and Exa page reads.
- Cost to close: operator written confirmation of the booked-call proxy, the post-launch window and the per-stage product count ($0); one ≈1-hour build demo shoot ($0); one consenting client's post-launch report (weeks); ≥3 consenting real owners for proof; restore Apify (or paste 5–10 top Reddit threads) to run HARVEST-01/09/23 (≈$1 of actor runs); one manual USPTO search; operator yes on `start_brand_spy` (8 cr) for get_top_ads + narrator counts; network access to readymerce.com / trustpilot.com / reddit.com for direct fetches.

### N · OPERATOR QUESTIONS STILL OPEN (never answered during the run)
1. `start_brand_spy` (8 cr) — yes/no. 2. Restore tool access: environment network policy (WebFetch/curl 403), Apify monthly limit, Firecrawl credits, Browserbase key, TikTok Ads OAuth. 3. The two ICP hypotheses were tested, not assumed: AV-05 Evening-Only Parent (fathers) and AV-06 Fixed-Income Retiree (50+ with money) are both UNPROVEN in reserve — see 09-AVATARS.md and handoff.json `avatar_portfolio`.

RUN COMPLETE · waves 7/7 · files 37/37 · PARTIAL agents [] · open HARVEST-## [01–23] (HARVEST-24 closed) · BLOCKED-ON-TOOL [Apify all actors, Firecrawl scrape, Browserbase, WebFetch/curl egress, TikTok Ads MCP, Meta EAS, search volume, Higgsfield CDN download; get_top_ads NOT RUN — needs operator yes: start_brand_spy] · wall-clock 3:34 · weakest link: zero Readymerce outcome proof (site disclaims income, reps claim 91%/$10k → DNS; 4 owned closes in 84 calls, all at $500) and a Reddit/Trustpilot lane fully BLOCKED-ON-TOOL, so the test plan rides a booked-call proxy · cost to close: operator confirms the proxy, the post-launch window and the per-stage product count ($0); one ≈1-hour build demo shoot ($0); one consenting client's post-launch report; restore Apify or paste 5–10 Reddit threads (≈$1 of actor runs, HARVEST-01/09/23); operator yes on start_brand_spy (8 cr)
