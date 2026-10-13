# StraightScale · Reel 02 "Klientët që kthehen" (clients who come back)

One file that says what this job is, where it stands, and what was decided. Update it at every stage.

## Brief
- Client / product: StraightScale, business growth partner, Tirana. The Client Engine (Foundation → Build → Grow).
- Goal of this piece: a second organic reel with a new angle (reel 01 was "patchwork marketing / customers only
  compare price"). Teach one useful thing, then the CTA.
- CTA: "Shkruaj ANALIZA në komente" (Comment ANALIZA); free business analysis, 45 min, Tirana office or at the
  client's business, no obligation; we also show their competitors' ads.
- Audience: owners of service businesses in Albania (clinics, salons, studios, consultants, schools, trades), 35-60.
- Platform and formats: Instagram/Facebook Reels, organic. 9:16 master (1080x1920). 4:5/1:1/16:9 not requested this round.
- Length: about 40 s.
- Language: Albanian voice and on-screen text, informal "ti"; English check line under each Albanian line.
- Voiceover: yes (the user asked for one after reel 01). Same brand voice as reel 01: ElevenLabs
  "StraightScale - Strategist (male, 45)".
- Music: our own (sampler/synth), no paid music generation.
- Brand assets: real logo files from the user's Drive (5 Oct 2026): full logo, white wordmark, symbol
  (`assets/brand/`, see manifest.json). Fonts from the brief: Playfair Display (headlines), Montserrat (body).
  straightscale.com could not be captured (blocked by this environment's network policy).
- Rules (brief): no founder name or face; never invent numbers, reviews, client names, testimonials or
  deadlines; don't lead with "we answer within 1 hour"; don't say we chase or follow up the client's leads (we
  build them a system); no prices; no em dashes; no hype words; avoid gold text on ivory and crimson text on charcoal.
- Proof we may show (brief): our team grew a consulting firm €15K → €55K/month; a courses business €30K → €100K/month;
  a new consulting business €0 → €140K/month.
- Service facts used (user's Drive, "STRAIGHTSCALE — FINAL OFFER" and "PHASE 2.5 — NEVER LOSE A LEAD + CLIENTS WHO
  COME BACK", 9 Oct 2026): "Clients Who Come Back and Bring Friends": rebooking reminders, recall messages
  ("it's been 6 months since your check-up"), review requests after every visit, a referral offer; recall timed to
  each service's interval (dental hygiene 6 months, hair roots 4-6 weeks, facials 4 weeks); comeback offers add
  value, never cut the price.
- Paid generation: ElevenLabs voice only (implicitly approved: the user asked for a voice). No paid images, video or music.

## Status
Stage: delivered (stage 12)
Current version: v1 (`deliver/v1/`)
Next step: the user's listen and a native Albanian check, then revisions into v2
Blockers / open questions: native Albanian check of script, on-screen text and VO (as for reel 01); nobody has listened yet.

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 2026-10-13 | Score from CC0 sampled instruments (VSCO 2 CE, VCSL), D minor turning to D major when the client lights up | our numpy synth (reel 01), paid music generation | real instruments sound premium; no paid generation was approved; the key change carries the story | Claude |
| 2026-10-13 | Engine: motion-studio canvas engine, not HyperFrames | HyperFrames (planned in the treatment) | the film is one camera ride at up to ~2,600 px/s; it needs real subframe motion blur (render.mjs, 60 fps x 4) | Claude |
| 2026-10-13 | Zoomed-in mark drawn from a trace of the real symbol, handing over to the PNG at native size | upscale the PNG (soft at 3x), redraw (banned) | sharp at 3.4x zoom and faithful (IoU 0.999) | Claude |
| 2026-10-13 | Concept A "The S path" (the logo's S channel is the client's path) | B phone book (needs invented names, imitates WhatsApp), C orbits (generic) | built from the brand's own mark; one survivor element; ends on the logo | Claude |
| 2026-10-13 | Voice take 4 of 4 (36.56 s) plus a 3.0 s music-only pause for the proof figures | takes 1-3 | steadiest pacing, clean ends, no clipping | Claude |
| 2026-10-13 | Use the logo's measured colours for the mark world: red #BE0F18, gold #DD9A10 | brief values #B31217 / #D4AF37 | the film is built from the real symbol; colours must match it exactly | Claude |
| 2026-10-13 | Angle: retention ("every month you start from zero; clients who come back and bring a friend") | likes-not-clients (already used in ad A7), speed-to-lead (V1, A2), lost enquiries (A3), attribution (A4), Google profile | unused in the 13 Oct ads and reel 01; taught from the user's own offer; fits "teach one useful thing" | Claude |
| 2026-10-13 | Voiceover yes, same voice as reel 01 | no VO | user asked "what about the voiceover" after reel 01 | user (earlier) |

## Approvals
| Date | What (brief, concept, script, VO, styleframes, cut vN) | By | Notes |
|---|---|---|---|

## Log
- 2026-10-13 · setup.sh, project folder from template · ok
- 2026-10-13 · logo files found in Drive and downloaded (full, white wordmark, symbol) · ok
- 2026-10-13 · straightscale.com capture · blocked (proxy 403), Firecrawl out of credits
- 2026-10-13 · read Drive: FINAL OFFER, Final Ads (13 videos, angles used), PHASE 2.5 retention flows · angle chosen
- 2026-10-13 · references measured (docs/refs/pacing.txt), 3 concepts, art direction (docs/treatment.md §1-3) · A chosen
- 2026-10-13 · script v1 (88 words), 4 ElevenLabs takes, take 4 chosen, Scribe word timings (audio/words.json) · ok
- 2026-10-13 · beat sheet (treatment §5), mark traced, styleframes round 0 · fixed 6 issues
- 2026-10-13 · score + foley (audio/score.py), word-timed ducking (audio/mix.py), master -14.0 LUFS / -1.5 dBTP · ok
- 2026-10-13 · review rounds 1-2 on 15 fps drafts (docs/review_log.md) · fixed 4 issues; final render 60 fps x 4 subframes
- 2026-10-13 · final: 2460 frames, seams clean, -14.0 LUFS / -1.5 dBTP after AAC, review round 3 · delivered v1
