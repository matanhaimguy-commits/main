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

