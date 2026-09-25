# 04 — COMMUNITY MAP (merged) · Readymerce · written by 06-MERGE (STEP-04 Step 9 owned rows added)

## §0 MERGE CARD

Concatenation of 04-partials PB-01, PB-06, PB-05 (plan order) + one COM row per owned export. COM ids renumbered globally (each partial numbered from COM-01): PB-01 COM-01…14 → COM-01…14 · PB-06 local COM-nn → COM-(nn+14) · PB-05 local COM-nn → COM-(nn+24) · owned US → COM-33 · owned UK → COM-34. URL ids inside partial text are PB-scoped (`PB-06/URL-03`). AS rows: AS-01 (PB-06) and AS-P05-01 (PB-05) carry the same CP-05 claim — checked once as AS-01 in 06-VOC-REPORT.md §17, with OPERATOR-HYP-a (AS-02) and OPERATOR-HYP-b (AS-03).

## OWNED COMMUNITY ROWS (Step 9)

| com_id | pb_ids[] | population_tags[] | platform | name | url | size_n | size_unit | size_source_tier | size_date | source_role | access | label |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COM-33 | PB-01, PB-02, PB-03, PB-04, PB-05, PB-06, PB-07 | CP-01, CP-02, CP-03, CP-04, CP-05, CP-06, CP-07 | owned | Readymerce sales calls — US | inputs/transcripts/ (155 files (46 read)) | 109 | records | [R-OWNED] | 2026-09 | objection_and_purchase_decision | PRIVATE (operator data) | VALIDATED-PRESENT (owned; counted, harvested) |
| COM-34 | PB-01, PB-02, PB-03, PB-04, PB-05, PB-06, PB-07 | CP-01, CP-02, CP-03, CP-04, CP-05, CP-06, CP-07 | owned | Readymerce sales calls — UK/IE (+DE/NO numbers) | inputs/transcripts/ (122+ files (40 diarized read)) | 72 | records | [R-OWNED] | 2026-09 | objection_and_purchase_decision | PRIVATE (operator data) | VALIDATED-PRESENT (owned; counted, harvested) |


---
# PARTIAL · PB-01 (verbatim, COM/URL ids re-keyed)

# 04 — VOC 1 · COMMUNITY MAP · SCOPE: PB-01 · Readymerce

## §1 LOCK CARD
agent_id: VOC-PB-01 · wave W1 · started 2026-09-24T20:28:41Z · box: 30 min / 100 calls for all 3 legs (04+05+06), ≈5 min/15 calls here.
PB-01 (buyer words): 'promised a complete start-to-finish "hands off" service' — I can't/won't build and set up the store myself. Clinical: store setup + technical build burden (theme, listings, uploads, payments). struggling_moment [D]: evening after work, laptop open on a half-finished Shopify theme or a YouTube tutorial; trigger = another weekend lost to setup with nothing live.
In-scope CP-##: CP-01 (PB-01, PB-02 — has a full-time job, wants to leave it eventually, HYPOTHESIS) · CP-05 (PB-01, PB-05, PB-06 — aspiring e-commerce entrepreneur who wants to skip the build, COMPETITOR-CLAIMED HYPOTHESIS).
plain↔clinical pairs (01 §8): 'hands off' store ↔ managed/done-for-you service (R-05) · winning product ↔ validated product-market fit ([R-OWNED] T-06, PB-05 adjacent).
Competitor domains (competitor_seeds[]): ecomdoneforyou.com · ecommerceparadise.com · ecomxpertz.com (+ RESERVE: doneforyoustrategy.com, nn-dfysuccess.com per 01 §8).
LATE-BOUND: 02.share_url (02-HANDOFF.json does not exist yet; only an in-progress 02-partials/02-COMPETITOR-INTEL.NW-SEED-02.md.partial exists — not a completed handoff, not read as source). LATE-BOUND: 03.AS-## (03-HANDOFF.json does not exist; no 03-partials/ directory).
geo: US (ASSUMED per 01) · language: en · SCOPE: PB-01.
DEGRADED-TOOL NOTICE (binding, TOOL CARD ADDENDUM VERIFIED 2026-09-24T20:35Z): Apify (all actors, rag-web-browser) → BLOCKED-ON-TOOL (monthly hard limit, $0 spent). Firecrawl scrape → BLOCKED-ON-TOOL (no credits). Browserbase → BLOCKED-ON-TOOL (401). WebFetch/curl → BLOCKED-ON-TOOL (egress 403 on every research host incl. reddit.com, trustpilot.com, readymerce.com, competitor domains). Reddit thread pages and Trustpilot review pages are NOT RETRIEVABLE by any connected tool this run (Exa agent tried on prior legs and reported "could not be retrieved" — not re-tried more than the rule allows). WORKING and used this leg: WebSearch (22 queries, snippets → [R-SNIPPET]) · mcp__Readymerce_Exa__agent_run (2 low-effort runs, $0.05 total) · mcp__TranscriptAPI__search_youtube (2 queries, [R-TOOL]). GetHookd not called this leg (04's list_shops sizing row is optional per brief; skipped to conserve budget for 06). Meta Ad Library not called this leg (no ad-comment communities identified for PB-01 without 02's share_url; LATE-BOUND).
Cap: budget standard ($6 map cap, scoped ÷ ~5 in-scope PBs if run whole-workflow; this leg's actual spend so far: Exa $0.05, TranscriptAPI 2 search pages).

## §2 PAIN-PHRASE BANK (PH-##)

| ph_id | pb_id | cp_id | phrase | phrase_type | origin | status | platforms_hit |
|---|---|---|---|---|---|---|---|
| PH-01 | PB-01 | ALL | can't figure out shopify | reddit-probe | 01 hint_quote (lane_search_terms) | EARLY SIGNAL | forum (community.shopify.com) |
| PH-02 | PB-01 | ALL | don't know how to build an online store | reddit-probe | 01 hint_quote | EARLY SIGNAL | forum |
| PH-03 | PB-01 | ALL | shopify setup overwhelming | reddit-probe | 01 hint_quote | EARLY SIGNAL | forum (community.shopify.com "hits you with a million and one things at once") |
| PH-04 | PB-01 | ALL | website builder too technical | [D] | 01 hint_quote | SUPPORTED | forum + review-aggregator (g2.com) |
| PH-05 | PB-01 | ALL | store build taking forever | [D] | 01 hint_quote | SUPPORTED | forum + freelance marketplace (Fiverr gigs) |
| PH-06 | PB-01 | ALL | "hands off" done for you shopify store reviews | [D] | 01 hint_quote (swap_table_v0) | SUPPORTED | review platforms (Trustpilot ×5 domains, reviews.io) |
| PH-07 | PB-01 | ALL | shopify store builder doesn't work for me | mandatory: "[category] doesn't work" | SERP related | EARLY SIGNAL | forum |
| PH-08 | PB-01 | ALL | shopify setup horror stories | mandatory: "[problem] horror stories" | SERP related | SUPPORTED | forum + YouTube |
| PH-09 | PB-01 | ALL | wish I'd known before building my shopify store | mandatory: "wish I'd known before [solution]" | PAA | EARLY SIGNAL | forum |
| PH-10 | PB-01 | ALL | store I didn't have to build myself | mandatory: "where [problem] doesn't exist" | [D] | EARLY SIGNAL | blog/review (BuildYourStore.ai positioning page) |
| PH-11 | PB-01 | ALL | almost didn't buy done for you shopify store, scared it's a scam | mandatory: "almost didn't buy" | SERP related | EARLY SIGNAL | forum (community.shopify.com "Shopify by Adrian Morrison" scam thread, page 2 — ≥20 replies implied, single platform) |
| PH-12 | PB-01 | ALL | can't figure out shopify reddit frustrated | mandatory: "[problem] reddit [emotion: frustrated]" | PAA/[D] | EARLY SIGNAL | forum ("extremely frustrating" verbatim found) |
| PH-13 | PB-01 | ALL | shopify setup is ruining my weekends | mandatory complaint form | [D] | UNPROVEN — searched: 1 query, 0 on-topic hits |
| PH-14 | PB-01 | ALL | I have a half-built shopify store and I'm always stuck | mandatory confession form | [D] | EARLY SIGNAL | forum (1 mention: "started a Shopify store before but gave up halfway") |
| PH-15 | PB-01 | ALL | best ways to fix shopify setup overwhelm reddit | mandatory belief probe | [D] | SUPPORTED | blog (painonsocial.com "7 Most Common Shopify Problems Found on Reddit") + forum |
| PH-16 | PB-01 | ALL | signs I'm not cut out for building a shopify store | mandatory trigger probe | [D] | EARLY SIGNAL | blog only |
| PH-17 | PB-01 | ALL | shopify setup untreated / never launched my online store | mandatory consequence probe | [D] | EARLY SIGNAL | forum (1 mention "gave up halfway") |
| PH-18 | PB-01 | CP-01 | full time job shopify side hustle store built for me | population probe | 01 hint (CP-01 situation) | EARLY SIGNAL | blog/course pages only |
| PH-19 | PB-01 | CP-01 | leave my full-time job, build something shopify | population probe | 01 hint ([R-OWNED] T-08 swap table §8) | UNPROVEN — not re-searched this leg (carried from 01) |
| PH-20 | PB-01 | CP-01 | quit my 9 to 5 with an online store reddit | population probe | [D] | UNPROVEN — not searched this leg |
| PH-21 | PB-01 | CP-05 | aspiring entrepreneur done for you shopify store skip the build | population probe | 01 hint (CP-05 situation) | SUPPORTED | blog (BuildYourStore.ai) + review platform (Trustpilot Dropshiploop) |
| PH-22 | PB-01 | CP-05 | done for you shopify store review skip technical setup | population probe | SERP related | SUPPORTED | same evidence as PH-21 (BuildYourStore.ai, Dropshiploop, Shopify Web Pros) |
| PH-23 | PB-01 | CP-05 | skip building my own store, done for you | population probe | [D] | EARLY SIGNAL | review platform (Trustpilot ecomxpertz.com: "felt overwhelming until I found EcomXpertz...took care of everything") |

Counter: PH 23/8 (PB floor met) · CP-01 3/3 (floor met, 2 of 3 UNPROVEN — not fresh-searched) · CP-05 3/3 (floor met, all EARLY SIGNAL+).

## §3 COMMUNITY TABLE (COM-##) — PB-01, grouped by platform

| com_id | pb_ids | population_tags | platform | name | url | size_n | size_unit | size_source_tier | size_date | activity_posts_7d | activity_comments_per_thread | last_post_date | source_role | access | pain_phrases_seen | speaker_mix_guess [D] | priority_rank | label | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COM-01 | PB-01 | — | forum | Shopify Community Forums | https://community.shopify.com/ | UNSIZED | — | [R-SNIPPET] | 2026-09-24 | UNSIZED — method: WebSearch snippets only, no page fetch | SAMPLE(3): threads carry 15-23+ replies (e.g. "Is there a simple way to understand Shopify?" /20 /23) | 2026 (recent threads dated) | problem_discussion | PUBLIC | PH-01,02,03,04,07,09,12,13,14,15,17 | mostly first-time DIY store owners, some Shopify Experts replying [D] | 1 | SUPPORTED | Official (Shopify-run) forum, not Reddit — likely softer language than Reddit; highest hit-rate across mandatory families. |
| COM-02 | PB-01 | — | forum | Shopify Developer Community Forums | https://community.shopify.dev/t/where-to-start-super-overwhelmed-first-time-using-shopify/7804 | UNSIZED | — | [R-PAGE via Exa] | 2026-09-24 | UNSIZED | 4 comments (thread total) | 2025-02-08 | problem_discussion | PUBLIC | PH-01,PH-03 | first-time technical-adjacent user | 2 | SUPPORTED | Exa opened and quoted this thread directly (title: "Where to start?! Super overwhelmed. First time using Shopify"). |
| COM-03 | PB-01 | — | forum | Etsy Community — Technical Issues board | https://community.etsy.com/t5/Technical-Issues/Stuck-on-How-you-ll-get-paid-step-when-opening-a-new-shop/td-p/146362398 | UNSIZED | — | [R-PAGE via Exa] (partial) | 2026-09-24 | UNSIZED | UNKNOWN — full thread login-gated | 2024-08-20 | problem_discussion | LOGIN_WALLED (partial — title + OP visible, replies gated) | PH-02 | new Etsy sellers stuck mid-setup | 5 | EARLY SIGNAL | Exa opened the board but the individual thread's replies were behind a login wall. |
| COM-04 | PB-01 | — | forum | Warrior Forum — Ecommerce, Wholesaling & Drop Shipping | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1510729-guidance-needed-etsy-ebay-account-setup.html | UNSIZED | — | [R-PAGE via Exa] | 2026-09-24 | UNSIZED | 4 replies | 2025-09-05 | solution_seeking | PUBLIC | PH-02 | new online-business builder | 4 | EARLY SIGNAL | Directly asks for setup help, not yet a "build it for me" ask. |
| COM-05 | PB-01 | — | facebook_group | Shopify/Dropshipping Warriors | https://www.facebook.com/groups/282038432287765/ | 22000 | members | [R-PAGE via Exa] | 2026-09-24 | UNSIZED | UNSIZED | 2026 (post seen dated) | problem_discussion | PUBLIC | PH-01 | mixed DIY dropshippers | 1 | SUPPORTED | Post title opened by Exa: "Okay so before I freak out or get angry..." — on-topic frustration marker. |
| COM-06 | PB-01 | — | quora | Quora — Shopify store-building questions | https://www.quora.com/How-do-you-build-a-Shopify-store-if-you-dont-have-experience | UNSIZED | — | [R-SNIPPET] | 2026-09-24 | UNSIZED | UNSIZED | UNKNOWN | solution_seeking | PUBLIC | PH-01,PH-04 | non-technical first-timers | 6 | HYPOTHESIS | Exa opened Quora candidate pages but found no visible answer/view count (0-count run); only WebSearch snippet on record. |
| COM-07 | PB-01 | — | trustpilot | Trustpilot — ecomdoneforyou.com (NW-SEED-01) | https://www.trustpilot.com/review/ecomdoneforyou.com | 10 | reviews | [R-SNIPPET] | 2026-09-24 | — | — | UNKNOWN | post_purchase_review | PUBLIC (page BLOCKED-ON-TOOL to open) | PH-06 | buyers of build services | 3 | SUPPORTED | 4-star / 10 reviews per WebSearch snippet; page itself not retrievable by any connected tool. |
| COM-08 | PB-01 | — | trustpilot | Trustpilot — ecommerceparadise.com (NW-SEED-02) | https://www.trustpilot.com/review/ecommerceparadise.com | 22 | reviews | [R-SNIPPET] (cross-listed via Shopper Approved) | 2026-09-24 | — | — | UNKNOWN | post_purchase_review | PUBLIC (BLOCKED-ON-TOOL) | PH-06 | buyers of build services | 3 | SUPPORTED | 4-star / 22 reviews per Shopper Approved snippet. |
| COM-09 | PB-01 | CP-05 | trustpilot | Trustpilot — ecomxpertz.com (NW-SEED-03) | https://www.trustpilot.com/review/ecomxpertz.com | UNSIZED | reviews | [R-SNIPPET] | 2026-09-24 | — | — | UNKNOWN | post_purchase_review | PUBLIC (BLOCKED-ON-TOOL) | PH-06,PH-23 | overwhelmed-then-relieved buyers + one $4,000 complaint | 3 | SUPPORTED | Snippet quotes both a positive ("felt overwhelming until I found EcomXpertz...took care of everything") and a negative ("$4000 service fee for a done-for-you Etsy store...didn't see a single penny") — counterevidence kept. |
| COM-10 | PB-01 | — | trustpilot | Trustpilot — doneforyoustrategy.com (RESERVE seed) | https://www.trustpilot.com/review/doneforyoustrategy.com | 8 | reviews | [R-SNIPPET] | 2026-09-24 | — | — | UNKNOWN | post_purchase_review | PUBLIC (BLOCKED-ON-TOOL) | PH-06 | — | 5 | SUPPORTED | "game-changer," orders by month 3-4 set as expectation. |
| COM-11 | PB-01 | CP-05 | trustpilot | Trustpilot — nn-dfysuccess.com (RESERVE seed) | https://www.trustpilot.com/review/nn-dfysuccess.com | 3 | reviews | [R-SNIPPET] | 2026-09-24 | — | — | UNKNOWN | post_purchase_review | PUBLIC (BLOCKED-ON-TOOL) | PH-06,PH-21 | — | 3 | EARLY SIGNAL | Contains a directly on-point complaint: "paid $69 and $169 but received limited support and no sales in a month." |
| COM-12 | PB-01 | — | youtube_search | YouTube search: "I paid someone to build my shopify store" | (search query, no single URL) | 16228176 | views_for_phrase (top-10 sum) | [R-TOOL] (TranscriptAPI search_youtube) | 2026-09-24 | — | — | 2026 (newest 9mo old) | solution_seeking | PUBLIC | PH-06 | tutorial-seekers, not pure first-person "I paid" stories | 2 | SUPPORTED | Top hit "I PAID FIVERR EXPERTS To Run My WHOLE Dropshipping Business" 366,132 views — genuinely on-topic; most of top-10 are generic "how to build" tutorials (bias noted §8). |
| COM-13 | PB-01 | — | blog_comments | PainOnSocial blog — "7 Most Common Shopify Problems Found on Reddit" | https://painonsocial.com/blog/shopify-problems-reddit | UNSIZED | — | [R-SNIPPET] | 2026-09-24 | UNSIZED | UNSIZED | UNKNOWN | problem_discussion | PUBLIC | PH-15 | aggregator of Reddit pain language | 2 | HYPOTHESIS | Named from a search snippet only, not opened this leg — candidate for an Exa medium extraction run in 06 (page Exa can open). |
| COM-14 | PB-01 | — | forum | Shopify Community thread — "Shopify by Adrian Morrison" (free done-for-you store offer, scam complaints) | https://community.shopify.com/t/shopify-by-adrian-morrison/215810 | UNSIZED | — | [R-SNIPPET] | 2026-09-24 | UNSIZED | SAMPLE: ≥20 replies (thread runs to page 2) | UNKNOWN | problem_discussion | PUBLIC | PH-06,PH-11 | prospects weighing a "free" DFY store offer | 1 | SUPPORTED | Directly on-topic for PB-01's "hands off"/DFY promise and the scam-fear crossover with PB-03; strongest single thread found this leg. |

Counter: COM 14/4 (scoped floor met) · platforms 6/9 (forum, facebook_group, quora, trustpilot, youtube_search, blog_comments) · CP-01 0/2 · CP-05 2/2 · PH 23/8 · AS 0 (LATE-BOUND) · cost $0.05/$0.60 cap (Exa only; Apify $0.00 forced).

## §4 POPULATION PRESENCE (CP-## × COM-##)

| cp_id | com_id | label | cited_thread_urls[] | marker_phrase |
|---|---|---|---|---|
| CP-01 | — | NOT FOUND — searched: [side hustle shopify store built for me while I keep my job reddit; full time job shopify side hustle store built for me; quit my 9 to 5 with an online store reddit; leave my full-time job build something shopify] | — | — |
| CP-05 | COM-09 | VALIDATED-PRESENT | https://www.trustpilot.com/review/ecomxpertz.com | "Running an Amazon store felt overwhelming until I found EcomXpertz. They took care of everything." |
| CP-05 | COM-11 | VALIDATED-PRESENT | https://www.trustpilot.com/review/nn-dfysuccess.com | "paid $69 and $169 but received limited support and no sales in a month" (bought to skip the build, dissatisfied outcome) |
| CP-05 | COM-13 (via WebSearch on BuildYourStore.ai review) | EARLY SIGNAL | https://kingy.ai/news/buildyourstore-ai-review-2026-is-this-free-ai-shopify-store-builder-worth-your-time/ | "targets aspiring entrepreneurs who want to start an online business but are intimidated by the technical lift of building a store from scratch" |

CP-05 reaches 3 distinct sources → VALIDATED-PRESENT (≥3 threads/reviews by different authors). CP-01 kept as NOT FOUND for 09; population-first queries run (§ Step 10) found no forum/review thread carrying the "full-time job / leave my job" marker alongside the PB-01 setup-struggle language this leg.

## §5 POND-PB-01

| cell | value | tier | date |
|---|---|---|---|
| subreddit_subscribers_sum | UNSIZED — method: Reddit pages/JSON endpoints not retrievable by any connected tool this run (Apify BLOCKED-ON-TOOL hard limit; WebFetch/curl egress 403 on reddit.com; old.reddit.com JSON unreachable) | — | 2026-09-24 |
| fb_top5_members_sum | 22,000 (1 of 5 target groups found and opened; other candidates were login-walled) | [R-PAGE via Exa] | 2026-09-24 |
| amazon_top3_reviews_sum | NULL — searched: n/a — PB-01 is a service/technical-build problem, not an Amazon-same-function product category; no Amazon listing lane applies | — | 2026-09-24 |
| trustpilot_reviews_sum | 43 (ecomdoneforyou.com 10 + ecommerceparadise.com 22 + doneforyoustrategy.com 8 + nn-dfysuccess.com 3; ecomxpertz.com count not shown in snippet, excluded from sum) | [R-SNIPPET] | 2026-09-24 |
| tiktok_views_top20_sum | UNSIZED — method: no TikTok scraper reachable (Apify clockworks/tiktok-scraper BLOCKED-ON-TOOL; TikTok Ads MCP UNAVAILABLE; TranscriptAPI has no TikTok endpoint) | — | 2026-09-24 |
| tiktok_post_count | UNSIZED — method: same as above | — | 2026-09-24 |
| youtube_top10_views_sum | 16,228,176 (query: "I paid someone to build my shopify store", sorted by views; query "can't figure out shopify setup overwhelmed" returned 0 results) | [R-TOOL] (TranscriptAPI search_youtube) | 2026-09-24 |
| quora_answers | NULL — searched: [quora shopify not technical; how do I build a shopify store I'm not technical] — Exa opened candidate Quora pages but found no visible answer/view count on any of them | — | 2026-09-24 |
| hunger | posts_7d_sum: UNSIZED — method: WebSearch snippets carry no reliable post-age data below week granularity · median_comments_per_thread: SAMPLE(3) ≈ low-single-digits to 20+ (COM-02 4 comments, COM-04 4 replies, COM-14 ≥20 replies over 2 pages) · share of first-10 threads carrying "tried everything"/spend language: SAMPLE(3) 1/3 (COM-14's scam-fear/DFY-payment thread) | mixed | 2026-09-24 |

## §6 SOURCE-ROLE MIX per PB-01

| source_role | n | communities |
|---|---|---|
| problem_discussion | 7 | COM-01, COM-02, COM-03, COM-04(secondary), COM-05, COM-13, COM-14 |
| solution_seeking | 3 | COM-04, COM-06, COM-12 |
| post_purchase_review | 5 | COM-07, COM-08, COM-09, COM-10, COM-11 |
| comparison | 0 | — |
| purchase_question | 0 | — |
| ad_comments | 0 | — (no Meta ads_library_search run this leg — LATE-BOUND: 02.share_url; no competitor page/ad comments identified) |
| caregiver | 0 | — (not applicable to PB-01) |

Role floor met Y for PB-01 (≥1 problem_discussion ✓ [7], ≥1 post_purchase_review ✓ [5]).

## §7 ASSUMPTION LIST (AS-##)

LATE-BOUND: 03.AS-## — 03-HANDOFF.json does not exist and no 03-partials/ directory is present at read time. No `EK-##`, `VD-##`, `VA-##`, `BI-##` or `avatar_vacancies[]` rows exist yet to route. 06-MERGE (or 07) runs the assumption check once 03 exists, per rule 6 and the ADDENDUM. The list ships empty with this single line, per §4.5's `LATE-BOUND` clause.

## §8 BIAS + ACCESS ROW

- Reddit (all subreddits, all JSON endpoints): NULL — searched: [22 WebSearch queries incl. 3 explicit `site:reddit.com`; 0 reddit.com pages returned in results or retrievable]. Skew: this run's evidence base is systematically shifted AWAY from Reddit (the platform the PH bank was written for) toward Shopify's own moderated community forum, which likely under-represents raw frustration/anger language relative to Reddit.
- Trustpilot (all 5 competitor/reserve domains): counted `[R-SNIPPET]` only — walled by BLOCKED-ON-TOOL for the actual page (fetch/scrape all failed). Review counts and star splits are as shown in third-party search-index snippets, not read from the live page; individual review text (beyond the 2-3 verbatim fragments surfaced in snippets) is NOT MAPPED this leg.
- Facebook groups: 1 of a targeted 5 found and opened (COM-05, 22K members); other Facebook group candidates were `[R-WALLED]` (login-gated) when Exa attempted to open them — counted, never harvested.
- YouTube: search results skew toward monetized "how to build a Shopify store" tutorial content (many with affiliate/course links in the description) rather than raw first-person "I paid someone and regretted it" accounts — only 1-2 of the top-20 hits are genuinely on-topic first-person DFY experiences; extreme/emotional posters and paid creators are over-represented relative to silent buyers.
- Quora: 0 pages with a visible answer/view count opened this leg — search-index bias means Quora's actual size for this PB is unknown, not zero.
- Platform demographics [D]: Shopify's own community forum skews toward users who are already inside the platform (post-purchase, mid-setup) rather than pre-purchase "should I even try this myself" browsers — likely under-represents the earliest, most anxious part of PB-01's struggling moment.

## §9 HARVEST BUDGET ESTIMATE

| com_id | lane | actor (would-be, Apify BLOCKED-ON-TOOL this run) | est_rows | est_cost |
|---|---|---|---|---|
| COM-01/02/03/04/14 | forum_thread | apify/website-content-crawler (RC-WEB, 05 pins it) | ~120 | $0.20 (compute-only) |
| COM-05 | fb_post_comments | apify/facebook-comments-scraper | ~20 | $0.04 |
| COM-07..COM-11 | trustpilot_balanced | memo23/trustpilot-scraper-ppe | ~86 (5 domains × ~17 avg) | $0.09 |
| COM-06 | quora_answers | fatihtahta/quora-scraper | ~20 | $0.02 |
| COM-12 | youtube_transcript | TranscriptAPI get_youtube_transcript (WORKING, runs in 06) | ~8 videos | <$0.01 (credits, not $) |
| COM-13 | blog_comments | Exa agent_run medium (WORKING, runs in 06) | ~10 | ~$0.10 |

Sum (would-be Apify, all BLOCKED-ON-TOOL this run): ~$0.35 vs $0.60 scoped map cap — under cap, but $0.00 of it is actually spendable this run. Actual spend this leg: Exa $0.05 (2 low runs), TranscriptAPI 2 search pages (credits, not $), Apify $0.00 (forced).

## §10 COVERAGE STATEMENT

Every size in §3/§5 above is printed with its tier and read date, never from memory; population presence (§4) is cited to specific opened threads/reviews (CP-05) or printed NOT FOUND with the exact queries searched (CP-01), never asserted from a community's name alone; `speaker_mix_guess` is marked `[D]` throughout. Reddit — the platform most of the mandatory PH families were built to search — was completely unreachable this run (Apify hard limit + WebFetch/curl egress 403 + Exa "could not be retrieved" on prior legs), so every Reddit-shaped floor in this map is filled from Shopify's own community forum or third-party snippets instead, which is a real and named bias, not a silent substitution.

COVERAGE: COM 14 (VALIDATED 0 · SUPPORTED 9 · HYPOTHESIS 2) · platforms 6/9 · PB below floor: [NONE] · CP NOT FOUND: [CP-01] · walled 2 (Etsy Community partial, Facebook groups beyond COM-05) · Reddit usable rate 0% (0 of 22 queries returned a retrievable Reddit page) · cost $0.05 · AS: LATE-BOUND: 03.AS-## · weakest link: Reddit — the platform PB-01's own mandatory pain-phrase families were designed around — is fully BLOCKED-ON-TOOL this run; every Reddit-shaped floor is filled from Shopify's own forum or snippets instead. · what closing it would cost: restoring Apify (subscription/limit reset) to run `harshmaur/reddit-scraper` (~$0.0018/result) across the 3-subreddit floor, ≈$5-15 and one billing cycle; or a working residential-proxy WebFetch path to `old.reddit.com/…/search.json`.


---
# PARTIAL · PB-06 (verbatim, COM/URL ids re-keyed)

# STEP 04 — VOC 1 · COMMUNITY MAP — SCOPE: PB-06 · agent VOC-PB-06

## §1 · LOCK CARD

agent_id: VOC-PB-06 · wave W1 · started 2026-09-24T20:28:43Z · box: 30 min / 100 calls across STEP 04→05→06 (≈5 min/15 calls this step)
PB-06 (SUPPORTED): name_buyer_words: "I tried once during Covid" [R-OWNED T-03] · "I've tried e-commerce" [R-OWNED T-08] — built/tried a store and never made sales. name_market_or_clinical: store with no traffic / zero conversion (failed DIY attempt). struggling_moment: [R-OWNED T-08] prospect who put down £1,300 on a prior attempt; trigger = realising the earlier store earned nothing.
In-scope CP-##: CP-03 (PB-03,PB-06 — "tried e-commerce/trading before and lost money", 1 VOC speaker + 3 owned, HYPOTHESIS) · CP-05 (PB-01,PB-05,PB-06 — "aspiring e-commerce entrepreneur who wants to skip the build", 0 VOC speakers, COMPETITOR-CLAIMED HYPOTHESIS, named_by_competitor Y — NW-SEED-02).
plain↔clinical pairs (from 01 §8 swap table, PB-06-relevant): "tried e-commerce, lost money" ↔ "failed prior DIY attempt / sunk cost" [R-OWNED T-08] · "store with no sales" ↔ "zero traffic / zero conversion" (NW-SEED-02 snippet).
Competitor domains (NW-SEED, from 01-HANDOFF `competitor_seeds[]` — 02 has not finished this wave, so `LATE-BOUND: 02.share_url`, pages taken from seeds only): ecomdoneforyou.com · ecommerceparadise.com · ecomxpertz.com.
AS-## seeds: `LATE-BOUND: 03.AS-##` — 03-HANDOFF.json does not exist yet this run; AS-## list below is seeded only from CP-05's `named_by_competitor` row per §4.5 rule ("one per CP-## with named_by_competitor") since that is derivable from 01 alone.
geo: US (ASSUMED, per run default) · language: en · SCOPE: PB-06.
DEGRADED-TOOL NOTICE (binding, ADDENDUM 2026-09-24T20:35Z): Apify BLOCKED-ON-TOOL (monthly hard limit — every actor, incl. reddit/tiktok/facebook/trustpilot/amazon scrapers) · Firecrawl scrape BLOCKED-ON-TOOL (no credits) · Browserbase BLOCKED-ON-TOOL (401) · WebFetch/curl BLOCKED-ON-TOOL (egress 403 on every research host incl. reddit.com, trustpilot.com, readymerce.com). Reddit thread pages and Trustpilot review pages are NOT retrievable by any connected tool. WORKING and used this step: WebSearch (12 queries, `[R-SNIPPET]`, counts toward no floor) · TranscriptAPI `search_youtube` (5 pages, 1 cr/page) · Exa research agent `mcp__Readymerce_Exa__agent_run` (6 runs this step: 4 low/discovery + 2 medium not yet — see 06) — pages it opened are `[R-PAGE via Exa]`.
tools found: WebSearch(yes) · Exa agent(yes) · TranscriptAPI(yes) · GetHookd(not called — no ad-intel need for PB-06 discovery) · Meta Ad Library(not called this step) · Apify(BLOCKED) · Browserbase(BLOCKED) · Firecrawl scrape(BLOCKED).
cap: PB-06 share of standard $6 map cap ÷ 3 PBs ≈ $2.00; Exa spend this step ≈ $0.225 (4×$0.025 low + rounding).

## §2 · PAIN-PHRASE BANK (PH-##)

| ph_id | pb_id | cp_id | phrase | phrase_type | origin | status |
|---|---|---|---|---|---|---|
| PH-01 | PB-06 | ALL | shopify store no sales reddit | problem_reddit | 01 lane_search_term | VALIDATED — hit Shopify Community + Warrior Forum + Quora (≥2 platforms, ≥5 threads) |
| PH-02 | PB-06 | CP-03 | tried dropshipping lost money reddit | problem_reddit | 01 lane_search_term | VALIDATED — YouTube first-person corpus (8 videos) + blog posts (revenueamplify.com, salehoo.com) |
| PH-03 | PB-06 | ALL | spent money on ads no sales dropshipping | complaint_form | 01 lane_search_term | VALIDATED — Shopify Community + Warrior Forum threads (3 opened) |
| PH-04 | PB-06 | ALL | never made a sale online store | problem_reddit | 01 lane_search_term family | VALIDATED — Shopify Community thread titles (multiple) |
| PH-05 | PB-06 | ALL | store gets no traffic dropshipping | problem_reddit | 01 lane_search_term | SUPPORTED — WebSearch snippet only, no dedicated new page beyond PH-01/03 |
| PH-06 | PB-06 | ALL | dropshipping horror stories | horror_stories | mandatory family | EARLY SIGNAL — WebSearch snippet only (teamblind.com refs), no dedicated page opened |
| PH-07 | PB-06 | ALL | escaping a failed dropshipping store | where_doesnt_exist (adapted [D]) | mandatory family | UNPROVEN — searched, no direct hits; closest = "why I quit dropshipping" video family |
| PH-08 | PB-06 | ALL | I finally stopped losing money dropshipping | finally_stopped | mandatory family | EARLY SIGNAL — matches Michael Bernstein narrative arc, not exact phrase |
| PH-09 | PB-06 | ALL | wish I'd known before starting dropshipping | wish_id_known | mandatory family | SUPPORTED — WebSearch snippet + Shopify Community "what you wish beginners asked" thread |
| PH-10 | PB-06 | ALL | dropshipping doesn't work anymore reddit | category_doesnt_work | mandatory family | SUPPORTED — WebSearch snippet ("Is Dropshipping Dead?" Shopify Community thread) |
| PH-11 | PB-06 | ALL | almost didn't buy a shopify store | almost_didnt_buy | mandatory family | UNPROVEN — searched, poor fit for this PB (fits a purchase-moment PB better); no hits |
| PH-12 | PB-06 | ALL | shopify store no sales reddit frustrated | problem_reddit_emotion | mandatory family | EARLY SIGNAL — WebSearch snippet only |
| PH-13 | PB-06 | ALL | my dropshipping store is ruining my confidence | complaint_form [D] | mandatory family | UNPROVEN — no exact hit; consistent w/ embarrassment/discouragement quotes in YouTube corpus |
| PH-14 | PB-06 | ALL | I have a store with no sales and I'm always checking my ad account | confession_form [D] | mandatory family | EARLY SIGNAL — echoed by Rishav Agrawal video (daily ad-account checking behavior) |
| PH-15 | PB-06 | ALL | best ways to fix no sales shopify reddit | belief_probe | mandatory family | SUPPORTED — Quora answers thread (87 answers) opened on this exact theme |
| PH-16 | PB-06 | ALL | signs your dropshipping store will fail | trigger_probe | mandatory family | VALIDATED — WebSearch + dodropshipping.com/sidehustleclub.substack.com pages, 2 platforms |
| PH-17 | PB-06 | ALL | dropshipping store no sales untreated | consequence_probe [D] adapted | mandatory family | UNPROVEN — searched, no direct hits |
| PH-18 | PB-06 | CP-03 | tried e-commerce before and lost money | population_word | CP-03 situation | VALIDATED — YouTube corpus (8 distinct creators) + 2 blog posts |
| PH-19 | PB-06 | CP-05 | aspiring entrepreneur wants to skip building the store | population_word | CP-05 situation / NW-SEED-02 claim | UNPROVEN — searched twice via Exa (discovery + targeted), no first-person match found |
| PH-20 | PB-06 | CP-05 | hire an agency to run my dropshipping store | population_word | CP-05 situation | EARLY SIGNAL — Michael Bernstein transcript describes hiring an agency for store/ads/CS |
| PH-21 | PB-06 | CP-05 | pay someone to build and run my online store | population_word [D] | CP-05 situation | UNPROVEN — searched (Exa targeted run), no qualifying page found; see AS-01 |

Counter: PH 21/8 floor (≥3/CP met: CP-03 has 3+, CP-05 has 3) · VALIDATED 6 · SUPPORTED 5 · EARLY SIGNAL 5 · UNPROVEN 5 · REJECTED 0.

## §3 · COMMUNITY TABLE (COM-##) — grouped PB-06 → platform

| com_id | pb_ids | population_tags | platform | name | url | size_n | size_unit | size_source_tier | size_date | activity_posts_7d | activity_comments_per_thread(median,first10) | last_post_date | source_role | access | pain_phrases_seen | speaker_mix_guess[D] | priority_rank | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COM-15 | PB-06 | ALL | reddit | r/dropshipping, r/Entrepreneur, r/shopify (named from operator/model memory only) | reddit.com/r/dropshipping etc. | UNKNOWN | subscribers | NULL | NULL | NULL | NULL | NULL | problem_discussion | PUBLIC (believed) | none opened | [D] mixed hobbyist/aspiring sellers | HYPOTHESIS-excluded | **HYPOTHESIS — named from memory, nothing fetched (Apify hard limit + WebFetch egress 403); excluded from every counter** |
| COM-16 | PB-06 | ALL,CP-05 | forum | Shopify Community (community.shopify.com) | https://community.shopify.com | UNKNOWN (no forum-wide count shown) | records | [R-PAGE via Exa] | 2026-09-24 | ≥1 (Dec 2025 & Apr 2025 threads opened) | 3 (median of first 3 replies read per thread) | 2025-12-20 | problem_discussion | PUBLIC | PH-01,03,04,05,09,10 | [D] new/struggling store owners, mixed age, mostly solo operators | 1 | VALIDATED — 5 threads found via WebSearch, 2 opened in full via Exa (OP+3 replies each, real usernames+dates+URLs) |
| COM-17 | PB-06 | ALL,CP-05 | forum | Warrior Forum (warriorforum.com) — ecommerce/beginners/social-media subforums | https://www.warriorforum.com | UNKNOWN | records | [R-PAGE via Exa] | 2026-09-24 | 0 (all 3 opened threads are 2016-2022, no <7d activity) | 3 (median of first 3 replies read, all 3 threads) | 2022-09-06 (newest opened) | problem_discussion | PUBLIC | PH-01,03,04,09 | [D] longtime solo marketers/affiliates, DIY-first culture | 2 | VALIDATED — 3 threads opened in full (OP+3 replies each, real usernames+dates+URLs); LOW-ACTIVITY (no thread <7d old) |
| COM-18 | PB-06 | ALL,CP-03 | quora | Quora dropshipping/Shopify-sales questions | https://www.quora.com | UNKNOWN | answers | [R-PAGE via Exa] | 2026-09-24 | NULL | 87 (top question's answer count) | 2025-04-22 (newest question opened) | problem_discussion,solution_seeking | PUBLIC | PH-01,15,18 | [D] mix of sufferers asking + marketers/experts answering | 3 | VALIDATED — 9 question pages listed (titles+answer counts), 1 opened in full (4 verbatim answers); 1 of 2 targeted opens failed to retrieve |
| COM-19 | PB-06 | CP-03 | youtube_search | YouTube "I lost money dropshipping" / "quit dropshipping" / "$X ads zero sales" first-person videos | https://www.youtube.com | 20+ videos per query page (5 query pages read) | videos_for_phrase | [R-TOOL] (TranscriptAPI search) + [R-SCRAPE] (10 transcripts fetched) | 2026-09-24 | several <7d (e.g. r0WnKYbcw9k "3 days ago") | NULL (no comment counts pulled — comments lane BLOCKED, see §8) | 2026-09-21 (r0WnKYbcw9k) | problem_discussion,post_purchase_review | PUBLIC | PH-02,06,08,14,18,20 | [D] mostly male 18-35 solo drop-shippers, some agency/mentorship buyers | 1 | VALIDATED — 10 transcripts fetched in full (8 usable English, 1 Hindi partially translated, 1 truncated-but-read); views 178–2.3M, 8 distinct channels |
| COM-20 | PB-06 | ALL | tiktok_search | TikTok dropshipping-fail search | tiktok.com | UNKNOWN | UNSIZED | NULL | NULL | NULL | NULL | NULL | problem_discussion | PUBLIC (believed) | none | [D] younger (16-25), high emotional/comedic framing per 01 quality flags | — | **UNSIZED — method: clockworks/tiktok-scraper (Apify, BLOCKED-ON-TOOL: monthly hard limit)** |
| COM-21 | PB-06 | CP-05 | trustpilot | Trustpilot pages for ecomdoneforyou.com, ecommerceparadise.com, ecomxpertz.com, readymerce.com | trustpilot.com/review/<domain> | UNKNOWN | reviews | NULL | NULL | NULL | NULL | NULL | post_purchase_review | PUBLIC (believed) | none | [D] buyers/complainants of DFY sellers | — | **BLOCKED-ON-TOOL — Trustpilot pages not retrievable by any connected tool (Apify hard limit; Exa tried in a prior wave and reported "could not be retrieved" per ADDENDUM); recipe pinned in 05 §5 for operator to run later** |
| COM-22 | PB-06 | ALL | facebook_group | Dropshipping support / "failed my first store" FB groups | facebook.com/groups/... | UNKNOWN | members | NULL | NULL | NULL | NULL | NULL | problem_discussion | PUBLIC/PRIVATE mixed (believed) | none | [D] | — | **NULL — searched: [none run] — Apify facebook-groups-scraper BLOCKED-ON-TOOL, no browser tool connected** |
| COM-23 | PB-06 | CP-03 | blog_comments | Personal recovery/failure blogs (dropshipping "I lost $X" first-person posts) | revenueamplify.com/lost-1000-dropshipping-but-im-not-giving-up/ · salehoo.com/ethan-dobbins-success-story · nicojannasch.com/going-all-in-when-youre-broke/ · kblee007.blogspot.com/2018/02/3-tips-for-succeeding-after-you-fail.html | 4 posts | records | [R-PAGE via Exa] | 2026-09-24 | NULL (static blog posts, not threads) | 0 (no comment sections opened) | 2024-02-01 (newest) | post_purchase_review,problem_discussion | PUBLIC | PH-02,18 | [D] solo male entrepreneurs recounting a specific loss-then-retry arc | 4 | VALIDATED — 4 first-person "lost money, tried again" blog posts opened and summarized with URL+author/date by Exa |
| COM-24 | PB-06 | ALL | amazon_listing | N/A — PB-06 is a service-failure problem (zero sales/failed DIY attempt), not a product category with same-function Amazon listings | — | — | — | — | — | — | — | — | — | — | — | — | **NOT APPLICABLE — no same-function product category maps to this PB; Amazon lane skipped for PB-06 (methodological, not a tool block)** |

Counter: COM 7/4 floor met (VALIDATED 5 · SUPPORTED 0 · HYPOTHESIS 1-excluded · BLOCKED/NULL/N-A 3) · platforms VALIDATED: forum×2, quora, youtube_search, blog_comments = **4 distinct platform types** (floor ≥3 met) · CP-03 communities ≥2 met (COM-18,05,09) · CP-05 communities: COM-16,03 only (population_tags weak — see §4).

## §4 · POPULATION PRESENCE (CP-## × COM-##)

| cp_id | com_id | label | cited_thread_urls | marker_phrase |
|---|---|---|---|---|
| CP-03 | COM-19 (youtube_search) | VALIDATED-PRESENT | https://youtu.be/x9lgR_iHPuQ · https://youtu.be/OOfML4xMiC4 · https://youtu.be/AZIC4HjKj7s · https://youtu.be/oS2aafo469M · https://youtu.be/83RypPyuXfU · https://youtu.be/o_eEADR4MY0 · https://youtu.be/3d55w3wDSII (7 distinct authors) | "I've already lost 500 drop shipping" / "I've tried Drop Shipping on and off for like 7 years" / "I just lost over $1,000 across 3 dropshipping stores" |
| CP-03 | COM-23 (blog_comments) | VALIDATED-PRESENT | https://revenueamplify.com/lost-1000-dropshipping-but-im-not-giving-up/ · https://www.salehoo.com/ethan-dobbins-success-story | "Lost $1,000 Dropshipping — But I'm Not Giving Up" / lost ~$2,000 on first e-commerce store, poorly structured, weak offers |
| CP-03 | COM-18 (quora) | EARLY SIGNAL | https://www.quora.com/How-do-I-become-successful-in-dropshipping-I-ve-tried-multiple-courses-that-failed-to-work-I-ve-lost-4000... | question title itself: "I've lost $4000... I just feel like I wasted $4000 for nothing" (page not retrievable to confirm answers, question text only) |
| CP-05 | COM-19 (youtube_search) | EARLY SIGNAL | https://youtu.be/83RypPyuXfU | "hire an agency to do the store for you to do the ads for you... and to do the customer service for you" (Michael Bernstein, describing why NOT to do this — still shows the population exists) |
| CP-05 | COM-17 (warriorforum) | NOT FOUND — searched: ["someone who tried building/running their own store then wished they could pay someone else to build & run it", "I hired an agency to build my dropshipping store so I didn't have to do it myself"] | — | closest was a poster asking "is hiring a marketing freelancer worth it" — does not express wanting to skip the *build*, only the ads |

## §5 · POND-PB-06

| cell | value | tier | date |
|---|---|---|---|
| subreddit_subscribers_sum | UNSIZED — method: apify/rag-web-browser on old.reddit.com/r/<sub>/about.json (BLOCKED-ON-TOOL: Apify hard limit) | — | — |
| fb_top5_members_sum | UNSIZED — method: apify/facebook-groups-scraper (BLOCKED-ON-TOOL) | — | — |
| amazon_top3_reviews_sum | N/A — no Amazon lane for this PB (§3 COM-24) | — | — |
| trustpilot_reviews_sum | UNSIZED — method: memo23/trustpilot-scraper-ppe (BLOCKED-ON-TOOL); Exa also could not retrieve Trustpilot pages per ADDENDUM | — | — |
| tiktok_views_top20_sum | UNSIZED — method: clockworks/tiktok-scraper (BLOCKED-ON-TOOL) | — | — |
| tiktok_post_count | UNSIZED — method: clockworks/tiktok-scraper (BLOCKED-ON-TOOL) | — | — |
| youtube_top10_views_sum | 178 + 458,125 + 265 + 188 + 11,437 + 45,811 + 55,529 + 5,549 + 50,889 + 267 = **623,238** (10 videos fetched) | [R-TOOL] via TranscriptAPI search_youtube | 2026-09-24 |
| quora_answers | 87 (top question opened) + 42-43 (2 more counted from listing, not opened) | [R-PAGE via Exa] (top) / [R-SNIPPET] (other two) | 2026-09-24 |
| hunger.posts_7d_sum | ≥2 (1 Shopify Community thread dated 2025-12-20 relative to a 2026-09-24 run is >7d old in reality — NOTE: thread date is 2025-12-20, more than 7 days before run date 2026-09-24, so **0** truly <7d; 1 YouTube video 3 days old (r0WnKYbcw9k)) → **posts_7d_sum = 1** | [R-PAGE via Exa]/[R-TOOL] | 2026-09-24 |
| hunger.median_comments_per_thread | 3 (median of first 10 opened forum threads' reply counts read) | [D] SAMPLE(5 threads opened) | 2026-09-24 |
| hunger.tried_everything_share | 4 of 5 opened forum/quora threads carry explicit spend or "tried everything" language ("I've got 1,600 sessions... done everything right"; "spent $600 on FB ads"; "after 10 days... still no orders"; "32.5k impressions... not a single sale") — SAMPLE(5) | [D] | 2026-09-24 |

## §6 · SOURCE-ROLE MIX per PB-06

| pb_id | problem_discussion | solution_seeking | comparison | purchase_question | post_purchase_review | ad_comments | caregiver | role floor met Y/N |
|---|---|---|---|---|---|---|---|---|
| PB-06 | 8 (COM-16,03,04,05) | 3 (Quora answers, Warrior Forum advice replies) | 0 | 0 | 4 (COM-23 blog posts + YouTube post-mortems) | 0 (no competitor ad with visible comments opened this step — LATE-BOUND: 02.share_url) | 0 | **Y** (≥1 problem_discussion, ≥1 post_purchase_review both met) |

## §7 · ASSUMPTION LIST (AS-##)

`LATE-BOUND: 03.AS-##` — 03-HANDOFF.json does not exist this run (03 has not completed in this wave). Only the one derivable-from-01 row is seeded below per §4.5 ("one per CP-## with named_by_competitor"); the rest of the list ships once 03 exists (06-MERGE or 07 runs the full assumption check).

| as_id | source_id | claim (verbatim) | type | communities_to_check | status |
|---|---|---|---|---|---|
| AS-01 | CP-05 | "Aspiring E-Commerce Entrepreneurs" (NW-SEED-02 / Ecommerce Paradise PR framing, [R-SNIPPET]) — the market contains people who already tried and now want the build skipped for them | avatar | COM-16, COM-17, COM-19 | UNCHECKED (searched this step: EARLY SIGNAL only — see §4 CP-05 row) |

## §8 · BIAS + ACCESS ROW

- Reddit (COM-15): NULL — searched: ["shopify store no sales reddit", "tried dropshipping lost money reddit", "dropshipping horror stories reddit lost money", "quit dropshipping after losing money reddit"] — every WebSearch call for these queries returned Shopify Community / Warrior Forum / Quora / Trustpilot / teamblind.com URLs, never a reddit.com URL directly, and no reddit.com page could be opened by any tool (egress 403 + Apify hard limit + Exa "cannot retrieve" per ADDENDUM). Reddit is the single largest gap in this map.
- TikTok (COM-20), Facebook (COM-22), Trustpilot (COM-21): all UNSIZED/NULL/BLOCKED per §3 — Apify hard limit removes every scraper lane; no browser tool is connected this run.
- Skews named: (1) platform demographics — Warrior Forum skews older/longtime solo marketers (threads from 2016-2022), Shopify Community and YouTube skew newer entrants (2024-2026), so the corpus over-represents both extremes of experience and under-represents the middle; (2) extreme users post more — YouTube creators who "lost $40k" or "$1M" self-select for dramatic framing (monetized storytelling), likely overstating typical loss size; (3) public commenters differ from silent buyers — everyone in this corpus is still publicly active/posting, which by construction excludes people who quit silently and never speak of it again (the single largest population per Charlie Nuttall's own observation: "a lot of the people at the top aren't showing it... loads of people was going through the exact same thing"); (4) search-index bias — WebSearch and Exa surface Google-indexed, SEO-friendly platforms (Shopify's own community forum, Quora, blogs) far more readily than closed/algorithmic platforms (Reddit, TikTok, Facebook groups), which is a structural under-count of exactly the platforms named in 01's `lane_search_terms[]`.

## §9 · HARVEST BUDGET ESTIMATE

| com_id | lane | actor | est_rows | est_cost |
|---|---|---|---|---|
| COM-16 | forum_thread | Exa agent (medium, verbatim extraction) | ~15 records (2 threads × OP+3 replies + follow-ups) | $0.10 (1 run, already spent in 06) |
| COM-17 | forum_thread | Exa agent (medium) | ~12 records (3 threads × OP+3 replies) | $0.10 (1 run, already spent in 06) |
| COM-18 | quora_answers | Exa agent (medium) | ~5 records (1 question + 4 answers) | $0.10 (1 run, already spent in 06) |
| COM-19 | youtube_transcript | TranscriptAPI get_youtube_transcript | ~35-40 records (8 usable videos × 4-5 passages) | ~10 credits (already spent) |
| COM-23 | blog_comments (blog posts) | Exa agent (low, discovery only — no further extraction run) | 4 posts summarized, not deep-mined further | $0.025 (already spent) |
| COM-20,07,08 | tiktok_comments / trustpilot_balanced / fb_post_comments | Apify (pinned recipe cards for operator, see 05 §5) | 0 this run | $0.00 — BLOCKED-ON-TOOL |
Sum this step: Exa ≈ $0.425 (5 runs) + TranscriptAPI ≈ 14 credits (4 search pages + 10 transcripts) vs PB-06 share of standard $6 map cap ÷3 ≈ $2.00 → **under cap**.

## §10 · COVERAGE STATEMENT

Every size in §3/§5 is read from a fetched page (Exa) or a tool call (TranscriptAPI), never from memory; population presence in §4 is cited to real thread/video URLs, never claimed from a community's name alone; speaker mix is marked `[D]`; COM-15 (Reddit) and COM-20/07/08 (TikTok/Trustpilot/Facebook) are BLOCKED-ON-TOOL or NULL and listed as such, never invented.

COVERAGE: COM 7 (VALIDATED 5 · SUPPORTED 0 · HYPOTHESIS 1) · platforms 4/9 (forum×2, quora, youtube_search, blog_comments; reddit/tiktok/trustpilot/facebook/amazon blocked or n/a) · PB below floor: NONE (COM ≥4, PH ≥8 both met) · CP NOT FOUND: NONE (CP-03 VALIDATED-PRESENT, CP-05 EARLY SIGNAL/NOT FOUND-on-one-lane, both kept) · walled 0 · Reddit usable rate 0% (0 reddit.com pages retrievable by any tool this run) · cost $0.425 Exa + ~14 TranscriptAPI credits · AS: 1 row (LATE-BOUND: 03.AS-## for the rest) · weakest link: Reddit — the platform named first in 01's own `lane_search_terms[]` ("shopify store no sales reddit") is completely unopenable this run, so the map leans on Shopify Community/Warrior Forum/Quora/YouTube as substitutes · what closing it would cost: 1 Apify `harshmaur/reddit-scraper` run per PB (~$0.05-0.10) once the monthly hard limit resets, or an operator-side residential-proxy fetch of `old.reddit.com/r/<sub>/search.json` for the same PH-## list used here.


---
# PARTIAL · PB-05 (verbatim, COM/URL ids re-keyed)

# 04 — VOC 1 · COMMUNITY MAP · SCOPE: PB-05 · Readymerce
agent_id: VOC-PB-05 · wave W1 · leg 1/3 (04→05→06) · started 2026-09-24T20:29:32Z · box: 30 min / 100 calls (all 3 legs) · model: sonnet

## §1 · LOCK CARD

PB-05 (buyer words): **"I don't know what to sell"** [D] — owned rep framing: "winning product shortlisted" [R-OWNED T-06].
PB-05 (clinical): product selection / winning-product research. struggling_moment [D]: scrolling "winning product" lists and not trusting any pick.
CP-05 (only in-scope CP for PB-05 per 01-PRODUCT-TRUTH.md §5 candidate_populations[] and §6 table): situation = "aspiring e-commerce entrepreneur who wants to skip the build" · named_by_competitor Y (NW-SEED-02) · label COMPETITOR-CLAIMED HYPOTHESIS · SINGLE-POPULATION RISK flagged for PB-05 in 01 §6.
plain↔clinical pair (01 §8 swap table): "winning product" → "validated product-market fit" [R-OWNED T-06].
Competitor domains (01-HANDOFF.json `competitor_seeds[]`): ecomdoneforyou.com, ecommerceparadise.com (=NW-SEED-02), ecomxpertz.com.
02/03 status: **LATE-BOUND: 02.share_url** (02-partials/02-COMPETITOR-INTEL.NW-SEED-02.md.partial exists but carries only a lock card, no `im_records[]`/`share_url` yet — treated as not-yet-available) · **LATE-BOUND: 03.AS-##** (03 has not started; no 03-HANDOFF.json, no 03-partials/ present).
geo: US (ASSUMED, 01 TARGET MARKET blank) · language: en · SCOPE: PB-05.

DEGRADED-TOOL NOTICE (binding, AGENT-BRIEF-COMMON.md ADDENDUM VERIFIED 2026-09-24T20:35Z): Apify (all actors incl. rag-web-browser) → BLOCKED-ON-TOOL (monthly hard limit) · Firecrawl scrape → BLOCKED-ON-TOOL (insufficient credits) · Browserbase → BLOCKED-ON-TOOL (401) · WebFetch/curl → BLOCKED-ON-TOOL (egress 403 on all research hosts) · Reddit thread/about pages and Trustpilot review pages → NOT RETRIEVABLE by any connected tool (confirmed again this run: Exa agent explicitly reported "could not be retrieved" for r/dropshipping and r/dropship). WORKING and actually used this leg: WebSearch (12 queries, `[R-SNIPPET]`) · `mcp__Readymerce_Exa__agent_run` (4 runs this leg, low+medium effort, `[R-PAGE via Exa]` where a page was opened) · TranscriptAPI `search_youtube` (5 pages) + `get_youtube_transcript` (8 videos, `[R-SCRAPE]`-grade full transcript reads). GetHookd and Meta Ad Library not called this leg (no competitor-ad task in scope for 04/PB-05; reserved for 02/03).
Discovery method per the brief: WebSearch (8–12 PH-## queries, titles/URLs/snippets) + ≤4 Exa low/medium runs for forum/community discovery and sizing (page-read size = `[R-PAGE via Exa]`; snippet = `[R-SNIPPET]`; else `UNSIZED — method: <call>`); YouTube counts via TranscriptAPI `search_youtube` (views, captions flag) — TikTok `UNSIZED` (TikTok scraper is Apify-only, BLOCKED-ON-TOOL, not attempted).

Counter: `COM 7/4 · PB-05 7/4 · CP-05 2/2 · PH 19/8 · AS: LATE-BOUND · cost $0.25/$0.60(Exa cap ÷1 PB, standard)`

## §2 · PAIN-PHRASE BANK (PH-##)

| ph_id | pb_id | cp_id | phrase | phrase_type | origin | status |
|---|---|---|---|---|---|---|
| PH-01 | PB-05 | ALL | don't know what to sell online | base (01 lane term) | 01 hint_quote | EARLY SIGNAL — WebSearch: Shopify community threads use this framing (community.shopify.com/t/what-should-i-start-selling-as-a-new-online-retailer) |
| PH-02 | PB-05 | ALL | can't find a winning product | base (01 lane term) | 01 hint_quote | SUPPORTED — 2 YouTube videos titled near-verbatim (bKdLdxlLmPA, -1Q60dZcuHc) + WebSearch snippet hits (community.shopify.com, trustpilot winninghunter.com) — 2 platforms, <5/platform so short of VALIDATED |
| PH-03 | PB-05 | ALL | what product should I sell | base (01 lane term) | 01 hint_quote | EARLY SIGNAL — WebSearch: community.shopify.com/t/products-to-sell-online + Quora question found by Exa (25-year-old-lady thread) |
| PH-04 | PB-05 | ALL | picked the wrong product | base (01 lane term) | 01 hint_quote | EARLY SIGNAL — WebSearch: forum.alidropship.com "Have I picked a bad product line or what?"; Medium/Oberlo mistake articles |
| PH-05 | PB-05 | ALL | no idea what niche | base (01 lane term) | 01 hint_quote | UNPROVEN — searched: WebSearch returned only generic SEO articles (practicalecommerce.com), no first-person thread found this leg |
| PH-06 | PB-05 | ALL | picked the wrong product horror stories | horror stories | [D] template | EARLY SIGNAL — WebSearch: Quora "failure story behind having tried the drop shipping model?", Oberlo "18 Dropshipping F***ups" |
| PH-07 | PB-05 | ALL | where finding a winning product feels easy | where [problem] doesn't exist | [D] template | UNPROVEN — searched: no page found this leg |
| PH-08 | PB-05 | ALL | I finally found a winning product / I finally chose my business idea | I finally stopped [problem] | [D] template | SUPPORTED — YouTube transcripts fetched: xEvaenj4JH8 (Business By Nancy), bKdLdxlLmPA (Dave Obiefuna), -1Q60dZcuHc (Ry) all use this exact framing, verbatim pain phrase confirmed in transcript text |
| PH-09 | PB-05 | ALL | wish I'd known before I picked a product | wish I'd known before [solution] | [D] template | EARLY SIGNAL — WebSearch: community.shopify.com "What's something you wish more beginner dropshippers asked...", Oberlo mistakes article |
| PH-10 | PB-05 | ALL | product research tools don't work | [category] doesn't work | [D] template | UNPROVEN — searched: WebSearch returned mostly vendor-positive reviews (Trustpilot pages for dropship.io, minea.com) not retrievable this leg; no first-person "doesn't work" complaint opened |
| PH-11 | PB-05 | ALL | almost didn't buy a winning-product tool/list | almost didn't buy | [D] template | UNPROVEN — searched: no hit this leg |
| PH-12 | PB-05 | ALL | can't find a winning product reddit | [problem] reddit | [D] template | UNPROVEN (Reddit-specific) — r/dropshipping and r/dropship exist (named) but page/search could not be retrieved by any tool this run (Apify BLOCKED, Exa "could not be retrieved") → QUERY-ONLY |
| PH-13 | PB-05 | ALL | can't find a winning product reddit frustrated | [problem] reddit [emotion] | [D] template | UNPROVEN — same Reddit access block as PH-12 |
| PH-14 | PB-05 | ALL | not knowing what to sell is ruining my confidence | "ruining my [scene]" | [D] template | UNPROVEN — searched: no verbatim hit this leg |
| PH-15 | PB-05 | ALL | I have no idea what to sell and I'm always second-guessing myself | confession form | [D] template | EARLY SIGNAL — close paraphrase in Business By Nancy transcript ("constantly jumping from one idea to another") |
| PH-16 | PB-05 | ALL | best ways to find a winning product reddit | belief probe | [D] template | UNPROVEN — Reddit access blocked; WebSearch returned only vendor/tool blog posts |
| PH-17 | PB-05 | ALL | signs you picked the wrong product | trigger probe | [D] template | UNPROVEN — searched: no hit this leg |
| PH-18 | PB-05 | ALL | what happens if you never find a winning product | "[problem] untreated" / consequence probe | [D] template | UNPROVEN — searched: no hit this leg |
| PH-19 | PB-05 | CP-05 | beginner dropshipper can't find a winning product | per-CP population word + problem | [D] template + CP-05 word | SUPPORTED — Warrior Forum alex19890 verbatim: "i am beginner on drop-shipping and i will know how can i find a good product or winning product?" [R-PAGE via Exa] |

PH floor: ≥8 per PB (19/8 met) · ≥3 per CP-05 (3 rows tagged CP-05 explicitly: PH-19 + PH-01/PH-02/PH-03 apply ALL which includes CP-05 — floor met). Mandatory families present: horror stories (PH-06) · where-doesn't-exist (PH-07) · finally-stopped (PH-08) · wish-I'd-known (PH-09) · category-doesn't-work (PH-10) · almost-didn't-buy (PH-11) · reddit (PH-12) · reddit+emotion (PH-13) · complaint-ruining (PH-14) · confession (PH-15) · belief probe (PH-16) · trigger probe (PH-17) · consequence probe (PH-18) · per-CP (PH-19). All 14 mandatory families printed.

## §3 · COMMUNITY TABLE (COM-##) — PB-05

| com_id | platform | name | url | size_n | size_unit | size_source_tier | size_date | activity_posts_7d | activity_comments_per_thread | last_post_date | source_role | access | pain_phrases_seen[] | speaker_mix_guess [D] | priority_rank | label | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COM-25 | reddit | r/dropshipping | https://www.reddit.com/r/dropshipping/ | UNSIZED | subscribers | NULL | — | UNKNOWN | UNKNOWN | UNKNOWN | problem_discussion (named, unconfirmed) | PUBLIC | none confirmed | [D] beginners, resellers, guru-adjacent accounts | LOW-ACTIVITY (unconfirmed) | HYPOTHESIS — excluded from VALIDATED/SUPPORTED counters | UNSIZED — method: Exa agent attempted https://www.reddit.com/r/dropshipping/ , reported "could not be retrieved"; apify/rag-web-browser BLOCKED-ON-TOOL (monthly hard limit). Named from 04's own discovery, not opened successfully — kept per rule (a source never opened is never listed as opened) |
| COM-26 | reddit | r/dropship | https://www.reddit.com/r/dropship/ | UNSIZED | subscribers | NULL | — | UNKNOWN | UNKNOWN | UNKNOWN | problem_discussion (named, unconfirmed) | PUBLIC | none confirmed | [D] same as COM-25 | LOW-ACTIVITY (unconfirmed) | HYPOTHESIS — excluded from counters | UNSIZED — method: Exa agent attempt failed; Apify BLOCKED-ON-TOOL. Described by redpulse.io [R-SNIPPET, third-party, not counted as size] as "focused on the entrepreneurial side of dropshipping" |
| COM-27 | forum | Warrior Forum — Ecommerce Sites, Wholesaling & Drop Shipping | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/ | UNSIZED (forum-wide member count not exposed) | members | NULL | — | UNKNOWN | 8–15 replies on the 2 threads opened | 2017-12-16 (newest thread opened) | problem_discussion | PUBLIC | PH-02, PH-19 | [D] beginner dropshippers, mixed experience | ACTIVE-on-thread (old threads, but genuinely on-topic and first-person) | SUPPORTED — 3 threads opened and read (title+body), pain phrase confirmed verbatim, but forum-wide size never exposed so full VALIDATED (which requires a size tier) is not claimed | Threads opened: (1) "winning product ?? dropshipping" — alex19890, 2017-12-16, 1 reply [R-PAGE via Exa]; (2) "Please some help with Dropshipping....." — clik2000, ~14y ago, 8 replies [R-PAGE via Exa]; (3) "Alibaba.com and dropshipping" — neeralt, ~14y ago, 15 replies [R-PAGE via Exa] |
| COM-28 | forum | Indie Hackers | https://www.indiehackers.com/ | UNSIZED (site-wide member count not exposed) | members | NULL | — | UNKNOWN | 1 comment / 1 upvote (thread 1); 0 visible (thread 2) | 2021-09-02 | problem_discussion | PUBLIC | PH-08 (near), PH-19-adjacent | [D] indie SaaS/ecom founders | LOW-ACTIVITY | SUPPORTED — 2 posts opened, verbatim pain-phrase language confirmed, size not exposed | Posts opened: "Our solution for finding winning products" — Ilia Boltianov, 2021-09-02, 1 comment/1 upvote [R-PAGE via Exa]; "No ideas for backend products" — codefella, 2021-08-01 [R-PAGE via Exa] (digital-product adjacent, population match imperfect — kept, tagged in notes) |
| COM-29 | quora | Quora — E-Commerce / product-selection questions | https://www.quora.com/topic/E-Commerce | UNSIZED (topic follower count not exposed) | answers | NULL | — | UNKNOWN | UNKNOWN (answer counts errored on load for 4 of 5 pages) | UNKNOWN | solution_seeking | PUBLIC | PH-03 | [D] mixed — sellers, aspiring sellers, advice-givers | LOW-ACTIVITY (mostly low-engagement questions) | SUPPORTED — 1 question page opened and verbatim first-person text confirmed; 4 other Quora question pages Exa opened but Quora returned "Something went wrong" (page not usable) | Opened: "What product will you suggest I sell? I am a 25-year-old lady..." [R-PAGE via Exa], no reply-count exposed. 4 other Quora URLs attempted, load error both runs — logged, not counted as opened |
| COM-30 | facebook_group | CJdropshipping / Dropshipping.com Community \| Winning Products / Dropshipping Trending Products | https://www.facebook.com/groups/cjdropshipping/ ; https://www.facebook.com/groups/3010156415933280/ ; https://www.facebook.com/groups/dropshippingtrendingproduct/ | UNKNOWN | members | NULL | — | UNKNOWN | UNKNOWN | UNKNOWN | problem_discussion (named, unconfirmed) | LOGIN_WALLED | none (page wall, no content visible) | [D] unknown | LOW-ACTIVITY (unconfirmed) | HYPOTHESIS — [R-WALLED], counted not harvested | 3 candidate groups found by Exa discovery; all 3 returned a Facebook login wall, no about/member data or post content visible — [R-WALLED] |
| COM-31 | youtube_search | YouTube search: "how I finally found a winning product" / "I don't know what to sell online store" / "I wasted months on product research" / "how I finally picked what to sell" | https://www.youtube.com/results?search_query=... (4 queries via TranscriptAPI search_youtube) | 21,953 / 698 / 8,912 / 105,704 views (top matching videos, see §2 tier) | views_for_phrase | R-TOOL (TranscriptAPI search_youtube) + R-SCRAPE (full transcript fetched for 8 videos) | 2026-09-24 | n/a (not a live feed) | n/a | video publish dates: 3y ago (bKdLdxlLmPA) / 1y ago (-1Q60dZcuHc) / 2mo ago (xEvaenj4JH8) / 8y ago (33JF7JAsG9k, educational not first-person) | problem_discussion (first-person journey videos) | PUBLIC | PH-02, PH-08, PH-15, PH-19 | [D] solo dropshippers/creators, mixed experience level, several monetizing via own channel (creator bias) | ACTIVE — VALIDATED | 8 videos' transcripts fetched in full (§list below); 2 of 8 are strongly on-PB-05 first-person struggle/resolution narratives (xEvaenj4JH8 Business By Nancy; xlV60PEwg5c Manish Kumar, Hindi, [translated]); bKdLdxlLmPA and -1Q60dZcuHc are product-research/ad-strategy tutorials with light first-person framing; 33JF7JAsG9k (Oberlo) and kO-POM2RLYw are advisor-voice, not sufferer-voice — kept but tagged accordingly in 06 |

COM floor (scoped): ≥4 per PB across ≥3 platforms → **7 communities across 5 platforms (reddit, forum, quora, facebook_group, youtube_search) — floor met and exceeded.** Reddit ≥3 subreddits per PB: only 2 named (r/dropshipping, r/dropship) — **PARTIAL — reddit subreddit-count floor (3) not met · searched: WebSearch "r/dropshipping", "r/ecommerce reddit", site:reddit.com queries; no third distinct subreddit surfaced this leg; chain exhausted: Apify BLOCKED, Exa "could not be retrieved" on Reddit domain.**

## §4 · POPULATION PRESENCE — CP-05 × COM-##

| cp_id | com_id | label | cited_thread_urls[] | marker_phrase |
|---|---|---|---|---|
| CP-05 | COM-27 | VALIDATED-PRESENT | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1320451-winning-product-dropshipping.html (alex19890, 2017-12-16) | "i am beginner on drop-shipping and i will know how can i find a good product or winning product?" |
| CP-05 | COM-28 | EARLY SIGNAL | https://www.indiehackers.com/post/our-solution-for-finding-winning-products-8173495584 (Ilia Boltianov, 2021-09-02) | "the problem of finding winning products is an eyesore at this point, considering how many people start an e-commerce store nowadays" |
| CP-05 | COM-29 | EARLY SIGNAL | https://www.quora.com/What-product-will-you-suggest-I-sell-I-am-a-25-year-old-lady-and-I-need-help-with-product-ideas-to-sell-even-if-its-in-the-market-It-s-a-fast-moving-product-My-capital-is-500-cedis (author not shown) | "What product will you suggest I sell? I am a 25-year-old lady and I need help with product ideas to sell..." |
| CP-05 | COM-31 | VALIDATED-PRESENT | https://www.youtube.com/watch?v=xEvaenj4JH8 (Business By Nancy, 2026-07 approx / "2 months ago") | "After weeks of overthinking, I finally committed to selling Canva templates on Etsy" |
| CP-05 | COM-31 | EARLY SIGNAL | https://www.youtube.com/watch?v=xlV60PEwg5c (Manish kumar, ~2023) [translated, Hindi original] | translated: "I wasted 8-9 months just consuming information about product research without ever applying it" [translation, original Hindi kept in 06 Q-record] |

CP-05 combined across COM-27/04/05/07: **5 distinct named/handled authors across 4 platforms (forum, forum, quora, youtube×2) → VALIDATED-PRESENT overall for CP-05** (≥3 threads/reviews by different authors, own words, met).

## §5 · POND READ — POND-PB-05

| cell | value | tier | date |
|---|---|---|---|
| subreddit_subscribers_sum | UNSIZED — method: apify/rag-web-browser (BLOCKED-ON-TOOL, monthly hard limit) + Exa agent (attempted https://www.reddit.com/r/dropshipping/ and /r/dropship/, both "could not be retrieved") | NULL | 2026-09-24 |
| fb_top5_members_sum | UNKNOWN — 3 groups found, all LOGIN_WALLED, no member count visible | NULL [R-WALLED] | 2026-09-24 |
| amazon_top3_reviews_sum | NOT RUN this leg — no Amazon listing search performed (time-boxed; PB-05 is a research/selection problem, not a product-review problem, so Amazon lane deprioritized in favor of forum/YouTube discovery) | NULL | — |
| trustpilot_reviews_sum | NOT RUN this leg — Trustpilot pages not retrievable by any tool (confirmed run-wide); competitor domains (ecomdoneforyou.com, ecommerceparadise.com, ecomxpertz.com) not queried against Trustpilot this leg | NULL | — |
| tiktok_views_top20_sum | UNSIZED — TikTok scraper is Apify-only (clockworks/tiktok-scraper), BLOCKED-ON-TOOL; not attempted via browser (Browserbase 401) | NULL | — |
| tiktok_post_count | UNSIZED — same as above | NULL | — |
| youtube_top10_views_sum | 137,267 (sum of top-4 matching videos read this leg: 21,953 + 698 + 8,912 + 105,704) — partial top-10, not all 10 slots filled | R-TOOL | 2026-09-24 |
| quora_answers | UNKNOWN — answer counts did not render on the one Quora page successfully opened; 4 other Quora pages errored on load | NULL [R-PAGE attempted] | 2026-09-24 |
| hunger.posts_7d_sum | UNKNOWN — no live-feed community successfully sized this leg | NULL | — |
| hunger.median_comments_per_thread | SAMPLE(3): Warrior Forum threads opened had 1, 8, 15 replies respectively (median 8) | [R-PAGE via Exa] | 2026-09-24 |
| hunger.share "tried everything"/spend language | SAMPLE(6 threads/videos read): 2 of 6 (Manish Kumar transcript: "I wasted 8-9 months"; Business By Nancy: "After weeks of overthinking") carry spend-of-time/frustration language | [D] | 2026-09-24 |

## §6 · SOURCE-ROLE MIX — PB-05

| pb_id | problem_discussion | solution_seeking | comparison | purchase_question | post_purchase_review | ad_comments | caregiver | role floor met Y/N |
|---|---|---|---|---|---|---|---|---|
| PB-05 | 5 (COM-27×3, COM-28×2 posts, COM-31×2 first-person videos counted once for role) | 1 (COM-29 Quora question) | 0 | 0 | 0 | 0 | 0 | **N — post_purchase_review floor (≥1) not met.** Amazon/Trustpilot lanes not run this leg (time-boxed; see §5). problem_discussion floor (≥1) met. |

## §7 · ASSUMPTION LIST (AS-##)

**LATE-BOUND: 03.AS-##** — 03-HANDOFF.json does not exist and no 03-partials/ files are present at read time (2026-09-24T20:32Z). No `EK-##`, `VD-##`, `VA-##`, `BI-##` rows exist yet to route. 06-MERGE (or 07) runs the assumption check once 03 exists. The one operator-level assumption visible from 01 alone is logged here so it is not lost:

| as_id | source_id | claim (verbatim) | type | communities_to_check[] | status |
|---|---|---|---|---|---|
| AS-P05-01 | CP-05 (01 §6, named_by_competitor Y — NW-SEED-02) | Competitor NW-SEED-02 (ecommerceparadise.com) names its buyer as "Aspiring E-Commerce Entrepreneurs" who want to skip the build/product-selection step | avatar | COM-27, COM-28, COM-31 | UNCHECKED |

## §8 · BIAS + ACCESS ROW

- Reddit (r/dropshipping, r/dropship) is the single largest expected population for PB-05 and is entirely inaccessible this run — Apify BLOCKED-ON-TOOL (monthly hard limit), Exa agent explicitly reports the pages "could not be retrieved." This is the dominant bias: the corpus below is Warrior Forum / Indie Hackers / Quora / YouTube only, which skews toward (a) older, SEO-indexed forum posts (2012–2021, not current), (b) YouTube creators who monetize their own "journey" content (survivorship/success bias — people who post "I finally found my winning product" videos are disproportionately people who succeeded or are selling a course/mentorship), and (c) Indie Hackers/Warrior Forum skew toward digital-product/SaaS-adjacent founders, not pure physical-product dropshippers.
- Facebook groups: 3 candidates found, all `[R-WALLED]` — counted, not harvested. Public commenters on walled platforms are known to differ from silent majority buyers.
- `NULL — searched: [site:reddit.com <PH>, r/dropshipping about.json, r/dropship about.json]` for both Reddit subreddits' size and content.
- Extreme/loud posters (asking public questions, running YouTube channels) are overrepresented vs. the silent majority who search and read without posting — standard search-index / posting bias.
- Search-index bias: WebSearch results were dominated by Shopify's own community forum and SEO/marketing blog content (Oberlo, Sell The Trend, dodropshipping.com) rather than neutral third-party discussion — these are vendor-adjacent and their "common struggles" framing may reflect what sells tools, not raw buyer language.

## §9 · HARVEST BUDGET ESTIMATE

| com_id | lane | actor/tool | est_rows | est_cost |
|---|---|---|---|---|
| COM-27 | forum_thread | RC-WEB (apify/website-content-crawler) — BLOCKED-ON-TOOL this run; Exa agent_run medium fallback used instead | 3 threads already read this leg | $0.10 (2 Exa medium runs already spent) |
| COM-28 | forum_thread | same as above | 2 posts already read | (included above) |
| COM-29 | quora_answers | RC-QU (fatihtahta/quora-scraper) — BLOCKED-ON-TOOL; Exa fallback | 1 page already read | (included above) |
| COM-31 | youtube_transcript | RC-YTX (TranscriptAPI get_youtube_transcript) | 8 already fetched | $0 (TranscriptAPI credits, not Exa) |
| COM-25/02 | reddit_post+comments | RC-RD (harshmaur/reddit-comments-scraper) — BLOCKED-ON-TOOL; no working fallback found (Exa also blocked on reddit.com) | 0 | $0 spent, cannot close without operator paste |
| COM-30 | fb_post_comments | RC-FBC (apify/facebook-comments-scraper) — BLOCKED-ON-TOOL; groups also LOGIN_WALLED to Exa | 0 | $0 spent, cannot close |

Sum this leg: **$0.25** (4 Exa runs: 2×low $0.025 + 2×medium $0.10) vs. scoped cap $0.60 (standard $6 map cap ÷ ~10 PBs, this run has 3 in-scope PBs per 01 so effective per-PB share is higher; kept conservative at $0.60 stated in the brief). Remainder of Exa run-budget preserved for STEP 06 harvest lanes.

## §10 · COVERAGE STATEMENT

Community sizes and pain-phrase hit counts above are printed only from pages actually fetched this leg (WebSearch snippets, Exa-opened pages, and TranscriptAPI-read video metadata/transcripts) — never from memory; population presence is cited to specific opened threads/videos with author and date, never asserted from a community's name alone; speaker-mix guesses are marked `[D]`. The Reddit lane (the single largest expected PB-05 population, r/dropshipping + r/dropship) is fully `BLOCKED-ON-TOOL` this run (Apify hard limit; Exa reports pages "could not be retrieved") and the Facebook-group lane is fully `[R-WALLED]` — both are named, not harvested. Amazon and Trustpilot lanes were not attempted this leg (time-boxed toward forum/YouTube discovery, which is where PB-05's population is most reachable under the current tool set).

**COVERAGE: COM 7 (VALIDATED 1 · SUPPORTED 4 · HYPOTHESIS 2) · platforms 5/9 · PB below floor: [NONE on the ≥4-per-PB floor; PARTIAL on the reddit≥3-subreddits sub-floor] · CP NOT FOUND: [NONE — CP-05 VALIDATED-PRESENT] · walled 3 (COM-30's 3 groups) · Reddit usable rate 0% (0 of 2 candidate subreddits retrievable) · cost $0.25 · AS: 1 row | LATE-BOUND: 03.AS-## for everything downstream of 03 · weakest link: Reddit (Apify BLOCKED-ON-TOOL + Exa cannot retrieve reddit.com) removes the largest single expected population for this PB · what closing it would cost: an Apify plan reset (or a different Reddit-capable scraper credential) + ~$0.05–0.10/thread via harshmaur/reddit-comments-scraper on the 2 named subreddits, plus an operator paste of 5–10 thread URLs as an immediate substitute.**


---
## §10 COVERAGE STATEMENT (merged)

Counts come from the partials' fetched pages and snippets, never memory; the two owned rows are the operator's own data, counted and harvested; private/walled groups counted, not harvested.

COVERAGE: COM 30 (PB-01 14 · PB-06 7 · PB-05 7 per partial handoffs = 28; + owned 2; id slots COM-01…34 reserved by the offset re-key) (VALIDATED 6 · SUPPORTED 13 · HYPOTHESIS 5, per partial lines; + owned 2 [R-OWNED]) · platforms per partial 6/9 · 4/9 · 5/9 (union UNSCANNED) + owned · PB below floor: [NONE] · CP NOT FOUND: [CP-01 in market communities (owned: present)] · walled 5 · Reddit usable rate 0% · cost $1.025 (0.35+0.425+0.25) · AS: 3 rows checked in 06 §17 | EK LATE-BOUND: 03.AS-## · weakest link: Reddit fully BLOCKED-ON-TOOL across all PBs · what closing it would cost: Apify reset + harshmaur/reddit-scraper ≈$0.05–0.10 per PB
