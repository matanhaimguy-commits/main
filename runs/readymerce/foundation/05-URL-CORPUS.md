# 05 — URL CORPUS (merged) · Readymerce · written by 06-MERGE

## §0 MERGE CARD

Concatenation of 05-partials PB-01, PB-06, PB-05 (plan order). URL ids are PB-scoped (`PB-01/URL-02`) because every partial numbers from URL-01; COM ids re-keyed as in 04-COMMUNITY-MAP.md §0. Every BLOCKED lane and OPERATOR-PASTE row is kept verbatim inside the partial blocks. Added: extra units mined in 06 but not listed in 05 (rule: add to 05 first — added retroactively here), and the two owned units.

## §2-ADD · URLs added by 06 harvesters + owned units

| url_id | pb_id | lane | url | records | note |
|---|---|---|---|---|---|
| PB-01/URL-21b | PB-01 | youtube_transcript | https://www.youtube.com/watch?v=JS2lX1FFAVs | 1 | extra source (06 floor loop / population-first) |
| PB-01/URL-26 | PB-01 | forum_thread | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1286522-several-drop-shipping-questions.html | 4 | extra source (06 floor loop / population-first) |
| PB-01/URL-6MKO7iAtiAE | PB-01 | youtube_transcript | https://www.youtube.com/watch?v=6MKO7iAtiAE | 2 | extra source (06 floor loop / population-first) |
| PB-01/URL-pzR | PB-01 | youtube_transcript | https://www.youtube.com/watch?v=pzR_ETZXAzI | 3 | extra source (06 floor loop / population-first) |
| PB-01/URL-sSShxoEBFkY | PB-01 | youtube_transcript | https://www.youtube.com/watch?v=sSShxoEBFkY | 2 | extra source (06 floor loop / population-first) |
| PB-01/URL-uCubamN3o4o | PB-01 | youtube_transcript | https://www.youtube.com/watch?v=uCubamN3o4o | 2 | extra source (06 floor loop / population-first) |
| OWNED-US | PB-01…PB-07 | owned_paste | inputs/transcripts/ (US files, 155) | 109 | RC-OWNED · HV VOC-OWNED-US · 46/155 read |
| OWNED-UK | PB-01…PB-07 | owned_paste | inputs/transcripts/ (UK/IE files, 122+) | 72 | RC-OWNED · HV VOC-OWNED-UK · 40 diarized read; 80 BLOCKED-FORMAT |

**RC-OWNED** (owned_paste) · python parse of speaker turns (formats A `Name HH:MM:SS`, B `[Speaker N] (m:ss - m:ss)`) · prospect turns → Q-O, rep pitch → C (cap 40) · $0.


---
# PARTIAL · PB-01 (verbatim, ids re-keyed)

# 05 — VOC 2 · URL CORPUS + HARVEST PLAN · SCOPE: PB-01 · Readymerce

agent_id: VOC-PB-01 · leg 2 of 3 · started 2026-09-24T20:34:57Z. Reads 04-partials/04-COMMUNITY-MAP.PB-01.md + 04-HANDOFF.PB-01.json (this session, same agent) · 01-HANDOFF.json + 01-PRODUCT-TRUTH.md §5-§8. LATE-BOUND: 02.share_url (02-HANDOFF.json absent) — ad-comment lane has no competitor share_url seeds; NW-SEED-## domains used for the Trustpilot/review lane instead. ASSUMED: N_PB=3 (the 3 SUPPORTED problem_lanes in 01 §7: PB-01, PB-06, PB-05) and N_CP=7 (01 §6 total CP rows) for computing the global-share floors below, since the true concurrent-agent count is not visible to this scoped leg.
DEGRADED-TOOL NOTICE (binding, unchanged from 04): Apify BLOCKED-ON-TOOL (all actors — $0 spendable) · Firecrawl scrape BLOCKED-ON-TOOL · Browserbase BLOCKED-ON-TOOL · WebFetch/curl BLOCKED-ON-TOOL (egress 403) · Reddit and Trustpilot pages NOT RETRIEVABLE by any tool. WORKING: WebSearch, TranscriptAPI (search_youtube, get_youtube_transcript), Exa agent (agent_run). Recipe cards RC-## below are pinned Apify inputs printed for the operator to run later (never executed this run); RC-YTX (TranscriptAPI) and RC-EXA (Exa verbatim extraction) are the cards that actually run in 06.

## §1 FLOOR TABLE

| floor_name | scope | floor | target | basis |
|---|---|---|---|---|
| records_total | total (workflow) | max(200, 3×40, 7×25+15)=200 | 400 | STEP05 §5 Step0 formula, N_PB=3 ASSUMED, N_CP=7 |
| records | PB-01 | 40 | 80 | per-PB floor (STEP05 §5 Step0), scoped brief |
| records | CP-01 | 25 (≥5 at [R-PAGE]/[R-SCRAPE]) | 50 | per-CP floor |
| records | CP-05 | 25 (≥5 at [R-PAGE]/[R-SCRAPE]) | 50 | per-CP floor |
| source_type reddit | PB-01 share | ceil(80÷3)=27 | 54 | global 80 ÷ N_PB=3 |
| source_type reviews | PB-01 share | ceil(60÷3)=20 (≥3 from 3★ — N/A, no Amazon lane) | 40 | global 60 ÷ 3 |
| source_type video_comments | PB-01 share | ceil(30÷3)=10 | 20 | global 30 ÷ 3 |
| source_type fb+forum+quora | PB-01 share | ceil(20÷3)=7 | 14 | global 20 ÷ 3 |
| source_type ad_comments | PB-01 share | ceil(10÷3)=4 (when available — none this leg, LATE-BOUND: 02.share_url) | 8 | global 10 ÷ 3 |
| source types | PB-01 | ≥4 distinct types present | — | STEP05 §4.1 floor |
| URL total | PB-01 | ≥12 across ≥3 platforms | — | scoped §1 SCOPE clause |
| URL reddit | PB-01 | ≥5 | — | scoped share of global ≥20 |
| URL per CP | CP-01, CP-05 | ≥4 each | — | §4.1 floor |
| tag pain | PB-01 share | ceil(20÷3)=7 | 14 | |
| tag scene | PB-01 share | ceil(15÷3)=5 | 10 | |
| tag failed_solution | PB-01 share | ceil(20÷3)=7 | 14 | |
| tag objection | PB-01 share | ceil(20÷3)=7 | 14 | |
| tag desire | PB-01 share | ceil(15÷3)=5 | 10 | |
| tag trigger | PB-01 share | ceil(15÷3)=5 | 10 | |
| tag belief | PB-01 share | ceil(15÷3)=5 | 10 | |
| tag symptom | PB-01 share | ceil(10÷3)=4 | 8 | |
| tag skepticism | PB-01 share | ceil(10÷3)=4 | 8 | |
| tag spend | PB-01 share | ceil(5÷3)=2 | 4 | |
| tag deeper_hope | PB-01 share | ceil(5÷3)=2 | 4 | |
| tag tired_of_hearing | PB-01 share | ceil(5÷3)=2 | 4 | |
| tag horror_story | PB-01 share | ceil(3÷3)=1 | 2 | |
| tag curiosity | PB-01 share | ceil(3÷3)=1 | 2 | |
| tag corruption | PB-01 share | ceil(3÷3)=1 | 2 | |

## §2 URL TABLE (URL-##) — PB-01, grouped by lane

| url_id | com_id | pb_ids | population_tags | platform | url | title | op_author | date_posted | engagement_primary | engagement_secondary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected | duplicate_of | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-01/URL-01 | COM-14 | PB-01 | — | forum | https://community.shopify.com/t/shopify-by-adrian-morrison/215810 | Shopify by Adrian Morrison (free DFY store, scam complaints) | UNKNOWN | UNKNOWN (page 2 exists) | ~20+ (est. from page count) | — | top | 1 | PH-06,PH-11 | forum_thread | 8 | RC-WEB | LISTED | [R-PAGE] | — | Strongest single on-topic thread found; title+URL seen via WebSearch, not yet opened for text. |
| PB-01/URL-02 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/is-there-a-simple-way-to-understand-shopify/192077 | Is there a simple way to understand Shopify? | UNKNOWN | UNKNOWN | ~23 (reply /23 seen) | — | top | 2 | PH-01,PH-03 | forum_thread | 8 | RC-WEB | LISTED | [R-PAGE] | — | Multiple reply-numbered URLs (/15,/20,/23) seen in search results. |
| PB-01/URL-03 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/shopify-seems-pretty-complicated/568388 | Shopify seems pretty complicated | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 3 | PH-03 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | |
| PB-01/URL-04 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/shopify-is-very-confusing-and-very-hard-to-setup/350760 | shopify is very confusing and very hard to setup | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 4 | PH-03 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | |
| PB-01/URL-05 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/building-your-shopify-store-what-is-the-biggest-problem-you-encountered/133383 | BUILDING YOUR SHOPIFY STORE? Biggest problem encountered? | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 5 | PH-09 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | Direct problem-elicitation thread. |
| PB-01/URL-06 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/what-s-one-thing-you-wish-you-knew-before-launching-your-first-shopify-store/578902 | One thing you wish you knew before launching first Shopify store | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 6 | PH-09 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | |
| PB-01/URL-07 | COM-01 | PB-01 | CP-01 | forum | https://community.shopify.com/t/is-anyone-else-struggling-with-adrian-morrisons-free-store-build/310831 | Is anyone else struggling with Adrian Morrison's free store build | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 7 | PH-05,PH-11 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | "misleading expectations — believed someone would build a complete store for them" — directly names PB-01's exact struggle. |
| PB-01/URL-08 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/i-received-proposal-from-someone-to-make-shopify-for-me/287432 | I received proposal from someone to make Shopify for me | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 8 | PH-06 | forum_thread | 5 | RC-WEB | LISTED | [R-PAGE] | — | |
| PB-01/URL-09 | COM-01 | PB-01 | CP-01 | forum | https://community.shopify.com/t/can-i-hire-a-trusted-professional-to-build-my-new-store/128838 | Can I hire a trusted professional to build my new store? | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 9 | PH-06 | forum_thread | 5 | RC-WEB | LISTED | [R-PAGE] | — | |
| PB-01/URL-10 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/shopifys-website-builder-is-garbage-and-our-business-is-suffering-almost-wish-i-never-switched/161168 | Shopify's website builder is garbage and our business is suffering | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 10 | PH-04,PH-07 | forum_thread | 5 | RC-WEB | LISTED | [R-PAGE] | — | |
| PB-01/URL-11 | COM-02 | PB-01 | — | forum | https://community.shopify.dev/t/where-to-start-super-overwhelmed-first-time-using-shopify/7804 | Where to start?! Super overwhelmed. First time using Shopify | UNKNOWN | 2025-02-08 | 4 comments | — | top | 11 | PH-01,PH-03 | forum_thread | 4 | RC-WEB | LISTED (Exa-opened) | [R-PAGE via Exa] | — | Exa opened and quoted this thread directly. |
| PB-01/URL-12 | COM-03 | PB-01 | — | forum | https://community.etsy.com/t5/Technical-Issues/Stuck-on-How-you-ll-get-paid-step-when-opening-a-new-shop/td-p/146362398 | Stuck on "How you'll get paid" step when opening a new shop | UNKNOWN | 2024-08-20 | UNKNOWN (replies gated) | — | top | 12 | PH-02 | forum_thread | 2 | RC-WEB | LISTED (partial, Exa-opened) | [R-PAGE via Exa] | — | Replies behind login wall — OP text only. |
| PB-01/URL-13 | COM-04 | PB-01 | — | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1510729-guidance-needed-etsy-ebay-account-setup.html | Guidance Needed for Etsy & eBay Account Setup | UNKNOWN | 2025-09-05 | 4 replies | — | top | 13 | PH-02 | forum_thread | 3 | RC-WEB | LISTED (Exa-opened) | [R-PAGE via Exa] | — | |
| PB-01/URL-14 | COM-05 | PB-01 | — | facebook_group | https://www.facebook.com/groups/282038432287765/posts/296994287458846/ | "Okay so before I freak out or get angry..." | UNKNOWN | UNKNOWN (2026) | UNKNOWN | — | top | 14 | PH-01 | fb_post_comments | 5 | RC-FBC | LISTED (Exa-opened) | [R-PAGE via Exa] | — | 22K-member group; only this 1 post opened. |
| PB-01/URL-15 | COM-09 | PB-01 | CP-05 | trustpilot | https://www.trustpilot.com/review/ecomxpertz.com | Ecomxpertz Reviews | UNKNOWN | UNKNOWN | UNSIZED (count not shown) | — | recent | 15 | PH-06,PH-23 | trustpilot_balanced | 10 | RC-TP | LISTED (snippet only — page BLOCKED-ON-TOOL to open) | [R-SNIPPET] | — | Snippet already carries 2 verbatim fragments (1 positive, 1 negative $4,000-complaint) — usable as [R-SNIPPET] pending page access. |
| PB-01/URL-16 | COM-11 | PB-01 | CP-05 | trustpilot | https://www.trustpilot.com/review/nn-dfysuccess.com | DONE FOR YOU® Reviews | UNKNOWN | UNKNOWN | 3 reviews | — | recent | 16 | PH-06,PH-21 | trustpilot_balanced | 3 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | "$69 and $169 paid, limited support, no sales in a month" fragment on record. |
| PB-01/URL-17 | COM-07 | PB-01 | — | trustpilot | https://www.trustpilot.com/review/ecomdoneforyou.com | Ecom Done For you Reviews | UNKNOWN | UNKNOWN | 10 reviews | — | recent | 17 | PH-06 | trustpilot_balanced | 4 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | NW-SEED-01. |
| PB-01/URL-18 | COM-08 | PB-01 | — | trustpilot | https://www.trustpilot.com/review/ecommerceparadise.com | Ecommerce Paradise Reviews | UNKNOWN | UNKNOWN | 22 reviews | — | recent | 18 | PH-06 | trustpilot_balanced | 9 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | NW-SEED-02. |
| PB-01/URL-19 | COM-10 | PB-01 | — | trustpilot | https://www.trustpilot.com/review/doneforyoustrategy.com | Done For You LLC Reviews | UNKNOWN | UNKNOWN | 8 reviews | — | recent | 19 | PH-06 | trustpilot_balanced | 3 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | RESERVE seed. |
| PB-01/URL-20 | COM-12 | PB-01 | — | youtube_search | https://www.youtube.com/watch?v=6MKO7iAtiAE | I PAID FIVERR EXPERTS To Run My WHOLE Dropshipping Business In 2023 | THE ECOM KING | ~3yr ago | 366132 views | UNKNOWN comments | most_liked | 20 | PH-06 | youtube_transcript | 3 | RC-YTX | LISTED | [R-TOOL] | — | Genuinely first-person "paid someone" DFY narrative; caption availability UNKNOWN — to confirm in 06. |
| PB-01/URL-21 | COM-12 | PB-01 | — | youtube_search | https://www.youtube.com/watch?v=rhuYy9LP72M | I Tried Shopify Dropshipping For 7 Days (Realistic Results) | Mark Tilbury | 4mo ago | 3954792 views | hasCaptions:true | most_liked | 21 | PH-06,PH-01 | youtube_transcript | 3 | RC-YTX | LISTED | [R-TOOL] | — | Captions confirmed available. |
| PB-01/URL-22 | COM-13 | PB-01 | — | blog_comments | https://painonsocial.com/blog/shopify-problems-reddit | 7 Most Common Shopify Problems Found on Reddit | UNKNOWN | UNKNOWN | UNKNOWN | — | — | 22 | PH-15 | blog_comments | 6 | RC-EXA | LISTED (snippet; queued for Exa medium open in 06) | [R-SNIPPET] → [R-PAGE via Exa] pending | — | Aggregates Reddit language in an openable (non-Reddit) page — priority Exa target for 06. |
| PB-01/URL-23 | — | PB-01 | CP-05 | blog_comments | https://kingy.ai/news/buildyourstore-ai-review-2026-is-this-free-ai-shopify-store-builder-worth-your-time/ | BuildYourStore.ai Review (2026) | UNKNOWN | 2026 | UNKNOWN | — | — | 23 | PH-10,PH-21,PH-22 | blog_comments | 4 | RC-EXA | LISTED (snippet) | [R-SNIPPET] | — | Names CP-05 directly ("aspiring entrepreneurs...intimidated by the technical lift"). |
| PB-01/URL-24 | — | PB-01 | — | forum | (reddit — no URL surfaced) | site:reddit.com shopify overwhelmed can't figure out | — | — | — | — | — | 24 | PH-01 | reddit_post+comments | 0 | RC-RD | QUERY-ONLY → BLOCKED | — | — | 0 of 22 WebSearch queries this leg surfaced an actual reddit.com URL (community.shopify.com dominates results); Reddit not retrievable by any tool. OPERATOR-PASTE row: operator should paste r/shopify or r/ecommerce thread URLs matching "can't figure out shopify" / "shopify setup overwhelming" if available. |
| PB-01/URL-25 | — | PB-01 | — | forum | (reddit — no URL surfaced) | site:reddit.com "paid someone" build shopify store for me | — | — | — | — | — | 25 | PH-06 | reddit_post+comments | 0 | RC-RD | QUERY-ONLY → BLOCKED | — | — | Same as PB-01/URL-24. OPERATOR-PASTE row: operator should paste any r/shopify/r/dropshipping thread on paying someone to build a store. |

Counter: URL 23/12 LISTED (scoped floor met; 2 additional BLOCKED/OPERATOR-PASTE rows for Reddit) · reddit_threads 0/5 (BLOCKED-ON-TOOL, PARTIAL) · lanes 6 (forum_thread, fb_post_comments, trustpilot_balanced, youtube_transcript, blog_comments, reddit_post+comments[BLOCKED]) · Σest PB-01 ≈ 116/(1.5×40=60) — PLAN-VALIDATED by raw count, but 9 of 23 rows are [R-SNIPPET]-only (not yet opened) so true realizable est is lower · Σest CP-01 ≈ 11/(1.5×25=37.5) — PLAN-THIN · Σest CP-05 ≈ 26/(1.5×25=37.5) — PLAN-THIN (close) · plan cost $0.05 spent / map cap.

## §3 EXCLUSIONS (EX-##)

| ex_id | url | reason | pb_id |
|---|---|---|---|
| EX-01 | https://community.shopify.com/t/customer-profile-unsubscribe-and-delete-account/20578/3 | off-topic (account deletion, not build-struggle) | PB-01 |
| EX-02 | https://community.shopify.com/t/i-need-help-urgently-i-need-to-contact-shopify/272004 | off-topic (support-contact request, no build-struggle content) | PB-01 |
| EX-03 | https://community.shopify.com/t/checkout-button-on-cart-page-is-not-working/36408/21 | off-topic (post-launch bug, not setup struggle) | PB-01 |
| EX-04 | Shopify app-store review pages (apps.shopify.com/reviews/*) surfaced repeatedly | off-topic (app reviews, not store-build reviews) | PB-01 |
| EX-05 | Gumroad course/product listing pages (multiple, e.g. tonyfiston.gumroad.com) | promotional | PB-01 |
| EX-06 | Fiverr gig listing pages (block.fiverr.com/gigs/*) | promotional | PB-01 |
| EX-07 | Wikipedia pages (Shopify, Wish company, Website builder) surfaced by broad queries | off-topic | PB-01 |
| EX-08 | Multiple community.shopify.com store-deactivation/termination threads | off-topic (platform enforcement, not build-struggle) | PB-01 |

## §4 LANE MIX per PB-01

| pb_id | forum_thread | fb_post_comments | trustpilot_balanced | youtube_transcript | blog_comments | reddit_post+comments | dominant platform share | SINGLE-PLATFORM flag |
|---|---|---|---|---|---|---|---|---|
| PB-01 | 13 | 1 | 5 | 2 | 2 | 0 (BLOCKED) | forum_thread 13/23 = 57% | SINGLE-PLATFORM: PB-01 (forum exceeds 50% — driven by Reddit being fully BLOCKED-ON-TOOL, forcing over-reliance on Shopify's own community forum) |

## §5 RECIPE CARDS (RC-##)

**RC-WEB** (forum_thread; would-be, Apify BLOCKED-ON-TOOL — printed for operator) · `apify/website-content-crawler` · input: `{"startUrls":[{"url":"<thread>"}, ...PB-01/URL-01..PB-01/URL-13...], "crawlerType":"cheerio","maxCrawlDepth":0,"maxCrawlPages":30,"htmlTransformer":"readableTextIfPossible","removeElementsCssSelector":"nav, footer, script, style, noscript, svg, [role=\"dialog\"]","saveMarkdown":true,"proxyConfiguration":{"useApifyProxy":true}}` · expected_rows: ~13 pages · unit_price: compute-only ≈$0.001-0.003/page · est_cost: $0.03 · output_field_map: text→markdown body, author→UNKNOWN (not exposed by this crawler), date→UNKNOWN, score→UNKNOWN, url→loadedUrl, parent_title→pageTitle · fallback_chain: [`apify/rag-web-browser` raw-http → this run's actual substitute: `mcp__Readymerce_Exa__agent_run` effort medium on the same URL] · no_apify_path: Exa agent_run (WORKING, used in 06).

**RC-FBC** (fb_post_comments; would-be) · `apify/facebook-comments-scraper` · input: `{"startUrls":[{"url":"https://www.facebook.com/groups/282038432287765/posts/296994287458846/"}],"resultsLimit":40,"includeNestedComments":false,"viewOption":"RANKED_UNFILTERED"}` · expected_rows: ≤40 · unit_price: $0.002/comment · est_cost: $0.08 · output_field_map: text→text, author→author.name, date→date, score→likesCount, url→commentUrl, parent_title→postText · fallback_chain: [`memo23/facebook-comments-scraper` → `dz_omar/facebook-comment-scraper` → Exa agent_run on the post URL] · no_apify_path: Exa agent_run.

**RC-TP** (trustpilot_balanced; would-be) · `memo23/trustpilot-scraper-ppe` · input: `{"startUrls":["ecomdoneforyou.com","ecommerceparadise.com","ecomxpertz.com","doneforyoustrategy.com","nn-dfysuccess.com"],"maxItems":100,"filterLanguages":["en"],"filterStars":[],"sampling":"balanced","sortBy":"recent","filterDateRange":"last12months","expandRegionalDomains":false,"scrapeAllReviews":false,"includeStats":true,"reviewInsights":true,"splitDatasets":false,"flattenCompanyData":true}` · expected_rows: ~29 (10+22+UNSIZED+8+3, capped) · unit_price: $0.00065/review + $0.02 insights · est_cost: $0.12 · output_field_map: text→text, author→consumer.displayName, date→dates.publishedDate, score→rating, url→reviewUrl, parent_title→companyName · fallback_chain: [`automation-lab/trustpilot` → page fetch `https://www.trustpilot.com/review/<domain>` → Exa agent_run] · no_apify_path: Exa agent_run (page not retrievable by Exa either per ADDENDUM — falls through to OPERATOR-PASTE).

**RC-YTX** (youtube_transcript; **WORKING, runs in 06**) · `mcp__TranscriptAPI__get_youtube_transcript` · input per video: `{"video_url":"<url>","format":"text","include_timestamp":true,"send_metadata":true}` · expected_rows: 1 transcript/video, coded into multiple Q-Y records · cost: TranscriptAPI credits (≤45 leg budget) · output_field_map: text→transcript segments, author→channelTitle (from search_youtube), date→publishedTimeText, url→video_url · fallback_chain: [`mcp__TranscriptAPI__get_youtube_video_info` to check caption languages first → skip if no captions] · no_apify_path: n/a, native tool.

**RC-EXA** (forum_thread/blog_comments/quora_answers verbatim extraction; **WORKING, runs in 06**) · `mcp__Readymerce_Exa__agent_run` · effort: medium · query template: "Open <URL> (or: search for and open the most relevant page(s) for <PH-##> on <domain/platform>) and return VERBATIM passages only — each with the exact page URL you opened, the author/handle as shown, and the date as shown. Do not paraphrase, do not merge separate comments, say explicitly if a page could not be retrieved. Use outputSchema: {passages:[{quote, author, date, url, platform}]}." · expected_rows: 3-8 passages/run · unit_price: ≈$0.03-0.10/run (effort-dependent) · est_cost: budgeted inside the $2.60 leg-wide Exa cap · fallback_chain: [effort low retry → mark BLOCKED with OPERATOR-PASTE row] · no_apify_path: n/a, native tool.

**RC-RD** (reddit_post+comments; would-be, and this run's actual status = BLOCKED-ON-TOOL, no fallback reached) · `harshmaur/reddit-comments-scraper` · input: `{"postUrls":[],"maxCommentsPerPost":40,"includeNSFW":false,"aiAnalysis":false}` · status this leg: no Reddit URL was ever surfaced by WebSearch or Exa to populate `postUrls[]` · fallback_chain: [`clearpath/reddit-post-comments-bulk-scraper` → `old.reddit.com/<post>/.json` via rag-web-browser (Apify BLOCKED) → browser (Browserbase BLOCKED, 401) → OPERATOR-PASTE] — all links in the chain BLOCKED-ON-TOOL this run; the PB-01/URL-24/PB-01/URL-25 OPERATOR-PASTE rows in §2 are the result.

## §6 HARVESTER ASSIGNMENTS

**HV-PB-01** (this agent, VOC-PB-01) · pb_id: PB-01 · cp_ids: [CP-01, CP-05] (CP-01 as an `HV-CP-01` task inside this harvester — its URL coverage is thin, see §2 rank 7 and 9 only) · url_ids (rank order): PB-01/URL-01, PB-01/URL-02, PB-01/URL-03, PB-01/URL-04, PB-01/URL-05, PB-01/URL-06, PB-01/URL-07, PB-01/URL-08, PB-01/URL-09, PB-01/URL-10, PB-01/URL-11, PB-01/URL-12, PB-01/URL-13, PB-01/URL-14, PB-01/URL-15, PB-01/URL-16, PB-01/URL-17, PB-01/URL-18, PB-01/URL-19, PB-01/URL-20, PB-01/URL-21, PB-01/URL-22, PB-01/URL-23 (PB-01/URL-24, PB-01/URL-25 BLOCKED, not mined) · recipe_ids: [RC-WEB(printed only), RC-FBC(printed only), RC-TP(printed only), RC-YTX(RUNS), RC-EXA(RUNS), RC-RD(BLOCKED)] · floors: per §1 · partial_file: `06-partials/06-VOC_MASTER.PB-01.csv` · max_extra_sources: 8.

**HV-CP-01** (task inside HV-PB-01, CP-01 thin — 0 VALIDATED-PRESENT communities from 04) · url_ids: PB-01/URL-07, PB-01/URL-09 (the only rows tagged CP-01) · task: Step 3(a) population-first pass in 06 — additional WebSearch/Exa queries on "<CP-01 situation word> <PB-01 plain word>" before declaring PARTIAL.

## §7 FALLBACK CHAINS per lane

| lane | chain | trigger |
|---|---|---|
| forum_thread | RC-WEB (Apify, BLOCKED) → rag-web-browser (Apify, BLOCKED) → RC-EXA (Exa agent, WORKING) → OPERATOR-PASTE | Apify call fails / monthly-limit error |
| fb_post_comments | RC-FBC (Apify, BLOCKED) → memo23/facebook-comments-scraper (BLOCKED) → RC-EXA on post URL (WORKING) → OPERATOR-PASTE | same |
| trustpilot_balanced | RC-TP (Apify, BLOCKED) → automation-lab/trustpilot (BLOCKED) → page fetch (WebFetch, BLOCKED — egress 403) → RC-EXA (Exa reports Trustpilot "could not be retrieved" per ADDENDUM — do not retry >once) → OPERATOR-PASTE | same, then Exa's own retrieval failure |
| youtube_transcript | RC-YTX (TranscriptAPI, WORKING) → `get_youtube_video_info` caption check → codepoetry/youtube-transcript-ai-scraper (Apify, BLOCKED) → skip, mark UNSIZED | no captions available |
| blog_comments / quora_answers | RC-EXA (Exa agent, WORKING) → OPERATOR-PASTE | Exa reports page not retrievable |
| reddit_post+comments | RC-RD (Apify, BLOCKED) → clearpath bulk scraper (BLOCKED) → old.reddit .json via rag-web-browser (BLOCKED) → browser (Browserbase, BLOCKED 401) → OPERATOR-PASTE naming the exact URL | Apify call fails; this run: no Reddit URL ever surfaced, chain exhausted at query stage |

## §8 COUNTER FORMAT

`records n/40 · PB-01 n/40 · CP-01 n/25 · CP-05 n/25 · sources n/23 (SCRAPED 0 · FETCHED n · 0-yield n · BLOCKED n · PASTE n) · types n/4 · pain n/7 · scene n/5 · failed_solution n/7 · objection n/7 · desire n/5 · trigger n/5 · belief n/5 · symptom n/4 · skepticism n/4 · spend n/2 · deeper_hope n/2 · tired_of_hearing n/2 · horror_story n/1 · curiosity n/1 · corruption n/1 · 3★ n/NA · cost $x.xx`

## §9 SOURCE MANIFEST (pre-filled)

| unit_id | lane | community/listing | date_range | expected_record_count | fields_available | access_limits | excluded_reason |
|---|---|---|---|---|---|---|---|
| SM-01..13 | forum_thread | community.shopify.com / community.shopify.dev / community.etsy.com / warriorforum.com threads (PB-01/URL-01..13) | mixed 2024-2026 | ~4-8 each | title, OP text, some reply counts; author/date mostly UNKNOWN pre-open | 1 partial login wall (Etsy) | — |
| SM-14 | fb_post_comments | Shopify/Dropshipping Warriors FB group post | 2026 | ~5 | text, comments (unopened) | group itself PUBLIC, only 1 post opened | 4 of target 5 groups not found/walled |
| SM-15..19 | trustpilot_balanced | 5 competitor/reserve Trustpilot pages | last 12mo (assumed) | ~3-10 each from snippet | review counts + 2-3 verbatim fragments only | page BLOCKED-ON-TOOL to open in full | — |
| SM-20..21 | youtube_transcript | 2 YouTube videos (PB-01/URL-20,21) | 2023, 2026 | 1 transcript each → several Q-Y records | full transcript if captioned | 1 of 2 caption status UNKNOWN pre-check | — |
| SM-22..23 | blog_comments | painonsocial.com, kingy.ai | UNKNOWN | ~5-6 each | full page text via Exa | none known | — |
| SM-24..25 | reddit_post+comments | (no URL surfaced) | — | 0 | none | Reddit fully unretrievable | BLOCKED-ON-TOOL, 0 URLs found |

## §10 COST SHEET

| recipe_id | runs | rows | unit_price | est_cost |
|---|---|---|---|---|
| RC-WEB | 0 (Apify BLOCKED; would-be 13) | 0 | compute-only | $0.00 spent / $0.03 would-be |
| RC-FBC | 0 (BLOCKED; would-be 1) | 0 | $0.002/comment | $0.00 spent / $0.08 would-be |
| RC-TP | 0 (BLOCKED; would-be 5) | 0 | $0.00065/review | $0.00 spent / $0.12 would-be |
| RC-YTX | 0 so far (runs in 06) | — | TranscriptAPI credits | budgeted ≤45 credits leg-wide |
| RC-EXA | 2 so far (low, discovery in 04) | — | $0.025/run avg | $0.05 spent so far / $2.60 leg-wide cap |
| RC-RD | 0 (chain exhausted, no URL) | 0 | $0.0015/comment | $0.00 |

Σ spent this leg: $0.05 (Exa only) vs scoped plan cap $8÷3≈$2.67. No trims needed — under cap; the constraint is tool access, not budget.

## §11 COVERAGE STATEMENT

Every engagement figure, date and author above is printed exactly as read (search-snippet numbers marked `[R-SNIPPET]`, Exa-opened pages marked `[R-PAGE via Exa]`); a 0-yield lane (`reddit_post+comments`) prints its reason (0 of 22 WebSearch queries this run, across both 04 and 05 legs, surfaced an actual reddit.com URL — Shopify's own community forum dominates results instead); walled pages (Etsy Community replies, 4 of 5 target Facebook groups, all 5 Trustpilot page bodies) are listed, not harvestable, and counted as such.

COVERAGE: URL 23/60 (LISTED 21 · QUERY-ONLY 0 · BLOCKED 2 · OPERATOR-PASTE 2) · PB below URL floor: [NONE — PB-01's own scoped floor of 12 across ≥3 platforms is met with 23 across 6 lanes] · CP THIN: [CP-01 (2 URLs, below its ≥4 floor)] · PLAN-VALIDATED: [PB-01 (raw Σest), CP-05 (close, 26/37.5)] · PLAN-THIN: [CP-01 (11/37.5)] · plan cost $0.05/$2.67 (this PB's share of the $8 standard harvest cap) · weakest link: Reddit is fully BLOCKED-ON-TOOL and was never even discoverable via WebSearch this run (0 reddit.com URLs surfaced across 22 queries) — the PB-01/URL-24/PB-01/URL-25 OPERATOR-PASTE rows are the only path to closing the ≥5-Reddit-thread floor. · what closing it would cost: an Apify billing-cycle reset to run `harshmaur/reddit-scraper` ($0.0018/result) plus `harshmaur/reddit-comments-scraper` ($0.0015/comment) across the 3-subreddit floor, ≈$5-15 total, or 2-3 operator-pasted Reddit thread URLs/texts mined by hand in 06.

**Continuing straight into STEP 06 with SCOPE: PB-01 (same session, same agent).**


---
# PARTIAL · PB-06 (verbatim, ids re-keyed)

# STEP 05 — VOC 2 · URL CORPUS + HARVEST PLAN — SCOPE: PB-06 · agent VOC-PB-06 (HV-PB-06)

Arriving from STEP 04 in the same session. DEGRADED-TOOL NOTICE unchanged from 04 §1 (binding, ADDENDUM 2026-09-24T20:35Z): Apify BLOCKED-ON-TOOL (all actors) · Firecrawl scrape BLOCKED-ON-TOOL · Browserbase BLOCKED-ON-TOOL · WebFetch/curl BLOCKED-ON-TOOL (egress 403, incl. every reddit.com/trustpilot.com URL). WORKING: WebSearch, TranscriptAPI, Exa research agent.

## §1 · FLOOR TABLE

| floor_name | scope | floor | target | basis |
|---|---|---|---|---|
| records_total | global (N_PB=3,N_CP=7) | max(200,3×40,7×25+15)=200 | 400 | STEP-05 §5 Step0 formula |
| records_per_PB | PB-06 | 40 | 80 | flat per-PB floor |
| records_per_CP | CP-03 | 25 (≥5 R-PAGE/R-SCRAPE) | 50 | flat per-CP floor |
| records_per_CP | CP-05 | 25 (≥5 R-PAGE/R-SCRAPE) | 50 | flat per-CP floor |
| URL_total | PB-06 (scoped ≥12) | 12 across ≥3 platforms | 24 | scoped floor |
| URL_reddit | PB-06 (scoped ≥5) | 5 | 10 | scoped floor — **0 URLs available, see §11** |
| source_type.reddit | PB-06 share | ceil(80/3)=27 | 54 | global 80 ÷ 3 PB |
| source_type.reviews | PB-06 share | ceil(60/3)=20 | 40 | global 60 ÷ 3 |
| source_type.video_comments | PB-06 share | ceil(30/3)=10 | 20 | global 30 ÷ 3 (re-mapped to youtube_transcript, the only working video lane) |
| source_type.fb_forum_quora | PB-06 share | ceil(20/3)=7 | 14 | global 20 ÷ 3 |
| source_type.ad_comments | PB-06 share | ceil(10/3)=4 | 8 | global 10 ÷ 3 — LATE-BOUND: 02.share_url, 0 available this run |
| source_types_n | PB-06 | ≥4 | — | diversity floor |
| tag.pain | PB-06 share | ceil(20/3)=7 | 14 | global ÷3 |
| tag.scene | PB-06 share | ceil(15/3)=5 | 10 | global ÷3 |
| tag.failed_solution | PB-06 share | ceil(20/3)=7 | 14 | global ÷3 |
| tag.objection | PB-06 share | ceil(20/3)=7 | 14 | global ÷3 |
| tag.desire | PB-06 share | ceil(15/3)=5 | 10 | global ÷3 |
| tag.trigger | PB-06 share | ceil(15/3)=5 | 10 | global ÷3 |
| tag.belief | PB-06 share | ceil(15/3)=5 | 10 | global ÷3 |
| tag.symptom | PB-06 share | ceil(10/3)=4 | 8 | global ÷3 |
| tag.skepticism | PB-06 share | ceil(10/3)=4 | 8 | global ÷3 |
| tag.spend | PB-06 share | ceil(5/3)=2 | 4 | global ÷3 |
| tag.deeper_hope | PB-06 share | ceil(5/3)=2 | 4 | global ÷3 |
| tag.tired_of_hearing | PB-06 share | ceil(5/3)=2 | 4 | global ÷3 |
| tag.horror_story | PB-06 share | ceil(3/3)=1 | 2 | global ÷3 |
| tag.curiosity | PB-06 share | ceil(3/3)=1 | 2 | global ÷3 |
| tag.corruption | PB-06 share | ceil(3/3)=1 | 2 | global ÷3 |

## §2 · URL TABLE (URL-##) — grouped PB-06 → lane → rank

### lane: youtube_transcript (10 URLs, all FETCHED)
| url_id | com_id | platform | url | title | op_author | date_posted | engagement_primary | engagement_secondary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-06/URL-01 | COM-19 | youtube_search | https://youtu.be/r0WnKYbcw9k | I Lost Money Dropshipping in India… The Harsh Reality Nobody Shows | RISHAV AGRAWAL | 2026-09-21 | 178 views | — | relevance | views | PH-02 | youtube_transcript | 2 | RC-YTX | FETCHED | [R-SCRAPE] |
| PB-06/URL-02 | COM-19 | youtube_search | https://youtu.be/x9lgR_iHPuQ | I Lost $1,000 Dropshipping.. So I Tried Again | Jenny Hoyos | ~2022 | 458,125 views | — | relevance | views | PH-02,18 | youtube_transcript | 4 | RC-YTX | FETCHED | [R-SCRAPE] |
| PB-06/URL-03 | COM-19 | youtube_search | https://youtu.be/OOfML4xMiC4 | I Lost $40,000 Dropshipping and Still Won | Dylan Fisher | ~2026 | 265 views | — | relevance | views | PH-02,20 | youtube_transcript | 6 | RC-YTX | FETCHED | [R-SCRAPE] |
| PB-06/URL-04 | COM-19 | youtube_search | https://youtu.be/AZIC4HjKj7s | I just lost over $1000 across 3 dropshipping stores | Charlie Nuttall | ~2026 | 188 views | — | relevance | views | PH-02,18 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| PB-06/URL-05 | COM-19 | youtube_search | https://youtu.be/oS2aafo469M | I Lost Thousands Dropshipping: Don't Make These Mistakes | Alex Ulbin | ~2024 | 11,437 views | — | relevance | views | PH-02,18,20 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| PB-06/URL-06 | COM-19 | youtube_search | https://youtu.be/83RypPyuXfU | How I lost A Million Dropshipping | Michael Bernstein | ~2023 | 45,811 views | — | relevance | views | PH-02,20 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| PB-06/URL-07 | COM-19 | youtube_search | https://youtu.be/Cszp_nIwu8I | i lost everything and then became rich with dropshipping | Liam Bradshaw | ~2024 | 55,529 views | — | relevance | views | PH-02 | youtube_transcript | 2 | RC-YTX | FETCHED (partial, output truncated) | [R-SCRAPE] |
| PB-06/URL-08 | COM-19 | youtube_search | https://youtu.be/iRObd23cn_U | I Lost ₹50,000 on Dropshipping | Tushar Jain | ~2026 | 5,549 views | — | relevance | views | PH-02 | youtube_transcript | 2 | RC-YTX | FETCHED (Hindi, [translated]) | [R-SCRAPE] |
| PB-06/URL-09 | COM-19 | youtube_search | https://youtu.be/o_eEADR4MY0 | Why I Quit Dropshipping After 4 Years.. (My Story) | Tanner Planes | ~2021 | 50,889 views | — | relevance | views | PH-02,07 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| PB-06/URL-10 | COM-19 | youtube_search | https://youtu.be/3d55w3wDSII | I lost ALL of my money Dropshipping...(Biggest Mistakes) | Owen's Bank Account | ~2021 | 267 views | — | relevance | views | PH-02,06 | youtube_transcript | 4 | RC-YTX | FETCHED | [R-SCRAPE] |

### lane: forum_thread (9 URLs: 5 Warrior Forum, 4 Shopify Community)
| url_id | com_id | platform | url | title | op_author | date_posted | engagement_primary | sort_seen | why_chosen | lane | est_records | recipe_id | status | tier_expected |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-06/URL-11 | COM-17 | forum | https://www.warriorforum.com/social-media/1458034-ive-spent-600on-fb-ads-still-no-sales.html | I've spent $600on FB ads and still no sales... | BluesPlayer | 2022-09-06 | 3 replies opened | top | PH-03 | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-12 | COM-17 | forum | https://www.warriorforum.com/beginners-area/1431345-facebook-ads-no-order.html | Facebook Ads no Order | rb10 | 2021-03-06 | 14 replies total, 3 opened | top | PH-03,19(assumption AS-01) | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-13 | COM-17 | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1214546-massive-traffic-but-no-sales.html | Massive Traffic But No Sales? | Gig Grand | 2016-08-31 | 28 replies total, 3 opened | top | PH-01,05 | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-14 | COM-17 | forum | https://www.warriorforum.com/social-media/1252728-facebook-ads-not-converting-why.html | Facebook Ads Not Converting - Why? | rijichouno | 2017-02-01 | 9 replies | top | PH-03 | forum_thread | 3 | RC-EXA | LISTED | [R-PAGE] |
| PB-06/URL-15 | COM-17 | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1283825-should-i-hire-marketing-freelancer-freelancer-com.html | Should I hire a Marketing Freelancer from Freelancer.com? | Mysterious Robin | 2017-06-30 | unknown | top | PH-20(assumption AS-01, closest-but-excluded) | forum_thread | 2 | RC-EXA | LISTED | [R-PAGE] |
| PB-06/URL-16 | COM-16 | forum | https://community.shopify.com/t/ive-got-1-600-session-and-no-sales-and-have-done-everything-right/580410 | I've got 1,600 session and no sales and have done everything right | cozyhomehaven | 2025-12-20 | 376 views, 15 users, 3 replies opened | new | PH-01,09 | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-17 | COM-16 | forum | https://community.shopify.com/t/no-sales-should-i-sell-or-close-my-store/408286 | No Sales – Should I Sell or Close My Store? | Hunter6 | 2025-04-13 | 3 replies opened | new | PH-01,03 | forum_thread | 3 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-18 | COM-16 | forum | https://community.shopify.com/t/google-ads-show-conversions-but-there-arent-any-on-my-store/377195/1 | Google Ads show conversions but there arent any on my store | noah_essentis | 2024-11-27 | 5 replies | new | PH-03 | forum_thread | 3 | RC-EXA | LISTED | [R-PAGE] |
| PB-06/URL-19 | COM-16 | forum | https://community.shopify.com/t/tiktok-ads-show-conversions-but-shopify-doesnt/258900/8 | TikTok Ads show conversions but shopify doesnt | unknown | 2023-10-12 | unknown | new | PH-03 | forum_thread | 2 | RC-EXA | LISTED | [R-PAGE] |

### lane: quora_answers (9 URLs: 1 FETCHED, 8 LISTED)
| url_id | com_id | url | title | engagement_primary | why_chosen | lane | est_records | recipe_id | status |
|---|---|---|---|---|---|---|---|---|---|
| PB-06/URL-20 | COM-18 | https://www.quora.com/Why-arent-I-driving-any-sales-on-my-online-Shopify-store-Ive-gotten-32-5k-impressions-367-ad-clicks-and-253-conversions-on-my-store-in-the-past-month-but-not-a-single-sale-Why-is-this | Why aren't I driving any sales on my online Shopify store?... | 87 answers | PH-01,15 | quora_answers | 5 | RC-EXA | FETCHED |
| PB-06/URL-21 | COM-18 | https://www.quora.com/Why-are-you-not-getting-expected-sales-to-your-Shopify-store | Why are you not getting expected sales to your Shopify store? | unknown | PH-01 | quora_answers | 2 | RC-EXA | LISTED |
| PB-06/URL-22 | COM-18 | https://www.quora.com/Why-do-sales-not-start-on-my-Shopify-store-I-am-fed-up | Why do sales not start on my Shopify store? I am fed up. | unknown | PH-01,12 | quora_answers | 2 | RC-EXA | LISTED |
| PB-06/URL-23 | COM-18 | https://www.quora.com/Why-isn-t-my-Shopify-store-getting-any-sales-after-700-online-sessions | Why isn't my Shopify store getting any sales after 700 online sessions? | unknown | PH-01 | quora_answers | 2 | RC-EXA | LISTED |
| PB-06/URL-24 | COM-18 | https://www.quora.com/How-do-I-become-successful-in-dropshipping-I-ve-tried-multiple-courses-that-failed-to-work-I-ve-lost-4000-I-m-17-y-o-making-10-an-hour-I-gave-it-up-a-couple-of-weeks-ago-but-I-just-feel-like-I-wasted-4000-for | ...I've lost $4000... I gave it up... wasted $4000 for nothing | unknown | PH-02,18 | quora_answers | 2 | RC-EXA | LISTED (retrieved:false on targeted open attempt) |
| PB-06/URL-25 | COM-18 | https://www.quora.com/Is-dropshipping-a-scam-It-seems-way-too-good-to-be-true-How-can-someone-make-money-without-owning-any-products | Is dropshipping a scam? ... | unknown | PH-10 | quora_answers | 2 | RC-EXA | LISTED |
| PB-06/URL-26 | COM-18 | https://www.quora.com/Is-drop-shipping-a-scam-and-how-do-I-start | Is drop shipping a scam, and how do I start? | 43 answers | PH-10 | quora_answers | 2 | RC-EXA | LISTED |
| PB-06/URL-27 | COM-18 | https://www.quora.com/Is-Dropshipping-really-a-scam-to-convince-people-to-buy-expensive-courses-Sell-courses | Is Dropshipping really a scam to convince people to buy expensive courses? | unknown | PH-10 | quora_answers | 2 | RC-EXA | LISTED |
| PB-06/URL-28 | COM-18 | https://www.quora.com/How-many-people-actually-make-profit-dropshipping | How many people actually make profit dropshipping? | 42 answers | PH-16 | quora_answers | 2 | RC-EXA | LISTED |

### lane: blog_comments (4 URLs, all FETCHED)
| url_id | com_id | url | title | op_author | date_posted | why_chosen | lane | est_records | recipe_id | status | tier_expected |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-06/URL-29 | COM-23 | https://revenueamplify.com/lost-1000-dropshipping-but-im-not-giving-up/ | Lost $1,000 Dropshipping - But I'm Not Giving Up | anonymous | 2024-02-01 | PH-02,18 | blog_comments | 2 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-30 | COM-23 | https://www.salehoo.com/ethan-dobbins-success-story | Ethan Dobbins Dropshipping Success Story | Sean Leonardia (interviewer) | 2026-07-08 | PH-02,18 | blog_comments | 2 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-31 | COM-23 | https://nicojannasch.com/going-all-in-when-youre-broke/ | When You're a Broke Entrepreneur | Nico Jannasch | 2016-06-19 | PH-02,18 | blog_comments | 1 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| PB-06/URL-32 | COM-23 | http://kblee007.blogspot.com/2018/02/3-tips-for-succeeding-after-you-fail.html | 3 Tips For Succeeding After You Fail | Unknown (page byline) | 2018-02-21 | PH-02,06 | blog_comments | 1 | RC-EXA | FETCHED | [R-PAGE via Exa] |

### lane: reddit_post+comments — 0 URLs (BLOCKED, see §11)

Counter (final): URL 32/12 floor · reddit 0/5 **PARTIAL** · CP-03 URLs: 16 (all youtube+blog + PH-02/18-tagged forum/quora) ≥4 met · CP-05 URLs: 4 (PB-06/URL-06,09,12,15) ≥4 met (thin) · platforms 5 (youtube_search, forum×2-communities, quora, blog_comments) · Σest PB-06 = 92 (well above 1.5×40=60) → **PLAN-VALIDATED** · Σest CP-03 ≈ 55 (above 1.5×25=37.5) → **PLAN-VALIDATED** · Σest CP-05 ≈ 12 (below 1.5×25=37.5) → **PLAN-THIN** · plan cost $0.425 Exa + ~14 TranscriptAPI credits, well under PB-06 share of standard $8 harvest cap ÷3≈$2.67.

## §3 · EXCLUSIONS (EX-##)

| ex_id | url | reason | pb_id |
|---|---|---|---|
| EX-01 | (2nd Quora dropshipping-course-loss question, targeted Exa open) | could not be retrieved — indexed title only, page extraction failed | PB-06 |
| EX-02 | https://apps.shopify.com/my-online-fashion-store/reviews (borderline CP-05 match from earlier Exa run) | off-topic — reviewer describes buying a prebuilt app-store, not a first-person build-then-fail narrative; excluded from URL table, kept as a note in 04 §4 | PB-06 |

## §4 · LANE MIX per PB-06

| pb_id | youtube_transcript | forum_thread | quora_answers | blog_comments | reddit | dominant platform share | SINGLE-PLATFORM flag |
|---|---|---|---|---|---|---|---|
| PB-06 | 10 | 9 | 9 | 4 | 0 | youtube_transcript 31% | NO — no lane exceeds 50% |

## §5 · RECIPE CARDS (RC-##)

**RC-YTX** (actually run) — TranscriptAPI `get_youtube_transcript`: `{"video_url": "<video id/url>", "format": "text", "include_timestamp": true, "send_metadata": true}` — cost ~1 credit/call · output_field_map: `content→exact_passage source, Author→unique_author_id, Title→thread_title` · fallback_chain: [`search_youtube` for more candidates → `codepoetry/youtube-transcript-ai-scraper` (Apify, BLOCKED) → browser transcript panel (no browser tool)] · no_apify_path: direct TranscriptAPI call (this IS the no-Apify path).

**RC-EXA** (actually run) — Exa agent `mcp__Readymerce_Exa__agent_run`, effort `medium`, verbatim-extraction template: `{"query": "Open this page: <URL>. Extract the original post/question verbatim (author, date) and top replies/answers verbatim (author, date), up to 60 words each. Do not paraphrase. State plainly if the page could not be retrieved.", "effort": "medium", "outputSchema": {...structured threads/answers...}}` — cost ≈$0.10/run (3 URLs/run typical) · output_field_map: `op_text→exact_passage, op_author→unique_author_id, op_date→date_posted, url→source_url` · fallback_chain: [Exa low-effort discovery → direct WebFetch (BLOCKED) → Apify rag-web-browser (BLOCKED)] · no_apify_path: this IS the no-Apify path.

**RC-RD** (pinned, NOT RUN) — `harshmaur/reddit-comments-scraper` `{"postUrls": [], "maxCommentsPerPost": 40, "includeNSFW": false, "aiAnalysis": false}` $0.0015/comment — BLOCKED-ON-TOOL (Apify hard limit); 0 Reddit URLs exist to feed it this run anyway (see §11).

**RC-TT** (pinned, NOT RUN) — `clockworks/tiktok-comments-scraper` `{"postURLs": [], "commentsPerPost": 40, "maxRepliesPerComment": 0}` $0.001/comment — BLOCKED-ON-TOOL.

**RC-TP** (pinned, NOT RUN) — `memo23/trustpilot-scraper-ppe` `{"startUrls": ["ecomdoneforyou.com","ecommerceparadise.com","ecomxpertz.com","readymerce.com"], "maxItems": 100, "filterLanguages": ["en"], "sampling": "balanced", "sortBy": "recent", "filterDateRange": "last12months", "expandRegionalDomains": true, "scrapeAllReviews": false, "includeStats": true}` $0.00065/review — BLOCKED-ON-TOOL.

**RC-FBC** (pinned, NOT RUN) — `apify/facebook-comments-scraper` `{"startUrls": [], "resultsLimit": 40, "includeNestedComments": false, "viewOption": "RANKED_UNFILTERED"}` $0.002/comment — BLOCKED-ON-TOOL; 0 Facebook group/page URLs found this run (no browser to discover public groups).

## §6 · HARVESTER ASSIGNMENTS

| hv_id | pb_id | cp_ids | url_ids (rank order) | recipe_ids | floors | partial_file | max_extra_sources |
|---|---|---|---|---|---|---|---|
| HV-PB-06 | PB-06 | [CP-03, CP-05] | PB-06/URL-02,05,06,04,09,10,03,08,01,07 (youtube, ranked by views desc within relevance) then PB-06/URL-11,12,13,16,17,14,18,15,19 (forum) then PB-06/URL-20,26,22,21,23,24,25,27,28 (quora) then PB-06/URL-29,30,31,32 (blog) | RC-YTX, RC-EXA | records≥40, CP-03≥25, CP-05≥25 (PARTIAL likely, see PLAN-THIN §2) | 06-partials/06-VOC_MASTER.PB-06.csv | 8 |

CP-05 has no dedicated `HV-CP-##` task — it is thin (PLAN-THIN) but its 4 URLs are inside HV-PB-06's own list already; 06 §Step 3(a) population-first pass runs against it directly.

## §7 · FALLBACK CHAINS per lane

| lane | chain | trigger |
|---|---|---|
| youtube_transcript | TranscriptAPI direct → `codepoetry/youtube-transcript-ai-scraper` (Apify, BLOCKED) → browser panel (none) | caption-less video |
| forum_thread / quora_answers / blog_comments | Exa agent medium → Exa agent low (discovery only) → direct WebFetch (BLOCKED) → Apify rag-web-browser (BLOCKED) → OPERATOR-PASTE | page not retrievable by Exa |
| reddit_* | Apify harshmaur/reddit-scraper (BLOCKED) → trudax/reddit-scraper-lite (BLOCKED) → rag-web-browser old.reddit.com/.json (BLOCKED, egress 403) → SERP site:reddit.com (WebSearch never surfaced a reddit.com URL) → OPERATOR-PASTE | any Reddit URL needed |
| tiktok_comments / trustpilot_balanced / fb_post_comments | Apify (all BLOCKED) → OPERATOR-PASTE | any URL in these lanes |

## §8 · COUNTER FORMAT

`records n/40 · PB-06 n/40 · CP-03 n/25 · CP-05 n/25 · sources n/32 (SCRAPED n · FETCHED n · 0-yield n · BLOCKED n · PASTE n) · types n/4 · tag.pain n/7 · tag.scene n/5 · tag.failed_solution n/7 · tag.objection n/7 · tag.desire n/5 · tag.trigger n/5 · tag.belief n/5 · tag.symptom n/4 · tag.skepticism n/4 · tag.spend n/2 · tag.deeper_hope n/2 · tag.tired_of_hearing n/2 · tag.horror_story n/1 · tag.curiosity n/1 · tag.corruption n/1 · cost $x.xx`

`max_extra_sources`: 8

## §9 · SOURCE MANIFEST (pre-filled)

| unit_id | lane | community/listing | date_range | expected_record_count | fields_available | access_limits | excluded_reason |
|---|---|---|---|---|---|---|---|
| U-01..U-10 | youtube_transcript | COM-19 | 2016-2026 (upload dates) | 35 | full transcript text, author, upload date, view count | none — public captions/ASR | — |
| U-11..U-19 | forum_thread | COM-16, COM-17 | 2016-2025 | 26 | OP+reply text, author, date, URL (via Exa) | 4 of 9 not opened in full (LISTED only, time box) | — |
| U-20..U-28 | quora_answers | COM-18 | unknown-2025 | 21 | question title always; full answers only for PB-06/URL-20 | 7 of 9 not opened in full; 1 targeted open failed (EX-01) | page could not be retrieved |
| U-29..U-32 | blog_comments | COM-23 | 2016-2026 | 6 | full post text, author, date, URL (via Exa) | none | — |

## §10 · COST SHEET

| recipe_id | runs | rows | unit_price | est_cost |
|---|---|---|---|---|
| RC-YTX | 10 | 10 transcripts | ~1 credit/call | ~10 credits |
| RC-EXA | 6 (4 low discovery + 2... actually 5 medium extraction, see 04 §9 and 06 log) | ~32 URLs surfaced, 15 opened in full | $0.025 (low) / $0.10 (medium) | $0.425 total this run |
Σ ≈ $0.425 + 10 TranscriptAPI search-page credits + 10 transcript credits = 20 credits, vs PB-06 share of standard $8 harvest cap ÷3 ≈ $2.67 → **under cap**. No trims needed.

**Merge instruction for 06-MERGE:** concatenate `06-partials/06-VOC_MASTER.PB-06.csv` with the other two PBs' partials on `(source_url, unique_author_id, hash(exact_quote))`; this PB's Reddit lane is entirely `BLOCKED-ON-TOOL` (0 URLs even discoverable) — 06-MERGE's Step 6 should print `HARVEST-## order: reddit_post+comments for PB-06, recipe RC-RD, once Apify's monthly hard limit resets or an operator supplies pasted thread text`.

## §11 · COVERAGE STATEMENT

Every URL in §2 was seen (title + engagement, or full text) before being listed; FETCHED rows carry the real author/date/URL read by TranscriptAPI or Exa; LISTED-only rows are marked and were not opened further inside this box; the Reddit lane is 0-yield for a structural reason (WebSearch never once surfaced a reddit.com URL across 12 queries in 04, and every direct-fetch path is egress-blocked or Apify-blocked) and is printed as BLOCKED, not padded with an invented subreddit URL.

COVERAGE: URL 32/60 global-scale-equivalent (LISTED 32 · QUERY-ONLY 0 · BLOCKED 0-URLs-exist(reddit) · OPERATOR-PASTE 0) · PB below URL floor: NONE (32≥12 scoped) · CP THIN: [CP-05] · PLAN-VALIDATED: [PB-06, CP-03] · PLAN-THIN: [CP-05] · plan cost $0.425/~$2.67 cap · weakest link: Reddit lane has zero URLs (not just zero harvested — zero discoverable) because no tool this run can reach reddit.com in any form · what closing it would cost: same as 04 §10 — 1 Apify reddit-scraper run (~$0.10) once the account's monthly hard limit resets.


---
# PARTIAL · PB-05 (verbatim, ids re-keyed)

# 05 — VOC 2 · URL CORPUS + HARVEST PLAN · SCOPE: PB-05 · Readymerce
agent_id: VOC-PB-05 · wave W1 · leg 2/3 (04→05→06) · reads 04-partials/04-HANDOFF.PB-05.json (this session, this leg) · model: sonnet

DEGRADED-TOOL NOTICE (binding, same as 04 §1): Apify (all actors) BLOCKED-ON-TOOL · Firecrawl scrape BLOCKED-ON-TOOL · Browserbase BLOCKED-ON-TOOL · WebFetch/curl BLOCKED-ON-TOOL (403 on all research hosts) · Reddit and Trustpilot pages NOT RETRIEVABLE by any tool. Degraded-run substitution per brief: recipe cards RC-## below are printed with their pinned Apify inputs for the operator to run later; RC-YTX (TranscriptAPI) and RC-EXA (Exa verbatim-extraction template) are the cards that actually ran this leg. Reddit thread URLs were not even surfaced in search this leg (no reddit.com permalink was returned by WebSearch or Exa) — logged BLOCKED with OPERATOR-PASTE rows rather than QUERY-ONLY, since no specific URL exists to mark query-only.

02 status this session: **LATE-BOUND: 02.share_url** (02-partials/02-COMPETITOR-INTEL.NW-SEED-02.md.partial carries only a lock card, no im_records[]/share_url yet) — ad_comments lane cannot be built; a HARVEST-## order is left for 06-MERGE.

## §1 · FLOOR TABLE

| floor_name | scope | floor | target (2×floor) | basis |
|---|---|---|---|---|
| records_total | PB-05 (this harvester's share) | 40 | 80 | STEP-06 §4.1 per-PB floor, scoped |
| records | CP-05 | 25 (≥5 at [R-PAGE]/[R-SCRAPE]) | 50 | STEP-06 §4.1 per-CP floor, scoped (only in-scope CP) |
| url_total | PB-05 | 12 across ≥3 platforms | 24 | STEP-05 §4.1, scoped |
| reddit_urls | PB-05 | 5 | 10 | STEP-05 §4.1, scoped — **PARTIAL: 0 obtained, chain exhausted (see §7)** |
| cp_urls | CP-05 | 4 | 8 | STEP-05 §4.1, scoped — **met: 5 URLs** |
| source_type: reddit | PB-05 share | ceil(80/3)=27 | 54 | global 80 ÷ N_PB(3 active lanes: PB-01,PB-06,PB-05) — **PARTIAL: 0** |
| source_type: reviews (incl. ≥ ceil(8/3)=3 from 3★) | PB-05 share | ceil(60/3)=20 | 40 | global 60 ÷ 3 — **NOT RUN this leg (Amazon/Trustpilot deprioritized under time box; BLOCKED-ON-TOOL for Trustpilot regardless)** |
| source_type: video comments | PB-05 share | ceil(30/3)=10 | 20 | global 30 ÷ 3 — note: this leg's video lane is `youtube_transcript`, not `youtube_comments`; comments lane itself is BLOCKED-ON-TOOL (RC-YT scraper is Apify-only) |
| source_type: fb+forum+quora combined | PB-05 share | ceil(20/3)=7 | 14 | global 20 ÷ 3 — **met: 6 forum/quora URLs (fb=0, walled)** |
| source_type: ad_comments | PB-05 share | ceil(10/3)=4 | 8 | global 10 ÷ 3 — **LATE-BOUND: 02.share_url**, 0 available |
| source_types_present | PB-05 | ≥4 (unscoped, diversity floor) | — | forum, quora, youtube, (reddit attempted) — **PARTIAL: 3 of 4 realized** |
| tag: pain | PB-05 share | ceil(20/3)=7 | 14 | global 20÷3 |
| tag: scene | PB-05 share | ceil(15/3)=5 | 10 | global 15÷3 |
| tag: failed_solution | PB-05 share | ceil(20/3)=7 | 14 | global 20÷3 |
| tag: objection | PB-05 share | ceil(20/3)=7 | 14 | global 20÷3 |
| tag: desire | PB-05 share | ceil(15/3)=5 | 10 | global 15÷3 |
| tag: trigger | PB-05 share | ceil(15/3)=5 | 10 | global 15÷3 |
| tag: belief | PB-05 share | ceil(15/3)=5 | 10 | global 15÷3 |
| tag: symptom | PB-05 share | ceil(10/3)=4 | 8 | global 10÷3 |
| tag: skepticism | PB-05 share | ceil(10/3)=4 | 8 | global 10÷3 |
| tag: spend | PB-05 share | ceil(5/3)=2 | 4 | global 5÷3 |
| tag: deeper_hope | PB-05 share | ceil(5/3)=2 | 4 | global 5÷3 |
| tag: tired_of_hearing | PB-05 share | ceil(5/3)=2 | 4 | global 5÷3 |
| tag: horror_story | PB-05 share | ceil(3/3)=1 | 2 | global 3÷3 |
| tag: curiosity | PB-05 share | ceil(3/3)=1 | 2 | global 3÷3 |
| tag: corruption | PB-05 share | ceil(3/3)=1 | 2 | global 3÷3 |

Counter: `URL 14/12 · PB-05 14/12 · CP-05 5/4 · reddit_threads 0/5 · lanes 3 (forum_thread, quora_answers, youtube_transcript) · Σest PB-05 26/(1.5×40=60) · Σest CP-05 11/(1.5×25=37.5) · plan cost $0.25/$2.67(scoped cap, $8÷3 active PBs)`

## §2 · URL TABLE (URL-##) — PB-05, grouped by lane, rank order

### lane: youtube_transcript (rank by relevance to PB-05 first-person struggle, then views)

| url_id | com_id | pb_ids[] | population_tags[] | platform | url | title | op_author | date_posted | engagement_primary | engagement_secondary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected | duplicate_of | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-05/URL-01 | COM-31 | PB-05 | CP-05 | youtube_search | https://www.youtube.com/watch?v=xEvaenj4JH8 | I FINALLY chose my business idea \| 90-days business challenge | Business By Nancy | 2026-07-24 approx ("2 months ago") | 8,912 views | n/a | relevance | 1 | PH-08, PH-15; population-first: CP-05 | youtube_transcript | 5 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Strongest PB-05 match this leg — explicit product/business-idea-choice paralysis in first person, own words |
| PB-05/URL-02 | COM-31 | PB-05 | CP-05 | youtube_search | https://www.youtube.com/watch?v=xlV60PEwg5c | Why I Wasted My 9 Months in the Starting Days of Dropshipping\| Real talk | Manish kumar | ~2023 ("3 years ago") | 942 views | n/a | relevance | 2 | PH-08(near), PH-19; population-first: CP-05 | youtube_transcript | 3 | RC-YTX | FETCHED (full transcript read, Hindi, [translated] in 06) | [R-SCRAPE] | — | Product-research/information-paralysis theme; language Hindi, translated passages only in 06 |
| PB-05/URL-03 | COM-31 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=bKdLdxlLmPA | I Finally Found My First Winning Organic DROPSHIPPING Product! | Dave Obiefuna | ~2023 ("3 years ago") | 21,953 views | n/a | relevance | 3 | PH-02, PH-08 | youtube_transcript | 2 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Mostly ad-strategy tutorial; light first-person framing around finding the product |
| PB-05/URL-04 | COM-31 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=-1Q60dZcuHc | i finally found a winning dropshipping product (Exact Strategy Revealed) | Ry | ~2025 ("1 year ago") | 698 views | n/a | relevance | 4 | PH-02, PH-08 | youtube_transcript | 1 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Almost entirely ad-metrics tutorial; minimal usable first-person pain language |
| PB-05/URL-05 | COM-31 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=33JF7JAsG9k | How to decide what to sell online for your dropshipping store | Oberlo (Tommy Walker) | ~2018 ("8 years ago") | 105,704 views | n/a | relevance | 5 | PH-01 (states the problem verbatim in intro) | youtube_transcript | 1 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Advisor/brand voice, not sufferer voice — corroborating context only, coded speaker_stage accordingly in 06 |
| PB-05/URL-06 | COM-31 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=kO-POM2RLYw | Skip months of research with this one method | The real ecom (Carmen) | ~2026 ("7 months ago") | 101 views | n/a | relevance | 6 | PH-10-adjacent | youtube_transcript | 0 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Tactical how-to, no first-person struggle narrative — 0 usable VOC records expected |
| PB-05/URL-07 | COM-31 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=9CrxDtJr-O4 | What I Sell Online So I Don't Have To Work a 9-5 Job | Taylor Jo | ~2026 ("2 months ago") | 11,122 views | n/a | relevance | 7 | PH-01 (title match only) | youtube_transcript | 0 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Off-topic on read: reseller "what sold" haul video, not a product-selection struggle — 0 usable records expected, kept per EX-01 |
| PB-05/URL-08 | COM-31 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=4hHFTcerXD4 | I Don't Sell Much Online Should I Keep My Online Store | Rafi And Klee | ~2023 ("2 years ago") | 2,334 views | n/a | relevance | 8 | PH-01 (title match only) | youtube_transcript | 1 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Podcast about whether to keep a store (low sales), not product-selection — closer to PB-06; kept, low weight for PB-05 |

### lane: forum_thread

| url_id | com_id | pb_ids[] | population_tags[] | platform | url | title | op_author | date_posted | engagement_primary | engagement_secondary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected | duplicate_of | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-05/URL-09 | COM-27 | PB-05 | CP-05 | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1320451-winning-product-dropshipping.html | winning product ?? dropshipping | alex19890 | 2017-12-16 | 1 reply | n/a | relevance | 1 | PH-02, PH-19; population-first: CP-05 | forum_thread | 1 | RC-EXA (Exa agent_run, medium) | LISTED + FETCHED (verbatim OP read) | [R-PAGE via Exa] | — | Direct beginner-in-dropshipping question naming "winning product" |
| PB-05/URL-10 | COM-28 | PB-05 | CP-05 | forum | https://www.indiehackers.com/post/our-solution-for-finding-winning-products-8173495584 | Our solution for finding winning products | Ilia Boltianov | 2021-09-02 | 1 comment | 1 upvote | relevance | 2 | PH-08(near); population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Founder framing the product-finding problem as widespread |
| PB-05/URL-11 | COM-27 | PB-05 | — | forum | https://www.warriorforum.com/offline-marketing/655739-alibaba-com-dropshipping.html | Alibaba.com and dropshipping | neeralt | ~2012 ("14 years ago") | 15 replies | n/a | relevance | 3 | PH-01-adjacent (sourcing/product question) | forum_thread | 2 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Sourcing/product-type question, older thread |
| PB-05/URL-12 | COM-27 | PB-05 | — | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/746185-please-some-help-dropshipping.html | Please some help with Dropshipping..... | clik2000 | ~2013 ("14 years ago") | 8 replies | n/a | relevance | 4 | PH-01-adjacent | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Niche/supplier question with product-selection sub-thread |
| PB-05/URL-13 | COM-28 | PB-05 | — | forum | https://www.indiehackers.com/post/no-ideas-for-backend-products-268e3559b8 | No ideas for backend products | codefella | 2021-08-01 | n/a | n/a | relevance | 5 | PH-05-adjacent | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Digital/SaaS product-ideation struggle, not physical dropshipping — population match imperfect, kept |

### lane: quora_answers

| url_id | com_id | pb_ids[] | population_tags[] | platform | url | title | op_author | date_posted | engagement_primary | engagement_secondary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected | duplicate_of | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-05/URL-14 | COM-29 | PB-05 | CP-05 | quora | https://www.quora.com/What-product-will-you-suggest-I-sell-I-am-a-25-year-old-lady-and-I-need-help-with-product-ideas-to-sell-even-if-its-in-the-market-It-s-a-fast-moving-product-My-capital-is-500-cedis | What product will you suggest I sell? I am a 25-year-old lady... | not shown on page | not shown | not shown | n/a | relevance | 1 | PH-03; population-first: CP-05 | quora_answers | 1 | RC-EXA | LISTED + FETCHED (question text verbatim; answer count not exposed) | [R-PAGE via Exa] | — | Direct product-idea request; author handle not exposed by the retrieved page |

**4 other Quora URLs attempted this leg (2 in the 04 discovery run, 2 in a follow-up), all returned Quora's own "Something went wrong" error on load — logged here, not counted as LISTED:** https://www.quora.com/I-want-to-create-a-business-and-sell-stuff-but-I-m-not-sure-what-to-sell-How-do-I-choose-a-good-product-service-and-or-item-to-sell · https://www.quora.com/How-can-I-find-winning-products-to-sell-on-Shopify-for-dropshipping · https://www.quora.com/What-is-the-step-by-step-process-to-find-a-winning-product-for-Shopify-dropshipping-I-have-seen-many-videos-but-I-still-can-t-understand-properly · https://www.quora.com/What-products-should-I-sell-as-a-beginner-on-my-eBay-store — status BLOCKED (page-load error), reason logged per row in §3 EXCLUSIONS.

### BLOCKED lanes (named, not harvestable this leg)

| url_id | com_id | platform | url | status | reason |
|---|---|---|---|---|---|
| PB-05/URL-15 | COM-25 | reddit | https://www.reddit.com/r/dropshipping/ | BLOCKED | subreddit named, no thread URL ever surfaced — Apify BLOCKED-ON-TOOL, Exa agent "could not be retrieved" — **OPERATOR-PASTE requested: 5-10 top r/dropshipping thread URLs matching "what should I sell" / "winning product"** |
| PB-05/URL-16 | COM-26 | reddit | https://www.reddit.com/r/dropship/ | BLOCKED | same as PB-05/URL-15 — **OPERATOR-PASTE requested: 3-5 top r/dropship thread URLs** |
| PB-05/URL-17 | COM-30 | facebook_group | https://www.facebook.com/groups/cjdropshipping/ | BLOCKED | LOGIN_WALLED, no post content visible to any tool |
| PB-05/URL-18 | COM-30 | facebook_group | https://www.facebook.com/groups/3010156415933280/ | BLOCKED | LOGIN_WALLED |
| PB-05/URL-19 | COM-30 | facebook_group | https://www.facebook.com/groups/dropshippingtrendingproduct/ | BLOCKED | LOGIN_WALLED |

## §3 · EXCLUSIONS (EX-##)

| ex_id | url | reason | pb_id |
|---|---|---|---|
| EX-01 | https://www.youtube.com/watch?v=9CrxDtJr-O4 | off-topic (reseller "what sold" haul, not a product-selection struggle narrative) | PB-05 |
| EX-02 | https://www.quora.com/I-want-to-create-a-business-and-sell-stuff-but-I-m-not-sure-what-to-sell-How-do-I-choose-a-good-product-service-and-or-item-to-sell | deleted/unavailable (Quora "Something went wrong" on load, twice) | PB-05 |
| EX-03 | https://www.quora.com/How-can-I-find-winning-products-to-sell-on-Shopify-for-dropshipping | deleted/unavailable (same Quora load error) | PB-05 |
| EX-04 | https://www.quora.com/What-is-the-step-by-step-process-to-find-a-winning-product-for-Shopify-dropshipping-I-have-seen-many-videos-but-I-still-can-t-understand-properly | deleted/unavailable (same) | PB-05 |
| EX-05 | https://www.quora.com/What-products-should-I-sell-as-a-beginner-on-my-eBay-store | deleted/unavailable (same) | PB-05 |
| EX-06 | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/614515-what-best-dropshipping-company.html | partial content only (nav/boilerplate loaded, thread body not retrievable per Exa) | PB-05 |

## §4 · LANE MIX — PB-05

| pb_id | youtube_transcript | forum_thread | quora_answers | reddit_* | fb_* | dominant platform share | SINGLE-PLATFORM flag |
|---|---|---|---|---|---|---|---|
| PB-05 | 8 | 5 | 1 | 0 (BLOCKED) | 0 (BLOCKED) | youtube_transcript 57% (8/14) | **SINGLE-PLATFORM: PB-05** — youtube_transcript exceeds 50% of listed URLs, driven entirely by Reddit and Facebook being fully blocked this run, not by choice |

## §5 · RECIPE CARDS (RC-##)

**RC-YTX** (ACTUALLY RAN this leg) — `mcp__TranscriptAPI__get_youtube_transcript` · input: `{"video_url": "<11-char videoId>", "format": "text", "include_timestamp": true}` · 8 calls this leg, cost: TranscriptAPI credit-metered (not itemized per call by the tool; run against the ≤45-credit budget alongside `search_youtube`'s 5 credits) · output_field_map: `text→exact_passage/exact_quote, title→thread_title, channelTitle→unique_author_id, publishedTimeText→date_posted (relative, converted), videoId→source_url` · fallback_chain: `codepoetry/youtube-transcript-ai-scraper` (Apify, BLOCKED-ON-TOOL) → browser transcript panel (Browserbase, BLOCKED-ON-TOOL) → skip, video kept UNSIZED-for-transcript.

**RC-EXA** (ACTUALLY RAN this leg) — `mcp__Readymerce_Exa__agent_run` · query template: *"Open these exact pages and extract VERBATIM first-person comments/posts about [PB-05 topic]. For each: page URL, author handle, exact quote (verbatim, do not paraphrase), date posted if shown. Pages: [list]. Say explicitly if a page could not be retrieved. Do not merge different speakers' words together."* · `effort: "medium"` for verbatim extraction (this leg: 2 medium runs, $0.10 each) / `effort: "low"` for discovery (this leg: 2 low runs, $0.025 each) · `outputSchema: {passages:[{url,author,date,quote,retrieved}]}` · total this leg: $0.25 · fallback_chain: none (Exa is itself the fallback for Apify's `apify/website-content-crawler` and `fatihtahta/quora-scraper`, both BLOCKED-ON-TOOL) · no_apify_path: this IS the no-Apify path.

**RC-WEB** (PINNED, NOT RUN — Apify BLOCKED-ON-TOOL; printed so the operator can run it later) — `apify/website-content-crawler` · input: `{"startUrls": [{"url": "<forum thread URL>"}], "crawlerType": "cheerio", "maxCrawlDepth": 0, "maxCrawlPages": 30, "htmlTransformer": "readableTextIfPossible", "removeElementsCssSelector": "nav, footer, script, style, noscript, svg, [role=\"dialog\"]", "saveMarkdown": true, "proxyConfiguration": {"useApifyProxy": true}}` · unit_price: compute-only ≈$0.001–0.003/page · output_field_map: `text→exact_passage, url→source_url` · fallback_chain: `apify/rag-web-browser` → RC-EXA (this leg's actual substitute).

**RC-QU** (PINNED, NOT RUN — Apify BLOCKED-ON-TOOL) — `fatihtahta/quora-scraper` · input: `{"queries": ["don't know what to sell online", "can't find a winning product", "what product should I sell"], "searchType": "Answer", "timeFilter": "All Time", "maxItemsPerQuery": 20, "startUrls": ["https://www.quora.com/What-product-will-you-suggest-I-sell-I-am-a-25-year-old-lady-and-I-need-help-with-product-ideas-to-sell-even-if-its-in-the-market-It-s-a-fast-moving-product-My-capital-is-500-cedis"]}` · unit_price: $0.00099/record · fallback_chain: `memo23/quora-scraper` → RC-EXA (actual substitute).

**RC-RD** (PINNED, NOT RUN — Apify BLOCKED-ON-TOOL; no Reddit thread URLs exist yet to feed it) — `harshmaur/reddit-comments-scraper` · input: `{"postUrls": [{"url": "<OPERATOR-PASTED r/dropshipping or r/dropship thread URL>"}], "maxCommentsPerPost": 40, "includeNSFW": false, "aiAnalysis": false}` · unit_price: $0.0015/comment · fallback_chain: `clearpath/reddit-post-comments-bulk-scraper` → `apify/rag-web-browser` on `old.reddit.com/<post>/.json` → SERP `site:reddit.com <PH>` (all BLOCKED-ON-TOOL / egress-403 this run) → **OPERATOR-PASTE is the only open path**.

**RC-FBC** (PINNED, NOT RUN — Apify BLOCKED-ON-TOOL; groups LOGIN_WALLED regardless) — `apify/facebook-comments-scraper` · input: `{"startUrls": [{"url": "<public FB post URL>"}], "resultsLimit": 40, "includeNestedComments": false, "viewOption": "RANKED_UNFILTERED"}` · unit_price: $0.002/comment · fallback_chain: `memo23/facebook-comments-scraper` → `dz_omar/facebook-comment-scraper` → `[R-WALLED]`, not harvestable.

## §6 · HARVESTER ASSIGNMENTS

| hv_id | pb_id | cp_ids | url_ids[] (rank order) | recipe_ids[] | floors | partial_file | max_extra_sources |
|---|---|---|---|---|---|---|---|
| HV-PB-05 | PB-05 | [CP-05] | [PB-05/URL-01..PB-05/URL-14] (PB-05/URL-15..19 BLOCKED, kept for the log) | [RC-YTX, RC-EXA, RC-WEB(pinned), RC-QU(pinned), RC-RD(pinned), RC-FBC(pinned)] | records≥40 (PB-05) · CP-05≥25 · reddit≥5 (PARTIAL) · url_total≥12 (met) | 06-partials/06-VOC_MASTER.PB-05.csv | 8 |

No separate `HV-CP-##` needed — CP-05 is the only in-scope CP and its 5 URLs already exceed the per-CP URL floor (≥4); it is carried inside HV-PB-05.

## §7 · FALLBACK CHAINS PER LANE

| lane | chain | trigger |
|---|---|---|
| forum_thread | apify/website-content-crawler → apify/rag-web-browser → Exa agent_run (RC-EXA, USED) → page fetch (WebFetch, BLOCKED-403) → skip | Apify BLOCKED-ON-TOOL at step 1 → RC-EXA used from step 3 this leg |
| quora_answers | fatihtahta/quora-scraper → memo23/quora-scraper → Exa agent_run (RC-EXA, USED) → skip | same, RC-EXA used |
| youtube_transcript | johnvc/YoutubeTranscripts (Apify, BLOCKED) → TranscriptAPI get_youtube_transcript (USED) → codepoetry/youtube-transcript-ai-scraper (Apify, BLOCKED) → browser transcript panel (Browserbase, BLOCKED-401) → skip | Apify blocked at step 1 → TranscriptAPI used at step 2 |
| reddit_post+comments | harshmaur/reddit-scraper (BLOCKED) → trudax/reddit-scraper-lite (BLOCKED) → apify/rag-web-browser on old.reddit.com (BLOCKED) → SERP site:reddit.com (WebSearch tried, returned 0 reddit.com URLs) → **OPERATOR-PASTE (open, unresolved)** | full chain exhausted this leg |
| fb_post_comments | apify/facebook-groups-scraper (BLOCKED) → apify/facebook-comments-scraper (BLOCKED) → memo23/facebook-public-group-posts-scraper (BLOCKED) → browser (Browserbase, BLOCKED-401) → **[R-WALLED], not harvestable** | full chain exhausted this leg |

## §8 · COUNTER FORMAT (verbatim string 06 prints after every source unit)

`records n/40(PB-05) · CP-05 n/25 · sources n/14 (FETCHED · 0-yield · BLOCKED · PASTE) · types n/4 · pain n/7 · scene n/5 · failed_solution n/7 · objection n/7 · desire n/5 · trigger n/5 · belief n/5 · symptom n/4 · skepticism n/4 · spend n/2 · deeper_hope n/2 · tired_of_hearing n/2 · horror_story n/1 · curiosity n/1 · corruption n/1 · cost $x.xx`

## §9 · SOURCE MANIFEST (pre-filled)

| unit_id | lane | community/listing | date_range | expected_record_count | fields_available | access_limits | excluded_reason |
|---|---|---|---|---|---|---|---|
| PB-05/URL-01 | youtube_transcript | Business By Nancy channel | single video, 2026 | 5 | full transcript, title, author, views, publish date (relative) | none | — |
| PB-05/URL-02 | youtube_transcript | Manish kumar channel | single video, ~2023 | 3 | full transcript (Hindi), title, author, views | language (Hindi — [translated] tag required in 06) | — |
| PB-05/URL-03..08 | youtube_transcript | 6 more channels | 2018-2026 | 1-2 each (2 est. 0) | full transcript, title, author, views | none | PB-05/URL-06/PB-05/URL-07 low/off-topic content |
| PB-05/URL-09,11,12 | forum_thread | Warrior Forum ecommerce/offline-marketing subforums | 2012-2017 | 1-2 each | OP text verbatim, author, date, reply count | forum-wide member count not exposed | — |
| PB-05/URL-10,13 | forum_thread | Indie Hackers | 2021 | 1 each | OP text verbatim, author, date | site member count not exposed | — |
| PB-05/URL-14 | quora_answers | Quora | undated | 1 | question text verbatim | author handle, date, answer count not exposed | — |
| PB-05/URL-15,16 | reddit_* | r/dropshipping, r/dropship | n/a | 0 (BLOCKED) | none | Apify hard limit + Exa retrieval failure | tool access |
| PB-05/URL-17,18,19 | fb_post_comments | 3 named FB groups | n/a | 0 (BLOCKED) | none | LOGIN_WALLED | access |

## §10 · COST SHEET

| recipe_id | runs | rows | unit_price | est_cost |
|---|---|---|---|---|
| RC-EXA | 4 (2 low + 2 medium, cumulative across 04+05) | 6 pages opened, ~13 passages returned | $0.025 (low) / $0.10 (medium) | $0.25 |
| RC-YTX | 8 | 8 transcripts (1 error/retried) | TranscriptAPI credits (not $-metered here) | $0 (credits) |
| RC-WEB / RC-QU / RC-RD / RC-FBC | 0 (pinned, not run) | 0 | — | $0 |

**Σ this leg: $0.25 vs. scoped cap $2.67 ($8 standard full-harvest cap ÷ 3 active-lane PBs). No trim needed — well under cap.** Remainder reserved for STEP 06 harvest (more Exa medium runs for forum/quora deep-mining, more transcript fetches if new videos surface in the population-first pass).

**Merge instruction for 06-MERGE (STEP 06 §5 Step 6):** concatenate this leg's `06-partials/06-VOC_MASTER.PB-05.csv` with the other active-lane partials (PB-01, PB-06) when present; the ad_comments lane stays `LATE-BOUND: 02.share_url` until 02 finishes — leave a `HARVEST-##` order for it; the reddit_* lane stays `BLOCKED-ON-TOOL` — leave a `HARVEST-##` order naming `RC-RD` and the two subreddit URLs once an operator pastes real thread URLs or Apify access is restored.

## §11 · COVERAGE STATEMENT

Every URL above was actually opened this leg (full page/transcript text read via Exa or TranscriptAPI) before being marked LISTED/FETCHED — engagement figures (reply counts, view counts) are printed exactly as the tool returned them, never estimated; a 0-yield lane (reddit_*, fb_*) prints its exact block reason (Apify hard limit, Exa "could not be retrieved", or LOGIN_WALLED) rather than a guess; walled Facebook pages are listed, not harvestable. The corpus this leg is single-platform-heavy toward YouTube (57%) purely because Reddit and Facebook — the platforms most likely to hold PB-05's real population — were fully blocked by tooling, not by choice; this is flagged as `SINGLE-PLATFORM: PB-05` above rather than hidden.

**COVERAGE: URL 14/12 (LISTED 14 · QUERY-ONLY 0 · BLOCKED 5 · OPERATOR-PASTE 2 requested) · PB below URL floor: [NONE on total; reddit-specific sub-floor unmet] · CP THIN: [NONE — CP-05 has 5 URLs ≥ floor 4] · PLAN-VALIDATED: [NONE] · PLAN-THIN: [PB-05 (Σest 26 < 1.5×40=60); CP-05 (Σest 11 < 1.5×25=37.5)] · plan cost $0.25/$2.67(scoped cap) · weakest link: Reddit and Facebook — the two platforms most likely to carry PB-05's real "what should I sell" population — are both fully BLOCKED-ON-TOOL this run, leaving the corpus YouTube/forum/Quora-heavy · what closing it would cost: Apify plan reset (or an alternate Reddit-capable credential) + ~$0.05-0.10/thread via RC-RD once real thread URLs exist (operator paste or restored access), plus RC-FBC once Facebook group access is granted.**

## §2b · ADDENDUM — URLs added during the 06 population-first mining pass (added here first, per rule: "a URL found later is added to it first")

| url_id | com_id | pb_ids[] | population_tags[] | platform | url | title | op_author | date_posted | engagement_primary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-05/URL-20 | COM-32 (new: Shopify Community) | PB-05 | CP-05 | forum | https://community.shopify.com/t/how-do-i-know-the-right-product-to-sell/189935 | How do i know the right product to sell | Deborah212399 | 2023-02-07 | 2 replies | relevance | 1 | PH-01; population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] |
| PB-05/URL-21 | COM-32 | PB-05 | CP-05 | forum | https://community.shopify.com/t/what-should-i-start-selling-as-a-new-online-retailer/118819 | What should I start selling as a new online retailer? | UserID1158907 | 2022-05-04 | 3 replies | relevance | 2 | PH-01; population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] |
| PB-05/URL-22 | COM-32 | PB-05 | CP-05 | forum | https://community.shopify.com/t/how-do-i-choose-my-first-product-to-sell-online/206448 | How do I choose my first product to sell online? | Marshmallow02 | 2023-04-07 | 1 reply | relevance | 3 | PH-15; population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] |

New COM-32: platform forum, name "Shopify Community" (community.shopify.com), a genuinely reachable (non-blocked) platform that this leg under-used initially — 3 OP threads opened, all CP-05 population-first hits, all VALIDATED-PRESENT-grade (named handles, dated, verbatim). Reply posts on these 3 threads are mostly Shopify staff / app-vendor marketing replies (Mac_2, PageFly-Kate, TeamSpocket, ReturnPrime, Skye_1, Victoria_13) — read and logged but not coded as sufferer VOC (vendor-adjacent, evidence_class CUSTOMER_EXPLANATION at best); not converted into Q-records this leg.

**Updated counter after addendum:** `URL 17/12 · PB-05 17/12 · CP-05 8/4 · lanes 3 · cost $0.55/$2.67(scoped cap)`


---
## §11 COVERAGE STATEMENT (merged)

Engagement, dates and authors only as read by the partials; 0-yield lanes keep their reasons; walled pages listed, not harvested.

COVERAGE: URL 80/60 (LISTED 70 · QUERY-ONLY 0 (PB-01 URL-24/25 print QUERY-ONLY → BLOCKED) · BLOCKED 7 · OPERATOR-PASTE 4; + 6 added in 06 + 2 owned units) · PB below URL floor: [NONE] · CP THIN: [CP-01, CP-05 (PB-06 leg)] · PLAN-VALIDATED: [PB-01, PB-06, CP-03, CP-05 (PB-01 leg)] · PLAN-THIN: [PB-05, CP-01, CP-05 (PB-05/PB-06 legs)] · plan cost $1.025/$8.00 · weakest link: reddit_post+comments has 0 URLs across all three PBs · what closing it would cost: Apify reset (≈$5–15 billing) + ≈$0.10 per PB reddit-scraper run, or operator-pasted thread URLs

## 09 APPENDIX — 2026-09-24 (URLs mined by step 09's population-first pass; appended, body untouched)

| URL-## | cluster | lane | url | author(s) | date | tier | Q-## minted | recipe |
|---|---|---|---|---|---|---|---|---|
| URL-09-01 | CL-05 | forum_thread | https://community.shopify.com/t/how-can-i-start-an-online-sports-shoe-store-with-minimal-skills/232314 | Anino | 2023-07-13 | [R-PAGE via Exa] | Q-F-9001, Q-F-9002 | RC-EXA (Exa agent_run medium) |
| URL-09-02 | CL-05 | forum_thread | https://community.shopify.com/t/is-committing-to-googles-ad-campaign-worth-the-cost-for-a-newbie/133672 | Marinerman44 (Edward) | 2022-07 | [R-PAGE via Exa] | Q-F-9003 | RC-EXA (Exa agent_run medium) |
| URL-09-03 | CL-05 | forum_thread | https://www.warriorforum.com/main-internet-marketing-discussion-forum/1418861-can-anyone-help-me-make-my-website-succeed-advice-only-please-im-getting-skint.html | Jim Bridge | NULL (page shows "6 years ago") | [R-PAGE via Exa] | Q-F-9004 | RC-EXA (Exa agent_run medium) |
| URL-09-04 | CL-05 | forum_thread | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1513502-shopify-syncee-dropshipping-good-combination.html | Darrell Hagan | NULL (page shows "1 year ago") | [R-PAGE via Exa] | Q-F-9005 | RC-EXA (Exa agent_run medium) |
| URL-09-05 | CL-05 | blog_comments/article | https://growingourretirement.com/about/ | Larry and Martha | NULL (not shown on page) | [R-PAGE via Exa] | Q-B-9001 | RC-EXA (Exa agent_run medium) |
| URL-09-06 | CL-04 | blog_comments/article | https://kaboutjie.com/why-i-want-to-be-a-mommy-blogger/ | Lynne Huysamen | 2016-02-16 | [R-PAGE via Exa] | Q-B-9002, Q-B-9003 | RC-EXA (Exa agent_run medium) |
| URL-09-07 | CL-04 | blog_comments/article | https://shopstorm.com/blog/shopstorm-stories-trendy-treehouse/ | Tara Johnston | 2016-08-24 | [R-PAGE via Exa] | Q-B-9004 | RC-EXA (Exa agent_run medium) |
| URL-09-08 | CL-04 | blog_comments/article | https://www.everythingshewants.net/2016/05/natural-beauty-products-and-soy-candles.html | Sophia Sylvester | 2016-05-19 | [R-PAGE via Exa] | Q-B-9005 | RC-EXA (Exa agent_run medium) |
| URL-09-09 | CL-04 | blog_comments/article | https://www.websitebuilderexpert.com/interviews/simply-preloved-childrens-boutique/ | Kate Casey | 2023-05-31 | [R-PAGE via Exa] | Q-B-9006, Q-B-9007 | RC-EXA (Exa agent_run medium) |
| URL-09-10 | CL-04 | blog_comments/article | https://isossychildren.blogspot.com/2013/06/isossy-children-meets-natrice-grosvenor.html | Natrice Grosvenor | 2013-06-21 | [R-PAGE via Exa] | Q-B-9008 | RC-EXA (Exa agent_run medium) |
| URL-09-11 | CL-07 | blog_comments/article | https://www.noshameincome.com/blog/ecommerce-store-case-study/ | John Shea | 2015-09-14 | [R-PAGE via Exa] | Q-B-9009, Q-B-9010 | RC-EXA (Exa agent_run medium) |
| URL-09-12 | CL-07 | blog_comments/article | https://voyagedallas.com/interview/inspiring-conversations-with-becky-beach-of-mom-beach-llc/ | Becky Beach | 2025-06-05 | [R-PAGE via Exa] | Q-B-9011 | RC-EXA (Exa agent_run medium) |
| URL-09-13 | CL-07 | blog_comments/article | https://blog.ordoro.com/2012/03/08/customer-success-ethereal-decor/ | Cynthia Oliver | 2012-03-08 | [R-PAGE via Exa] | Q-B-9012 | RC-EXA (Exa agent_run medium) |
| URL-09-14 | CL-07 | blog_comments/article | https://www.starterstory.com/launch-store-from-home | Dennis Michels | 2019-10-20 | [R-PAGE via Exa] | Q-B-9013 | RC-EXA (Exa agent_run medium) |
| URL-09-15 | CL-07 | blog_comments/article | https://www.shopify.com/au/blog/14081185-how-an-ex-con-turned-his-life-around-and-built-an-80k-per-month-ecommerce-business | Robert Nava | 2016-12-10 | [R-PAGE via Exa] | Q-B-9014 | RC-EXA (Exa agent_run medium) |
| URL-09-16 | CL-06 | forum_thread | https://community.shopify.com/t/can-i-easily-move-my-woocommerce-store-to-shopify-as-a-non-techy-user/577555/1 | emmaoli3 | 2025-11-29 | [R-PAGE via Exa] | Q-F-9006 | RC-EXA (Exa agent_run medium) |
| URL-09-17 | CL-06 | forum_thread | https://community.shopify.com/t/how-can-i-modify-variant-options-and-stock-info-in-supply-theme/68832 | _littlehoney | 2021-09-29 | [R-PAGE via Exa] | Q-F-9007 | RC-EXA (Exa agent_run medium) |
| URL-09-18 | CL-06 | forum_thread | https://www.ukbusinessforums.co.uk/threads/new-business-model-vat.418609/ | dafcjim | 2022-06-20 | [R-PAGE via Exa] | Q-F-9008 | RC-EXA (Exa agent_run medium) |

Not retrieved (listed, not harvested): https://www.quora.com/How-do-I-start-a-Shopify-store-if-I-have-no-experience (shell only) · https://www.quora.com/How-much-time-will-it-take-to-create-a-Shopify-store-Also-how-much-time-should-be-dedicated-daily-for-managing-it (shell only). Count: 18 URLs appended · 22 Q-## appended to 06-VOC_MASTER.csv (harvester_id 09).


## 11-AV-03 APPENDIX — 2026-09-24 (single P0 re-mine HARVEST-24 for B-02.AV-3 INTERNAL, which rested on one thread; appended, body untouched)
| url_id | cluster | lane | url | author | date | tier | Q-## | recipe |
|---|---|---|---|---|---|---|---|---|
| URL-11A3-01 | CL-02 | forum_thread | https://community.shopify.com/t/how-can-i-deactivate-my-online-shop-with-minimal-tech-skills/185762/1 | Heartwork_beads | 2023-01-23 | [R-PAGE via Exa] | Q-F-8301 | RC-EXA (Exa agent_run medium, agent_run_0f900213ad3648cea3327d6f2513c6d7) |
| URL-11A3-02 | CL-02 | forum_thread | https://community.constantcontact.com/ask-the-community/post/do-i-just-quit-BsjcNQse7meIa0T | YvondaL | "7 months ago" | [R-PAGE via Exa] | Q-F-8302 | RC-EXA |
| URL-11A3-03 | CL-02 | blog_post | https://gracecwalker.com/why-i-decided-to-close-my-shopify-ecommerce-fashion-clothing-store-a-reflection-on-challenges-and-lessons-learned/ | Grace C. Walker | 2023-01-22 | [R-PAGE via Exa] | Q-B-8301 | RC-EXA |
| URL-11A3-04 | CL-02 | forum_thread | https://community.shopify.com/t/help-no-sales-on-my-store-getting-frustrated/342203/1 | Tinamarie31094 | 2024-07-24 | [R-PAGE via Exa] | Q-F-8303 | RC-EXA |

Count: 4 URLs appended · 4 Q-## appended to 06-VOC_MASTER.csv (harvester_id 11-AV-03; copy datasets/11-AV-03-minted.csv). Exa returned 4 of ≤10 requested; no page reported unretrievable. Cost ≈ $0.10.
