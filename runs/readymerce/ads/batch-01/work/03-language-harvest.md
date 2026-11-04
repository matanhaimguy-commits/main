# 03 · Language Harvest (A2b) · Readymerce ads batch-01 · P1 SLATE

Source: `foundation/06-VOC_MASTER.csv` read with python3 csv (362 rows). Every phrase below was checked in code as a verbatim substring of that row's `exact_quote` or `exact_passage` (110 of 110 PASS; grammar, spelling and punctuation preserved, e.g. "Ive", "a a income", "hired and expert", "???"). Machine table: `work/03-language-harvest.csv` (ranked by charge).

**Rules applied.** MARKET_VOC rows → `[MKT-LANG]`. OWNED_PROOF rows (sales-call prospects, NOT customers) → `[MKT-LANG]` with `owned=Y`: they shape any slot and every story beat, are never attributed as a Readymerce customer and never shown as a review. PRODUCT_TRUTH rows (Q-E-#### competitor reviews, 10 rows) are EXCLUDED from voice (facts/context only). No `[WRITTEN]` rows in this file (P1 authored no customer lines). **Owned reviews: NONE** (handoff.json `curated_reviews.readymerce = []`; PT-03/PT-07/PT-11..13/PT-18 NULL; site testimonials disclose actors, DNS-10) → A14: market wording goes unattributed into Avatar Callouts and native surfaces; no review screenshots (N6 unavailable), no names, no stars.

`HARVEST: phrases 110 (owned=Y 50, market 60) · per avatar AV-01 29, AV-02 18, AV-03 25, AV-04 17, AV-07 21 · per slot hook 23, subhead 11, body 6, proof 5, cta 9, story 31, hate-doubt 25 · charge 5:24 4:49 3:34 2:3 · PRODUCT_TRUTH used as voice 0 · [WRITTEN] 0`

**Lint notes carried with the phrases (never lift into copy as OUR claim):** Q-O-0001 "fully automate" = his word only (DNS-04, MC-02: correct in copy, managed not automatic) · Q-O-0053 / Q-O-0176 / Q-O-0105 = his want, never our promise (DNS-13, PT-09) · Q-Y-0064 "winning product" = hate-doubt fuel only, never a first line (DNS-09) · Q-Y-0016 "easy money" = his distrust, honoured, never contradicted (DNS-08) · Q-O-0104 / Q-O-0006 / Q-O-0028 prices = alternatives and fears, not our prices (only $500 is live) · Q-Y-0026 = peer voice, never Readymerce proof (P-106.AV-01).

## HOOK fuel (the problem in their exact words, moments, named emotions)

| rank | phrase (verbatim) | Q-## | avatar | charge | desire | angle | tag | owned |
|---|---|---|---|---|---|---|---|---|
| 2 | "still no sales. i've got ~600 clicks" | Q-F-0019 | AV-01 | 5 | MD-04 | AN-06 | [MKT-LANG] | N |
| 3 | "Ive had 2 stores on Shopify both failed" | Q-F-9004 | AV-01 | 5 | MD-04 | AN-05 | [MKT-LANG] | N |
| 4 | "the product did not sell, so I had to close the store" | Q-O-0108 | AV-01 | 5 | MD-04 | AN-05 | [MKT-LANG] | Y |
| 5 | "i got zero sales which means i lost 254 dollars" | Q-Y-0014 | AV-01 | 5 | MD-04 | AN-06 | [MKT-LANG] | N |
| 9 | "now I can't access it, contact an administrator which should be me" | Q-F-0001 | AV-02 | 5 | MD-04 | AN-13 | [MKT-LANG] | N |
| 10 | "your store is half-ass done" | Q-F-0002 | AV-02 | 5 | MD-04 | AN-13 | [MKT-LANG] | N |
| 11 | "they said they would build a store, but i am building the store???" | Q-F-0004 | AV-02 | 5 | MD-04 | AN-13 | [MKT-LANG] | N |
| 14 | "tons of links that are like a snowstorm of information" | Q-F-0006 | AV-03 | 5 | MD-04 | AN-16 | [MKT-LANG] | N |
| 15 | "I'm tech savvy and competent. I cannot find a simple step by step" | Q-F-0012 | AV-03 | 5 | MD-04 | AN-16 | [MKT-LANG] | N |
| 16 | "I've spent 10 weeks on simple tasks" | Q-F-0013 | AV-03 | 5 | MD-04 | AN-16 | [MKT-LANG] | N |
| 20 | "I work a full time job as well, so am only able to attend to my store after hours" | Q-F-0015 | AV-04 | 5 | MD-01 | AN-09 | [MKT-LANG] | N |
| 23 | "I earn good money now, so I don't want to quit and then start struggling." | Q-O-0133 | AV-04 | 5 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 24 | "I must have three or four Shopify stores just sitting there" | Q-O-0103 | AV-07 | 5 | MD-02 | AN-01 | [MKT-LANG] | Y |
| 26 | "After 10 days of campaign, still no orders." | Q-F-0021 | AV-01 | 4 | MD-04 | AN-06 | [MKT-LANG] | N |
| 28 | "not a single sale. Why is this?" | Q-Q-0001 | AV-01 | 4 | MD-04 | AN-06 | [MKT-LANG] | N |
| 29 | "i've already lost 500 drop shipping" | Q-Y-0013 | AV-01 | 4 | MD-04 | AN-06 | [MKT-LANG] | N |
| 35 | "it didn't sell one product not one product" | Q-Y-0046 | AV-01 | 4 | MD-04 | AN-05 | [MKT-LANG] | N |
| 46 | "but nothing that actually helps me!" | Q-F-0006 | AV-03 | 4 | MD-04 | AN-16 | [MKT-LANG] | N |
| 51 | "I don't know where to start or what I should sell" | Q-F-0040 | AV-03 | 4 | MD-04 | AN-18 | [MKT-LANG] | N |
| 52 | "Do I just choose what I want to sell" | Q-F-0041 | AV-03 | 4 | MD-04 | AN-17 | [MKT-LANG] | N |
| 54 | "It won't let me get on live at all" | Q-O-0014 | AV-03 | 4 | MD-04 | AN-16 | [MKT-LANG] | Y |
| 63 | "The one thing I don't have in my life is time." | Q-O-0143 | AV-04 | 4 | MD-02 | AN-12 | [MKT-LANG] | Y |
| 93 | "trying to scale my business while keeping my full-time job" | Q-F-0017 | AV-04 | 3 | MD-01 | AN-09 | [MKT-LANG] | N |

## SUBHEAD fuel (what they believe causes it, what they tried, what they doubt)

| rank | phrase (verbatim) | Q-## | avatar | charge | desire | angle | tag | owned |
|---|---|---|---|---|---|---|---|---|
| 21 | "I don't wanna be trained to do it. I wanna just put the money forward." | Q-O-0056 | AV-04 | 5 | MD-02 | AN-12 | [MKT-LANG] | Y |
| 27 | "I am growing tired of looking at all the traffic and no sales" | Q-F-0022 | AV-01 | 4 | MD-04 | AN-06 | [MKT-LANG] | N |
| 31 | "the strategy was dead, and no one told me" | Q-Y-0018 | AV-01 | 4 | MD-04 | AN-05 | [MKT-LANG] | N |
| 53 | "I hired and expert and he did a good job but then it still wasn't making sales" | Q-F-8303 | AV-03 | 4 | MD-04 | AN-16 | [MKT-LANG] | N |
| 56 | "At what point do I take over the store? Is it something I have to run on my own?" | Q-O-0169 | AV-03 | 4 | MD-02 | AN-16 | [MKT-LANG] | Y |
| 65 | "You guys can fully automate my online business" | Q-O-0001 | AV-07 | 4 | MD-02 | AN-03 | [MKT-LANG] | Y |
| 71 | "at an exorbitant cost, $5,000, $20,000, $15,000" | Q-O-0104 | AV-07 | 4 | MD-01 | AN-02 | [MKT-LANG] | Y |
| 89 | "hire an agency to do the store for you to do the ads for you" | Q-Y-0035 | AV-03 | 3 | MD-02 | AN-16 | [MKT-LANG] | N |
| 92 | "Time intensive early on (i work a full time job right now)" | Q-F-0016 | AV-04 | 3 | MD-01 | AN-09 | [MKT-LANG] | N |
| 98 | "Should I hire a developer" | Q-F-9006 | AV-07 | 3 | MD-02 | AN-02 | [MKT-LANG] | N |
| 102 | "we don't have the budget to be able to do a lot of ads" | Q-O-0005 | AV-07 | 3 | MD-02 | AN-03 | [MKT-LANG] | Y |

## BODY fuel (the benefits they want / the cost of the problem, in their words)

| rank | phrase (verbatim) | Q-## | avatar | charge | desire | angle | tag | owned |
|---|---|---|---|---|---|---|---|---|
| 47 | "It's intensely time consuming and aggravating." | Q-F-0012 | AV-03 | 4 | MD-04 | AN-16 | [MKT-LANG] | N |
| 49 | "No wonder people give up" | Q-F-0014 | AV-03 | 4 | MD-04 | AN-16 | [MKT-LANG] | N |
| 62 | "I want to make sure this one is working before I talk of quitting." | Q-O-0133 | AV-04 | 4 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 74 | "no one had bought anything" | Q-F-0024 | AV-01 | 3 | MD-04 | AN-06 | [MKT-LANG] | N |
| 94 | "I don't have the time to do the due diligence" | Q-O-0042 | AV-04 | 3 | MD-02 | AN-12 | [MKT-LANG] | Y |
| 110 | "I don't need to mix the other business with my own" | Q-O-0045 | AV-07 | 2 | MD-02 | AN-03 | [MKT-LANG] | Y |

## PROOF fuel (what they will accept as proof; no owned reviews exist)

| rank | phrase (verbatim) | Q-## | avatar | charge | desire | angle | tag | owned |
|---|---|---|---|---|---|---|---|---|
| 41 | "go do a Google review of your company and see" | Q-O-0102 | AV-02 | 4 | MD-01 | AN-14 | [MKT-LANG] | Y |
| 43 | "I need a proof of concept that actually works." | Q-O-0132 | AV-02 | 4 | MD-04 | AN-14 | [MKT-LANG] | Y |
| 61 | "Can I review full contract before making payment?" | Q-O-0116 | AV-04 | 4 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 79 | "you could have nine failed stores" | Q-Y-0026 | AV-01 | 3 | MD-04 | AN-08 | [MKT-LANG] | N |
| 100 | "I thought this call was gonna just show me exactly what the $500 pays for" | Q-O-0002 | AV-07 | 3 | MD-01 | AN-02 | [MKT-LANG] | Y |

## CTA fuel (their words for the outcome they want)

| rank | phrase (verbatim) | Q-## | avatar | charge | desire | angle | tag | owned |
|---|---|---|---|---|---|---|---|---|
| 1 | "I was afraid to ever try again, but eventually I did" | Q-B-0004 | AV-01 | 5 | MD-04 | AN-05 | [MKT-LANG] | N |
| 37 | "I would just link into the store once it is finished" | Q-F-0005 | AV-02 | 4 | MD-04 | AN-14 | [MKT-LANG] | N |
| 55 | "build a a income that I can sit back and relax" | Q-O-0015 | AV-03 | 4 | MD-02 | AN-18 | [MKT-LANG] | Y |
| 57 | "After weeks of overthinking, I finally committed" | Q-Y-0053 | AV-03 | 4 | MD-04 | AN-17 | [MKT-LANG] | N |
| 59 | "I want a stable income flow" | Q-O-0046 | AV-04 | 4 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 75 | "I'm looking for a steady income" | Q-O-0109 | AV-01 | 3 | MD-01 | AN-05 | [MKT-LANG] | Y |
| 104 | "I'll start with the 500, and then I'll hopefully graduate to the next level" | Q-O-0029 | AV-07 | 3 | MD-04 | AN-02 | [MKT-LANG] | Y |
| 105 | "I just wanna go through with it" | Q-O-0054 | AV-07 | 3 | MD-04 | AN-02 | [MKT-LANG] | Y |
| 106 | "turn this side hustle into a main job" | Q-O-0105 | AV-07 | 3 | MD-01 | AN-01 | [MKT-LANG] | Y |

## STORY fuel (sequences, scenes, what they tried, the moment they gave up)

| rank | phrase (verbatim) | Q-## | avatar | charge | desire | angle | tag | owned |
|---|---|---|---|---|---|---|---|---|
| 6 | "it's extremely discouraging and it just makes you want to give up" | Q-Y-0031 | AV-01 | 5 | MD-04 | AN-05 | [MKT-LANG] | N |
| 7 | "pure loss of money of time of energy of honestly hope" | Q-Y-0047 | AV-01 | 5 | MD-04 | AN-05 | [MKT-LANG] | N |
| 8 | "i had to give up or else i would literally lose all my money" | Q-Y-0049 | AV-01 | 5 | MD-01 | AN-07 | [MKT-LANG] | N |
| 12 | "I gave somebody $4,500, and they took my money" | Q-O-0062 | AV-02 | 5 | MD-01 | AN-15 | [MKT-LANG] | Y |
| 13 | "soon after I launched my store, the nightmare began." | Q-B-8301 | AV-03 | 5 | MD-04 | AN-16 | [MKT-LANG] | N |
| 17 | "When the store was transferred to me, the store was shutdown almost immediately" | Q-F-0018 | AV-03 | 5 | MD-04 | AN-16 | [MKT-LANG] | N |
| 18 | "I'm left wondering if I just flushed the money and time down the drain" | Q-F-0018 | AV-03 | 5 | MD-04 | AN-16 | [MKT-LANG] | N |
| 19 | "I developed one, but I never launched it. That's the problem." | Q-O-0153 | AV-03 | 5 | MD-04 | AN-17 | [MKT-LANG] | Y |
| 22 | "I wish I was doing something else" | Q-O-0096 | AV-04 | 5 | MD-01 | AN-11 | [MKT-LANG] | Y |
| 25 | "I'm running $50 ad sets. I'm targeting different interests. Still no sales." | Q-F-0019 | AV-01 | 4 | MD-04 | AN-06 | [MKT-LANG] | N |
| 32 | "there's plenty of us losing, including myself" | Q-Y-0027 | AV-01 | 4 | MD-04 | AN-05 | [MKT-LANG] | N |
| 33 | "I spent thousands of dollars and hundreds of hours of my own time" | Q-Y-0029 | AV-01 | 4 | MD-04 | AN-06 | [MKT-LANG] | N |
| 39 | "over a thousand dollars sitting in my account" | Q-O-0074 | AV-02 | 4 | MD-01 | AN-15 | [MKT-LANG] | Y |
| 40 | "my store didn't even make $20, so I had to come out" | Q-O-0101 | AV-02 | 4 | MD-04 | AN-14 | [MKT-LANG] | Y |
| 42 | "I got scammed by the marketing guy." | Q-O-0130 | AV-02 | 4 | MD-01 | AN-13 | [MKT-LANG] | Y |
| 45 | "this coach never even scheduled a call with me" | Q-Y-0019 | AV-02 | 4 | MD-04 | AN-13 | [MKT-LANG] | N |
| 48 | "Just performing one task is a marathon of reading." | Q-F-0013 | AV-03 | 4 | MD-04 | AN-16 | [MKT-LANG] | N |
| 50 | "I had someone build a shopify store for me because I wanted to get started quickly" | Q-F-0018 | AV-03 | 4 | MD-04 | AN-16 | [MKT-LANG] | N |
| 64 | "To make 100% of my salary and above from it." | Q-O-0176 | AV-04 | 4 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 68 | "I'm actually thinking to, you know, replace my job" | Q-O-0053 | AV-07 | 4 | MD-01 | AN-01 | [MKT-LANG] | Y |
| 69 | "I had one before. I just ended it because I was dealing with a lot" | Q-O-0097 | AV-07 | 4 | MD-04 | AN-01 | [MKT-LANG] | Y |
| 70 | "ready to be loaded, and I haven't done anything with them in years" | Q-O-0103 | AV-07 | 4 | MD-02 | AN-01 | [MKT-LANG] | Y |
| 73 | "the marketing was the one bringing in the money, but it's slowed down so much" | Q-O-0124 | AV-07 | 4 | MD-01 | AN-03 | [MKT-LANG] | Y |
| 77 | "i failed the challenge" | Q-Y-0015 | AV-01 | 3 | MD-04 | AN-08 | [MKT-LANG] | N |
| 81 | "it took me over a year straight of failing consistently" | Q-Y-0034 | AV-01 | 3 | MD-04 | AN-08 | [MKT-LANG] | N |
| 87 | "I set up a shop but was too hard for me" | Q-F-8301 | AV-03 | 3 | MD-04 | AN-16 | [MKT-LANG] | N |
| 91 | "constantly jumping from one idea to another" | Q-Y-0059 | AV-03 | 3 | MD-04 | AN-17 | [MKT-LANG] | N |
| 96 | "I've not been able to figure out like, what's gonna be the best platform" | Q-O-0049 | AV-04 | 3 | MD-04 | AN-09 | [MKT-LANG] | Y |
| 101 | "I invested a lot of my money into buying this business" | Q-O-0004 | AV-07 | 3 | MD-01 | AN-01 | [MKT-LANG] | Y |
| 107 | "I'm a computer consultant and I have very little time." | Q-O-0154 | AV-07 | 3 | MD-02 | AN-01 | [MKT-LANG] | Y |
| 108 | "I definitely was not an expert so take what I say with a grain of salt" | Q-Y-0039 | AV-01 | 2 | MD-04 | AN-05 | [MKT-LANG] | N |

## HATE + DOUBT fuel (skepticism about the category; feeds objection reversal + narrator skepticism)

| rank | phrase (verbatim) | Q-## | avatar | charge | desire | angle | tag | owned |
|---|---|---|---|---|---|---|---|---|
| 30 | "make it seem like easy money when it's really not" | Q-Y-0016 | AV-01 | 4 | MD-01 | AN-07 | [MKT-LANG] | N |
| 34 | "I've been burned many times" | Q-Y-0030 | AV-01 | 4 | MD-01 | AN-07 | [MKT-LANG] | N |
| 36 | "promises of more templates, ads, products etc. after you have paid" | Q-B-0001 | AV-02 | 4 | MD-01 | AN-14 | [MKT-LANG] | N |
| 38 | "I felt like it was a scam" | Q-O-0073 | AV-02 | 4 | MD-01 | AN-13 | [MKT-LANG] | Y |
| 44 | "you know, the pitch is almost always the same" | Q-Y-0004 | AV-02 | 4 | MD-01 | AN-14 | [MKT-LANG] | N |
| 58 | "if it's gonna take fourteen days how can i take back your money in seven" | Q-O-0030 | AV-04 | 4 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 60 | "anytime that I know that I'm ready ... I'll get back to you" | Q-O-0052 | AV-04 | 4 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 66 | "I would not pay $2,500 to anybody unless I could see some results" | Q-O-0006 | AV-07 | 4 | MD-01 | AN-02 | [MKT-LANG] | Y |
| 67 | "I pay $500 and then I'm gonna have to pay more money down the road" | Q-O-0028 | AV-07 | 4 | MD-01 | AN-02 | [MKT-LANG] | Y |
| 72 | "I'm like, seriously? Come on." | Q-O-0104 | AV-07 | 4 | MD-01 | AN-02 | [MKT-LANG] | Y |
| 76 | "Is that one-off payment or I need to make a regular payment?" | Q-O-0112 | AV-01 | 3 | MD-01 | AN-07 | [MKT-LANG] | Y |
| 78 | "it isn't all sunshine and rainbows" | Q-Y-0025 | AV-01 | 3 | MD-01 | AN-07 | [MKT-LANG] | N |
| 80 | "a lot of them fake the reviews" | Q-Y-0032 | AV-01 | 3 | MD-01 | AN-07 | [MKT-LANG] | N |
| 82 | "it takes years to find a winning product" | Q-Y-0064 | AV-01 | 3 | MD-04 | AN-08 | [MKT-LANG] | N |
| 83 | "I need to, you know, get my money together" | Q-O-0063 | AV-02 | 3 | MD-01 | AN-15 | [MKT-LANG] | Y |
| 84 | "I assume that the followers are fake" | Q-Y-0005 | AV-02 | 3 | MD-01 | AN-14 | [MKT-LANG] | N |
| 85 | "a clever Shopify affiliate funnel with a big upsell" | Q-Y-0009 | AV-02 | 3 | MD-01 | AN-15 | [MKT-LANG] | N |
| 86 | "numerous chats, bots, and emails only wastes time" | Q-F-0011 | AV-03 | 3 | MD-04 | AN-16 | [MKT-LANG] | N |
| 88 | "I would like to get in touch with y'all when I'm more prepared" | Q-O-0026 | AV-03 | 3 | MD-04 | AN-18 | [MKT-LANG] | Y |
| 90 | "why would someone buy from a new shop" | Q-Y-0054 | AV-03 | 3 | MD-04 | AN-17 | [MKT-LANG] | N |
| 95 | "I'm just worried about the total cost" | Q-O-0048 | AV-04 | 3 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 97 | "send me something to make me understand that you are legitimate" | Q-O-0055 | AV-04 | 3 | MD-01 | AN-10 | [MKT-LANG] | Y |
| 99 | "I simply can't compete with the likes of H&B, Amazon etc." | Q-F-9008 | AV-07 | 3 | MD-04 | AN-01 | [MKT-LANG] | N |
| 103 | "how fast do I start making a return on my investment" | Q-O-0027 | AV-07 | 3 | MD-01 | AN-02 | [MKT-LANG] | Y |
| 109 | "Call me back in two weeks" | Q-O-0064 | AV-02 | 2 | MD-01 | AN-15 | [MKT-LANG] | Y |

## Coverage per avatar × slot

| avatar | hook | subhead | body | proof | cta | story | hate-doubt | total |
|---|---|---|---|---|---|---|---|---|
| AV-07 | 1 | 4 | 1 | 1 | 3 | 6 | 5 | 21 |
| AV-01 | 8 | 2 | 1 | 1 | 2 | 9 | 6 | 29 |
| AV-04 | 4 | 2 | 2 | 1 | 1 | 3 | 4 | 17 |
| AV-02 | 3 | 0 | 0 | 2 | 1 | 5 | 7 | 18 |
| AV-03 | 7 | 3 | 2 | 0 | 2 | 8 | 3 | 25 |

Avatar assignment: `foundation/datasets/09-cluster-qids.json` (CL-06→AV-07, CL-01b→AV-01, CL-03→AV-04, CL-01a→AV-02, CL-02→AV-03), overridden where handoff.json cites a row for another avatar (Q-F-9004, Q-Y-0018 → AV-01; Q-O-0143, Q-O-0042 → AV-04; Q-O-0154 → AV-07; Q-O-0153, Q-F-0018 → AV-03).
