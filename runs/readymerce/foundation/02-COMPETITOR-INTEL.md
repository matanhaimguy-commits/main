# 02 — COMPETITOR INTELLIGENCE · Readymerce · scope ALL (MERGED by agent 03, MODE: MERGE, wave W2)
LOCK CARD: merge = concatenation + dedupe + renumbering of 9 partials (8 NW + KEYWORDS); no re-research. Tools used at merge: GetHookd get_user_profile (free), get_ad ×3 (free, re-opened bodies the partials had already opened), search_ads ×2 charged (0.05 each, both to resolve NAMED ambiguities, printed §5/§18). BLOCKED-ON-TOOL (addendum): Apify, Firecrawl scrape, Browserbase, WebFetch/curl; not called. VALIDATION-DEGRADED: the three original seeds (NW-05, NW-07, NW-08) carry 1, 0 and 0 ads — printed, not hidden.
## §1 · INPUT CARD + SEARCH PLAN + MERGE MAP
| field | value | state |
|---|---|---|
| PRODUCT NAME | Readymerce (readymerce.com) — DFY Shopify/Etsy store service | GIVEN |
| TARGET MARKET | US · USD · en | ASSUMED |
| SCOPE | ALL (merge of 9 partials) | GIVEN (brief) |
| MAX_IM_RECORDS / MAX_PER_NETWORK | 120 / 30 | ASSUMED (02 §2 defaults) |
| inputs | 02-partials/* (8 NW partials + KEYWORDS: .json, .md, swipe CSVs) · 01-HANDOFF.json · 01-partials/01-HANDOFF.DEEP.json | read |
| our own network (NOT a competitor row) | Readymerce Meta page_id 923106680896349 · 31 active ads (Meta estimated_total_count) · ILS billing · link title "We build it. We run it. You own it." (02-KEYWORDS §17) | [R-TOOL] reference row only |

**Search plan (as executed by the partials):** lanes L=3 searched (PB-01, PB-06, PB-05; buyer + clinical forms) + 5 avatar phrases (CP-02 fathers/parents, CP-06 near-retirement) in KEYWORDS; 3 original seeds + 5 NEW SEEDs crawled to their printed ends.

**Counter:** partials 9 of 9 expected · NW 8 → 8 after dedupe (root domains all distinct: ecomdegree.com, ecomfamily.com [D unresolved], ecomaccelerator.io, doneforyoubrands.co, ecomxpertz.com, ecomwebsites.com, ecomdoneforyou.com, ecommerceparadise.com) · IM 32 (30 partial rows incl. 1 DCO-variant row + 2 NW-APPEND ad rows surfaced by merge search #1) · NEW SEED 11 surfaced (5 crawled → NW-01..04, NW-06; NOT CRAWLED 5; off-topic logged 1)

**MERGE-WATCH (not merged — root domains differ):** NW-04 (doneforyoubrands.co) and NW-06 (ecomwebsites.com) share one playbook — "$20/free store, Shopify pays us a commission" (NW-04 ad body [D]; NW-06 IM-31) — and NW-04's funnel testimonial page is titled "DFY Ecom Websites" (02-NW-NEW-SEED-03 §15). Possible single operator, UNCONFIRMED. Every independence count below is printed as-is; collapsing this pair would reduce the DFY low-ticket networks from 2 to 1. Cameron Hoffman - Business (page 1134544756404510) runs NW-03's identical creative on Meta; merge search #1 did not surface it on GetHookd → NOT MERGED, NOT CRAWLED.

### partial_id → id map (networks, ordered by active_ads desc; each partial's printed line and count_basis kept; COUNT-UNKNOWN last)
| partial_id | → nw_id | name | active_ads line (value · tool/basis · date) |
|---|---|---|---|
| NW-NEW-SEED-05 | NW-01 | Ecom Degree University | 203 · GetHookd get_brand active_ads · 2026-09-23 (210 GetHookd exact total; 262 Meta estimated — never added) |
| NW-NEW-SEED-02 | NW-02 | Ecom Family net | 160 · Meta per-page ACTIVE estimated_total_count 48+54+58 · 2026-09-24 |
| NW-NEW-SEED-04 | NW-03 | Ecom Accelerator | 85 · GetHookd brand.active_ads · 2026-09-24 (domain-scoped 29/46 — never added) |
| NW-NEW-SEED-03 | NW-04 | Done for you brands | 32 · GetHookd brand.active_ads · 2026-09-24 (Meta 35) |
| NW-SEED-03 | NW-05 | EcomXpertz | 1 · Meta page_ids enumeration · 2026-09-24 |
| NW-NEW-SEED-01 | NW-06 | Ecom Websites | 0 current · GetHookd + Meta · 2026-09-24 (historical 922 GetHookd / 627 Meta — not comparable) |
| NW-SEED-01 | NW-07 | Ecom Done For You | COUNT-UNKNOWN (GetHookd 0 rows; Meta 0) |
| NW-SEED-02 | NW-08 | Ecommerce Paradise | COUNT-UNKNOWN (NOT INDEXED; Meta 0/3 matched) |

### partial IM → IM-## (by NW, then days_active desc) and concept → CO-## (unique per NW)

| partial_id | partial im | ad_id | → im_id | nw_id | → CO | days | longevity (merged; INCUMBENT drop applied) |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-05 | IM-02 | 121358569 | IM-01 | NW-01 | CO-01 (was CO-08) | 70 | PROVEN |
| NW-NEW-SEED-05 | IM-04 | 126787289 | IM-02 | NW-01 | CO-01 (was CO-08) | 68 | PROVEN |
| NW-NEW-SEED-05 | IM-01 | 121358672 | IM-03 | NW-01 | CO-02 (was CO-01) | 63 | PROVEN |
| NW-NEW-SEED-05 | IM-03 | 134426761 | IM-04 | NW-01 | CO-01 (was CO-08) | 60 | PROVEN |
| NW-NEW-SEED-05 | IM-13 | 134427111 | IM-05 | NW-01 | CO-01 (was CO-08) | 60 | PROVEN |
| NW-NEW-SEED-05 | IM-14 | 134426818 | IM-06 | NW-01 | CO-03 (was CO-02) | 60 | PROVEN |
| NW-NEW-SEED-05 | IM-07 | 134426835 | IM-07 | NW-01 | CO-04 (was CO-04) | 57 | PROVEN |
| NW-NEW-SEED-05 | IM-06 | 144205353 | IM-08 | NW-01 | CO-05 (was CO-03) | 48 | PROVEN |
| NW-NEW-SEED-05 | IM-05 | 159706760 | IM-09 | NW-01 | CO-03 (was CO-02) | 31 | LIKELY |
| NW-NEW-SEED-05 | IM-08 | 169343657 | IM-10 | NW-01 | CO-06 (was CO-05) | 24 | LIKELY |
| NW-NEW-SEED-05 | IM-09 | 169343649 | IM-11 | NW-01 | CO-05 (was CO-03) | 24 | LIKELY |
| NW-NEW-SEED-05 | IM-10 | 169343631 | IM-12 | NW-01 | CO-07 (was CO-06) | 24 | LIKELY |
| NW-NEW-SEED-05 | IM-11 | 169343626 | IM-13 | NW-01 | CO-05 (was CO-03) | 24 | LIKELY |
| NW-NEW-SEED-05 | IM-12 | 169343625 | IM-14 | NW-01 | CO-08 (was CO-07) | 24 | LIKELY |
| NW-NEW-SEED-02 | IM-01 | 2157168075190848 | IM-15 | NW-02 | CO-09 (was CO-01 [D] (o) | 0.1 | BET |
| NW-NEW-SEED-02 | IM-03 | 1658080129273784 | IM-16 | NW-02 | CO-09 (was CO-01 [D] (o) | 0.1 | BET |
| NW-NEW-SEED-02 | IM-02 | 2771287676600895 | IM-17 | NW-02 | CO-09 (was CO-01 [D] (o) | 0.0 | BET |
| NW-NEW-SEED-04 | IM-02 | 41256434 | IM-18 | NW-03 | CO-10 (was CO-02) | 540 | CONTROL-GRADE (dropped 1 rung: INCUMBENT) |
| NW-NEW-SEED-04 | IM-03 | 41256429 | IM-19 | NW-03 | CO-11 (was CO-03) | 519 | CONTROL-GRADE (dropped 1 rung: INCUMBENT) |
| 03-MERGE (search_ads ambiguity 1) | — | 78640432 | IM-20 | NW-03 | CO-12 (was —) | 206 | CONTROL-GRADE (dropped 1 rung: INCUMBENT) |
| NW-NEW-SEED-04 | IM-01 | 103675232 | IM-21 | NW-03 | CO-13 (was CO-01) | 119 | PROVEN (dropped 1 rung: INCUMBENT) |
| 03-MERGE (search_ads ambiguity 1) | — | 93128874 | IM-22 | NW-03 | CO-12 (was —) | 109 | PROVEN (dropped 1 rung: INCUMBENT) |
| NW-NEW-SEED-03 | IM-03 | 74657770 | IM-23 | NW-04 | CO-14 (was CO-02) | 87 | PROVEN |
| NW-NEW-SEED-03 | IM-04 | 59411595 | IM-24 | NW-04 | CO-14 (was CO-03) | 78 | PROVEN |
| NW-NEW-SEED-03 | IM-05 | 59618906 | IM-25 | NW-04 | CO-15 (was CO-04) | 77 | PROVEN |
| NW-NEW-SEED-03 | IM-02 | 150503331 | IM-26 | NW-04 | CO-14 (was CO-02) | 35 | LIKELY |
| NW-NEW-SEED-03 | IM-01 | 169243242 | IM-27 | NW-04 | CO-16 (was CO-01) | 24 | LIKELY |
| NW-SEED-03 | IM-01 | 1376173990650081 | IM-28 | NW-05 | CO-17 (was NULL) | 36 | LIKELY |
| NW-NEW-SEED-01 | (DCO variant of IM-01, not a separate IM | 70486040 | IM-29 | NW-06 | CO-18 (was CO-01) | 271 | CONTROL-GRADE (dropped 1 rung: INCUMBENT) |
| NW-NEW-SEED-01 | IM-01 | 70823628 | IM-30 | NW-06 | CO-18 (was CO-01) | 169 | PROVEN (dropped 1 rung: INCUMBENT) |
| NW-NEW-SEED-01 | IM-02 | 97210901 | IM-31 | NW-06 | CO-19 (was CO-02) | 47 | LIKELY (dropped 1 rung: INCUMBENT) |
| NW-NEW-SEED-01 | IM-03 | 97803506 | IM-32 | NW-06 | CO-20 (was CO-03) | 13 | BET |

Lint fix at merge: 02-NW-NEW-SEED-03 IM-04 (ad 59411595, Spanish verbatim translation) had its own CO-03 → folded into CO-14 (a translation is an execution variant, not a materially different concept).

## §2 · ADVERTISER NETWORK MAP

| nw_id | name | page_identities | shared_domains | network_type | merge_evidence | active_ads (value · tool · date) | pct_active | longest_days_active | first_seen | competitor_quality | scale | lanes_sold |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| NW-01 | Ecom Degree University | Ecom Degree University (brand 6294245, page 396204450233314) + Will Rivera personal page (brand 118898, page 100871195660447) — NW-APPEND | ecomdegree.com · join./live. · ecomdegreeu.com (checkout) | **EDUCATION/COACHING** (teach-you-to-resell on Walmart; NOT a DFY store build — same desire, different product) | same domain | 203 · GetHookd get_brand active_ads · 2026-09-23 (210 GetHookd exact total; 262 Meta estimated — never added) | NOT MAPPED (203 active / 210 exact total, same tool) | {126787289 · 68d active; 121358569 · 70d} (14 of 210 sampled) | UNKNOWN — not queried | ESTABLISHED | **ABOVE-FLOOR** (78,722 monthly_visits [R-TOOL list_shops]) | PB-02, PB-05, PB-07 |
| NW-02 | Ecom Family net | Ecomfamilyhub 621287414391369 · Ecomfamcrew 626035603916177 · Ecom Family Academy 570801579454344 (not GetHookd-indexed) | UNRESOLVED — candidate ecomfamily.com / ecomfamilyacademy.* [D] | BRAND (ASSUMED); candidate brand = education/coaching ladder [D] | identical creative (≥157 ad ids, 3 pages) | 160 · Meta per-page ACTIVE estimated_total_count 48+54+58 · 2026-09-24 | NOT MAPPED | ≤0.1d (all launched ≤2 days before read) | UNKNOWN | YOUNG-SCALER (ad-evidence) | UNSIZED | PB-02, PB-07 (title-level) |
| NW-03 | Ecom Accelerator | Ecom Accelerator (brand 134049, page 356933574178501); sibling candidate Cameron Hoffman page NOT MERGED | ecomaccelerator.io · go. · www./r/ | BRAND (managed store; capital-in profit share) | same domain family + identical copy | 85 · GetHookd brand.active_ads · 2026-09-24 (domain-scoped 29/46 — never added) | NOT MAPPED | {41256434 · 540d} | 2026-05-29 (go.) [R-TOOL] | INCUMBENT | UNSIZED | PB-07, PB-02 (+PB-05, PB-01 light) |
| NW-04 | Done for you brands | Done for you brands (brand 297031, page 952198114852442) | doneforyoubrands.co · shop./go./www. | BRAND (low-ticket DFY Shopify build) | same domain family + identical copy | 32 · GetHookd brand.active_ads · 2026-09-24 (Meta 35) | NOT MAPPED | {74657770 · 87d} | UNKNOWN | ESTABLISHED (caveat) | UNSIZED | PB-01, PB-05, PB-02, PB-03 |
| NW-05 | EcomXpertz | Ecomxpertz (page 125209367173618) | ecomxpertz.com | BRAND (DFY marketplace service, profit-share retainer) | same domain | 1 · Meta page_ids enumeration · 2026-09-24 | 100% (1/1) | {1376173990650081 · 36d} | 2026-08-18 [R-TOOL Meta] | UNCLASSIFIED (1 ad) | UNSIZED | PB-01, PB-05 |
| NW-06 | Ecom Websites | Ecom Websites (brand 1437830, page 113202963644035) | ecomwebsites.com · build./get./go. | BRAND (free/$20 DFY Shopify build) | same domain family + identical copy | 0 current · GetHookd + Meta · 2026-09-24 (historical 922 GetHookd / 627 Meta — not comparable) | 0% current (DORMANT since 2026-06-21) | {70486040 · 271d} | UNKNOWN | INCUMBENT (DORMANT) | UNSIZED | PB-01, PB-05, PB-03, PB-02 |
| NW-07 | Ecom Done For You | Ecom Done For You (FB page, not indexed) | ecomdoneforyou.com | BRAND (DFY marketplace automation) | same domain | COUNT-UNKNOWN (GetHookd 0 rows; Meta 0) | UNKNOWN | NONE FOUND — 0 ads | UNKNOWN | UNKNOWN | UNSIZED | PB-01, PB-05 (PDP) |
| NW-08 | Ecommerce Paradise | Ecommerce Paradise (FB page, not indexed) | ecommerceparadise.com · shop. | BRAND (high-ticket DFY build agency) | same domain + same product | COUNT-UNKNOWN (NOT INDEXED; Meta 0/3 matched) | UNKNOWN | UNKNOWN — no ad corpus | UNKNOWN | INSUFFICIENT DATA | UNSIZED | PB-01, PB-05, PB-06 (PDP) |

CRAWL COMPLETE lines (from each partial §2): NW-01 after 4 searches · NW-02 after 7 · NW-03 after 4 · NW-04 after 5 · NW-05 after 6 · NW-06 after 4 · NW-07 after 8 · NW-08 after 9. NW-APPEND at merge: 2 NW-03 ads (78640432, 93128874) surfaced by merge search #1 → IM-20, IM-22 (no new network).

## §3 · THE MONEY READ

**MARKET PROVES THE MONEY** — ≥1 NW with ≥50 active ads after a completed scan: NW-01 203 (GetHookd active_ads), NW-02 160 (Meta estimated, summed per page), NW-03 85 (GetHookd active_ads). Counts keep their count_basis; never added across tools.

Read by product type (honest split): the ≥50 networks are NW-01 (EDUCATION/COACHING — same desire, different product), NW-02 (title-level only; candidate brand is education/coaching [D]) and NW-03 (managed store for $15K+ capital holders). **Same-product (low-ticket DFY store build) tier: NW-04 32–35 active → PROVISIONAL (30–49)**; NW-06 is dormant (0 current, 922 historical); NW-05 1; NW-07/NW-08 0 / COUNT-UNKNOWN.

| lane | ABOVE-FLOOR networks selling it (ads) | UNSIZED networks selling it (ads) |
|---|---|---|
| PB-01 | 0 (—) | 4 (NW-03, NW-04, NW-05, NW-06) |
| PB-02 | 1 (NW-01) | 4 (NW-02, NW-03, NW-04, NW-06) |
| PB-03 | 0 (—) | 2 (NW-04, NW-06) |
| PB-04 | 0 (—) | 0 (—) |
| PB-05 | 1 (NW-01) | 3 (NW-03, NW-04, NW-06) |
| PB-06 | 0 (—) | 0 (—) |
| PB-07 | 1 (NW-01) | 2 (NW-02, NW-03) |

ABOVE-FLOOR = NW-01 only (the one network with a tool traffic figure). Every other network is UNSIZED — never counted toward crowding, never discarded.

## §4 · NETWORK SIZING CARDS (with competitor_components[] — COMPETITOR-CLAIMED, concatenated verbatim from each partial §4)

### NW-01 · Ecom Degree University (from NW-NEW-SEED-05)
- active_ads: 203 · GetHookd get_brand active_ads · 2026-09-23 (210 GetHookd exact total; 262 Meta estimated — never added) · scale: **ABOVE-FLOOR** (78,722 monthly_visits [R-TOOL list_shops]) · competitor_quality: ESTABLISHED · network_type: **EDUCATION/COACHING** (teach-you-to-resell on Walmart; NOT a DFY store build — same desire, different product)
- price ladder: Free webinar → $27 → $47–97 → $99/mo → $1,995–1,997 → $2,997–3,000 → $4,300 · trustpilot: 3.9/444 on ecomdegreeuniversity.com [D probable alternate]; BBB F-rated, 31–37 complaints · penetration: FREE webinar
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-NEW-SEED-05.md` §4):

| component | claim_verbatim (≤15w) | url |
|---|---|---|
| Walmart Seller Program (fulfillment) | "Walmart actually handles everything for you... hold all your inventory, ship it" | ad 121358672 transcript [R-TOOL] |
| Supplier sourcing | "suppliers that allow you to buy name brand products directly... at a wholesale price" | ad 121358672 transcript [R-TOOL] |
| Product-research AI tool | "an AI tool that I use to find products that are profitable to sell" | ad 121358672 transcript [R-TOOL] |
| Product-scanning app | "use ScanProfit mobile app to find discounted name brand products online" | ad 169343625 on-screen bullet list [R-TOOL] |
| Market-timing claim | "Walmart in 2026 looks like Amazon in 2015" | ad body, all DCO-family ads [R-TOOL] |
| Market-size claim | "200 million buyers but less than 200,000 sellers" on Walmart's platform | ad 121358672 transcript [R-TOOL] |
| Mechanism name | The **"Walmart Wealth Window™"** — a closing 12-18 month opportunity window | join.ecomdegree.com |
| Mechanism name | The **"Scan To Profits™"** System | join.ecomdegree.com |
| Mechanism name | The **"Second Chance Blueprint™"** | join.ecomdegree.com |
| Founder proof claim | "$30M+ in online sales using a 'backdoor' method most sellers don't know exists" | join.ecomdegree.com |
| Founder proof claim | "helping 12,600+ regular people build profitable Amazon businesses" | join.ecomdegree.com |
| Time-commitment claim | "working just 1 to 2 hours a day" | join.ecomdegree.com |
| Beginner-friendliness claim | "ordinary people with zero business experience" | join.ecomdegree.com |
| Coaching add-on | "30 Day access to my Amazon coaches via Voxer" — $197 | ecomdegreeu.com/join52883096 |

### NW-02 · Ecom Family net (from NW-NEW-SEED-02)
- active_ads: 160 · Meta per-page ACTIVE estimated_total_count 48+54+58 · 2026-09-24 · scale: UNSIZED · competitor_quality: YOUNG-SCALER (ad-evidence) · network_type: BRAND (ASSUMED); candidate brand = education/coaching ladder [D]
- price ladder (candidate brand [D]): FREE AI store builder → $1,495 course → $7,500 coaching · trustpilot BLOCKED-ON-TOOL; BBB complaints page read · penetration: FREE AI store builder [D]
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-NEW-SEED-02.md` §4):

- **products[] (of the CANDIDATE brand, `[D]` unconfirmed link, COMPETITOR-CLAIMED, [R-PAGE via Exa]):** e-commerce coaching/education (print-on-demand, dropshipping, affiliate marketing, "Content is Currency" personal-brand training, "AI Task Force" membership), a done-for-you AI Shopify store builder (`store.ecomfamilyacademy.io`), and two higher-ticket coaching tiers ("A-Z POD Main Course" / "Gift Giving Take Over", "Winner's Circle 12-Week Accelerator").

### NW-03 · Ecom Accelerator (from NW-NEW-SEED-04)
- active_ads: 85 · GetHookd brand.active_ads · 2026-09-24 (domain-scoped 29/46 — never added) · scale: UNSIZED · competitor_quality: INCUMBENT · network_type: BRAND (managed store; capital-in profit share)
- price: $15K–$30K / $25K–$35K liquid capital, 70/30 profit share, 16-month "No Profit No Payment" guarantee (not a cash refund) · claim-vs-delivery gap: ads say TikTok, live PDP says eBay & Walmart (partial §4) · trustpilot read (5 quotes, tally NOT MAPPED) · penetration: NONE
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-NEW-SEED-04.md` §4):

| component | claim_verbatim (≤15w) | url |
|---|---|---|
| store setup/management | "Our team sets up and manages your e-commerce store, handling everything from inventory to customer service" | ecomaccelerator.io |
| product research | "seasoned eCommerce individuals analyze e-commerce trends and consumer behavior to find in-demand products" | ecomaccelerator.io |
| sourcing | "sources inventory for your business through our network of vendors and suppliers at competitive prices" | ecomaccelerator.io |
| listings | "craft engaging product listings that are optimized for eBay and Walmart's algorithm and audience" | ecomaccelerator.io |
| marketing | "Targeted campaigns are launched on behalf of your store by our social media marketing team" | ecomaccelerator.io |
| fulfillment | "our team manages the fulfillment process, including payment processing, order management, and shipping" | ecomaccelerator.io |
| platform mix | "3 of the largest ecom giants around" (eBay, Walmart named; 3rd unstated on retrieved passage) | ecomaccelerator.io |
| profit split | "70/30 profit split—you keep 70%, we earn 30% when the store is profitable" | ecomaccelerator.io |
| guarantee | "16-month profit guarantee...we give up our profit split and work for free until you do" | ecomaccelerator.io |
| funnel guarantee | "If You Qualify You Will Be Covered By Our 'No Profit No Payment' Guarantee" | go.ecomaccelerator.io/fb/vsl |
| launch speed | "We Build & Manage Your Ecommerce Business - Live in as little as 31 Days" | go.ecomaccelerator.io/fb/vsl |
| track record | "We have launched 300+ stores...FTC-backed earnings claims disclosure has reported 32% ROI...Jan–Dec 2025" | ecomaccelerator.io |
| team size | "250+ person operations team" | ecomaccelerator.io |

### NW-04 · Done for you brands (from NW-NEW-SEED-03)
- active_ads: 32 · GetHookd brand.active_ads · 2026-09-24 (Meta 35) · scale: UNSIZED · competitor_quality: ESTABLISHED (caveat) · network_type: BRAND (low-ticket DFY Shopify build)
- price: $20 (20 products) / $97 (50) + Shopify $1/mo×3 then $39/mo + Zendrop $79/mo (disclosed) · 30-day 100% refund · quiz asks "why you want to start": Time / Location / Financial freedom [R-PAGE via Exa] · penetration: $20 store
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-NEW-SEED-03.md` §4):

| component | claim_verbatim (≤15w) | url |
|---|---|---|
| store build | "I'll Build You A Beautiful Ecommerce Website In Under 24 Hours" | shop.doneforyoubrands.co funnel material |
| products (base) | "PLUS 20 Hand Picked Products & High Quality Suppliers" | shop.doneforyoubrands.co funnel material |
| products (upsell) | "the $97 option, your custom store will come with 50 products" | shop.doneforyoubrands.co funnel material |
| suppliers | "high-quality US suppliers... that'll actually ship out your products FOR YOU" | ad body [D] |
| platform | "They build your store on a platform called Shopify" | ad body [D] |
| funding model | "Shopify pays them a commission for the stores they set up" | ad body [D] |
| platform cost (disclosed) | "$1/month for the first 3 months! After that, it's $39/month" | shop.doneforyoubrands.co funnel material |
| supplier cost (disclosed) | "$79.00 USD per month" (Zendrop) | shop.doneforyoubrands.co funnel material |
| shipping upsell | "Fast Shipping Suppliers" — "$49" (older checkout variant) | shop.doneforyoubrands.co funnel material |
| guarantee | "I'll refund you 100% of your purchase" within 30 days, "no questions asked" | ad body [D] + funnel material |
| guarantee (CO-04 variant, stronger) | "worst case? You pay nothing... refunded and keep the setup anyway" | ad body [D] |
| discovery gate | 5-question quiz before price is shown (location, time budget, store "feel," motivation, product type) | shop.doneforyoubrands.co/dfy-quiz-a134 |

### NW-05 · EcomXpertz (from NW-SEED-03)
- active_ads: 1 · Meta page_ids enumeration · 2026-09-24 · scale: UNSIZED · competitor_quality: UNCLASSIFIED (1 ad) · network_type: BRAND (DFY marketplace service, profit-share retainer)
- price: $3K–$8K / yr profit-split tiers · refund only if project not started (20 days) · penetration: NONE
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-SEED-03.md` §4):

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

### NW-06 · Ecom Websites (from NW-NEW-SEED-01)
- active_ads: 0 current · GetHookd + Meta · 2026-09-24 (historical 922 GetHookd / 627 Meta — not comparable) · scale: UNSIZED · competitor_quality: INCUMBENT (DORMANT) · network_type: BRAND (free/$20 DFY Shopify build)
- price: $0 / $20 advertised; funnel-actual $1/mo×3 + "processing fee of up to $500", "all sales final" · Trustpilot 4.7/5, 2,042 reviews [R-PAGE via Exa] · penetration: free/$20 store
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-NEW-SEED-01.md` §4):

| component | claim_verbatim (≤15w) | url |
|---|---|---|
| store build | "We'll Build Your eCommerce Website in 10 Minutes — For Free" | build.ecomwebsites.com |
| products | "30 high-potential products in your niche — completely free" | build.ecomwebsites.com |
| suppliers | "Integrated suppliers ship products directly to your customers" | build.ecomwebsites.com |
| platform | "We build every store on Shopify — the world's leading ecommerce platform" | build.ecomwebsites.com |
| customization | "You can change the colors, fonts, layout, products, pricing" | build.ecomwebsites.com |
| training | "training on how to drive traffic... social media, paid advertising, organic" | build.ecomwebsites.com |
| support | "Our team provides ongoing support... questions, store changes, issues" | build.ecomwebsites.com |
| partnership claim | "We're official Shopify Partners" | build.ecomwebsites.com |
| pricing claim | "No Hidden Fees" / "Same Shopify Price" | build.ecomwebsites.com |
| guarantee | NONE STATED on the ad-facing page — funnel terms instead say "no refunds... all sales final" | go.ecomwebsites.com/go |
| actual charge | "$1 /mo for 3 months" then "a one-time processing fee of up to $500 USD may apply" | go.ecomwebsites.com/go |

### NW-07 · Ecom Done For You (from NW-SEED-01)
- active_ads: COUNT-UNKNOWN (GetHookd 0 rows; Meta 0) · scale: UNSIZED · competitor_quality: UNKNOWN · network_type: BRAND (DFY marketplace automation)
- price: $2,000 (Walmart automation; others UNKNOWN) · "100% ROI guarantee within 6 months" (conditional, credit substitution) · penetration: NONE STATED
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-SEED-01.md` §4):

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

### NW-08 · Ecommerce Paradise (from NW-SEED-02)
- active_ads: COUNT-UNKNOWN (NOT INDEXED; Meta 0/3 matched) · scale: UNSIZED · competitor_quality: INSUFFICIENT DATA · network_type: BRAND (high-ticket DFY build agency)
- price: $9,997 / $14,997 / $19,997 (promo $9,998.50) + $2,997/mo + add-ons · milestone-rebuild guarantee, no cash refunds · penetration: top-tier 50% off "Only 5 Spots"
- competitor_components[] (full card and remaining fields: `02-partials/02-COMPETITOR-INTEL.NW-SEED-02.md` §4):

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

## §5 · CORPUS COVERAGE STATEMENT (merged; the query-level tables stay in each partial §5)

| nw_id | queries (partial) | total + count_basis | rows read | ads opened (body) | NOT OPENED (cap) | NOT MAPPED |
|---|---|---|---|---|---|---|
| NW-01 | 4 crawl + 11 sizing/opening (02-NW-NEW-SEED-05 §5) | 210 exact (explore_search_total) / 203 active (brand) / 262 Meta est. | 14 IM | 14 (9 full body; 5 transcript pending — merge get_ad re-check: 134426835 still pending, 169343626 not_requested) | 196 | cls_* fields; 196 unopened ads; first_seen |
| NW-02 | 7 crawl (02-NW-NEW-SEED-02 §5) | 159–160 Meta estimated | 159 rows (3 pages) | 0 bodies (Meta titles only; NOT OPENED (tool)) | ≥154 duplicates | landing domain; body; format |
| NW-03 | 4 crawl + sizing (02-NW-NEW-SEED-04 §5) + merge search #1 | 85 active (brand); 563 Meta est. ("ecom accelerator", loose) | 6 + 5 (merge search) | 5 (3 partial bodies + 2 transcripts surfaced at merge) | ~80 active unopened | Cameron Hoffman sibling; loser/winner pairs |
| NW-04 | 5 crawl + 38-row sample (02-NW-NEW-SEED-03 §5) | 32 active (brand) / 35 Meta | 38 | 5 | 33 | historical total (truncated) |
| NW-05 | 6 crawl + 3 (02-NW-SEED-03 §5) | 1 (Meta ALL) | 1 | 0 (no GetHookd id) | 0 | body, format, landing |
| NW-06 | 4 crawl + opening (02-NW-NEW-SEED-01 §5) | 922 inactive exact (GetHookd) / 627 Meta ALL | ~27 | 4 (3 IM + 1 DCO variant row) | ~24 DCO siblings | shop roster |
| NW-07 | 8 crawl (02-NW-SEED-01 §5) | 0 / 0 | 0 | 0 | 0 | ad corpus (none found) |
| NW-08 | 9 crawl + 3 Meta (02-NW-SEED-02 §5) | 0 / 0 matched | 0 | 0 | 0 | ad corpus (none found) |
| KEYWORDS | 28 GetHookd + 14 Meta (02-KEYWORDS §11) | per-term totals §11 | top rows per term | — | — | 2 of 9 GetHookd cells (~, batch re-verification) |
| MERGE | search_ads ×2 charged (0.05 each) + get_ad ×3 free | #1 "Want My Team To Build You An eCom Business" total 631 (brand-capped, exact); #2 "I Didn't Have a Cape…" total 9 (brand-capped, exact) | 5 + 5 | 3 re-opened (free); 2 new bodies from #1 | — | #1: Cameron Hoffman not surfaced → sibling UNRESOLVED; #2: 0 Ecom Family rows → domain UNRESOLVED |

Buckets (32 IM): {'BORDERLINE': 9, 'NON-STORY': 22, 'COPY-STRICT/CREATIVE-HYBRID': 1} — STRICT-STORY 0 of 32.

## §6 · RANKED WINNERS — STRICT

`NONE FOUND — searched: 32 IM across 6 ad-bearing networks coded by manual inspection in the partials; 0 met STRICT-STORY; nearest: IM-03 (COPY-STRICT/CREATIVE-HYBRID, founder math VSL, 63d)`. ranked_winners_strict[] = [] → PARTIAL (N=0/10) — chain exhausted: [no long-form first-person story ads in this market sample; 5 NW-01 transcripts pending; NW-02 bodies not openable].

## §7 · RANKED WINNERS — ALL-FORMAT (ads ≤7 days excluded: IM-15..IM-17 recorded, never ranked — rule 6.5)

Ranked in code by: networks carrying the same Big Idea → days_active → active status → performance title → used_count.

| Rank | NW | Page | Ad ID | Link | Days Active | Status | Performance | used_count | longevity_label | Big Idea | Concept | Avatar | Lanes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NW-03 | Ecom Accelerator | 41256434 | https://app.gethookd.ai/share/ad/41256434?signature=e8a15c2928e9af905e43d3910890fbb812ff2bb9633 | 540 | inactive | NULL | 2 | CONTROL-GRADE (dropped 1 rung: INCUMBENT) | BI-03 (2 NW) | CO-10 | wants a high-return investment opportunity without tradition | PB-02, PB-07 |
| 2 | NW-03 | Ecom Accelerator | 41256429 | https://app.gethookd.ai/share/ad/41256429?signature=cd7fb61172b397f9cf1ed31f15b016ffcde566992b6 | 519 | inactive | NULL | 2 | CONTROL-GRADE (dropped 1 rung: INCUMBENT) | BI-03 (2 NW) | CO-11 | business owner with ~$25K liquid capital wanting portfolio d | PB-02, PB-07 |
| 3 | NW-06 | Ecom Websites | 70486040 | https://app.gethookd.ai/share/ad/70486040?signature=b7db77c179553f0c8f51bda348fd316240e45a9fab2 | 271 | inactive | NULL | 1 | CONTROL-GRADE (dropped 1 rung: INCUMBENT) | BI-01 (2 NW) | CO-18 | aspiring online-business starter overwhelmed by DIY setup an | PB-01, PB-05 |
| 4 | NW-06 | Ecom Websites | 70823628 | https://app.gethookd.ai/share/ad/70823628?signature=6120835b930418bb3cc11e315adcc84b0d35b3c9213 | 169 | inactive | NULL | 2 (cross-b | PROVEN (dropped 1 rung: INCUMBENT) | BI-01 (2 NW) | CO-18 | aspiring online-business starter overwhelmed by DIY setup an | PB-01, PB-05 |
| 5 | NW-04 | Done for you brands | 74657770 | https://app.gethookd.ai/share/ad/74657770?signature=6f779e03e342dd398fa616c388c6e144bd4ece9be24 | 87 | inactive | NULL | 2 | PROVEN | BI-01 (2 NW) | CO-14 | course-burned aspiring seller, no store yet | PB-01, PB-03, PB-05 |
| 6 | NW-04 | Done for you brands | 59411595 | https://app.gethookd.ai/share/ad/59411595?signature=272b1fe119a29c973dcac9ba3e90311e2154265b2ac | 78 | inactive | NULL | 1 | PROVEN | BI-01 (2 NW) | CO-14 | Spanish-speaking aspiring online seller | PB-01, PB-05 |
| 7 | NW-01 | Ecom Degree University | 121358569 | https://app.gethookd.ai/share/ad/121358569 | 70 | inactive | NULL | 1 | PROVEN | BI-03 (2 NW) | CO-01 | young adult / side-hustle seeker [D from shared body] | PB-02 |
| 8 | NW-01 | Ecom Degree University | 126787289 | https://app.gethookd.ai/share/ad/126787289 | 68 | active | Winning | 1 | PROVEN | BI-03 (2 NW) | CO-01 | young adult / side-hustle seeker [D] | PB-02 |
| 9 | NW-01 | Ecom Degree University | 134426761 | https://app.gethookd.ai/share/ad/134426761 | 60 | active | Winning | 2 | PROVEN | BI-03 (2 NW) | CO-01 | young adult / side-hustle seeker [D] | PB-02 |
| 10 | NW-01 | Ecom Degree University | 134427111 | https://app.gethookd.ai/share/ad/134427111 | 60 | active | Growing | 1 | PROVEN | BI-03 (2 NW) | CO-01 | young adult, competitive/status-driven | PB-02, PB-07 |
| 11 | NW-01 | Ecom Degree University | 134426835 | https://app.gethookd.ai/share/ad/134426835 | 57 | active | Optimized | 1 | PROVEN | BI-03 (2 NW) | CO-04 | broad/undifferentiated - no visible demographic signal | PB-02 |
| 12 | NW-01 | Ecom Degree University | 144205353 | https://app.gethookd.ai/share/ad/144205353 | 48 | active | Optimized | 1 | PROVEN | BI-03 (2 NW) | CO-05 | wealth/status-motivated aspirational viewer | PB-02, PB-07 |
| 13 | NW-06 | Ecom Websites | 97210901 | https://app.gethookd.ai/share/ad/97210901?signature=934e795d8ebd0568d7c95568076fbe44fb1df5eb280 | 47 | inactive | NULL | 1 per row  | LIKELY (dropped 1 rung: INCUMBENT) | BI-01 (2 NW) | CO-19 | skeptical prospect worried the free offer is a scam | PB-01, PB-03 |
| 14 | NW-05 | Ecomxpertz | 1376173990650081 | https://www.facebook.com/ads/library/?id=1376173990650081 | 36 | active | NULL — searched | NULL — sea | LIKELY | BI-01 (2 NW) | CO-17 | wants to launch an Amazon store but lacks confidence (INFERR | PB-01 |
| 15 | NW-04 | Done for you brands | 150503331 | https://app.gethookd.ai/share/ad/150503331?signature=3711eb03b9d012e6660423adc347087b15c9e200ac | 35 | active | NULL | 1 | LIKELY | BI-01 (2 NW) | CO-14 | course-burned aspiring seller, no store yet | PB-01, PB-03, PB-05 |
| 16 | NW-01 | Ecom Degree University | 169343649 | https://app.gethookd.ai/share/ad/169343649 | 24 | active | Scaling | 1 | LIKELY | BI-03 (2 NW) | CO-05 | aspirational | PB-02 |
| 17 | NW-01 | Ecom Degree University | 169343631 | https://app.gethookd.ai/share/ad/169343631 | 24 | active | Scaling | 1 | LIKELY | BI-03 (2 NW) | CO-07 | status/wealth-signaling-motivated | PB-02, PB-07 |
| 18 | NW-01 | Ecom Degree University | 169343626 | https://app.gethookd.ai/share/ad/169343626 | 24 | active | Scaling | 1 | LIKELY | BI-03 (2 NW) | CO-05 | older adult / retiree | PB-02, PB-07 |
| 19 | NW-04 | Done for you brands | 169243242 | https://app.gethookd.ai/share/ad/169243242?signature=6797bde10225a3ff86c983861303b40ab8f2ec2c78 | 24 | active | NULL | 2 | LIKELY | BI-01 (2 NW) | CO-16 | chronic procrastinator on starting a business | PB-01, PB-02, PB-05 |
| 20 | NW-06 | Ecom Websites | 97803506 | https://app.gethookd.ai/share/ad/97803506?signature=6c0bfd58c7fb7b6582c05530b87149f917bc9a1d612 | 13 | inactive | NULL | 1 (2-way b | BET | BI-01 (2 NW) | CO-20 | repeat procrastinator who has put off starting an online sto | PB-01, PB-02 |

## §8 · INDIVIDUAL AD RECORDS (IM-## cards, grouped by NW; excerpts ≤15w; every field in 02-swipe.csv)

**NW-01** — 14 IM

- **IM-01** · ad 121358569 · inactive · 70d · PROVEN · perf NULL · used 1 · reuse Y · format video, 71s · bucket **BORDERLINE** · CO-01 · hook: "REPORT: A growing wave of young adults is cashing in on a hidden Walmart income" · awareness Unaware · funnel MSL->squeeze_page->(offline sales)->paid · avatar: young adult / side-hustle seeker [D from shared body] (TITLE-BODY) · cp CP-01 · pb PB-02 · COMPETITOR-CLAIMED
- **IM-02** · ad 126787289 · active · 68d · PROVEN · perf Winning · used 1 · reuse Y · format video, 12s · bucket **NON-STORY** · CO-01 · hook: "REPORT: A growing wave of young adults is cashing in on a hidden Walmart income" · awareness Unaware · funnel MSL->squeeze_page->(offline sales)->paid · avatar: young adult / side-hustle seeker [D] (TITLE-BODY) · cp CP-01 · pb PB-02 · COMPETITOR-CLAIMED
- **IM-03** · ad 121358672 · inactive · 63d · PROVEN · perf NULL · used 1 · reuse Y · format video, 192s · bucket **COPY-STRICT/CREATIVE-HYBRID** · CO-02 · hook: "If you make less than $50 an hour, you should keep watching this ad" · awareness Problem · funnel MSL->squeeze_page(free webinar)->(offlin · avatar: hourly-wage worker in a low-ceiling job (TRANSCRIPT) · cp CP-01,CP-03 · pb PB-02,PB-05 · COMPETITOR-CLAIMED
- **IM-04** · ad 134426761 · active · 60d · PROVEN · perf Winning · used 2 · reuse Y · format video, 17s · bucket **NON-STORY** · CO-01 · hook: "REPORT: A growing wave of young adults is cashing in on a hidden Walmart income" · awareness Unaware · funnel MSL->squeeze_page->(offline sales)->paid · avatar: young adult / side-hustle seeker [D] (TITLE-BODY) · cp CP-01 · pb PB-02 · COMPETITOR-CLAIMED
- **IM-05** · ad 134427111 · active · 60d · PROVEN · perf Growing · used 1 · reuse Y · format video, 10s · bucket **NON-STORY** · CO-01 · hook: "POV: How life looks when you sell products on Walmart while everyone else is still" · awareness Unaware · funnel MSL->squeeze_page->(offline sales)->paid · avatar: young adult, competitive/status-driven (TITLE-BODY) · cp CP-01 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-06** · ad 134426818 · active · 60d · PROVEN · perf Growing · used 1 · reuse Y · format video, 46s · bucket **NON-STORY** · CO-03 · hook: "EXPOSED - Ecom expert exposes the top 10 products to sell on Walmart (And why" · awareness Solution · funnel MSL->squeeze_page->(offline sales)->paid · avatar: aspiring reseller wanting concrete proof (TITLE-BODY;PAGE-NAME) · cp CP-01,CP-05 · pb PB-02,PB-05 · COMPETITOR-CLAIMED
- **IM-07** · ad 134426835 · active · 57d · PROVEN · perf Optimized · used 1 · reuse N · format video, 102s · bucket **BORDERLINE** · CO-04 · hook: "did you just... just fell!" · awareness Unaware · funnel MSL->squeeze_page->(offline sales)->paid · avatar: broad/undifferentiated - no visible demographic signal (TITLE-BODY) · cp NULL · pb PB-02 · COMPETITOR-CLAIMED
- **IM-08** · ad 144205353 · active · 48d · PROVEN · perf Optimized · used 1 · reuse Y · format video, 125s · bucket **BORDERLINE** · CO-05 · hook: "The Next Online Gold Rush" · awareness Problem · funnel MSL->squeeze_page->(offline sales)->paid · avatar: wealth/status-motivated aspirational viewer (TITLE-BODY) · cp CP-01,CP-02 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-09** · ad 159706760 · active · 31d · LIKELY · perf Optimized · used 3 · reuse Y · format video, 55s · bucket **NON-STORY** · CO-03 · hook: "10 Everyday Walmart Products I Used to Quit My 9-5 For Good" · awareness Solution · funnel MSL->squeeze_page->(offline sales)->paid · avatar: aspiring reseller wanting concrete proof (TITLE-BODY) · cp CP-01,CP-05 · pb PB-02,PB-05 · COMPETITOR-CLAIMED
- **IM-10** · ad 169343657 · active · 24d · LIKELY · perf Scaling · used 1 · reuse N · format video, 19s · bucket **NON-STORY** · CO-06 · hook: "The biggest lie in business? 'You need your own product.'" · awareness Unaware · funnel MSL->squeeze_page->(offline sales)->paid · avatar: product-ideation-anxious, deterred by the 'need your own product' beli (TITLE-BODY) · cp CP-05 · pb PB-05 · COMPETITOR-CLAIMED
- **IM-11** · ad 169343649 · active · 24d · LIKELY · perf Scaling · used 1 · reuse Y · format video, 58s · bucket **BORDERLINE** · CO-05 · hook: "No better business to start in 2026" · awareness Problem · funnel MSL->squeeze_page->(offline sales)->paid · avatar: aspirational (TITLE-BODY) · cp CP-01 · pb PB-02 · COMPETITOR-CLAIMED
- **IM-12** · ad 169343631 · active · 24d · LIKELY · perf Scaling · used 1 · reuse N · format video, 29s · bucket **NON-STORY** · CO-07 · hook: "The biggest opportunity of 2026 - Comment 'Walmart' for an invite to my next workshop" · awareness Unaware · funnel comment-gated DM funnel [D] - differs fr · avatar: status/wealth-signaling-motivated (TITLE-BODY) · cp CP-01 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-13** · ad 169343626 · active · 24d · LIKELY · perf Scaling · used 1 · reuse Y · format video, 56s · bucket **BORDERLINE** · CO-05 · hook: "Grandmas can still get rich / How a 65-Year-Old Grandma Makes $7K a Month" · awareness Problem · funnel MSL->squeeze_page->(offline sales)->paid · avatar: older adult / retiree (TITLE-BODY (explicit age ) · cp CP-06 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-14** · ad 169343625 · active · 24d · LIKELY · perf Scaling · used 1 · reuse N · format video, 6s · bucket **NON-STORY** · CO-08 · hook: "Don't get another job in 2026" · awareness Solution · funnel MSL->squeeze_page->(offline sales)->paid · avatar: job-averse young adult wanting a concrete recipe (TITLE-BODY (clearest mech) · cp CP-01 · pb PB-02,PB-05 · COMPETITOR-CLAIMED

**NW-02** — 3 IM

- **IM-15** · ad 2157168075190848 · active · 0.1d · BET · perf NULL — searched · used NULL — · reuse Y [ · format UNKNOWN — searched · bucket **BORDERLINE** · CO-09 · hook: "I Didn’t Have a Cape. Just a Laptop and a Family to Fight For!" · awareness Problem · funnel UNKNOWN — searched · avatar: father/parent providing for family via a laptop-run business, no prior (TITLE-BODY + PAGE-NAME) · cp CP-01,CP-02 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-16** · ad 1658080129273784 · active · 0.1d · BET · perf NULL — searched · used NULL — · reuse Y [ · format UNKNOWN — searched · bucket **BORDERLINE** · CO-09 · hook: "I Didn’t Have a Cape. Just a Laptop and a Family to Fight For!" · awareness Problem · funnel UNKNOWN — searched · avatar: father/parent providing for family via a laptop-run business, no prior (TITLE-BODY + PAGE-NAME) · cp CP-01,CP-02 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-17** · ad 2771287676600895 · active · 0.0d · BET · perf NULL — searched · used NULL — · reuse Y [ · format UNKNOWN — searched · bucket **BORDERLINE** · CO-09 · hook: "I Didn’t Have a Cape. Just a Laptop and a Family to Fight For!" · awareness Problem · funnel UNKNOWN — searched · avatar: father/parent providing for family via a laptop-run business, no prior (TITLE-BODY + PAGE-NAME) · cp CP-01,CP-02 · pb PB-02,PB-07 · COMPETITOR-CLAIMED

**NW-03** — 5 IM

- **IM-18** · ad 41256434 · inactive · 540d · CONTROL-GRADE (dropped 1 rung: INCUMBENT) · perf NULL · used 2 · reuse Y ( · format dco · bucket **NON-STORY** · CO-10 · hook: "THIS New Ecommerce Platform Will Be Even Bigger Than Amazon" · awareness Problem · funnel MSL->VSL · avatar: wants a high-return investment opportunity without traditional ecommer (TITLE-BODY) · cp CP-06 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-19** · ad 41256429 · inactive · 519d · CONTROL-GRADE (dropped 1 rung: INCUMBENT) · perf NULL · used 2 · reuse Y ( · format dco · bucket **NON-STORY** · CO-11 · hook: "Top Economists Are Referring To THIS As Amazon's New Rival" · awareness Solution · funnel MSL->application-gated VSL · avatar: business owner with ~$25K liquid capital wanting portfolio diversifica (TITLE-BODY) · cp CP-06 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-20** · ad 78640432 · inactive · 206d · CONTROL-GRADE (dropped 1 rung: INCUMBENT) · perf NULL (no score on ro · used 2 · reuse Y · format video · bucket **NON-STORY** · CO-12 · hook: "If you are sitting on $25,000 or more and are looking for a smarter way" · awareness Solution · funnel MSL -> VSL (application-gated) · avatar: capital holder ($25K+) wanting money to work; kids college fund / earl (TRANSCRIPT) · cp CP-02,CP-06 · pb PB-02,PB-07 · COMPETITOR-CLAIMED
- **IM-21** · ad 103675232 · active · 119d · PROVEN (dropped 1 rung: INCUMBENT) · perf Testing · used 1 (per · reuse Y ( · format video · bucket **NON-STORY** · CO-13 · hook: "If You Have Between $15K and $30k Liquid And Are Looking For" · awareness Solution · funnel MSL->VSL · avatar: has $15K-$30K liquid capital, wants a new income stream without runnin (TITLE-BODY) · cp CP-06 · pb PB-01,PB-02,PB-05,PB-07 · COMPETITOR-CLAIMED
- **IM-22** · ad 93128874 · inactive · 109d · PROVEN (dropped 1 rung: INCUMBENT) · perf NULL (no score on ro · used 2 · reuse Y · format video · bucket **NON-STORY** · CO-12 · hook: "If You Have Between $25K and $35k Liquid and Are Looking For" · awareness Solution · funnel MSL -> VSL (application-gated) · avatar: capital holder comparing e-commerce to stocks/bonds (TITLE-BODY + TRANSCRIPT) · cp CP-06 · pb PB-02,PB-07 · COMPETITOR-CLAIMED

**NW-04** — 5 IM

- **IM-23** · ad 74657770 · inactive · 87d · PROVEN · perf NULL · used 2 · reuse Y · format video · bucket **NON-STORY** · CO-14 · hook: "STOP buying courses! I'll design you a beautiful store" · awareness UNKNOWN · funnel NULL · avatar: course-burned aspiring seller, no store yet (TITLE-BODY) · cp CP-03,CP-05 · pb PB-01,PB-03,PB-05 · COMPETITOR-CLAIMED
- **IM-24** · ad 59411595 · inactive · 78d · PROVEN · perf NULL · used 1 · reuse Y · format video · bucket **NON-STORY** · CO-14 · hook: "NO compres mas cursos. Yo te hago una tienda online hermosa" · awareness UNKNOWN · funnel NULL · avatar: Spanish-speaking aspiring online seller (LANDING-SLUG+TITLE-BODY) · cp CP-03,CP-05 · pb PB-01,PB-05 · COMPETITOR-CLAIMED
- **IM-25** · ad 59618906 · inactive · 77d · PROVEN · perf NULL · used 1 · reuse N · format image · bucket **NON-STORY** · CO-15 · hook: "People are stealing your money. And it's legal." · awareness UNKNOWN · funnel NULL · avatar: frustrated buyer wanting a second income stream (TITLE-BODY) · cp CP-01,CP-02 · pb PB-01,PB-02 · COMPETITOR-CLAIMED
- **IM-26** · ad 150503331 · active · 35d · LIKELY · perf NULL · used 1 · reuse Y · format video · bucket **NON-STORY** · CO-14 · hook: "STOP buying courses! I'll design you a beautiful store" · awareness UNKNOWN · funnel NULL · avatar: course-burned aspiring seller, no store yet (TITLE-BODY) · cp CP-03,CP-05 · pb PB-01,PB-03,PB-05 · COMPETITOR-CLAIMED
- **IM-27** · ad 169243242 · active · 24d · LIKELY · perf NULL · used 2 · reuse Y · format video · bucket **NON-STORY** · CO-16 · hook: "77,254+ people have already claimed their online store" · awareness UNKNOWN · funnel NULL · avatar: chronic procrastinator on starting a business (TITLE-BODY) · cp CP-01,CP-05 · pb PB-01,PB-02,PB-05 · COMPETITOR-CLAIMED

**NW-05** — 1 IM

- **IM-28** · ad 1376173990650081 · active · 36d · LIKELY · perf NULL — searched · used NULL — · reuse UNK · format UNKNOWN — searched · bucket **BORDERLINE** · CO-17 · hook: "Launch Your Amazon Store with Confidence" · awareness Problem · funnel UNKNOWN — searched · avatar: wants to launch an Amazon store but lacks confidence (INFERRED from ad (TITLE-BODY (partial — tit) · cp CP-05 · pb PB-01 · COMPETITOR-CLAIMED

**NW-06** — 4 IM

- **IM-29** · ad 70486040 · inactive · 271d · CONTROL-GRADE (dropped 1 rung: INCUMBENT) · perf NULL · used 1 · reuse Y · format dco/image · bucket **NON-STORY** · CO-18 · hook: "Let me guess... You've been thinking about starting an online business" · awareness Problem · funnel MSL->quiz->Shopify-trial-upsell · avatar: aspiring online-business starter overwhelmed by DIY setup and product  (TITLE-BODY) · cp CP-05 · pb PB-01,PB-05 · COMPETITOR-CLAIMED
- **IM-30** · ad 70823628 · inactive · 169d · PROVEN (dropped 1 rung: INCUMBENT) · perf NULL · used 2 (cro · reuse Y · format dco (carousel of vid · bucket **NON-STORY** · CO-18 · hook: "Let me guess... You've been thinking about starting an online business" · awareness Problem · funnel MSL->quiz->Shopify-trial-upsell · avatar: aspiring online-business starter overwhelmed by DIY setup and product  (TITLE-BODY) · cp CP-05 · pb PB-01,PB-05 · COMPETITOR-CLAIMED
- **IM-31** · ad 97210901 · inactive · 47d · LIKELY (dropped 1 rung: INCUMBENT) · perf NULL · used 1 per  · reuse Y · format image · bucket **NON-STORY** · CO-19 · hook: "We were named the #1 Commerce Coach in North America" · awareness Product · funnel MSL->quiz->Shopify-trial-upsell · avatar: skeptical prospect worried the free offer is a scam (TITLE-BODY) · cp CP-03,CP-05 · pb PB-01,PB-03 · COMPETITOR-CLAIMED
- **IM-32** · ad 97803506 · inactive · 13d · BET · perf NULL · used 1 (2-w · reuse Y · format video · bucket **NON-STORY** · CO-20 · hook: "You've thought about starting an online store before" · awareness Problem · funnel MSL->quiz->Shopify-trial-upsell · avatar: repeat procrastinator who has put off starting an online store (TITLE-BODY) · cp CP-01,CP-05 · pb PB-01,PB-02 · COMPETITOR-CLAIMED

**NW-07** — 0 IM


**NW-08** — 0 IM


NW-07, NW-08: `NONE FOUND — searched` (0 ads; PDP-only evidence in their partials).

## §9 · AVATAR COVERAGE MAP (persona × NW; cell {ad_count, longest_days_active, awareness_entries, lanes}; label = 02 rule 8 on ABOVE-FLOOR networks; shadow = same rule counting UNSIZED networks — printed, never a label)

| persona | NW-01 | NW-02 | NW-03 | NW-04 | NW-05 | NW-06 | NW-07 | NW-08 | independent_networks (AF) | networks (all) | total_serious_ads | label | shadow_if_unsized_counted |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CP-01 full-time job, wants out | {11, 70d, Problem/Solution/Unaware, PB-02/PB-05/PB-07} | {3, 0.1d, Problem, PB-02/PB-07} | — | {2, 77d, UNKNOWN, PB-01/PB-02/PB-05} | — | {1, 13d, Problem, PB-01/PB-02} | — | — | 1 | 4 | 17 | EARLY SIGNAL (PROVEN ads present; <2 AF networks) | VALIDATED-CONTESTED |
| CP-02 parent with kids (op. hyp. a) | {1, 48d, Problem, PB-02/PB-07} | {3, 0.1d, Problem, PB-02/PB-07} | {1, 206d, Solution, PB-02/PB-07} | {1, 77d, UNKNOWN, PB-01/PB-02} | — | — | — | — | 1 | 4 | 6 | EARLY SIGNAL (PROVEN ads present; <2 AF networks) | SUPPORTED |
| CP-03 tried & lost money | {1, 63d, Problem, PB-02/PB-05} | — | — | {3, 87d, UNKNOWN, PB-01/PB-03/PB-05} | — | {1, 47d, Product, PB-01/PB-03} | — | — | 1 | 3 | 5 | EARLY SIGNAL (PROVEN ads present; <2 AF networks) | SUPPORTED |
| CP-04 busy e-com owner | — | — | — | — | — | — | — | — | 0 | 0 | 0 | 0 ads — NOT MAPPED (0 avatar-phrase searches <3) | 0 ads — NOT MAPPED (0 avatar-phrase searches <3) |
| CP-05 aspiring, skip the build | {3, 60d, Solution/Unaware, PB-02/PB-05} | — | — | {4, 87d, UNKNOWN, PB-01/PB-02/PB-03/PB-05} | {1, 36d, Problem, PB-01} | {4, 271d, Problem/Product, PB-01/PB-02/PB-03/PB-05} | — | — | 1 | 4 | 12 | EARLY SIGNAL (PROVEN ads present; <2 AF networks) | VALIDATED-CONTESTED |
| CP-06 near-retirement savings (op. hyp. b) | {1, 24d, Problem, PB-02/PB-07} | — | {5, 540d, Problem/Solution, PB-01/PB-02/PB-05/PB-07} | — | — | — | — | — | 1 | 2 | 6 | EARLY SIGNAL (PROVEN ads present; <2 AF networks) | SUPPORTED |
| CP-07 spouse can't work (kids) | — | — | — | — | — | — | — | — | 0 | 0 | 0 | 0 ads — NOT MAPPED (1 avatar-phrase searches <3) | 0 ads — NOT MAPPED (1 avatar-phrase searches <3) |
| AV-cand-01 capital holder ($15–35K liquid) seeking returns | — | — | {5, 540d, Problem/Solution, PB-01/PB-02/PB-05/PB-07} | — | — | — | — | — | 0 | 1 | 5 | EARLY SIGNAL (PROVEN ads present; <2 AF networks) · UNSIZED-only | EARLY SIGNAL (PROVEN ads present; <2 AF networks) · UNSIZED-only |
| AV-cand-02 young adult / job-averse side-hustle seeker | {5, 70d, Solution/Unaware, PB-02/PB-05/PB-07} | — | — | — | — | — | — | — | 1 | 1 | 5 | EARLY SIGNAL (PROVEN ads present; <2 AF networks) | EARLY SIGNAL (PROVEN ads present; <2 AF networks) |
| AV-cand-03 Spanish-speaking aspiring seller | — | — | — | {1, 78d, UNKNOWN, PB-01/PB-05} | — | — | — | — | 0 | 1 | 1 | HYPOTHESIS | HYPOTHESIS |

VACANT / unsearched rows carry their searches: CP-02 phrases "online business for dads", "side income for fathers", "passive income for parents"; CP-06 "retirement online business", "online store for retirees"; CP-07 "passive income for parents" (02-KEYWORDS §11 — every phrase SATURATED by raw count, 0 father/retiree-relevant DFY bodies in rows read). CP-04: 0 avatar-phrase searches → NOT MAPPED. NW-07/NW-08 columns are 0-ad (PDP-level persona claims live in their partial §9).

## §10 · PROBLEM-LANE COVERAGE MAP (PB × NW; same cell)

| lane | NW-01 | NW-02 | NW-03 | NW-04 | NW-05 | NW-06 | NW-07 | NW-08 | independent_networks (AF) | networks (all) | ads |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PB-01 | — | — | {1, 119d, Solution} | {5, 87d, UNKNOWN} | {1, 36d, Problem} | {4, 271d, Problem/Product} | — | — | 0 | 4 | 11 |
| PB-02 | {13, 70d, Problem/Solution/Unaware} | {3, 0.1d, Problem} | {5, 540d, Problem/Solution} | {2, 77d, UNKNOWN} | — | {1, 13d, Problem} | — | — | 1 | 5 | 24 |
| PB-03 | — | — | — | {2, 87d, UNKNOWN} | — | {1, 47d, Product} | — | — | 0 | 2 | 3 |
| PB-04 | — | — | — | — | — | — | — | — | 0 | 0 | 0 |
| PB-05 | {5, 63d, Problem/Solution/Unaware} | — | {1, 119d, Solution} | {4, 87d, UNKNOWN} | — | {2, 271d, Problem} | — | — | 1 | 4 | 12 |
| PB-06 | — | — | — | — | — | — | — | — | 0 | 0 | 0 |
| PB-07 | {4, 60d, Problem/Unaware} | {3, 0.1d, Problem} | {5, 540d, Problem/Solution} | — | — | — | — | — | 1 | 3 | 12 |

**lanes_nobody_sells[] = ['PB-04', 'PB-06']** — PB-06 (built/tried a store, never made sales — 01's runner-up lead lane) and PB-04 (no time to run the store) appear in 0 of 32 ad records across 8 networks. PDP-level only: NW-08 PDP names PB-06 ("even a finished store often doesn't sell"); NW-03/NW-07/NW-08 sell operations management (PB-04-adjacent) on their pages, not in ads.

## §11 · KEYWORD ADVERTISER BANDS (concatenated verbatim from 02-partials/02-KEYWORDS.md §11; counts keep their count_basis)

**Method note (rule 2, printed plainly):** K1 launched all 18 GetHookd `search_ads` calls (2 per lane term: default `limit:5,compact:true` capped at `ads_per_brand_limit:4`, plus one with `ads_per_brand_limit:0` for the raw total) and all 9 Meta `ads_library_search` calls for the 9 lane terms in one batch, then the 10 GetHookd + 5 Meta calls for the 5 avatar phrases in a second batch (`limit:1` on GetHookd per the ≤2-charged-searches-per-phrase cap). Every total below is copied from a real tool response's own `meta.total` / `estimated_total_count` field — none is invented. **VALIDATION-DEGRADED, printed per rule 2:** at this batch scale (27 then 15 near-simultaneous calls returning very large payloads) a small number of the GetHookd buyer/clinical term pairs could not be re-verified against their `explore_url` field with full certainty after the fact; those cells are marked `~` (best-effort, anchored on a real response, cross-term attribution not 100% certain) rather than presented as exact. The two GetHookd totals I re-verified against `explore_url` with certainty ("can't figure out shopify": capped 256 / raw 867; "don't know how to build an online store": capped 2 / raw 2, both near-zero on a semantically-noisy hybrid match) are printed without `~`. Meta totals are printed as returned; Meta's own connector is known (tool-card addendum) to loose/semantic-match short phrases against its whole ad corpus, so a large `estimated_total_count` is corpus noise, not evidence of DFY-ecom advertiser density — `distinct page_id` relevant to DFY-ecom is the signal that matters, and is called out per row where a relevant page surfaced.

| term (form) | pb_id | advertisers_gethookd (brand-capped, apbl:4) | advertisers_gethookd (raw, apbl:0) | advertisers_meta (estimated_total_count, loose match) | relevant distinct page_id surfaced | oldest_days_active (relevant ad) | ads_live_90d+ | band (GetHookd, brand-capped) | late |
|---|---|---|---|---|---|---|---|---|---|
| "can't figure out shopify" (buyer) | PB-01 | 256 [R-TOOL count_basis:total,brand_capped] | 867 [R-TOOL count_basis:total,ads] | 1,047,982 [R-TOOL count_basis:estimated_total_count] — loose (fitness/TikTok noise, 0 of 50 skimmed DFY-relevant) | none DFY-relevant | — | — | SATURATED (≥50) | Y — oldest relevant ad seen in corpus (Merchant Mastery skool community) 17d, not ≥90d, so **late = N** on the ads actually inspected |
| "don't know how to build an online store" (buyer) | PB-01 | 2 [R-TOOL] (near-zero, low-relevance semantic match — Nerve Support Community / Julie Anderson neuropathy ads, category error, not DFY-ecom) | 2 [R-TOOL] | 360,927 [R-TOOL] — loose, generic phrase (mattress/gym/novel-app noise) | none DFY-relevant | — | — | UNCLAIMED (0 DFY-relevant advertisers found; GetHookd's 2 hits are off-category) | — |
| "hands-off store setup service" (clinical) | PB-01 | ~ (batch-scale, not re-verified) | ~ | 6,878 [R-TOOL] | none DFY-relevant in the rows read | — | — | NOT MAPPED — GetHookd cell not re-verifiable this session | — |
| "shopify store no sales" (buyer) | PB-06 | ~278 [R-TOOL, best-effort] | ~781 [R-TOOL, best-effort] | 148,236 [R-TOOL] — loose (leather-goods/gym noise) | Debutify (Shopify theme app, not DFY-ecom — adjacent tool, not a competitor) | 58 | Y (2 of 2 read ≥45d) | CROWDED–SATURATED range (best-effort) | — |
| "tried dropshipping lost money" (buyer) | PB-06 | ~204 [R-TOOL, best-effort] | ~535 [R-TOOL, best-effort] | 32 [R-TOOL] — tight literal match, meaningful low count | Drop Ship Lifestyle (dropshiplifestyle.com, brand_id 6960, page "Drop Ship Lifestyle") — DFY-adjacent education/coaching, COMPETITOR-CLAIMED close analog | 101 | Y | OPEN (Meta literal, 32) / CONTESTED-ish (GetHookd semantic) — bands disagree by tool, never averaged | — |
| "store with zero conversion" (clinical) | PB-06 | ~146 [R-TOOL, best-effort] | ~ | 34,490 [R-TOOL] — loose | none DFY-relevant | — | — | NOT MAPPED (GetHookd) / loose-noise (Meta) | — |
| "don't know what to sell online" (buyer) | PB-05 | 364 [R-TOOL] | 662 [R-TOOL] | 1,337,122 [R-TOOL] — loose (generic 3-word phrase) | **Ecom Websites** (get.ecomwebsites.com, brand_id 1437830, page_id 113202963644035) — direct DFY-ecom competitor, ad body literally reads "You don't know what to sell" — exact-match; also Patricia Demitro/kitlypet.com (off-category pet brand, noise) | 169 | Y | SATURATED (raw/capped both ≥50) | Y — 169d oldest ≥90d |
| "can't find a winning product" (buyer) | PB-05 | 163 [R-TOOL] | 266 [R-TOOL] | 12,156 [R-TOOL] — loose | Helium 10 (Amazon product-research SaaS, adjacent tool not DFY-ecom); Winning Hunter (product-research SaaS, same) | 332 (Winning Hunter ad) | Y | CROWDED–SATURATED | Y (332d ≥90d) |
| "validated product research service" (clinical) | PB-05 | 37 [R-TOOL] | 48 [R-TOOL] | 13 [R-TOOL] — tight literal match | Helium 10 (2 of 5 rows) | 57 | Y | CROWDED (37 brand-capped) | N |
| **avatar phrases (all ≤2 charged GetHookd calls at limit:1, ads_per_brand_limit as noted)** | | | | | | | | | |
| "online business for dads" | CP-02 (fathers, operator hypothesis a) | 182 [R-TOOL, limit:1 apbl:4] | 499 [R-TOOL, limit:1 apbl:0] | 10,971 [R-TOOL] — loose | none father/DFY-relevant in the row read (Everyday Wellness Journal, off-category) | — | — | SATURATED | Y (batch — not individually timed) |
| "side income for fathers" | CP-02 | 176 [R-TOOL] | 753 [R-TOOL] | 3,827 [R-TOOL] — loose | none relevant (Pocket FM fiction ads — pure semantic noise both tools) | — | — | SATURATED | Y |
| "retirement online business" | CP-06 (near-retirement, operator hypothesis b) | 253 [R-TOOL] | 696 [R-TOOL] | 1,133 [R-TOOL] — loose | none relevant (RV seat cushion ad — semantic noise) | — | — | SATURATED | Y |
| "online store for retirees" | CP-06 | 504 [R-TOOL] | 1,352 [R-TOOL] | 7,411 [R-TOOL] — loose | none relevant (neuropathy ad — noise) | — | — | SATURATED | Y |
| "passive income for parents" | CP-02, CP-07 | 122 [R-TOOL] | 220 [R-TOOL] | 1,728 [R-TOOL] — loose; **Cameron Hoffman - Business** ("Want My Team To Build You An eCom Business?"), **ECOM Auto Agency**, **Ecom Accelerator**, **Done for you brands**, **Joseph Lewis** (store-flipping, off-model) all surfaced here | none of the DFY-relevant pages read a body claiming the "dads/parents" avatar directly — avatar match is by the search term only, `avatar_evidence: PAGE-NAME` for the DFY pages found, not TITLE-BODY | — | — | SATURATED (raw) | — |

**Reading (rule 9 pattern threshold does not apply — this is a discovery count, not a structure count):** every one of the 14 lane-term + avatar-phrase queries returns a GetHookd/Meta total in the hundreds-to-millions, but almost none of the top rows actually read are DFY-ecom-relevant — the "shopify"/"online business"/"parents"/"dads" vocabulary is heavily shared with fitness studios, romance-fiction apps, health supplements and generic SaaS, which is itself a finding: **no lane term or avatar phrase is a clean, low-noise wedge into this market** — a paid-search or ad-library keyword strategy built on these literal phrases will spend against a saturated, off-category corpus unless narrowed by `landing_page_domain` or `niche` filters 03/07 can apply at MERGE. The handful of DFY-ecom-relevant advertisers that DID surface (Ecom Websites, Drop Ship Lifestyle, Cameron Hoffman - Business, Ecom Accelerator, Done for you brands, ECOM Auto Agency, and — from the K1 crawl-completeness checks other partials ran — Ecomfamilyhub/Ecomfamcrew/Ecom Family Academy) are listed once each in §17 as NEW SEED rows rather than repeated per keyword row.


## §12 · INCUMBENT MECHANISM MAP (one row per NW; ad ids renamed) + stated_cause_counts

| nw_id | stated_cause | stated_fix | handle | named_ingredient_or_feature | awareness_entry | ad_ids |
|---|---|---|---|---|---|---|
| NW-01 | Amazon/Shopify side hustles saturated; Walmart wide open; people think they need their own brand; job wage ceiling | resell trusted brand-name products on Walmart Marketplace; Walmart fulfils | "Walmart Wealth Window™" / "Scan To Profits™" | "ScanProfit mobile app"; AI product tool | Unaware→Problem (REPORT/lifestyle) · Solution (lists) | IM-01..IM-14 |
| NW-02 | ad-level NULL (body unopened); candidate site: no "cape" — an ordinary parent without capital or connections [D] | candidate site: free AI-built Shopify store → course → coaching [D] | "A-Z POD Main Course", "Winner's Circle" [D] | "EcomFamilyAcademy AI Shopify Store Builder" [D] | UNKNOWN (title-level) | IM-15..IM-17 |
| NW-03 | capital idle / under-performing (stocks, bonds, CDs, rental property); saturated mainstream platforms; lack of trend data & operating history | managed store on a "new"/"30-year" platform, 70/30 profit share, 16-month payback guarantee | "e-cash flow model"; "No Profit No Payment" | "100+ stores we manage"; "one store per person" (why partners) | Solution (offer) · Unaware-of-platform (curiosity teasers) | IM-18..IM-22 |
| NW-04 | tech/setup/product-picking overwhelm; procrastination; courses teach without delivering; being on the paying side of money | a DFY team builds, stocks (20/50 products + US suppliers) and hands over a Shopify store for $20, funded by Shopify commission | "$20 done-for-you store" | "Shopify pays them a commission"; 60-second quiz | Problem (CO-16) · Solution (CO-14) · Unaware (CO-15) | IM-23..IM-27 |
| NW-05 | "overwhelmed by the process", "complexities", account suspensions (site copy) | EcomXpertz sets up, sources, lists, manages (+ reinstatement) | NULL | NULL (service); "100% Money Back Guarantee" (conditioned) | Problem (site) | IM-28 |
| NW-06 | store-building complexity + not knowing what to sell; distrust of free offers; procrastination/self-doubt | DFY build (30 winning products, suppliers) funded by Shopify referral commission — "we only get paid when you succeed" | "$20/Free Done For You eCommerce Store" | Shopify Certified Partner; 2-minute quiz | Problem (2) · Product (1) | IM-29..IM-32 |
| NW-07 | "manual processes slow you down or create costly mistakes" (PDP) | automated store build/listing/sourcing/management across Shopify/Amazon/Walmart | "Fully Automated E-Commerce Store" | AI supplier screening | UNKNOWN (no ads) | none |
| NW-08 | beginners stuck for months building/sourcing/traffic; low-ticket products carry thin margins (PDP) | DFY build + high-ticket US dealer suppliers + ads setup | N/A (no ads) | high-ticket ($500+ AOV) positioning; milestone guarantee | Solution/Product (PDP) | none |

**stated_cause_counts** (stated_cause, networks n of NW 8 — ad-level first, page-level added; ABOVE-FLOOR in brackets):

| stated_cause | networks (ad-level) | networks (+PDP/site-level) | ABOVE-FLOOR | ad_ids |
|---|---|---|---|---|
| setup/tech complexity — the build is the barrier | 2 of 8 (NW-04, NW-06) | 5 of 8 (+NW-05, NW-07, NW-08) | 0 | IM-23,24,26,27,29,30 |
| not knowing what to sell / product choice | 3 of 8 (NW-04, NW-06, NW-03) | 4 of 8 (+NW-08) | 0 | IM-27,29,30,21 |
| marketplace saturation vs an open/new platform (timing) | 2 of 8 (NW-01, NW-03) | 2 of 8 (+—) | 1 | IM-01,02,04,05,07,08,11,12,18,19 |
| procrastination / self-doubt | 2 of 8 (NW-04, NW-06) | 2 of 8 (+—) | 0 | IM-27,32 |
| lack of operating data / expertise | 1 of 8 (NW-03) | 2 of 8 (+NW-05) | 0 | IM-21 |
| courses/gurus teach without delivering | 1 of 8 (NW-04) | 2 of 8 (+NW-08) | 0 | IM-23,24,25,26 |
| distrust of free offers / scam fear | 1 of 8 (NW-06) | 1 of 8 (+—) | 0 | IM-31 |
| idle or under-performing capital | 1 of 8 (NW-03) | 1 of 8 (+—) | 0 | IM-18(cards),20,21,22 |
| believing you need your own product/brand | 1 of 8 (NW-01) | 1 of 8 (+—) | 1 | IM-03,10 |
| job wage ceiling | 1 of 8 (NW-01) | 1 of 8 (+—) | 1 | IM-03,14 |
| being on the paying side of e-commerce money | 1 of 8 (NW-04) | 1 of 8 (+—) | 0 | IM-25 |
| no prior advantage as a parent ("no cape") | 0 of 8 (—) | 1 of 8 (+NW-02) | 0 | IM-15..17 (title) [D] |

## §13 · OFFER + FUNNEL TABLE

| nw_id | price_points[] | ladder_shape | guarantee | gifts | subscription | funnel_split (IM ads by destination) | penetration_offer |
|---|---|---|---|---|---|---|---|
| NW-01 | Free webinar → $27 → $47–97 → $99/mo → $1,995–1,997 → $2,997–3,000 → $4,300 | free webinar → high-ticket coaching (4+ rungs) | CONTRADICTORY (claimed "four figures or refund" vs BBB refund complaints) | none in ads | Y ($99/mo community, [R-PAGE]) | webinar/squeeze 13, comment-DM 1 | FREE webinar |
| NW-02 | candidate: FREE / $1,495 / $7,500 [D] | free lead magnet → course → coaching [D] | internally conflicting (30-day vs 72-hour) [D] | "30 Winning Products" [D] | Y (Shopify $1/mo pass-through) [D] | unknown 3 | FREE AI store builder [D] |
| NW-03 | $15K–$30K / $25K–$35K liquid; 70/30 split | single capital-threshold tier + ongoing profit share | 16-month "No Profit No Payment" (operator forgoes its share; not a cash refund) | none | N (profit share) | vsl 5 | NONE |
| NW-04 | $20 / $97 + Shopify $39/mo after 3×$1 + Zendrop $79/mo | low-ticket entry → upsell tier → disclosed recurring fees | 30-day 100% refund, "no questions asked"; CO-15 "refunded and keep the setup" | none | Y (platform + supplier fees, disclosed) | unknown 5 | $20 pre-built store |
| NW-05 | $3K–$8K / yr profit-split tiers | 3-rung annual retainer | refund only if not started (20 days) | none | Y (annual) | unknown 1 | NONE STATED |
| NW-06 | $0 / $20 advertised → $1/mo×3 + "processing fee of up to $500" | bait-then-upsell (ad price ≠ funnel price) | none in ads; funnel "all sales final" | none | Y (Shopify trial → paid plan) | quiz 4 | free/$20 store |
| NW-07 | $2,000 (Walmart automation); others UNKNOWN | UNKNOWN | "100% ROI guarantee within 6 months" (conditional) | none | N | 0 ads | NONE STATED |
| NW-08 | $9,997 / $14,997 / $19,997 + $2,997/mo + add-ons | 3 one-time build tiers + monthly turnkey + add-ons | milestone rebuild, no cash refunds | none | Y | 0 ads | top-tier 50% off, "Only 5 Spots" |

**penetration_offer (market):** the youngest scaler (NW-02, YOUNG-SCALER on ad evidence) = FREE AI store builder [D unconfirmed link]; the replicated low-ticket entry = $0–$20 DFY store (NW-04, NW-06). Readymerce's own $500 one-time package (01 F-12) has no ad-visible price neighbour: the ad corpus is bimodal ($0–$20 bait entries vs $1,995+ coaching / $15K+ capital) — [D] count from this table.

## §14 · LOSER / WINNER PAIRS

| pair_id | nw_id | loser_im | winner_im | what_differs |
|---|---|---|---|---|
| PAIR-01 (was PAIR-05-01) | NW-01 | IM-01 (ad 121358569, 70d, inactive, CTA "Learn more", 71s) | IM-02 (ad 126787289, 68d, active, Winning 100, CTA "See details", 12s) | visual (length/pacing 71s→12s) + CTA text; same CO-01 body. Caveat: the loser ran 70d — not an early kill (≤14d); printed as the partial coded it |

All other networks: `NONE FOUND — searched` (NW-02 one concept, all <1d; NW-03 6 ads all ≥119d; NW-04 synchronized rotation-out 72–89d; NW-05 1 ad; NW-06 variants differ only in media — reuse, not test pairs (cross-concept note: CO-20 free/procrastinator 13d vs CO-18 $20/setup 169–271d, partial §14); NW-07/NW-08 0 ads).

## §15 · KEEP-LIST (LK-##, renumbered; COMPETITOR-CLAIMED / company-hosted flagged)

| lk_id | nw_id | quote | url | kind | frequency |
|---|---|---|---|---|---|
| LK-01 | NW-06 | "Thank you to Evangelyn from Ecom Websites for being an amazing support agent and resolving questions I had about setting up my site." — Catherine Barrett, May 14 2025 | https://ca.trustpilot.com/review/ecomwebsites.com | trust | SAMPLE(1) |
| LK-02 | NW-06 | "The training videos are easy to understand. … the customer service was great. Very fast to respond" — David, May 14 2025 | https://ca.trustpilot.com/review/ecomwebsites.com | simplicity + trust | SAMPLE(1) |
| LK-03 | NW-06 | "They Did As Promise! Made Me A $20 Website!" — Natalie Lashley, Apr 17 2025 | https://uk.trustpilot.com/review/ecomwebsites.com | functional relief | SAMPLE(1) |
| LK-04 | NW-08 | "My first quarter of 2025 was 25K. After working with Trevor and his team, my first quarter of 2026 was 100K." — Kristin Store | https://shop.ecommerceparadise.com/pages/reviews | functional relief (company-hosted) | 1 |
| LK-05 | NW-08 | "Trevor has helped me make 7 figures in sales. The model works" — Zack Franklin | https://shop.ecommerceparadise.com/pages/reviews | trust (company-hosted) | 1 |
| LK-06 | NW-08 | "Recommend it for anyone who wants to skip the trial and error." — Nick Baxter | https://shop.ecommerceparadise.com/pages/reviews | simplicity (company-hosted) | 1 |
| LK-07 | NW-03 | "The stores run, and I get to focus on my family—and I have a very large family, so that matters." — Jen Michele Buckley, Mar 3 2026 | trustpilot.com/review/ecomaccelerator.io | functional relief (hands-off) | SAMPLE(1 of 5) |
| LK-08 | NW-03 | "The team is honest, reliable and responsive." — Don Carley, Nov 14 2025 | trustpilot.com/review/ecomaccelerator.io | trust | SAMPLE(1 of 5) |
| LK-09 | NW-03 | "The onboarding process was simple and seamless" — Mike Jansen, May 13 2025 | trustpilot.com/review/ecomaccelerator.io | simplicity | SAMPLE(1 of 5) |
| LK-10 | NW-04 | "I started selling in the health niche beginning of this month and was averaging 30% profit at $8K/day" — Noor Naser | doneforyoubrands funnel page "DFY Ecom Websites" [R-PAGE via Exa] | trust (company-hosted, unverifiable) | 1 |
| LK-11 | NW-02 | "We made six figures in just six months! I have 4 young kids too! This REALLY works!" | https://ecomfamily.com/ (candidate brand [D]) | functional relief (company-hosted) | 1 |
| LK-12 | NW-02 | "We made over 400% more than we spent on ads!" | https://ecomfamily.com/ (candidate brand [D]) | trust (company-hosted) | 1 |
| LK-13 | NW-02 | "This year alone our store has been able to generate over ONE MILLION DOLLARS in revenue!" | https://ecomfamily.com/ (candidate brand [D]) | aspirational (company-hosted) | 1 |
| LK-14 | NW-01 | "EDU is the best e-commerce program out there!" — Jill Nguyen | https://www.ecomdegree.com/testimonials | trust (company-hosted) | 1 |
| LK-15 | NW-01 | "Will doesn't gate-keep anything!" — Emily Eaton; Mark Michet | https://www.ecomdegree.com/testimonials | transparency (company-hosted) | 2 attributions |
| LK-16 | NW-01 | "Awesome people" — Luis C. | https://www.bbb.org/us/ga/duluth/profile/college-and-university/ecom-degree-university-0443-91821659 | rapport (on an F-rated profile) | 1 |

NW-05, NW-07: `LK: NONE FOUND — BLOCKED-ON-TOOL (Trustpilot)`. Counter-evidence kept in partials: NW-03 TikTok inconsistency / offshore-team complaints (5★ reviews); NW-02 BBB complaints ($1,500 course + $1,000 fast-track "still didn't work"); NW-01 BBB refund complaints.

## §16 · HOOK BANK (raw)

| im_id | nw_id | hook_verbatim (≤15w) | longevity_label | avatar_addressed |
|---|---|---|---|---|
| IM-01 | NW-01 | REPORT: A growing wave of young adults is cashing in on a hidden Walmart income | PROVEN | young adult / side-hustle seeker [D from shared body] |
| IM-02 | NW-01 | REPORT: A growing wave of young adults is cashing in on a hidden Walmart income | PROVEN | young adult / side-hustle seeker [D] |
| IM-03 | NW-01 | If you make less than $50 an hour, you should keep watching this ad | PROVEN | hourly-wage worker in a low-ceiling job |
| IM-04 | NW-01 | REPORT: A growing wave of young adults is cashing in on a hidden Walmart income | PROVEN | young adult / side-hustle seeker [D] |
| IM-05 | NW-01 | POV: How life looks when you sell products on Walmart while everyone else is still | PROVEN | young adult, competitive/status-driven |
| IM-06 | NW-01 | EXPOSED - Ecom expert exposes the top 10 products to sell on Walmart (And why | PROVEN | aspiring reseller wanting concrete proof |
| IM-07 | NW-01 | did you just... just fell! | PROVEN | broad/undifferentiated - no visible demographic signal |
| IM-08 | NW-01 | The Next Online Gold Rush | PROVEN | wealth/status-motivated aspirational viewer |
| IM-09 | NW-01 | 10 Everyday Walmart Products I Used to Quit My 9-5 For Good | LIKELY | aspiring reseller wanting concrete proof |
| IM-10 | NW-01 | The biggest lie in business? 'You need your own product.' | LIKELY | product-ideation-anxious, deterred by the 'need your own pro |
| IM-11 | NW-01 | No better business to start in 2026 | LIKELY | aspirational |
| IM-12 | NW-01 | The biggest opportunity of 2026 - Comment 'Walmart' for an invite to my next workshop | LIKELY | status/wealth-signaling-motivated |
| IM-13 | NW-01 | Grandmas can still get rich / How a 65-Year-Old Grandma Makes $7K a Month | LIKELY | older adult / retiree |
| IM-14 | NW-01 | Don't get another job in 2026 | LIKELY | job-averse young adult wanting a concrete recipe |
| IM-15 | NW-02 | I Didn’t Have a Cape. Just a Laptop and a Family to Fight For! | BET | father/parent providing for family via a laptop-run business |
| IM-16 | NW-02 | I Didn’t Have a Cape. Just a Laptop and a Family to Fight For! | BET | father/parent providing for family via a laptop-run business |
| IM-17 | NW-02 | I Didn’t Have a Cape. Just a Laptop and a Family to Fight For! | BET | father/parent providing for family via a laptop-run business |
| IM-18 | NW-03 | THIS New Ecommerce Platform Will Be Even Bigger Than Amazon | CONTROL-GRADE (dropped 1 rung: INCUMBENT) | wants a high-return investment opportunity without tradition |
| IM-19 | NW-03 | Top Economists Are Referring To THIS As Amazon's New Rival | CONTROL-GRADE (dropped 1 rung: INCUMBENT) | business owner with ~$25K liquid capital wanting portfolio d |
| IM-20 | NW-03 | If you are sitting on $25,000 or more and are looking for a smarter way | CONTROL-GRADE (dropped 1 rung: INCUMBENT) | capital holder ($25K+) wanting money to work; kids college f |
| IM-21 | NW-03 | If You Have Between $15K and $30k Liquid And Are Looking For | PROVEN (dropped 1 rung: INCUMBENT) | has $15K-$30K liquid capital, wants a new income stream with |
| IM-22 | NW-03 | If You Have Between $25K and $35k Liquid and Are Looking For | PROVEN (dropped 1 rung: INCUMBENT) | capital holder comparing e-commerce to stocks/bonds |
| IM-23 | NW-04 | STOP buying courses! I'll design you a beautiful store | PROVEN | course-burned aspiring seller, no store yet |
| IM-24 | NW-04 | NO compres mas cursos. Yo te hago una tienda online hermosa | PROVEN | Spanish-speaking aspiring online seller |
| IM-25 | NW-04 | People are stealing your money. And it's legal. | PROVEN | frustrated buyer wanting a second income stream |
| IM-26 | NW-04 | STOP buying courses! I'll design you a beautiful store | LIKELY | course-burned aspiring seller, no store yet |
| IM-27 | NW-04 | 77,254+ people have already claimed their online store | LIKELY | chronic procrastinator on starting a business |
| IM-28 | NW-05 | Launch Your Amazon Store with Confidence | LIKELY | wants to launch an Amazon store but lacks confidence (INFERR |
| IM-29 | NW-06 | Let me guess... You've been thinking about starting an online business | CONTROL-GRADE (dropped 1 rung: INCUMBENT) | aspiring online-business starter overwhelmed by DIY setup an |
| IM-30 | NW-06 | Let me guess... You've been thinking about starting an online business | PROVEN (dropped 1 rung: INCUMBENT) | aspiring online-business starter overwhelmed by DIY setup an |
| IM-31 | NW-06 | We were named the #1 Commerce Coach in North America | LIKELY (dropped 1 rung: INCUMBENT) | skeptical prospect worried the free offer is a scam |
| IM-32 | NW-06 | You've thought about starting an online store before | BET | repeat procrastinator who has put off starting an online sto |

## §17 · NEIGHBOURS + NEW SEEDS (deduped across all partials)

`list_similar_shops`: NOT RUN — no DFY-ecom shop_id resolved in any partial (NW-01 shop 24121 is education; not run at merge — no new research).

| seed_id | domain | how_found | sizing_row | queued |
|---|---|---|---|---|
| NEW SEED-01 | ecomwebsites.com | NW-SEED-01 §3; KEYWORDS K01 | UNSIZED (not shop-indexed); 922 historical ads | CRAWLED → NW-06 |
| NEW SEED-02 | Ecom Family pages (domain UNRESOLVED) | NW-SEED-03 NEW SEED-A; KEYWORDS K03 | 160 active (Meta) | CRAWLED → NW-02 |
| NEW SEED-03 | doneforyoubrands.co | NW-NEW-SEED-01 cand-1; KEYWORDS K06 | 32 active (GetHookd) | CRAWLED → NW-04 |
| NEW SEED-04 | ecomaccelerator.io | NW-NEW-SEED-01 cand-2; KEYWORDS K05 | 85 active (GetHookd) | CRAWLED → NW-03 |
| NEW SEED-05 | ecomdegree.com | NW-NEW-SEED-02 NEW SEED-C | 203 active; 78,722 visits | CRAWLED → NW-01 |
| NEW SEED-06 | Cameron Hoffman - Business (page 1134544756404510; domain UNRESOLVED) | KEYWORDS K04; NW-NEW-SEED-04 sibling candidate | UNSIZED; identical creative to NW-03 on Meta; merge search #1: not on GetHookd | NOT CRAWLED (cap) — if merged, joins NW-03 |
| NEW SEED-07 | socialtoast.ai | NW-SEED-01 §3; KEYWORDS K02 | UNSIZED; AI tool for existing brands (poor fit) | NOT CRAWLED (cap) |
| NEW SEED-08 | ecomflame.com | NW-NEW-SEED-01 §17 cand-3 | UNSIZED | NOT CRAWLED (cap) |
| NEW SEED-09 | ecomfamilyacademy.io ("The Ecom Family", brand 268253) | NW-NEW-SEED-02 NEW SEED-B | 0 active (dormant); last ad 32d, used_count 8 | NOT CRAWLED (cap) |
| NEW SEED-10 | dropshiplifestyle.com (Drop Ship Lifestyle, brand 6960) | KEYWORDS §11 "tried dropshipping lost money" | UNSIZED; education/coaching analog; oldest ad 101d | NOT CRAWLED (cap) |
| — off-topic | Joseph Lewis (page 1312002331990389) | KEYWORDS K1 | store-liquidation buyer | NOT QUEUED — category mismatch |

## §18 · CREDIT RECONCILIATION + EVIDENCE LEDGER

| scope | GetHookd spent (reported) | Exa $ | Meta | Apify |
|---|---|---|---|---|
| NW-SEED-01 | 0.66 | 0.100 | $0 | $0 (BLOCKED) |
| NW-SEED-02 | 1.58 | 0.125 | $0 | $0 (BLOCKED) |
| NW-SEED-03 | 1.28 | 0.100 | $0 | $0 (BLOCKED) |
| NW-NEW-SEED-01 | 1.90 | 0.130 | $0 | $0 (BLOCKED) |
| NW-NEW-SEED-02 | 1.92 | 0.150 | $0 | $0 (BLOCKED) |
| NW-NEW-SEED-03 | 1.34 | 0.100 | $0 | $0 (BLOCKED) |
| NW-NEW-SEED-04 | 1.04 | 0.200 | $0 | $0 (BLOCKED) |
| NW-NEW-SEED-05 | 0.45 | 0.150 | $0 | $0 (BLOCKED) |
| KEYWORDS | 2.29 | 0.000 | $0 | $0 (BLOCKED) |
| **partials total** | **12.46** | **1.055** | $0 | $0 |
| 03 MERGE | 0.10 (search_ads ×2 at 0.05; get_ad ×3 free; get_user_profile free) | 0 | $0 | $0 |

Merge balance: remaining_credits before 283.63 → after 283.17 (delta 0.46; reported used_credits 0.10; unattributed 0.36 — the account is shared by concurrent W2 agents, ASSUMED; final re-read printed in 03 §22).

**Evidence ledger — every ad id with share_url** (landing page in brackets):

- IM-01 · NW-01 · ad 121358569 · https://app.gethookd.ai/share/ad/121358569 [https://join.ecomdegree.com/]
- IM-02 · NW-01 · ad 126787289 · https://app.gethookd.ai/share/ad/126787289 [https://join.ecomdegree.com/]
- IM-03 · NW-01 · ad 121358672 · https://app.gethookd.ai/share/ad/121358672 [https://join.ecomdegree.com/]
- IM-04 · NW-01 · ad 134426761 · https://app.gethookd.ai/share/ad/134426761 [https://join.ecomdegree.com/]
- IM-05 · NW-01 · ad 134427111 · https://app.gethookd.ai/share/ad/134427111 [https://join.ecomdegree.com/]
- IM-06 · NW-01 · ad 134426818 · https://app.gethookd.ai/share/ad/134426818 [https://join.ecomdegree.com/]
- IM-07 · NW-01 · ad 134426835 · https://app.gethookd.ai/share/ad/134426835 [https://join.ecomdegree.com/]
- IM-08 · NW-01 · ad 144205353 · https://app.gethookd.ai/share/ad/144205353 [https://join.ecomdegree.com/]
- IM-09 · NW-01 · ad 159706760 · https://app.gethookd.ai/share/ad/159706760 [https://join.ecomdegree.com/]
- IM-10 · NW-01 · ad 169343657 · https://app.gethookd.ai/share/ad/169343657 [https://join.ecomdegree.com/]
- IM-11 · NW-01 · ad 169343649 · https://app.gethookd.ai/share/ad/169343649 [https://join.ecomdegree.com/]
- IM-12 · NW-01 · ad 169343631 · https://app.gethookd.ai/share/ad/169343631 [https://join.ecomdegree.com/]
- IM-13 · NW-01 · ad 169343626 · https://app.gethookd.ai/share/ad/169343626 [https://join.ecomdegree.com/]
- IM-14 · NW-01 · ad 169343625 · https://app.gethookd.ai/share/ad/169343625 [https://join.ecomdegree.com/]
- IM-15 · NW-02 · ad 2157168075190848 · https://www.facebook.com/ads/library/?id=2157168075190848 [UNKNOWN — searched: Meta connector returns no destination-URL field]
- IM-16 · NW-02 · ad 1658080129273784 · https://www.facebook.com/ads/library/?id=1658080129273784 [UNKNOWN — searched: Meta connector returns no destination-URL field]
- IM-17 · NW-02 · ad 2771287676600895 · https://www.facebook.com/ads/library/?id=2771287676600895 [UNKNOWN — searched: Meta connector returns no destination-URL field]
- IM-18 · NW-03 · ad 41256434 · https://app.gethookd.ai/share/ad/41256434?signature=e8a15c2928e9af905e43d3910890fbb812ff2bb963359a0f0735c73c5531106d [https://go.ecomaccelerator.io/fb/vsl]
- IM-19 · NW-03 · ad 41256429 · https://app.gethookd.ai/share/ad/41256429?signature=cd7fb61172b397f9cf1ed31f15b016ffcde566992b61520b8c2729d3b099db79 [https://go.ecomaccelerator.io/fb/vsl]
- IM-20 · NW-03 · ad 78640432 · https://app.gethookd.ai/share/ad/78640432?signature=479e6dd58f5153a0e3c071b04251b0f0118ec2f78c90cf1756c700a3d3960892 [https://go.ecomaccelerator.io/fb/vsl]
- IM-21 · NW-03 · ad 103675232 · https://app.gethookd.ai/share/ad/103675232?signature=60433a54256945cbcdb5a0821ffc33a367828edef41fc929f2da71fbf469e1c4 [https://go.ecomaccelerator.io/fb/vsl]
- IM-22 · NW-03 · ad 93128874 · https://app.gethookd.ai/share/ad/93128874?signature=a03a35fd0ea5abb859584f7c25f2bad7767f4d516e0d2dc179ca6afe146d9377 [https://go.ecomaccelerator.io/fb/vsl]
- IM-23 · NW-04 · ad 74657770 · https://app.gethookd.ai/share/ad/74657770?signature=6f779e03e342dd398fa616c388c6e144bd4ece9be24e20e8a92347a47c0b05cb [https://go.doneforyoubrands.co/main-fe-dup-v2]
- IM-24 · NW-04 · ad 59411595 · https://app.gethookd.ai/share/ad/59411595?signature=272b1fe119a29c973dcac9ba3e90311e2154265b2acb04d511f5957c2c97e97a [https://www.doneforyoubrands.co/esp-start]
- IM-25 · NW-04 · ad 59618906 · https://app.gethookd.ai/share/ad/59618906?signature=40a869f5466ec7c527a980451058595b2f6e2c1d12264dd468ad6a70f6be5104 [https://go.doneforyoubrands.co/main-fe-dup-v2]
- IM-26 · NW-04 · ad 150503331 · https://app.gethookd.ai/share/ad/150503331?signature=3711eb03b9d012e6660423adc347087b15c9e200ac98237ebc420386cedb566e [https://shop.doneforyoubrands.co/dfy-quiz-a134]
- IM-27 · NW-04 · ad 169243242 · https://app.gethookd.ai/share/ad/169243242?signature=6797bde10225a3ff86c983861303b40ab8f2ec2c787d57ec8ffb5821308fea47 [https://shop.doneforyoubrands.co/dfy-quiz-a169]
- IM-28 · NW-05 · ad 1376173990650081 · https://www.facebook.com/ads/library/?id=1376173990650081 [UNKNOWN — searched]
- IM-29 · NW-06 · ad 70486040 · https://app.gethookd.ai/share/ad/70486040?signature=b7db77c179553f0c8f51bda348fd316240e45a9fab29a5fdc9e52b230182a9f7 [https://get.ecomwebsites.com/start]
- IM-30 · NW-06 · ad 70823628 · https://app.gethookd.ai/share/ad/70823628?signature=6120835b930418bb3cc11e315adcc84b0d35b3c9213e6234979bb5afe1535ed0 [https://get.ecomwebsites.com/start]
- IM-31 · NW-06 · ad 97210901 · https://app.gethookd.ai/share/ad/97210901?signature=934e795d8ebd0568d7c95568076fbe44fb1df5eb280d87560d60edfbad75bba3 [https://build.ecomwebsites.com/]
- IM-32 · NW-06 · ad 97803506 · https://app.gethookd.ai/share/ad/97803506?signature=6c0bfd58c7fb7b6582c05530b87149f917bc9a1d61279df2a13acd7cd35a7435 [https://build.ecomwebsites.com/]

Landing-page / PDP URLs read by the partials (Exa, [R-PAGE via Exa]): join.ecomdegree.com · ecomdegree.com/testimonials · ecomfamily.com · store.ecomfamilyacademy.io · ecomaccelerator.io · go.ecomaccelerator.io/fb/vsl · shop.doneforyoubrands.co/dfy-quiz-a134 · go.doneforyoubrands.co/main-fe-dup-v2 · ecomxpertz.com (11 pages) · build.ecomwebsites.com · get.ecomwebsites.com · go.ecomwebsites.com · ecomdoneforyou.com/* · ecommerceparadise.com/products/* · shop.ecommerceparadise.com/pages/reviews (full lists in each partial §18).

## COVERAGE STATEMENT (02, scope ALL — merged)

COVERAGE: networks 8 (ABOVE-FLOOR 1 · UNSIZED 7) from 3 seeds + 5 NEW SEEDs and q=91 queries (47 crawl-end searches per partial CRAWL COMPLETE lines + 42 KEYWORDS calls + 2 merge ambiguity searches); serious ads found per NW with count_basis (NW-01 210 exact · NW-02 160 Meta est. · NW-03 85 active · NW-04 32 active · NW-05 1 · NW-06 922 historical · NW-07 0 · NW-08 0 — never added), 32 IM coded, 23 FULL-BODY opened, NOT OPENED (cap) ≈ 196 + ≥154 duplicates + ~80 + 33 + ~24 (per partial); STRICT 0; avatar detected 32 of 32 (NW-02 and NW-05 from titles only); lanes covered 5 of 7 (PB-04, PB-06 nobody sells); competitor components captured 8 of 8 PDP sets (NW-02 candidate brand [D]); new seeds 10 (5 crawled → NW-01..04, NW-06 / 5 NOT CRAWLED (cap)) + 1 off-topic; credits spent GetHookd 12.56 (partials 12.46 + merge 0.10; reported), Exa $1.055, Apify $0 (BLOCKED-ON-TOOL); NOT MAPPED: traffic for 7 of 8 networks (UNSIZED), NW-02 landing domain + bodies, Cameron Hoffman sibling, 5 NW-01 transcripts, GetHookd cls_* fields, pct_active on 6 networks, 2 of 9 KEYWORDS GetHookd cells; counts keep their count_basis and are never added across tools; CONFIDENCE: network map PARTIAL (8 networks crawled to end, but only 1 sized ABOVE-FLOOR and 1 sibling unresolved), winners FULL-BODY 23 of 32 (STRICT 0), coverage map [10 personas incl. 3 AV-cand, 0 VACANT, 2 NOT MAPPED (<3 avatar-phrase searches) after 5 avatar-phrase searches] because the three original seeds carry ~0 ads (VALIDATION-DEGRADED) and the ad-rich networks are UNSIZED or education/coaching.
