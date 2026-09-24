# STEP 02 — COMPETITOR INTELLIGENCE · PARTIAL · SCOPE: NW-SEED-03 (ecomxpertz.com)

agent_id: 02-NW-SEED-03 · wave W1 · seed_id: 01 (third entry in `01-HANDOFF.json` `competitor_seeds[]`) · model: sonnet
run_start (UTC): 2026-09-24T20:28:04Z · max_minutes: 25 · max_tool_calls: 80
LOCK CARD: **VALIDATION-DEGRADED** — GetHookd does not index ecomxpertz.com (`get_domain_advertisers`, `aggregate_ads{landing_page_domain}`, and a `list_shops{q:"ecomxpertz.com"}` sweep all returned zero/irrelevant rows). Per TOOL CARD ADDENDUM, this network is carried on **Meta Ad Library `page_ids` enumeration + one Exa agent PDP read**. `LK: NONE FOUND — BLOCKED-ON-TOOL (Trustpilot)` applies (ca.trustpilot.com/review/ecomxpertz.com is known to exist from 01-PRODUCT-TRUTH.md §3 but is not retrievable by any connected tool).

## §1 · INPUT CARD + SEARCH PLAN

- Product: Readymerce DFY Shopify/Etsy store service (01-HANDOFF.json `product_identity`) · Target market: US ASSUMED.
- Seed: `NW-SEED-03` = `ecomxpertz.com`, confirmed as the third entry of `competitor_seeds[]` in `01-HANDOFF.json` and in `01-PRODUCT-TRUTH.md` §3 (`how_found`: web search 'done for you ecommerce store business service reviews' → ca.trustpilot.com/review/ecomxpertz.com; page name listed there only as "EcomXpertz"; §3 recorded 0 of 3 seed PDPs fetched at SEED stage — 02 reads).
- `SCOPE: NW-SEED-03` (network scope, one seed, method §5 step 1 then N1–N8).
- Budget: GetHookd ≤2.0 credits (spent 1.28, see §18) · Meta free · Exa agent ≤6 runs / ≤$0.60 (spent 1 run / $0.10) · `MAX_PER_NETWORK` 30 · `MAX_IM_RECORDS` 40 (this partial: 1 IM record — the network has only 1 ad in total).
- Plan: N1 GetHookd domain discovery (0.02 cr) → N1b `list_shops` sweep (0.3 cr, returned unrelated shops — GetHookd's `q` free-text search did not resolve the bare domain to a shop record) → N1c `search_brands`/`search_ads{query:"ecomxpertz"}` fallback (per degraded instructions) → N2 Meta crawl (`search_terms:"ecomxpertz"`, `"ecom xpertz"`, then `page_ids` enumeration with `ad_active_status:"ALL"`) → N3 sizing (GetHookd sizing tools skipped — no shop record) → N5/N6 open + code the one ad from Meta fields only (no GetHookd `get_ad`, since the ad is not in GetHookd's index) + one Exa `agent_run` (effort medium) reading ecomxpertz.com's own pages for `competitor_components[]`, price ladder, guarantee text and testimonials → N7/N8 write.

## §2 · ADVERTISER NETWORK MAP

| nw_id | name | page_identities[] | shared_domains[] | network_type | merge_evidence | active_ads | pct_active | longest_days_active | first_seen | competitor_quality | scale | lanes_sold |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NW-SEED-03 | EcomXpertz | [{name:"Ecomxpertz", brand_id: NULL (not in GetHookd), external_page_id:"125209367173618"}] | root: ecomxpertz.com; product: /amazon-wholesale-fba, /amazon-private-label, /shopify-dropshipping, /shopify-private-label, /facebook-marketplace, /tiktokshop-automation-with-ecomXpertz, /account-reinstatement; advertorial: NONE FOUND; funnel: NONE FOUND | BRAND | same domain (Meta page name "Ecomxpertz" ↔ domain ecomxpertz.com; page_id=external_page_id used as the only identity found) | 1 {value:1, tool:"Meta ads_library_search page_ids enum, ad_active_status:ALL", verb:"estimated_total_count/rows returned", date:"2026-09-24"} | 100% (1 active of 1 total known) | {ad_id:"1376173990650081", days:36} | 2026-08-18 [R-TOOL Meta `ad_delivery_start_time`] (only known ad; GetHookd `first_seen` UNAVAILABLE — 0 advertisers indexed for this domain) | UNCLASSIFIED — does not meet the floor for YOUNG-SCALER (needs ≥30 active ads), ESTABLISHED (needs ≥30 active + pct_active≥50%), or INCUMBENT (needs >400 active or ≥1 ad ≥180d); only 1 active ad and 1 page identity found after CRAWL COMPLETE. Not REAL-BRAND either (no Amazon-presence-of-its-own, custom product or IG following found — it is a service seller, not a product brand). | UNSIZED (no GetHookd shop record → no `monthly_visits`) | PB-01 (confident: "overwhelmed by the process", "complexities involved", "the process can be daunting" — matches lane_search_terms "shopify setup overwhelming" pattern, applied to Amazon/TikTok/FB setup instead of Shopify); PB-05 (site claims: "Product Hunting", "Identify Niche Market", "Supplier Hunting & Selection" — matches "can't find a winning product" mechanism) |

**CRAWL COMPLETE after 6 searches** (GetHookd `get_domain_advertisers{domain}` → 0; GetHookd `aggregate_ads{group_by:"brand_id", landing_page_domain}` → 0 groups; GetHookd `list_shops{q:"ecomxpertz.com"}` → 3 unrelated shops, none matching, `total:100798` confirms the query ran unfiltered/fuzzy rather than resolving the domain; GetHookd `search_ads{query:"ecomxpertz"}` → 0 rows; Meta `search_terms:"ecomxpertz"` → 1 ad, page_id 125209367173618; Meta `search_terms:"ecom xpertz"` → identical 1 ad, no new page; Meta `page_ids:["125209367173618"], ad_active_status:"ALL"` → still exactly 1 ad, confirming the whole roster). Three consecutive searches (variant spelling, page enumeration, and the ALL-status re-check) added no new page identity, domain or funnel connection. NW-APPEND: none surfaced.

`search_brands{search:"ecomxpertz"}` → **errored** (`tool_execution_failed`, "brand search took too long") — retried via `search_ads{query:"ecomxpertz", geo:"US", limit:5, compact:true}` instead (0 rows, confirming GetHookd holds no brand record under any spelling). Not retried a third time (rule: at most 3 attempts across a blocked source's chain; 2 of 3 GetHookd routes tried and exhausted before falling back fully to Meta).

## §4 · NETWORK SIZING CARD (competitor_components[])

**NW-SEED-03 · EcomXpertz (ecomxpertz.com)**
- `page_identities`: 1 (Meta page "Ecomxpertz", page_id 125209367173618) — GetHookd `brand_id`: NULL (not indexed).
- `shared_domains`: root ecomxpertz.com only; no advertorial/funnel domain found (no landing pages other than ecomxpertz.com's own service pages).
- `products[]`: NOT A PRODUCT SELLER — this is a done-for-you **service** business across several marketplaces (Amazon Wholesale FBA, Amazon Private Label, Shopify Dropshipping, Shopify Private Label, Facebook Marketplace, TikTok Shop, plus Amazon account reinstatement) — same category shape as Readymerce (service, not SKU).
- `active_ads`: 1 {tool: Meta, verb: page_ids enum ad_active_status:ALL, date: 2026-09-24} · `pct_active`: 100% (1/1) · `longest_days_active`: {ad_id 1376173990650081, days 36}.
- `first_seen`: 2026-08-18 [R-TOOL Meta] · `launch_cadence`: UNKNOWN — searched: no GetHookd `live_ads_sparkline`/`new_ads_last_7_days` (0 advertisers indexed, no brand to spy).
- `media_mix`: UNKNOWN — searched: Meta `ads_library_search` connector does not return `display_format`; ad body/media not opened (no GetHookd `get_ad_id` exists for this ad).
- `traffic`: state UNSIZED — no GetHookd shop record, no `monthly_visits`.
- `scale`: UNSIZED.
- `product_count`: NOT APPLICABLE — service business, no GetHookd shop catalogue to page.
- `price_ladder[]` (all [R-PAGE via Exa], `ecomxpertz.com/tiktokshop-automation-with-ecomXpertz` and `.../Why-Choose-EcomXpertz-for-Your-Amazon-Wholesale-FBA-Store...`, `COMPETITOR-CLAIMED`):
  - TikTok Shop Automation: **$3,000/yr** (Profit Split 70% client / 30% EcomXpertz) · **$5,000/yr** (80/20) · **$7,000/yr** (100% client profit, i.e. flat annual fee, no rev-share)
  - Amazon Wholesale FBA DFY: **$4,000/yr** (70/30) · **$6,000/yr** (80/20) · **$8,000/yr** (100% client profit)
  - Facebook Marketplace store: **custom** pricing (no figure shown) — url `ecomxpertz.com/facebook-marketplace`
  - Shopify Dropshipping, Shopify Private Label, Amazon Private Label pages were opened by Exa but carried **NO explicit price** (NONE STATED — searched).
- `ladder_shape` [D]: a 3-rung **profit-share annual retainer** — price rises as EcomXpertz's cut of client profit falls; NOT a one-time build fee like Readymerce's $500/$2,000 ([R-OWNED], 01-PRODUCT-TRUTH.md §2). This is a structurally different economic model from Readymerce's product_identity price (INFERRED $500 entry / $2,000 full launch) — flagged for step 10/12.
- `offer_apps[]`: subscription-like annual contract (Y, but rev-share not SaaS-subscription); no bundle-break, no post-purchase upsell found; NONE STATED for gifts/bumps.
- `trustpilot`: {rating: UNKNOWN, count: UNKNOWN} — BLOCKED-ON-TOOL (ca.trustpilot.com/review/ecomxpertz.com known to exist per 01-PRODUCT-TRUTH.md §3, not retrievable by any connected tool per TOOL CARD ADDENDUM).
- `top_ad_image_urls[]`: NONE — Meta `ads_library_search` connector returns no media URL field.
- `shop_created_at`: UNKNOWN.
- `competitor_quality`: UNCLASSIFIED (see §2).
- `lanes_sold[]`: PB-01, PB-05 (see §2).
- `competitor_components[]` (verbatim ≤15w claims, `[R-PAGE via Exa]`, `COMPETITOR-CLAIMED`):
  | component | claim_verbatim (≤15w) | url |
  |---|---|---|
  | headline | "Get Your Own Fully Automated Ecom Store On Leading Marketplaces!" | https://ecomxpertz.com/ |
  | guarantee (homepage) | "guaranteed to drive sales and deliver measurable results" | https://ecomxpertz.com/ |
  | guarantee (account reinstatement) | "100% Money Back Guarantee" | https://ecomxpertz.com/account-reinstatement |
  | refund policy | "full refund if the project has not been started" within 20 days | https://ecomxpertz.com/terms-and-conditions |
  | revision policy | "unlimited revisions is guaranteed. Revision turnaround time is 48 hours" | https://ecomxpertz.com/terms-and-conditions |
  | included (Amazon Wholesale FBA) | LLC Creation, Amazon Account Setup, Product Research, Supplier Research, Brand Approval, ROI Estimation, Order + Inventory Management | https://ecomxpertz.com/amazon-wholesale-fba |
  | included (TikTok automation) | LLC & EIN Application, TikTok Shop Setup, Product Hunting, Supplier Hunting, Creator/Influencer Management, Monthly Profitability Reports | https://ecomxpertz.com/tiktokshop-automation-with-ecomXpertz |
  | named problem | "overwhelmed by the process" / "the process can be daunting" (Amazon Wholesale FBA) | https://ecomxpertz.com/Why-Choose-EcomXpertz-for-Your-Amazon-Wholesale-FBA-Store-A-Complete-Done-for-You-Solution |
  | named problem | "potential account suspensions" | same URL |
  | named problem (account reinstatement page, 13 items) | Multiple Amazon Accounts, Inauthentic/counterfeit item, IP complaints, Product safety complaints, Listing mismatch, Used item sold as new, Not as advertised, Review manipulation, Negative feedback, Restricted products, Price fixing, Fulfillment-by-merchant issues | https://ecomxpertz.com/account-reinstatement |
  | testimonials | NONE STATED — Exa opened `ecomxpertz.com/ecommerce-success-stories`; page exposed reviewer names/media placeholders but **no quotable praise text** | https://ecomxpertz.com/ecommerce-success-stories |

  competitor components captured: 10 of 11 pages opened yielded a usable claim (1 page — success-stories — opened but yielded no text claim).

## §5 · CORPUS COVERAGE STATEMENT (this network)

| query | tool | params | total | count_basis | rows read | ads opened | NOT OPENED (cap) | NOT MAPPED |
|---|---|---|---|---|---|---|---|---|
| domain advertisers | GetHookd `get_domain_advertisers` | domain:ecomxpertz.com | 0 | domain_advertisers_db_roster_live | 0 | 0 | — | — |
| domain aggregate | GetHookd `aggregate_ads` | group_by:brand_id, landing_page_domain:ecomxpertz.com | 0 groups | ads_aggregate_facet_counts | 0 | 0 | — | — |
| shop lookup | GetHookd `list_shops` | q:"ecomxpertz.com", limit:3 | 100798 (unfiltered — no domain match) | shop_live_ads_linked_pages_at_last_sync | 3 (0 relevant) | 0 | — | GetHookd's `q` free-text did not resolve the bare domain to a shop row; `total:100798` shows the query effectively ran near-unscoped rather than matching "ecomxpertz.com" |
| brand search | GetHookd `search_brands` | search:"ecomxpertz" | ERROR (timeout) | — | 0 | 0 | — | tool_execution_failed |
| ad search fallback | GetHookd `search_ads` | query:"ecomxpertz", geo:US, limit:5, compact:true | 0 | explore_brand_capped_exact_sum | 0 | 0 | — | — |
| Meta keyword 1 | Meta `ads_library_search` | search_terms:"ecomxpertz", countries:[US], ACTIVE, limit:50 | estimated_total_count:1 | Meta estimated_total_count | 1 | 0 (body NOT OPENED) | — | — |
| Meta keyword 2 | Meta `ads_library_search` | search_terms:"ecom xpertz", countries:[US], ACTIVE, limit:50 | estimated_total_count:1 (same ad) | Meta estimated_total_count | 1 | 0 | — | — |
| Meta keyword 3 (context, not this network) | Meta `ads_library_search` | search_terms:"done for you shopify store", countries:[US], ACTIVE, limit:50 | estimated_total_count:64090 | Meta estimated_total_count | 50 | 0 | — | run only to test crawl completeness / surface new seeds for the orchestrator (§ below); no ecomxpertz.com hit among the 50 |
| Meta page enum | Meta `ads_library_search` | page_ids:["125209367173618"], ad_active_status:ALL, limit:50 | estimated_total_count:1 | Meta estimated_total_count | 1 | 0 (body NOT OPENED — Meta connector returns no body field; no GetHookd ad_id exists to open via `get_ad`) | 1 ad: NOT OPENED (tool) — id 1376173990650081 | — |
| landing pages | Exa `agent_run` (effort medium) | site ecomxpertz.com, 11 pages | 11 pages retrieved, 0 failed | [R-PAGE via Exa] | 11 | — | — | — |

**Counters:** networks 1 (this partial) · serious ads found 1, opened (body) 0 of 1 — `NOT OPENED (cap)` 0, `NOT OPENED (tool)` 1 · STRICT 0 (no body → cannot classify STRICT) · avatar detected 1 of 1 (from title only, `avatar_evidence: TITLE-BODY` partial) · lanes tagged 1 of 1 (PB-01) · competitor components captured 10 of 11 PDPs read.

## §6 · RANKED WINNERS — STRICT STORY (this network)

NONE — the network's only ad has no readable body/transcript (Meta connector does not return one and it is not in GetHookd's index), so STRICT-STORY bucket classification cannot be made. `swipe_candidate: N`.

## §7 · RANKED WINNERS — ALL-FORMAT (this network)

| Rank | NW | Page | Ad ID | Link | Days Active | Status | Performance | used_count | longevity_label | Big Idea | Concept | Avatar | Lanes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NW-SEED-03 | Ecomxpertz | 1376173990650081 | https://www.facebook.com/ads/library/?id=1376173990650081 | 36 | active | UNKNOWN — searched: Meta connector has no `performance_score` field | UNKNOWN | LIKELY | UNKNOWN — searched: body NOT OPENED (tool) | UNKNOWN — searched: body NOT OPENED (tool) | wants to launch an Amazon store, currently lacks confidence (INFERRED from `ad_creative_link_title` only) | PB-01 |

## §8 · INDIVIDUAL AD RECORD (IM-01, this network)

**IM-01** — bucket: **BORDERLINE** (definition: "transcript missing" — here, body/transcript entirely unavailable, only the Meta link-title field is known)
*Identification:* `im_id: IM-01, nw_id: NW-SEED-03, page_identity: Ecomxpertz, brand_id: NULL (not in GetHookd), ad_id: 1376173990650081 (Meta ad id; no GetHookd internal id exists), external_ad_id: 1376173990650081, share_url: https://www.facebook.com/ads/library/?id=1376173990650081, status: active, days_active: 36, start_date: 2026-08-18, end_date: NULL (still active), longevity_label: LIKELY, performance_score: NULL — searched: Meta connector has no field, performance_title: NULL, used_count: NULL — searched: only 1 ad total in the whole page's roster so reuse cannot be assessed against a second creative, variants_count: NULL, reuse: UNKNOWN, eu_total_reach: NULL, ad_spend_range: NULL, countries: [US] (queried scope only — Meta connector did not return a `countries` array on this row), landing_page: UNKNOWN — searched: Meta connector returns `ad_creative_link_title` but no destination URL field, landing_page_slug: NULL, destination_domain: ecomxpertz.com [D] (inferred — the network's own domain; ad title matches the site's Amazon-service pages), page_type: UNKNOWN, funnel_destination: UNKNOWN — searched: landing URL not returned by tool, tier: [R-TOOL] for identification fields, NOT OPENED (tool) for body`
*Format:* `display_format: UNKNOWN — searched (Meta connector field not returned), word_count/video_seconds: NULL, narrator_pov: NULL, native_creative_description: NULL — searched: no media returned, transcript_status: NOT AVAILABLE (no GetHookd ad_id to transcribe)`
*Argument:* ALL FIELDS NULL — searched: NOT OPENED (tool). Only field available: `ad_creative_link_title (Meta field, not necessarily the ad's true hook/opening line) = "Launch Your Amazon Store with Confidence"`.
*Avatar detection:* `avatar_addressed: wants to launch an Amazon store but lacks confidence (≤15w, INFERRED from link title only), avatar_evidence: TITLE-BODY (partial — title only, no body text available), age_audience_min/max: NULL, gender_audience: NULL, cls_who_in_ad/cls_angle/cls_story_type/cls_expert_type: NULL — searched: GetHookd classification not available (ad not in GetHookd index), cp_ids: [CP-05] (aspiring e-commerce entrepreneur who wants to skip the build — 01-PRODUCT-TRUTH.md §6), pb_ids: [PB-01]`

## §12 · INCUMBENT MECHANISM MAP (this NW row)

| nw_id | stated_cause | stated_fix | handle | named_ingredient_or_feature | awareness_entry | ad_ids[] |
|---|---|---|---|---|---|---|
| NW-SEED-03 | "overwhelmed by the process" / "the complexities involved" / "potential account suspensions" (site copy, [R-PAGE via Exa], COMPETITOR-CLAIMED) | EcomXpertz does the setup, sourcing, listing, account management and (for Amazon) suspension reinstatement for the client | NULL — searched: no named proprietary system/algorithm found on the site | NULL — service business, no named ingredient/feature; closest is the "100% Money Back Guarantee" claim | Problem-aware (site opens on the named problem, e.g. "Looking to start an Amazon Wholesale FBA business but overwhelmed by the process?") | [1376173990650081] |

## §13 · OFFER + FUNNEL TABLE (this NW)

`price_points`: $3,000 / $5,000 / $7,000 per yr (TikTok Shop, profit-split tiers); $4,000 / $6,000 / $8,000 per yr (Amazon Wholesale FBA, profit-split tiers); custom (Facebook Marketplace); NONE STATED (Shopify Dropshipping, Shopify Private Label, Amazon Private Label pages — no price shown).
`ladder_shape`: 3-rung annual profit-share retainer, ascending price ↔ descending EcomXpertz profit cut.
`guarantee`: "100% Money Back Guarantee" (account-reinstatement page) qualified by a heavily-conditioned refund policy (terms-and-conditions: full refund only if the project has not started within 20 days; void after revisions viewed; non-refundable if unresponsive >20 days, on disputes, or on urgent projects).
`gifts`: NONE STATED. `subscription`: Y (annual contract w/ profit-share, not a SaaS subscription). `funnel_split`: UNKNOWN — searched: `aggregate_ads{group_by:"page_type"}` returned 0 groups (domain not indexed by GetHookd). `penetration_offer`: NONE STATED — searched (no free/trial/low-cost entry point found on any of the 11 pages Exa opened; every service is a $3k–$8k/yr contract).

## §14 · LOSER / WINNER PAIRS (this NW)

`NONE FOUND — searched: only 1 total ad exists for this network (CRAWL COMPLETE, §2); no second ad exists to pair against.`

## §15 · KEEP-LIST (LK-##, this NW)

`LK: NONE FOUND — BLOCKED-ON-TOOL (Trustpilot)`. Exa `agent_run` also opened `ecomxpertz.com/ecommerce-success-stories` (the brand's own results/testimonial page) per the degraded-tool fallback instruction; the page exposed reviewer names and video/image placeholders but returned no quotable praise text — so the own-site fallback also yields nothing quotable. No `LK-##` rows recorded for NW-SEED-03.

## §16 · HOOK BANK (raw, this NW)

| hook_verbatim | im_id | nw_id | longevity_label | avatar_addressed |
|---|---|---|---|---|
| "Launch Your Amazon Store with Confidence" (Meta `ad_creative_link_title` field — NOT confirmed to be the ad's actual written/spoken hook; body NOT OPENED) | IM-01 | NW-SEED-03 | LIKELY | wants to launch an Amazon store but lacks confidence |

## §17 · NEIGHBOURS + NEW SEEDS (observed in passing, for the orchestrator — this scope did not crawl them)

While testing crawl completeness, Meta `search_terms:"done for you shopify store"` (estimated_total_count 64,090; 50 read) surfaced three distinct pages sharing one identical ad body/hook ("I Didn't Have a Cape. Just a Laptop and a Family to Fight For!") — a DFY-ecommerce "family income" funnel, NOT ecomxpertz.com and not part of NW-SEED-03. Printed here only as `NEW SEED` candidates for the orchestrator/KEYWORDS scope, not crawled or sized by this agent (out of this scope's budget):

| seed_id | domain | how_found | page_name(s) | queued |
|---|---|---|---|---|
| NEW SEED-A | UNKNOWN — searched: Meta connector gives no landing URL, page_name only | Meta `search_terms:"done for you shopify store"`, ACTIVE, US | Ecomfamilyhub (page_id 621287414391369), Ecomfamcrew (page_id 626035603916177), Ecom Family Academy (page_id 570801579454344) — 3 distinct pages, identical ad creative title, likely one operator running several page identities (`merge_evidence`: identical creative) | NOT CRAWLED (out of NW-SEED-03 scope/cap) |

## §18 · CREDIT RECONCILIATION + EVIDENCE LEDGER

**GetHookd:** `remaining_credits` before: 289.96 · after: 288.68 · delta: 1.28 · sum of reported `used_credits` across calls: 0.01 (domain_advertisers) + 0.01 (aggregate_ads) + 0.3 (list_shops) + 0 (search_ads) = 0.32 · **unattributed: 0.96** — likely the errored `search_brands` call (`tool_execution_failed`, timeout) was billed despite failing; not confirmed, printed as `NOT MAPPED`. Both within the ≤2.0 cr budget for this network.
**Meta Ad Library:** free (4 calls: 2 keyword searches on ecomxpertz variants, 1 keyword search on "done for you shopify store" for crawl-completeness/new-seed context, 1 page_ids enumeration).
**Exa agent:** 1 run of ≤6 budgeted, effort medium, cost **$0.10** (well under the ≤$0.60 cap), 12 searches, 11 pages retrieved, 0 failed.

**Evidence ledger:**
- Ad: id 1376173990650081, share_url https://www.facebook.com/ads/library/?id=1376173990650081
- Landing/PDP pages read (Exa, [R-PAGE via Exa]): https://ecomxpertz.com/ · https://ecomxpertz.com/terms-and-conditions · https://ecomxpertz.com/account-reinstatement · https://ecomxpertz.com/amazon-wholesale-fba · https://ecomxpertz.com/facebook-marketplace · https://ecomxpertz.com/tiktokshop-automation-with-ecomXpertz · https://ecomxpertz.com/ecommerce-success-stories · https://ecomxpertz.com/amazon-private-label · https://ecomxpertz.com/Why-Choose-EcomXpertz-for-Your-Amazon-Wholesale-FBA-Store-A-Complete-Done-for-You-Solution · https://ecomxpertz.com/shopify-dropshipping · https://ecomxpertz.com/shopify-private-label
- Known-not-retrievable: https://ca.trustpilot.com/review/ecomxpertz.com — BLOCKED-ON-TOOL (Trustpilot).

Counts keep their `count_basis` and are never added or compared across tools.

## COVERAGE STATEMENT (SCOPED — NW-SEED-03)

COVERAGE: networks 1 (ABOVE-FLOOR 0 · UNSIZED 1) from 1 seed and 9 queries (3 GetHookd domain/shop/brand routes + 1 GetHookd search_ads fallback + 4 Meta ads_library_search calls + 1 Exa agent_run); serious ads 1 found, 0 opened (body) — `NOT OPENED (tool)` 1 (id 1376173990650081, Meta connector returns no body field and the ad is not in GetHookd's index so `get_ad`/`transcribe_ad` cannot reach it); STRICT 0 (no body available to classify); avatar detected 1 of 1 (TITLE-BODY, partial); lanes covered 1 of 3 seed lanes (PB-01 confident; PB-05 suggested by site copy but not by the one ad itself); competitor components captured 10 of 11 PDPs read; new seeds 1 (NEW SEED-A, NOT CRAWLED — cap/out of scope); credits spent: GetHookd 1.28 of ≤2.0 (reported 0.32, unattributed 0.96 — NOT MAPPED, likely the errored `search_brands` call), Meta $0 (free), Exa $0.10 of ≤$0.60 (1 of ≤6 runs); NOT MAPPED: GetHookd `search_brands` timeout cost, exact landing-page URL of the one ad (Meta connector limitation), the ad's body/transcript (VALIDATION-DEGRADED — GetHookd does not index this domain); counts keep their `count_basis` and are never added across tools; CONFIDENCE: network map [PARTIAL — sized entirely from Meta + Exa, no GetHookd traffic/shop data exists for this domain], winners [FULL-BODY 0 of 1], coverage map [1 persona cell (CP-05), 0 VACANT for this network — persona/lane VACANT status is a MERGE-level judgment across all networks, not assessable from one network alone] because GetHookd holds zero indexed data for ecomxpertz.com (VALIDATION-DEGRADED, confirmed by three independent GetHookd calls returning 0/irrelevant rows) and the Meta Ad Library connector returns identification fields only, never ad body text.
