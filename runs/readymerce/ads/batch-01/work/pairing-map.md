# Pairing map · P3 CAPTIONS · Readymerce ads batch-01

Pools (A18 + references/captions-and-headlines.md): 5 evergreen captions CAP-01..05 (captions.txt, fragments/captions.json) and 5 Meta headlines HL-01..05 (headlines.txt). They are two independent pools for the **V1 and V2 ads only**. V3 ads carry their own per-ad story text (Part B); video ads use the writers' 80-200 word primary text, because every pool caption runs 387-393 words.

Loading rule for the operator (campaign-spec): Meta takes up to 5 primary texts and 5 headlines per ad. Load **L** first, then **E**. **W** is allowed but off-situation (load last, or leave out). Never load **X**.
Grades: **L** lead · **E** eligible, no conflict · **W** weak, no contradiction but a different lived situation · **X** incompatible (the caption or headline contradicts what the image says).

## Caption pool at a glance
| id | narrative route | lived situation it opens on | leans to | final 3-word CTA | words |
|---|---|---|---|---|---|
| CAP-01 | a familiar moment | business owner opens the admin; 3 or 4 stores built and just sitting there | AV-07 (C1) | Not just sitting. | 387 |
| CAP-02 | failed attempts | closed a Shopify store (or two) after one product didn't sell; every workaround tried | AV-01 (C2) | A second shot. | 389 |
| CAP-03 | an interrupted activity | full-time job; the store interrupted through one workday | AV-04 (C3) | Keep the paycheck. | 390 |
| CAP-04 | an honest explanation | "what does $500 actually pay for?"; paid a builder before and ended up doing half of it | AV-02 (C4), universal | In your name. | 393 |
| CAP-05 | a personal brand letter | weeks in the settings; store still not live | AV-03 (C5) | Live, not stuck. | 387 |

CAP-01's CTA uses "Not just sitting" in place of the slate's "Loaded and live" / "No longer sitting". Both slate lines could read as a promise to load or take over the owner's existing stores (DNS-11; PT-04 is a new build).

## Ad x caption (V1/V2 ids from work/batch-skeleton.json)
| ad | status | image hook (skeleton hook_proposed) | CAP-01 | CAP-02 | CAP-03 | CAP-04 | CAP-05 |
|---|---|---|---|---|---|---|---|
| C1-V1 | launch | "Three or four stores built. Still just sitting there." | **L** | X ¹ | X ² | E | W ³ |
| C1-V2 | launch | "marketing's slowed down so much and my stores are just sitting there" | **L** | X ¹ | X ² | E | W ³ |
| C2-V1 | launch | "~600 clicks. Still no sales. Then I closed the store." | X ⁴ | **L** | X ⁵ | E | X ⁶ |
| C2-V2 | launch | "Ive had 2 stores on Shopify both failed" | X ⁴ | **L** | X ⁵ | E | X ⁶ |
| C3-V1 | launch | "Earn good money now? Don't quit to start a store." | X ⁷ | E ⁸ | **L** | E | E ⁹ |
| C3-V2 | launch | "I work a full time job, so my store only gets me after hours" | X ⁷ | E ⁸ | **L** | E | E ⁹ |
| C4-V1 | benched | "\"Contact an administrator.\" On the store I paid for." | W | W | W | **L** | W ¹⁰ |
| C4-V2 | benched | "they said they would build a store but i am building the store" | W | W | W | **L** | E ¹⁰ |
| C5-V1 | benched | "10 weeks on simple tasks. The store still isn't live." | X ¹¹ | X ¹² | E ⁹ | E | **L** |
| C5-V2 | benched | "trying to set up my store for weeks. i'm tech savvy and competent. still no simple step by step" | X ¹¹ | X ¹² | E ⁹ | E | **L** |

**Recommended primary-text load (launch ads):** C1-V1/V2 → CAP-01, CAP-04 (not CAP-05: C1 leads with HL-01, and CAP-05 x HL-01 is X) · C2-V1/V2 → CAP-02, CAP-04 · C3-V1/V2 → CAP-03, CAP-04, CAP-02, CAP-05. **Benched ads, when switched on:** C4 → CAP-04 (+ CAP-05 on C4-V2) · C5 → CAP-05, CAP-04, CAP-03.
CAP-04 fits all ten ads without conflict. It is the fallback caption for any ad whose lead caption fatigues.

Incompatible pairs and why:
1. C1 × CAP-02: the image shows stores that were built and never loaded; CAP-02 opens on a store that launched, didn't sell and was closed.
2. C1 × CAP-03: C1 is a business owner (Q-O-0103, Q-O-0124); CAP-03 opens "Got a full-time job".
3. C1 × CAP-05 (W): the letter's reader is mid-setup; the C1 owner's stores are built. They share the "a built store is not a running store" belief, so it is weak, not a contradiction.
4. C2 × CAP-01: CAP-01 opens on a business owner whose stores are built and idle; C2 is a store that launched and closed.
5. C2 × CAP-03: CAP-03 speaks to a store the reader is working on now ("only gets you after hours"); the C2 image says the store is closed.
6. C2 × CAP-05: the letter says "a store that still isn't live"; the C2 image says the store went live and closed.
7. C3 × CAP-01: C3 is salaried ("Earn good money now? Don't quit"); CAP-01 opens "You run a business".
8. C3 × CAP-02 (E): AV-04 also closed a first store ("I picked the baby store. It just didn't work" Q-O-0082), so this pair has no conflict.
9. C3 / C5 × CAP-03 / CAP-05 (E): after-hours evenings in the settings fit both avatars.
10. C4 × CAP-05: C4-V2 (she ended up doing the setup herself, Q-F-0004) fits the letter (E); C4-V1 (locked out of a finished store) does not match "weeks setting up" (W).
11. C5 × CAP-01: CAP-01 says "Logo done. Pages done."; the C5 image says the setup is still not done.
12. C5 × CAP-02: CAP-02 is about a store that launched and closed; C5's store never went live.

## Ad x headline
| ad | HL-01 recognition "Built a store that's just sitting there?" | HL-02 objection "What the $500 covers, and what it doesn't" | HL-03 desire/outcome "Your store in your name, not left at launch" | HL-04 offer/benefit "$500 to give your store more than one shot" | HL-05 situation/benefit "Full-time job? Your store can still get tested." |
|---|---|---|---|---|---|
| C1-V1, C1-V2 | **L** | E | E | E | X (owner, not salaried) |
| C2-V1, C2-V2 | X (a closed store is not "sitting") | E | E | **L** (one-shot match) | W |
| C3-V1, C3-V2 | W | E | E | E | **L** |
| C4-V1, C4-V2 | W | E | **L** (in your name, left at launch) | E | W |
| C5-V1, C5-V2 | X (the store is not built yet) | E | **L** | E | W |

HL-02, HL-03 and HL-04 pair with every ad and every caption.

**Recommended headline load:** C1 → HL-01, HL-03, HL-04, HL-02 · C2 → HL-04, HL-02, HL-03 · C3 → HL-05, HL-02, HL-03, HL-04 · C4 → HL-03, HL-02, HL-04 · C5 → HL-03, HL-04, HL-02. HL-01 is loaded only on C1 and HL-05 only on C3. Following both recommended loads keeps every text x headline combination Meta can assemble at E or better, with two W exceptions on C3 (CAP-02 and CAP-05 with HL-05).

## Caption x headline (for ads that load several of each)
| | HL-01 | HL-02 | HL-03 | HL-04 | HL-05 |
|---|---|---|---|---|---|
| CAP-01 | E | E | E | E | **X** (business owner vs full-time job) |
| CAP-02 | **X** (closed store vs "sitting there") | E | E | E | W |
| CAP-03 | W | E | E | E | E |
| CAP-04 | E | E | E | E | E |
| CAP-05 | **X** (store not live vs "built and sitting") | E | E | E | W |

The ad-level X cells above already block most incompatible caption x headline pairs: CAP-01 and HL-05 never share an ad (C1 loads CAP-01, and HL-05 is X there), and neither do CAP-02 and HL-01 (C2 loads CAP-02, and HL-01 is X there). CAP-05 and HL-01 need a manual guard. Meta mixes every loaded text with every loaded headline, so never load both on one ad. That means no CAP-05 on C1 (HL-01 leads there), and no HL-01 on C3 when CAP-05 is loaded. C5 is already safe because HL-01 is X there.
