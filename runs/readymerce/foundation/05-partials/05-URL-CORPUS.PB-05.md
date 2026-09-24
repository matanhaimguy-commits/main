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
| URL-01 | COM-07 | PB-05 | CP-05 | youtube_search | https://www.youtube.com/watch?v=xEvaenj4JH8 | I FINALLY chose my business idea \| 90-days business challenge | Business By Nancy | 2026-07-24 approx ("2 months ago") | 8,912 views | n/a | relevance | 1 | PH-08, PH-15; population-first: CP-05 | youtube_transcript | 5 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Strongest PB-05 match this leg — explicit product/business-idea-choice paralysis in first person, own words |
| URL-02 | COM-07 | PB-05 | CP-05 | youtube_search | https://www.youtube.com/watch?v=xlV60PEwg5c | Why I Wasted My 9 Months in the Starting Days of Dropshipping\| Real talk | Manish kumar | ~2023 ("3 years ago") | 942 views | n/a | relevance | 2 | PH-08(near), PH-19; population-first: CP-05 | youtube_transcript | 3 | RC-YTX | FETCHED (full transcript read, Hindi, [translated] in 06) | [R-SCRAPE] | — | Product-research/information-paralysis theme; language Hindi, translated passages only in 06 |
| URL-03 | COM-07 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=bKdLdxlLmPA | I Finally Found My First Winning Organic DROPSHIPPING Product! | Dave Obiefuna | ~2023 ("3 years ago") | 21,953 views | n/a | relevance | 3 | PH-02, PH-08 | youtube_transcript | 2 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Mostly ad-strategy tutorial; light first-person framing around finding the product |
| URL-04 | COM-07 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=-1Q60dZcuHc | i finally found a winning dropshipping product (Exact Strategy Revealed) | Ry | ~2025 ("1 year ago") | 698 views | n/a | relevance | 4 | PH-02, PH-08 | youtube_transcript | 1 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Almost entirely ad-metrics tutorial; minimal usable first-person pain language |
| URL-05 | COM-07 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=33JF7JAsG9k | How to decide what to sell online for your dropshipping store | Oberlo (Tommy Walker) | ~2018 ("8 years ago") | 105,704 views | n/a | relevance | 5 | PH-01 (states the problem verbatim in intro) | youtube_transcript | 1 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Advisor/brand voice, not sufferer voice — corroborating context only, coded speaker_stage accordingly in 06 |
| URL-06 | COM-07 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=kO-POM2RLYw | Skip months of research with this one method | The real ecom (Carmen) | ~2026 ("7 months ago") | 101 views | n/a | relevance | 6 | PH-10-adjacent | youtube_transcript | 0 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Tactical how-to, no first-person struggle narrative — 0 usable VOC records expected |
| URL-07 | COM-07 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=9CrxDtJr-O4 | What I Sell Online So I Don't Have To Work a 9-5 Job | Taylor Jo | ~2026 ("2 months ago") | 11,122 views | n/a | relevance | 7 | PH-01 (title match only) | youtube_transcript | 0 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Off-topic on read: reseller "what sold" haul video, not a product-selection struggle — 0 usable records expected, kept per EX-01 |
| URL-08 | COM-07 | PB-05 | — | youtube_search | https://www.youtube.com/watch?v=4hHFTcerXD4 | I Don't Sell Much Online Should I Keep My Online Store | Rafi And Klee | ~2023 ("2 years ago") | 2,334 views | n/a | relevance | 8 | PH-01 (title match only) | youtube_transcript | 1 | RC-YTX | FETCHED (full transcript read) | [R-SCRAPE] | — | Podcast about whether to keep a store (low sales), not product-selection — closer to PB-06; kept, low weight for PB-05 |

### lane: forum_thread

| url_id | com_id | pb_ids[] | population_tags[] | platform | url | title | op_author | date_posted | engagement_primary | engagement_secondary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected | duplicate_of | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| URL-09 | COM-03 | PB-05 | CP-05 | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1320451-winning-product-dropshipping.html | winning product ?? dropshipping | alex19890 | 2017-12-16 | 1 reply | n/a | relevance | 1 | PH-02, PH-19; population-first: CP-05 | forum_thread | 1 | RC-EXA (Exa agent_run, medium) | LISTED + FETCHED (verbatim OP read) | [R-PAGE via Exa] | — | Direct beginner-in-dropshipping question naming "winning product" |
| URL-10 | COM-04 | PB-05 | CP-05 | forum | https://www.indiehackers.com/post/our-solution-for-finding-winning-products-8173495584 | Our solution for finding winning products | Ilia Boltianov | 2021-09-02 | 1 comment | 1 upvote | relevance | 2 | PH-08(near); population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Founder framing the product-finding problem as widespread |
| URL-11 | COM-03 | PB-05 | — | forum | https://www.warriorforum.com/offline-marketing/655739-alibaba-com-dropshipping.html | Alibaba.com and dropshipping | neeralt | ~2012 ("14 years ago") | 15 replies | n/a | relevance | 3 | PH-01-adjacent (sourcing/product question) | forum_thread | 2 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Sourcing/product-type question, older thread |
| URL-12 | COM-03 | PB-05 | — | forum | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/746185-please-some-help-dropshipping.html | Please some help with Dropshipping..... | clik2000 | ~2013 ("14 years ago") | 8 replies | n/a | relevance | 4 | PH-01-adjacent | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Niche/supplier question with product-selection sub-thread |
| URL-13 | COM-04 | PB-05 | — | forum | https://www.indiehackers.com/post/no-ideas-for-backend-products-268e3559b8 | No ideas for backend products | codefella | 2021-08-01 | n/a | n/a | relevance | 5 | PH-05-adjacent | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] | — | Digital/SaaS product-ideation struggle, not physical dropshipping — population match imperfect, kept |

### lane: quora_answers

| url_id | com_id | pb_ids[] | population_tags[] | platform | url | title | op_author | date_posted | engagement_primary | engagement_secondary | sort_seen | rank_key | why_chosen | lane | est_records | recipe_id | status | tier_expected | duplicate_of | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| URL-14 | COM-05 | PB-05 | CP-05 | quora | https://www.quora.com/What-product-will-you-suggest-I-sell-I-am-a-25-year-old-lady-and-I-need-help-with-product-ideas-to-sell-even-if-its-in-the-market-It-s-a-fast-moving-product-My-capital-is-500-cedis | What product will you suggest I sell? I am a 25-year-old lady... | not shown on page | not shown | not shown | n/a | relevance | 1 | PH-03; population-first: CP-05 | quora_answers | 1 | RC-EXA | LISTED + FETCHED (question text verbatim; answer count not exposed) | [R-PAGE via Exa] | — | Direct product-idea request; author handle not exposed by the retrieved page |

**4 other Quora URLs attempted this leg (2 in the 04 discovery run, 2 in a follow-up), all returned Quora's own "Something went wrong" error on load — logged here, not counted as LISTED:** https://www.quora.com/I-want-to-create-a-business-and-sell-stuff-but-I-m-not-sure-what-to-sell-How-do-I-choose-a-good-product-service-and-or-item-to-sell · https://www.quora.com/How-can-I-find-winning-products-to-sell-on-Shopify-for-dropshipping · https://www.quora.com/What-is-the-step-by-step-process-to-find-a-winning-product-for-Shopify-dropshipping-I-have-seen-many-videos-but-I-still-can-t-understand-properly · https://www.quora.com/What-products-should-I-sell-as-a-beginner-on-my-eBay-store — status BLOCKED (page-load error), reason logged per row in §3 EXCLUSIONS.

### BLOCKED lanes (named, not harvestable this leg)

| url_id | com_id | platform | url | status | reason |
|---|---|---|---|---|---|
| URL-15 | COM-01 | reddit | https://www.reddit.com/r/dropshipping/ | BLOCKED | subreddit named, no thread URL ever surfaced — Apify BLOCKED-ON-TOOL, Exa agent "could not be retrieved" — **OPERATOR-PASTE requested: 5-10 top r/dropshipping thread URLs matching "what should I sell" / "winning product"** |
| URL-16 | COM-02 | reddit | https://www.reddit.com/r/dropship/ | BLOCKED | same as URL-15 — **OPERATOR-PASTE requested: 3-5 top r/dropship thread URLs** |
| URL-17 | COM-06 | facebook_group | https://www.facebook.com/groups/cjdropshipping/ | BLOCKED | LOGIN_WALLED, no post content visible to any tool |
| URL-18 | COM-06 | facebook_group | https://www.facebook.com/groups/3010156415933280/ | BLOCKED | LOGIN_WALLED |
| URL-19 | COM-06 | facebook_group | https://www.facebook.com/groups/dropshippingtrendingproduct/ | BLOCKED | LOGIN_WALLED |

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
| HV-PB-05 | PB-05 | [CP-05] | [URL-01..URL-14] (URL-15..19 BLOCKED, kept for the log) | [RC-YTX, RC-EXA, RC-WEB(pinned), RC-QU(pinned), RC-RD(pinned), RC-FBC(pinned)] | records≥40 (PB-05) · CP-05≥25 · reddit≥5 (PARTIAL) · url_total≥12 (met) | 06-partials/06-VOC_MASTER.PB-05.csv | 8 |

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
| URL-01 | youtube_transcript | Business By Nancy channel | single video, 2026 | 5 | full transcript, title, author, views, publish date (relative) | none | — |
| URL-02 | youtube_transcript | Manish kumar channel | single video, ~2023 | 3 | full transcript (Hindi), title, author, views | language (Hindi — [translated] tag required in 06) | — |
| URL-03..08 | youtube_transcript | 6 more channels | 2018-2026 | 1-2 each (2 est. 0) | full transcript, title, author, views | none | URL-06/URL-07 low/off-topic content |
| URL-09,11,12 | forum_thread | Warrior Forum ecommerce/offline-marketing subforums | 2012-2017 | 1-2 each | OP text verbatim, author, date, reply count | forum-wide member count not exposed | — |
| URL-10,13 | forum_thread | Indie Hackers | 2021 | 1 each | OP text verbatim, author, date | site member count not exposed | — |
| URL-14 | quora_answers | Quora | undated | 1 | question text verbatim | author handle, date, answer count not exposed | — |
| URL-15,16 | reddit_* | r/dropshipping, r/dropship | n/a | 0 (BLOCKED) | none | Apify hard limit + Exa retrieval failure | tool access |
| URL-17,18,19 | fb_post_comments | 3 named FB groups | n/a | 0 (BLOCKED) | none | LOGIN_WALLED | access |

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
| URL-20 | COM-08 (new: Shopify Community) | PB-05 | CP-05 | forum | https://community.shopify.com/t/how-do-i-know-the-right-product-to-sell/189935 | How do i know the right product to sell | Deborah212399 | 2023-02-07 | 2 replies | relevance | 1 | PH-01; population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] |
| URL-21 | COM-08 | PB-05 | CP-05 | forum | https://community.shopify.com/t/what-should-i-start-selling-as-a-new-online-retailer/118819 | What should I start selling as a new online retailer? | UserID1158907 | 2022-05-04 | 3 replies | relevance | 2 | PH-01; population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] |
| URL-22 | COM-08 | PB-05 | CP-05 | forum | https://community.shopify.com/t/how-do-i-choose-my-first-product-to-sell-online/206448 | How do I choose my first product to sell online? | Marshmallow02 | 2023-04-07 | 1 reply | relevance | 3 | PH-15; population-first: CP-05 | forum_thread | 1 | RC-EXA | LISTED + FETCHED | [R-PAGE via Exa] |

New COM-08: platform forum, name "Shopify Community" (community.shopify.com), a genuinely reachable (non-blocked) platform that this leg under-used initially — 3 OP threads opened, all CP-05 population-first hits, all VALIDATED-PRESENT-grade (named handles, dated, verbatim). Reply posts on these 3 threads are mostly Shopify staff / app-vendor marketing replies (Mac_2, PageFly-Kate, TeamSpocket, ReturnPrime, Skye_1, Victoria_13) — read and logged but not coded as sufferer VOC (vendor-adjacent, evidence_class CUSTOMER_EXPLANATION at best); not converted into Q-records this leg.

**Updated counter after addendum:** `URL 17/12 · PB-05 17/12 · CP-05 8/4 · lanes 3 · cost $0.55/$2.67(scoped cap)`
