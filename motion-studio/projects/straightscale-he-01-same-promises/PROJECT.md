# StraightScale (Hebrew, Israel) · 01 "What everyone promises"

One file that says what this job is, where it stands, and what was decided. Update it at every stage.

## Brief
- Client / product: StraightScale, for Israeli business owners, in Hebrew. The method stays unnamed (Research, Offer,
  Organic, Funnel, Paid ads). The free entry is a 45-minute analysis that includes a growth and marketing plan made for
  that business, plus a live look at its competitors' ads (Matan, 1 Nov 2026).
- Goal of this piece and the single action (CTA): top of funnel. Owners see that when their ad says what everyone in
  their field says, the client compares on price, and they leave with one test to run on their own ad. CTA: soft
  (save it, send it to a business-owner friend). No keyword. (Matan, intake 5 Nov: "30-45 s, soft ending".)
- Audience: Israeli owners of service businesses who advertise on Facebook and Instagram (clinics, advisers,
  contractors, studios, consultants). They already believe "my ads don't work" or "people only ask about price".
- Platform and formats: Instagram Reels, 9:16 master 1080x1920. Re-layouts (4:5, 1:1, 16:9) only if asked.
- Length: 30 to 45 s.
- Language: Hebrew voice and on-screen text; English check line under each script line for the record.
- Voiceover: yes. Matan's HeyGen voice clone, speaking as Matan (intake 5 Nov). Blocked until the HeyGen file hosts are
  allowed in the environment's network settings (probe 5 Nov: resource/files2/static/dynamic.heygen.ai and
  api/upload.heygen.com refused). Matan approves the script before the voice is generated.
- Music: synthesized or sampler score in code ($0), ducked under the voice.
- Brand assets: clients/straightscale/brand (logo-full.png, symbol.png, wordmark-white.png, brand.json).
- References: refbank picks (docs/treatment.md section 1) and the StraightScale pattern bank (vault, Idea runs
  2026-11-01/research/2): a live audit of real ads is a format no Israeli creator in this niche uses yet.
- Proof and data: docs/research/ad-library-2026-11-05.md. Only "8 out of 14 mortgage advisers, in their ad's headline,
  say one of two things: free, or save" (Meta Ad Library, Israel, active ads, 5 Nov 2026). Never "all" or "everyone".
- Rules: no proof numbers or results, no prices, no follow-up, reply speed, CRM or sales-team claims, no guarantees,
  no hype words, no em dashes; plural address; never show an advertiser's name, logo or screenshot (typed headlines
  only); no AI person presented as a client.
- Paid generation: none ($0, intake 5 Nov). HeyGen voice credits are logged per call.
- Deadline: none given.

## Status
Stage: styleframes done (round 2, every axis 8+); silent draft v2 answers the round 4 fresh review (N1 to N9)
Current version: draft v2, silent, `renders/draft-v2-silent.mp4` (40.3 s); not approved, not delivered
Next step: Matan's read-aloud of the script (gate 5e), then the voice, `tools/retime.py audio/words.json`, score and
foley (stage 9), review rounds 2 and 3, final render.
Blockers / open questions: HeyGen file hosts blocked by the environment network (voice). Matan to allow them. Matan to
decide the optional sample headline labelled "דוגמה" (built, off by default).

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 2026-11-05 | The draft runs on scratch timing in ONE file, `film/timing.json`: every cue is anchored to a spoken word, so real word timings are a data change (`tools/retime.py`) | hard-coded seconds per scene | the voice is blocked; retiming must not touch code | producer session |
| 2026-11-05 | Key line in the top band, captions only for the words the key line does not show | full captions under every key line | the same words twice crowds a 9:16 frame; sound-off still gets every spoken word | producer session |
| 2026-11-05 | Tape over the business name instead of a drawn thumb | a thumb shape (script line 8) | a drawn hand looks cheap next to paper and ink; tape stays in the paper world | producer session |
| 2026-11-05 | Sample headline "דוגמה": built as a slot, off by default (HyperFrames variables `exampleEnabled`, `exampleText`) | write a sample ourselves | Matan writes it or keeps the empty caret (script.md section 5, question 4) | producer session |
| 2026-11-05 | The end card opens out of the blinking caret | a cut to charcoal | the caret is what survives the last transition | producer session |

## Approvals
| Date | What (brief, concept, script, VO, styleframes, cut vN) | By | Notes |
|---|---|---|---|

## Log
- 2026-11-05 · intake answered by Matan (topic, his HeyGen voice, 30-45 s soft ending, $0) · brief written
- 2026-11-05 · Ad Library pulled (mortgage advisers, physiotherapy) · 8 of 14 mortgage-adviser headlines say free or save; physio too mixed
- 2026-11-05 · HeyGen hosts probed · blocked; voice waits
- 2026-11-05 · styleframes and silent draft v0 (HyperFrames 0.8.150, Concept A "The stamp") · built in `film/`: a small
  `index.html` that only wires the parts; one file per part in `film/src/` (desk, slip, ink, stamp, sticker, tally,
  band for the key lines, source, captions, viewer's slip, hint, camera, end card; the choreography in `scenes/pile.js`
  and `scenes/stamping.js`; positions and camera framings in `layout.js`, every on-screen word in `content.js`); one
  timing file `film/timing.json` (12 lines, 91 words with estimated starts, 26 cues); styles in `film/styles/`; tests in
  `film/tests/` and `tools/test_timing.py`. Fonts and the white wordmark copied into `film/assets/` (served files).
  Tools: `tools/timing_scratch.py` (scratch timing from docs/script.md), `tools/retime.py` (real word timings from
  audio/words.json), `tools/contact.py` (phone-size contact sheets). Styleframes: `docs/styleframes/` (round 1 and 2
  sheets, 4 full frames). Draft: `renders/draft-v0-silent.mp4` (40.3 s, 30 fps, silent). Contact sheet:
  `docs/contact-draft-v0.jpg`. Checks (seekcheck 24 samples, HyperFrames check with the bottom 400 px caption zone,
  pacing.py, unit tests) all pass; results and the three worst problems in `docs/review_log.md`. Beat sheet in
  `docs/treatment.md` section 5.
- 2026-11-05 · draft v1 (silent) for the round 3 fresh review (FAIL; coordinator's decisions D1 to D8) · price tag in
  Heebo 800 "₪?" read right to left (D1); 21 new word cues with the stamp, finger shadow, tape press, word-by-word
  underline, settle bounce and camera following them (D2); line 11's pointer in the top band (D3); the stamp drawn
  as a rubber stamp with a wooden handle, neck ring and rubber layer, turning over at the hook to show its mirrored
  face (D4, new `film/src/stamp-body.js`); word reveals without hard masks (D5); source label 46 px clear of the pile
  (D6); end card centred on x 540 (D7); hover beside the headline (D8). New files `cover.js`, `underline.js`;
  `hint.js` removed. `renders/draft-v1-silent.mp4`, `docs/contact-draft-v1.jpg`, `docs/strips-draft-v1.jpg`; checks
  in `docs/review_log.md`. Not committed (the coordinator commits after the next fresh review).
- 2026-11-05 · draft v2 (silent) for the round 4 fresh review (FAIL on pacing only; coordinator's decisions N1 to N8) ·
  story events on word cues through 25-36 s (the competitors' identical slips slide in, line up on "אחד", part, are
  pushed off on "בפגישה"; your placeholder struck and backspaced; the old reflex "חינם" typed, struck, deleted; the push
  into the caret in three steps) and an earlier, middle-first cascade at 3-5.5 s (N1, N9); a hand's shadow with a
  fingertip (N2, new `finger.js`); opaque tape (N3); the logo starts after the card has opened (N4); charcoal stamp face
  with red ink (N5); right-aligned second lines (N7); words start at 60 % ink (N8). New files `rivals.js`,
  `headline.js`, `finger.js`. Energy 3-5.5 s 2.05 to 3.57, 25-36 s 2.17 to 2.90 (same method). `renders/draft-v2-silent.mp4`,
  `docs/contact-draft-v2.jpg`, `docs/strips-draft-v2.jpg`; checks in `docs/review_log.md`. Not committed.
