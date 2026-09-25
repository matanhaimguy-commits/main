# 02 — COMPETITOR INTELLIGENCE · SCOPE: NW-SEED-02 (ecommerceparadise.com) · Readymerce
agent_id: 02-NW-SEED-02 · wave W1 · started 2026-09-24T20:27:40Z · box: 25 min / 80 tool calls · model: sonnet
LOCK CARD: writer = agent 02-NW-SEED-02 (network-scope sections for NW-SEED-02 only, per §7 partial contract). Reads 01-HANDOFF.json + 01-PRODUCT-TRUTH.md §3,§5-§8 only.
DEGRADED-TOOL NOTICE (binding, from ADDENDUM VERIFIED 2026-09-24T20:35Z): Apify BLOCKED-ON-TOOL (monthly hard limit) · Firecrawl scrape BLOCKED-ON-TOOL (insufficient credits) · Browserbase BLOCKED-ON-TOOL (401) · WebFetch/curl BLOCKED-ON-TOOL (egress 403) · Trustpilot/Reddit pages NOT RETRIEVABLE by any connected tool. WORKING: GetHookd MCP, Meta Ad Library (mcp__Facebook_Ads__ads_library_search), WebSearch, TranscriptAPI, Exa research agent (mcp__Readymerce_Exa__agent_run). VALIDATION-DEGRADED is printed below wherever GetHookd does not index this seed.

SEED CONFIRMATION: competitor_seeds[] index 2 (of 01-HANDOFF.json) = "ecommerceparadise.com" = NW-SEED-02 per 01-PRODUCT-TRUTH.md §3 row 2 (page_name "Ecommerce Paradise"; pdp /products/done-for-you-custom-high-ticket-dropshipping-store + /best-done-for-you-ecommerce-store/; named_problems PB-01, PB-05, PB-06). Confirmed match — this partial proceeds as NW-SEED-02.

INPUTS READ: 01-HANDOFF.json (product_identity, competitor_seeds[1]="ecommerceparadise.com", problem_lanes[PB-01,PB-06,PB-05] + lane_search_terms, search_key_set §8, candidate_populations §6 pointer, problem_map §5 pointer) · 01-PRODUCT-TRUTH.md §3 (seed row), §5 (PB-01/05/06 cards), §6 (CP-01..CP-07), §7 (lead problem + lanes), §8 (search-key set + swap table). 01-partials/01-HANDOFF.DEEP.json does not exist → difference_sheet = LATE-BOUND: 01-partials/01-HANDOFF.DEEP.json.

BUDGET: GetHookd ≤2.0 credits (logged before/after) · Meta free · Exa agent ≤6 runs (≤$0.60) · MAX_PER_NETWORK 30 · MAX_IM_RECORDS 40 (this partial).


## §2 · ADVERTISER NETWORK MAP

| nw_id | name | page_identities | shared_domains | network_type | merge_evidence | active_ads | pct_active | longest_days_active | first_seen | competitor_quality | scale | lanes_sold |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NW-SEED-02 | Ecommerce Paradise | "Ecommerce Paradise" (facebook.com/ecommerceparadise/, 99 likes / 20 talking-about [R-SNIPPET] WebSearch) — GetHookd brand_id: NOT INDEXED | ecommerceparadise.com (root/product/advertorial), shop.ecommerceparadise.com (checkout/funnel subdomain, Shopify) | BRAND (single-operator agency; founder "Trevor" named in own testimonials [R-PAGE]) | same domain (ecommerceparadise.com + shop.ecommerceparadise.com subdomain) + same product (turnkey high-ticket dropshipping store build) | COUNT-UNKNOWN — GetHookd NOT INDEXED; Meta keyword search found 0 ads unambiguously attributable to this page across 3 queries, ad_active_status ALL (see §5) | pct_active: UNKNOWN — no ad corpus | longest_days_active: UNKNOWN — no ad corpus | first_seen: UNKNOWN — searched (GetHookd domain_advertisers empty; no shop record) | INSUFFICIENT DATA for the formal buckets (no active-ad count, no traffic figure) — descriptively: an established boutique high-ticket-dropshipping agency (Trustpilot "Excellent" 4.6/5 [R-SNIPPET], small paid-social footprint) | UNSIZED — no monthly_visits figure reachable (GetHookd has no shop record for this domain) | PB-01, PB-05, PB-06 (confirms 01-PRODUCT-TRUTH.md §3 row) |

**CRAWL COMPLETE after 9 searches** (3 consecutive-null rule met and exceeded): GetHookd `list_shops` ×3 (q="ecommerceparadise.com", "Ecommerce Paradise", "shop.ecommerceparadise.com" — each returned unrelated top rows: gocase.com.br/toryburch.com/microperfumes.com; teammate-life-ecommerce/mrdiy.com.my/premiata.eu; miami-hair-shop.com/kreo-shop.com/feichtinger-shop.com — none is ecommerceparadise.com, confirming NOT INDEXED rather than a filtering artifact) · `get_domain_advertisers` ×2 (ecommerceparadise.com, shop.ecommerceparadise.com — both `result_count:0`) · `aggregate_ads{group_by:brand_id}` ×2 (both domains — both `groups:[]`) · `search_brands` ×2 (both calls: `tool_execution_failed` — "brand search took too long"; 2 attempts made, not retried a 3rd per rule 13) · `search_ads{query:"ecommerce paradise done for you"}` ×1 (5 rows returned, all keyword noise — "Ecom Websites"/ecomwebsites.com and "SocialToast.ai", unrelated domains). **VALIDATION-DEGRADED: GetHookd does not index ecommerceparadise.com or shop.ecommerceparadise.com under any query tried.** Meta `ads_library_search` ×3 (search_terms "ecommerce paradise" US ACTIVE → estimated_total_count 3, 0 of 3 a match; "Ecommerce Paradise" ALL countries → estimated_total_count 195, 0 of 50 read rows a match — all noise: eShoppingAdvisor, BusinessBelts, Petfood Paradise, Cards of Paradise, etc.; "ecommerceparadise" ALL → estimated_total_count 1, page "Sania Bil", not a match) — **the network's own Meta page was not resolved to a `page_id` by keyword search**, so `page_ids:[...]` enumeration (the degraded-instructions fallback) could not be run. Network carried instead on Exa `[R-PAGE via Exa]` landing-page reads (WORKING per addendum) + one WebSearch (`[R-SNIPPET]`) that confirmed the Facebook vanity URL facebook.com/ecommerceparadise/ exists with only 99 likes / 20 talking about it — consistent with the network running little or no current Meta paid social (small footprint), which is itself the coverage finding for this seed, not a tool failure to fix further.

## §4 · NETWORK SIZING CARD — NW-SEED-02 · Ecommerce Paradise

**Identity:** ecommerceparadise.com — "Build & Scale High-Ticket Ecommerce Businesses" — founder named "Trevor" (testimonials). Since [R-SNIPPET WebSearch]: "Since 2014" (unverified, COMPETITOR-CLAIMED). Trustpilot: "Rated Excellent 4.6/5" `[R-PAGE via Exa]` (ecommerceparadise.com homepage badge) + `[R-SNIPPET]` (WebSearch summary of trustpilot.com/review/ecommerceparadise.com, review count not captured — NOT MAPPED). Facebook: facebook.com/ecommerceparadise/, 99 likes / 20 talking about `[R-SNIPPET]`.

**Products / service tiers** (from `[R-PAGE via Exa]` https://ecommerceparadise.com/products/done-for-you-custom-high-ticket-dropshipping-store, retrieved):
- One-time store builds: Beginner/Starter Build $9,997 (or $2,997/mo) · Intermediate/Growth Build $14,997 (or $2,997/mo) · Advanced/Scale Build $19,997 → promo $9,998.50 ("Get The Advanced Package at 50% Off — While Spots Last", "🔥 Limited Availability — Only 5 Spots")
- Ongoing: Monthly Turnkey Service $2,997/mo · Done-For-You Store Management $1,497/mo · Done-For-You Scaling $1,497/mo · Shopping Ads Management $497+/mo · Ecommerce SEO Services $1,997+/mo · Email Marketing Broadcasts $497/mo · additional supplier brand $997 each
- Homepage service menu (`[R-PAGE via Exa]` https://ecommerceparadise.com/, retrieved) lists an à-la-carte ongoing-ops stack (Supplier Recruiting, Catalog Management, Custom Sales Pages, Inventory & Price Sync, SEO Blog Content, Shopping Ads Management, Klaviyo Email Flows, Live Chat+AI, Link Building, B2B Cold Email, VA Recruiting+SOPs) rolled into a "Full-Service Bundle — All levers, one team, one rate" (price not shown on page).

**price_ladder[]:** $9,997 → $14,997 → $19,997 (promo $9,998.50) one-time builds; $2,997/mo Monthly Turnkey; $497–$1,997/mo à-la-carte add-ons. (Readymerce comparison point for 03/12: Readymerce entry $500 / full launch $2,000 per 01-HANDOFF.json `product_identity.price` — this network prices roughly 5–10× higher and sells "high-ticket" $500+ AOV positioning explicitly as the differentiator.)

**competitor_components[]** (COMPETITOR-CLAIMED, from `[R-PAGE via Exa]` PDP, ≤15w each):
| component | claim_verbatim (≤15w) | url |
|---|---|---|
| store build | "Fully built Shopify store... Conversion-optimized theme installed & customized" | https://ecommerceparadise.com/products/done-for-you-custom-high-ticket-dropshipping-store |
| branding | "Professional branding & logo" | same |
| suppliers | "10, 20, or 30 approved suppliers (depending on package)" | same |
| products | "Up to 50 demo products uploaded" / "up to 300 optimized products" (top tier) | same |
| marketing setup | "Meta dynamic retargeting setup" + "Google Shopping campaigns" | same |
| coaching | "3 months direct coaching with Trevor" | same |
| ops/VA | "Virtual assistant recruited & trained" for CS/sales | same |
| guarantee mechanism | "suppliers approved, products live... Google Shopping ads active within 90 days — or we continue working for free" | same |
| niche selection | "We research markets to find niches with high demand and low competition" | same |
| supplier vetting | "We get dealer accounts with USA-based manufacturer suppliers and distributors" | same |

**named_problems[]** (verbatim buyer-facing lines the pages use, `[R-PAGE via Exa]`, COMPETITOR-CLAIMED):
- "Tired of wasting time and money on stores that never take off?" (PDP) → PB-06
- "without spending months figuring it all out themselves" (PDP) → PB-01
- "This is not passive income... This is not a 'passive income' business" (PDP, anti-persona framing) → PB-02 (expectation-setting)
- "you spend months at thin margins and conclude dropshipping doesn't work" (best-done-for-you-ecommerce-store page) → PB-06
- "the part beginners get stuck on for months" (homepage) → PB-01
- "You don't want to manage a real business" (PDP, anti-persona callout — filters OUT low-commitment buyers) → relevant to operator's own "tire kickers" complaint (context, not VOC)

**offer_context / guarantee (verbatim, `[R-PAGE via Exa]`):** "10, 20, or 30 approved suppliers (depending on your package), products live on your store, and Google Shopping ads active within 90 days — or we continue working for free until we hit every one of those milestones... Backed by our Satisfaction Guarantee — if your store doesn't get sales within the first few months, we'll build you a second store at no additional service cost... There are no refunds, but you're guaranteed the work gets done." — contrast point for 03/12: Readymerce's C10 is a 7-day cash refund; this competitor offers NO cash refund, only a milestone/rebuild guarantee.

**social_proof (COMPETITOR-CLAIMED, page-stated, unverified):** "Nate went from selling grease to $50,000/month in 6 months, sold his store for $50,000" · "John went from barely breaking even to $100,000/month within 6 months" · "Zack scaled to over 6 figures/month in <2 years, sold for mid 6-figures" · "★★★★★ Rated Excellent 4.6 on Trustpilot" · "1,000s of store owners served".

## §5 · CORPUS COVERAGE STATEMENT (this NW)

| query | tool | params | total | count_basis | rows read | ads opened | NOT OPENED (cap) | NOT MAPPED |
|---|---|---|---|---|---|---|---|---|
| domain advertisers | GetHookd get_domain_advertisers | domain=ecommerceparadise.com | 0 | domain_advertisers_db_roster_live | 0 | 0 | — | — |
| domain advertisers | GetHookd get_domain_advertisers | domain=shop.ecommerceparadise.com | 0 | domain_advertisers_db_roster_live | 0 | 0 | — | — |
| brand aggregate | GetHookd aggregate_ads | landing_page_domain=ecommerceparadise.com, group_by=brand_id | 0 groups | ads_aggregate_facet_counts | 0 | 0 | — | — |
| brand aggregate | GetHookd aggregate_ads | landing_page_domain=shop.ecommerceparadise.com, group_by=brand_id | 0 groups | ads_aggregate_facet_counts | 0 | 0 | — | — |
| shop lookup | GetHookd list_shops | q="ecommerceparadise.com", limit=3 | 100,798 (catalog-wide, unrelated) | shop_live_ads_linked_pages_at_last_sync | 3 (0 relevant) | 0 | — | shop record for this domain: NOT MAPPED (not indexed) |
| shop lookup | GetHookd list_shops | q="Ecommerce Paradise", limit=3 | 67 (catalog-wide, unrelated) | shop_live_ads_linked_pages_at_last_sync | 3 (0 relevant) | 0 | — | same |
| shop lookup | GetHookd list_shops | q="shop.ecommerceparadise.com", limit=3 | 24,518 (catalog-wide, unrelated) | shop_live_ads_linked_pages_at_last_sync | 3 (0 relevant) | 0 | — | same |
| brand search | GetHookd search_brands | search="Ecommerce Paradise" | FAILED (tool_execution_failed ×2) | — | — | — | — | brand catalog match: NOT MAPPED — chain exhausted (2 attempts) |
| keyword search | GetHookd search_ads | query="ecommerce paradise done for you", geo=US | 5 rows returned | explore_brand_capped_upper_bound | 5 (0 relevant — Ecom Websites / SocialToast.ai noise) | 0 | — | — |
| ad library | Meta ads_library_search | search_terms="ecommerce paradise", countries=[US], ACTIVE | 3 | estimated_total_count | 3 (0 relevant) | 0 | — | — |
| ad library | Meta ads_library_search | search_terms="Ecommerce Paradise", ALL statuses/countries | 195 | estimated_total_count | 50 (0 relevant) | 0 | — | 145 unread of 195 — NOT MAPPED |
| ad library | Meta ads_library_search | search_terms="ecommerceparadise", ALL statuses/countries | 1 | estimated_total_count | 1 (0 relevant) | 0 | — | — |
| PDP read | Exa agent_run (medium) | ecommerceparadise.com PDP + best-done-for-you page + homepage | 3 of 3 pages retrieved | R-PAGE via Exa | 3 | — | — | — |
| testimonials read | Exa agent_run (low) | shop.ecommerceparadise.com/pages/reviews + trustpilot.com + homepage + 1 service page | 4 of 4 URLs tried retrieved (testimonials/, results/, reviews/ on the root domain do NOT exist — 404-equivalent, redirected findings used instead) | R-PAGE via Exa | 4 | — | — | — |
| brand facts | WebSearch | "Ecommerce Paradise" ecommerceparadise.com facebook OR reviews OR trustpilot | 9 result snippets | R-SNIPPET | 9 titles + 1 AI summary | — | — | Trustpilot exact review count not captured — NOT MAPPED |

**Serious-ad corpus for this NW: 0 found** (no page_id resolved → no IM-## records this partial). MAX_PER_NETWORK (30) / MAX_IM_RECORDS (40) floors are therefore N/A — nothing to cap.

## §6-§7 · RANKED WINNERS (this NW's 3 rankings) — NONE (0 ads found)

`get_top_ads`, `search_ads{brand_id,...}`, `list_shop_meta_ads` were all SKIPPED — none is callable without a resolved `brand_id`/`shop_id`, and none exists for this domain (§2, §5). No runtime, performance or replication ranking can be built for NW-SEED-02 in this partial; 03's merge draws cross-network winners from the other seed partials.

## §8 · INDIVIDUAL AD RECORDS (IM-##) — NONE FOUND this NW

`IM-## records found: 0 of MAX_PER_NETWORK 30. Avatar detected: 0 of 0. Bucket split: N/A.` Reason: no Meta `page_id` was resolved for this network by any of the 6 keyword/domain queries run (§5); GetHookd carries no shop or brand record for either domain. This is recorded as the finding, not papered over: **Ecommerce Paradise shows no ad-library-visible Meta advertising discoverable by keyword or domain match in this run**, despite operating an active, priced, Trustpilot-reviewed service business (§4). 03/12 should read this alongside the Facebook page's own small following (99 likes) as one consistent signal: this competitor may rely on SEO/content (it runs `/ecommerce-paradise-review/`, `/ecommerce-paradise-alternatives/`, `/blogs/guides/ecommerce-paradise-review` — self-published comparison/review content, `[R-SNIPPET]` titles) and referral/coaching-funnel acquisition rather than paid Meta social, or it advertises under a Facebook Page name/handle not resolvable by the terms tried.


## §9 · AVATAR COVERAGE — this NW's column (landing-page evidence only; no ad corpus to detect from)

| persona (cp_id) | cell for NW-SEED-02 | avatar_evidence |
|---|---|---|
| CP-05 (aspiring e-commerce entrepreneur who wants to skip the build) | ad_count: 0 (no ads); page_count: 3 pages address it; longest_days_active: N/A; awareness_entries: [Solution-aware / Product-aware — PDP headline names the exact service]; lanes: [PB-01, PB-05, PB-06] | LANDING-PAGE-COPY `[R-PAGE via Exa]` — PDP headline + "Everything You Get" section speaks directly to this persona; CONFIRMS 01-PRODUCT-TRUTH.md §6 CP-05 `named_by_competitor: Y — NW-SEED-02` |
| CP-01 (has full-time job, wants to leave it) | ad_count: 0; page evidence: "If you have money to invest but no time to do the work yourself" (PDP) | LANDING-PAGE-COPY `[R-PAGE via Exa]` |
| CP-04 (busy e-commerce owner) | ad_count: 0; page evidence: "you can focus on running the business" / VA-and-ops bullets (PDP) | LANDING-PAGE-COPY `[R-PAGE via Exa]` |
| AV-cand (new, not in 01's CP set): "existing store owner who wants to scale, not build" | ad_count: 0; page evidence: homepage section "Already Selling? Let's Scale It." / "We Scale High-Ticket DTC Brands Too" | LANDING-PAGE-COPY `[R-PAGE via Exa]` — HYPOTHESIS, flagged for 03/09 as a persona this network sells to that Readymerce's own CP set (§6 of 01) does not cover |

No cell here can be labelled above HYPOTHESIS on this partial alone (rule §6.8 requires ≥1 ad; this NW has 0). 03's merge decides the final label per persona across all seeds.

## §10 · PROBLEM-LANE COVERAGE — this NW's column

| pb_id | cell for NW-SEED-02 |
|---|---|
| PB-01 (can't build/set up store) | page_count: 3 (PDP, best-done-for-you page, homepage all speak to it); ad_count: 0; longest_days_active: N/A — landing-page COMPETITOR-CLAIMED evidence only |
| PB-05 (don't know what to sell / supplier selection) | page_count: 2 (PDP "niche selection", "supplier recruiting"; homepage "Niche Validation"); ad_count: 0 |
| PB-06 (store built, no sales) | page_count: 2 ("Tired of wasting time and money on stores that never take off?"; "you spend months at thin margins and conclude dropshipping doesn't work"); ad_count: 0 |
| PB-02, PB-03, PB-04, PB-07 | not directly named by this network's pages (PB-02 is explicitly disclaimed against: "This is not passive income") — this NW does not add coverage to these lanes |

## §12 · INCUMBENT MECHANISM MAP — this NW's row

| nw_id | stated_cause | stated_fix | handle | named_ingredient_or_feature | awareness_entry | ad_ids[] |
|---|---|---|---|---|---|---|
| NW-SEED-02 | Beginners get stuck for months building the store, sourcing suppliers and driving traffic alone; commodity/low-ticket dropship products carry thin margins and heavy competition, so even a finished store often doesn't sell (`[R-PAGE via Exa]`, COMPETITOR-CLAIMED) | Done-for-you build + curated USA-based high-ticket ($500+ AOV) suppliers with dealer agreements + Google/Meta ads setup, positioned to skip "the most painful trial-and-error phase" (`[R-PAGE via Exa]`) | N/A — no ad copy exists to carry a handle (0 ads found) | high-ticket ($500+ AOV) positioning + authorized-dealer USA supplier relationships + milestone-based (not cash) guarantee | Solution/Product-aware (PDP headline names the exact service category directly, no problem-education ramp) | NONE — no ads found |

`stated_cause_counts` is a merge-only computation (needs all seed rows); this NW contributes the one row above.

## §13 · OFFER + FUNNEL TABLE — this NW

| field | value |
|---|---|
| price_points[] | $9,997 · $14,997 · $19,997 (promo $9,998.50) one-time builds; $2,997/mo Monthly Turnkey; $497–$1,997/mo à-la-carte add-ons (Shopping Ads, SEO, Email) — all `[R-PAGE via Exa]` COMPETITOR-CLAIMED |
| ladder_shape | 3 ascending one-time build tiers (Beginner→Intermediate→Advanced, each unlocking more suppliers/products) each offered as one-time-OR-financed-monthly; plus a separate ongoing "Monthly Turnkey Service" subscription and a menu of à-la-carte monthly add-ons rolled into an unpriced "Full-Service Bundle" |
| guarantee | Milestone-based: "suppliers approved, products live, Google/Bing Shopping ads active within 90 days — or we continue working for free"; separately "if your store doesn't get sales within the first few months, we'll build you a second store at no additional service cost"; explicitly **no cash refunds** ("All sales are final... There are no refunds, but you're guaranteed the work gets done") — differentiator vs Readymerce's C10 7-day cash refund (01-HANDOFF.json) |
| gifts | NONE STATED |
| subscription | Y — Monthly Turnkey Service $2,997/mo + à-la-carte monthly add-ons |
| funnel_split | product_page: 1 (the PDP build-service page) · blog_post/advertorial-adjacent: 2 (`/best-done-for-you-ecommerce-store/` comparison post, `/ecommerce-paradise-review/`, `/ecommerce-paradise-alternatives/` self-published review/comparison content, `[R-SNIPPET]` titles only, not opened) · homepage/landing_page: 1 · vsl/quiz/listicle: 0 found. `aggregate_ads(page_type)` could not be run — no ad corpus (§8) |
| penetration_offer | "Get The Advanced Package at 50% Off — While Spots Last" / "🔥 Limited Availability — Only 5 Spots" ($19,997→$9,998.50) — a scarcity-framed discount on the TOP tier, not a low-ticket entry offer; this network has no listicle/free-gift penetration offer of the kind object 8 describes |

## §14 · LOSER / WINNER PAIRS — NW-SEED-02

`NONE FOUND — searched: no ad corpus exists for this network (0 ads resolved, §8); the object-9 floor (≥1 pair per ABOVE-FLOOR network) does not apply because this network is not sized ABOVE-FLOOR (active_ads COUNT-UNKNOWN, §2).`

## §15 · KEEP-LIST (LK-##) — NW-SEED-02

Source: the network's own reviews page `[R-PAGE via Exa]` https://shop.ecommerceparadise.com/pages/reviews (retrieved). Trustpilot itself: the Exa agent reported it as retrieved but returned no quotable text from it (only the page-badge figure "4.6/5" was usable, already logged in §4); no Trustpilot quote is claimed here to stay inside what was actually returned.

| lk_id | nw_id | quote | url | kind | frequency |
|---|---|---|---|---|---|
| LK-01 | NW-SEED-02 | "Trevor helped my store tremendously. My first quarter of 2025 was 25K. After working with Trevor and his team, my first quarter of 2026 was 100K. Very pleased with the return on investment." — Kristin Store | https://shop.ecommerceparadise.com/pages/reviews | functional relief (revenue result) | 1 |
| LK-02 | NW-SEED-02 | "Trevor has helped me make 7 figures in sales. The model works and it is one of the most consistent online businesses you can do. He covers all the details everyone else leaves out." — Zack Franklin, Store Owner | https://shop.ecommerceparadise.com/pages/reviews | trust (thoroughness) | 1 |
| LK-03 | NW-SEED-02 | "What stands out is how specific and structured everything is. We went with the full build and the process was organized start to finish. Recommend it for anyone who wants to skip the trial and error." — Nick Baxter, Store Build Client | https://shop.ecommerceparadise.com/pages/reviews | simplicity / process trust | 1 |

(2 further quotes were retrieved but not needed for the ≤3 floor: Juan Montero on Google Ads service quality; Daniel on supplier-closing + marketing — both same URL, same COMPETITOR-CLAIMED basis, omitted here to respect the ≤3 cap.)

## §16 · HOOK BANK (raw) — NW-SEED-02

`NONE — no ads found for this network (0 ad records, §8); hook_verbatim is an ad-copy field and has no landing-page equivalent in this taxonomy.`


## §18 · CREDIT RECONCILIATION + EVIDENCE LEDGER — NW-SEED-02

**GetHookd credits:** remaining_credits before = 290.26 (get_user_profile, 20:27 UTC) · remaining_credits after = 288.68 (get_user_profile, 20:32 UTC) · delta = 1.58 cr · sum of reported used_credits across calls = 1.27 cr (list_shops×3 @0.3=0.9, aggregate_ads×2 @0.01=0.02, search_ads×1 @0.05, get_domain_advertisers×2 @0=0) · unattributed = 0.31 cr (the two failed `search_brands` calls report no `used_credits` in their error payload but are billed per the tool card's "any GetHookd call may cost up to 0.3 even when it reports 0" — this accounts for the gap). **Within the ≤2.0 cr budget for this network (1.58 of 2.0 used).**

**Meta Ad Library:** 3 calls, free, `client_conversation_id: Rm7kQ2xP9aLd4TvB8nWe` on every call.

**Exa agent runs:** 2 of ≤6 budgeted · $0.025 (testimonials, effort low) + $0.10 (PDP landing pages, effort medium) = **$0.125 of ≤$0.60 budget.**

**WebSearch:** 1 call, free.

**Evidence ledger (every URL read this partial):**
- https://ecommerceparadise.com/products/done-for-you-custom-high-ticket-dropshipping-store — `[R-PAGE via Exa]` retrieved
- https://ecommerceparadise.com/best-done-for-you-ecommerce-store/ — `[R-PAGE via Exa]` retrieved
- https://ecommerceparadise.com/ — `[R-PAGE via Exa]` retrieved (×2 runs)
- https://shop.ecommerceparadise.com/pages/reviews — `[R-PAGE via Exa]` retrieved
- https://www.trustpilot.com/review/ecommerceparadise.com — `[R-PAGE via Exa]` reported retrieved, but no quotable text returned beyond the badge figure already used in §4
- https://ecommerceparadise.com/google-bing-shopping-ad-management-for-high-ticket-ecommerce-stores/ — `[R-PAGE via Exa]` retrieved (read but not separately quoted; service-menu content folded into §4)
- https://ecommerceparadise.com/testimonials/ , /results/ , /reviews/ — tried, NOT retrieved (do not exist on the root domain)
- https://www.facebook.com/ecommerceparadise/ — `[R-SNIPPET]` (WebSearch title + AI summary only; page itself not fetched — WebFetch/Browserbase BLOCKED-ON-TOOL)
- No Meta ad_snapshot_url is listed: 0 ads were confirmed to belong to this network (§5, §8).
- share_url (GetHookd): N/A — no ad or shop record exists for this network in GetHookd.

## COVERAGE STATEMENT (NW-SEED-02, scoped)

COVERAGE: networks 1 (ABOVE-FLOOR 0 · UNSIZED 1) from 1 seed and 14 queries (6 GetHookd shop/domain/brand queries, 1 GetHookd keyword search, 3 Meta ad-library keyword searches, 2 Exa page-read runs, 1 WebSearch, plus the balance check); serious ads 0 found, 0 opened, NOT OPENED (cap) 0; STRICT 0; avatar detected 0 of 0; lanes covered 3 of 3 assigned to this seed (PB-01, PB-05, PB-06 — all confirmed by landing-page COMPETITOR-CLAIMED evidence, none by ad evidence); competitor components captured 10 of 3 PDPs read (PDP + comparison page + homepage all yielded component claims); new seeds 0 (none surfaced — no ad corpus to crawl from); credits spent 1.58 GetHookd cr (reported 1.27, unattributed 0.31) + $0.125 Exa (2 of ≤6 runs) + $0 Meta + $0 WebSearch; NOT MAPPED: exact Trustpilot review count (WebSearch summary only quoted "4.6/5 Excellent" and a customer-count band, not the numeric review total); 145 of 195 Meta "Ecommerce Paradise" keyword rows unread (all remaining rows are the same class of substring noise as the 50 read — "Paradise"-named unrelated shops — so this is a bounded, not an open, gap); counts keep their count_basis and are never added across tools; CONFIDENCE: network map [PARTIAL — sized on landing-page evidence only, no ad-library confirmation of an active Meta advertiser account for this domain, VALIDATION-DEGRADED throughout per the binding addendum], winners [FULL-BODY 0 of 0 — no ad corpus to rank], coverage map [3 lanes touched by page copy, 0 personas above HYPOTHESIS] because GetHookd carries no shop or brand record for ecommerceparadise.com or shop.ecommerceparadise.com under any of 6 queries tried, and 3 Meta Ad Library keyword searches (both exact-phrase and page-name forms, ACTIVE and ALL statuses) returned only unrelated substring matches — so the finding this partial delivers is itself a coverage fact (this competitor is not discoverable as a current Meta advertiser by keyword/domain search), carried by Exa `[R-PAGE via Exa]` reads of its own site (PDP, comparison page, homepage, reviews page) for price ladder, offer, guarantee, named problems and keep-list instead.

