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
| URL-01 | COM-14 | PB-01 | — | forum | https://community.shopify.com/t/shopify-by-adrian-morrison/215810 | Shopify by Adrian Morrison (free DFY store, scam complaints) | UNKNOWN | UNKNOWN (page 2 exists) | ~20+ (est. from page count) | — | top | 1 | PH-06,PH-11 | forum_thread | 8 | RC-WEB | LISTED | [R-PAGE] | — | Strongest single on-topic thread found; title+URL seen via WebSearch, not yet opened for text. |
| URL-02 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/is-there-a-simple-way-to-understand-shopify/192077 | Is there a simple way to understand Shopify? | UNKNOWN | UNKNOWN | ~23 (reply /23 seen) | — | top | 2 | PH-01,PH-03 | forum_thread | 8 | RC-WEB | LISTED | [R-PAGE] | — | Multiple reply-numbered URLs (/15,/20,/23) seen in search results. |
| URL-03 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/shopify-seems-pretty-complicated/568388 | Shopify seems pretty complicated | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 3 | PH-03 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | |
| URL-04 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/shopify-is-very-confusing-and-very-hard-to-setup/350760 | shopify is very confusing and very hard to setup | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 4 | PH-03 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | |
| URL-05 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/building-your-shopify-store-what-is-the-biggest-problem-you-encountered/133383 | BUILDING YOUR SHOPIFY STORE? Biggest problem encountered? | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 5 | PH-09 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | Direct problem-elicitation thread. |
| URL-06 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/what-s-one-thing-you-wish-you-knew-before-launching-your-first-shopify-store/578902 | One thing you wish you knew before launching first Shopify store | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 6 | PH-09 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | |
| URL-07 | COM-01 | PB-01 | CP-01 | forum | https://community.shopify.com/t/is-anyone-else-struggling-with-adrian-morrisons-free-store-build/310831 | Is anyone else struggling with Adrian Morrison's free store build | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 7 | PH-05,PH-11 | forum_thread | 6 | RC-WEB | LISTED | [R-PAGE] | — | "misleading expectations — believed someone would build a complete store for them" — directly names PB-01's exact struggle. |
| URL-08 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/i-received-proposal-from-someone-to-make-shopify-for-me/287432 | I received proposal from someone to make Shopify for me | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 8 | PH-06 | forum_thread | 5 | RC-WEB | LISTED | [R-PAGE] | — | |
| URL-09 | COM-01 | PB-01 | CP-01 | forum | https://community.shopify.com/t/can-i-hire-a-trusted-professional-to-build-my-new-store/128838 | Can I hire a trusted professional to build my new store? | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 9 | PH-06 | forum_thread | 5 | RC-WEB | LISTED | [R-PAGE] | — | |
| URL-10 | COM-01 | PB-01 | — | forum | https://community.shopify.com/t/shopifys-website-builder-is-garbage-and-our-business-is-suffering-almost-wish-i-never-switched/161168 | Shopify's website builder is garbage and our business is suffering | UNKNOWN | UNKNOWN | UNKNOWN | — | top | 10 | PH-04,PH-07 | forum_thread | 5 | RC-WEB | LISTED | [R-PAGE] | — | |
| URL-11 | COM-02 | PB-01 | — | forum | https://community.shopify.dev/t/where-to-start-super-overwhelmed-first-time-using-shopify/7804 | Where to start?! Super overwhelmed. First time using Shopify | UNKNOWN | 2025-02-08 | 4 comments | — | top | 11 | PH-01,PH-03 | forum_thread | 4 | RC-WEB | LISTED (Exa-opened) | [R-PAGE via Exa] | — | Exa opened and quoted this thread directly. |
| URL-12 | COM-03 | PB-01 | — | forum | https://community.etsy.com/t5/Technical-Issues/Stuck-on-How-you-ll-get-paid-step-when-opening-a-new-shop/td-p/146362398 | Stuck on "How you'll get paid" step when opening a new shop | UNKNOWN | 2024-08-20 | UNKNOWN (replies gated) | — | top | 12 | PH-02 | forum_thread | 2 | RC-WEB | LISTED (partial, Exa-opened) | [R-PAGE via Exa] | — | Replies behind login wall — OP text only. |
| URL-13 | COM-04 | PB-01 | — | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1510729-guidance-needed-etsy-ebay-account-setup.html | Guidance Needed for Etsy & eBay Account Setup | UNKNOWN | 2025-09-05 | 4 replies | — | top | 13 | PH-02 | forum_thread | 3 | RC-WEB | LISTED (Exa-opened) | [R-PAGE via Exa] | — | |
| URL-14 | COM-05 | PB-01 | — | facebook_group | https://www.facebook.com/groups/282038432287765/posts/296994287458846/ | "Okay so before I freak out or get angry..." | UNKNOWN | UNKNOWN (2026) | UNKNOWN | — | top | 14 | PH-01 | fb_post_comments | 5 | RC-FBC | LISTED (Exa-opened) | [R-PAGE via Exa] | — | 22K-member group; only this 1 post opened. |
| URL-15 | COM-09 | PB-01 | CP-05 | trustpilot | https://www.trustpilot.com/review/ecomxpertz.com | Ecomxpertz Reviews | UNKNOWN | UNKNOWN | UNSIZED (count not shown) | — | recent | 15 | PH-06,PH-23 | trustpilot_balanced | 10 | RC-TP | LISTED (snippet only — page BLOCKED-ON-TOOL to open) | [R-SNIPPET] | — | Snippet already carries 2 verbatim fragments (1 positive, 1 negative $4,000-complaint) — usable as [R-SNIPPET] pending page access. |
| URL-16 | COM-11 | PB-01 | CP-05 | trustpilot | https://www.trustpilot.com/review/nn-dfysuccess.com | DONE FOR YOU® Reviews | UNKNOWN | UNKNOWN | 3 reviews | — | recent | 16 | PH-06,PH-21 | trustpilot_balanced | 3 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | "$69 and $169 paid, limited support, no sales in a month" fragment on record. |
| URL-17 | COM-07 | PB-01 | — | trustpilot | https://www.trustpilot.com/review/ecomdoneforyou.com | Ecom Done For you Reviews | UNKNOWN | UNKNOWN | 10 reviews | — | recent | 17 | PH-06 | trustpilot_balanced | 4 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | NW-SEED-01. |
| URL-18 | COM-08 | PB-01 | — | trustpilot | https://www.trustpilot.com/review/ecommerceparadise.com | Ecommerce Paradise Reviews | UNKNOWN | UNKNOWN | 22 reviews | — | recent | 18 | PH-06 | trustpilot_balanced | 9 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | NW-SEED-02. |
| URL-19 | COM-10 | PB-01 | — | trustpilot | https://www.trustpilot.com/review/doneforyoustrategy.com | Done For You LLC Reviews | UNKNOWN | UNKNOWN | 8 reviews | — | recent | 19 | PH-06 | trustpilot_balanced | 3 | RC-TP | LISTED (snippet) | [R-SNIPPET] | — | RESERVE seed. |
| URL-20 | COM-12 | PB-01 | — | youtube_search | https://www.youtube.com/watch?v=6MKO7iAtiAE | I PAID FIVERR EXPERTS To Run My WHOLE Dropshipping Business In 2023 | THE ECOM KING | ~3yr ago | 366132 views | UNKNOWN comments | most_liked | 20 | PH-06 | youtube_transcript | 3 | RC-YTX | LISTED | [R-TOOL] | — | Genuinely first-person "paid someone" DFY narrative; caption availability UNKNOWN — to confirm in 06. |
| URL-21 | COM-12 | PB-01 | — | youtube_search | https://www.youtube.com/watch?v=rhuYy9LP72M | I Tried Shopify Dropshipping For 7 Days (Realistic Results) | Mark Tilbury | 4mo ago | 3954792 views | hasCaptions:true | most_liked | 21 | PH-06,PH-01 | youtube_transcript | 3 | RC-YTX | LISTED | [R-TOOL] | — | Captions confirmed available. |
| URL-22 | COM-13 | PB-01 | — | blog_comments | https://painonsocial.com/blog/shopify-problems-reddit | 7 Most Common Shopify Problems Found on Reddit | UNKNOWN | UNKNOWN | UNKNOWN | — | — | 22 | PH-15 | blog_comments | 6 | RC-EXA | LISTED (snippet; queued for Exa medium open in 06) | [R-SNIPPET] → [R-PAGE via Exa] pending | — | Aggregates Reddit language in an openable (non-Reddit) page — priority Exa target for 06. |
| URL-23 | — | PB-01 | CP-05 | blog_comments | https://kingy.ai/news/buildyourstore-ai-review-2026-is-this-free-ai-shopify-store-builder-worth-your-time/ | BuildYourStore.ai Review (2026) | UNKNOWN | 2026 | UNKNOWN | — | — | 23 | PH-10,PH-21,PH-22 | blog_comments | 4 | RC-EXA | LISTED (snippet) | [R-SNIPPET] | — | Names CP-05 directly ("aspiring entrepreneurs...intimidated by the technical lift"). |
| URL-24 | — | PB-01 | — | forum | (reddit — no URL surfaced) | site:reddit.com shopify overwhelmed can't figure out | — | — | — | — | — | 24 | PH-01 | reddit_post+comments | 0 | RC-RD | QUERY-ONLY → BLOCKED | — | — | 0 of 22 WebSearch queries this leg surfaced an actual reddit.com URL (community.shopify.com dominates results); Reddit not retrievable by any tool. OPERATOR-PASTE row: operator should paste r/shopify or r/ecommerce thread URLs matching "can't figure out shopify" / "shopify setup overwhelming" if available. |
| URL-25 | — | PB-01 | — | forum | (reddit — no URL surfaced) | site:reddit.com "paid someone" build shopify store for me | — | — | — | — | — | 25 | PH-06 | reddit_post+comments | 0 | RC-RD | QUERY-ONLY → BLOCKED | — | — | Same as URL-24. OPERATOR-PASTE row: operator should paste any r/shopify/r/dropshipping thread on paying someone to build a store. |

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

**RC-WEB** (forum_thread; would-be, Apify BLOCKED-ON-TOOL — printed for operator) · `apify/website-content-crawler` · input: `{"startUrls":[{"url":"<thread>"}, ...URL-01..URL-13...], "crawlerType":"cheerio","maxCrawlDepth":0,"maxCrawlPages":30,"htmlTransformer":"readableTextIfPossible","removeElementsCssSelector":"nav, footer, script, style, noscript, svg, [role=\"dialog\"]","saveMarkdown":true,"proxyConfiguration":{"useApifyProxy":true}}` · expected_rows: ~13 pages · unit_price: compute-only ≈$0.001-0.003/page · est_cost: $0.03 · output_field_map: text→markdown body, author→UNKNOWN (not exposed by this crawler), date→UNKNOWN, score→UNKNOWN, url→loadedUrl, parent_title→pageTitle · fallback_chain: [`apify/rag-web-browser` raw-http → this run's actual substitute: `mcp__Readymerce_Exa__agent_run` effort medium on the same URL] · no_apify_path: Exa agent_run (WORKING, used in 06).

**RC-FBC** (fb_post_comments; would-be) · `apify/facebook-comments-scraper` · input: `{"startUrls":[{"url":"https://www.facebook.com/groups/282038432287765/posts/296994287458846/"}],"resultsLimit":40,"includeNestedComments":false,"viewOption":"RANKED_UNFILTERED"}` · expected_rows: ≤40 · unit_price: $0.002/comment · est_cost: $0.08 · output_field_map: text→text, author→author.name, date→date, score→likesCount, url→commentUrl, parent_title→postText · fallback_chain: [`memo23/facebook-comments-scraper` → `dz_omar/facebook-comment-scraper` → Exa agent_run on the post URL] · no_apify_path: Exa agent_run.

**RC-TP** (trustpilot_balanced; would-be) · `memo23/trustpilot-scraper-ppe` · input: `{"startUrls":["ecomdoneforyou.com","ecommerceparadise.com","ecomxpertz.com","doneforyoustrategy.com","nn-dfysuccess.com"],"maxItems":100,"filterLanguages":["en"],"filterStars":[],"sampling":"balanced","sortBy":"recent","filterDateRange":"last12months","expandRegionalDomains":false,"scrapeAllReviews":false,"includeStats":true,"reviewInsights":true,"splitDatasets":false,"flattenCompanyData":true}` · expected_rows: ~29 (10+22+UNSIZED+8+3, capped) · unit_price: $0.00065/review + $0.02 insights · est_cost: $0.12 · output_field_map: text→text, author→consumer.displayName, date→dates.publishedDate, score→rating, url→reviewUrl, parent_title→companyName · fallback_chain: [`automation-lab/trustpilot` → page fetch `https://www.trustpilot.com/review/<domain>` → Exa agent_run] · no_apify_path: Exa agent_run (page not retrievable by Exa either per ADDENDUM — falls through to OPERATOR-PASTE).

**RC-YTX** (youtube_transcript; **WORKING, runs in 06**) · `mcp__TranscriptAPI__get_youtube_transcript` · input per video: `{"video_url":"<url>","format":"text","include_timestamp":true,"send_metadata":true}` · expected_rows: 1 transcript/video, coded into multiple Q-Y records · cost: TranscriptAPI credits (≤45 leg budget) · output_field_map: text→transcript segments, author→channelTitle (from search_youtube), date→publishedTimeText, url→video_url · fallback_chain: [`mcp__TranscriptAPI__get_youtube_video_info` to check caption languages first → skip if no captions] · no_apify_path: n/a, native tool.

**RC-EXA** (forum_thread/blog_comments/quora_answers verbatim extraction; **WORKING, runs in 06**) · `mcp__Readymerce_Exa__agent_run` · effort: medium · query template: "Open <URL> (or: search for and open the most relevant page(s) for <PH-##> on <domain/platform>) and return VERBATIM passages only — each with the exact page URL you opened, the author/handle as shown, and the date as shown. Do not paraphrase, do not merge separate comments, say explicitly if a page could not be retrieved. Use outputSchema: {passages:[{quote, author, date, url, platform}]}." · expected_rows: 3-8 passages/run · unit_price: ≈$0.03-0.10/run (effort-dependent) · est_cost: budgeted inside the $2.60 leg-wide Exa cap · fallback_chain: [effort low retry → mark BLOCKED with OPERATOR-PASTE row] · no_apify_path: n/a, native tool.

**RC-RD** (reddit_post+comments; would-be, and this run's actual status = BLOCKED-ON-TOOL, no fallback reached) · `harshmaur/reddit-comments-scraper` · input: `{"postUrls":[],"maxCommentsPerPost":40,"includeNSFW":false,"aiAnalysis":false}` · status this leg: no Reddit URL was ever surfaced by WebSearch or Exa to populate `postUrls[]` · fallback_chain: [`clearpath/reddit-post-comments-bulk-scraper` → `old.reddit.com/<post>/.json` via rag-web-browser (Apify BLOCKED) → browser (Browserbase BLOCKED, 401) → OPERATOR-PASTE] — all links in the chain BLOCKED-ON-TOOL this run; the URL-24/URL-25 OPERATOR-PASTE rows in §2 are the result.

## §6 HARVESTER ASSIGNMENTS

**HV-PB-01** (this agent, VOC-PB-01) · pb_id: PB-01 · cp_ids: [CP-01, CP-05] (CP-01 as an `HV-CP-01` task inside this harvester — its URL coverage is thin, see §2 rank 7 and 9 only) · url_ids (rank order): URL-01, URL-02, URL-03, URL-04, URL-05, URL-06, URL-07, URL-08, URL-09, URL-10, URL-11, URL-12, URL-13, URL-14, URL-15, URL-16, URL-17, URL-18, URL-19, URL-20, URL-21, URL-22, URL-23 (URL-24, URL-25 BLOCKED, not mined) · recipe_ids: [RC-WEB(printed only), RC-FBC(printed only), RC-TP(printed only), RC-YTX(RUNS), RC-EXA(RUNS), RC-RD(BLOCKED)] · floors: per §1 · partial_file: `06-partials/06-VOC_MASTER.PB-01.csv` · max_extra_sources: 8.

**HV-CP-01** (task inside HV-PB-01, CP-01 thin — 0 VALIDATED-PRESENT communities from 04) · url_ids: URL-07, URL-09 (the only rows tagged CP-01) · task: Step 3(a) population-first pass in 06 — additional WebSearch/Exa queries on "<CP-01 situation word> <PB-01 plain word>" before declaring PARTIAL.

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
| SM-01..13 | forum_thread | community.shopify.com / community.shopify.dev / community.etsy.com / warriorforum.com threads (URL-01..13) | mixed 2024-2026 | ~4-8 each | title, OP text, some reply counts; author/date mostly UNKNOWN pre-open | 1 partial login wall (Etsy) | — |
| SM-14 | fb_post_comments | Shopify/Dropshipping Warriors FB group post | 2026 | ~5 | text, comments (unopened) | group itself PUBLIC, only 1 post opened | 4 of target 5 groups not found/walled |
| SM-15..19 | trustpilot_balanced | 5 competitor/reserve Trustpilot pages | last 12mo (assumed) | ~3-10 each from snippet | review counts + 2-3 verbatim fragments only | page BLOCKED-ON-TOOL to open in full | — |
| SM-20..21 | youtube_transcript | 2 YouTube videos (URL-20,21) | 2023, 2026 | 1 transcript each → several Q-Y records | full transcript if captioned | 1 of 2 caption status UNKNOWN pre-check | — |
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

COVERAGE: URL 23/60 (LISTED 21 · QUERY-ONLY 0 · BLOCKED 2 · OPERATOR-PASTE 2) · PB below URL floor: [NONE — PB-01's own scoped floor of 12 across ≥3 platforms is met with 23 across 6 lanes] · CP THIN: [CP-01 (2 URLs, below its ≥4 floor)] · PLAN-VALIDATED: [PB-01 (raw Σest), CP-05 (close, 26/37.5)] · PLAN-THIN: [CP-01 (11/37.5)] · plan cost $0.05/$2.67 (this PB's share of the $8 standard harvest cap) · weakest link: Reddit is fully BLOCKED-ON-TOOL and was never even discoverable via WebSearch this run (0 reddit.com URLs surfaced across 22 queries) — the URL-24/URL-25 OPERATOR-PASTE rows are the only path to closing the ≥5-Reddit-thread floor. · what closing it would cost: an Apify billing-cycle reset to run `harshmaur/reddit-scraper` ($0.0018/result) plus `harshmaur/reddit-comments-scraper` ($0.0015/comment) across the 3-subreddit floor, ≈$5-15 total, or 2-3 operator-pasted Reddit thread URLs/texts mined by hand in 06.

**Continuing straight into STEP 06 with SCOPE: PB-01 (same session, same agent).**
