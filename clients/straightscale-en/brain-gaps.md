# straightscale-en · Client Brain gaps

Checked 2026-10-28 by `organic.py brain-check`.

## Blocking

None: production may run.

## Gaps to fill (required, not blocking)

| Field | Missing | How to get it |
|---|---|---|
| package.monthly_usd_cap | the monthly Atlas generation cap in USD; until it is set G-BUDGET fails every paid generation and only free formats route | owner decision (STANDARDS.md 10 prices each format) |
| business_model.capacity | how many new clients a month the business can take | ask the owner |
| lead_magnets[WORDS] | resource or keyword flow not live yet | Conversion Agent builds it; no posts may use the keyword until then |
| messaging | one-liner, pitch, 3 value props and boilerplate the bot, site and captions reuse, approved | draft from the brain's mechanism and offer; owner approves |
| voice.samples | 3 to 5 real samples of how the owner talks | owner ramble, past posts |
| voice.register | ju or ti not decided | owner decision (section 13.3) |
| visual.ai_label | how the AI character is labeled | owner decision (section 13.1) |
| baseline | followers, 30-day reach, median views, where clients come from | account audit (Insights) + owner |
| constraints.turnaround_hours | approval contact and turnaround | contract / owner |
| belief_ladder.state | which beliefs the audience already holds | comments, DMs, sales calls; update monthly |
| proof_bank | no public proof yet: B6 posts only through 'The Build' / process (7.6) | film the first clients from day one, with permission |

## Decisions for the owner

- **E1** The method's name and step names: keep Research, Offer, Organic, Funnel, Paid ads as plain names, or name them (earlier Find, Own, Attract, Convert, Close; suggested Find, Own, Attract, Convert, Scale)? Until then: Scripts name only Patchwork Marketing; the method stays unnamed and the steps are called by what they are (EN 03 reveal plan).
- **E2** Do the sales team StraightScale provides and trains, and the CRM for every client (25 Oct operator facts), belong in the English offer? Until then: Never mentioned in content, captions or the DM bot.
- **E3** The free business analysis: what it covers beyond a look at the competitors' ads, how long, where (call or in person), what the person keeps, and how it is booked (link, calendar, DM). Also: who answers the WORDS hand-offs and sends the voice note, and should the proposed WORDS routing lines go into the hub's business profile? Recommended: Write it down; it unlocks B8 posts and the funnel's hand-off. Until then: No post explains the analysis; the WORDS funnel is not created.
- **E4** Price, capacity and the sales process after the analysis for the English offer (none is recorded; the Albanian packages do not apply). Until then: Never in content; the DM bot never quotes prices or results.
- **E5** Proof: collect the evidence files for the five owner-reported results (offer sheet) and confirm they may be shown anonymously by niche. Recommended: Collect them; B6 has no material until then. Until then: No result number on screen; B6 only through process content.
- **E6** Where is the foundation-v2 research run stored? 06-VOC_MASTER.csv (567 quotes from 414 authors), 07 and 09 exist only on the Mac (~/Downloads/Organic-Engine/) and in a cloud session's temporary copy; no repo holds them. Recommended: Commit it to a private repo (or clients/straightscale-en/research/) with push access, so every quote id can be checked. Until then: Use only quotes already cited with their Q-ids. The "567" on EN 02 and in the WORDS Sheet has no evidence file in the repo until then (offer-sheet rule).
- **E7** Patchwork form and a second avatar: the offer sheet says buyers tried several agencies ("they tried other agencies that failed them"), while the research finds AV-01 mostly never hired an acquisition firm (6 of 181 codable rows) and the song uses the DIY form. Keep the DIY form for AV-01, and add the research's AV-03 "the burned category buyer" (fits Matan's objections) as AV-02? Recommended: Keep the DIY form for AV-01; add the burned buyer only with Matan's yes. Until then: AV-01 only; agency-burn lines only as buyer quotes.
- **E8** AI labels and the host: how are Matan's HeyGen twin, AI voices and AI scenes labelled on this account, and are the twin's consent and footage in place? Until then: No twin pieces until decided; claymation and faceless pieces only.
- **E9** Cadence and budget for the English page: posts a week, videos and carousels a month, stories, posting times, and a monthly generation cap (Atlas dollars or Higgsfield credits). Until then: package fields are 0 placeholders; paid generation under this slug fails G-BUDGET until set.
- **E10** The hub: when does the business connected to @straightscale_ (straightscale) switch from the Albanian setup (analiza funnels active) to the English offer, and does the Albanian carousel from 15 Oct stay on the English grid? Where does the Albanian offer post? Until then: Before the WORDS funnel is created, run `hub.py clients` to see which hub business holds @straightscale_ and which funnels are active on it.
- **E11** Approve the messaging block (one-liner, pitch, 3 value props, boilerplate) for the bio, the DM bot and captions. Until then: Draft only; nothing reuses it until approved.
- **E12** Owner ramble: a 15 to 20 minute voice note in English (what annoys you in the industry, what clients always ask, what everyone gets wrong)? Recommended: Yes: it fills the voice samples, the contrarian vault and the story bank.
- **E13** Insights access for @straightscale_ so the baseline (followers, reach, median views) and the Learn loop can fill. Until then: Baseline stays unknown.
- **E14** The series order: is part five Funnel (EN 06) or Paid ads (the song sings ads last)? EN 06's tier A needs a wildcard slot; EN 05's CTA says "the next part" instead of "part five". Until then: EN 06 waits on the answer before any picture.

## Notes on this check (added by the Brain Builder, 28 Oct 2026; a new `--write` run drops this section)

- **voice.register** is a false gap for English: the check only knows the Albanian ti/ju choice. The register is "you
  and your" (second person), as every EN script uses.
- **Not checked by the tool, still missing:**

| Field | Missing | Who fills it |
|---|---|---|
| offer.delivers | what the free business analysis covers, how long, where, what the person keeps, how it is booked (E3) | Matan |
| business_model.price_notes, sales_process | price and the steps after the analysis for the English offer (E4) | Matan |
| research corpus | foundation-v2 (06-VOC_MASTER.csv, 567 rows; 07; 09) is in no repo; every Q-id in the demand map and the "567" on EN 02 depend on it (E6) | Matan (storage and push access), then the main session commits it |
| package | posts a week, formats, posting times, monthly generation cap are 0 placeholders (E9); G-BUDGET fails paid generation under this slug until set | Matan |
| hub business | @straightscale_ is still served by the hub's Albanian `straightscale` business with the analiza funnels (E10) | Matan in the hub dashboard |
| visual.style_bible | no style bible for the English account | Organic Director, from EN 02 to EN 06 once Matan approves a look |
| avatars | a second avatar for the agency-burned buyer (research AV-03) is proposed, not added (E7) | Matan |
| voice.adjectives | only two recorded (calm, direct); no third | owner ramble (E12) |

## Proposed monthly USD cap (28 Oct 2026, for Matan; not set in brain.json)

Budgets moved from Higgsfield credits to Atlas USD (STANDARDS.md 10). `package.monthly_usd_cap` is empty, so G-BUDGET
fails every paid generation on this slug and the router offers only free formats. The cap is Matan's decision (E9).

Per-piece prices with 25% retakes (`config/organic.json` `usd`, prices of 28 Oct): carousel $0.96 to 1.92, single
image $0.07 to 0.89, quote reel $0.75 to 1.19, motion reel up to $2.34, animation short $1.35 to 2.05, strategist or
UGC reel $1.58 to 4.15, narrated story $4.00 to 5.23, song $2.48 to 5.93, drama up to $8.28. A 10 s OmniHuman
talking-object clip is about $0.90 (+25%).

| Month (about 5 posts a week, 22 pieces) | Pieces | At the top of each range |
|---|---|---|
| Carousels | 8 | $15.36 |
| Single images | 4 | $3.56 |
| Quote and motion reels | 6 | $10.59 |
| Tier B story reels (narrated, strategist, animation short) | 3 | $15.69 |
| Tier A (song, drama or animation, wildcard) | 1 | $8.28 |
| **Total** | 22 | **$53.48** |

**Proposed cap: $60 a month** (the plan above at the top of every range, plus about $6 for a re-test or a new cast's
sheets). At 7 posts a week with two tier A pieces it would be about $100. The live Atlas balance on 28 Oct was about
$7 (shared with every session), so whichever cap is set, the balance needs a top-up first.
