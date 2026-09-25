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
| URL-01 | COM-05 | youtube_search | https://youtu.be/r0WnKYbcw9k | I Lost Money Dropshipping in India… The Harsh Reality Nobody Shows | RISHAV AGRAWAL | 2026-09-21 | 178 views | — | relevance | views | PH-02 | youtube_transcript | 2 | RC-YTX | FETCHED | [R-SCRAPE] |
| URL-02 | COM-05 | youtube_search | https://youtu.be/x9lgR_iHPuQ | I Lost $1,000 Dropshipping.. So I Tried Again | Jenny Hoyos | ~2022 | 458,125 views | — | relevance | views | PH-02,18 | youtube_transcript | 4 | RC-YTX | FETCHED | [R-SCRAPE] |
| URL-03 | COM-05 | youtube_search | https://youtu.be/OOfML4xMiC4 | I Lost $40,000 Dropshipping and Still Won | Dylan Fisher | ~2026 | 265 views | — | relevance | views | PH-02,20 | youtube_transcript | 6 | RC-YTX | FETCHED | [R-SCRAPE] |
| URL-04 | COM-05 | youtube_search | https://youtu.be/AZIC4HjKj7s | I just lost over $1000 across 3 dropshipping stores | Charlie Nuttall | ~2026 | 188 views | — | relevance | views | PH-02,18 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| URL-05 | COM-05 | youtube_search | https://youtu.be/oS2aafo469M | I Lost Thousands Dropshipping: Don't Make These Mistakes | Alex Ulbin | ~2024 | 11,437 views | — | relevance | views | PH-02,18,20 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| URL-06 | COM-05 | youtube_search | https://youtu.be/83RypPyuXfU | How I lost A Million Dropshipping | Michael Bernstein | ~2023 | 45,811 views | — | relevance | views | PH-02,20 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| URL-07 | COM-05 | youtube_search | https://youtu.be/Cszp_nIwu8I | i lost everything and then became rich with dropshipping | Liam Bradshaw | ~2024 | 55,529 views | — | relevance | views | PH-02 | youtube_transcript | 2 | RC-YTX | FETCHED (partial, output truncated) | [R-SCRAPE] |
| URL-08 | COM-05 | youtube_search | https://youtu.be/iRObd23cn_U | I Lost ₹50,000 on Dropshipping | Tushar Jain | ~2026 | 5,549 views | — | relevance | views | PH-02 | youtube_transcript | 2 | RC-YTX | FETCHED (Hindi, [translated]) | [R-SCRAPE] |
| URL-09 | COM-05 | youtube_search | https://youtu.be/o_eEADR4MY0 | Why I Quit Dropshipping After 4 Years.. (My Story) | Tanner Planes | ~2021 | 50,889 views | — | relevance | views | PH-02,07 | youtube_transcript | 5 | RC-YTX | FETCHED | [R-SCRAPE] |
| URL-10 | COM-05 | youtube_search | https://youtu.be/3d55w3wDSII | I lost ALL of my money Dropshipping...(Biggest Mistakes) | Owen's Bank Account | ~2021 | 267 views | — | relevance | views | PH-02,06 | youtube_transcript | 4 | RC-YTX | FETCHED | [R-SCRAPE] |

### lane: forum_thread (9 URLs: 5 Warrior Forum, 4 Shopify Community)
| url_id | com_id | platform | url | title | op_author | date_posted | engagement_primary | sort_seen | why_chosen | lane | est_records | recipe_id | status | tier_expected |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| URL-11 | COM-03 | forum | https://www.warriorforum.com/social-media/1458034-ive-spent-600on-fb-ads-still-no-sales.html | I've spent $600on FB ads and still no sales... | BluesPlayer | 2022-09-06 | 3 replies opened | top | PH-03 | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-12 | COM-03 | forum | https://www.warriorforum.com/beginners-area/1431345-facebook-ads-no-order.html | Facebook Ads no Order | rb10 | 2021-03-06 | 14 replies total, 3 opened | top | PH-03,19(assumption AS-01) | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-13 | COM-03 | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1214546-massive-traffic-but-no-sales.html | Massive Traffic But No Sales? | Gig Grand | 2016-08-31 | 28 replies total, 3 opened | top | PH-01,05 | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-14 | COM-03 | forum | https://www.warriorforum.com/social-media/1252728-facebook-ads-not-converting-why.html | Facebook Ads Not Converting - Why? | rijichouno | 2017-02-01 | 9 replies | top | PH-03 | forum_thread | 3 | RC-EXA | LISTED | [R-PAGE] |
| URL-15 | COM-03 | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1283825-should-i-hire-marketing-freelancer-freelancer-com.html | Should I hire a Marketing Freelancer from Freelancer.com? | Mysterious Robin | 2017-06-30 | unknown | top | PH-20(assumption AS-01, closest-but-excluded) | forum_thread | 2 | RC-EXA | LISTED | [R-PAGE] |
| URL-16 | COM-02 | forum | https://community.shopify.com/t/ive-got-1-600-session-and-no-sales-and-have-done-everything-right/580410 | I've got 1,600 session and no sales and have done everything right | cozyhomehaven | 2025-12-20 | 376 views, 15 users, 3 replies opened | new | PH-01,09 | forum_thread | 4 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-17 | COM-02 | forum | https://community.shopify.com/t/no-sales-should-i-sell-or-close-my-store/408286 | No Sales – Should I Sell or Close My Store? | Hunter6 | 2025-04-13 | 3 replies opened | new | PH-01,03 | forum_thread | 3 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-18 | COM-02 | forum | https://community.shopify.com/t/google-ads-show-conversions-but-there-arent-any-on-my-store/377195/1 | Google Ads show conversions but there arent any on my store | noah_essentis | 2024-11-27 | 5 replies | new | PH-03 | forum_thread | 3 | RC-EXA | LISTED | [R-PAGE] |
| URL-19 | COM-02 | forum | https://community.shopify.com/t/tiktok-ads-show-conversions-but-shopify-doesnt/258900/8 | TikTok Ads show conversions but shopify doesnt | unknown | 2023-10-12 | unknown | new | PH-03 | forum_thread | 2 | RC-EXA | LISTED | [R-PAGE] |

### lane: quora_answers (9 URLs: 1 FETCHED, 8 LISTED)
| url_id | com_id | url | title | engagement_primary | why_chosen | lane | est_records | recipe_id | status |
|---|---|---|---|---|---|---|---|---|---|
| URL-20 | COM-04 | https://www.quora.com/Why-arent-I-driving-any-sales-on-my-online-Shopify-store-Ive-gotten-32-5k-impressions-367-ad-clicks-and-253-conversions-on-my-store-in-the-past-month-but-not-a-single-sale-Why-is-this | Why aren't I driving any sales on my online Shopify store?... | 87 answers | PH-01,15 | quora_answers | 5 | RC-EXA | FETCHED |
| URL-21 | COM-04 | https://www.quora.com/Why-are-you-not-getting-expected-sales-to-your-Shopify-store | Why are you not getting expected sales to your Shopify store? | unknown | PH-01 | quora_answers | 2 | RC-EXA | LISTED |
| URL-22 | COM-04 | https://www.quora.com/Why-do-sales-not-start-on-my-Shopify-store-I-am-fed-up | Why do sales not start on my Shopify store? I am fed up. | unknown | PH-01,12 | quora_answers | 2 | RC-EXA | LISTED |
| URL-23 | COM-04 | https://www.quora.com/Why-isn-t-my-Shopify-store-getting-any-sales-after-700-online-sessions | Why isn't my Shopify store getting any sales after 700 online sessions? | unknown | PH-01 | quora_answers | 2 | RC-EXA | LISTED |
| URL-24 | COM-04 | https://www.quora.com/How-do-I-become-successful-in-dropshipping-I-ve-tried-multiple-courses-that-failed-to-work-I-ve-lost-4000-I-m-17-y-o-making-10-an-hour-I-gave-it-up-a-couple-of-weeks-ago-but-I-just-feel-like-I-wasted-4000-for | ...I've lost $4000... I gave it up... wasted $4000 for nothing | unknown | PH-02,18 | quora_answers | 2 | RC-EXA | LISTED (retrieved:false on targeted open attempt) |
| URL-25 | COM-04 | https://www.quora.com/Is-dropshipping-a-scam-It-seems-way-too-good-to-be-true-How-can-someone-make-money-without-owning-any-products | Is dropshipping a scam? ... | unknown | PH-10 | quora_answers | 2 | RC-EXA | LISTED |
| URL-26 | COM-04 | https://www.quora.com/Is-drop-shipping-a-scam-and-how-do-I-start | Is drop shipping a scam, and how do I start? | 43 answers | PH-10 | quora_answers | 2 | RC-EXA | LISTED |
| URL-27 | COM-04 | https://www.quora.com/Is-Dropshipping-really-a-scam-to-convince-people-to-buy-expensive-courses-Sell-courses | Is Dropshipping really a scam to convince people to buy expensive courses? | unknown | PH-10 | quora_answers | 2 | RC-EXA | LISTED |
| URL-28 | COM-04 | https://www.quora.com/How-many-people-actually-make-profit-dropshipping | How many people actually make profit dropshipping? | 42 answers | PH-16 | quora_answers | 2 | RC-EXA | LISTED |

### lane: blog_comments (4 URLs, all FETCHED)
| url_id | com_id | url | title | op_author | date_posted | why_chosen | lane | est_records | recipe_id | status | tier_expected |
|---|---|---|---|---|---|---|---|---|---|---|---|
| URL-29 | COM-09 | https://revenueamplify.com/lost-1000-dropshipping-but-im-not-giving-up/ | Lost $1,000 Dropshipping - But I'm Not Giving Up | anonymous | 2024-02-01 | PH-02,18 | blog_comments | 2 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-30 | COM-09 | https://www.salehoo.com/ethan-dobbins-success-story | Ethan Dobbins Dropshipping Success Story | Sean Leonardia (interviewer) | 2026-07-08 | PH-02,18 | blog_comments | 2 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-31 | COM-09 | https://nicojannasch.com/going-all-in-when-youre-broke/ | When You're a Broke Entrepreneur | Nico Jannasch | 2016-06-19 | PH-02,18 | blog_comments | 1 | RC-EXA | FETCHED | [R-PAGE via Exa] |
| URL-32 | COM-09 | http://kblee007.blogspot.com/2018/02/3-tips-for-succeeding-after-you-fail.html | 3 Tips For Succeeding After You Fail | Unknown (page byline) | 2018-02-21 | PH-02,06 | blog_comments | 1 | RC-EXA | FETCHED | [R-PAGE via Exa] |

### lane: reddit_post+comments — 0 URLs (BLOCKED, see §11)

Counter (final): URL 32/12 floor · reddit 0/5 **PARTIAL** · CP-03 URLs: 16 (all youtube+blog + PH-02/18-tagged forum/quora) ≥4 met · CP-05 URLs: 4 (URL-06,09,12,15) ≥4 met (thin) · platforms 5 (youtube_search, forum×2-communities, quora, blog_comments) · Σest PB-06 = 92 (well above 1.5×40=60) → **PLAN-VALIDATED** · Σest CP-03 ≈ 55 (above 1.5×25=37.5) → **PLAN-VALIDATED** · Σest CP-05 ≈ 12 (below 1.5×25=37.5) → **PLAN-THIN** · plan cost $0.425 Exa + ~14 TranscriptAPI credits, well under PB-06 share of standard $8 harvest cap ÷3≈$2.67.

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
| HV-PB-06 | PB-06 | [CP-03, CP-05] | URL-02,05,06,04,09,10,03,08,01,07 (youtube, ranked by views desc within relevance) then URL-11,12,13,16,17,14,18,15,19 (forum) then URL-20,26,22,21,23,24,25,27,28 (quora) then URL-29,30,31,32 (blog) | RC-YTX, RC-EXA | records≥40, CP-03≥25, CP-05≥25 (PARTIAL likely, see PLAN-THIN §2) | 06-partials/06-VOC_MASTER.PB-06.csv | 8 |

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
| U-01..U-10 | youtube_transcript | COM-05 | 2016-2026 (upload dates) | 35 | full transcript text, author, upload date, view count | none — public captions/ASR | — |
| U-11..U-19 | forum_thread | COM-02, COM-03 | 2016-2025 | 26 | OP+reply text, author, date, URL (via Exa) | 4 of 9 not opened in full (LISTED only, time box) | — |
| U-20..U-28 | quora_answers | COM-04 | unknown-2025 | 21 | question title always; full answers only for URL-20 | 7 of 9 not opened in full; 1 targeted open failed (EX-01) | page could not be retrieved |
| U-29..U-32 | blog_comments | COM-09 | 2016-2026 | 6 | full post text, author, date, URL (via Exa) | none | — |

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
