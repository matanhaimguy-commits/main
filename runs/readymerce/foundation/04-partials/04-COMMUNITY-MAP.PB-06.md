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
| COM-01 | PB-06 | ALL | reddit | r/dropshipping, r/Entrepreneur, r/shopify (named from operator/model memory only) | reddit.com/r/dropshipping etc. | UNKNOWN | subscribers | NULL | NULL | NULL | NULL | NULL | problem_discussion | PUBLIC (believed) | none opened | [D] mixed hobbyist/aspiring sellers | HYPOTHESIS-excluded | **HYPOTHESIS — named from memory, nothing fetched (Apify hard limit + WebFetch egress 403); excluded from every counter** |
| COM-02 | PB-06 | ALL,CP-05 | forum | Shopify Community (community.shopify.com) | https://community.shopify.com | UNKNOWN (no forum-wide count shown) | records | [R-PAGE via Exa] | 2026-09-24 | ≥1 (Dec 2025 & Apr 2025 threads opened) | 3 (median of first 3 replies read per thread) | 2025-12-20 | problem_discussion | PUBLIC | PH-01,03,04,05,09,10 | [D] new/struggling store owners, mixed age, mostly solo operators | 1 | VALIDATED — 5 threads found via WebSearch, 2 opened in full via Exa (OP+3 replies each, real usernames+dates+URLs) |
| COM-03 | PB-06 | ALL,CP-05 | forum | Warrior Forum (warriorforum.com) — ecommerce/beginners/social-media subforums | https://www.warriorforum.com | UNKNOWN | records | [R-PAGE via Exa] | 2026-09-24 | 0 (all 3 opened threads are 2016-2022, no <7d activity) | 3 (median of first 3 replies read, all 3 threads) | 2022-09-06 (newest opened) | problem_discussion | PUBLIC | PH-01,03,04,09 | [D] longtime solo marketers/affiliates, DIY-first culture | 2 | VALIDATED — 3 threads opened in full (OP+3 replies each, real usernames+dates+URLs); LOW-ACTIVITY (no thread <7d old) |
| COM-04 | PB-06 | ALL,CP-03 | quora | Quora dropshipping/Shopify-sales questions | https://www.quora.com | UNKNOWN | answers | [R-PAGE via Exa] | 2026-09-24 | NULL | 87 (top question's answer count) | 2025-04-22 (newest question opened) | problem_discussion,solution_seeking | PUBLIC | PH-01,15,18 | [D] mix of sufferers asking + marketers/experts answering | 3 | VALIDATED — 9 question pages listed (titles+answer counts), 1 opened in full (4 verbatim answers); 1 of 2 targeted opens failed to retrieve |
| COM-05 | PB-06 | CP-03 | youtube_search | YouTube "I lost money dropshipping" / "quit dropshipping" / "$X ads zero sales" first-person videos | https://www.youtube.com | 20+ videos per query page (5 query pages read) | videos_for_phrase | [R-TOOL] (TranscriptAPI search) + [R-SCRAPE] (10 transcripts fetched) | 2026-09-24 | several <7d (e.g. r0WnKYbcw9k "3 days ago") | NULL (no comment counts pulled — comments lane BLOCKED, see §8) | 2026-09-21 (r0WnKYbcw9k) | problem_discussion,post_purchase_review | PUBLIC | PH-02,06,08,14,18,20 | [D] mostly male 18-35 solo drop-shippers, some agency/mentorship buyers | 1 | VALIDATED — 10 transcripts fetched in full (8 usable English, 1 Hindi partially translated, 1 truncated-but-read); views 178–2.3M, 8 distinct channels |
| COM-06 | PB-06 | ALL | tiktok_search | TikTok dropshipping-fail search | tiktok.com | UNKNOWN | UNSIZED | NULL | NULL | NULL | NULL | NULL | problem_discussion | PUBLIC (believed) | none | [D] younger (16-25), high emotional/comedic framing per 01 quality flags | — | **UNSIZED — method: clockworks/tiktok-scraper (Apify, BLOCKED-ON-TOOL: monthly hard limit)** |
| COM-07 | PB-06 | CP-05 | trustpilot | Trustpilot pages for ecomdoneforyou.com, ecommerceparadise.com, ecomxpertz.com, readymerce.com | trustpilot.com/review/<domain> | UNKNOWN | reviews | NULL | NULL | NULL | NULL | NULL | post_purchase_review | PUBLIC (believed) | none | [D] buyers/complainants of DFY sellers | — | **BLOCKED-ON-TOOL — Trustpilot pages not retrievable by any connected tool (Apify hard limit; Exa tried in a prior wave and reported "could not be retrieved" per ADDENDUM); recipe pinned in 05 §5 for operator to run later** |
| COM-08 | PB-06 | ALL | facebook_group | Dropshipping support / "failed my first store" FB groups | facebook.com/groups/... | UNKNOWN | members | NULL | NULL | NULL | NULL | NULL | problem_discussion | PUBLIC/PRIVATE mixed (believed) | none | [D] | — | **NULL — searched: [none run] — Apify facebook-groups-scraper BLOCKED-ON-TOOL, no browser tool connected** |
| COM-09 | PB-06 | CP-03 | blog_comments | Personal recovery/failure blogs (dropshipping "I lost $X" first-person posts) | revenueamplify.com/lost-1000-dropshipping-but-im-not-giving-up/ · salehoo.com/ethan-dobbins-success-story · nicojannasch.com/going-all-in-when-youre-broke/ · kblee007.blogspot.com/2018/02/3-tips-for-succeeding-after-you-fail.html | 4 posts | records | [R-PAGE via Exa] | 2026-09-24 | NULL (static blog posts, not threads) | 0 (no comment sections opened) | 2024-02-01 (newest) | post_purchase_review,problem_discussion | PUBLIC | PH-02,18 | [D] solo male entrepreneurs recounting a specific loss-then-retry arc | 4 | VALIDATED — 4 first-person "lost money, tried again" blog posts opened and summarized with URL+author/date by Exa |
| COM-10 | PB-06 | ALL | amazon_listing | N/A — PB-06 is a service-failure problem (zero sales/failed DIY attempt), not a product category with same-function Amazon listings | — | — | — | — | — | — | — | — | — | — | — | — | **NOT APPLICABLE — no same-function product category maps to this PB; Amazon lane skipped for PB-06 (methodological, not a tool block)** |

Counter: COM 7/4 floor met (VALIDATED 5 · SUPPORTED 0 · HYPOTHESIS 1-excluded · BLOCKED/NULL/N-A 3) · platforms VALIDATED: forum×2, quora, youtube_search, blog_comments = **4 distinct platform types** (floor ≥3 met) · CP-03 communities ≥2 met (COM-04,05,09) · CP-05 communities: COM-02,03 only (population_tags weak — see §4).

## §4 · POPULATION PRESENCE (CP-## × COM-##)

| cp_id | com_id | label | cited_thread_urls | marker_phrase |
|---|---|---|---|---|
| CP-03 | COM-05 (youtube_search) | VALIDATED-PRESENT | https://youtu.be/x9lgR_iHPuQ · https://youtu.be/OOfML4xMiC4 · https://youtu.be/AZIC4HjKj7s · https://youtu.be/oS2aafo469M · https://youtu.be/83RypPyuXfU · https://youtu.be/o_eEADR4MY0 · https://youtu.be/3d55w3wDSII (7 distinct authors) | "I've already lost 500 drop shipping" / "I've tried Drop Shipping on and off for like 7 years" / "I just lost over $1,000 across 3 dropshipping stores" |
| CP-03 | COM-09 (blog_comments) | VALIDATED-PRESENT | https://revenueamplify.com/lost-1000-dropshipping-but-im-not-giving-up/ · https://www.salehoo.com/ethan-dobbins-success-story | "Lost $1,000 Dropshipping — But I'm Not Giving Up" / lost ~$2,000 on first e-commerce store, poorly structured, weak offers |
| CP-03 | COM-04 (quora) | EARLY SIGNAL | https://www.quora.com/How-do-I-become-successful-in-dropshipping-I-ve-tried-multiple-courses-that-failed-to-work-I-ve-lost-4000... | question title itself: "I've lost $4000... I just feel like I wasted $4000 for nothing" (page not retrievable to confirm answers, question text only) |
| CP-05 | COM-05 (youtube_search) | EARLY SIGNAL | https://youtu.be/83RypPyuXfU | "hire an agency to do the store for you to do the ads for you... and to do the customer service for you" (Michael Bernstein, describing why NOT to do this — still shows the population exists) |
| CP-05 | COM-03 (warriorforum) | NOT FOUND — searched: ["someone who tried building/running their own store then wished they could pay someone else to build & run it", "I hired an agency to build my dropshipping store so I didn't have to do it myself"] | — | closest was a poster asking "is hiring a marketing freelancer worth it" — does not express wanting to skip the *build*, only the ads |

## §5 · POND-PB-06

| cell | value | tier | date |
|---|---|---|---|
| subreddit_subscribers_sum | UNSIZED — method: apify/rag-web-browser on old.reddit.com/r/<sub>/about.json (BLOCKED-ON-TOOL: Apify hard limit) | — | — |
| fb_top5_members_sum | UNSIZED — method: apify/facebook-groups-scraper (BLOCKED-ON-TOOL) | — | — |
| amazon_top3_reviews_sum | N/A — no Amazon lane for this PB (§3 COM-10) | — | — |
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
| PB-06 | 8 (COM-02,03,04,05) | 3 (Quora answers, Warrior Forum advice replies) | 0 | 0 | 4 (COM-09 blog posts + YouTube post-mortems) | 0 (no competitor ad with visible comments opened this step — LATE-BOUND: 02.share_url) | 0 | **Y** (≥1 problem_discussion, ≥1 post_purchase_review both met) |

## §7 · ASSUMPTION LIST (AS-##)

`LATE-BOUND: 03.AS-##` — 03-HANDOFF.json does not exist this run (03 has not completed in this wave). Only the one derivable-from-01 row is seeded below per §4.5 ("one per CP-## with named_by_competitor"); the rest of the list ships once 03 exists (06-MERGE or 07 runs the full assumption check).

| as_id | source_id | claim (verbatim) | type | communities_to_check | status |
|---|---|---|---|---|---|
| AS-01 | CP-05 | "Aspiring E-Commerce Entrepreneurs" (NW-SEED-02 / Ecommerce Paradise PR framing, [R-SNIPPET]) — the market contains people who already tried and now want the build skipped for them | avatar | COM-02, COM-03, COM-05 | UNCHECKED (searched this step: EARLY SIGNAL only — see §4 CP-05 row) |

## §8 · BIAS + ACCESS ROW

- Reddit (COM-01): NULL — searched: ["shopify store no sales reddit", "tried dropshipping lost money reddit", "dropshipping horror stories reddit lost money", "quit dropshipping after losing money reddit"] — every WebSearch call for these queries returned Shopify Community / Warrior Forum / Quora / Trustpilot / teamblind.com URLs, never a reddit.com URL directly, and no reddit.com page could be opened by any tool (egress 403 + Apify hard limit + Exa "cannot retrieve" per ADDENDUM). Reddit is the single largest gap in this map.
- TikTok (COM-06), Facebook (COM-08), Trustpilot (COM-07): all UNSIZED/NULL/BLOCKED per §3 — Apify hard limit removes every scraper lane; no browser tool is connected this run.
- Skews named: (1) platform demographics — Warrior Forum skews older/longtime solo marketers (threads from 2016-2022), Shopify Community and YouTube skew newer entrants (2024-2026), so the corpus over-represents both extremes of experience and under-represents the middle; (2) extreme users post more — YouTube creators who "lost $40k" or "$1M" self-select for dramatic framing (monetized storytelling), likely overstating typical loss size; (3) public commenters differ from silent buyers — everyone in this corpus is still publicly active/posting, which by construction excludes people who quit silently and never speak of it again (the single largest population per Charlie Nuttall's own observation: "a lot of the people at the top aren't showing it... loads of people was going through the exact same thing"); (4) search-index bias — WebSearch and Exa surface Google-indexed, SEO-friendly platforms (Shopify's own community forum, Quora, blogs) far more readily than closed/algorithmic platforms (Reddit, TikTok, Facebook groups), which is a structural under-count of exactly the platforms named in 01's `lane_search_terms[]`.

## §9 · HARVEST BUDGET ESTIMATE

| com_id | lane | actor | est_rows | est_cost |
|---|---|---|---|---|
| COM-02 | forum_thread | Exa agent (medium, verbatim extraction) | ~15 records (2 threads × OP+3 replies + follow-ups) | $0.10 (1 run, already spent in 06) |
| COM-03 | forum_thread | Exa agent (medium) | ~12 records (3 threads × OP+3 replies) | $0.10 (1 run, already spent in 06) |
| COM-04 | quora_answers | Exa agent (medium) | ~5 records (1 question + 4 answers) | $0.10 (1 run, already spent in 06) |
| COM-05 | youtube_transcript | TranscriptAPI get_youtube_transcript | ~35-40 records (8 usable videos × 4-5 passages) | ~10 credits (already spent) |
| COM-09 | blog_comments (blog posts) | Exa agent (low, discovery only — no further extraction run) | 4 posts summarized, not deep-mined further | $0.025 (already spent) |
| COM-06,07,08 | tiktok_comments / trustpilot_balanced / fb_post_comments | Apify (pinned recipe cards for operator, see 05 §5) | 0 this run | $0.00 — BLOCKED-ON-TOOL |
Sum this step: Exa ≈ $0.425 (5 runs) + TranscriptAPI ≈ 14 credits (4 search pages + 10 transcripts) vs PB-06 share of standard $6 map cap ÷3 ≈ $2.00 → **under cap**.

## §10 · COVERAGE STATEMENT

Every size in §3/§5 is read from a fetched page (Exa) or a tool call (TranscriptAPI), never from memory; population presence in §4 is cited to real thread/video URLs, never claimed from a community's name alone; speaker mix is marked `[D]`; COM-01 (Reddit) and COM-06/07/08 (TikTok/Trustpilot/Facebook) are BLOCKED-ON-TOOL or NULL and listed as such, never invented.

COVERAGE: COM 7 (VALIDATED 5 · SUPPORTED 0 · HYPOTHESIS 1) · platforms 4/9 (forum×2, quora, youtube_search, blog_comments; reddit/tiktok/trustpilot/facebook/amazon blocked or n/a) · PB below floor: NONE (COM ≥4, PH ≥8 both met) · CP NOT FOUND: NONE (CP-03 VALIDATED-PRESENT, CP-05 EARLY SIGNAL/NOT FOUND-on-one-lane, both kept) · walled 0 · Reddit usable rate 0% (0 reddit.com pages retrievable by any tool this run) · cost $0.425 Exa + ~14 TranscriptAPI credits · AS: 1 row (LATE-BOUND: 03.AS-## for the rest) · weakest link: Reddit — the platform named first in 01's own `lane_search_terms[]` ("shopify store no sales reddit") is completely unopenable this run, so the map leans on Shopify Community/Warrior Forum/Quora/YouTube as substitutes · what closing it would cost: 1 Apify `harshmaur/reddit-scraper` run per PB (~$0.05-0.10) once the monthly hard limit resets, or an operator-side residential-proxy fetch of `old.reddit.com/r/<sub>/search.json` for the same PH-## list used here.
