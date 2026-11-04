# 06 — VOC REPORT · Readymerce · MODE: MERGE · corpus_version v1
agent 06-MERGE · wave W2 · written 2026-09-24 · inputs: 5 harvest partials (PB-01, PB-06, PB-05, OWNED-US, OWNED-UK) · 01-HANDOFF + 01-DEEP (PT-##) · 04/05 partials · `03-HANDOFF.json` ABSENT → `LATE-BOUND: 03.AS-##` for EK stamps. Cost of this merge: $0.00 (code execution only, no web calls).

**Reading rule for this report.** Three corpora are never mixed: `MARKET_VOC` (people living the problem on the public web), `PRODUCT_TRUTH` (10 Trustpilot reviews of a competitor DFY vendor filed by HV-PB-01 — PROXY-SKU, never proof for Readymerce), `OWNED_PROOF` (the operator's own sales-call transcripts, prospect turns only). Every ledger prints MARKET_VOC ‖ OWNED_PROOF ‖ TOTAL. Market themes are argued on MARKET_VOC; OWNED_PROOF is one platform (a label there tops out at SUPPORTED). Ledger format: `obs · units · authors · threads · platforms → label`. Owned authors = persons (84 calls collapse to 78 persons via the harvesters' 'same prospect as' markers). `C-####` rows are rep pitch — contextual, never VOC, never in a bank; they appear only in §9, §16, §17. `[D]` = analyst inference.

## §0 · COVERAGE HEADER

| corpus | Q-records | floor-eligible (non-snippet) | source units | persons/authors | source types | tiers |
|---|---|---|---|---|---|---|
| MARKET_VOC | 116 | 111 | 42 | 64 | 4 | {'[R-PAGE via Exa]': 45, '[R-PAGE]': 12, '[R-SNIPPET]': 5, '[R-SCRAPE]': 54} |
| PRODUCT_TRUTH | 10 | 10 | 2 | 10 | 1 | {'[R-PAGE via Exa]': 10} |
| OWNED_PROOF | 181 | 181 | 84 | 78 | 1 | {'[R-OWNED]': 181} |
| TOTAL | 307 | 302 | 128 | 152 | 6 | {'[R-PAGE via Exa]': 55, '[R-PAGE]': 12, '[R-SNIPPET]': 5, '[R-SCRAPE]': 54, '[R-OWNED]': 181} |

Context rows: C-#### = 29 (OWNED-US 16 · OWNED-UK 13), excluded from every count. Dedupe on (source_url, unique_author_id, sha1(exact_quote)): 336 rows in → 0 duplicates → 336 out. **ledgers n = 307 = corpus n 307.** hyper_responsive flagged: 67 (top 20% longest passage per corpus × primary PB; the partials had flagged 0).

### GLOBAL FLOOR TABLE — tested twice (MARKET_VOC alone · MARKET_VOC + OWNED_PROOF); PRODUCT_TRUTH printed as a third column for completeness

| floor | floor/target | MARKET_VOC | MARKET_VOC + OWNED_PROOF | + PRODUCT_TRUTH (all) |
|---|---|---|---|---|
| records_total (floor-eligible) | 200 / 400 | 111/200 PARTIAL | 292/200 MET | 302/200 MET |
| PB-01 | 40 / 80 | 30/40 PARTIAL | 75/40 MET | 85/40 MET |
| PB-06 | 40 / 80 | 54/40 MET | 80/40 MET | 80/40 MET |
| PB-05 | 40 / 80 | 27/40 PARTIAL | 44/40 MET | 44/40 MET |
| CP-01 | 25 / 50 | 4/25 PARTIAL | 29/25 MET | 29/25 MET |
| CP-02 | 25 / 50 | 0/25 PARTIAL | 21/25 PARTIAL | 21/25 PARTIAL |
| CP-03 | 25 / 50 | 46/25 MET | 81/25 MET | 81/25 MET |
| CP-04 | 25 / 50 | 0/25 PARTIAL | 19/25 PARTIAL | 19/25 PARTIAL |
| CP-05 | 25 / 50 | 43/25 MET | 60/25 MET | 70/25 MET |
| CP-06 | 25 / 50 | 0/25 PARTIAL | 15/25 PARTIAL | 15/25 PARTIAL |
| CP-07 | 25 / 50 | 0/25 PARTIAL | 2/25 PARTIAL | 2/25 PARTIAL |
| reddit | 80 | 0/80 PARTIAL — BLOCKED-ON-TOOL | 0/80 PARTIAL | 0/80 PARTIAL |
| reviews (≥8 from 3★) | 60 | 0/60 PARTIAL | 0/60 PARTIAL | 10/60 PARTIAL · 3★ 0/8 |
| video comments | 30 | 0/30 PARTIAL — BLOCKED-ON-TOOL (youtube_transcript 66 records are a separate lane, no floor) | 0/30 PARTIAL | 0/30 PARTIAL |
| fb+forum+quora | 20 | 42/20 MET | 42/20 MET | 42/20 MET |
| ad comments | 10 when available | 0 — LATE-BOUND: 02.share_url | 0 | 0 |
| source types | ≥4 | 4/4 MET (youtube_search, forum, quora, blog_comments) | 5/4 MET | 6/4 MET |

| tag floor | floor | MARKET_VOC | MARKET_VOC + OWNED_PROOF | TOTAL (+PRODUCT_TRUTH) |
|---|---|---|---|---|
| pain | 20 | 51/20 MET | 52/20 MET | 53/20 MET |
| scene | 15 | 9/15 PARTIAL | 34/15 MET | 34/15 MET |
| failed_solution | 20 | 14/20 PARTIAL | 43/20 MET | 43/20 MET |
| objection | 20 | 18/20 PARTIAL | 65/20 MET | 66/20 MET |
| desire | 15 | 7/15 PARTIAL | 41/15 MET | 46/15 MET |
| trigger | 15 | 7/15 PARTIAL | 18/15 MET | 18/15 MET |
| belief | 15 | 31/15 MET | 62/15 MET | 62/15 MET |
| symptom | 10 | 5/10 PARTIAL | 8/10 PARTIAL | 8/10 PARTIAL |
| skepticism | 10 | 23/10 MET | 59/10 MET | 61/10 MET |
| spend | 5 | 23/5 MET | 71/5 MET | 76/5 MET |
| deeper_hope | 5 | 6/5 MET | 12/5 MET | 13/5 MET |
| tired_of_hearing | 5 | 4/5 PARTIAL | 7/5 MET | 7/5 MET |
| horror_story | 3 | 8/3 MET | 8/3 MET | 10/3 MET |
| curiosity | 3 | 2/3 PARTIAL | 3/3 MET | 3/3 MET |
| corruption | 3 | 0/3 PARTIAL | 0/3 PARTIAL | 0/3 PARTIAL |

Tags below floor — MARKET_VOC alone: ['scene 9/15', 'failed_solution 14/20', 'objection 18/20', 'desire 7/15', 'trigger 7/15', 'symptom 5/10', 'tired_of_hearing 4/5', 'curiosity 2/3', 'corruption 0/3'] · MARKET_VOC + OWNED_PROOF: ['symptom 8/10', 'corruption 0/3'].

Per-PB harvest status: PB-01 PARTIAL-types (3/4 floor-eligible) · PB-06 MET 55/40 · PB-05 `PARTIAL (N=30/40) — chain exhausted: [Apify monthly hard limit, egress 403, Exa cannot retrieve reddit.com/Trustpilot]` · PB-02, PB-03, PB-04, PB-07: `PARTIAL — PB-## not harvested` (no MARKET_VOC harvester was planned for them; they carry OWNED_PROOF records only). OWNED-US 109/70 MET (46/155 calls read) · OWNED-UK 72/70 MET (40/42 diarized calls; 80 undiarized files unread).

## §1 · PAIN LANDSCAPE (PP-##) + per-PB / per-CP

| pp_id | pb_id | pain (buyer words) | emotional_reality (verbatim anchor) | ledgers MARKET_VOC ‖ OWNED_PROOF ‖ TOTAL | intensity | population_tags[] |
|---|---|---|---|---|---|---|
| PP-01 | PB-01 | I can't get the store built or live myself | 'tons of links that are like a snowstorm of information' | MARKET_VOC: obs 6 · units 3 · authors 6 · threads 3 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 8 · units 5 · authors 8 · threads 5 · platforms 3 → VALIDATED | Very High [D] | CP-05:3 |
| PP-02 | PB-06 | I built / ran a store and got no sales — money gone | 'pure loss of money of time of energy of honestly hope' | MARKET_VOC: obs 7 · units 6 · authors 6 · threads 6 · platforms 3 → VALIDATED ‖ OWNED_PROOF: obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED ‖ TOTAL: obs 10 · units 9 · authors 9 · threads 9 · platforms 4 → VALIDATED | Very High [D] | CP-03:10, CP-05:1, CP-06:1 |
| PP-03 | PB-05 | I don't know what to sell | 'I don't know where to start or what I should sell' | MARKET_VOC: obs 8 · units 8 · authors 8 · threads 8 · platforms 3 → VALIDATED ‖ OWNED_PROOF: 0 ‖ TOTAL: obs 8 · units 8 · authors 8 · threads 8 · platforms 3 → VALIDATED | High [D] | CP-05:7 |
| PP-04 | PB-03 | I've been burned by scams / vendors and can't trust the next one | 'I've been burned many times' | MARKET_VOC: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ PRODUCT_TRUTH: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ OWNED_PROOF: obs 5 · units 5 · authors 5 · threads 5 · platforms 1 → SUPPORTED ‖ TOTAL: obs 7 · units 7 · authors 7 · threads 7 · platforms 3 → VALIDATED | Low [D] | CP-03:6, CP-05:1 |
| PP-05 | PB-02 | I'm stuck in (or out of) a job and need another income | 'I've been doing this for 20 years, I'm tired now.' | MARKET_VOC: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ OWNED_PROOF: obs 7 · units 7 · authors 7 · threads 7 · platforms 1 → SUPPORTED ‖ TOTAL: obs 8 · units 8 · authors 8 · threads 8 · platforms 2 → VALIDATED | Low [D] | CP-01:6, CP-02:1, CP-03:1 |
| PP-06 | PB-04 | No time to run it | 'The one thing I don't have in my life is time.' | MARKET_VOC: obs 2 · units 1 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ OWNED_PROOF: obs 4 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED ‖ TOTAL: obs 6 · units 5 · authors 6 · threads 6 · platforms 2 → VALIDATED | Low [D] | CP-01:2, CP-02:1, CP-04:1, CP-06:1 |
| PP-07 | PB-07 | Retirement / family money needs to work | 'I need some retirement money, you know, to live.' | MARKET_VOC: 0 ‖ OWNED_PROOF: obs 6 · units 6 · authors 6 · threads 6 · platforms 1 → SUPPORTED ‖ TOTAL: obs 6 · units 6 · authors 6 · threads 6 · platforms 1 → SUPPORTED | Moderate [D] | CP-01:1, CP-02:1, CP-06:4 |

Member quotes per PP (MARKET_VOC first, then OWNED_PROOF):
- **PP-01** MARKET: "tons of links that are like a snowstorm of information" (Q-F-0006) · "I'm tech savvy and competent. I cannot find a simple step by step" (Q-F-0012) · "10 weeks on simple tasks that the system doesn't verify" (Q-F-0013) ‖ OWNED: "It won't let me get on live at all" (Q-O-0014) · "I don't know what to do. This is not working for me" (Q-O-0077)
- **PP-02** MARKET: "i got zero sales which means i lost 254 dollars" (Q-Y-0014) · "it didn't sell one product not one product" (Q-Y-0046) · "pure loss of money of time of energy of honestly hope" (Q-Y-0047) ‖ OWNED: "the product did not sell, so I had to close the store" (Q-O-0108) · "my store didn't even make $20, so I had to come out" (Q-O-0101) · "I picked the baby store. It just didn't work" (Q-O-0082)
- **PP-03** MARKET: "I don't know where to start or what I should sell" (Q-F-0040) · "pls can someone direct me on the right product to sell" (Q-F-0039) · "how can i find a good product or winning product?" (Q-F-0028) ‖ OWNED: NULL
- **PP-04** MARKET: "I've been burned many times" (Q-Y-0030) ‖ OWNED: "I gave somebody $4,500, and they took my money" (Q-O-0062) · "I was involved in a cryptocurrency scam, so I've lost a lot of money in that." (Q-O-0148) · "I felt like it was a scam" (Q-O-0073)
- **PP-05** MARKET: "trying to scale my business while keeping my full-time job" (Q-F-0017) ‖ OWNED: "I've been doing this for 20 years, I'm tired now." (Q-O-0111) · "I wish I was doing something else" (Q-O-0096) · "I still haven't got a job with over 700 applications" (Q-O-0065)
- **PP-06** MARKET: "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015) · "Time intensive early on (i work a full time job right now)" (Q-F-0016) ‖ OWNED: "The one thing I don't have in my life is time. Plus I have a child of five years old." (Q-O-0143) · "I'm a computer consultant and I have very little time." (Q-O-0154) · "I closed it because I didn't have time to work the business" (Q-O-0090)
- **PP-07** MARKET: NULL ‖ OWNED: "No, I'm retired now, you get it? So I need some retirement money, you know, to live." (Q-O-0121) · "I've been on the list for two years for apartment" (Q-O-0069) · "I have to pay for my student my son college fees" (Q-O-0085)

**Pain hierarchy per harvested PB** (surface → practical → emotional → identity/social → conflict/tradeoff → deeper desired state; each rung a Q-##):
- PB-01: 'I cannot find a simple step by step' (Q-F-0012) → '10 weeks on simple tasks' (Q-F-0013) → 'snowstorm of information' (Q-F-0006) → 'I'm tech savvy and competent' yet stuck (Q-F-0012) → 'I work a full time job as well' (Q-F-0015) → 'I would just link into the store once it is finished' (Q-F-0005).
- PB-06: 'not a single sale' (Q-Q-0001) → 'lost 254 dollars' (Q-Y-0014) → 'pure loss of money of time of energy of honestly hope' (Q-Y-0047) → 'there's plenty of us losing, including myself' (Q-Y-0027) → 'give up or else i would literally lose all my money' (Q-Y-0049) → 'I was afraid to ever try again, but eventually I did' (Q-B-0004).
- PB-05: 'I don't know where to start or what I should sell' (Q-F-0040) → 'constantly jumping from one idea to another' (Q-Y-0059) → 'competition on Etsy is huge, that was intimidating' (Q-Y-0055) → NULL (no identity rung stated) → 'I'm not going to let perfection slow me down' (Q-Y-0057) → 'I don't need to invent something completely new' (Q-Y-0056).
- PB-02/03/04/07 (OWNED_PROOF only): 'I'm tired now' (Q-O-0111) → 'I still haven't got a job with over 700 applications' (Q-O-0065) → 'I lost everything' (Q-O-0128) → 'I'm 56. I'm not in Internet' (Q-O-0076) → 'I don't want to quit and then start struggling' (Q-O-0133) → 'turn this side hustle into a main job' (Q-O-0105).

**Desire hierarchy** — reserved to 08 (§4); records exported raw. **Pattern ratings** [D] (Recurrence · Emotional Intensity · Urgency · Solution-Seeking · Confidence): PB-06 High · Very High · Moderate · High · High (VALIDATED market ledger) — PB-01 High · Moderate · Low · High · Moderate — PB-05 Moderate · Low · Low · High · Moderate. **If untreated** [D]: the store stays unbuilt or unsold and the loss stays the last word (Q-Y-0049, Q-F-0014). **Toleration threshold** [D]: people quit after a cash figure they name (Q-Y-0014 $254, Q-Y-0023 ~$1,000) or after repeated attempts (Q-F-0010 'second attempt').

**Per-CP sections** (ledgers MARKET_VOC ‖ OWNED_PROOF ‖ TOTAL):
- **CP-01**: MARKET_VOC: obs 4 · units 1 · authors 4 · threads 4 · platforms 1 → SUPPORTED ‖ OWNED_PROOF: obs 25 · units 15 · authors 15 · threads 15 · platforms 1 → SUPPORTED ‖ TOTAL: obs 29 · units 16 · authors 19 · threads 19 · platforms 2 → VALIDATED · e.g. MARKET "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015) · "Time intensive early on (i work a full time job right now)" (Q-F-0016) ‖ OWNED "I get Social Security, so I need to protect that" (Q-O-0007) · "Could I get up to at least $10,000 a month in three months" (Q-O-0008)
- **CP-02**: MARKET_VOC: 0 ‖ OWNED_PROOF: obs 21 · units 11 · authors 11 · threads 11 · platforms 1 → SUPPORTED ‖ TOTAL: obs 21 · units 11 · authors 11 · threads 11 · platforms 1 → SUPPORTED · e.g. MARKET NULL ‖ OWNED "I'm in a parking lot, and I'm gonna pick up my son" (Q-O-0017) · "I need to talk to my husband about it" (Q-O-0018)
- **CP-03**: MARKET_VOC: obs 47 · units 18 · authors 18 · threads 18 · platforms 4 → VALIDATED ‖ OWNED_PROOF: obs 35 · units 18 · authors 14 · threads 18 · platforms 1 → SUPPORTED ‖ TOTAL: obs 82 · units 36 · authors 32 · threads 36 · platforms 5 → VALIDATED · e.g. MARKET "i've already lost 500 drop shipping" (Q-Y-0013) · "i got zero sales which means i lost 254 dollars" (Q-Y-0014) ‖ OWNED "I invested a lot of my money into buying this business" (Q-O-0004) · "we don't have the budget to be able to do a lot of ads" (Q-O-0005)
- **CP-04**: MARKET_VOC: 0 ‖ OWNED_PROOF: obs 19 · units 9 · authors 8 · threads 9 · platforms 1 → SUPPORTED ‖ TOTAL: obs 19 · units 9 · authors 8 · threads 9 · platforms 1 → SUPPORTED · e.g. MARKET NULL ‖ OWNED "You guys can fully automate my online business" (Q-O-0001) · "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002)
- **CP-05**: MARKET_VOC: obs 46 · units 24 · authors 27 · threads 24 · platforms 4 → VALIDATED ‖ PRODUCT_TRUTH: obs 10 · units 2 · authors 10 · threads 2 · platforms 1 → SUPPORTED ‖ OWNED_PROOF: obs 17 · units 6 · authors 6 · threads 6 · platforms 1 → SUPPORTED ‖ TOTAL: obs 73 · units 32 · authors 43 · threads 32 · platforms 6 → VALIDATED · e.g. MARKET "now I can't access it, contact an administrator which should be me" (Q-F-0001) · "your store is half-ass done" (Q-F-0002) ‖ OWNED "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002) · "It won't let me get on live at all" (Q-O-0014)
- **CP-06**: MARKET_VOC: 0 ‖ OWNED_PROOF: obs 15 · units 8 · authors 7 · threads 8 · platforms 1 → SUPPORTED ‖ TOTAL: obs 15 · units 8 · authors 7 · threads 8 · platforms 1 → SUPPORTED · e.g. MARKET NULL ‖ OWNED "he used to say, man, cherish this time" (Q-O-0041) · "I don't have the time to do the due diligence" (Q-O-0042)
- **CP-07**: MARKET_VOC: 0 ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL · e.g. MARKET NULL ‖ OWNED "I need to talk to my husband about it" (Q-O-0018) · "I have some funds, but it's jointly owned. So, we're sharing it, let's say." (Q-O-0134)

## §2 · PAIN LANGUAGE

**Exact phrases ranked by ledger** (case-insensitive match in exact_passage; authors = persons):

| phrase | MARKET_VOC authors | OWNED_PROOF persons | TOTAL obs |
|---|---|---|---|
| 'store' | 25 | 20 | 58 |
| 'time' | 14 | 28 | 50 |
| '500' | 3 | 14 | 20 |
| 'job' | 3 | 11 | 15 |
| 'the money' | 3 | 9 | 15 |
| '$500' | 1 | 8 | 10 |
| 'lost' | 4 | 3 | 10 |
| 'scam' | 1 | 4 | 7 |
| 'winning product' | 5 | 0 | 5 |
| 'tired' | 1 | 4 | 5 |
| 'kids' | 0 | 5 | 5 |
| 'trust' | 2 | 1 | 4 |
| 'give up' | 4 | 0 | 4 |
| 'side hustle' | 0 | 3 | 3 |
| 'retire' | 0 | 3 | 3 |
| 'no sales' | 2 | 1 | 3 |
| 'wife' | 0 | 2 | 2 |
| 'not one' | 1 | 0 | 2 |
| 'full time job' | 2 | 0 | 2 |
| 'husband' | 0 | 1 | 1 |

**TOP 50 VERBATIM, hook-grade ≤ grade 8** (hyper_responsive first; MARKET_VOC 25 then OWNED_PROOF 25; eligible pool MARKET 98 · OWNED 159):
- [MARKET] "you have to scramble around looking for youtube videos" (Q-F-0008) — grade 6
- [MARKET] "so you can watch me either make money or lose money" (Q-Y-0010) — grade 7
- [MARKET] "people struggle to pay that kind of amount" (Q-Y-0006) — grade 7
- [MARKET] "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015) — grade 7
- [MARKET] "I tried to design by myself it didn't become nice" (Q-Y-0012) — grade 7
- [MARKET] "no one had bought anything" (Q-F-0024) — grade 5.2
- [MARKET] "to see if it's worth paying someone on Fiverr" (Q-Y-0003) — grade 7
- [MARKET] "I would just link into the store once it is finished" (Q-F-0005) — grade 7
- [MARKET] "it will be hard to convert a random social media visitor" (Q-F-0023) — grade 6.9
- [MARKET] "you must do a lot of research yourself" (Q-F-0033) — grade 8
- [MARKET] "I don't know where to start or what I should sell" (Q-F-0040) — grade 5
- [MARKET] "After 10 days of campaign, still no orders." (Q-F-0021) — grade 4.0
- [MARKET] "that money is instantly going on hold" (Q-Y-0042) — grade 4.0
- [MARKET] "hire an agency to do the store for you to do the ads for you" (Q-Y-0035) — grade 5.2
- [MARKET] "find a product you have a passion for" (Q-F-0035) — grade 6
- [MARKET] "hard at the beginning to put your emotions aside" (Q-Y-0065) — grade 7
- [MARKET] "I'm going to be creating a successful e-commerce store within the next 30 days" (Q-Y-0040) — grade 7.6
- [MARKET] "Do I just choose what I want to sell" (Q-F-0041) — grade 5
- [MARKET] "i've already lost 500 drop shipping" (Q-Y-0013) — grade 7.6
- [MARKET] "make it seem like easy money when it's really not" (Q-Y-0016) — grade 6.0
- [MARKET] "i got zero sales which means i lost 254 dollars" (Q-Y-0014) — grade 3.7
- [MARKET] "tons of links that are like a snowstorm of information" (Q-F-0006) — grade 6
- [MARKET] "why not pay Shopify expert to create my very own store" (Q-Y-0001) — grade 7
- [MARKET] "numerous chats, bots, and emails only wastes time" (Q-F-0011) — grade 6
- [MARKET] "I had someone build a shopify store for me because I wanted to get started quickly" (Q-F-0018) — grade 7
- [OWNED_] "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002) — grade 4.5
- [OWNED_] "I have a friend that does it online... when I saw your advert yesterday, I just clicked on it." (Q-O-0166) — grade 4.3
- [OWNED_] "He's coming to service my boiler ready for the winter." (Q-O-0172) — grade 7.2
- [OWNED_] "You guys can fully automate my online business" (Q-O-0001) — grade 5.1
- [OWNED_] "making the skin be nice, something like that" (Q-O-0044) — grade 8.0
- [OWNED_] "The AI is getting too fast. Too crazy" (Q-O-0079) — grade 1.1
- [OWNED_] "I just got out of prison for seven years" (Q-O-0010) — grade 3.2
- [OWNED_] "I'm at that age now where a gamble doesn't really frighten you." (Q-O-0181) — grade 5.8
- [OWNED_] "I've just taken a retirement, so I want to focus on doing it well." (Q-O-0141) — grade 6.7
- [OWNED_] "At what point do I take over the store? Is it something I have to run on my own?" (Q-O-0169) — grade 3.6
- [OWNED_] "I'm struggling on my financial side. I believe it's not the best time to just start investing." (Q-O-0156) — grade 5.8
- [OWNED_] "I will start at least three to four businesses" (Q-O-0087) — grade 6.4
- [OWNED_] "I had other businesses then that I was running... I'm regretting now because if I had started then." (Q-O-0152) — grade 6.3
- [OWNED_] "I don't have a job at the moment, so I'm using my my wife's income" (Q-O-0033) — grade 0.5
- [OWNED_] "we don't have the budget to be able to do a lot of ads" (Q-O-0005) — grade 2.4
- [OWNED_] "Is it $500 it's starting from, and it goes up to $5,000 or what?" (Q-O-0155) — grade 1.9
- [OWNED_] "I don't really like showing my face on social media" (Q-O-0035) — grade 5.5
- [OWNED_] "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006) — grade 6.1
- [OWNED_] "he used to say, man, cherish this time" (Q-O-0041) — grade 2.6
- [OWNED_] "how much is it? Is it 500 investment? 200 investment?" (Q-O-0057) — grade 1.5
- [OWNED_] "I would like to get in touch with y'all when I'm more prepared" (Q-O-0026) — grade 6.5
- [OWNED_] "My computer just broke. My son just broke the computer." (Q-O-0146) — grade 5.2
- [OWNED_] "they want $2,800 for me to just get it out of there" (Q-O-0067) — grade 5.8
- [OWNED_] "I'm busy paying off my debts. I'm on government benefits as well." (Q-O-0149) — grade 3.5
- [OWNED_] "Could I get up to at least $10,000 a month in three months" (Q-O-0008) — grade 2.1

**EXPRESSIONS grouped** (verbatim, ≤4 per group, MARKET ‖ OWNED):
- Pain (pain): MARKET "now I can't access it, contact an administrator which should be me" (Q-F-0001) · "your store is half-ass done" (Q-F-0002) · "they said they would build a store, but i am building the store???" (Q-F-0004) ‖ OWNED "I've been doing this for 20 years, I'm tired now." (Q-O-0111)
- Functional limitation (symptom): MARKET "How can I give you a SPECIFIC question" (Q-F-0007) · "grasping things A LOT quicker and easier" (Q-F-0009) · "numerous chats, bots, and emails only wastes time" (Q-F-0011) ‖ OWNED "It won't let me get on live at all" (Q-O-0014) · "I'm 56. I don't have I'm not in Internet" (Q-O-0076) · "I don't know what to do. This is not working for me" (Q-O-0077)
- Identity (identity): MARKET "there's plenty of us losing, including myself" (Q-Y-0027) · "I've tried Drop Shipping on and off for like 7 years now" (Q-Y-0028) · "I am the extreme version of not caring about any problem at all" (Q-Y-0037) ‖ OWNED "I just got out of prison for seven years" (Q-O-0010) · "I have some health issue. I don't work. I'm carpenter" (Q-O-0020) · "I do have a girlfriend. I have four children" (Q-O-0059)
- Fear (fear): MARKET "he's a scam, I was told he doesn't work with Shopify" (Q-F-0003) · "that money is instantly going on hold" (Q-Y-0042) · "i had to give up or else i would literally lose all my money" (Q-Y-0049) ‖ OWNED "I invested a lot of my money into buying this business" (Q-O-0004) · "these fucking Americans ... won a $170,000 from me" (Q-O-0011) · "I have some health issue. I don't work. I'm carpenter" (Q-O-0020)
- Desire (desire): MARKET "I would just link into the store once it is finished" (Q-F-0005) · "why not pay Shopify expert to create my very own store" (Q-Y-0001) · "to see if it's worth paying someone on Fiverr" (Q-Y-0003) ‖ OWNED "You guys can fully automate my online business" (Q-O-0001) · "Could I get up to at least $10,000 a month in three months" (Q-O-0008) · "would I at least have $50,000 worth of money" (Q-O-0009)
- Failed attempts (failed_solution): MARKET "now I can't access it, contact an administrator which should be me" (Q-F-0001) · "your store is half-ass done" (Q-F-0002) · "they said they would build a store, but i am building the store???" (Q-F-0004) ‖ OWNED "I invested a lot of my money into buying this business" (Q-O-0004) · "It won't let me get on live at all" (Q-O-0014) · "I had a Zoom meeting with somebody the other day" (Q-O-0023)
- Skepticism (skepticism): MARKET "now I can't access it, contact an administrator which should be me" (Q-F-0001) · "he's a scam, I was told he doesn't work with Shopify" (Q-F-0003) · "you know, the pitch is almost always the same" (Q-Y-0004) ‖ OWNED "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002) · "I need to just trust the supplier that everything ... is a trusted supplier" (Q-O-0003) · "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006)
- Urgency (trigger): MARKET "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015) · "Time intensive early on (i work a full time job right now)" (Q-F-0016) · "trying to scale my business while keeping my full-time job" (Q-F-0017) ‖ OWNED "I just got out of prison for seven years" (Q-O-0010) · "I still haven't got a job with over 700 applications" (Q-O-0065) · "The AI is getting too fast. Too crazy" (Q-O-0079)
- Relief (emotion:relief): MARKET "After weeks of overthinking, I finally committed" (Q-Y-0053) ‖ OWNED NULL
- Desired future (deeper_hope): MARKET "No wonder people give up" (Q-F-0014) · "fully Outsource my whole Drop Shipping Store" (Q-Y-0007) · "so you can watch me either make money or lose money" (Q-Y-0010) ‖ OWNED "build a a income that I can sit back and relax" (Q-O-0015) · "I was gonna buy an electric bike with this money" (Q-O-0037) · "he used to say, man, cherish this time" (Q-O-0041)
- Relationships (keyword wife/husband/kids/children/son/daughter/family): 13 records — "I'm in a parking lot, and I'm gonna pick up my son" (Q-O-0017) · "I need to talk to my husband about it" (Q-O-0018) · "Almost everything I paid, and now it's very expensive" (Q-O-0021) · "I don't have a job at the moment, so I'm using my my wife's income" (Q-O-0033) · "I do have a girlfriend. I have four children" (Q-O-0059)

**METAPHORS + sensory language:** "tons of links that are like a snowstorm of information" (Q-F-0006) · "throwing cash off a cliff" (Q-Y-0048) · "They promised the moon, but ... they do not deliver" (Q-E-0008) · "it isn't all sunshine and rainbows" (Q-Y-0025) · "हम इनफॉरमेशन के बकरी रहते हैं" (Q-Y-0061) (Q-Y-0061 Hindi, original kept).
**TRANSFORMATION SENTENCES** (before→after in their own words): "I was afraid to ever try again, but eventually I did" (Q-B-0004) · "After weeks of overthinking, I finally committed" (Q-Y-0053) · "turn this side hustle into a main job" (Q-O-0105) · "I'm actually thinking to, you know, replace my job" (Q-O-0053)
**HOOK LIST** = the TOP 50 above (verbatim candidates only; no copy written here).

## §3 · FAILED-SOLUTIONS MAP (FS-##) — most-used first; OWNED_PROOF ledger beside MARKET_VOC

### FS-01 · Own DIY store (Shopify/Wix/Etsy/dropshipping) that got no sales · primary PB-06
- ledgers: MARKET_VOC: obs 23 · units 16 · authors 16 · threads 16 · platforms 4 → VALIDATED ‖ OWNED_PROOF: obs 9 · units 9 · authors 9 · threads 9 · platforms 1 → SUPPORTED ‖ TOTAL: obs 32 · units 25 · authors 25 · threads 25 · platforms 5 → VALIDATED
- why it made sense: wanted to get started quickly / thought it was the route (Q-F-0018, Q-Y-0045) · hope before trying: make money online (Q-Y-0040) · expected vs actual: sales vs 'not one product' (Q-Y-0046); 'still no sales' (Q-F-0019) · practical failure: traffic without conversion (Q-F-0022); money on hold (Q-Y-0042)
- emotional residue [D] from tagged records: skepticism 0 · fear 2 · horror_story 2 · almost_stopped 2
- internal dialogue / disappointment language — MARKET: "i've already lost 500 drop shipping" (Q-Y-0013) · "i got zero sales which means i lost 254 dollars" (Q-Y-0014) · "lost 40k in total, and almost had zero results" (Q-Y-0017) ‖ OWNED: "I picked the baby store. It just didn't work" (Q-O-0082) · "I have one of the Wix Wix store" (Q-O-0092) · "I had one before. I just ended it because I was dealing with a lot" (Q-O-0097)
- what they blame: the strategy / gurus / customers (Q-Y-0018, Q-Y-0044) · solution_status mix: {'TRIED-FAILED': 24, 'STOPPED-SIDE-EFFECTS': 1, 'NULL': 1, 'TRIED-UNCLEAR': 5, 'TRIED-HELPED-THEN-RETURNED': 1} — SAMPLE(32) · hardest moment: "pure loss of money of time of energy of honestly hope" (Q-Y-0047) · emotional_load [D]: High · price paid (spend-tagged): "i've already lost 500 drop shipping" (Q-Y-0013) · "i got zero sales which means i lost 254 dollars" (Q-Y-0014) · "lost 40k in total, and almost had zero results" (Q-Y-0017) · "I've lost about $1,000 in total across three stores" (Q-Y-0023)
### FS-02 · Paid a done-for-you builder / agency / vendor that under-delivered · primary PB-01
- ledgers: MARKET_VOC: obs 9 · units 6 · authors 8 · threads 6 · platforms 3 → VALIDATED ‖ PRODUCT_TRUTH: obs 5 · units 2 · authors 5 · threads 2 · platforms 1 → SUPPORTED ‖ OWNED_PROOF: obs 4 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED ‖ TOTAL: obs 18 · units 12 · authors 17 · threads 12 · platforms 5 → VALIDATED
- why it made sense: 'why not pay Shopify expert to create my very own store' (Q-Y-0001) · hope before trying: a finished store (Q-F-0005) · expected vs actual: 'they said they would build a store, but i am building the store???' (Q-F-0004) · practical failure: half-done store (Q-F-0002), locked out (Q-F-0001)
- emotional residue [D] from tagged records: skepticism 5 · fear 2 · horror_story 4 · almost_stopped 0
- internal dialogue / disappointment language — MARKET: "now I can't access it, contact an administrator which should be me" (Q-F-0001) · "your store is half-ass done" (Q-F-0002) · "they said they would build a store, but i am building the store???" (Q-F-0004) ‖ OWNED: "my store didn't even make $20, so I had to come out" (Q-O-0101) · "I gave somebody $4,500, and they took my money" (Q-O-0062) · "I invested a lot of my money into buying this business" (Q-O-0004)
- what they blame: the vendor (Q-E-0006, Q-E-0007) · solution_status mix: {'TRIED-FAILED': 15, 'TRIED-UNCLEAR': 1, 'STOPPED-SIDE-EFFECTS': 1, 'TRIED-HELPED-THEN-RETURNED': 1} — SAMPLE(18) · hardest moment: "They stole $20,000 and have lied to me repeatedly" (Q-E-0006) · emotional_load [D]: High · price paid (spend-tagged): "I had someone build a shopify store for me because I wanted to get started quickly" (Q-F-0018) · "They stole $20,000 and have lied to me repeatedly" (Q-E-0006) · "they are not to be trusted with your money" (Q-E-0007) · "They promised the moon, but ... they do not deliver" (Q-E-0008)
### FS-05 · Teaching myself the platform (help docs, YouTube, support chats) · primary PB-01
- ledgers: MARKET_VOC: obs 8 · units 2 · authors 6 · threads 2 · platforms 2 → SUPPORTED ‖ OWNED_PROOF: obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED ‖ TOTAL: obs 11 · units 5 · authors 9 · threads 5 · platforms 3 → VALIDATED
- why it made sense: free and self-paced [D] · hope before trying: a simple step by step (Q-F-0012) · expected vs actual: '10 weeks on simple tasks' (Q-F-0013) · practical failure: 'snowstorm of information' (Q-F-0006); can't get live (Q-O-0014)
- emotional residue [D] from tagged records: skepticism 0 · fear 0 · horror_story 1 · almost_stopped 1
- internal dialogue / disappointment language — MARKET: "tons of links that are like a snowstorm of information" (Q-F-0006) · "How can I give you a SPECIFIC question" (Q-F-0007) · "you have to scramble around looking for youtube videos" (Q-F-0008) ‖ OWNED: "It won't let me get on live at all" (Q-O-0014) · "I've not been able to figure out like, what's gonna be the best platform" (Q-O-0049) · "I don't know what to do. This is not working for me" (Q-O-0077)
- what they blame: the platform's support (Q-F-0011) · solution_status mix: {'TRIED-FAILED': 5, 'NULL': 4, 'STOPPED-SIDE-EFFECTS': 1, 'CONSIDERING': 1} — SAMPLE(11) · hardest moment: "No wonder people give up" (Q-F-0014) · emotional_load [D]: Moderate · price paid (spend-tagged): "you have to scramble around looking for youtube videos" (Q-F-0008)
### FS-04 · Trading / crypto / online-investment schemes · primary PB-03
- ledgers: MARKET_VOC: 0 ‖ OWNED_PROOF: obs 5 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED ‖ TOTAL: obs 5 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED
- why it made sense: NULL — not stated · hope before trying: NULL — not stated · expected vs actual: 'It didn't work.' (Q-O-0110) · practical failure: lost money (Q-O-0148)
- emotional residue [D] from tagged records: skepticism 2 · fear 2 · horror_story 0 · almost_stopped 0
- internal dialogue / disappointment language — MARKET: NULL ‖ OWNED: "I tried to get into this trading stuff. It didn't work." (Q-O-0110) · "Most of the trading done online regarding cryptocurrency, most of them are scams." (Q-O-0147) · "I was involved in a cryptocurrency scam, so I've lost a lot of money in that." (Q-O-0148)
- what they blame: scammers (Q-O-0147) · solution_status mix: {'TRIED-FAILED': 5} — SAMPLE(5) · hardest moment: "I was involved in a cryptocurrency scam, so I've lost a lot of money in that." (Q-O-0148) · emotional_load [D]: Moderate · price paid (spend-tagged): "I was involved in a cryptocurrency scam, so I've lost a lot of money in that." (Q-O-0148) · "these fucking Americans ... won a $170,000 from me" (Q-O-0011)
### FS-06 · Suppliers / fulfilment partners · primary PB-05
- ledgers: MARKET_VOC: obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 4 · units 4 · authors 4 · threads 4 · platforms 3 → VALIDATED
- why it made sense: NULL — not stated · hope before trying: NULL — not stated · expected vs actual: 'I didn't find good suppliers' (Q-Y-0063) · practical failure: misdeliveries and pricing errors (Q-F-0034)
- emotional residue [D] from tagged records: skepticism 0 · fear 1 · horror_story 1 · almost_stopped 0
- internal dialogue / disappointment language — MARKET: "I didn't find good suppliers, that was the main problem" (Q-Y-0063) · "got sick of misdeliveries and errors in pricing" (Q-F-0034) · "that money is instantly going on hold" (Q-Y-0042) ‖ OWNED: "I'm a computer consultant and I have very little time." (Q-O-0154)
- what they blame: suppliers / payment holds (Q-Y-0042) · solution_status mix: {'TRIED-FAILED': 3, 'TRIED-HELPED-THEN-RETURNED': 1} — SAMPLE(4) · hardest moment: "got sick of misdeliveries and errors in pricing" (Q-F-0034) · emotional_load [D]: Moderate · price paid (spend-tagged): NULL
### FS-03 · Paid course / coach / mentorship / challenge · primary PB-06
- ledgers: MARKET_VOC: obs 4 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ OWNED_PROOF: obs 2 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 6 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED
- why it made sense: 'I've just paid $10,000 for this one-on-one mentorship' (Q-Y-0020) · hope before trying: NULL — not stated · expected vs actual: 'this coach never even scheduled a call with me' (Q-Y-0019) · practical failure: expelled from community (Q-Y-0021)
- emotional residue [D] from tagged records: skepticism 3 · fear 0 · horror_story 1 · almost_stopped 0
- internal dialogue / disappointment language — MARKET: "i failed the challenge" (Q-Y-0015) · "this coach never even scheduled a call with me" (Q-Y-0019) · "i've just paid $10,000 for this one-on-one mentorship" (Q-Y-0020) ‖ OWNED: "I got scammed by the marketing guy." (Q-O-0130) · "They just lost a thousand pounds." (Q-O-0131)
- what they blame: the coach / 'marketing guy' (Q-Y-0019, Q-O-0130) · solution_status mix: {'TRIED-FAILED': 6} — SAMPLE(6) · hardest moment: "he pretty much kicked me out the community" (Q-Y-0021) · emotional_load [D]: High · price paid (spend-tagged): "i've just paid $10,000 for this one-on-one mentorship" (Q-Y-0020) · "he pretty much kicked me out the community" (Q-Y-0021) · "I got scammed by the marketing guy." (Q-O-0130) · "They just lost a thousand pounds." (Q-O-0131)

**FS available per PB:** PB-01: 3 · PB-06: 5 · PB-05: 2 · PB-02: 1 · PB-03: 3 · PB-04: 1 · PB-07: 0

## §4 · DESIRES — RESERVED (08 synthesizes)

- MARKET_VOC: 15 records exported raw (desire/deeper_hope/if_only/micro_dream) — Q-F-0005 Q-F-0014 Q-Y-0001 Q-Y-0003 Q-Y-0007 Q-F-0015 Q-F-0018 Q-Y-0010 Q-Y-0027 Q-Y-0038 Q-Y-0040 Q-Y-0050 Q-B-0004 Q-Y-0056 Q-Y-0064
- PRODUCT_TRUTH: 5 records exported raw (desire/deeper_hope/if_only/micro_dream) — Q-E-0001 Q-E-0002 Q-E-0003 Q-E-0004 Q-E-0005
- OWNED_PROOF: 36 records exported raw (desire/deeper_hope/if_only/micro_dream) — Q-O-0001 Q-O-0008 Q-O-0009 Q-O-0015 Q-O-0024 Q-O-0027 Q-O-0037 Q-O-0041 Q-O-0044 Q-O-0046 Q-O-0053 Q-O-0056 Q-O-0058 Q-O-0087 Q-O-0095 Q-O-0096 Q-O-0105 Q-O-0107 Q-O-0109 Q-O-0114 Q-O-0115 Q-O-0120 Q-O-0121 Q-O-0123 Q-O-0127 Q-O-0137 Q-O-0141 Q-O-0142 Q-O-0150 Q-O-0152 Q-O-0160 Q-O-0162 Q-O-0174 Q-O-0175 Q-O-0176 Q-O-0180
No desire ranking, no LF8 root, no synthesis here.

## §5 · MISCONCEPTIONS + BELIEF MAP (MC-##)

| mc_id | believe | true: | usable | ledgers MARKET_VOC ‖ OWNED_PROOF ‖ TOTAL | MARKET quotes | OWNED quotes |
|---|---|---|---|---|---|---|
| MC-01 | Online selling is (sold as) easy money | PT-09 (seller: 'Results are not typical and are not guaranteed') | RECOGNISE-ONLY | MARKET_VOC: obs 3 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ OWNED_PROOF: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 4 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED | "make it seem like easy money when it's really not" (Q-Y-0016) · "it isn't all sunshine and rainbows" (Q-Y-0025) | "Visibility and the fact that it works twenty four seven." (Q-O-0162) |
| MC-02 | A done-for-you service can fully automate it / make it hands-free | PT-05 + PT-08 (ad spend/product costs excluded; management level agreed per call) | CORRECT-IN-COPY | MARKET_VOC: 0 ‖ PRODUCT_TRUTH: obs 2 · units 1 · authors 2 · threads 1 · platforms 1 → EARLY SIGNAL ‖ OWNED_PROOF: obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED ‖ TOTAL: obs 5 · units 4 · authors 5 · threads 4 · platforms 2 → VALIDATED | NULL | "You guys can fully automate my online business" (Q-O-0001) · "I don't wanna be trained to do it" (Q-O-0056) |
| MC-03 | I can reach $10k+/month (or a million) fast | PT-05 / PT-09 (no income guarantee; results not typical) | CORRECT-IN-COPY | MARKET_VOC: 0 ‖ OWNED_PROOF: obs 6 · units 5 · authors 5 · threads 5 · platforms 1 → SUPPORTED ‖ TOTAL: obs 6 · units 5 · authors 5 · threads 5 · platforms 1 → SUPPORTED | NULL | "Could I get up to at least $10,000 a month in three months" (Q-O-0008) · "would I at least have $50,000 worth of money" (Q-O-0009) |
| MC-04 | Traffic / marketing, not the store, is where people fail | PT-05 (ad spend excluded from the $500 package) | CORRECT-IN-COPY | MARKET_VOC: obs 3 · units 2 · authors 3 · threads 2 · platforms 2 → SUPPORTED ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 5 · units 4 · authors 5 · threads 4 · platforms 3 → VALIDATED | "getting profitable traffic is where 90% of beginners fail" (Q-Y-0008) · "it will be hard to convert a random social media visitor" (Q-F-0023) | "My problem is again, a marketing and visibility" (Q-O-0089) · "The marketing was the one bringing in the money, but it's slowed down so much." (Q-O-0124) |
| MC-05 | Most online opportunities are scams | NULL (PT-16 = low automated trust scores, non-buyer) | RECOGNISE-ONLY | MARKET_VOC: obs 3 · units 2 · authors 3 · threads 2 · platforms 2 → SUPPORTED ‖ PRODUCT_TRUTH: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 6 · units 5 · authors 6 · threads 5 · platforms 4 → VALIDATED | "यह एक स्कैम ही है" (Q-Y-0052) · "there seems to be fake reviews" (Q-Q-0002) | "Most of the trading done online regarding cryptocurrency, most of them are scams." (Q-O-0147) · "with all these fucking scams ... stop fucking calling me" (Q-O-0012) |
| MC-06 | The winning product is the key (and the hard part) | NULL | RECOGNISE-ONLY | MARKET_VOC: obs 6 · units 5 · authors 6 · threads 5 · platforms 2 → VALIDATED ‖ OWNED_PROOF: 0 ‖ TOTAL: obs 6 · units 5 · authors 6 · threads 5 · platforms 2 → VALIDATED | "problem of finding winning products is an eyesore" (Q-F-0031) · "it takes years to find a winning product" (Q-Y-0064) | NULL |
| MC-07 | A 7-day refund window protects me | PT-15 (guarantee voids on acceptance or any add-on) | CORRECT-IN-COPY | MARKET_VOC: 0 ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL | NULL | "if it's gonna take fourteen days how can i take back your money in seven" (Q-O-0030) · "seven days is two lesser time. Seven days too. It's not realistic" (Q-O-0047) |

**Belief Map** [D] — dominant explanations for failure: no traffic / marketing (MC-04: Q-Y-0008, Q-O-0089) · wrong product (MC-06: Q-F-0031) · scammers and gurus (MC-05: Q-Y-0018, Q-O-0147). Competing explanations: 'you must do a lot of research yourself' (Q-F-0033) vs 'NUMBERS AND DATA MAKE ALL DECISIONS' (Q-F-0036) vs 'find a product you have a passion for' (Q-F-0035). Contradictions: 'hands-free' praise (Q-E-0005) vs 'they do not deliver' (Q-E-0008) about the same vendor pool. Distrusted explanations: 'make it seem like easy money' (Q-Y-0016); 'the pitch is almost always the same' (Q-Y-0004). Unresolved questions: 'why would someone buy from a new shop' (Q-Y-0054); 'At what point do I take over the store?' (Q-O-0169); 'What would stop me from just doing this?' (Q-O-0068).

**BELIEFS REQUIRED BEFORE TRYING AGAIN** (ledgers MARKET_VOC ‖ OWNED_PROOF ‖ TOTAL):
- BR-01 "my problem can actually improve" — MARKET_VOC: obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED ‖ OWNED_PROOF: 0 ‖ TOTAL: obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED — MARKET "I was afraid to ever try again, but eventually I did" (Q-B-0004) · "don't get too stuck up on failure" (Q-Y-0050) ‖ OWNED NULL
- BR-02 "this could work for someone like me" — MARKET_VOC: 0 ‖ OWNED_PROOF: obs 4 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED ‖ TOTAL: obs 4 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED — MARKET NULL ‖ OWNED "I'm 56. I don't have I'm not in Internet" (Q-O-0076) · "I'm at that age now where a gamble doesn't really frighten you." (Q-O-0181)
- BR-03 "this is not the same thing I already tried" — MARKET_VOC: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ OWNED_PROOF: obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED ‖ TOTAL: obs 4 · units 4 · authors 4 · threads 4 · platforms 2 → VALIDATED — MARKET "you know, the pitch is almost always the same" (Q-Y-0004) ‖ OWNED "I gave somebody $4,500, and they took my money" (Q-O-0062) · "my store didn't even make $20, so I had to come out" (Q-O-0101)
- BR-04 "the effort is worth it" — MARKET_VOC: obs 2 · units 2 · authors 2 · threads 2 · platforms 2 → EARLY SIGNAL ‖ OWNED_PROOF: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 3 · units 3 · authors 3 · threads 3 · platforms 3 → VALIDATED — MARKET "No wonder people give up" (Q-F-0014) · "it's extremely discouraging and it just makes you want to give up" (Q-Y-0031) ‖ OWNED "I don't have the time to do the due diligence" (Q-O-0042)
- BR-05 "I will not have to make an unacceptable sacrifice" — MARKET_VOC: 0 ‖ OWNED_PROOF: obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED ‖ TOTAL: obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED — MARKET NULL ‖ OWNED "I earn good money now, so I don't want to quit and then start struggling." (Q-O-0133) · "I get Social Security, so I need to protect that" (Q-O-0007)
- BR-06 "I am not about to waste money again" — MARKET_VOC: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ PRODUCT_TRUTH: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 4 · units 4 · authors 4 · threads 4 · platforms 3 → VALIDATED — MARKET "I've been burned many times" (Q-Y-0030) ‖ OWNED "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006) · "I need a proof of concept that actually works." (Q-O-0132)
- BR-07 "there is a logical reason this might work" — MARKET_VOC: 0 ‖ OWNED_PROOF: obs 4 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED ‖ TOTAL: obs 4 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED — MARKET NULL ‖ OWNED "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002) · "Just give me a big a figure. That's all I want" (Q-O-0091)

'I believe …' statements: 0 begin with I believe/think/feel — NULL. Upvotes as agreement proxy: `unit_score` NULL on 307/307 records — UNSCANNED (no scrape lane returned votes).

## §6 · OBJECTION TABLE (OBJ-##) — MARKET_VOC and OWNED_PROOF ledgers side by side + outcome co-occurrence

Outcome denominators (OWNED_PROOF calls): {'DEPOSIT': 2, 'DECLINED': 12, 'BOOKED-FOLLOWUP': 56, 'PAID': 2, 'UNKNOWN': 11, 'HUNG-UP': 1} — 84 calls. Co-occurrence counts calls where the objection was voiced, by that call's `call_outcome`; association only, never cause [D].

| obj_id | verbatim (as they said it) | tier | MARKET_VOC ledger | OWNED_PROOF ledger | TOTAL | outcome co-occurrence (calls/denominator) | population_tags[] | answered_by | proof_object_id |
|---|---|---|---|---|---|---|---|---|---|
| OBJ-01 | I don't have the money / it's not the right time financially — "I'm not able to get the funds for it" (Q-O-0016) "people struggle to pay that kind of amount" (Q-Y-0006) | T1 | obs 2 · units 2 · authors 2 · threads 2 · platforms 2 → EARLY SIGNAL | obs 16 · units 14 · authors 14 · threads 14 · platforms 1 → SUPPORTED | obs 18 · units 16 · authors 16 · threads 16 · platforms 3 → VALIDATED | DECLINED/HUNG-UP 6/13 · PAID/DEPOSIT 0/4 · BOOKED-FOLLOWUP 8/56 · UNKNOWN 0/11 | CP-01:1, CP-02:2, CP-03:3, CP-05:5, CP-06:2 | NULL | NULL |
| OBJ-02 | Show me proof / results / a contract before I pay — "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002) "I assume that the followers are fake" (Q-Y-0005) | T1 | obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED | obs 9 · units 8 · authors 8 · threads 8 · platforms 1 → SUPPORTED | obs 12 · units 11 · authors 11 · threads 11 · platforms 3 → VALIDATED | DECLINED/HUNG-UP 3/13 · PAID/DEPOSIT 1/4 · BOOKED-FOLLOWUP 3/56 · UNKNOWN 1/11 | CP-01:1, CP-03:2, CP-04:2, CP-05:2, CP-06:1 | NULL | NULL |
| OBJ-03 | This is (probably) a scam — I've been scammed before — "with all these fucking scams ... stop fucking calling me" (Q-O-0012) "he's a scam, I was told he doesn't work with Shopify" (Q-F-0003) | T1 | obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED | obs 7 · units 7 · authors 6 · threads 7 · platforms 1 → SUPPORTED | obs 12 · units 11 · authors 11 · threads 11 · platforms 4 → VALIDATED | DECLINED/HUNG-UP 2/13 · PAID/DEPOSIT 1/4 · BOOKED-FOLLOWUP 3/56 · UNKNOWN 1/11 | CP-03:7, CP-05:4 | NULL | NULL |
| OBJ-04 | $500 is only the start — hidden / further costs — "I pay $500 and then I'm gonna have to pay more money down the road" (Q-O-0028) "promises of more templates, ads, products etc. after you have paid" (Q-B-0001) | T1 | obs 3 · units 3 · authors 3 · threads 3 · platforms 3 → VALIDATED | obs 6 · units 6 · authors 5 · threads 6 · platforms 1 → SUPPORTED | obs 10 · units 10 · authors 9 · threads 10 · platforms 5 → VALIDATED | DECLINED/HUNG-UP 1/13 · PAID/DEPOSIT 0/4 · BOOKED-FOLLOWUP 5/56 · UNKNOWN 0/11 | CP-01:1, CP-04:2, CP-05:3 | NULL | NULL |
| OBJ-05 | I need to talk to my spouse / think / call me back — "I need to talk to my husband about it" (Q-O-0018)  | T2 | 0 | obs 7 · units 7 · authors 7 · threads 7 · platforms 1 → SUPPORTED | obs 7 · units 7 · authors 7 · threads 7 · platforms 1 → SUPPORTED | DECLINED/HUNG-UP 1/13 · PAID/DEPOSIT 0/4 · BOOKED-FOLLOWUP 6/56 · UNKNOWN 0/11 | CP-02:1, CP-03:1, CP-05:2, CP-07:1 | NULL | NULL |
| OBJ-06 | I don't have the time — "I don't have the time to do the due diligence" (Q-O-0042) "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015) | T2 | obs 3 · units 1 · authors 3 · threads 3 · platforms 1 → SUPPORTED | obs 4 · units 4 · authors 4 · threads 4 · platforms 1 → SUPPORTED | obs 7 · units 5 · authors 7 · threads 7 · platforms 2 → VALIDATED | DECLINED/HUNG-UP 2/13 · PAID/DEPOSIT 0/4 · BOOKED-FOLLOWUP 1/56 · UNKNOWN 1/11 | CP-01:3, CP-02:1, CP-04:1, CP-06:1 | NULL | NULL |
| OBJ-07 | How fast / how much will it make — what is guaranteed — "Could I get up to at least $10,000 a month in three months" (Q-O-0008) "getting profitable traffic is where 90% of beginners fail" (Q-Y-0008) | T1 | obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED | obs 9 · units 7 · authors 7 · threads 7 · platforms 1 → SUPPORTED | obs 12 · units 10 · authors 10 · threads 10 · platforms 3 → VALIDATED | DECLINED/HUNG-UP 1/13 · PAID/DEPOSIT 1/4 · BOOKED-FOLLOWUP 5/56 · UNKNOWN 0/11 | CP-01:3, CP-04:1, CP-05:3 | NULL | NULL |
| OBJ-08 | Done-for-you vendors don't deliver — I end up doing it myself — "my store didn't even make $20, so I had to come out" (Q-O-0101) "now I can't access it, contact an administrator which should be me" (Q-F-0001) | T2 | obs 7 · units 5 · authors 7 · threads 5 · platforms 2 → VALIDATED | obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL | obs 10 · units 8 · authors 10 · threads 8 · platforms 4 → VALIDATED | DECLINED/HUNG-UP 1/13 · PAID/DEPOSIT 0/4 · BOOKED-FOLLOWUP 1/56 · UNKNOWN 0/11 | CP-01:1, CP-03:3, CP-05:8 | NULL | NULL |
| OBJ-09 | I won't market myself / show my face — visibility is my problem — "I don't really like showing my face on social media" (Q-O-0035)  | T3 | 0 | obs 2 · units 2 · authors 1 · threads 2 · platforms 1 → HYPOTHESIS (ANECDOTE) | obs 2 · units 2 · authors 1 · threads 2 · platforms 1 → HYPOTHESIS (ANECDOTE) | DECLINED/HUNG-UP 0/13 · PAID/DEPOSIT 0/4 · BOOKED-FOLLOWUP 1/56 · UNKNOWN 1/11 | CP-03:2 | NULL | NULL |
| OBJ-10 | Stop calling me / don't repeat yourself — "with all these fucking scams ... stop fucking calling me" (Q-O-0012)  | T3 | 0 | obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED | obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED | DECLINED/HUNG-UP 1/13 · PAID/DEPOSIT 1/4 · BOOKED-FOLLOWUP 1/56 · UNKNOWN 0/11 | CP-03:1 | NULL | NULL |
| OBJ-11 | I won't risk my job / benefits / family money — "I get Social Security, so I need to protect that" (Q-O-0007)  | T2 | 0 | obs 4 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED | obs 4 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED | DECLINED/HUNG-UP 1/13 · PAID/DEPOSIT 0/4 · BOOKED-FOLLOWUP 2/56 · UNKNOWN 0/11 | CP-01:2, CP-02:1, CP-07:1 | NULL | NULL |

All members per objection: OBJ-01: Q-O-0016 Q-O-0022 Q-O-0025 Q-O-0051 Q-O-0060 Q-O-0063 Q-O-0071 Q-O-0075 Q-O-0083 Q-O-0098 Q-O-0149 Q-O-0156 Q-O-0157 Q-O-0158 Q-O-0177 Q-O-0021 Q-Y-0006 Q-Q-0005 ‖ OBJ-02: Q-O-0002 Q-O-0006 Q-O-0055 Q-O-0081 Q-O-0102 Q-O-0116 Q-O-0118 Q-O-0132 Q-O-0178 Q-Y-0005 Q-Y-0032 Q-Q-0002 ‖ OBJ-03: Q-O-0012 Q-O-0062 Q-O-0073 Q-O-0100 Q-O-0144 Q-O-0147 Q-O-0011 Q-F-0003 Q-Y-0052 Q-E-0006 Q-E-0007 Q-Y-0016 ‖ OBJ-04: Q-O-0028 Q-O-0048 Q-O-0104 Q-O-0112 Q-O-0135 Q-O-0155 Q-B-0001 Q-Y-0009 Q-E-0010 Q-F-0020 ‖ OBJ-05: Q-O-0018 Q-O-0026 Q-O-0052 Q-O-0064 Q-O-0113 Q-O-0170 Q-O-0173 ‖ OBJ-06: Q-O-0042 Q-O-0090 Q-O-0143 Q-O-0154 Q-F-0015 Q-F-0016 Q-F-0017 ‖ OBJ-07: Q-O-0008 Q-O-0009 Q-O-0027 Q-O-0030 Q-O-0047 Q-O-0091 Q-O-0117 Q-O-0139 Q-O-0140 Q-Y-0008 Q-F-0023 Q-Y-0054 ‖ OBJ-08: Q-F-0001 Q-F-0002 Q-F-0004 Q-F-0005 Q-F-0018 Q-Y-0019 Q-Y-0035 Q-E-0008 Q-O-0101 Q-O-0094 ‖ OBJ-09: Q-O-0035 Q-O-0089 ‖ OBJ-10: Q-O-0012 Q-O-0138 Q-O-0165 ‖ OBJ-11: Q-O-0007 Q-O-0133 Q-O-0040 Q-O-0134

## §6b · ANTI-DESIRES (AD-##)

- AD-01 "I want income, but I will not quit my job and start struggling" — MARKET_VOC: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ OWNED_PROOF: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 2 · units 2 · authors 2 · threads 2 · platforms 2 → EARLY SIGNAL — "I earn good money now, so I don't want to quit and then start struggling." (Q-O-0133) · "Time intensive early on (i work a full time job right now)" (Q-F-0016)
- AD-02 "I want a business, but I will not risk my Social Security / benefits" — MARKET_VOC: 0 ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL — "I get Social Security, so I need to protect that" (Q-O-0007) · "I'm busy paying off my debts. I'm on government benefits as well." (Q-O-0149)
- AD-03 "I want a store, but I will not be trained / build it myself" — MARKET_VOC: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED — "I don't wanna be trained to do it" (Q-O-0056) · "I would just link into the store once it is finished" (Q-F-0005) · "You guys can fully automate my online business" (Q-O-0001)
- AD-04 "I want it, but I will not pay until I see results" — MARKET_VOC: 0 ‖ OWNED_PROOF: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL — "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006) · "I need a proof of concept that actually works." (Q-O-0132)
- AD-05 "I want to sell online, but I will not show my face on social media" — MARKET_VOC: 0 ‖ OWNED_PROOF: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) — "I don't really like showing my face on social media" (Q-O-0035)
- AD-06 "I want the store, but I will not mix it with my other business" — MARKET_VOC: 0 ‖ OWNED_PROOF: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) — "I don't need to mix the other business with my own" (Q-O-0045)

## §7 · SKEPTICISM BANK (SK-##)

| sk_id | reason | kind | MARKET_VOC ledger | OWNED_PROOF ledger | speaker_stage mix | phrases |
|---|---|---|---|---|---|---|
| SK-01 | wasted money | emotional | obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) | obs 3 · units 3 · authors 3 · threads 3 · platforms 1 → SUPPORTED | {'dissatisfied': 3, 'veteran': 1, 'seeker': 1} | "I gave somebody $4,500, and they took my money" (Q-O-0062) · "they are not to be trusted with your money" (Q-E-0007) · "I've been burned many times" (Q-Y-0030) |
| SK-02 | too many promises | logical | obs 4 · units 4 · authors 4 · threads 4 · platforms 2 → VALIDATED | 0 | {'dissatisfied': 1, 'seeker': 1, 'NULL': 2, 'veteran': 1} | "They promised the moon, but ... they do not deliver" (Q-E-0008) · "make it seem like easy money when it's really not" (Q-Y-0016) · "promises of more templates, ads, products etc. after you have paid" (Q-B-0001) |
| SK-03 | recommender exaggerates (fake reviews / followers / unlabelled proof) | logical | obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED | obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) | {'NULL': 1, 'veteran': 1, 'unknown': 2} | "I assume that the followers are fake" (Q-Y-0005) · "a lot of them fake the reviews" (Q-Y-0032) · "there seems to be fake reviews" (Q-Q-0002) |
| SK-04 | tried too many | emotional | obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) | obs 2 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL | {'veteran': 2, 'seeker': 1} | "I've been burned many times" (Q-Y-0030) · "I tried to get into this trading stuff. It didn't work." (Q-O-0110) · "Most of the trading done online regarding cryptocurrency, most of them are scams." (Q-O-0147) |
| SK-05 | is this company even real (legitimacy) | logical | 0 | obs 6 · units 6 · authors 6 · threads 6 · platforms 1 → SUPPORTED | {'seeker': 5, 'passive': 1} | "send me something to make me understand that you are legitimate" (Q-O-0055) · "How do I know you're real?" (Q-O-0081) · "Have you tried to reach this number back when you see it or it doesn't show anything?" (Q-O-0119) |
| SK-06 | the price is a low anchor (hidden costs) | logical | 0 | obs 5 · units 5 · authors 5 · threads 5 · platforms 1 → SUPPORTED | {'seeker': 3, 'dissatisfied': 1, 'unknown': 1} | "I pay $500 and then I'm gonna have to pay more money down the road" (Q-O-0028) · "After paying $500, I should be paying £1 every month. You didn't tell me that earlier." (Q-O-0135) · "Is it $500 it's starting from, and it goes up to $5,000 or what?" (Q-O-0155) |

tired_of_hearing (7): MARKET "I would just link into the store once it is finished" (Q-F-0005) · "make it seem like easy money when it's really not" (Q-Y-0016) · "it isn't all sunshine and rainbows" (Q-Y-0025) · "I am growing tired of looking at all the traffic and no sales" (Q-F-0022) ‖ OWNED "with all these fucking scams ... stop fucking calling me" (Q-O-0012) · "I don't want to trade on your platform at the moment, because I am trading." (Q-O-0138) · "Next time you repeat yourself, I'm going to cut off." (Q-O-0165). Distrusted explanations: Q-Y-0016, Q-Y-0004. Self-protective narratives [D]: 'I'm not going to let perfection slow me down' (Q-Y-0057); 'I'm at that age now where a gamble doesn't really frighten you' (Q-O-0181); 'I earn good money now, so I don't want to quit' (Q-O-0133).

## §8 · TRUST SIGNALS + AUTHORITY READ

- **Who they trust** — MARKET: a peer's shown reality 'this is like the reality of what it is' (Q-Y-0024); peers over gurus 'take what I say with a grain of salt' (Q-Y-0039) ‖ OWNED: a friend already selling online (Q-O-0137, Q-O-0166); Google reviews (Q-O-0102); a contract (Q-O-0116); 'a trusted supplier' (Q-O-0003).
- **Proof they demand** — MARKET: real reviews, not fake ones (Q-Y-0032, Q-Q-0002), real followers (Q-Y-0005) ‖ OWNED: results before paying (Q-O-0006), 'a proof of concept that actually works' (Q-O-0132), 'send me something to make me understand that you are legitimate' (Q-O-0055), 'How do I know you're real?' (Q-O-0081), who the video is from (Q-O-0178), whether the calling number is real (Q-O-0119).
- **Do they trust experts here, or resent them?** [D] Resent: coaches/gurus are named as the enemy in MARKET_VOC ('the strategy was dead, and no one told me' Q-Y-0018; 'this coach never even scheduled a call with me' Q-Y-0019; 'a lot of them fake the reviews' Q-Y-0032). In OWNED_PROOF the resentment points at callers and scams (Q-O-0012, Q-O-0165). No expert or study is filed (C-#### expert records = rep pitch only). authority_read: RESENT — MARKET_VOC SUPPORTED (≥3 authors), OWNED_PROOF SUPPORTED.

## §9 · PRICE-SENSITIVITY MAP — wallet quotes with amounts (MARKET_VOC ‖ OWNED_PROOF) + the operator's CURRENT offer as reps state it (C-####, contextual)

**MARKET_VOC — 15 wallet quotes with an amount** (persons 11):
- "we ended up losing 1,646 dollars" (Q-Y-0002)
- "people struggle to pay that kind of amount" (Q-Y-0006)
- "a clever Shopify affiliate funnel with a big upsell" (Q-Y-0009)
- "promises of more templates, ads, products etc. after you have paid" (Q-B-0001)
- "i've already lost 500 drop shipping" (Q-Y-0013)
- "i got zero sales which means i lost 254 dollars" (Q-Y-0014)
- "lost 40k in total, and almost had zero results" (Q-Y-0017)
- "i've just paid $10,000 for this one-on-one mentorship" (Q-Y-0020)
- "he pretty much kicked me out the community" (Q-Y-0021)
- "I've lost about $1,000 in total across three stores" (Q-Y-0023)
- "how I lost a million dollars with my Drop Shipping business" (Q-Y-0033)
- "I lost anywhere between like $500 and $11,000 every single day" (Q-Y-0036)
- "still no sales. i've got ~600 clicks" (Q-F-0019)
- "मुझे ₹50,000 की पड़ी" (Q-Y-0051)
- "My capital is 500 cedis" (Q-Q-0005)
**PRODUCT_TRUTH — 3 wallet quotes with an amount** (persons 3):
- "They stole $20,000 and have lied to me repeatedly" (Q-E-0006)
- "I had over $2000 worth of inventory" (Q-E-0009)
- "paid $69 and an additional $169... not one sale" (Q-E-0010)
**OWNED_PROOF — 17 wallet quotes with an amount** (persons 14):
- "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006)
- "these fucking Americans ... won a $170,000 from me" (Q-O-0011)
- "I pay $500 and then I'm gonna have to pay more money down the road" (Q-O-0028)
- "I don't have a job at the moment, so I'm using my my wife's income" (Q-O-0033)
- "sometimes 14 thousand 14 k sometimes 10 k" (Q-O-0043)
- "I'm just worried about the total cost" (Q-O-0048)
- "how much is it? Is it 500 investment? 200 investment?" (Q-O-0057)
- "I gave somebody $4,500, and they took my money" (Q-O-0062)
- "I owe a $180,000 after doing seven years in prison" (Q-O-0066)
- "they want $2,800 for me to just get it out of there" (Q-O-0067)
- "It's not easy to get $500, especially with other bills" (Q-O-0083)
- "I don't know that I would have the full 500 right away" (Q-O-0098)
- "at an exorbitant cost, $5,000, $20,000, $15,000" (Q-O-0104)
- "My store was nearly about 10,000 pounds, and that is before me paying the money to open properly." (Q-O-0127)
- "After paying $500, I should be paying £1 every month. You didn't tell me that earlier." (Q-O-0135)
- "Take-home pay would be around $2,500." (Q-O-0150)
- "Is it $500 it's starting from, and it goes up to $5,000 or what?" (Q-O-0155)

**Spend now vs worth-if-proven** (OWNED_PROOF): can't/won't now — OBJ-01 ledger in §6 (Q-O-0016, Q-O-0071, Q-O-0157) ‖ worth-if-proven — 'I would not pay $2,500 to anybody unless I could see some results' (Q-O-0006); 'I'll start with the 500, and then I'll hopefully graduate to the next level' (Q-O-0029); 'I need a proof of concept that actually works' (Q-O-0132). Prior spend ceilings stated: $4,500 lost (Q-O-0062); DFY quotes '$5,000, $20,000, $15,000' (Q-O-0104); '£1,000' (Q-O-0131). MARKET_VOC: '$10,000 for this one-on-one mentorship' (Q-Y-0020); '$69 and an additional $169' (Q-E-0010, PRODUCT_TRUTH).

**CURRENT OFFER as the reps state it** (C-####, never VOC; recurrence = calls pattern-matched by the harvesters):
- "to get started, is only 500 US dollar" (C-0001; 61 of 155 calls)
- "You can get in on this with $500, which is like 375 quid." (C-0019; ~10+ calls read)
- "Start small. 375 pounds is something you can do." (C-0023; ~10+ calls read)
- "the gateway ... you pay $500 for one time it creates one store" (C-0011; 2 of 155 calls)
- "you do have a seven day money back guarantee" (C-0002; 17 of 155 calls)
- "we find three products from our researching team" (C-0003; 25 of 155 calls)
- "we build it for you. We find the pro[duct]" (C-0004; 50 of 155 calls)
- "we find the pro[duct], the supplier" (C-0014; 43 of 155 calls)
- "we can run ads for your shop as well" (C-0013; 39 of 155 calls)
- "you're gonna always have a personal assigned account manager" (C-0007; 4 of 155 calls)
- "Do you have credit on your credit card?" (C-0006; 15 of 155 calls)
- "clients that have done the $500 ... graduated immediately in one day, two days" (C-0016; 2 of 155 calls)
- "Our goal is for every shop to make at least $10,000 in 6 months." (C-0020; ~4 calls read)
- "We will build the online store from our site, and we will get it ready in seven after ten days." (C-0022; ~12+ calls read)
- "We build around your legal property, your own. You are the sole legal owner." (C-0018; ~6+ calls read)
- "We will design it for you ... but it is yours" (C-0010; 9 of 155 calls)
- "We give you digital training and no experience required" (C-0012; 5 of 155 calls)
- "If you don't go to the website within this minute, I'm gonna have to hang up and close this opportunity for you forever." (C-0024; ~3)

FE-price gap: NULL (12 fills it). Owned price reactions to the $500 entry: sticker shock (Q-O-0157) · 'not easy to get $500' (Q-O-0083) · anchor suspicion '$500 it's starting from, and it goes up to $5,000 or what?' (Q-O-0155) · undisclosed recurring platform fee (Q-O-0135, HUNG-UP).

## §10 · CATEGORIZED INSIGHTS

- **Top pain points** (MARKET_VOC ledger order): PP-02 no sales/lost money · PP-03 don't know what to sell · PP-01 can't build it — OWNED_PROOF adds PP-05 job/income, PP-04 burned before, PP-07 retirement money (see §1).
- **Failed solutions:** FS-01 DIY store no sales · FS-02 DFY vendor under-delivered · FS-05 self-teaching the platform · FS-03 courses/coaches · FS-04 trading/crypto (OWNED only) · FS-06 suppliers (§3).
- **Desired outcomes incl. deeper hopes:** reserved (§4, raw ids). **Objections as a Redditor would say it:** 'they said they would build a store, but i am building the store???' (Q-F-0004) · 'They promised the moon, but ... they do not deliver' (Q-E-0008) · 'I would not pay $2,500 to anybody unless I could see some results' (Q-O-0006). **Misconceptions:** MC-01…MC-07 (§5).
- **GOLDEN NUGGETS** — frustration: "I am growing tired of looking at all the traffic and no sales" (Q-F-0022) · skepticism: "make it seem like easy money when it's really not" (Q-Y-0016) · humour: "who do i come to who do i kill for my money" (Q-O-0032) · hopelessness: "pure loss of money of time of energy of honestly hope" (Q-Y-0047) · DIY struggle: "10 weeks on simple tasks that the system doesn't verify" (Q-F-0013)
- **icp_language_analysis** [D]: tone — MARKET: confessional, post-mortem ('how I lost…', Q-Y-0033); OWNED: guarded, transactional, question-led (Q-O-0057, Q-O-0122). emotional_style — resignation + wariness; money named in exact figures. vocabulary — 'no sales', 'winning product', 'scam', 'side hustle', 'the 500', 'legit', 'store'. swap_table below.

**SWAP TABLE** (from swap_table_v0, corpus-checked):

| clinical / market | plain (corpus) | Q-## | hook-grade |
|---|---|---|---|
| managed / done-for-you service | "hands-free" | Q-E-0005 | grade 6 |
| failed prior DIY attempt / sunk cost | "I picked the baby store. It just didn't work" | Q-O-0082 | grade 7.0 |
| vendor trust deficit | "he's a scam" | Q-F-0003 | grade 6 |
| validated product-market fit | "winning product" | Q-F-0028 | grade 4 |
| income replacement | "replace my job" | Q-O-0053 | grade 4.8 |
| zero traffic / zero conversion | "still no sales" | Q-F-0019 | grade 2.5 |
| transferable digital asset | NULL — only rep lines (C-0018) | NULL | NULL |
| ongoing store operations management | "they handle the backend" | Q-E-0003 | grade 6 |

**MEDIA-TERMS** (earliest_fetched_date = earliest date_retrieved in corpus: 2026-09-24): 'dropshipping' 3 records · 'drop shipping' 11 records · 'shopify' 27 records · 'etsy' 6 records · 'winning product' 5 records · 'side hustle' 3 records · 'passive income' 1 records · 'amazon' 4 records

## §11 · PRODUCT MAP (PT-## from 01-DEEP §T3; LF8 ROOT and HANDLING NULL — 08 and 11 fill)

| FEATURE (PT-##) | BENEFIT [D] | DESIRE (corpus wording, Q-##) | LF8 ROOT | PAIN (PP-##) | STRUGGLE (Q-##) | OBJ-## | HANDLING | AVATAR (CP-##) |
|---|---|---|---|---|---|---|---|---|
| PT-01 $500 Store Build & Research Package | a store without building it | "I will like to make a online shop" (Q-O-0024) | NULL | PP-01 | Q-F-0013 | OBJ-01, OBJ-04 | NULL | CP-05 |
| PT-02 managed fee quoted on the call, not published | NULL [D] | NULL | NULL | PP-04 | "I pay $500 and then I'm gonna have to pay more money down the road" (Q-O-0028) | OBJ-04 | NULL | CP-04 |
| PT-04 research + build + listings + staged release + ad testing | product chosen for them | "fully Outsource my whole Drop Shipping Store" (Q-Y-0007) | NULL | PP-03 | Q-F-0040 | OBJ-08 | NULL | CP-05 |
| PT-05 excludes product costs, platform fees, ad spend; no income guarantee | NULL — a limitation | NULL | NULL | PP-02 | Q-Y-0008 | OBJ-04, OBJ-07 | NULL | CP-03 |
| PT-08 ongoing optimisation, level agreed on the call | someone else runs it | "I focus on scaling while they handle the backend" (Q-E-0003, PRODUCT_TRUTH) | NULL | PP-06 | Q-F-0015 | OBJ-06 | NULL | CP-01, CP-04 |
| PT-14 buyer owns a live Shopify/Etsy store, not a course | an asset, not training | "I don't wanna be trained to do it" (Q-O-0056) | NULL | PP-01 | Q-F-0006 | OBJ-08 | NULL | CP-05 |
| PT-15 7-day refund, voided on acceptance / any add-on | NULL — risk reversal is narrow | NULL | NULL | PP-04 | "if it's gonna take fourteen days how can i take back your money in seven" (Q-O-0030) | OBJ-07, OBJ-03 | NULL | CP-03 |

PT-07 (results page renders empty), PT-16 (automated trust scores 0/100, 25%) are not features — they bear on OBJ-02/OBJ-03 and are routed to 11/12.

## §12 · UNAWARE AMMUNITION

**BIG-WIN chains** [D] (feature → benefit → benefit-of-the-benefit → deeper-hope Q-##): (1) PT-04 build+listings → no DIY → evenings back → "turn this side hustle into a main job" (Q-O-0105) · (2) PT-14 own the store → an asset → something for the family → "I have to pay for my student my son college fees" (Q-O-0085) · (3) PT-08 managed → no daily running → steady income → "I'm looking for a steady income" (Q-O-0109)

**Ranked SYMPTOM list by ledger:** "How can I give you a SPECIFIC question" (Q-F-0007) · "grasping things A LOT quicker and easier" (Q-F-0009) · "numerous chats, bots, and emails only wastes time" (Q-F-0011) · "constantly jumping from one idea to another" (Q-Y-0059) · "Do I just choose what I want to sell" (Q-F-0041) · "It won't let me get on live at all" (Q-O-0014) · "I'm 56. I don't have I'm not in Internet" (Q-O-0076) · "I don't know what to do. This is not working for me" (Q-O-0077) — MARKET_VOC: obs 5 · units 3 · authors 5 · threads 3 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 3 · units 2 · authors 2 · threads 2 · platforms 1 → EARLY SIGNAL ‖ TOTAL: obs 8 · units 5 · authors 7 · threads 5 · platforms 3 → VALIDATED

**HIDDEN FEARS** (verbatim): "I might not wake up tomorrow. So who knows?" (Q-O-0084) · "I'm enjoying this. I won't be when I start spending money." (Q-O-0125) · "I get Social Security, so I need to protect that" (Q-O-0007)

**WORLDVIEW MAP** [D]: suspects — fake reviews/followers (Q-Y-0032, Q-Y-0005), callers (Q-O-0119) · blames (tallied enemy_blame targets, 11 records): gurus/coaches/strategy 3 (Q-Y-0016, Q-Y-0018, Q-O-0130→FS-03) · scammers/vendors 5 (Q-E-0006, Q-E-0007, Q-E-0009, Q-O-0011, Q-Y-0052) · customers/shipping 1 (Q-Y-0044) · other 2 · permission — 'I don't need to invent something completely new' (Q-Y-0056); 'a gamble doesn't really frighten you' (Q-O-0181) · validate — 'there's plenty of us losing, including myself' (Q-Y-0027) · flip — 'I was afraid to ever try again, but eventually I did' (Q-B-0004).

## §13 · CORPUS COVERAGE + BIAS

- **MARKET_VOC** by PB: {'PB-01': 31, 'PB-06': 55, 'PB-05': 30} · by CP: {'CP-05': 46, 'NULL': 27, 'CP-01': 4, 'CP-03': 47} · by source_type: {'forum': 41, 'youtube_search': 66, 'blog_comments': 4, 'quora': 5} · by tier: {'[R-PAGE via Exa]': 45, '[R-PAGE]': 12, '[R-SNIPPET]': 5, '[R-SCRAPE]': 54}
- **PRODUCT_TRUTH** by PB: {'PB-01': 10} · by CP: {'CP-05': 10} · by source_type: {'trustpilot': 10} · by tier: {'[R-PAGE via Exa]': 10}
- **OWNED_PROOF** by PB: {'PB-04': 15, 'PB-01': 45, 'PB-03': 31, 'PB-06': 26, 'PB-02': 48, 'PB-05': 17, 'PB-07': 12, 'NULL': 2} · by CP: {'CP-04': 19, 'CP-05': 16, 'CP-03': 33, 'CP-01': 24, 'CP-02': 20, 'CP-07': 2, 'CP-06': 15, 'NULL': 59} · by source_type: {'operator_paste': 181} · by tier: {'[R-OWNED]': 181}
- **TOTAL** by PB: {'PB-01': 86, 'PB-06': 81, 'PB-05': 47, 'PB-04': 15, 'PB-03': 31, 'PB-02': 48, 'PB-07': 12, 'NULL': 2} · by CP: {'CP-05': 72, 'NULL': 86, 'CP-01': 28, 'CP-03': 80, 'CP-04': 19, 'CP-02': 20, 'CP-07': 2, 'CP-06': 15} · by source_type: {'forum': 41, 'trustpilot': 10, 'youtube_search': 66, 'blog_comments': 4, 'quora': 5, 'operator_paste': 181} · by tier: {'[R-PAGE via Exa]': 55, '[R-PAGE]': 12, '[R-SNIPPET]': 5, '[R-SCRAPE]': 54, '[R-OWNED]': 181}

**Usable rate per lane** (source units yielding ≥1 record / units attempted, from the partial handoffs): forum_thread + quora + blog (Exa page lane) and youtube_transcript — PB-01 13 units yielded / 15 attempted · PB-06 18 / 21 · PB-05 13 / 17 · owned_paste US 44 / 46 calls · UK 40 / 40 diarized calls (80 undiarized = BLOCKED-FORMAT). reddit_* 0/0 (0 URLs retrievable) · trustpilot_* 10 records from 1 competitor page via Exa (PB-01) · amazon_*, tiktok_comments, youtube_comments, fb_*, ad_comments: BLOCKED-ON-TOOL / LATE-BOUND.

**Distributions** (SAMPLE(N) per corpus):
- awareness_stage · MARKET_VOC: AW-2 46 · AW-3 38 · AW-4 24 · NULL 8 — SAMPLE(116)
- awareness_stage · OWNED_PROOF: NULL 128 · AW-4 40 · AW-3 9 · AW-5 4 — SAMPLE(181)
- speaker_stage · MARKET_VOC: veteran 33 · seeker 21 · NULL 20 · former 19 · sufferer 10 · dissatisfied 6 · unknown 5 · recent_buyer 2 — SAMPLE(116)
- speaker_stage · OWNED_PROOF: seeker 88 · unknown 42 · sufferer 16 · dissatisfied 14 · passive 8 · recent_buyer 7 · veteran 5 · satisfied 1 — SAMPLE(181)
- evidence_class · MARKET_VOC: VERBATIM_VOC 98 · CUSTOMER_EXPLANATION 16 · REPORTED_OUTCOME 2 — SAMPLE(116)
- evidence_class · OWNED_PROOF: VERBATIM_VOC 163 · REPORTED_OUTCOME 18 — SAMPLE(181)
- solution_status · MARKET_VOC: NULL 54 · TRIED-FAILED 43 · CONSIDERING 8 · STOPPED-SIDE-EFFECTS 5 · TRIED-HELPED-THEN-RETURNED 2 · TRIED-HELPED 2 · TRIED-UNCLEAR 1 · REFUSES 1 — SAMPLE(116)
- solution_status · OWNED_PROOF: NULL 145 · TRIED-FAILED 21 · TRIED-UNCLEAR 9 · CONSIDERING 3 · CURRENTLY-USING 2 · TRIED-HELPED-THEN-RETURNED 1 — SAMPLE(181)

**Bias row:** seeded by problem-language queries, over-weights problem-aware by construction; MARKET_VOC is YouTube-transcript heavy (66/116, creators narrating their own failure = veteran/former over-represented) and has 0 Reddit; OWNED_PROOF is prospects who registered on a Readymerce ad and took a sales call (selection toward AW-3/AW-4 and toward the rep's framing), US read to rank 46/155 by prospect word count (longer talkers over-represented), UK read only where diarized (40/122).

**SATURATION per theme** (beside counts; see 06-VOC-LEDGERS.csv col `saturation`): last-3-units new codes — MARKET_VOC none · OWNED_PROOF none · PRODUCT_TRUTH new (2 units only).
- OBJ-01 MARKET_VOC: 2 obs / 2 authors → EARLY SIGNAL · INSUFFICIENT
- OBJ-01 OWNED_PROOF: 16 obs / 14 authors → SUPPORTED · EARLY SIGNAL
- OBJ-02 MARKET_VOC: 3 obs / 3 authors → VALIDATED · STRONG
- OBJ-02 OWNED_PROOF: 9 obs / 8 authors → SUPPORTED · EARLY SIGNAL
- OBJ-03 MARKET_VOC: 3 obs / 3 authors → VALIDATED · STRONG
- OBJ-03 OWNED_PROOF: 7 obs / 6 authors → SUPPORTED · EARLY SIGNAL
- OBJ-04 MARKET_VOC: 3 obs / 3 authors → VALIDATED · STRONG
- OBJ-04 OWNED_PROOF: 6 obs / 5 authors → SUPPORTED · EARLY SIGNAL
- OBJ-05 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- OBJ-05 OWNED_PROOF: 7 obs / 7 authors → SUPPORTED · EARLY SIGNAL
- OBJ-06 MARKET_VOC: 3 obs / 3 authors → SUPPORTED · EARLY SIGNAL
- OBJ-06 OWNED_PROOF: 4 obs / 4 authors → SUPPORTED · EARLY SIGNAL
- OBJ-07 MARKET_VOC: 3 obs / 3 authors → VALIDATED · STRONG
- OBJ-07 OWNED_PROOF: 9 obs / 7 authors → SUPPORTED · EARLY SIGNAL
- OBJ-08 MARKET_VOC: 7 obs / 7 authors → VALIDATED · STRONG
- OBJ-08 OWNED_PROOF: 2 obs / 2 authors → EARLY SIGNAL · INSUFFICIENT
- OBJ-09 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- OBJ-09 OWNED_PROOF: 2 obs / 1 authors → HYPOTHESIS (ANECDOTE) · INSUFFICIENT
- OBJ-10 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- OBJ-10 OWNED_PROOF: 3 obs / 3 authors → SUPPORTED · EARLY SIGNAL
- OBJ-11 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- OBJ-11 OWNED_PROOF: 4 obs / 3 authors → SUPPORTED · EARLY SIGNAL
- FS-01 MARKET_VOC: 23 obs / 16 authors → VALIDATED · STRONG
- FS-01 OWNED_PROOF: 9 obs / 9 authors → SUPPORTED · EARLY SIGNAL
- FS-02 MARKET_VOC: 9 obs / 8 authors → VALIDATED · STRONG
- FS-02 OWNED_PROOF: 4 obs / 4 authors → SUPPORTED · EARLY SIGNAL
- FS-03 MARKET_VOC: 4 obs / 2 authors → EARLY SIGNAL · EARLY SIGNAL
- FS-03 OWNED_PROOF: 2 obs / 1 authors → HYPOTHESIS (ANECDOTE) · INSUFFICIENT
- FS-04 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- FS-04 OWNED_PROOF: 5 obs / 4 authors → SUPPORTED · EARLY SIGNAL
- FS-05 MARKET_VOC: 8 obs / 6 authors → SUPPORTED · EARLY SIGNAL
- FS-05 OWNED_PROOF: 3 obs / 3 authors → SUPPORTED · EARLY SIGNAL
- FS-06 MARKET_VOC: 3 obs / 3 authors → VALIDATED · STRONG
- FS-06 OWNED_PROOF: 1 obs / 1 authors → HYPOTHESIS (ANECDOTE) · INSUFFICIENT
- MC-01 MARKET_VOC: 3 obs / 2 authors → EARLY SIGNAL · EARLY SIGNAL
- MC-01 OWNED_PROOF: 1 obs / 1 authors → HYPOTHESIS (ANECDOTE) · INSUFFICIENT
- MC-02 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- MC-02 OWNED_PROOF: 3 obs / 3 authors → SUPPORTED · EARLY SIGNAL
- MC-03 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- MC-03 OWNED_PROOF: 6 obs / 5 authors → SUPPORTED · EARLY SIGNAL
- MC-04 MARKET_VOC: 3 obs / 3 authors → SUPPORTED · EARLY SIGNAL
- MC-04 OWNED_PROOF: 2 obs / 2 authors → EARLY SIGNAL · INSUFFICIENT
- MC-05 MARKET_VOC: 3 obs / 3 authors → SUPPORTED · EARLY SIGNAL
- MC-05 OWNED_PROOF: 2 obs / 2 authors → EARLY SIGNAL · INSUFFICIENT
- MC-06 MARKET_VOC: 6 obs / 6 authors → VALIDATED · STRONG
- MC-06 OWNED_PROOF: 0 obs / 0 authors → NULL · INSUFFICIENT
- MC-07 MARKET_VOC: 0 obs / 0 authors → NULL · INSUFFICIENT
- MC-07 OWNED_PROOF: 2 obs / 2 authors → EARLY SIGNAL · INSUFFICIENT

Saturation tally (theme × corpus): STRONG 9 · MODERATE 0 · EARLY SIGNAL 21 · INSUFFICIENT 18. hyper_responsive: 67. New niche tags logged (outside the closed vocabulary, kept as written by harvesters): ['emotion:betrayed', 'emotion:devastated', 'emotion:discouraged', 'emotion:frustrated', 'emotion:hopeless', 'emotion:overwhelm', 'emotion:painful', 'emotion:relief', 'emotion:tired', 'population_marker', 'solution_mentioned', 'time_with_problem'].

**pain_score_pre re-printed** (01 §10 → 01-DEEP T7): PB-01 7/10 → 7/10 · PB-06 9/10 → 9/10 · PB-05 5/10 → 6/10 (DEEP).
### §13-OWNED · the operator's sales-call cut (OWNED_PROOF only; table + verbatim Q-O quotes; interpretation only where marked [D])

Calls with ≥1 record: 84 (US 44 · UK-file 40) · persons 78 · records 181 · C rows 29.

**By call_outcome**

| call_outcome | records | calls | example (verbatim) |
|---|---|---|---|
| PAID | 7 | 2 | "if it's gonna take fourteen days how can i take back your money in seven" (Q-O-0030) |
| DEPOSIT | 5 | 2 | "You guys can fully automate my online business" (Q-O-0001) |
| BOOKED-FOLLOWUP | 120 | 56 | "I get Social Security, so I need to protect that" (Q-O-0007) |
| DECLINED | 30 | 12 | "I invested a lot of my money into buying this business" (Q-O-0004) |
| HUNG-UP | 2 | 1 | "After paying $500, I should be paying £1 every month. You didn't tell me that earlier." (Q-O-0135) |
| UNKNOWN | 17 | 11 | "I don't have a job at the moment, so I'm using my my wife's income" (Q-O-0033) |

**By call_market**

| call_market | records | calls | outcomes (calls) |
|---|---|---|---|
| US | 109 | 44 | {'BOOKED-FOLLOWUP': 26, 'PAID': 2, 'UNKNOWN': 7, 'DECLINED': 7, 'DEPOSIT': 2} |
| UK | 67 | 37 | {'BOOKED-FOLLOWUP': 28, 'UNKNOWN': 3, 'DECLINED': 5, 'HUNG-UP': 1} |
| IE | 3 | 2 | {'BOOKED-FOLLOWUP': 1, 'UNKNOWN': 1} |
| NO | 2 | 1 | {'BOOKED-FOLLOWUP': 1} |

**By CP-##** (records · calls · outcomes of those calls)

| CP | records | calls | outcomes (calls) | verbatim |
|---|---|---|---|---|
| CP-01 | 24 | 14 | {'DECLINED': 1, 'UNKNOWN': 2, 'BOOKED-FOLLOWUP': 10, 'PAID': 1} | "I get Social Security, so I need to protect that" (Q-O-0007) |
| CP-02 | 20 | 11 | {'BOOKED-FOLLOWUP': 7, 'DECLINED': 3, 'UNKNOWN': 1} | "I'm in a parking lot, and I'm gonna pick up my son" (Q-O-0017) |
| CP-03 | 33 | 17 | {'BOOKED-FOLLOWUP': 11, 'UNKNOWN': 2, 'DECLINED': 3, 'DEPOSIT': 1} | "I invested a lot of my money into buying this business" (Q-O-0004) |
| CP-04 | 19 | 9 | {'BOOKED-FOLLOWUP': 6, 'DECLINED': 1, 'UNKNOWN': 1, 'DEPOSIT': 1} | "You guys can fully automate my online business" (Q-O-0001) |
| CP-05 | 16 | 6 | {'DECLINED': 2, 'PAID': 1, 'BOOKED-FOLLOWUP': 2, 'DEPOSIT': 1} | "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002) |
| CP-06 | 15 | 8 | {'BOOKED-FOLLOWUP': 6, 'UNKNOWN': 1, 'DECLINED': 1} | "he used to say, man, cherish this time" (Q-O-0041) |
| CP-07 | 2 | 2 | {'BOOKED-FOLLOWUP': 2} | "I need to talk to my husband about it" (Q-O-0018) |
| NULL | 59 | 42 | {'BOOKED-FOLLOWUP': 30, 'UNKNOWN': 6, 'DECLINED': 5, 'HUNG-UP': 1} | "I'm 56. I don't have I'm not in Internet" (Q-O-0076) |

**lead_quality_marker tallied** (harvester-written markers, not verbatim; one call counts once per category; keyword rule printed; categories overlap) 

| marker category | calls | DECLINED/HUNG-UP | PAID/DEPOSIT | BOOKED-FOLLOWUP | UNKNOWN |
|---|---|---|---|---|---|
| funds absent / declined card / debts / benefits | 8/84 | 3 | 0 | 5 | 0 |
| out of work / unwell / between jobs | 6/84 | 1 | 1 | 3 | 1 |
| prior loss / scam / failed store | 16/84 | 2 | 1 | 13 | 0 |
| wants proof / legitimacy / contract / guarantee | 10/84 | 3 | 0 | 6 | 1 |
| price / ROI questions before committing | 13/84 | 1 | 2 | 10 | 0 |
| retired / age stated | 14/84 | 0 | 1 | 11 | 2 |
| existing business / store owner | 8/84 | 0 | 1 | 5 | 2 |
| time-constrained / parenting duties | 15/84 | 3 | 0 | 11 | 1 |
| spouse / joint money decision | 5/84 | 0 | 0 | 4 | 1 |
| confused by offer / screen-share | 8/84 | 2 | 0 | 4 | 2 |
| hostile / irritated by calls | 3/84 | 1 | 1 | 1 | 0 |

Per-call marker list (call id = unique_author_id; first marker as written by the harvester; outcome):

- O-7e217243 · BOOKED-FOLLOWUP · no personal funds disclosed as income source — receives Social Security and is putting the store in a partner's name to protect benefits
- O-f85633d6 · BOOKED-FOLLOWUP · wants to show a court/parole system he is 'a regular member of society'
- O-9d547e9d · BOOKED-FOLLOWUP · wants to talk to her husband before deciding
- O-decf68af · BOOKED-FOLLOWUP · wants an e-bike parts store
- O-3dd099fe · BOOKED-FOLLOWUP · wants an ROI timeline before paying
- O-48b8dedb · BOOKED-FOLLOWUP · runs an existing import/sewing side business with self-reported $10k-14k monthly revenue
- O-32a00cca · BOOKED-FOLLOWUP · wants proof of results before paying
- O-735a0ad4 · BOOKED-FOLLOWUP · wants to review materials at her desk before deciding
- O-82f75d9e · BOOKED-FOLLOWUP · asks for proof the company is legitimate before committing
- O-f2df9424 · BOOKED-FOLLOWUP · card declined for insufficient funds
- O-81abb644 · BOOKED-FOLLOWUP · lost $4,500 to a prior scam
- O-cd4a2a0d · BOOKED-FOLLOWUP · turning 68 in September, on Social Security, doing DoorDash, on a two-year apartment waitlist
- O-ff7f44b5 · BOOKED-FOLLOWUP · 56 years old, describes herself as not internet-savvy
- O-6c263bde · BOOKED-FOLLOWUP · frames AI as a closing window of opportunity he needs to move fast on
- O-1bf10396 · BOOKED-FOLLOWUP · prior Wix store attempt ('Dream...Boutique') did not work
- O-264472f5 · BOOKED-FOLLOWUP · exploring 3-4 business ideas in parallel, online being one
- O-7198f7ec · BOOKED-FOLLOWUP · wants to wait until she finishes school before committing money or time
- O-0dc3510d · BOOKED-FOLLOWUP · same prospect as Q-O-0033/0034/0035 on a later call
- O-f3e705fd · BOOKED-FOLLOWUP · repeatedly refuses to proceed without a concrete return-on-investment number
- O-a0874b00 · BOOKED-FOLLOWUP · a prior affiliate/marketing program cost him more than it returned
- O-09a3b957 · BOOKED-FOLLOWUP · closed a prior online store while moving
- O-b9ed2904 · BOOKED-FOLLOWUP · same retired prospect as Q-O-0095 on a later call
- O-3fd51b13 · BOOKED-FOLLOWUP · same fitness/mindset-coaching prospect as Q-O-0027/0028/0029 on a later call
- O-cca911d9 · BOOKED-FOLLOWUP · lost his job after traveling to visit family abroad
- O-f721f574 · BOOKED-FOLLOWUP · same prospect as Q-O-0062/0063/0064 (prior $4,500 scam loss) on a later call
- O-89f4c88a · BOOKED-FOLLOWUP · commission-only solar sales income is unpredictable, wants something steadier
- O-65d201c9 · BOOKED-FOLLOWUP · 20 years same manual job, fatigue-driven, no stated funds figure
- O-99d7bf25 · BOOKED-FOLLOWUP · academic, deliberate decision style, wants to reflect before committing
- O-35d2317c · BOOKED-FOLLOWUP · checks the caller's number credibility before continuing
- O-a69fc3b4 · BOOKED-FOLLOWUP · asks costs before committing, no figure given yet
- O-b4f00a87 · BOOKED-FOLLOWUP · already has a niche product idea in mind (African/Nigerian food)
- O-a680bb4d · BOOKED-FOLLOWUP · confused by on-screen store dashboard wording during live walkthrough
- O-42a004a9 · BOOKED-FOLLOWUP · compounding losses: job, bank fraud, phone theft, severe head injury — rebuilding from scratch
- O-6c960800 · BOOKED-FOLLOWUP · burned ~3-4 years and money paying fees to a marketing scammer with no results
- O-8960189a · BOOKED-FOLLOWUP · money available is jointly owned with a partner, not solely his to spend
- O-df4f4cad · BOOKED-FOLLOWUP · fields frequent unsolicited sales calls, wary of being sold to repeatedly
- O-559d043f · BOOKED-FOLLOWUP · demands a guarantee against losing the invested money
- O-c018d848 · BOOKED-FOLLOWUP · retired from the NHS, now has time to properly pursue a store he tried before but under-invested time in
- O-0e78dc62 · BOOKED-FOLLOWUP · council-house tenant supporting a wife and kids on a factory wage
- O-6ffa9c82 · BOOKED-FOLLOWUP · explicit prior financial loss to an online scam, still being resolved by a solicitor
- O-59e9ab02 · BOOKED-FOLLOWUP · already running a niche sourcing + Shopify business (county GAA jerseys)
- O-4b3eb2a1 · BOOKED-FOLLOWUP · built a store previously but never launched it — a stalled DIY attempt
- O-96f490a3 · BOOKED-FOLLOWUP · prior fulfillment attempt failed due to lack of time to pack/ship on schedule
- O-8482e001 · BOOKED-FOLLOWUP · had money set aside but spent it, pushing the purchase out by roughly two weeks
- O-6fe9d604 · BOOKED-FOLLOWUP · parent of four, currently between jobs
- O-d30315f1 · BOOKED-FOLLOWUP · evening call cut short by parenting duties (kids' bedtime)
- O-afd2e48b · BOOKED-FOLLOWUP · unclear on the handover point between done-for-you build and ongoing self-management
- O-de8c9529 · BOOKED-FOLLOWUP · time-boxed and reluctant to rush the conversation
- O-2e22a9c0 · BOOKED-FOLLOWUP · engaged enough to complete a live screen-share walkthrough
- O-b4359de7 · BOOKED-FOLLOWUP · missed the scheduled call due to a home boiler service appointment
- O-c3127ef1 · BOOKED-FOLLOWUP · reschedules to 7pm same day rather than declining outright
- O-26a023e8 · BOOKED-FOLLOWUP · wants the store as a side hustle alongside existing income, long-held intention
- O-4d24d591 · BOOKED-FOLLOWUP · repeats 'side hustle' framing — supplemental income, not a job replacement
- O-0bc431fa · BOOKED-FOLLOWUP · social worker aiming to eventually fully replace her salary with store income
- O-429f17e9 · BOOKED-FOLLOWUP · walking through the live screen-share, asking where the actual build step is
- O-eb798e63 · BOOKED-FOLLOWUP · frames risk tolerance as an age-related identity shift, near/at retirement age
- O-bd81d158 · DECLINED · wants proof of results before paying $2,500
- O-a09fbc4f · DECLINED · could not get the storefront live (repeated app errors), wanted hands-on help picking products, declines at the end citing no funds
- O-22f51137 · DECLINED · carpenter off work 1+ year for a heart condition
- O-9fc681ce · DECLINED · originally exploring the store for his daughter, who preferred cash to a business
- O-5625961c · DECLINED · curious about e-commerce for about 5 years without acting
- O-cc8c465f · DECLINED · ran a dropshipping store before that felt like a scam — over $1,000 is still stuck in that account and she cannot withdraw it
- O-78f82c95 · DECLINED · checks Google reviews before trusting any DFY-store vendor's claims
- O-5a711bda · DECLINED · disputes what the screen-share actually shows vs. what was promised
- O-29a3a362 · DECLINED · did independent research on the company before declining outright
- O-40d9bf9a · DECLINED · openly financially struggling, self-assesses now as the wrong time to invest
- O-7b3e52d9 · DECLINED · irritated by the rep repeating the same script, threatens to hang up
- O-852df385 · DECLINED · self-assesses as financially not ready to invest right now
- O-a654f844 · DEPOSIT · existing business owner asked mid-call to move money between his own bank accounts to fund the $500 package
- O-aeea92be · DEPOSIT · opens hostile ('all these fucking scams'), ends agreeing to set up the store — second call with the same prospect as Q-O-0010/0011
- O-c5e20736 · HUNG-UP · ends the call abruptly after confusion over Shopify vs Etsy platform claims
- O-5455cbcf · PAID · paid $500 and received a confirmation email during the call
- O-7efb82c7 · PAID · unwell and out of work
- O-0feb370b · UNKNOWN · unemployed, relying on wife's inconsistent-hours income
- O-9750469a · UNKNOWN · same prospect as Q-O-0010/0011/0012/0013 on a later call
- O-3f6219f9 · UNKNOWN · works Medicare insurance sales, licensed 9 years
- O-7e92990b · UNKNOWN · references an existing Wix store while getting confused navigating the Readymerce sign-up flow
- O-d5f8ca6a · UNKNOWN · retired, describes himself as a newcomer to Canada, wants to stay active and productive
- O-b64e4cf7 · UNKNOWN · warehouse worker who wants an alternative to his current job
- O-27a44c94 · UNKNOWN · former Walmart manager
- O-01701f10 · UNKNOWN · gives a generic always-on-income motivation under heavy rep pressure
- O-c8bbdefc · UNKNOWN · already running an 18-month-old store, exploring expansion rather than starting fresh
- O-5ab32cbb · UNKNOWN · friend's no-physical-goods online selling model is the direct trigger for registering
- O-9b45680c · UNKNOWN · questions the unlabeled video source shown during the screen-share, wary of unverified content

**PAID / DEPOSIT calls — verbatim** (what the 10 converting calls said): "You guys can fully automate my online business" (Q-O-0001) · "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002) · "I need to just trust the supplier that everything ... is a trusted supplier" (Q-O-0003) · "with all these fucking scams ... stop fucking calling me" (Q-O-0012) · "I'm getting it ready promise" (Q-O-0013) · "if it's gonna take fourteen days how can i take back your money in seven" (Q-O-0030) · "purchase ready thank you for purchase i got a confirmation email" (Q-O-0031) · "who do i come to who do i kill for my money" (Q-O-0032) · "I've been out of work. And I'm just not well" (Q-O-0036) · "I was gonna buy an electric bike with this money" (Q-O-0037) · "I had so much fraud through this federal credit union" (Q-O-0038) · "It says payment's on its way" (Q-O-0039)

**DECLINED / HUNG-UP calls — verbatim** (first record per call): "I invested a lot of my money into buying this business" (Q-O-0004) · "It won't let me get on live at all" (Q-O-0014) · "I have some health issue. I don't work. I'm carpenter" (Q-O-0020) · "she rather me give her the money than pay for what y'all offering" (Q-O-0040) · "I've not been able to figure out like, what's gonna be the best platform" (Q-O-0049) · "I felt like it was a scam" (Q-O-0073) · "my store didn't even make $20, so I had to come out" (Q-O-0101) · "Can I review full contract before making payment?" (Q-O-0116) · "After paying $500, I should be paying £1 every month. You didn't tell me that earlier." (Q-O-0135) · "The one thing I don't have in my life is time. Plus I have a child of five years old." (Q-O-0143) · "I'm struggling on my financial side. I believe it's not the best time to just start investing." (Q-O-0156) · "Next time you repeat yourself, I'm going to cut off." (Q-O-0165) · "I may not be the best place to invest in anything at the moment." (Q-O-0177)

[D] Only what the counts show (§6 co-occurrence column): 3 of the 4 PAID/DEPOSIT calls (call ids a654, aeea, 5455) voiced a proof, scam or refund objection on the call (OBJ-02 / OBJ-03 / OBJ-07), so a spoken objection does not mark a lost call; OBJ-01 (no money now) co-occurs with DECLINED/HUNG-UP in 6 of 13 such calls and with PAID/DEPOSIT in 0 of 4 — the highest DECLINED/HUNG-UP share of any objection. Association only, SAMPLE(84 calls); no causal claim.

## §14 · BATTERY ANSWERS (MARKET_VOC ‖ OWNED_PROOF)

- **TRIGGERS (struggling moments)** — MARKET_VOC: obs 7 · units 5 · authors 7 · threads 7 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 11 · units 11 · authors 10 · threads 11 · platforms 1 → SUPPORTED ‖ TOTAL: obs 18 · units 16 · authors 17 · threads 18 · platforms 3 → VALIDATED
  - MARKET: "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015) · "Time intensive early on (i work a full time job right now)" (Q-F-0016) · "trying to scale my business while keeping my full-time job" (Q-F-0017) · "i didn't know the perfect route to go" (Q-Y-0045) · "After weeks of overthinking, I finally committed" (Q-Y-0053) · "तीन मठ के अंदर कुछ ना कुछ तो करना ही है" (Q-Y-0062)
  - OWNED: "I just got out of prison for seven years" (Q-O-0010) · "I still haven't got a job with over 700 applications" (Q-O-0065) · "The AI is getting too fast. Too crazy" (Q-O-0079) · "I learned about a lot of this stuff when I was locked up in county" (Q-O-0093) · "When I came back, I didn't get a job" (Q-O-0106) · "I've been doing this for 20 years, I'm tired now." (Q-O-0111) · "I've just taken a retirement, so I want to focus on doing it well." (Q-O-0141) · "I developed one, but I never launched it. That's the problem." (Q-O-0153)
- **ALMOST-STOPPED** — MARKET_VOC: obs 6 · units 6 · authors 6 · threads 6 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 8 · units 8 · authors 8 · threads 8 · platforms 1 → SUPPORTED ‖ TOTAL: obs 14 · units 14 · authors 14 · threads 14 · platforms 3 → VALIDATED
  - MARKET: "he's a scam, I was told he doesn't work with Shopify" (Q-F-0003) · "you have to scramble around looking for youtube videos" (Q-F-0008) · "I'm definitely quitting fashion drop shipper" (Q-Y-0022) · "it's extremely discouraging and it just makes you want to give up" (Q-Y-0031) · "i had to give up or else i would literally lose all my money" (Q-Y-0049) · "I'm not going to let perfection slow me down" (Q-Y-0057)
  - OWNED: "I need to talk to my husband about it" (Q-O-0018) · "I would like to get in touch with y'all when I'm more prepared" (Q-O-0026) · "anytime that I know that I'm ready ... I'll get back to you" (Q-O-0052) · "I want to have time to reflect and have a look because I have another." (Q-O-0113) · "I can't continue the call anymore." (Q-O-0136) · "I developed one, but I never launched it. That's the problem." (Q-O-0153) · "I spent the money I budgeted for it, but I have to be in two weeks' time." (Q-O-0158) · "Where I am now, no." (Q-O-0163)
- **WHAT-MADE-THEM-ACT** — MARKET_VOC: obs 6 · units 6 · authors 6 · threads 6 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 10 · units 10 · authors 9 · threads 10 · platforms 1 → SUPPORTED ‖ TOTAL: obs 16 · units 16 · authors 15 · threads 16 · platforms 3 → VALIDATED
  - MARKET: "i failed the challenge" (Q-Y-0015) · "I was devastated and frustrated" (Q-B-0002) · "I was afraid to ever try again, but eventually I did" (Q-B-0004) · "After weeks of overthinking, I finally committed" (Q-Y-0053) · "तीन मठ के अंदर कुछ ना कुछ तो करना ही है" (Q-Y-0062) · "it takes years to find a winning product" (Q-Y-0064)
  - OWNED: "I just got out of prison for seven years" (Q-O-0010) · "I'm getting it ready promise" (Q-O-0013) · "I'll start with the 500, and then I'll hopefully graduate to the next level" (Q-O-0029) · "purchase ready thank you for purchase i got a confirmation email" (Q-O-0031) · "It says payment's on its way" (Q-O-0039) · "I just wanna go through with it" (Q-O-0054) · "Call me back in two weeks" (Q-O-0064) · "If I can make the money, I'm a do it" (Q-O-0072)
- **IF-ONLY** — MARKET_VOC: obs 3 · units 3 · authors 3 · threads 3 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 1 · units 1 · authors 1 · threads 1 · platforms 1 → HYPOTHESIS (ANECDOTE) ‖ TOTAL: obs 4 · units 4 · authors 4 · threads 4 · platforms 3 → VALIDATED
  - MARKET: "I made so many mistakes in this video" (Q-Y-0038) · "don't get too stuck up on failure" (Q-Y-0050) · "I was afraid to ever try again, but eventually I did" (Q-B-0004)
  - OWNED: "I had other businesses then that I was running... I'm regretting now because if I had started then." (Q-O-0152)
- **MICRO-DREAM SCENES** — MARKET_VOC: obs 9 · units 8 · authors 9 · threads 9 · platforms 2 → VALIDATED ‖ OWNED_PROOF: obs 25 · units 22 · authors 21 · threads 22 · platforms 1 → SUPPORTED ‖ TOTAL: obs 34 · units 30 · authors 30 · threads 31 · platforms 3 → VALIDATED
  - MARKET: "tons of links that are like a snowstorm of information" (Q-F-0006) · "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015) · "trying to scale my business while keeping my full-time job" (Q-F-0017) · "i've already lost 500 drop shipping" (Q-Y-0013) · "this is like the reality of what it is" (Q-Y-0024) · "I've tried Drop Shipping on and off for like 7 years now" (Q-Y-0028)
  - OWNED: "I just got out of prison for seven years" (Q-O-0010) · "I'm in a parking lot, and I'm gonna pick up my son" (Q-O-0017) · "I have some health issue. I don't work. I'm carpenter" (Q-O-0020) · "I've been out of work. And I'm just not well" (Q-O-0036) · "a part time job ... fifteen to eighteen hours a week" (Q-O-0050) · "I do have a girlfriend. I have four children" (Q-O-0059) · "I still haven't got a job with over 700 applications" (Q-O-0065) · "they want $2,800 for me to just get it out of there" (Q-O-0067)
- **3★ VERDICTS** — NULL — searched: 0 star-rated 3★ reviews retrievable (Trustpilot/Amazon BLOCKED-ON-TOOL; the 10 PRODUCT_TRUTH reviews carry no 3★).
- trigger/scene floor PB-01: MARKET_VOC 4/15 PARTIAL · +OWNED 7/15 PARTIAL
- trigger/scene floor PB-06: MARKET_VOC 6/15 PARTIAL · +OWNED 10/15 PARTIAL
- trigger/scene floor PB-05: MARKET_VOC 3/15 PARTIAL · +OWNED 4/15 PARTIAL

## §15 · STORY MATERIAL

**ORGANIC OPENINGS OPN-##** (46 records carry an opening_first_sentence; floor 30 / target 50 → MET):
- OPN-01 [MARKET·forum] “I did the free shopify store through the Adrian Morrison website.” (Q-F-0001) · length 11w · style: confession [D]
- OPN-02 [MARKET·forum] “It's cause your store is half-ass done.” (Q-F-0002) · length 7w · style: raw [D]
- OPN-03 [MARKET·forum] “I just spoke to Shopify about Adrian Morrison and they told me to come here.” (Q-F-0003) · length 15w · style: confession [D]
- OPN-04 [MARKET·forum] “I too have found this process to be not as they said it would be.” (Q-F-0004) · length 15w · style: confession [D]
- OPN-05 [MARKET·forum] “I am so glad I read these reviews.” (Q-F-0005) · length 8w · style: confession [D]
- OPN-06 [MARKET·forum] “I ended up cancelling my first attempt at Shopify.” (Q-F-0006) · length 9w · style: confession [D]
- OPN-07 [MARKET·forum] “Problem is.” (Q-F-0007) · length 2w · style: raw [D]
- OPN-08 [MARKET·forum] “I agree, it would be much better if the important things were simple like they said it was.” (Q-F-0008) · length 18w · style: confession [D]
- OPN-09 [MARKET·forum] “I could not agree with you more.” (Q-F-0009) · length 7w · style: confession [D]
- OPN-10 [MARKET·forum] “I AGREE It's EXTREMELY difficult.” (Q-F-0010) · length 5w · style: confession [D]
- OPN-11 [MARKET·forum] “I am stuck with trying to get the storefront up and running.” (Q-F-0011) · length 12w · style: confession [D]
- OPN-12 [MARKET·forum] “I've been trying to set up shopify for over a week.” (Q-F-0012) · length 11w · style: raw [D]
- OPN-13 [MARKET·forum] “I've spent 10 weeks on simple tasks that the system doesn't verify.” (Q-F-0013) · length 12w · style: timeline [D]
- OPN-14 [MARKET·forum] “I spent months here on trying over and over again to get a site going.” (Q-F-0014) · length 15w · style: confession [D]
- OPN-15 [PRODUC·trustpilot] “My e-commerce business dream started and continues to grow with EcomXpertz.” (Q-E-0001) · length 11w · style: raw [D]
- OPN-16 [PRODUC·trustpilot] “Highly professional team with deep eCommerce expertise!” (Q-E-0002) · length 7w · style: raw [D]
- OPN-17 [PRODUC·trustpilot] “EcomXpertz built my Shopify store and automated everything.” (Q-E-0003) · length 8w · style: raw [D]
- OPN-18 [PRODUC·trustpilot] “EcomXpertz set up my Amazon store from scratch.” (Q-E-0004) · length 8w · style: raw [D]
- OPN-19 [PRODUC·trustpilot] “EcomXpertz made my eCommerce business completely hands-free!” (Q-E-0005) · length 7w · style: raw [D]
- OPN-20 [PRODUC·trustpilot] “They stole $20,000 and have lied to me repeatedly about inventory and dates.” (Q-E-0006) · length 13w · style: timeline [D]
- OPN-21 [PRODUC·trustpilot] “These people paint a rosy picture.” (Q-E-0007) · length 6w · style: raw [D]
- OPN-22 [PRODUC·trustpilot] “I would never, ever do business with this company again.” (Q-E-0008) · length 10w · style: confession [D]
- OPN-23 [PRODUC·trustpilot] “This company scammed me.” (Q-E-0009) · length 4w · style: raw [D]
- OPN-24 [PRODUC·trustpilot] “I started my Shopify store, but after my store was online.” (Q-E-0010) · length 11w · style: confession [D]
- OPN-25 [MARKET·youtube_search] “I bought three gigs on Fiverr to create brand new profitable Shopify stores for me.” (Q-Y-0001) · length 15w · style: confession [D]
- OPN-26 [MARKET·youtube_search] “So all in all was buying a Shopify store on Fiverr a guaranteed way to start a profitable Shopify store, absolutely not.” (Q-Y-0002) · length 22w · style: raw [D]
- OPN-27 [MARKET·youtube_search] “Hey guys, what's going on? Welcome back to a new video.” (Q-Y-0003) · length 11w · style: question [D]
- OPN-28 [MARKET·youtube_search] “Okay so I'm sure you guys have seen the ads online for pre-built shopify stores.” (Q-Y-0004) · length 15w · style: raw [D]
- OPN-29 [MARKET·youtube_search] “Overall I would say that the store it's been well done right.” (Q-Y-0005) · length 12w · style: raw [D]
- OPN-30 [MARKET·youtube_search] “Okay friends so in this video I am going to show you how you can hire someone to build a high quality Shopify store for you in low price.” (Q-Y-0006) · length 29w · style: raw [D]
- OPN-31 [MARKET·youtube_search] “So in today's Drop Shipping experiment I'm going to try and fully Outsource my whole Drop Shipping Store.” (Q-Y-0007) · length 18w · style: raw [D]
- OPN-32 [MARKET·youtube_search] “The AI Store Builder program, promoted via livestorebuild.com by brothers Adrian and Anthony Morrison.” (Q-Y-0008) · length 14w · style: raw [D]
- OPN-33 [MARKET·youtube_search] “This free webinar promises to help you build a Shopify store live on the event.” (Q-Y-0009) · length 15w · style: raw [D]
- OPN-34 [MARKET·forum] “At what level of revenue did those of you who use Virtual Assistants, start using them?” (Q-F-0015) · length 16w · style: question [D]
- OPN-35 [MARKET·forum] “ECOMMERCE DROPSHIPPING Pros - Fulfills 5/5 of the CENTS criteria.” (Q-F-0016) · length 10w · style: timeline [D]
- OPN-36 [MARKET·forum] “I started my business hand making vegan soaps and skincare products in 2021 as a side business/passion project.” (Q-F-0017) · length 18w · style: confession [D]
- OPN-37 [MARKET·forum] “I had someone build a shopify store for me because I wanted to get started quickly.” (Q-F-0018) · length 16w · style: confession [D]
- OPN-38 [MARKET·youtube_search] “Now I've got something really exciting to tell you guys.” (Q-Y-0010) · length 10w · style: raw [D]
- OPN-39 [MARKET·youtube_search] “I am going to show you how you can hire someone to build a high quality Shopify store for you in low price.” (Q-Y-0011) · length 23w · style: confession [D]
- OPN-40 [MARKET·youtube_search] “Finally after promoting affiliate products for lots of years now I've decided to put my hands on Drop Shipping.” (Q-Y-0012) · length 19w · style: raw [D]
- OPN-41 [MARKET·blog_comments] “A few negative reviews mention paying the $97 and not receiving the promised features.” (Q-B-0001) · length 14w · style: timeline [D]
- OPN-42 [MARKET·youtube_search] “Hi, I'm Nancy and this is day two of building an online business in just 90 days.” (Q-Y-0053) · length 17w · style: timeline [D]
- OPN-43 [MARKET·forum] “hello my friends, i am Alex” (Q-F-0028) · length 6w · style: raw [D]
- OPN-44 [MARKET·forum] “Hello every one” (Q-F-0039) · length 3w · style: raw [D]
- OPN-45 [MARKET·forum] “Hello friends” (Q-F-0040) · length 2w · style: raw [D]
- OPN-46 [MARKET·forum] “I'm new here and honestly trying to figure how to start.” (Q-F-0041) · length 11w · style: raw [D]
What real users DON'T do [D]: they don't use brand names or 'passive income' jargon on calls; they don't describe the product's features; they name money in exact figures (Q-Y-0014, Q-O-0062).

**POSTABLE MOMENTS PM-##:** PM-01 "I just got out of prison for seven years" (Q-O-0010) · PM-02 "I'm in a parking lot, and I'm gonna pick up my son" (Q-O-0017) · PM-03 "your car has insufficient funds to complete" (Q-O-0060) · PM-04 "My computer just broke. My son just broke the computer." (Q-O-0146) · PM-05 "I'm doing DoorDash, and I just got out of nursing home" (Q-O-0070) · PM-06 "I was gonna buy an electric bike with this money" (Q-O-0037) · PM-07 "who do i come to who do i kill for my money" (Q-O-0032) · PM-08 "I lost anywhere between like $500 and $11,000 every single day" (Q-Y-0036) · PM-09 "he pretty much kicked me out the community" (Q-Y-0021) · PM-10 "they said they would build a store, but i am building the store???" (Q-F-0004) · PM-11 "He's coming to service my boiler ready for the winter." (Q-O-0172) · PM-12 "I lost everything... I lost my job, and all my bank details go stolen." (Q-O-0128) · PM-13 "I learned about a lot of this stuff when I was locked up in county" (Q-O-0093)

**DEEPER-HOPE QUOTES** (13; MARKET 6 ‖ OWNED 6 ‖ PRODUCT_TRUTH 1): "No wonder people give up" (Q-F-0014) · "my eCommerce business completely hands-free" (Q-E-0005) · "fully Outsource my whole Drop Shipping Store" (Q-Y-0007) · "so you can watch me either make money or lose money" (Q-Y-0010) · "there's plenty of us losing, including myself" (Q-Y-0027) · "I don't need to invent something completely new" (Q-Y-0056) · "it takes years to find a winning product" (Q-Y-0064) · "build a a income that I can sit back and relax" (Q-O-0015) · "I was gonna buy an electric bike with this money" (Q-O-0037) · "he used to say, man, cherish this time" (Q-O-0041) · "I want to at least get to a million or a billion" (Q-O-0058) · "turn this side hustle into a main job" (Q-O-0105) · "I had other businesses then that I was running... I'm regretting now because if I had started then." (Q-O-0152)

**CURIOSITY CU-##:** CU-01 item: "to see if it's worth paying someone on Fiverr" (Q-Y-0003) · origin CORPUS(Q-Y-0003) · tier [R-PAGE] · usable_as: research question · CU-02 item: "so you can watch me either make money or lose money" (Q-Y-0010) · origin CORPUS(Q-Y-0010) · tier [R-PAGE] · usable_as: research question · CU-03 item: "I'm kind of like a six out of ten, I'd say at this stage." (Q-O-0114) · origin CORPUS(Q-O-0114) · tier [R-OWNED] · usable_as: research question
**CORRUPTION CB-##:** NULL — searched: tag `corruption` 0/307 records across all lanes (no industry-corruption claim surfaced first-person).

## §16 · CONTRADICTIONS · COMPETING INTERPRETATIONS · MISSING EVIDENCE

- say-vs-do [D]: "with all these fucking scams ... stop fucking calling me" (Q-O-0012) vs "I'm getting it ready promise" (Q-O-0013) — same call, outcome DEPOSIT.
- say-vs-do [D]: "if it's gonna take fourteen days how can i take back your money in seven" (Q-O-0030) vs "purchase ready thank you for purchase i got a confirmation email" (Q-O-0031) — sceptical of the refund window, then PAID.
- say-vs-do [D]: "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006) (won't pay without results) — DECLINED; vs "I'll start with the 500, and then I'll hopefully graduate to the next level" (Q-O-0029) (will start with 500) — BOOKED-FOLLOWUP.
- vendor pool split (PRODUCT_TRUTH, one competitor page): "my eCommerce business completely hands-free" (Q-E-0005) vs "They stole $20,000 and have lied to me repeatedly" (Q-E-0006) — 5 positive / 5 negative, SAMPLE(10).
- rep pitch vs seller's own pages (C-#### vs PT-##): 'Our goal is for every shop to make at least $10,000 in 6 months.' (C-0020) vs PT-09 / 01-DEEP CONTRADICTS block ('We make no income guarantees'); 'seven day money back guarantee' (C-0002, 17/155 US calls) vs PT-15 (voids on acceptance or any add-on); 'personal assigned account manager' (C-0007) vs PT-19 UNKNOWN; urgency close 'I'm gonna have to hang up and close this opportunity' (C-0024).
- data-quality flags: C-0021 ('What I need is I need a proof of concept that actually works.') duplicates the prospect line Q-O-0132 and C-0026 ('You're offering these sites for $500 or so.') reads as prospect speech — both kept as filed by VOC-OWNED-UK (never rewritten), excluded from VOC counts, flagged for 11/12. Owned `notes` cross-references ('same prospect as Q-O-00xx') use pre-merge ids — see crosswalk in 06-HARVEST-LOG.md.
- competing interpretations [D]: BOOKED-FOLLOWUP (120 records / 58 calls) may mean interest or a polite exit ('Call me back in two weeks' Q-O-0064; 'anytime that I know that I'm ready' Q-O-0052); owned objections are voiced to a rep mid-pitch, market objections are volunteered — not the same speech act.
- missing evidence — searched-and-not-found: Reddit (0 URLs retrievable, all 3 PB lanes; queries in 05 partials §2) · Readymerce's own Trustpilot/BBB/Sitejabber reviews (01-DEEP: 0) · Amazon (n/a lane) · TikTok/YouTube/FB comments (Apify limit) · ad comments (LATE-BOUND: 02.share_url) · 3★ reviews 0 · CP-01 market voice 4 records / 1 unit · CP-07 2 records · corruption 0 · 80 undiarized UK transcripts + US ranks 47–155 unread.

## §17 · ASSUMPTION CHECK + ek_stamps[]

`LATE-BOUND: 03.AS-##` — 03-HANDOFF.json absent at merge time; ek_stamps[] = [] (0/N, 07 runs the EK check). Run now on the AS rows the 04 partials seeded and on the operator's two ICP hypotheses (confirming and contradicting quotes searched with equal effort, per corpus):

| as_id | source_id | claim | corpus | confirming (authors/threads) | contradicting (authors) | verdict | Q-## |
|---|---|---|---|---|---|---|---|
| AS-01 | AS-01 (04 PB-06) + AS-P05-01 (04 PB-05) · CP-05 | "Aspiring E-Commerce Entrepreneurs" who want the build / product selection skipped | MARKET_VOC | 5/5 | 3 | CONFIRMED | conf Q-F-0005 Q-Y-0007 Q-Y-0001 Q-Y-0003 Q-Y-0012 · contra Q-Y-0040 Q-Y-0053 Q-Y-0035 |
| AS-01 | AS-01 (04 PB-06) + AS-P05-01 (04 PB-05) · CP-05 | "Aspiring E-Commerce Entrepreneurs" who want the build / product selection skipped | OWNED_PROOF | 3/3 | 0 | CONFIRMED | conf Q-O-0056 Q-O-0001 Q-O-0024 · contra NULL |
| AS-02 | OPERATOR-HYP-a · CP-02 | fathers of children who want a better future for them / more time with kids and wife | MARKET_VOC | 0/0 | 0 | UNSEEN — searched: [MARKET_VOC records tagged CP-02] | conf NULL · contra NULL |
| AS-02 | OPERATOR-HYP-a · CP-02 | fathers of children who want a better future for them / more time with kids and wife | OWNED_PROOF | 4/4 | 3 | CONFIRMED | conf Q-O-0085 Q-O-0086 Q-O-0059 Q-O-0145 Q-O-0161 Q-O-0160 · contra Q-O-0143 Q-O-0167 Q-O-0040 |
| AS-03 | OPERATOR-HYP-b · CP-06 | adults 50+ with money who want an online business | MARKET_VOC | 0/0 | 0 | UNSEEN — searched: [MARKET_VOC records tagged CP-06] | conf NULL · contra NULL |
| AS-03 | OPERATOR-HYP-b · CP-06 | adults 50+ with money who want an online business | OWNED_PROOF | 3/3 | 5 | CONTRADICTED | conf Q-O-0142 Q-O-0181 Q-O-0141 Q-O-0095 · contra Q-O-0069 Q-O-0071 Q-O-0083 Q-O-0007 Q-O-0121 Q-O-0076 |

Notes [D]: AS-02 — Q-O-0018 excluded from both sides (speaker is a mother deferring to her husband: bears on CP-02, not on 'fathers'). 'parent with kids' is CONFIRMED as a situation in OWNED_PROOF, but 'father' is a gender claim the corpus mostly does not state (never inferred); the 'more time with kids and wife' half is met by time-scarcity quotes that DECLINED or cut calls short (Q-O-0143, Q-O-0167). AS-03 — '50+' is a demographic (01 REJECTED it as a population; CP-06 reframe); 'with money' is contradicted by more CP-06 persons than confirm it (Q-O-0071 'I ain't getting the money right this second', Q-O-0083 'It's not easy to get $500'). MARKET_VOC has 0 records placing CP-02 or CP-06 → UNSEEN there. AS-01 (CP-05) CONFIRMED in MARKET_VOC (VOC-PB-01/PB-06 lanes), consistent with 04 PB-06's seed.

## §18 · HANDOFF FIELDS + COVERAGE STATEMENT

**Honesty sentence.** Every count above is computed in code from 307 Q-records whose verbatim text was harvested by the five partials (the merge fetched nothing); percentages appear only as SAMPLE(N); no desire is read from an emotion, no avatar from one anecdote, no awareness from a community's name; no study is filed (the 29 C-#### rows are the operator's own reps, never evidence); a competitor reviewer's outcome (PRODUCT_TRUTH, SAMPLE(10)) is never proof for Readymerce; unstated demographics, LF8 roots and handling lines stay NULL; owned prospects' objections are said to a rep on a sales call and are read as such.

**HARVEST-## orders** (one per BLOCKED lane family + owned re-mine + thin CPs):

| order | lane | exact recipe | expected_yield | est. cost |
|---|---|---|---|---|
| HARVEST-01 | reddit_post+comments (all PBs) | harshmaur/reddit-scraper {searchTerms:["can't figure out shopify","shopify store no sales","tried dropshipping lost money","don't know what to sell online","paid someone to build my shopify store","quit my job side hustle store"], type: posts+comments, sort: top, time: year, maxItems: 40 each} → RC-RD harshmaur/reddit-comments-scraper {postUrls:[ranked threads], maxCommentsPerPost:40, includeNSFW:false} → clearpath/reddit-post-comments-bulk-scraper → apify/rag-web-browser on old.reddit.com/<post>/.json?limit=200&sort=top (raw-http, RESIDENTIAL, htmlTransformer none) → OPERATOR-PASTE (05 PB-01 URL-24/URL-25 query rows) | 80 (reddit floor) | ≈$0.10–0.50 after Apify reset |
| HARVEST-02 | trustpilot_balanced | RC-TP memo23/trustpilot-scraper-ppe {startUrls:[ecomdoneforyou.com, ecommerceparadise.com, ecomxpertz.com, doneforyoustrategy.com, nn-dfysuccess.com, readymerce.com], maxItems:100, filterLanguages:[en], star lanes 1-2/3/4-5} → OPERATOR-PASTE of the review pages | 60 (≥8 from 3★) | ≈$0.40 |
| HARVEST-03 | amazon_* (critical/3★/5★) | junglee/Amazon-crawler on the top-3 same-function listings per PB by review count (dropshipping / Shopify how-to books & kits; country US) {maxReviews: 100 per star lane} — n/a for PB-01/PB-06 per partials; PB-05 not attempted | 20 | ≈$0.30 |
| HARVEST-04 | tiktok_comments | clockworks/tiktok-scraper {searchQueries:[PH-## per PB], searchSection:/video, resultsPerPage:20, videoSearchSorting:MOST_LIKED, commentsPerPost:40} | 30 | ≈$0.25 |
| HARVEST-05 | youtube_comments | streamers/youtube-comments-scraper (or apify youtube comments actor) on the 25 video URLs already transcribed in 06 (Q-Y-####) {maxComments:100 per video, sort: top} | 30 (video comments floor) | ≈$0.20 |
| HARVEST-06 | fb_post_comments / fb_group | RC-FBC apify/facebook-comments-scraper → memo23/facebook-comments-scraper on the FB post found by HV-PB-01; apify/facebook-groups-scraper on facebook.com/groups/282038432287765 (PUBLIC) {resultsLimit:50, comments on}; LOGIN_WALLED groups (3 named by PB-05) counted, never harvested | 20 (fb+forum+quora) | ≈$0.15 |
| HARVEST-07 | ad_comments | LATE-BOUND: 02.share_url — once 02 hands off share_url for competitor ads with visible comments: apify/facebook-comments-scraper {startUrls:[share_url], resultsLimit:100} | 10 | ≈$0.10 |
| HARVEST-08 | owned_paste RE-MINE | OWNED-US: read prospect turns of datasets/owned-US-ranking.csv ranks 47–155 (109 calls) in the same method; OWNED-UK: the 80 undiarized format-B files (+2 unresolved-name, +1 US mis-file) — split speakers by the rep-script markers (C-0017 opening, $500/375-quid pitch lines) in code, then read; fill call_outcome for all 280 calls to give every §6 denominator the full base | +100–150 Q-O records; CP-07 and PAID/DEPOSIT base | $0 · ≈1.5 h agent time |
| HARVEST-09 | population-first CP-01 / CP-07 | harshmaur/reddit-scraper {searchTerms:["full time job" shopify store after work, "9 to 5" dropshipping no time, wife "can't work" kids "side income", "stay at home" "online store"], 40 each} + RC-EXA on forum/Quora hits; OWNED: HARVEST-08 keyword pass for 'wife'/'husband'/'kids' + 'can't work' | CP-01 25 (market 4 now) · CP-07 25 (2 now) | ≈$0.20 + Exa ≈$0.30 |

**Handoff fields (exact names):**
- `voc_corpus_path`: 06-VOC_MASTER.csv
- `ledgers_path`: 06-VOC-LEDGERS.csv
- `harvest_log_path`: 06-HARVEST-LOG.md
- `corpus_version`: v1
- `records_total`: 307 (MARKET_VOC 116 · PRODUCT_TRUTH 10 · OWNED_PROOF 181) + C rows 29
- `records_by_tier`: {'[R-PAGE via Exa]': 55, '[R-PAGE]': 12, '[R-SNIPPET]': 5, '[R-SCRAPE]': 54, '[R-OWNED]': 181}
- `floors`: §0 GLOBAL FLOOR TABLE
- `saturation`: §13 + ledgers col saturation
- `pain_points[]`: §1 PP-01..PP-07
- `pain_phrases[]`: §2
- `swap_table[]`: §10
- `icp_language_analysis`: §10
- `media_terms[]`: §10
- `top_verbatim[]`: §2 TOP 50
- `hook_list[]`: §2
- `failed_solutions[]`: §3 FS-01..FS-06
- `misconceptions[]`: §5 MC-01..MC-07
- `belief_map`: §5
- `beliefs_required[]`: §5 BR-01..BR-07
- `objections[]`: §6 OBJ-01..OBJ-11
- `anti_desires[]`: §6b AD-01..AD-06
- `skepticism_bank[]`: §7 SK-01..SK-06
- `tired_of_hearing[]`: §7
- `trust_signals`: §8
- `authority_read`: RESENT (§8)
- `price_sensitivity_map`: §9
- `product_map[]`: §11
- `ranked_symptoms[]`: §12
- `hidden_fears[]`: §12 Q-O-0084 Q-O-0125 Q-O-0007
- `big_win_chains[]`: §12
- `worldview_map`: §12
- `battery_answers`: §14
- `openings[]`: §15 OPN-##
- `postable_moments[]`: §15 PM-01..PM-13
- `deeper_hope_quotes[]`: §15
- `curiosity_bank[]`: §15 CU-##
- `corruption_bank[]`: NULL — searched (§15)
- `contradictions[]`: §16
- `missing_evidence[]`: §16
- `assumption_check`: §17 (04-seeded AS + OPERATOR-HYP-a/-b); EK: LATE-BOUND: 03.AS-##
- `ek_stamps[]`: [] — LATE-BOUND: 03.AS-##
- `awareness_distribution`: §13 SAMPLE(N) per corpus
- `speaker_stage_distribution`: §13 SAMPLE(N) per corpus
- `population_coverage`: §1 per-CP + ledgers cp rows
- `bias_row`: §13
- `harvest_orders[]`: HARVEST-01..HARVEST-09
- `cost_usd`: 0.00 (merge) · harvest legs $1.925 Exa + TranscriptAPI credits

### QC (Step 8)

- PASS · No synthesized-as-verbatim (every bank line is an exact_quote pulled by q_id in code)
- PASS · No one-person overcount (owned: 84 calls → 78 persons via 'same prospect' aliases; market authors by handle)
- PASS · Outcomes not mislabelled as desires (PRODUCT_TRUTH outcome_reported kept out of §4 desire banks except where the harvester co-tagged desire — listed raw only)
- PASS · Problem states not mislabelled as angles (no angles written)
- PASS · 'I tried everything' not an angle
- PASS · Contradicting evidence preserved (§6 market+owned, §16 say-vs-do, §17 contradicting columns)
- PASS · Every conclusion traces to Q-##s
- PASS · Openings sound like their platform (OPN-## carry corpus·source_type)
- PASS · Synthesized concepts labelled ([D]; BIG-WIN chains [D]; no SYNTHESIZED CREATIVE IDEA written)
- PASS · Usable tomorrow by a human and by an LLM (CSV + ledgers + section pointers)
- FAIL — report is long (full per-call marker list in §13-OWNED); kept because the operator asked for the owned cut; repair: 07 reads §6/§13-OWNED tables first · Concise
- PASS · Surveillance test per PB/CP (no phone numbers, surnames or employers inside quotes; the one digit-run hit, Q-Y-0006 '50 100 200', is dollar amounts — false positive; call locators with numbers live only in source_url/thread_id as BRIEF-VOC-OWNED mandates, never in this report)
- PASS · Daily-reality check (scenes are parking lots, DoorDash, boilers, bedtime — Q-O-0017, Q-O-0070, Q-O-0172, Q-O-0167)
- PASS · Reading-grade flags present (127 blanks filled by FK formula in code; hook bank ≤ grade 8)
- PASS · ledgers n = corpus n (307 = 307)
- PASS · Three corpora never mixed in any ledger/count/floor (MARKET_VOC ‖ OWNED_PROOF ‖ TOTAL; PRODUCT_TRUTH separate)
- PASS · C-#### never in a language bank
- PASS · §4 reserved; LF8 and handling NULL

QC: 17/18 PASS (1 FAIL: concise — repaired by reading order note).

FLOORS: see §0 — MARKET_VOC alone PARTIAL on total/reddit/reviews/video-comments/CP; MARKET_VOC + OWNED_PROOF MET on total.

COVERAGE: records MARKET_VOC 111/200 ‖ MARKET_VOC+OWNED_PROOF 292/200 ‖ all 302/200 (target 400; +PRODUCT_TRUTH 10) · R-PAGE/R-SCRAPE 121 (incl. [R-PAGE via Exa]; + [R-OWNED] 181) · PB: [PB-01 30‖75/40 PB-06 54‖80/40 PB-05 27‖44/40 PB-02 0‖48/40 PB-03 0‖31/40 PB-04 0‖15/40 PB-07 0‖12/40] · CP: [CP-01 4‖28/25 CP-02 0‖20/25 CP-03 46‖79/25 CP-04 0‖19/25 CP-05 43‖59/25 CP-06 0‖15/25 CP-07 0‖2/25] · types MARKET_VOC 4/4 ‖ +OWNED 5/4 · tags below floor: MARKET_VOC [scene 9/15, failed_solution 14/20, objection 18/20, desire 7/15, trigger 7/15, symptom 5/10, tired_of_hearing 4/5, curiosity 2/3, corruption 0/3] ‖ +OWNED [symptom 8/10, corruption 0/3] · saturation STRONG/MODERATE/EARLY/INSUFFICIENT 9/0/21/18 · unique authors MARKET_VOC 64 ‖ OWNED persons 78 · independent threads MARKET_VOC 45 ‖ OWNED calls 84 · hyper-responsive 67 · usable rate per lane: page/transcript PB-01 13/15 · PB-06 18/21 · PB-05 13/17 · owned US 44/46 · UK 40/40 (+80 BLOCKED-FORMAT) · reddit 0/0 · blocked: [reddit_*, amazon_*, trustpilot_* (Readymerce), tiktok_comments, youtube_comments, fb_*, ad_comments LATE-BOUND: 02.share_url] · AS CONFIRMED/CONTRADICTED/UNSEEN 3/1/2 (3 AS × 2 corpora; EARLY SIGNAL 0) | EK: LATE-BOUND: 03.AS-## · EK stamped 0/LATE-BOUND · weakest link: MARKET_VOC has 0 Reddit and 0 review/comment lanes, so CP-01/CP-02/CP-06/CP-07 and every operator-ICP question rest on OWNED_PROOF alone (one platform, max SUPPORTED) · what closing it would cost: HARVEST-01..07 ≈ 150–250 sources · ≈$1.7–2.2 Apify after the monthly reset + ≈$0.30 Exa · ≈3 h; HARVEST-08 owned re-mine $0 · ≈1.5 h
