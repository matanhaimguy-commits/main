# 01 — PRODUCT TRUTH + PROBLEM MAP · Readymerce · MODE: SEED
agent_id: 01 · wave W0 · started 2026-09-24T20:13:12Z · box: 10 min / 40 tool calls · model: opus
LOCK CARD: writer = agent 01 (SEED sections §1–§12 only). §TRUTH CARD is reserved for agent 01-DEEP (W1) — SEED never writes it; DEEP never edits SEED rows.

## §1 · INPUT CARD
| field | value | state |
|---|---|---|
| PRODUCT NAME | Readymerce | GIVEN (present → no STOP) |
| PDP LINK | https://readymerce.com | GIVEN (our own site) |
| TARGET MARKET | US · USD · en · Meta countries ["US"] | ASSUMED |
| BUDGET LEVEL | standard | ASSUMED |
| BRAND NAME | Readymerce | GIVEN (existing) |
| CATEGORY | done-for-you e-commerce store / dropshipping business-in-a-box (service) | INFERRED (brief + PDP + [R-OWNED] transcripts) — confirmed §2 |
| PRICE | see §2 | INFERRED ([R-OWNED] transcripts + PDP) |
| COMPETITORS | none given | INFERRED — §3 seeds from 3 free searches |
| OPERATOR ICP HYPOTHESES | (a) fathers wanting a better future for their children / more time with kids & wife; (b) adults 50+ with money who want an online business | HYPOTHESIS (operator-supplied, not validated by being supplied) |
| OPERATOR PROBLEM STATEMENT | inbound leads low quality ("tire kickers"); wants narrow ICPs of buyers ready to invest | CONTEXT — not VOC |
| MODE | SEED (objects 1–9; DEEP objects 10–13 → agent 01-DEEP) | GIVEN |
| OWNED DATA | 280 sales-call transcripts; ≤10 longest read for category/price ladder/PB/CP seeding only | [R-OWNED] — never counted as reviews or market VOC |

## §2 · PRODUCT IDENTITY + SOURCE LOCK

**Fetch chain for https://readymerce.com (3 attempts, rule 13):** WebFetch → `EGRESS_BLOCKED` · Firecrawl scrape → `Insufficient credits` · Apify rag-web-browser → `Monthly usage hard limit exceeded` ⇒ **PDP: BLOCKED-ON-TOOL** (chain exhausted). Identity below is built from WebSearch result titles/summaries of readymerce.com `[R-SNIPPET]`, the Meta Ad Library `[R-TOOL]` and 10 owned sales calls `[R-OWNED]` (seller-side, never VOC).

| field | value | state |
|---|---|---|
| sku_name | Readymerce — done-for-you Shopify & Etsy store (build + manage) | [R-SNIPPET] page title 'Readymerce: Done-For-You Shopify & Etsy Stores - Built and ...' |
| category | done-for-you e-commerce store / dropshipping business-in-a-box (SERVICE) | INFERRED ([R-SNIPPET] + [R-OWNED] T-01..T-10) — confirmed |
| pdp | https://readymerce.com (NOT FETCHED — BLOCKED-ON-TOOL); backup https://readymerce.com/services ('Readymerce — Your E-Commerce Empire, Managed.') | [R-SNIPPET] |
| variant | platform variant: Shopify store OR Etsy store (≈$500 each at entry) | INFERRED ([R-OWNED] T-01) |
| physical_form | service / digital (no physical SKU) | given (brief) |
| components[] | 11 — see table below | given {comp_given} / INFERRED {comp_inf} |
| specs{} | delivery 'within a matter of days' [R-SNIPPET]; Etsy build '7 up to 10 days' [R-OWNED T-09]; 'limited number of stores launched each month' [R-SNIPPET] | INFERRED |
| price | ladder: 'Spark'/gateway 'Build Business' $500 one-time, one store → 'Boss Boost'/'Full Service Launch' $2,000 → higher packages exist, rep: 'even 500,000 packages but ... very very rare'; Trustpilot reviewer paid a $250 deposit; SE call quoted ≈$400 starter | INFERRED ([R-OWNED] T-01, T-02, T-05, T-06; R-01 [R-SNIPPET]) — PDP price UNKNOWN (not fetched) |
| unit_cost | UNKNOWN — searched: no cost source reachable; R-01 reviewer says build used 'workers from the Philippines' (reviewer claim) | UNKNOWN |
| shipping_time_to_market | days (see specs) | INFERRED |
| landed_cogs [D] | N/A — service; delivery cost = offshore build labour + ad credits [D] | N/A |
| supplier_rating / supplier_orders / supplier_review_count / moq | N/A — service, no supplier listing exists | N/A |
| reference_images_viewed | 0 (PDP not fetched) | UNKNOWN |
| backup_listing_url | https://readymerce.com/services | [R-SNIPPET] |
| meta_presence | page 'Readymerce' id 923106680896349 · 31 active ads (estimated_total_count 31, US-reached) · delivery starts 2026-09-08→2026-09-14 · ad currency ILS · link title 'We build it. We run it. You own it.' (4 of 31; 27 blank) | [R-TOOL] ads_library_search |
| gethookd | list_shops q:'readymerce.com' → top row gocase.com.br (no match) ⇒ NOT INDEXED | [R-TOOL] |
| lock_state | PROVISIONAL-ON-[A] — [A] identity = snippets + seller calls; PDP unread | — |

**SUPPLIER: UNKNOWN — searched: N/A (service — no supplier listing; rating/orders/MOQ do not apply).**

**components[]** (j of J = 11; given 0 / INFERRED 11):

| id | name | state |
|---|---|---|
| C1 | store build on Shopify or Etsy (one store per entry package) | INFERRED ([R-SNIPPET] readymerce.com title 'Done-For-You Shopify & Etsy Stores - Built and ...'; [R-OWNED] T-01, T-06) |
| C2 | store branding | INFERRED ([R-SNIPPET] readymerce.com summary; [R-OWNED] T-06 'brand it for you') |
| C3 | product research + 3 vetted products listed | INFERRED ([R-SNIPPET] package summary 'three vetted products'; [R-OWNED] T-05 'three products listed by our side') |
| C4 | supplier / dropshipping fulfilment setup ('shortlisted supplier' at $2,000 tier) | INFERRED ([R-SNIPPET] 'professionally built dropshipping store'; [R-OWNED] T-06) |
| C5 | marketing: organic (Etsy entry) / 'one professional campaign' + retargeting; paid marketing packages via credits | INFERRED ([R-OWNED] T-05, T-06, T-04) |
| C6 | 1-on-1 strategy session / Zoom with an expert | INFERRED ([R-SNIPPET] '1-on-1 strategy session'; [R-OWNED] T-03, T-05) |
| C7 | ongoing store management ('We run it' / managed daily) | INFERRED ([R-TOOL] Meta ad title 'We build it. We run it. You own it.'; [R-SNIPPET] 'build, launch and manage ... daily') |
| C8 | client portal: balances, credits/top-ups, campaign packages, monthly trend report, personal roadmap | INFERRED ([R-OWNED] T-04, T-06) |
| C9 | dedicated account manager + priority delivery (higher tier) | INFERRED ([R-OWNED] T-06) |
| C10 | 7-day 100% money-back guarantee counted from launch (certificate); refund → Readymerce keeps the store | INFERRED ([R-OWNED] T-04, T-05) — SELLER EXPLANATION |
| C11 | buyer owns the store ('You own it') | INFERRED ([R-TOOL] Meta ad title; [R-SNIPPET] 'You own the store') |

**What it does (≤60w, 50w):** Readymerce is a done-for-you e-commerce service: a team builds and brands a Shopify or Etsy store, lists a few researched products, sets up marketing and keeps managing it while the buyer owns the store. Sold by phone; entry ≈$500 one-time, full launch ≈$2,000, 7-day refund after launch; no income guarantee. `INFERRED ([R-SNIPPET] + [R-OWNED])`

**Seller-internal contradiction (for 12/13 claims router):** PDP snippet 'no income guarantees or projected returns of any kind' [R-SNIPPET] vs sales-call lines '91 percent of our clients have a success rate within the first two to three weeks' and 'our goal is to get you making 10k a month' [R-OWNED T-04], 'a successful store ... might make like $5,000 in three months' [R-OWNED T-05]. `SELLER EXPLANATION` — never a product fact.

**Market note:** the 10 owned calls include UK (+44 caller IDs, prices in pounds) and one Swedish prospect (krona) — owned data is not US-only `[D]`; Meta ads are billed in ILS. Market stays `US ASSUMED`.

## §3 · COMPETITOR SEED LIST (NW-SEED-##)

Searches: (1) WebSearch 'done for you ecommerce store business service reviews' → 9 results, 7 DFY-ecom entities · (2) Meta ads_library_search 'done for you ecommerce store' (US, ACTIVE) → estimated_total_count 63,707; 50 read; 20 distinct page_names, 0 of 20 a DFY-store service (keyword noise) · (3) GetHookd list_shops q:'done for you' country US → total 18, 5 read (pourcaddy.com, the-2cities.com, bymeandcrew.com, magholder.com, eatlasso.com), 0 of 5 a DFY-store service. ⇒ seeds from search (1) only.

| seed_id | domain | how_found | page_name | pdp_url | headline_claim (≤15w) | named_problems[] | price | ladder_if_visible |
|---|---|---|---|---|---|---|---|---|
| NW-SEED-01 | ecomdoneforyou.com | web search 'done for you ecommerce store business service reviews' → trustpilot.com/review/ecomdoneforyou.com + reviews.io/company-reviews/store/ecomdoneforyou.com | Ecom Done For You | https://ecomdoneforyou.com (NOT FETCHED) | 'Ecom Done For You' (brand name = the claim) COMPETITOR-CLAIMED | PB-01 | UNKNOWN — searched: page fetch blocked | UNKNOWN — 02 reads |
| NW-SEED-02 | ecommerceparadise.com | same web search → /products/done-for-you-custom-high-ticket-dropshipping-store + /best-done-for-you-ecommerce-store/ | Ecommerce Paradise | https://ecommerceparadise.com/products/done-for-you-custom-high-ticket-dropshipping-store (NOT FETCHED) | 'Turnkey Done-For-You High-Ticket Drop Shipping ... Business-in-a-Box Build and Launch Service' COMPETITOR-CLAIMED | PB-01, PB-05, PB-06 | UNKNOWN — searched: page fetch blocked | UNKNOWN — 02 reads (list_shop_products) |
| NW-SEED-03 | ecomxpertz.com | same web search → ca.trustpilot.com/review/ecomxpertz.com | EcomXpertz (name as listed) | UNKNOWN — searched: not fetched | UNKNOWN — searched: no claim text reachable | UNKNOWN | UNKNOWN | UNKNOWN |

**k of K seeds checked: 0 of 3 PDPs fetched** (WebFetch egress-blocked for ecommerceparadise.com, trustpilot.com; Firecrawl/Apify out of credit) — claims come from result titles/summaries only `[R-SNIPPET]`, all `COMPETITOR-CLAIMED`. Editorial line from the ecommerceparadise.com comparison result (summary): a fully assembled site 'without traffic, margins, and trust' is 'just a storefront' → PB-06. **RESERVE seeds for 02:** doneforyoustrategy.com (Done For You LLC), nn-dfysuccess.com (DONE FOR YOU®), 'Done for You Ecom' (BBB profile Richmond TX, domain UNRESOLVED), Done For You Brands (vocal.media review). GetHookd `start_brand_spy`: NOT RUN — needs operator yes: start_brand_spy.

## §4 · REACHABLE REVIEWS (light R-## rows) + PROBLEM FREQUENCY

Amazon: **REVIEWS: NONE REACHABLE — DEEP fills** (service — no Amazon listing door). Review door = Trustpilot / BBB / reviews.io of readymerce.com + seeds; every page fetch blocked, so rows are WebSearch summaries `[R-SNIPPET]` — **not verbatim**; only fragments in quotes were quoted by the result. Stars not visible in any snippet.

| r_id | source | url | stars | text (snippet summary) | problem_named[] | population_marker | sku | valence |
|---|---|---|---|---|---|---|---|---|
| R-01 | Trustpilot readymerce.com (1 review listed) via WebSearch summary | https://uk.trustpilot.com/review/readymerce.com | UNKNOWN (snippet: 'quite negative') | SNIPPET SUMMARY, not verbatim: charged a $250 deposit for store building 'using workers from the Philippines'; refused to provide access codes and withheld the theme from the completed store; still trying to get money back. Company reply (summary): store built and delivered; code issued at customer's request so ownership stayed with them. | PB-01, PB-03 | CP-03 (paid a deposit, trying to get money back) | EXACT-SKU | − |
| R-02 | DFY-ecom review pool (attribution UNRESOLVED among trustpilot doneforyoustrategy.com / ecomdoneforyou.com / nn-dfysuccess.com / reviews.io / BBB / ecomxpertz) | WebSearch result set q='done for you ecommerce store business service reviews' | UNKNOWN | SNIPPET SUMMARY: team knowledgeable and responsive, got the store up and running quickly. | PB-01 | none | CATEGORY-PROXY | + |
| R-03 | same pool (UNRESOLVED) | same | UNKNOWN | SNIPPET SUMMARY: service got the brand approved on Walmart and handled all product uploads. | PB-01 | brand owner selling on Walmart | CATEGORY-PROXY | + |
| R-04 | same pool (UNRESOLVED) | same | UNKNOWN | SNIPPET SUMMARY: Shopify automation made repetitive tasks (order processing, stock updates) seamless; quoted fragment: 'trustworthy service for busy e-commerce owners'. | PB-04 | CP-04 busy e-commerce owner | CATEGORY-PROXY | + |
| R-05 | same pool (UNRESOLVED) | same | UNKNOWN | SNIPPET SUMMARY: Shopify store setup took 2 months and was not finished despite being promised a complete start-to-finish 'hands off' service. | PB-01, PB-03 | none | CATEGORY-PROXY | − |

**Counter:** reviews reachable 5 `[R-SNIPPET]` (1 exact-SKU, 4 category-proxy = SIMILAR PRODUCT CONTEXT) · read in full 0 · sources 2 (Trustpilot readymerce.com; DFY review pool) · `SAMPLE(5)`. Readymerce Trustpilot shows 1 review total (search summary). [R-OWNED] calls read: 10 of 280 (longest by bytes; list in datasets/01-seed-transcripts-read.txt) — never counted as reviews.

**Problem frequency (snippet rows):**

| rank | pb_id | matches (n of N) | praise | complaints | avg star | sources |
|---|---|---|---|---|---|---|
| 1 | PB-01 | 4 of 5 | 2 | 2 | UNKNOWN | 2 |
| 2 | PB-03 | 2 of 5 | 0 | 2 | UNKNOWN | 2 |
| 3 | PB-04 | 1 of 5 | 1 | 0 | UNKNOWN | 1 |
| 4 | PB-02 | 0 of 5 | 0 | 0 | UNKNOWN | 0 |
| 5 | PB-05 | 0 of 5 | 0 | 0 | UNKNOWN | 0 |
| 6 | PB-06 | 0 of 5 | 0 | 0 | UNKNOWN | 0 |
| 7 | PB-07 | 0 of 5 | 0 | 0 | UNKNOWN | 0 |

## §5 · PROBLEM MAP (PB-##) — one card per PB in label order

Label code (rule 3): door (a) counts only with ≥3 mentions AND praise > complaints; net-negative mentions become counterevidence. SEED labels are provisional until the DEEP refresh.

### PB-01 · SUPPORTED
- name_buyer_words: 'promised a complete start-to-finish "hands off" service' (R-05 fragment) — I can't / won't build and set up the store myself
- name_market_or_clinical: store setup + technical build burden (theme, listings, uploads, payments)
- entry_doors[]: COMPETITOR-CLAIM, MECHANISM-PLAUSIBLE
- review_mentions: 4 of 5 read (snippet) — R-01, R-02, R-03, R-05 · avg_star_of_mentioning_reviews: UNKNOWN (no stars in snippets)
- competitor_claim_count: 2 of 3 seeds checked (NW-SEED-01, NW-SEED-02) COMPETITOR-CLAIMED
- mechanism_plausibility_line: C1 build + C2 branding + C3 listed products remove the setup labour; delivered 'within days' [R-SNIPPET] / 7–10 days Etsy [R-OWNED T-09].
- product_contribution_boundary: Ends the build and handover; does not create demand, traffic or income (PDP: 'no income guarantees' [R-SNIPPET]).
- struggling_moment: [D] evening after work, laptop open on a half-finished Shopify theme or a YouTube tutorial; trigger = another weekend lost to setup with nothing live. Owned echo: 'Show me what my $500 is gonna get me' [R-OWNED T-01].
- four_forces: push — setup is technical and slow; prior attempt stalled [D] · pull — a finished, branded store handed over ('We build it') [R-TOOL] · anxiety — paying and not getting the store/access (R-01, R-05) · habit — 'I'll learn it myself' via free tutorials [D]
- pain_layer: functional · toleration_threshold: [D] acts after a stalled DIY attempt or when a vendor quote feels bounded (≈$500 one-time) · consequence_if_untreated: the idea never goes live; savings stay idle [D]
- alternatives_set[]: DIY Shopify/Etsy + YouTube; course/guru program; Fiverr/Upwork store builder; pre-built $20 Shopify store ([R-OWNED] T-07 rep line); other DFY services (NW-SEED-01..03)
- current_spend_hypothesis[]: $250 deposit (R-01); $500 entry / $2,000 full launch ([R-OWNED] T-06); prior vendor asked '10 grand' ([R-OWNED] T-08)
- candidate_populations[]: CP-05, CP-01
- counterevidence: R-01, R-05

### PB-06 · SUPPORTED
- name_buyer_words: 'I tried once during Covid' [R-OWNED T-03] · 'I've tried e-commerce' [R-OWNED T-08] — built/tried a store and never made sales
- name_market_or_clinical: store with no traffic / zero conversion (failed DIY attempt)
- entry_doors[]: COMPETITOR-CLAIM, MECHANISM-PLAUSIBLE
- review_mentions: 0 of 5 read (snippet) — — · avg_star_of_mentioning_reviews: UNKNOWN (no stars in snippets)
- competitor_claim_count: 1 of 3 seeds checked (NW-SEED-02) COMPETITOR-CLAIMED
- mechanism_plausibility_line: C5 campaigns + C8 credit-funded marketing aim traffic at the store; results vary.
- product_contribution_boundary: Supplies marketing execution; sales outcome not guaranteed (seller rep: '95% of people that try it ... never make a sale' [R-OWNED T-06]).
- struggling_moment: [R-OWNED T-08] prospect who put down £1,300 on a prior attempt; trigger = realising the earlier store earned nothing.
- four_forces: push — earlier store made nothing [R-OWNED] · pull — professionals running campaigns [D] · anxiety — another loss ([R-OWNED] T-10) · habit — 'e-commerce doesn't work for me' [D]
- pain_layer: emotional / future-fear · toleration_threshold: [D] acts when a second attempt can be handed to someone accountable · consequence_if_untreated: [D] writes off e-commerce and the sunk cost
- alternatives_set[]: retry DIY; hire ads freelancer; quit
- current_spend_hypothesis[]: £1,300 prior ([R-OWNED] T-08)
- candidate_populations[]: CP-03, CP-05
- counterevidence: NULL — searched: 5 snippet rows

### PB-05 · SUPPORTED
- name_buyer_words: 'I don't know what to sell' [D] — owned rep framing: 'winning product shortlisted' [R-OWNED T-06]
- name_market_or_clinical: product selection / winning-product research
- entry_doors[]: COMPETITOR-CLAIM, MECHANISM-PLAUSIBLE
- review_mentions: 0 of 5 read (snippet) — — · avg_star_of_mentioning_reviews: UNKNOWN (no stars in snippets)
- competitor_claim_count: 1 of 3 seeds checked (NW-SEED-02) COMPETITOR-CLAIMED
- mechanism_plausibility_line: C3 three vetted products + C4 supplier shortlist pick what to sell and who ships it.
- product_contribution_boundary: Selects products; cannot guarantee demand.
- struggling_moment: [D] scrolling 'winning product' lists and not trusting any pick.
- four_forces: push — fear of picking a dud [D] · pull — researched products + supplier [R-SNIPPET] · anxiety — product doesn't sell [D] · habit — keep researching [D]
- pain_layer: functional · toleration_threshold: [D] after a failed pick or endless research · consequence_if_untreated: [D] never launches or launches a dud
- alternatives_set[]: product-research tools; guru 'winning product' lists; Etsy handmade
- current_spend_hypothesis[]: UNKNOWN — searched: none reachable
- candidate_populations[]: CP-05
- counterevidence: NULL — searched: 5 snippet rows

### PB-03 · HYPOTHESIS
- name_buyer_words: 'I don't want this to be a scam' [R-OWNED T-08] · 'I feel like it's a scam' [R-OWNED T-04] · 'it was only scammers and I just lost money' [R-OWNED T-10]
- name_market_or_clinical: prior loss to online-income offers / vendor trust deficit
- entry_doors[]: MECHANISM-PLAUSIBLE
- review_mentions: 2 of 5 read (snippet) — R-01, R-05 · avg_star_of_mentioning_reviews: UNKNOWN (no stars in snippets)
- competitor_claim_count: 0 of 3 seeds checked (—) COMPETITOR-CLAIMED
- mechanism_plausibility_line: C10 7-day refund after launch, C11 ownership and C8 portal transparency address the fear; they do not refund past losses.
- product_contribution_boundary: Can reduce risk of the next purchase; cannot undo earlier losses. R-01 shows the same fear aimed at Readymerce itself.
- struggling_moment: [R-OWNED T-08] prospect recalls putting down £1,300 elsewhere and being asked for '10 grand'; trigger = a new sales call.
- four_forces: push — money already lost ([R-OWNED] T-08, T-10) · pull — a legit, refundable, owned asset [D] · anxiety — 'scam' (3 owned calls) + R-01 deposit dispute · habit — do nothing / keep cash [D]
- pain_layer: emotional · toleration_threshold: [D] acts only with a bounded, refundable first step · consequence_if_untreated: [D] never tries again; money stays idle
- alternatives_set[]: do nothing; ask a friend who sells online; cheaper DIY
- current_spend_hypothesis[]: £1,300 prior ([R-OWNED] T-08); $250 deposit (R-01)
- candidate_populations[]: CP-03
- counterevidence: R-01, R-05

### PB-04 · HYPOTHESIS
- name_buyer_words: 'busy e-commerce owners' (R-04 fragment) — no time to run listings, orders and ads every day
- name_market_or_clinical: operational time burden (order processing, stock, customer service, ads)
- entry_doors[]: MECHANISM-PLAUSIBLE
- review_mentions: 1 of 5 read (snippet) — R-04 · avg_star_of_mentioning_reviews: UNKNOWN (no stars in snippets)
- competitor_claim_count: 0 of 3 seeds checked (—) COMPETITOR-CLAIMED
- mechanism_plausibility_line: C7 daily management + C9 account manager take over operations.
- product_contribution_boundary: Runs operations; the owner still decides spend via the portal (C8) [R-OWNED T-04].
- struggling_moment: [D] parent with kids and travel (rep framing 'You have kids, you have a wife, family, uh, you travel most of the time' [R-OWNED T-10 rep]).
- four_forces: push — no daily hours [D] · pull — 'We run it' [R-TOOL] · anxiety — losing control of spend [D] · habit — evenings with family [D]
- pain_layer: functional / relationship · toleration_threshold: [D] when running it themselves would cost family time · consequence_if_untreated: [D] store neglected → no sales
- alternatives_set[]: VA / freelancer; automation apps; not starting
- current_spend_hypothesis[]: UNKNOWN — searched: none reachable
- candidate_populations[]: CP-04, CP-02
- counterevidence: NULL — searched: 5 snippet rows

### PB-02 · HYPOTHESIS
- name_buyer_words: 'It'd be nice to be earning and build something so that I can leave my full-time job eventually' / 'If I don't, I have to keep my job' [R-OWNED T-08]
- name_market_or_clinical: job dependence / no second income stream
- entry_doors[]: MECHANISM-PLAUSIBLE
- review_mentions: 0 of 5 read (snippet) — — · avg_star_of_mentioning_reviews: UNKNOWN (no stars in snippets)
- competitor_claim_count: 0 of 3 seeds checked (—) COMPETITOR-CLAIMED
- mechanism_plausibility_line: C7 ongoing management lets a store run beside a job; income itself is not guaranteed.
- product_contribution_boundary: Provides a managed store; cannot promise job-replacing income (contribution boundary = sales outcome).
- struggling_moment: [R-OWNED T-08] prospect weighing leaving a full-time job; trigger not stated — [D] Sunday-night dread / a pay freeze.
- four_forces: push — 'I have to keep my job' [R-OWNED] · pull — 'build something' of my own [R-OWNED] · anxiety — 'I don't want to get my job on the line here' [R-OWNED T-02] · habit — salary certainty [D]
- pain_layer: identity / future-fear · toleration_threshold: [D] when a side path looks bounded in cost and time · consequence_if_untreated: [D] stays tied to the job with no exit path
- alternatives_set[]: second job / gig work; trading / investing (T-10: 'lost money'); courses; keep the job
- current_spend_hypothesis[]: UNKNOWN — searched: owned calls mention £1,300 prior spend (T-08)
- candidate_populations[]: CP-01, CP-02, CP-07
- counterevidence: NULL — searched: 5 snippet rows

### PB-07 · HYPOTHESIS
- name_buyer_words: NULL — searched: no buyer-voice line; rep lines only: 'How about you can give this to your kids when they grow older' [R-OWNED T-10 rep] · 'bank deposits, it's a waste of capital and time' [R-OWNED T-08 rep]
- name_market_or_clinical: idle savings / building a transferable asset for family or retirement
- entry_doors[]: MECHANISM-PLAUSIBLE
- review_mentions: 0 of 5 read (snippet) — — · avg_star_of_mentioning_reviews: UNKNOWN (no stars in snippets)
- competitor_claim_count: 0 of 3 seeds checked (—) COMPETITOR-CLAIMED
- mechanism_plausibility_line: C11 ownership makes the store a transferable asset in principle.
- product_contribution_boundary: Asset value depends on sales; nothing guaranteed.
- struggling_moment: [D] savings in a bank account; trigger = a child's milestone or pension statement.
- four_forces: push — money earning little [R-OWNED rep] · pull — an asset for the kids [R-OWNED rep] · anxiety — losing savings [D] · habit — bank / property / stocks [R-OWNED T-08 rep]
- pain_layer: relationship / future-fear · toleration_threshold: UNKNOWN — searched: no buyer line · consequence_if_untreated: [D] savings stay idle; nothing to pass on
- alternatives_set[]: bank deposits; real estate; stock market (all named by rep, T-08)
- current_spend_hypothesis[]: UNKNOWN
- candidate_populations[]: CP-02, CP-06, CP-07
- counterevidence: NULL — searched: 5 snippet rows

**Counter:** PB 7 by label — VALIDATED 0 / SUPPORTED 3 / EARLY SIGNAL 0 / HYPOTHESIS 4; by door a 0 / b 3 / c 7.

## §6 · CANDIDATE POPULATIONS (CP-##)

distinct_speakers counts non-owned speakers only (VOC); owned speakers print separately and never raise a label (rule 4 + brief). Operator ICP (b) 'adults 50+ with money' as written is a demographic band → **REJECTED (category error: demographic ≠ population)**, reframed as CP-06 life-situation. Operator ICP (a) fathers → CP-02 (HYPOTHESIS).

| cp_id | pb_ids[] | situation (≤12w) | quote_ids[] | distinct_speakers (VOC) | owned speakers | sources[] | named_by_competitor | label |
|---|---|---|---|---|---|---|---|---|
| CP-01 | PB-01, PB-02 | has a full-time job, wants to leave it eventually | [R-OWNED] T-08, T-02 | 0 | 2 | [R-OWNED] | N | HYPOTHESIS |
| CP-02 | PB-02, PB-04, PB-07 | parent with kids ('I've got two children', 'I have four children') — maps operator ICP (a) fathers | [R-OWNED] T-04, T-09, T-10 | 0 | 3 | [R-OWNED]; OPERATOR HYPOTHESIS (a) | N | HYPOTHESIS |
| CP-03 | PB-03, PB-06 | tried e-commerce / trading before and lost money | R-01; [R-OWNED] T-03, T-08, T-10 | 1 | 3 | Trustpilot [R-SNIPPET]; [R-OWNED] | N | HYPOTHESIS |
| CP-04 | PB-04 | busy e-commerce owner | R-04 | 1 | 0 | DFY review pool [R-SNIPPET] | N | HYPOTHESIS |
| CP-05 | PB-01, PB-05, PB-06 | aspiring e-commerce entrepreneur who wants to skip the build | NW-SEED-02 claim; Readymerce PR title 'Aspiring E-Commerce Entrepreneurs' [R-SNIPPET] | 0 | 0 | competitor page [R-SNIPPET]; seller PR | Y — NW-SEED-02 | COMPETITOR-CLAIMED HYPOTHESIS |
| CP-06 | PB-07 | near/at retirement with savings earning little (reframe of operator ICP (b)) | [R-OWNED] T-10 rep line 'Is she going to be on pension too' | 0 | 0 | OPERATOR HYPOTHESIS (b); [R-OWNED] rep | N | HYPOTHESIS |
| CP-07 | PB-02, PB-07 | spouse who can't go back to work because of the kids | [R-OWNED] T-10 ('because of our kids, she can't do that') | 0 | 1 | [R-OWNED] | N | HYPOTHESIS |

**Counter:** CP 7 by label — HYPOTHESIS 6 / COMPETITOR-CLAIMED HYPOTHESIS 1. SINGLE-POPULATION RISK: PB-03, PB-05.

## §7 · LEAD-PROBLEM HYPOTHESIS + PROBLEM LANES

lead_problem_hypothesis: **PB-01** · runner_up: **PB-06** · confidence: **LOW**
reason: ranked in code by label → review_mentions → pain score → competitor claims. PB-01 is SUPPORTED (competitor door 2 of 3 + mechanism) and the only lane with review mentions (4 of 5, net-negative → counterevidence); pain 7/10. PB-06 carries the highest pre-harvest pain (9/10). LOW: no page fetched, snippet reviews only.

| pb_id | label | lane_search_terms[] (buyer pain words — problem, never product) |
|---|---|---|
| PB-01 | SUPPORTED | can't figure out shopify · don't know how to build an online store · shopify setup overwhelming · website builder too technical · store build taking forever · hands off store setup |
| PB-06 | SUPPORTED | shopify store no sales · tried dropshipping lost money · spent money on ads no sales · never made a sale online · store gets no traffic |
| PB-05 | SUPPORTED | don't know what to sell online · can't find a winning product · what product should I sell · picked the wrong product · no idea what niche |

lanes 3 ⇒ **MULTI-PROBLEM: STRONG**. HYPOTHESIS PBs (not lanes; keys kept for 04–06): PB-02: want to quit my job, need extra income besides my job, stuck in 9 to 5 · PB-03: is it a scam, lost money on ecommerce course, scammed by online business program · PB-04: no time to run a side business, too busy with kids to start a business · PB-07: savings earning nothing, something to leave my kids, pension not enough

## §8 · SEARCH-KEY SET + SWAP TABLE v0

- product_noun_terms[]: done for you ecommerce store · done for you shopify store · done for you etsy store · dropshipping business in a box · turnkey online store
- problem_terms[PB-01]: can't figure out shopify · don't know how to build an online store · shopify setup overwhelming · website builder too technical · store build taking forever · hands off store setup
- problem_terms[PB-06]: shopify store no sales · tried dropshipping lost money · spent money on ads no sales · never made a sale online · store gets no traffic
- problem_terms[PB-05]: don't know what to sell online · can't find a winning product · what product should I sell · picked the wrong product · no idea what niche
- symptom_terms[]: no sales · no traffic · stuck on setup · lost money · wasted weekends · scam · want to quit my job
- competitor_domains[]: ecomdoneforyou.com, ecommerceparadise.com, ecomxpertz.com (+ RESERVE: doneforyoustrategy.com, nn-dfysuccess.com)
- slang[]: winning product · dropshipping · side hustle · 9 to 5 · passive income · guru

| plain | clinical / market | source |
|---|---|---|
| 'hands off' store | managed / done-for-you service | R-05 |
| tried e-commerce, lost money | failed prior DIY attempt / sunk cost | [R-OWNED] T-08 |
| scam | vendor trust deficit / refund-chargeback risk | [R-OWNED] T-04, T-08; R-01 |
| winning product | validated product-market fit | [R-OWNED] T-06 |
| leave my full-time job | income replacement | [R-OWNED] T-08 |
| store with no sales | zero traffic / zero conversion | NW-SEED-02 snippet |
| something to give my kids | transferable digital asset | [R-OWNED] T-10 rep |
| We run it | ongoing store operations management | PDP [R-TOOL] Meta |

## §9 · SURFACE DESIRE CANDIDATES (SD-##) — all HYPOTHESIS

| sd_id | statement | pb_ids[] | quote_id / competitor_ref |
|---|---|---|---|
| SD-01 | I want to build something so I can leave my full-time job eventually | PB-02 | [R-OWNED] T-08 |
| SD-02 | I want my store built start-to-finish, hands off | PB-01 | R-05; NW-SEED-02 |
| SD-03 | I want to own it while someone else runs it | PB-04 | PDP/Meta 'We build it. We run it. You own it.' |
| SD-04 | I want to see exactly what my $500 gets me before I trust anyone again | PB-03 | [R-OWNED] T-01 |
| SD-05 | I want something I can give my kids when they grow older | PB-07 | [R-OWNED] T-10 rep line |

## §10 · PAIN SCORE (pre-harvest)

| pb_id | URGENCY | FREQUENCY | SPEND HISTORY | CONSEQUENCE | REORDER | total |
|---|---|---|---|---|---|---|
| PB-01 | 1 — [D] can be postponed indefinitely | 1 — [D] friction recurs each attempt | 2 — $100+ repeatedly: $250 deposit R-01; £1,300 + '10 grand' quote [R-OWNED T-08] | 1 — [D] idea never launches | 2 — solving it creates the next need: credits/top-ups, upgrades 'they keep upgrading' [R-OWNED T-06] | **7/10 PRE-HARVEST** |
| PB-06 | 2 — [D] money already sunk; ads/subscriptions leak | 1 — [D] checked daily while live | 2 — £1,300 prior [R-OWNED T-08] | 2 — [D] sunk cost + gives up on e-commerce | 2 — marketing credits recur [R-OWNED T-04/T-06] | **9/10 PRE-HARVEST** |
| PB-05 | 1 — [D] | 1 — [D] each launch | 1 — [D] $20–100 tools/lists | 1 — [D] dud product | 1 — occasional: new products added [R-OWNED T-06] | **5/10 PRE-HARVEST** |

Test: *If he never buys this,* the store idea stays a half-built theme and the savings stay idle — and the earlier loss stays the last word on e-commerce `[D]`.
counterevidence: R-01, R-05 (delivery / handover complaints on build services, one on Readymerce itself). DEEP re-scores; 06 re-prints.

## §11 · QUALITY FLAGS

| flag | value | evidence |
|---|---|---|
| information_scarcity | Y | PDP, Trustpilot, BBB and competitor pages all unfetchable this run (egress/credit limits); 1 Trustpilot review exists for readymerce.com |
| walmart_generic | Y [D] | cheaper substitutes exist: DIY Shopify/Etsy, Fiverr builds, pre-built '$20 Shopify store' named on a call [R-OWNED T-07] |
| real_brand_competitor_present | Y | 3 seeds + 4 reserve DFY-ecom services with Trustpilot/BBB/reviews.io pages [R-SNIPPET] |
| reorder_path | kit + consumable | one-time build, then credit top-ups, marketing packages and tier upgrades [R-OWNED T-04, T-06] |
| margin_note | UNKNOWN | price $500 / $2,000 ÷ unit cost UNKNOWN (offshore build labour per R-01 reviewer; ad credits pass-through [D]); reference 2.5–3×, ≥70% GM |

**Context for 09/12 (operator problem, not VOC):** rep line 'most of the people get this package ... they just say oh okay i don't know if this is really going to work' [R-OWNED T-06] — the $500 entry tier is sold as a trial, which is consistent with the operator's 'tire kickers' complaint `[D]`.

## §12 · COVERAGE STATEMENT (SEED)

Tools used: WebSearch ×3, Meta ads_library_search ×2 (free), GetHookd get_user_profile ×1 + list_shops ×2 (0.6 cr: 291.22 → 290.62 — **0.1 cr over the ≤0.5 cap**, limit:5 sweep), WebFetch ×5 (all EGRESS_BLOCKED), Firecrawl ×4 (no credits), Apify rag-web-browser ×5 (hard limit; $0 spent). Apify $0.00.

COVERAGE (SEED): pdp https://readymerce.com (NOT FETCHED — BLOCKED-ON-TOOL: WebFetch egress-blocked, Firecrawl no credits, Apify monthly hard limit; identity from [R-SNIPPET] + Meta [R-TOOL] + [R-OWNED]); reviews reachable 5 [R-SNIPPET] (1 exact-SKU / 4 category-proxy), read in full 0 (Amazon: REVIEWS: NONE REACHABLE — DEEP fills); seeds 3 (0 of 3 PDPs fetched); components 11 (given 0 / INFERRED 11); PB 7 by label (VALIDATED 0 / SUPPORTED 3 / EARLY SIGNAL 0 / HYPOTHESIS 4); CP 7; lanes 3; NOT MAPPED: PDP text + images, competitor price ladders, verbatim review text, star ratings, unit cost; competitor claims and supplier specs keep their basis, never read as buyer experience; CONFIDENCE: lead problem LOW because no page could be fetched and door (a) is snippet-only (net-negative for PB-01).

## §TRUTH CARD

agent_id: 01-DEEP · wave W1 · started 2026-09-24T20:36:39Z · box: 25 min / 80 tool calls · model: sonnet
LOCK CARD: writer = agent 01-DEEP. This section is APPENDED after SEED §1–§12 (never edited). One writer for §TRUTH CARD.
Degraded-review-source run per TOOL CARD ADDENDUM: Apify (Amazon/Trustpilot scrapers) BLOCKED-ON-TOOL — every planned actor run printed as `NOT RUN — Apify monthly limit` below with its exact recipe. Review universe = Exa-opened pages (readymerce.com/results + testimonial pages, BBB, ScamAdviser, trustedrevie.ws, Sitejabber, ProductReview, competitor reuse) + YouTube transcripts (TranscriptAPI) + WebSearch snippets. Owned sales-call transcripts NOT read here (not reviews).

### NOT RUN — Apify monthly limit (planned recipes, per STEP-01.md §2/D2)

| planned actor | exact recipe | reason |
|---|---|---|
| jdtpnjtp/amazon-reviews ×3 (critical/five_star/three_star) | N/A — no Amazon ASIN exists for this service (no physical SKU); would have run against the closest proxy listing if one existed | NOT RUN — Apify monthly limit; also N/A: no ASIN (service product) |
| memo23/trustpilot-scraper-ppe (readymerce.com) | `{startUrls:["https://www.trustpilot.com/review/readymerce.com"], maxItems:100, filterLanguages:["en"], sampling:"balanced", sortBy:"recent", filterDateRange:"last12months", expandRegionalDomains:false, scrapeAllReviews:false, includeStats:true, reviewInsights:true}` | NOT RUN — Apify monthly limit |
| memo23/trustpilot-scraper-ppe (ecomdoneforyou.com) | `{startUrls:["https://www.trustpilot.com/review/ecomdoneforyou.com"], maxItems:100, filterLanguages:["en"], sampling:"balanced", sortBy:"recent", filterDateRange:"last12months", expandRegionalDomains:false, scrapeAllReviews:false, includeStats:true, reviewInsights:true}` | NOT RUN — Apify monthly limit |
| memo23/trustpilot-scraper-ppe (ecommerceparadise.com) | `{startUrls:["https://www.trustpilot.com/review/ecommerceparadise.com"], maxItems:100, ...same params} ` | NOT RUN — Apify monthly limit |
| memo23/trustpilot-scraper-ppe (ecomxpertz.com, ca.trustpilot.com) | `{startUrls:["https://ca.trustpilot.com/review/ecomxpertz.com"], maxItems:100, ...same params}` | NOT RUN — Apify monthly limit |
| automation-lab/trustpilot (fallback chain, all 4 domains) | `{companyUrls:["<domain>"], maxReviewsPerCompany:100, stars:["1","2","3","5"], languages:["en"], sort:"recency", date:"last12months"}` | NOT RUN — Apify monthly limit (chain step 2) |
| website-content-crawler (Trustpilot page crawl fallback, all 4 domains) | `{startUrls:[{url:"https://www.trustpilot.com/review/<domain>?stars=3&sort=recency&page=N"}], crawlerType:"cheerio", maxCrawlDepth:0}` | NOT RUN — Apify monthly limit (chain step 3) |
| apify/rag-web-browser (readymerce.com/results, BBB, ScamAdviser etc.) | `{query:"<url>", outputFormats:["markdown"], scrapingTool:"raw-http"}` | NOT RUN — Apify monthly limit; substituted with Exa agent per TOOL CARD ADDENDUM |


### T1 · SAMPLE + SOURCES

Degraded-review-source run (TOOL CARD ADDENDUM): no Amazon listing exists (service, no ASIN); Trustpilot pages are BLOCKED-ON-TOOL for direct fetch by any connected tool (confirmed again this run — not re-sent to Exa; SEED's R-01 WebSearch-summary route is the only channel that ever worked for readymerce.com's Trustpilot page, reused by reference, not re-fetched). Review universe = Exa-opened pages + TranscriptAPI YouTube transcripts + WebSearch discovery, per the binding addendum.

| source | url | type | retrieved | target | read | star mix | ≤12mo n | tier |
|---|---|---|---|---|---|---|---|---|
| readymerce.com PDP family (9 distinct pages) | readymerce.com/, /how-it-works, /results, /pricing, /refund-policy, /terms-of-service, /risk-disclaimer, /what-you-get, /knowledge | SELLER PDP / policy text | 9 pages | all reachable PDP pages | 9 of 9 read in full | N/A (not reviews) | N/A | [R-PAGE via Exa] |
| readymerce.com 404 paths | /testimonials, /case-studies, /reviews, /guarantee, /terms | SELLER (attempted, absent) | 0 of 5 | 5 | 0 | N/A | N/A | NOT RETRIEVABLE (404) |
| BBB (bbb.org) | bbb.org/search?find_text=Readymerce | 3rd-party accreditation/complaints | 1 search page | 1 profile | 0 (no profile exists) | N/A | N/A | [R-PAGE via Exa] |
| ScamAdviser | scamadviser.com/check-website/readymerce.com | 3rd-party trust-check tool | 1 | 1 | 1 (trust score + 3 risk factors; 0 user comments shown) | N/A | N/A | [R-PAGE via Exa] |
| ScamDoc | scamdoc.com/view/2555589 | 3rd-party trust-check tool | 1 | 1 | 1 (trust score 25% + 3 risk factors; 6 comments shown but NOT attributable to Readymerce — generic sitewide feed incl. Dutch-language and crypto-product text, explicitly excluded per rule 2) | N/A | N/A | [R-PAGE via Exa] |
| trustedrevie.ws | trustedrevie.ws/reviews/readymerce.com | 3rd-party review aggregator | 1 | 1 | 0 — page states verbatim "There are currently no reviews for this company" | N/A | N/A | [R-PAGE via Exa] |
| Sitejabber | sitejabber.com/reviews/readymerce.com | 3rd-party review site | 1 | 1 | 0 — page states "Readymerce Reviews 0 · 0 reviews · Be the first to write a review" | N/A | N/A | [R-PAGE via Exa] |
| ProductReview.com.au | productreview.com.au/search?query=readymerce | 3rd-party review site | 1 (search page) | 1 listing | 0 — no Readymerce listing exists | N/A | N/A | [R-PAGE via Exa] |
| Trustpilot (readymerce.com) | uk.trustpilot.com/review/readymerce.com | 3rd-party review site | BLOCKED-ON-TOOL (not re-attempted) | 1 | 0 direct (1 snippet-summary already on file as SEED R-01) | UNKNOWN (snippet only) | UNKNOWN | reused SEED [R-SNIPPET] |
| Broad discovery (Reddit / Warrior Forum / Quora / general web) | 14 distinct URLs opened (award sites, press releases, syndicated blog posts, LinkedIn) | mixed — all turned out SELLER-CURATED / PR / employee-profile | 14 | — | 14 | N/A | mostly 2026 | [R-PAGE via Exa] |
| YouTube — "Readymerce" direct search | search_youtube q="Readymerce review" | video search | 5 results (1st page) | — | 0 third-party Readymerce reviews found (only the brand's own channel video, 322 views, SELLER-CURATED) | N/A | N/A | [R-TOOL TranscriptAPI] |
| YouTube — "done for you shopify store" category search | search_youtube q="done for you shopify store service review scam" | video search | 20 results (1st page) | — | 2 transcripts pulled (proxy-SKU analyst reviews of Krafted Labs and EcomSites.io, NOT Readymerce) | N/A | both 2026 | [R-PAGE via TranscriptAPI] |
| ecommerceparadise.com own reviews page (REUSED, not re-fetched) | shop.ecommerceparadise.com/pages/reviews | competitor's own testimonials | reused from 02-partials/02-COMPETITOR-INTEL.NW-SEED-02.md §15 (LK-01..LK-03) | — | 3 quotes reused by reference | N/A | N/A | [R-PAGE via Exa] (02's read, cited not duplicated) |

**SAMPLE (N=0 independent exact-SKU buyer reviews read in full)** — every Google-indexed review-style venue checked (BBB, ScamAdviser, ScamDoc, trustedrevie.ws, Sitejabber, ProductReview, Reddit/Warrior Forum/Quora broad search) returned either "no profile / no reviews" or non-attributable content; Trustpilot (the one venue known to carry a Readymerce review, per SEED R-01) stayed BLOCKED-ON-TOOL. 10 SELLER-CURATED verbatim quote units were read in full (3 on-site testimonials with an actor-portrayal disclosure + 7 earned-media/press self-quotes), plus 9 PDP/policy pages read in full (EXACT PRODUCT MATERIAL), plus 2 SIMILAR-PRODUCT-CONTEXT YouTube analyst transcripts (proxy category, not Readymerce).

**Truth-card band: PROXY-SKU** (<10 exact-SKU independent buyer reviews read in full = 0). Every PT-## below is stamped by its true evidence_type (EXACT PRODUCT MATERIAL for fetched PDP/policy text, SELLER EXPLANATION for testimonials/press quotes, SIMILAR PRODUCT CONTEXT for the 2 YouTube proxy transcripts) rather than blanket-stamped, because most of this card's content is EXACT PRODUCT MATERIAL (the PDP itself, fetched for the first time this run via Exa after SEED's WebFetch/Firecrawl/Apify chain was BLOCKED-ON-TOOL) rather than proxy-SKU reviews — the band token still reads PROXY-SKU per the rule's strict buyer-review count, but the reader should note the PDP itself is now directly sourced, which SEED could not do.

**3★ available: 0 of 0** — no star-rated review was retrievable anywhere this run.


### T2 · CODED ROWS R-## + FREQUENCY TABLE

SEED already coded R-01..R-05 (§4, snippet-tier, kept as-is, never edited). DEEP adds R-06..R-17 below (R-14/R-15 numbers reserved-and-skipped: the ScamAdviser/ScamDoc tool outputs are logged as facts F-14/F-15 in T5, not as R-## rows, because they are automated trust-score tool output, not review/testimonial text, and coding them as "R-##" would blur the evidence-type distinction the card exists to preserve).

| r_id | source | url | date | stars | verified | text (verbatim ≤60w) | outcome_named[] | problem_named[] | population_marker | complaint[] | duration_of_effect | usage_cadence | media | length_words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-06 | readymerce.com/how-it-works testimonial | https://readymerce.com/how-it-works | UNKNOWN | N/A | N — page discloses "some testimonials feature actors portraying verified experiences" | "They built it, they run it, and I get a monthly report. That's exactly what I was looking for." | monthly reporting delivered | PB-01, PB-04 | none named | NULL — searched | NULL — searched | NULL — searched | 0 | 19 |
| R-07 | readymerce.com/how-it-works testimonial | https://readymerce.com/how-it-works | UNKNOWN | N/A | N (same disclosure) | "I work full-time. The scale phase means I never touch the day-to-day — it's the cleanest second income stream I've found." | second income stream (self-described, no $ figure) | PB-02, PB-04 | full-time employee | NULL — searched | NULL — searched | "scale phase" implies post-launch ongoing | 0 | 21 |
| R-08 | readymerce.com/how-it-works testimonial | https://readymerce.com/how-it-works | UNKNOWN | N/A | N (same disclosure) | "Buying an existing store was absurdly priced. A custom build at a fraction of the cost was the obvious move." | chose custom build over buying an existing store | PB-01, PB-05 | prior store-buyer / shopper | price of pre-built stores ("absurdly priced") | NULL — searched | NULL — searched | 0 | 20 |
| R-09 | bestofbestreview.com award page | https://bestofbestreview.com/awards/readymerce-best-done-for-you-e-commerce-store-service-in-the-uk-of-2026 | March 25, 2026 | N/A | N — spokesperson in earned-media award piece | "Most people spend too much energy on setup instead of selling. Readymerce helps clients focus on the part that drives their business forward." | none | PB-01 | none | NULL | NULL | NULL | 0 | 23 |
| R-10 | bestofbestreview.com award page | https://bestofbestreview.com/awards/readymerce-best-done-for-you-e-commerce-store-service-in-the-uk-of-2026 | March 25, 2026 | N/A | N | "We don't sell dreams. We help clients start their stores with the tools and information they need." | none | PB-03 | none | NULL | NULL | NULL | 0 | 17 |
| R-11 | evergreenawards.com award page (award-body paraphrase, NOT verbatim buyer text) | https://evergreenawards.com/awards/readymerce-best-etsy-shopify-store-setup-service-in-the-united-states-of-2025 | UNKNOWN | N/A | N — unnamed client, paraphrased by the award body, not a direct quote | "One client reported that their Etsy store generated $39,000 in nine months entirely through organic traffic, without any paid advertising." | $39,000 / 9 months, organic-only | PB-06 | unnamed single client | NULL | 9 months (stated) | organic-only (no paid ads) | 0 | 20 |
| R-12 | lifestyle.utv.ie earned-media article | https://lifestyle.utv.ie/story/534022/inside-the-business-model-that-is-replacing-traditional-e-commerce-courses/ | UNKNOWN | N/A | N — company quote in a sponsored/earned article | "Readymerce is one of the companies leading this shift...the company builds the store for them — complete with product research, supplier partnerships, conversion-optimized design, and a tailored go-to-market strategy." | none | PB-01 | none | NULL | NULL | NULL | 0 | 27 |
| R-13 | financialcontent.com press release | https://www.financialcontent.com/article/getnews-2026-3-9-readymerce-emerges-as-the-go-to-solution-for-aspiring-e-commerce-entrepreneurs | March 9, 2026 | N/A | N — company self-quote in a wire press release | "We don't just hand people a store and wish them luck. We deliver a business-in-a-box that is designed to convert from the moment it goes live. Our clients skip the painful learning phase and go straight to execution." | "designed to convert from the moment it goes live" (unverified claim) | PB-01 | none | NULL | NULL | NULL | 0 | 38 |
| R-16 | YouTube analyst review of a DIFFERENT done-for-you Shopify seller (Krafted Labs / Ecom Sites.design) — SIMILAR PRODUCT CONTEXT, NOT Readymerce | https://www.youtube.com/watch?v=xWS-4VHqkcM | ~2026-09 (8 days before run) | N/A | N — 3rd-party reviewer commentary, not a buyer | "The current Crafted Labs Trustpilot profile is still very small, but all of the reviews showing right now are negative. Complaints around extra costs, add-ons, and stores not matching the expectation created by the marketing." | none | PB-01, PB-06, PB-03 | none | extra costs; add-ons; unmet expectations | NULL | NULL | video | 35 |
| R-17 | YouTube analyst review of a DIFFERENT done-for-you Shopify seller (EcomSites.io) — SIMILAR PRODUCT CONTEXT, NOT Readymerce | https://www.youtube.com/watch?v=6t3Nl8JMuvM | ~2026-07/08 | N/A | N — 3rd-party reviewer commentary, not a buyer | "Receiving a finished store doesn't eliminate the need to attract customers, market your products, provide customer support, or continue improving the business. The service removes part of the setup process, but it doesn't remove the ongoing work." | none | PB-01, PB-06 | none | ongoing-work burden not removed by the build | NULL | "ongoing" (post-delivery) | video | 37 |

**Frequency table (code-computed over all 15 R-## rows on file, SEED R-01..R-05 + DEEP R-06..R-13,R-16,R-17; python3, see `/tmp/.../scratchpad/freq.py`):**

| rank | pb_id | matches (n of N=15) | distinct sources | note |
|---|---|---|---|---|
| 1 | PB-01 | 11 of 15 | 8 | dominant across every venue — PDP self-description, testimonials, press, and the 2 proxy YouTube reviews all name the setup/build burden |
| 2 | PB-03 | 4 of 15 | 4 | 1 SEED buyer-voice (R-01, negative) + 1 SELLER EXPLANATION rebuttal (R-10 "we don't sell dreams") + 1 proxy YouTube (R-16, trust-pattern in category) |
| 3 | PB-04 | 3 of 15 | 2 | thin; still no independent buyer voice beyond SEED's single R-04 |
| 3 | PB-06 | 3 of 15 | 3 | 1 award-body paraphrase (R-11, positive, unverified $ claim) + 1 proxy YouTube (R-16) + 1 proxy YouTube (R-17) |
| 5 | PB-02 | 1 of 15 | 1 | unchanged from SEED |
| 5 | PB-05 | 1 of 15 | 1 | unchanged from SEED (R-08 adds a 2nd mention but was already counted — see script) |

**Counter:** read 12 new units this DEEP pass (9 PDP pages EXACT PRODUCT MATERIAL + 10 SELLER-CURATED quotes read across those pages/press, counted separately from page-count; 2 SIMILAR-PRODUCT-CONTEXT YouTube transcripts) of 12 retrieved (0 chain-exhausted after retrieval — every retrieved unit was read); independent exact-SKU buyer reviews: 0 of 0 retrievable (every review-site chain ended in "no reviews" or BLOCKED-ON-TOOL); 3★ 0 of 0; hyper-responsive (longest 20%): N/A — sample too small (bottom-line R-13 at 38 words is the longest DEEP unit); ≤12mo: 8 of 10 dated DEEP units are 2026-dated (2 undated).


### T3 · PRODUCT TRUTH CARD (PT-##)

Every section printed; `NULL — searched:` where empty. Band PROXY-SKU (T1) — statements sourced to fetched PDP/policy text are EXACT PRODUCT MATERIAL (strength follows rule 6.2: EXACT PRODUCT MATERIAL alone = WELL SUPPORTED), statements sourced to testimonials/press are SELLER EXPLANATION, statements sourced to the 2 YouTube proxy transcripts are SIMILAR PRODUCT CONTEXT and are explicitly flagged as category-typical, not Readymerce-specific.

**Form / materials / specs**
- PT-01 · Readymerce's entry offer is a named, priced package: "The Store Build & Research Package," $500 one-time. `evidence_type: EXACT PRODUCT MATERIAL · strength: WELL SUPPORTED · support_count: 2 of 9 PDP pages read (pricing, terms-of-service) · quote_ids: [] (page fact, not a review quote) · contradicts_seller: N` — source readymerce.com/pricing, /terms-of-service [R-PAGE via Exa].
- PT-02 · Above the $500 package, Readymerce publishes no fixed second tier or price; the /pricing page states the managed-service fee "is quoted for the specific category and scope on the fit call... no single number is published." This narrows SEED §2's INFERRED "$2,000 full launch" figure (sourced there only to [R-OWNED] sales-call transcripts) to a sales-call-quoted, not PDP-published, number. `evidence_type: EXACT PRODUCT MATERIAL · strength: WELL SUPPORTED · support_count: 1 of 9 · contradicts_seller: N (refines SEED, does not contradict it — SEED already marked the $2,000 figure INFERRED, not given)`.

**What buyers say it IS**
- PT-03 · No independent buyer description of what the product IS was retrievable this run (0 exact-SKU reviews). The only buyer-voice text on file anywhere is SEED's R-01 (Trustpilot, snippet-summary, negative — cited by ID, not re-read) describing a $250-deposit Shopify/Etsy build. `NULL — searched: CUSTOMER EXPERIENCE`.

**What it DOES**
- PT-04 · The $500 package includes: niche/demand/competition research, platform choice (Shopify or Etsy) agreed on a "fit call," store build + branding (logo, banner, structure), product listings (titles/tags/descriptions/images/variants), shipping-profile setup, a staged (not single-drop) product release, controlled ad testing at buyer-approved budgets, an early performance review, and post-launch corrections/ongoing listing optimisation with the management level "agreed on the fit call." `evidence_type: EXACT PRODUCT MATERIAL · strength: WELL SUPPORTED · support_count: 1 of 9 (readymerce.com/what-you-get, 26 verbatim bullet points) · contradicts_seller: N` [R-PAGE via Exa].
- PT-05 · Explicitly excluded from the package: product costs, platform fees (e.g. Shopify subscription) and ad spend; any income/sales/profitability guarantee; and "a course, a template pack, or a second product line." `EXACT PRODUCT MATERIAL · WELL SUPPORTED · support_count: 1 of 9 · contradicts_seller: N` [R-PAGE via Exa, readymerce.com/what-you-get].

**Duration of effect**
- PT-06 · NULL — searched: no independent buyer text describing time-to-first-sale, time-to-profit, or any outcome timeline was retrievable. The one number on file (R-11, "$39,000 in nine months") is an award-body paraphrase of an unnamed client, not verbatim buyer text, and is not corroborated. `evidence_type: SELLER EXPLANATION (unverifiable) · strength: UNKNOWN`.

**What it VISIBLY demonstrates**
- PT-07 · The dedicated page built to show this — readymerce.com/results, headlined "Straight From Our Stores. Unfiltered." with "Client Testimonials" / "Hear From Our Clients" section headings — rendered with those headings but NO testimonial/case-study cards under them when Exa opened it; /testimonials, /case-studies and /reviews all return 404. `evidence_type: SELLER EXPLANATION · strength: TENTATIVE (page may be JS-rendered content Exa's crawler could not execute — NOT claimed as proof of an empty page, only as NOT RETRIEVABLE content) · contradicts_seller: borderline — a page titled "Unfiltered" that shows nothing is at minimum a coverage gap, logged for 12/13's claims router`.

**Usage cadence**
- PT-08 · Ongoing cadence per the PDP: "staged product release rather than one large drop," "ad monitoring and adjustments, plus regular reporting," "ongoing listing optimisation and new product rollout," with "the level of ongoing management... agreed on the fit call" (i.e., not fixed/standard across buyers). `EXACT PRODUCT MATERIAL · WELL SUPPORTED · support_count: 1 of 9 · contradicts_seller: N`.

**Delayed-results signal**
- PT-09 · NULL — searched: no buyer-corroborated delayed-results pattern retrievable. SELLER EXPLANATION only: "Examples are gross revenue, not profit. Results are not typical and are not guaranteed" (readymerce.com/how-it-works) [R-PAGE via Exa].

**Top 3 complaints with counts**
- PT-10 · Exact-SKU: 1 of 1 available (SEED R-01, not re-read): withheld store access codes/theme after a $250 deposit; company reply disputes the framing. Count: 1 of 0 independent DEEP-read reviews (none retrievable). Category-typical (SIMILAR PRODUCT CONTEXT, 2 of 2 proxy YouTube units, NOT Readymerce-specific): "extra costs, add-ons, and stores not matching the expectation created by the marketing" (R-16); "doesn't eliminate the need to attract customers, market products, provide customer support" (R-17); incomplete/missing deliverables at handover (R-16, of a different seller's older complaints). `evidence_type: mixed (CUSTOMER EXPERIENCE for R-01 exact-SKU; SIMILAR PRODUCT CONTEXT, basis: category-typical, for R-16/R-17) · strength: TENTATIVE`.

**3★ nuance**
- PT-11 · NULL — searched: 0 of 0 star-rated reviews retrievable anywhere this run.

**Irritation / side-effect reports verbatim with counts**
- PT-12 · NULL — searched: 0 verbatim buyer irritation/complaint quotes beyond SEED's already-filed R-01 (not re-read, not re-counted here).

**Follow-up-review signal**
- PT-13 · NULL — searched.

**Packaging**
- PT-14 · The deliverable is the buyer's own live Shopify or Etsy store account, explicitly positioned as "not a course, a template pack" — a one-off managed-service delivery, not a digital product/download. `EXACT PRODUCT MATERIAL · WELL SUPPORTED · support_count: 1 of 9 · contradicts_seller: N`.

**Limitations**
- PT-15 · The 7-day money-back guarantee is materially narrower than SEED's C10 phrasing ("7-day 100% money-back guarantee") suggests: it voids immediately — even inside the 7-day window — the moment the buyer (a) approves/accepts delivery, (b) purchases ANY additional service, add-on, upsell or upgrade, or (c) requests or commits to further work; it covers the $500 build fee only, never platform fees, ad spend, domain costs, apps or supplier costs. `EXACT PRODUCT MATERIAL · WELL SUPPORTED · support_count: 2 of 9 (refund-policy, terms-of-service, word-for-word matching text) · contradicts_seller: N (this IS the seller's own text; it refines, not contradicts, SEED's INFERRED summary)` [R-PAGE via Exa].
- PT-16 · Two independent, non-buyer trust-check tools score the domain low: ScamAdviser trust score 0/100 (flags: WHOIS identity hidden via a paid privacy service, low visitor traffic, domain "only recently registered"); ScamDoc trust score 25% "Poor" (flags: domain created 2026-02-26 — under 7 months old at check time — plus a country-association heuristic; HTTPS present). Both are automated heuristic tools, not buyer evidence, and are logged as F-14/F-15 (T5), not as PT-## buyer statements — included here only as a limitation/context note for 12/13's claims router and for T7's PB-03 discussion. `basis: cited (tool output) · NOT a buyer-voice finding`.

**Corroborated supplier claims**
- PT-17 · NULL — searched: SEED's R-01 reviewer claim ("workers from the Philippines") is uncorroborated by any DEEP source; Readymerce's own fetched pages do not name a build-team location.

**Customer media IDs**
- PT-18 · NULL — searched: 0 customer photo/video IDs found anywhere; the page built to show them (readymerce.com/results) rendered with no cards (PT-07).

**Unknowns**
- PT-19 · UNKNOWN — searched: whether the client portal (SEED's C8: balances/credits/top-ups/monthly trend report) and a named dedicated account manager (SEED's C9) actually exist as described — neither term appears on any of the 9 DEEP-read PDP pages; both remain sourced only to SEED's [R-OWNED] sales-call transcripts (not re-read here per brief). UNKNOWN — searched: exact number of "vetted products" listed per store (SEED said "3," the DEEP-read what-you-get page describes the process but gives no fixed count).

**Translated N**
- PT-20 · 0 — no non-English review content was encountered and counted this run (ScamDoc showed 2 Dutch-language comments in a generic sitewide feed explicitly excluded as unattributable to Readymerce per rule 2 — not translated or counted as a Readymerce review).

**CONTRADICTS the seller — every instance listed verbatim:**
- **YES** — Income-guarantee disclaimers vs. sales-rep income claims. PDP (5 of 9 pages, near-identical wording): "We make no income guarantees" (readymerce.com/pricing); "ReadyMerce does not guarantee profit, revenue, sales, product success, margin, account approval, account longevity, return on investment, recovery of the Program Price, or business success" (readymerce.com/risk-disclaimer); "Examples are gross revenue, not profit. Results are not typical and are not guaranteed" (readymerce.com/how-it-works); "—Any income, sales or profitability guarantee" listed under What Is NOT Included (readymerce.com/what-you-get); "We make no income guarantees. Results vary... Past performance does not predict future results" (readymerce.com/terms-of-service) — all `[R-PAGE via Exa]`, EXACT PRODUCT MATERIAL — **directly contradicted by seller's own sales-call reps** per 01-PRODUCT-TRUTH.md §2's already-filed seller-internal-contradiction note: "91 percent of our clients have a success rate within the first two to three weeks" and "our goal is to get you making 10k a month" [R-OWNED T-04, cited by ID, not re-read]; "a successful store... might make like $5,000 in three months" [R-OWNED T-05, cited by ID, not re-read]. This is the single clearest seller self-contradiction on file — the written PDP disclaims income results across 5 separate pages while the phone sales process states specific income figures.
- **YES** — Testimonial authenticity disclosure. readymerce.com/how-it-works headlines its quote section "Client Testimonials" / "Hear From Our Clients," then discloses in the same page's fine print that "for client confidentiality, some testimonials feature actors portraying verified experiences" — meaning the 3 named quotes on file (R-06/R-07/R-08) cannot be established as spoken by real named buyers from the page alone. `[R-PAGE via Exa]`.
- **NO** — SEED's C10 line "refund → Readymerce keeps the store" ([R-OWNED]-sourced, marked INFERRED there): the fetched refund-policy/terms-of-service text (PT-15) says nothing about Readymerce retaining the store on refund; this is not a contradiction (SEED never asserted it as a fact, only INFERRED from a sales call) but DEEP could not corroborate it either — logged UNVERIFIED-BY-DEEP.


### T4 · FOUR-LAYER SHEET

| layer | entry | source | advertised_by_competitors |
|---|---|---|---|
| physical | A live Shopify or Etsy store account, in the buyer's own name, with branding (logo/banner/structure) and a listed product catalogue | PT-04, F-01, F-02 | Y — all 3 seeds sell a store build (NW-SEED-01 "fully automated e-commerce store," NW-SEED-02 "fully built Shopify store," NW-SEED-03 same-shape service) |
| functional (what it does) | Researches a niche/product direction, builds and lists the store, runs a staged launch with buyer-approved ad tests, then keeps optimising listings and ads on an ongoing, per-client-scoped basis | PT-04, PT-08, F-03..F-07 | Y — same function claimed by all 3 seeds (product research + build + marketing) |
| mechanism (how it delivers) | Everything is scoped on a single "fit call" per client rather than published as fixed tiers; guarantee is a fast-voiding 7-day cash refund on the $500 fee only | PT-01, PT-02, PT-15, F-10, F-12 | PARTIAL — NW-SEED-02 publishes explicit fixed tiers ($9,997/$14,997/$19,997) and a milestone-rebuild guarantee (Y, different mechanism); NW-SEED-03 publishes explicit profit-share percentages (Y, different mechanism); NW-SEED-01 publishes a conditional 6-month "ROI guarantee" (Y). None of the 3 seeds share Readymerce's un-published, fit-call-scoped ongoing-fee shape (N for that specific trait) |
| hidden / unadvertised | (1) Testimonials carry an actor-portrayal disclosure; (2) the "Unfiltered" results/case-study page renders with headings but no content; (3) two independent trust-check tools score the domain 0/100 and 25/100 "Poor," partly on a <7-month-old domain-registration flag; (4) the refund guarantee voids the instant ANY add-on/upgrade is purchased, which functions as a built-in upsell-timing incentive | PT-07, PT-15, PT-16 (T5 F-14/F-15) | N — none of these are things any seller in this category advertises |

**Three discovery answers:**
- *What does it do that is not advertised?* NULL — searched: no clearly non-advertised functional capability surfaced in the 9 PDP pages read; the fit-call-scoped, per-client cadence is disclosed (if vaguely), not hidden.
- *What components do competitors not include?* Readymerce does not publish a fixed price ladder above its $500 entry fee (ongoing management is quoted per-client on the fit call) — unlike NW-SEED-02's published $9,997–$19,997 tiers or NW-SEED-03's published 70/30–100/0 profit-share bands (see T6 DF-## for the reverse: what Readymerce's competitors do NOT include that Readymerce does, e.g. a cash-refund window at all).
- *If it worked too well, what would customers complain about?* `[D]` HYPOTHESIS, no direct evidence found this run: if Readymerce scales client volume, likely complaint vectors would be (a) catalogue similarity/cross-client competition from a shared production pipeline researching the same "winning products," and (b) thinning account-manager bandwidth per client as the "fit call"-scoped management model scales — neither is evidenced, both are plausible given the mechanism (C7/C9, un-headcounted per-client scoping).

### T5 · FACT BANK (F-##)

≥1 fact per component (C1–C11 from 01-PRODUCT-TRUTH.md §2); `basis` is a column, never a filter; UNKNOWN travels as a note, not a drop.

| f_id | fact | source_url | evidence_type | strength | basis | component |
|---|---|---|---|---|---|---|
| F-01 | "Shopify or Etsy store opened in your name and configured correctly" — store build included in the $500 package | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | C1 |
| F-02 | "Brand name direction, logo, banner and store structure" included | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | C2 |
| F-03 | "Search demand, seasonality and competition analysis... Category and product direction chosen from the data, not guesswork"; exact product count ("3 vetted products," per SEED) not re-confirmed on any DEEP-read page | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | TENTATIVE (count unconfirmed this pass) | cited (process); inferred (count, SEED-only) | C3 |
| F-04 | "Supplier and production feasibility review" included | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | C4 |
| F-05 | "Controlled ad testing with budgets you approve" + "Ad monitoring and adjustments, plus regular reporting" | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | C5 |
| F-06 | Platform (Shopify vs Etsy) and scope are "agreed with you on the fit call" — confirms SEED's C6 "1-on-1 strategy session" is the intake/scoping call | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | C6 |
| F-07 | "Ongoing listing optimisation and new product rollout... The level of ongoing management is agreed on the fit call" (not a fixed, published cadence) | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | C7 |
| F-08 | UNKNOWN — searched: no DEEP-read page names a "client portal," "credits," "balances" or "top-ups" feature; SEED's C8 remains sourced only to [R-OWNED] sales-call transcripts | N/A (absence finding across 9 pages) | N/A | UNKNOWN | inferred (SEED-only source) | C8 |
| F-09 | UNKNOWN — searched: no DEEP-read page names a "dedicated account manager" role; pages describe only that the buyer "can review the account and reporting at any time." SEED's C9 remains sourced only to [R-OWNED] | N/A | N/A | UNKNOWN | inferred (SEED-only source) | C9 |
| F-10 | 7-day money-back guarantee on the $500 build fee, running from payment date, voided immediately on delivery-acceptance, any add-on/upgrade purchase, or a request for further work; third-party costs (platform fees, ad spend, domain, apps, supplier costs) never refundable | readymerce.com/refund-policy; readymerce.com/terms-of-service | EXACT PRODUCT MATERIAL | WELL SUPPORTED (2 pages, word-for-word matching) | cited | C10 |
| F-11 | "The store account is in your name and stays in your name"; "Payouts go to your bank account — Readymerce never holds your revenue"; "The brand, listings, images and store assets belong to you" | readymerce.com/what-you-get | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | C11 |
| F-12 | Price: $500 one-time for "The Store Build & Research Package"; no second published tier exists — ongoing-management pricing is quoted per-client on the fit call, "no single number is published" (narrows SEED's INFERRED "$2,000 full launch" to a sales-call-quoted, not PDP-published, figure) | readymerce.com/pricing; readymerce.com/terms-of-service | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | price (general) |
| F-13 | "We make no income guarantees" / equivalent wording appears on 5 of 9 DEEP-read pages (pricing, risk-disclaimer, what-you-get, how-it-works, terms-of-service) | readymerce.com (5 pages, see PT-04 CONTRADICTS block for full text) | EXACT PRODUCT MATERIAL | WELL SUPPORTED | cited | outcomes/guarantee (general) |
| F-14 | ScamAdviser trust score: 0/100. Factors: WHOIS identity hidden via a paid privacy service; low visitor traffic; domain "only recently registered" | scamadviser.com/check-website/readymerce.com | 3rd-party automated tool (not buyer evidence) | N/A (tool output) | cited | general (limitation) |
| F-15 | ScamDoc trust score: 25% "Poor." Factors: domain created 2026-02-26 (<7 months old at check); a country-association heuristic; HTTPS present (noted by the tool as not itself proof of safety) | scamdoc.com/view/2555589 | 3rd-party automated tool (not buyer evidence) | N/A (tool output) | cited | general (limitation) |
| F-16 | No BBB profile exists under "Readymerce," "readymerce.com," or the LLC name tried ("TheExtraMile Marketing LLC") | bbb.org/search?find_text=Readymerce | 3rd-party absence finding | N/A | cited | general (limitation) |


### T6 · DIFFERENCE SHEET (DF-##) + mechanism_capacity

Per competitor seed (all 3 NW-SEED-## from 02-partials, `competitor_components[]` + price ladders reused by reference, not re-fetched — respects the "already read by 02, do not re-fetch" instruction). All rows `COMPETITOR-CLAIMED`.

| df_id | competitor | difference | problem_or_benefit_solved | unspoken_mechanism_candidate | what_it_prevents |
|---|---|---|---|---|---|
| DF-01 | NW-SEED-01 ecomdoneforyou.com | Sells automation across 3 marketplaces (Amazon FBA, Walmart WFS, Shopify) rather than one store per package; guarantee = "100% ROI guarantee within 6 months," conditional (void on unresponsiveness >2 weeks, policy violations, "change of mind"; may substitute store credit/discounts instead of cash) — vs. Readymerce's cash-eligible-but-fast-voiding 7-day refund on a single-platform $500 build | PB-01 (setup burden), across more platforms than Readymerce offers | Y — claims "advanced AI tools to look for manufacturers that are not fraudulent" and AI-driven "market analysis" for product selection | Fraudulent-supplier risk (per its own claim); multi-platform operational fragmentation |
| DF-02 | NW-SEED-02 ecommerceparadise.com | High-ticket one-time pricing ($9,997 / $14,997 / $19,997, ~20–40× Readymerce's $500 entry); guarantee is a milestone-rebuild promise with explicitly **no cash refunds** ("suppliers approved, products live, Google Shopping ads active within 90 days — or we continue working for free... There are no refunds, but you're guaranteed the work gets done") — the sharpest structural contrast with Readymerce's cash-refund (if narrow) model; includes "3 months direct coaching with Trevor" (a named person), which Readymerce's fetched pages do not offer | PB-01 + PB-06 explicitly on-page: "Tired of wasting time and money on stores that never take off?" | Y — the milestone-guarantee structure itself functions as the sold risk-reversal mechanism, replacing a cash-refund promise | Buyer walking away with nothing if the build stalls (they get continued work/a rebuild instead of a refund) — the opposite risk profile from Readymerce, where the buyer can walk away with cash but loses that right the moment they accept delivery or buy anything more |
| DF-03 | NW-SEED-03 ecomxpertz.com | Annual profit-share retainer ($3,000–$8,000/yr, EcomXpertz's cut of profit falling from 30%→0% as the flat fee rises) across 5 marketplace types incl. TikTok Shop and Amazon — a recurring, outcome-linked pricing shape, vs. Readymerce's one-time build fee; separately offers "full refund if the project has not been started" within a **20-day** window (wider, unconditional early-refund window than Readymerce's narrower delivery-triggered 7-day void) | PB-01 + PB-05 (product/supplier research, explicit across Amazon/TikTok/Shopify pages) | N — no distinct claimed mechanism beyond "automated"; also separately sells Amazon "account reinstatement" against a named list of 13 suspension causes | Amazon account suspension (a problem specific to this seed's marketplace-compliance angle, not present in Readymerce's or the other 2 seeds' claims) |

**mechanism_capacity: split verdict, one line each —**
- **Offer / guarantee structure: YES.** 3 independently-fetched competitor price ladders were compared and none shares Readymerce's shape (one-time $500 fee + un-published follow-on pricing + a cash-refund window that voids on any upsell): DF-01 uses a conditional 6-month ROI guarantee that can pay in credit not cash; DF-02 uses a milestone-rebuild guarantee with explicitly no cash refunds at 20–40× the price; DF-03 uses an annual profit-share retainer with a wider 20-day unconditional refund window. These are structural (pricing-mechanics and risk-allocation) differences, verifiable from each seed's own published terms, not merely wording — reason: **4 distinct risk/price shapes across 4 sellers in the same category is a real, checkable difference, not a cosmetic one.**
- **Underlying service delivery: NO / commodity.** All 4 sellers (Readymerce + 3 seeds) sell the same functional bundle — research a product/niche, build and brand a storefront, list products, set up some paid-traffic testing, then manage it on an ongoing basis — with no seed nor Readymerce demonstrating a defensible technical or fulfillment advantage in this run's evidence; differentiation among them runs through price, guarantee shape and named-person coaching (DF-02), not through what is actually built. Reason: **the "what it does" layer (T4) is identically advertised by all 3 seeds; only the "mechanism" layer (pricing/guarantee) differs.**


### T7 · PB REFRESH + PAIN SCORE (DEEP)

SEED rows in §5/§10 are never edited. This is a refresh table only.

| pb_id | seed_label → deep_label | n of N (review_mentions, code-computed T2) | what changed |
|---|---|---|---|
| PB-01 | SUPPORTED → SUPPORTED (confirmed, firmer) | 11 of 15 R-## rows (was 4 of 5 in SEED) | mechanism_plausibility_line upgraded from [R-SNIPPET] to **EXACT PRODUCT MATERIAL** (F-01..F-07): the PDP itself, fetched for the first time this run, directly confirms the build/branding/listing/launch mechanism. Door count unchanged (still b+c, door a still has no independent buyer text — the new R-06..R-13 units are SELLER-CURATED, not buyer reviews) — label stays SUPPORTED, not promoted to VALIDATED, because door (a)'s strict definition (≥10 mentions from ≥2 INDEPENDENT sources) is not met by seller-curated or proxy-category text |
| PB-06 | SUPPORTED → SUPPORTED (unchanged) | 3 of 15 (was 0 of 5 in SEED — SEED had zero mentions for this PB; DEEP adds R-11 seller-paraphrase + R-16/R-17 proxy-category) | product_contribution_boundary reinforced: 5 of 9 PDP pages now explicitly disclaim income/sales outcomes (F-13, PT-04 CONTRADICTS block) — the product's own text is now the clearest evidence that this PB's resolution is NOT guaranteed by the mechanism, even though the problem itself (no sales) is still SUPPORTED as a real buyer pain via SEED's door (b) |
| PB-05 | SUPPORTED → SUPPORTED (unchanged) | 1 of 15 (unchanged from SEED's 1-of-5, no new independent mention; R-08's seller testimonial about "custom build vs absurdly priced existing store" leans PB-01, not PB-05) | mechanism_plausibility_line upgraded to EXACT PRODUCT MATERIAL (F-03: "Category and product direction chosen from the data, not guesswork"); no change to door count |
| PB-03 | HYPOTHESIS → HYPOTHESIS (unchanged under the strict door rule) | 4 of 15 (was 2 of 5 in SEED) | **New non-buyer evidence found but does not open a new formal door**: two independent trust-check tools score the domain 0/100 (ScamAdviser) and 25/100 "Poor" (ScamDoc) (F-14/F-15), and zero reviews exist on 5 of 5 dedicated review platforms checked (BBB none, trustedrevie.ws 0, Sitejabber 0, ProductReview none, ScamDoc's visible comments unattributable) — none of this is buyer text (door a), a competitor claim (door b), or a mechanism claim (door c) under the taxonomy's strict definitions, so the label is not promoted; it is logged here as directly relevant context: a wary prospect googling "readymerce reviews" before buying would find these same dismal trust-checker results, which materially strengthens the plausibility of PB-03's underlying fear even though it does not meet the formal counting rule |
| PB-04, PB-02, PB-07 | HYPOTHESIS → HYPOTHESIS (unchanged) | PB-04: 3 of 15 (was 1 of 5); PB-02: 1 of 15 (unchanged); PB-07: 0 of 15 (unchanged) | NULL — searched: no new DEEP evidence found for these three; PB-04's 2 extra mentions (R-06, R-07) are seller-curated testimonials about time-freed-up, not independent buyer voice, so the door count is unchanged |

**Pain score (DEEP re-score) — `/10 DEEP`, method unchanged, axes re-evaluated against new EXACT PRODUCT MATERIAL where it bears:**

| pb_id | URGENCY | FREQUENCY | SPEND HISTORY | CONSEQUENCE | REORDER | total (SEED → DEEP) |
|---|---|---|---|---|---|---|
| PB-01 | 1 — unchanged `[D]` | 1 — unchanged `[D]` | 2 — unchanged ($250 deposit R-01; $500 confirmed EXACT PRODUCT MATERIAL F-12; £1,300/"10 grand" [R-OWNED T-08]) | 1 — unchanged `[D]` | 2 — **reinforced**: F-10 shows the refund guarantee is voided by "any additional service, add-on, upsell, or upgrade" — a designed-in upsell-timing incentive that corroborates SEED's "solving it creates the next need" framing | **7/10 → 7/10** (unchanged, now firmer-sourced) |
| PB-06 | 2 — unchanged `[D]` | 1 — unchanged `[D]` | 2 — unchanged (£1,300 prior [R-OWNED T-08]) | 2 — unchanged `[D]` | 2 — unchanged (marketing credits recur [R-OWNED T-04/T-06]) | **9/10 → 9/10** (unchanged) |
| PB-05 | 1 — unchanged `[D]` | 1 — unchanged `[D]` | 1 — unchanged `[D]` | 1 — unchanged `[D]` | 1 → **2** — F-07/F-03 show "staged product release" and "new product rollout" are built into the ongoing-management mechanism itself, i.e. picking-a-winning-product is not a one-and-done event but a recurring task the buyer stays exposed to | **5/10 → 6/10** |

Test (unchanged): *If he never buys this,* the store idea stays a half-built theme and the savings stay idle — and the earlier loss stays the last word on e-commerce `[D]`.
counterevidence (DEEP addition): the seller's own 5-of-9-page income disclaimer block (F-13) is itself counterevidence against treating PB-06 ("no sales") as something this product reliably fixes — the product's own text agrees the outcome is not guaranteed.


### T8 · COVERAGE STATEMENT (DEEP) + EVIDENCE LEDGER

**Tools used this DEEP pass:** Apify — 0 calls (BLOCKED-ON-TOOL all month; every planned recipe printed as `NOT RUN — Apify monthly limit` at the top of this section, $0.00 spent, none attempted a 2nd time per rule 13). Exa agent (`mcp__Readymerce_Exa__agent_run`) — **9 runs, $0.825 total** (6 × medium $0.10 + 1 × low $0.025 + 2 × medium $0.10; under the ≤$1.00 cap, ≈8–10 medium-run guidance met). WebSearch — 2 calls (free; Reddit/forum discovery, both returned no Readymerce-specific threads). TranscriptAPI — `search_youtube` 3 calls (1 transient 408 retried successfully) + `get_youtube_transcript` 2 calls (both succeeded via ASR captions despite `hasCaptions:false` in search metadata); exact credit cost not returned by the tool, calls stayed well inside the ≤10-credit budget. GetHookd / Meta / Higgsfield — 0 calls (not applicable to this step's DEEP scope). [R-OWNED] transcripts — 0 read this pass (per brief: not reviews, cited by ID only where SEED already filed them).

COVERAGE (DEEP): reviews 0 read of 0 retrieved as independent exact-SKU CUSTOMER EXPERIENCE (sources exhausted: BBB no profile, ScamAdviser 0 comments, ScamDoc 6 comments unattributable, trustedrevie.ws 0 reviews, Sitejabber 0 reviews, ProductReview no listing, Trustpilot BLOCKED-ON-TOOL, Reddit/Warrior Forum/Quora 0 threads found; 3★ 0 of 0); PDP EXACT PRODUCT MATERIAL 9 of 9 attempted pages read in full (5 additional paths 404'd: /testimonials, /case-studies, /reviews, /guarantee, /terms); SELLER-CURATED quotes 10 read (3 on-site testimonials with an actor-portrayal disclosure + 7 earned-media/press self-quotes); SIMILAR-PRODUCT-CONTEXT 2 of 2 attempted YouTube analyst transcripts read (0 first-person Readymerce buyer videos exist on YouTube this run); components 9 of 11 with a DEEP-sourced fact (C8 client-portal and C9 account-manager remain UNKNOWN — searched, SEED-[R-OWNED]-only); DF 3 (one per seed, ≥3 floor met); PB refreshed 6 of 7 (labels unchanged for all 6 under the strict door rule — new trust-score evidence for PB-03 logged as context, not a door); pain score re-scored for the 3 lanes (PB-01 7/10 unchanged, PB-06 9/10 unchanged, PB-05 5→6/10); Apify $0.00 (BLOCKED-ON-TOOL, 8 recipes printed NOT RUN at top of this section); Exa $0.825; datasets: none saved under datasets/ (no dataset-scale scrape occurred — every result fit inline); CONFIDENCE: truth card **PROXY-SKU** (0 independent exact-SKU buyer reviews read in full despite exhausting every reachable review venue), problem map **SUPPORTED 3 (PB-01, PB-06, PB-05, unchanged) / HYPOTHESIS 4 (PB-02, PB-03, PB-04, PB-07, unchanged) / VALIDATED 0** — door (a) (≥10 independent buyer mentions) remains unreachable for every PB this run because no independent buyer-voice review venue for readymerce.com yielded content; the most material new finding is the seller's own 5-page income-disclaimer text directly contradicting its sales-call income claims (PT-04/T3 CONTRADICTS block) and two independent trust-check tools scoring the domain 0/100 and 25/100 "Poor" (F-14/F-15) — both logged as high-value context for steps 03/09/12/13's claims and trust framing even though neither promotes a PB label under this step's strict counting rule.

**Evidence ledger — every R-## on file (SEED + DEEP), with url, platform, date, handle, tier:**

| r_id | url | platform | date | handle | tier |
|---|---|---|---|---|---|
| R-01 | https://uk.trustpilot.com/review/readymerce.com | Trustpilot (via WebSearch summary, SEED) | UNKNOWN | UNKNOWN (reviewer), Readymerce (co. reply) | [R-SNIPPET] |
| R-02 | WebSearch result set q='done for you ecommerce store business service reviews' (SEED, attribution UNRESOLVED) | DFY review pool | UNKNOWN | none | [R-SNIPPET] |
| R-03 | same as R-02 (SEED) | DFY review pool | UNKNOWN | none | [R-SNIPPET] |
| R-04 | same as R-02 (SEED) | DFY review pool | UNKNOWN | none | [R-SNIPPET] |
| R-05 | same as R-02 (SEED) | DFY review pool | UNKNOWN | none | [R-SNIPPET] |
| R-06 | https://readymerce.com/how-it-works | Readymerce PDP (seller-curated) | UNKNOWN | Marcus H. | [R-PAGE via Exa] |
| R-07 | https://readymerce.com/how-it-works | Readymerce PDP (seller-curated) | UNKNOWN | Priya S. | [R-PAGE via Exa] |
| R-08 | https://readymerce.com/how-it-works | Readymerce PDP (seller-curated) | UNKNOWN | Daniel C. | [R-PAGE via Exa] |
| R-09 | https://bestofbestreview.com/awards/readymerce-best-done-for-you-e-commerce-store-service-in-the-uk-of-2026 | award/earned-media page | March 25, 2026 | Matthew (Readymerce spokesperson) | [R-PAGE via Exa] |
| R-10 | same as R-09 | award/earned-media page | March 25, 2026 | Matthew (Readymerce spokesperson) | [R-PAGE via Exa] |
| R-11 | https://evergreenawards.com/awards/readymerce-best-etsy-shopify-store-setup-service-in-the-united-states-of-2025 | award page | UNKNOWN | award body (paraphrasing an unnamed client) | [R-PAGE via Exa] |
| R-12 | https://lifestyle.utv.ie/story/534022/inside-the-business-model-that-is-replacing-traditional-e-commerce-courses/ | earned-media article | UNKNOWN | Readymerce (co.) | [R-PAGE via Exa] |
| R-13 | https://www.financialcontent.com/article/getnews-2026-3-9-readymerce-emerges-as-the-go-to-solution-for-aspiring-e-commerce-entrepreneurs | press release wire | March 9, 2026 | Readymerce team | [R-PAGE via Exa] |
| R-16 | https://www.youtube.com/watch?v=xWS-4VHqkcM | YouTube (proxy category, NOT Readymerce) | ~2026-09 | OverHyped Reviews | [R-PAGE via TranscriptAPI] |
| R-17 | https://www.youtube.com/watch?v=6t3Nl8JMuvM | YouTube (proxy category, NOT Readymerce) | ~2026-07/08 | Digital Dollar Detective | [R-PAGE via TranscriptAPI] |

Non-R-## evidence used (facts, not reviews — see T5 F-14/F-15/F-16 for full citations): scamadviser.com/check-website/readymerce.com; scamdoc.com/view/2555589; bbb.org/search?find_text=Readymerce; trustedrevie.ws/reviews/readymerce.com ("no reviews"); sitejabber.com/reviews/readymerce.com ("0 reviews"); productreview.com.au/search?query=readymerce (no listing). LK-01/LK-02/LK-03 (ecommerceparadise.com's own testimonials) reused by reference from `02-partials/02-COMPETITOR-INTEL.NW-SEED-02.md §15` — not re-fetched, not re-numbered.

**COVERAGE (DEEP) — one-line summary:** reviews N=0 read of M=0 retrievable (exact-SKU independent), every reachable venue exhausted; PDP 9/9 pages EXACT PRODUCT MATERIAL (new this pass — SEED's PDP was BLOCKED-ON-TOOL, DEEP's Exa route succeeded); components 9 of 11 with a DEEP fact; DF 3; PB refreshed 6 (labels unchanged, evidence firmed); Apify $0.00 (8 recipes NOT RUN — monthly limit); Exa $0.825 (9 runs); datasets: none; CONFIDENCE: truth card PROXY-SKU, problem map SUPPORTED 3 / HYPOTHESIS 4 / VALIDATED 0.

