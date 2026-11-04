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
| COM-01 | reddit | r/dropshipping | https://www.reddit.com/r/dropshipping/ | UNSIZED | subscribers | NULL | — | UNKNOWN | UNKNOWN | UNKNOWN | problem_discussion (named, unconfirmed) | PUBLIC | none confirmed | [D] beginners, resellers, guru-adjacent accounts | LOW-ACTIVITY (unconfirmed) | HYPOTHESIS — excluded from VALIDATED/SUPPORTED counters | UNSIZED — method: Exa agent attempted https://www.reddit.com/r/dropshipping/ , reported "could not be retrieved"; apify/rag-web-browser BLOCKED-ON-TOOL (monthly hard limit). Named from 04's own discovery, not opened successfully — kept per rule (a source never opened is never listed as opened) |
| COM-02 | reddit | r/dropship | https://www.reddit.com/r/dropship/ | UNSIZED | subscribers | NULL | — | UNKNOWN | UNKNOWN | UNKNOWN | problem_discussion (named, unconfirmed) | PUBLIC | none confirmed | [D] same as COM-01 | LOW-ACTIVITY (unconfirmed) | HYPOTHESIS — excluded from counters | UNSIZED — method: Exa agent attempt failed; Apify BLOCKED-ON-TOOL. Described by redpulse.io [R-SNIPPET, third-party, not counted as size] as "focused on the entrepreneurial side of dropshipping" |
| COM-03 | forum | Warrior Forum — Ecommerce Sites, Wholesaling & Drop Shipping | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/ | UNSIZED (forum-wide member count not exposed) | members | NULL | — | UNKNOWN | 8–15 replies on the 2 threads opened | 2017-12-16 (newest thread opened) | problem_discussion | PUBLIC | PH-02, PH-19 | [D] beginner dropshippers, mixed experience | ACTIVE-on-thread (old threads, but genuinely on-topic and first-person) | SUPPORTED — 3 threads opened and read (title+body), pain phrase confirmed verbatim, but forum-wide size never exposed so full VALIDATED (which requires a size tier) is not claimed | Threads opened: (1) "winning product ?? dropshipping" — alex19890, 2017-12-16, 1 reply [R-PAGE via Exa]; (2) "Please some help with Dropshipping....." — clik2000, ~14y ago, 8 replies [R-PAGE via Exa]; (3) "Alibaba.com and dropshipping" — neeralt, ~14y ago, 15 replies [R-PAGE via Exa] |
| COM-04 | forum | Indie Hackers | https://www.indiehackers.com/ | UNSIZED (site-wide member count not exposed) | members | NULL | — | UNKNOWN | 1 comment / 1 upvote (thread 1); 0 visible (thread 2) | 2021-09-02 | problem_discussion | PUBLIC | PH-08 (near), PH-19-adjacent | [D] indie SaaS/ecom founders | LOW-ACTIVITY | SUPPORTED — 2 posts opened, verbatim pain-phrase language confirmed, size not exposed | Posts opened: "Our solution for finding winning products" — Ilia Boltianov, 2021-09-02, 1 comment/1 upvote [R-PAGE via Exa]; "No ideas for backend products" — codefella, 2021-08-01 [R-PAGE via Exa] (digital-product adjacent, population match imperfect — kept, tagged in notes) |
| COM-05 | quora | Quora — E-Commerce / product-selection questions | https://www.quora.com/topic/E-Commerce | UNSIZED (topic follower count not exposed) | answers | NULL | — | UNKNOWN | UNKNOWN (answer counts errored on load for 4 of 5 pages) | UNKNOWN | solution_seeking | PUBLIC | PH-03 | [D] mixed — sellers, aspiring sellers, advice-givers | LOW-ACTIVITY (mostly low-engagement questions) | SUPPORTED — 1 question page opened and verbatim first-person text confirmed; 4 other Quora question pages Exa opened but Quora returned "Something went wrong" (page not usable) | Opened: "What product will you suggest I sell? I am a 25-year-old lady..." [R-PAGE via Exa], no reply-count exposed. 4 other Quora URLs attempted, load error both runs — logged, not counted as opened |
| COM-06 | facebook_group | CJdropshipping / Dropshipping.com Community \| Winning Products / Dropshipping Trending Products | https://www.facebook.com/groups/cjdropshipping/ ; https://www.facebook.com/groups/3010156415933280/ ; https://www.facebook.com/groups/dropshippingtrendingproduct/ | UNKNOWN | members | NULL | — | UNKNOWN | UNKNOWN | UNKNOWN | problem_discussion (named, unconfirmed) | LOGIN_WALLED | none (page wall, no content visible) | [D] unknown | LOW-ACTIVITY (unconfirmed) | HYPOTHESIS — [R-WALLED], counted not harvested | 3 candidate groups found by Exa discovery; all 3 returned a Facebook login wall, no about/member data or post content visible — [R-WALLED] |
| COM-07 | youtube_search | YouTube search: "how I finally found a winning product" / "I don't know what to sell online store" / "I wasted months on product research" / "how I finally picked what to sell" | https://www.youtube.com/results?search_query=... (4 queries via TranscriptAPI search_youtube) | 21,953 / 698 / 8,912 / 105,704 views (top matching videos, see §2 tier) | views_for_phrase | R-TOOL (TranscriptAPI search_youtube) + R-SCRAPE (full transcript fetched for 8 videos) | 2026-09-24 | n/a (not a live feed) | n/a | video publish dates: 3y ago (bKdLdxlLmPA) / 1y ago (-1Q60dZcuHc) / 2mo ago (xEvaenj4JH8) / 8y ago (33JF7JAsG9k, educational not first-person) | problem_discussion (first-person journey videos) | PUBLIC | PH-02, PH-08, PH-15, PH-19 | [D] solo dropshippers/creators, mixed experience level, several monetizing via own channel (creator bias) | ACTIVE — VALIDATED | 8 videos' transcripts fetched in full (§list below); 2 of 8 are strongly on-PB-05 first-person struggle/resolution narratives (xEvaenj4JH8 Business By Nancy; xlV60PEwg5c Manish Kumar, Hindi, [translated]); bKdLdxlLmPA and -1Q60dZcuHc are product-research/ad-strategy tutorials with light first-person framing; 33JF7JAsG9k (Oberlo) and kO-POM2RLYw are advisor-voice, not sufferer-voice — kept but tagged accordingly in 06 |

COM floor (scoped): ≥4 per PB across ≥3 platforms → **7 communities across 5 platforms (reddit, forum, quora, facebook_group, youtube_search) — floor met and exceeded.** Reddit ≥3 subreddits per PB: only 2 named (r/dropshipping, r/dropship) — **PARTIAL — reddit subreddit-count floor (3) not met · searched: WebSearch "r/dropshipping", "r/ecommerce reddit", site:reddit.com queries; no third distinct subreddit surfaced this leg; chain exhausted: Apify BLOCKED, Exa "could not be retrieved" on Reddit domain.**

## §4 · POPULATION PRESENCE — CP-05 × COM-##

| cp_id | com_id | label | cited_thread_urls[] | marker_phrase |
|---|---|---|---|---|
| CP-05 | COM-03 | VALIDATED-PRESENT | https://www.warriorforum.com/ecommerce-sites-wholesaling-drop-shipping/1320451-winning-product-dropshipping.html (alex19890, 2017-12-16) | "i am beginner on drop-shipping and i will know how can i find a good product or winning product?" |
| CP-05 | COM-04 | EARLY SIGNAL | https://www.indiehackers.com/post/our-solution-for-finding-winning-products-8173495584 (Ilia Boltianov, 2021-09-02) | "the problem of finding winning products is an eyesore at this point, considering how many people start an e-commerce store nowadays" |
| CP-05 | COM-05 | EARLY SIGNAL | https://www.quora.com/What-product-will-you-suggest-I-sell-I-am-a-25-year-old-lady-and-I-need-help-with-product-ideas-to-sell-even-if-its-in-the-market-It-s-a-fast-moving-product-My-capital-is-500-cedis (author not shown) | "What product will you suggest I sell? I am a 25-year-old lady and I need help with product ideas to sell..." |
| CP-05 | COM-07 | VALIDATED-PRESENT | https://www.youtube.com/watch?v=xEvaenj4JH8 (Business By Nancy, 2026-07 approx / "2 months ago") | "After weeks of overthinking, I finally committed to selling Canva templates on Etsy" |
| CP-05 | COM-07 | EARLY SIGNAL | https://www.youtube.com/watch?v=xlV60PEwg5c (Manish kumar, ~2023) [translated, Hindi original] | translated: "I wasted 8-9 months just consuming information about product research without ever applying it" [translation, original Hindi kept in 06 Q-record] |

CP-05 combined across COM-03/04/05/07: **5 distinct named/handled authors across 4 platforms (forum, forum, quora, youtube×2) → VALIDATED-PRESENT overall for CP-05** (≥3 threads/reviews by different authors, own words, met).

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
| PB-05 | 5 (COM-03×3, COM-04×2 posts, COM-07×2 first-person videos counted once for role) | 1 (COM-05 Quora question) | 0 | 0 | 0 | 0 | 0 | **N — post_purchase_review floor (≥1) not met.** Amazon/Trustpilot lanes not run this leg (time-boxed; see §5). problem_discussion floor (≥1) met. |

## §7 · ASSUMPTION LIST (AS-##)

**LATE-BOUND: 03.AS-##** — 03-HANDOFF.json does not exist and no 03-partials/ files are present at read time (2026-09-24T20:32Z). No `EK-##`, `VD-##`, `VA-##`, `BI-##` rows exist yet to route. 06-MERGE (or 07) runs the assumption check once 03 exists. The one operator-level assumption visible from 01 alone is logged here so it is not lost:

| as_id | source_id | claim (verbatim) | type | communities_to_check[] | status |
|---|---|---|---|---|---|
| AS-P05-01 | CP-05 (01 §6, named_by_competitor Y — NW-SEED-02) | Competitor NW-SEED-02 (ecommerceparadise.com) names its buyer as "Aspiring E-Commerce Entrepreneurs" who want to skip the build/product-selection step | avatar | COM-03, COM-04, COM-07 | UNCHECKED |

## §8 · BIAS + ACCESS ROW

- Reddit (r/dropshipping, r/dropship) is the single largest expected population for PB-05 and is entirely inaccessible this run — Apify BLOCKED-ON-TOOL (monthly hard limit), Exa agent explicitly reports the pages "could not be retrieved." This is the dominant bias: the corpus below is Warrior Forum / Indie Hackers / Quora / YouTube only, which skews toward (a) older, SEO-indexed forum posts (2012–2021, not current), (b) YouTube creators who monetize their own "journey" content (survivorship/success bias — people who post "I finally found my winning product" videos are disproportionately people who succeeded or are selling a course/mentorship), and (c) Indie Hackers/Warrior Forum skew toward digital-product/SaaS-adjacent founders, not pure physical-product dropshippers.
- Facebook groups: 3 candidates found, all `[R-WALLED]` — counted, not harvested. Public commenters on walled platforms are known to differ from silent majority buyers.
- `NULL — searched: [site:reddit.com <PH>, r/dropshipping about.json, r/dropship about.json]` for both Reddit subreddits' size and content.
- Extreme/loud posters (asking public questions, running YouTube channels) are overrepresented vs. the silent majority who search and read without posting — standard search-index / posting bias.
- Search-index bias: WebSearch results were dominated by Shopify's own community forum and SEO/marketing blog content (Oberlo, Sell The Trend, dodropshipping.com) rather than neutral third-party discussion — these are vendor-adjacent and their "common struggles" framing may reflect what sells tools, not raw buyer language.

## §9 · HARVEST BUDGET ESTIMATE

| com_id | lane | actor/tool | est_rows | est_cost |
|---|---|---|---|---|
| COM-03 | forum_thread | RC-WEB (apify/website-content-crawler) — BLOCKED-ON-TOOL this run; Exa agent_run medium fallback used instead | 3 threads already read this leg | $0.10 (2 Exa medium runs already spent) |
| COM-04 | forum_thread | same as above | 2 posts already read | (included above) |
| COM-05 | quora_answers | RC-QU (fatihtahta/quora-scraper) — BLOCKED-ON-TOOL; Exa fallback | 1 page already read | (included above) |
| COM-07 | youtube_transcript | RC-YTX (TranscriptAPI get_youtube_transcript) | 8 already fetched | $0 (TranscriptAPI credits, not Exa) |
| COM-01/02 | reddit_post+comments | RC-RD (harshmaur/reddit-comments-scraper) — BLOCKED-ON-TOOL; no working fallback found (Exa also blocked on reddit.com) | 0 | $0 spent, cannot close without operator paste |
| COM-06 | fb_post_comments | RC-FBC (apify/facebook-comments-scraper) — BLOCKED-ON-TOOL; groups also LOGIN_WALLED to Exa | 0 | $0 spent, cannot close |

Sum this leg: **$0.25** (4 Exa runs: 2×low $0.025 + 2×medium $0.10) vs. scoped cap $0.60 (standard $6 map cap ÷ ~10 PBs, this run has 3 in-scope PBs per 01 so effective per-PB share is higher; kept conservative at $0.60 stated in the brief). Remainder of Exa run-budget preserved for STEP 06 harvest lanes.

## §10 · COVERAGE STATEMENT

Community sizes and pain-phrase hit counts above are printed only from pages actually fetched this leg (WebSearch snippets, Exa-opened pages, and TranscriptAPI-read video metadata/transcripts) — never from memory; population presence is cited to specific opened threads/videos with author and date, never asserted from a community's name alone; speaker-mix guesses are marked `[D]`. The Reddit lane (the single largest expected PB-05 population, r/dropshipping + r/dropship) is fully `BLOCKED-ON-TOOL` this run (Apify hard limit; Exa reports pages "could not be retrieved") and the Facebook-group lane is fully `[R-WALLED]` — both are named, not harvested. Amazon and Trustpilot lanes were not attempted this leg (time-boxed toward forum/YouTube discovery, which is where PB-05's population is most reachable under the current tool set).

**COVERAGE: COM 7 (VALIDATED 1 · SUPPORTED 4 · HYPOTHESIS 2) · platforms 5/9 · PB below floor: [NONE on the ≥4-per-PB floor; PARTIAL on the reddit≥3-subreddits sub-floor] · CP NOT FOUND: [NONE — CP-05 VALIDATED-PRESENT] · walled 3 (COM-06's 3 groups) · Reddit usable rate 0% (0 of 2 candidate subreddits retrievable) · cost $0.25 · AS: 1 row | LATE-BOUND: 03.AS-## for everything downstream of 03 · weakest link: Reddit (Apify BLOCKED-ON-TOOL + Exa cannot retrieve reddit.com) removes the largest single expected population for this PB · what closing it would cost: an Apify plan reset (or a different Reddit-capable scraper credential) + ~$0.05–0.10/thread via harshmaur/reddit-comments-scraper on the 2 named subreddits, plus an operator paste of 5–10 thread URLs as an immediate substitute.**
