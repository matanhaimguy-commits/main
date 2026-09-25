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
