# 02-COMPETITOR-INTEL — Partial · SCOPE: NW-SEED-01 (ecomdoneforyou.com)

agent_id: 02-NW-SEED-01 · wave W1 · model: sonnet · started: 2026-09-24T20:27:23Z
LOCK CARD: VALIDATION-DEGRADED (GetHookd does not index this domain/brand under any query tried; Meta Ad Library returns 0 ads for the literal domain and unrelated noise for broader phrase terms). Trustpilot/reviews.io pages for this seed are BLOCKED-ON-TOOL (not retrievable by any connected tool, per binding addendum). PDP evidence comes from the Exa research agent (1 run, effort medium, $0.10), which DID successfully open 8 pages on ecomdoneforyou.com.

## §1 · INPUT CARD + SEARCH PLAN

- PRODUCT NAME: Readymerce · TARGET MARKET: US (ASSUMED) · SCOPE: NW-SEED-01
- Seed confirmed from `/home/user/main/runs/readymerce/foundation/01-HANDOFF.json` → `competitor_seeds[0]` = ecomdoneforyou.com; `01-PRODUCT-TRUTH.md` §3 → seed_id **NW-SEED-01**, how_found: web search 'done for you ecommerce store business service reviews' → trustpilot.com/review/ecomdoneforyou.com + reviews.io/company-reviews/store/ecomdoneforyou.com; page_name "Ecom Done For You"; pdp NOT FETCHED at 01 (WebFetch egress-blocked at that time).
- Inputs read (per rule 6, HANDOFF-first): `01-HANDOFF.json` (product_identity, competitor_seeds, problem_lanes+lane_search_terms, search_key_set) · `01-PRODUCT-TRUTH.md` §3 (seed row), §5 (PB-01/PB-06/PB-05 cards + HYPOTHESIS PB-02/03/04/07), §6 (CP-01..CP-07), §7 (lead_problem_hypothesis PB-01, lane_search_terms), §8 (search_key_set + swap_table_v0). `01-partials/01-HANDOFF.DEEP.json` does not exist → `difference_sheet: LATE-BOUND`.
- MAX_IM_RECORDS: 40 (ASSUMED per brief, this partial) · MAX_PER_NETWORK: 30 · GetHookd budget: ≤2.0 credits (used 0.66, see §18) · Exa budget: ≤6 runs / ≤$0.60 (used 1 run, $0.10).
- Plan: N1 discover from seed domain (get_domain_advertisers, aggregate_ads, list_shops) → N2 crawl to end → N3 size → N4 three rankings → N5 open ads batch → N6 classify → N7 per-network objects → N8 write. Executed exactly this order; N4/N5/N6 could not run because N1–N2 surfaced zero ads (see below).

## §2 · ADVERTISER NETWORK MAP

| nw_id | name | page_identities | shared_domains | network_type | merge_evidence | active_ads | pct_active | longest_days_active | first_seen | competitor_quality | scale | lanes_sold |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NW-SEED-01 | Ecom Done For You | "Ecom Done For You" (facebook.com/Ecomdoneforyou1, ~1,197 page likes [R-SNIPPET via WebSearch]); brand_id UNKNOWN (not indexed in GetHookd) | root: ecomdoneforyou.com; subpages seen: /walmart-wfs-automation, /amazon-fba-automation, /shopify-automation, /amazon-store-management-services, /contact-us, /refund-policy.php (no separate funnel/advertorial domain found — none needed, since no ads were found to reveal one) | BRAND | same domain (PDP + FB page both resolve to ecomdoneforyou.com per WebSearch) | COUNT-UNKNOWN — GetHookd `get_domain_advertisers`: 0 rows; `aggregate_ads{group_by:brand_id, landing_page_domain:ecomdoneforyou.com}`: 0 groups; Meta `ads_library_search{search_terms:"ecomdoneforyou.com", ad_active_status:ALL}`: estimated_total_count 0 | UNKNOWN — no ad rows to compute from | NONE FOUND | UNKNOWN — searched (no `get_domain_advertisers.first_seen`, domain not indexed) | UNKNOWN — insufficient signal: no active-ad count, no first-seen date, no traffic figure computable from any connected tool (competitor_quality requires exactly this data per §3 definitions) | UNSIZED (no `list_shops.monthly_visits` row exists for this domain — rule 10) | PB-01, PB-05 (COMPETITOR-CLAIMED, from PDP text); PB-06 touched only via the ROI guarantee, not a named problem |

**CRAWL COMPLETE after 8 searches** (0 new page identities, 0 new domains beyond the seed root + its one known FB page): `get_domain_advertisers{domain}` → 0 · `aggregate_ads{group_by:brand_id, landing_page_domain}` → 0 groups · `list_shops{q:"ecomdoneforyou.com"}` → 0 relevant (3 unrelated rows returned: gocase.com.br, toryburch.com, microperfumes.com) · `list_shops{q:"Ecom Done For You"}` → 0 relevant (3 unrelated rows: microjingles.com, pourcaddy.com, arcadymedia.com — all matched only because their taglines contain the phrase "done for you") · `search_brands{search:"ecom done for you"}` → tool_execution_failed (timeout), retried `search_brands{search:"ecomdoneforyou"}` → tool_execution_failed (timeout; 2 attempts, per rule 13 cap of 3 not exceeded, third attempt not made — diminishing returns) · `search_ads{query:"ecom done for you", geo:US}` → 5 rows returned, all unrelated brands (SocialToast.ai, Ecom Websites — DIFFERENT DFY-ecom competitors, NOT ecomdoneforyou.com; flagged as `NEW SEED` candidates for the orchestrator, not sized further here — out of this scope) · Meta `ads_library_search{search_terms:"ecom done for you"}` and `{search_terms:"Ecom Done For You"}` → near-identical noise sets of unrelated pages (Total Fitness Kickboxing, Zoe Sasha, etc. — estimated_total_count ~41.7k, confirming loose/semantic matching, not a page-name filter) · Meta `ads_library_search{search_terms:"ecomdoneforyou.com", ad_active_status:ALL}` → estimated_total_count **0** (clean negative, confirms the domain literal appears in zero ad creatives Meta's connector can see). NW-APPEND: none surfaced.

## §3 · NW-APPEND (brands found while searching this seed, NOT part of NW-SEED-01 — logged for the orchestrator)

`search_ads{query:"ecom done for you"}` surfaced two unrelated but topically-adjacent DFY-ecom advertisers not in `competitor_seeds[]`: **SocialToast.ai** (brand_id in ad 44372497; AI/sales-automation for existing e-com brands, not a store-build service — poor fit) and **Ecom Websites** (brand_id linked to ads 97210901/97210897/97210898/70823628; landing pages build.ecomwebsites.com / get.ecomwebsites.com; "$20 done-for-you eCommerce store", 40,000+ built per ad claim, ad_spend_range_score_title "0-$500", longest ad 169 days_active, used_count 2 — a much closer product match to Readymerce than NW-SEED-01 itself). Printed here as `NEW SEED` candidates per §4-object-12; NOT crawled or sized under this scope (out of SCOPE: NW-SEED-01) — the orchestrator/KEYWORDS agent should queue `NEW SEED-01: ecomwebsites.com` if budget allows.

## §4 · NETWORK SIZING CARD — NW-SEED-01

- **Identity:** Ecom Done For You · ecomdoneforyou.com · FB page facebook.com/Ecomdoneforyou1 (~1,197 likes) [R-SNIPPET via WebSearch, not independently verified by GetHookd/Meta]
- **products[]:** Amazon FBA automation, Amazon store management, Walmart WFS automation, Shopify automation/store build [R-PAGE via Exa]
- **price_ladder[]:** Walmart automation services $2,000 [R-PAGE via Exa, url: ecomdoneforyou.com/walmart-wfs-automation]; all other service prices NOT STATED on the pages Exa could open (pricing/services pages returned not-retrievable — see `pages_failed` below); 01-PRODUCT-TRUTH.md §3 additionally carries an UNRESOLVED-attribution WebSearch fragment ("$257 after a $20 Facebook ad escalated into upsells for a Diamond VIP bundle... AutoDS automation") that names a $20 entry ad — but that fragment is about a DIFFERENT competitor ("Ecom Websites" / "Ecomwebsites Reviews" per the same search), not confirmed as ecomdoneforyou.com, so it is NOT added to this network's ladder (basis discipline, rule 12).
- **offer_apps[]:** none identified (no bundle-break/subscription/post-purchase upsell language found on the pages read)
- **guarantee:** "100% ROI guarantee within 6 months" — conditional (void on customer unresponsiveness >2 weeks, policy violations, "change of mind"; may substitute store credit/discounts instead of cash refund) [R-PAGE via Exa, url: ecomdoneforyou.com/refund-policy.php] COMPETITOR-CLAIMED
- **trustpilot:** rating/count NOT VERIFIED by any connected tool this run — WebSearch snippet claims "4.2 rating based on 23 reviews" on trustpilot.com/review/ecomdoneforyou.com and "8 reviews... average score of 5.00" on reviews.io/company-reviews/store/ecomdoneforyou.com [R-SNIPPET], but the pages themselves are BLOCKED-ON-TOOL (binding addendum: Trustpilot not retrievable by any connected tool) so these are UNVERIFIED SNIPPET SUMMARIES, not read in full, and are NOT promoted to a verbatim keep-list (see §15).
- **shop_created_at / first_seen:** UNKNOWN — searched (no GetHookd shop record, no `get_domain_advertisers.first_seen`)
- **competitor_quality:** UNKNOWN — cannot compute (needs active-ad count + first-seen + pct_active + traffic, none available)
- **competitor_components[]** (COMPETITOR-CLAIMED, ≤15w each, all [R-PAGE via Exa]):

| component | claim_verbatim (≤15w) | url |
|---|---|---|
| Amazon FBA suppliers | "develops relationships with top manufacturers to source products" | ecomdoneforyou.com/amazon-fba-automation |
| Amazon FBA supplier screening | "advanced AI tools to look for manufacturers that are not fraudulent" | ecomdoneforyou.com/amazon-fba-automation |
| Amazon FBA product research | "advanced enough to conduct a market analysis" for "the perfect product" | ecomdoneforyou.com/amazon-fba-automation |
| Amazon FBA profit margin | "target a 20% profit margin for every customer" | ecomdoneforyou.com/amazon-fba-automation |
| Shopify product listing | "upload bulk products with descriptions, graphics, pricing, and variants" | ecomdoneforyou.com/shopify-automation |
| Walmart product research | "compare the supplier costs, calculate profitability, and refine the search" | ecomdoneforyou.com/walmart-wfs-automation |
| Walmart product listing | "craft a compelling product description" for every product | ecomdoneforyou.com/walmart-wfs-automation |
| Walmart WFS | "Walmart handles storage, packing, shipping, and customer support" | ecomdoneforyou.com/walmart-wfs-automation |
| Site build | "Complete W3C Certified HTML" | ecomdoneforyou.com |
| Ongoing catalog mgmt | "Add new Suppliers and Products" | ecomdoneforyou.com |

- **headline_claim (verbatim):** "Ecom Done For You — Get Your Fully Automated E-Commerce Store on Top Marketplaces" [R-PAGE via Exa, ecomdoneforyou.com]
- **named_problems[] (verbatim/near-verbatim, COMPETITOR-CLAIMED):** "manual processes slow you down or create costly mistakes" · "process depends on multiple people and constant manual effort" · "store runs on multiple channels and needs unified automation" · "manual operations often lead to stock issues, incorrect details, and delayed updates" · "running a Shopify store revolves around many repetitive tasks... annoying for every entrepreneur" · "product listing and customer support consume hours that can be dedicated to scaling" · "pricing is something most sellers at Walmart don't focus on" · "without an advanced reporting tool, it is next to impossible to scale your business"
- **what's-included lines (verbatim):** "Walk through all the Steps" · "Fulfilling Requirements for Store Setup" · "Onboarding & Business Setup" · "Listing Setup & Product Launch" · "Complete W3C Certified HTML" · "A working capital strategy set" · "Add new Suppliers and Products" · "2x your Profitability" · "Double your investment to Triple your Profits" (offer-context language, no price attached)
- **Exa pages_opened (8):** ecomdoneforyou.com, /index.php, /walmart-wfs-automation, /amazon-fba-automation, /shopify-automation, /amazon-store-management-services, /contact-us, /refund-policy.php
- **Exa pages_failed / NOT RETRIEVABLE (7):** /pricing, /services, /reviews, /results, /testimonials, /pricing.php, /services.php — no full price list or on-site testimonials page could be read.

## §5 · CORPUS COVERAGE STATEMENT (this network)

| query | tool | params | total | count_basis | rows read | ads opened | NOT OPENED (cap) | NOT MAPPED |
|---|---|---|---|---|---|---|---|---|
| domain advertisers | GetHookd `get_domain_advertisers` | domain=ecomdoneforyou.com | 0 | domain_advertisers_db_roster_live | 0 | 0 | — | — |
| brand aggregate | GetHookd `aggregate_ads` | group_by=brand_id, landing_page_domain=ecomdoneforyou.com | 0 groups | ads_aggregate_facet_counts | 0 | 0 | — | — |
| shop lookup | GetHookd `list_shops` | q="ecomdoneforyou.com", limit=3 | 100,798 (catalog-wide; 0 of 3 returned rows relevant) | shop_live_ads_linked_pages_at_last_sync | 3 (0 relevant) | 0 | — | — |
| shop lookup | GetHookd `list_shops` | q="Ecom Done For You", limit=3 | 19 (catalog match on "done for you" tagline text; 0 of 3 relevant) | shop_live_ads_linked_pages_at_last_sync | 3 (0 relevant) | 0 | — | — |
| brand search | GetHookd `search_brands` | search="ecom done for you" / "ecomdoneforyou" | ERROR (tool_execution_failed ×2, timeout) | — | 0 | 0 | — | brand catalog NOT MAPPED for this name |
| keyword search | GetHookd `search_ads` | query="ecom done for you", geo=US, limit=5 | 488 (brand-capped) | explore_brand_capped_exact_sum | 5 (0 = this network; 2 = NW-APPEND candidates) | 0 | — | — |
| Meta library | Meta `ads_library_search` | search_terms="ecom done for you", countries=[US], ACTIVE | 41,729 | Meta explore counter (loose/semantic match) | 5 read | 0 (0 relevant) | — | noise, not this network |
| Meta library | Meta `ads_library_search` | search_terms="Ecom Done For You", countries=[US], ACTIVE | 41,681 | same | 5 read | 0 (0 relevant) | — | noise, not this network |
| Meta library | Meta `ads_library_search` | search_terms="ecomdoneforyou.com", countries=[US], ALL | **0** | same | 0 | 0 | — | clean negative |
| PDP crawl | Exa agent (medium effort, 1 run) | 8 target pages on ecomdoneforyou.com | 8 opened / 7 failed | R-PAGE via Exa | 8 pages | n/a (PDP, not ads) | — | pricing/services/reviews pages NOT MAPPED (not retrievable) |
| brand FB page | WebSearch | "ecomdoneforyou" site:facebook.com | 1 relevant hit (facebook.com/Ecomdoneforyou1) | R-SNIPPET | 1 | n/a | — | numeric page_id NOT MAPPED (WebFetch/browser blocked, could not open the page to read it) |

**Serious ads found: 0.** No ad met the §3 "serious ad" bar because no ad from this brand was located by any connected tool. IM-## records: 0. This is a data-availability floor miss, not a market judgment — printed as `PARTIAL (N=0/floor) — chain exhausted: [GetHookd domain/brand/shop index has no record; Meta Ad Library literal-domain search returns estimated_total_count 0; WebFetch/Browserbase egress-blocked so the FB page itself could not be opened to find a page_id for `page_ids:[...]` enumeration]`.

## §6-8 · RANKED WINNERS (STRICT / ALL-FORMAT) — this network's column

`NONE FOUND — searched:` all queries in §5. Zero ads open, zero winners rankable for NW-SEED-01. (Note: the two NW-APPEND brands surfaced incidentally — SocialToast.ai ad 44372497, 289 days_active, CONTROL-GRADE-band by longevity; Ecom Websites ad 70823628, 169 days_active, PROVEN-band — are NOT this network's ads and are excluded from NW-SEED-01's rankings; they are logged in §3 for the orchestrator.)

## §9 · INDIVIDUAL AD RECORDS (IM-##)

None. 0 serious ads found for this network (see §5). `02-swipe.NW-SEED-01.csv` ships header-only, 0 data rows.

## §10 · AVATAR / PROBLEM-LANE COVERAGE COLUMN (NW-SEED-01)

No ad-level avatar detection was possible (0 ads). PDP-level evidence only (COMPETITOR-CLAIMED, not ad-level, so it does NOT feed the avatar coverage map's ad-count cells at merge — recorded here for 03's use):

| persona/lane | cell (PDP evidence only — not an ad count) |
|---|---|
| PB-01 (can't build/set up store) | PDP claims "repetitive tasks" + full store-build/automation as the fix — COMPETITOR-CLAIMED, 0 ads to corroborate |
| PB-05 (don't know what to sell) | PDP claims product-research + supplier vetting for Amazon/Walmart — COMPETITOR-CLAIMED, 0 ads to corroborate |
| PB-06 (no sales/traffic) | touched only via the "100% ROI guarantee within 6 months" — COMPETITOR-CLAIMED, thin |
| PB-04 (busy owner, operational time burden — HYPOTHESIS PB, not a lane) | PDP claims "consume hours that can be dedicated to scaling" — COMPETITOR-CLAIMED |

`independent_networks` contribution of NW-SEED-01 to any persona/lane at merge: **0** (an UNSIZED, 0-ad network never counts toward "independent means ABOVE-FLOOR" per rule 1, but per rule 1 it is also never discarded — it ships as a PDP-only, ad-free data point).

## §11 · KEYWORD ADVERTISER BANDS

Out of scope for `NW-SEED-01` (object 6 is `[KW]`-scoped; owned by the KEYWORDS-scope agent). Not duplicated here.

## §12 · INCUMBENT MECHANISM MAP (this network's row)

| nw_id | stated_cause | stated_fix | handle | named_ingredient_or_feature | awareness_entry | ad_ids |
|---|---|---|---|---|---|---|
| NW-SEED-01 | "manual processes slow you down or create costly mistakes"; "process depends on multiple people and constant manual effort" [D from PDP, COMPETITOR-CLAIMED] | full automation of store build, listing, supplier sourcing and ongoing catalog management across Shopify/Amazon/Walmart | "Fully Automated E-Commerce Store on Top Marketplaces" | AI-assisted supplier screening ("advanced AI tools to look for manufacturers that are not fraudulent") | UNKNOWN — searched: no ad copy available to read where the conversation starts (PDP is Product/Most-aware register: assumes the reader already knows what "Amazon FBA automation" and "Walmart WFS" mean) | none (no ads found) |

## §13 · OFFER + FUNNEL TABLE (this network's row)

| nw_id | price_points[] | ladder_shape | guarantee | gifts | subscription | funnel_split | penetration_offer |
|---|---|---|---|---|---|---|---|
| NW-SEED-01 | $2,000 (Walmart automation, only price stated) [R-PAGE via Exa]; other tiers UNKNOWN — searched: pricing/services pages not retrievable | UNKNOWN — searched: only 1 of N price points visible | "100% ROI guarantee within 6 months" (conditional; store-credit/discount substitution allowed; void on non-response >2 weeks or policy breach) | none stated | N (not stated) | UNKNOWN — searched: no ads/landing funnel data (0 ads found; `aggregate_ads{group_by:page_type}` not run — no ads to scope it to) | NONE STATED — searched (no low-ticket entry offer like competitors' "$20 store" language found on ecomdoneforyou.com itself; that language belongs to the different brand "Ecom Websites", §3) |

## §14 · LOSER / WINNER PAIRS

`NONE FOUND — searched:` (0 ads; floor requires ≥1 pair per ABOVE-FLOOR network, and this network is UNSIZED/0-ad, so the floor does not apply — printed per rule 3 regardless).

## §15 · KEEP-LIST (LK-##)

`LK: NONE FOUND — BLOCKED-ON-TOOL (Trustpilot)`. Attempted per the degraded-tool instruction: (1) Trustpilot/reviews.io pages for ecomdoneforyou.com are confirmed by the binding TOOL CARD ADDENDUM to be unretrievable by any connected tool this run (the Exa agent has already tried and reported failure for this class of page in earlier steps); not re-attempted a second time (rule: do not send Reddit/Trustpilot URLs to Exa more than once run-wide). (2) One Exa run was made on the brand's own site asking explicitly for a testimonials/results/reviews page — it tried `/reviews`, `/results`, `/testimonials` and all three came back in `pages_failed` (not retrievable / do not exist at those paths) — `testimonial_quotes: []`. No verbatim on-site praise quote exists to file. WebSearch snippets state "4.2 rating (23 reviews)" on Trustpilot and "5.00 avg (8 reviews)" on reviews.io, but these are counts only, not quotes, and the pages cannot be opened to pull a verbatim line — not promoted to LK per rule 2 (never invent/paraphrase a quote).

## §16 · HOOK BANK (raw)

None. 0 ads found for this network.

## §17 · NEIGHBOURS + NEW SEEDS

Owned by KEYWORDS scope; not run here. NW-APPEND candidates surfaced incidentally are logged in §3 (SocialToast.ai, Ecom Websites / ecomwebsites.com) for the orchestrator to queue if in budget.

## §18 · CREDIT RECONCILIATION + EVIDENCE LEDGER

**GetHookd credits (this agent's calls only):** `get_user_profile` (before) remaining_credits=290.62 → `get_user_profile` (after) remaining_credits=288.68. Delta over the session = 1.94, but this account is shared across the whole `readymerce` W1 run (parallel sibling seed/KEYWORDS agents draw from the same 291-credit pool), so the delta is NOT attributable to this agent alone. **This agent's own reported `used_credits` sum: 0.66** — `list_shops×2` (0.3+0.3=0.6) + `get_domain_advertisers` (0) + `aggregate_ads` (0.01) + `search_ads` (0.05) + `search_brands×2` (0, both errored) = **0.66 of the ≤2.0 cap for this network** — well within budget. Unattributed delta (1.94 − 0.66 = 1.28) = other agents' concurrent usage, not this scope's.

**Exa agent:** 1 run, effort medium, cost $0.10 of the ≤$0.60 (≤6 runs) cap for this network. 8 pages opened, 7 pages failed (see §4).

**WebSearch:** 5 calls (free, no floor/cap) — "ecomdoneforyou.com facebook page ads" (no direct hit), "ecomdoneforyou.com reviews price" (Trustpilot/reviews.io existence + rating snippets), "ecomdoneforyou site:facebook.com" (found facebook.com/Ecomdoneforyou1), "facebook.com/Ecomdoneforyou1 page id" (no numeric id recoverable, WebFetch/Browserbase blocked so the page itself could not be opened).

**Meta Ad Library:** 3 calls (free) — see §5.

**Evidence ledger (every URL read this scope):**
- https://ecomdoneforyou.com [R-PAGE via Exa]
- https://ecomdoneforyou.com/index.php [R-PAGE via Exa]
- https://ecomdoneforyou.com/walmart-wfs-automation [R-PAGE via Exa]
- https://ecomdoneforyou.com/amazon-fba-automation [R-PAGE via Exa]
- https://ecomdoneforyou.com/shopify-automation [R-PAGE via Exa]
- https://ecomdoneforyou.com/amazon-store-management-services [R-PAGE via Exa]
- https://ecomdoneforyou.com/contact-us [R-PAGE via Exa]
- https://ecomdoneforyou.com/refund-policy.php [R-PAGE via Exa]
- https://www.facebook.com/Ecomdoneforyou1/ [R-SNIPPET via WebSearch, not opened]
- https://www.trustpilot.com/review/ecomdoneforyou.com [R-SNIPPET via WebSearch, BLOCKED-ON-TOOL to open]
- https://www.reviews.io/company-reviews/store/ecomdoneforyou.com [R-SNIPPET via WebSearch, BLOCKED-ON-TOOL to open]
- No ad share_urls — 0 ads found for this network.

Ad ids read that belong to OTHER brands (NW-APPEND, §3, not this network): SocialToast.ai ad 44372497 (https://app.gethookd.ai/share/ad/44372497); Ecom Websites ads 97210901, 97210898, 97210897, 70823628 (https://app.gethookd.ai/share/ad/{id}).

## COVERAGE STATEMENT (NW-SEED-01)

COVERAGE: networks 1 (ABOVE-FLOOR 0 · UNSIZED 1) from 1 seed and 11 queries (3 GetHookd shop/brand lookups relevant-zero, 2 GetHookd brand-index calls, 2 GetHookd search_brands errors, 1 GetHookd search_ads keyword call, 3 Meta ads_library_search calls, 1 Exa PDP-crawl run, 5 WebSearch calls); serious ads 0 found, 0 opened, NOT OPENED (cap) 0; STRICT 0; avatar detected 0 of 0; lanes covered 2 of 3 (PB-01, PB-05 directly claimed on the PDP; PB-06 touched only via the ROI guarantee — COMPETITOR-CLAIMED, not ad-validated); competitor components captured 10 of 1 PDP (root domain + 4 sub-pages read as one PDP unit); new seeds 2 (NOT CRAWLED — SocialToast.ai, ecomwebsites.com — logged §3 for the orchestrator, out of this scope's budget); credits spent 0.66 GetHookd (reported 0.66, cap 2.0) + $0.10 Exa (cap $0.60) + $0.00 Meta + $0.00 WebSearch; NOT MAPPED: this network's active-ad count, first-seen date, monthly traffic, Trustpilot verbatim quotes, full price ladder (pricing/services pages unretrievable), numeric Facebook page_id (WebFetch/Browserbase egress-blocked); counts keep their count_basis and are never added across tools; CONFIDENCE: network map [PARTIAL — identity and PDP claims confirmed via WebSearch+Exa, but ad-level sizing (active_ads, pct_active, longevity, competitor_quality) is COUNT-UNKNOWN/UNSIZED because neither GetHookd nor Meta Ad Library indexes any ad for this domain or page, and the FB page itself could not be opened to resolve a numeric page_id for a page_ids enumeration], winners [FULL-BODY 0 of 0 — no ads exist to open], coverage map [4 problem lanes/PBs touched by PDP claims only, 0 personas VACANT-tested at ad level since 0 ads exist to search avatars in] because this network appears to run no (or no currently-library-visible) paid Meta advertising, so this partial documents its organic PDP/offer claims in full while flagging the ad-intelligence objects as a genuine data-floor miss (VALIDATION-DEGRADED), not a market judgment about NW-SEED-01's spend.
