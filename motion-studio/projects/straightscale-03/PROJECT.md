# StraightScale · Reel 03 "Qartësia" (clarity), after a reference reel

One file that says what this job is, where it stands, and what was decided. Update it at every stage.

## Brief
- Request (user, 13 Oct 2026): "generate a similar reel like that same idea and concept, similar visuals, just for
  us for StraightScale", reference https://www.instagram.com/reel/Da0DayIpsie/ (divyansh.fx_, "Faceless video
  edit", 26.4 s, 348K plays, posted 15 Jul 2026).
- Reference idea: attention is expensive; every second spent trying to understand you loses prospects, momentum
  and opportunities; the leaders aren't louder, they're clearer; clarity isn't an advantage, it's leverage.
- Our film: the same idea in StraightScale's voice and market (Albanian, informal "ti"), our own copy, our brand
  (ivory, crimson, Playfair Display + Montserrat), our real logo, our CTA. Nothing of the reference is copied:
  no footage, no assets, no text; the grammar is studied and rebuilt in code.
- CTA: "Shkruaj ANALIZA në komente" (free 45-minute analysis), as in reels 01 and 02.
- Platform: Instagram/Facebook Reels, 9:16 master 1080x1920, about 32 s.
- Voiceover: yes. The reference is voice-led and the user asked for a voice on reel 01; same ElevenLabs voice
  "StraightScale - Strategist (male, 45)". (Decided, not asked again: logged here.)
- Music: our own, sampled CC0 instruments (Lemo sampler), as reel 02.
- Rules (brief): no invented numbers, reviews, client names, testimonials or deadlines; no prices; no em dashes;
  no hype words; no founder; avoid gold text on ivory and crimson text on charcoal.
- Facts on screen: "1.800" active ads using the word "cilësi" (Meta Ad Library, 11 Oct 2026, from the brief);
  "45 minuta" (offer, brief). Nothing else numeric except the decorative stopwatch and countdown (no claims).

## Status
Stage: delivered (v1)
Current version: v1 (`deliver/v1/`)
Next step: the user's listen and a native Albanian check, then revisions into v2
Blockers / open questions: native Albanian check; nobody has listened.

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 2026-10-13 | English cut ("Make it in English"): same film source with a language switch (index.html?lang=en), own English script, same voice (take 2 of 4), English score timed to the English voice | a separate English project; translating the reference's English text | one source keeps both cuts in step; the Albanian frames and audio were proven unchanged (100/100 frame hashes, bit-identical music and effects) | user request; Claude |
| 2026-10-13 | Keep the comment keyword ANALIZA in the English cut | an English keyword (e.g. ANALYSIS) | it is the brief's keyword and the one used across reels 01-03; changing it needs a new voice line | Claude (ask the user) |
| 2026-10-13 | Engine: canvas engine (focus pulls with canvas blur, subframe motion blur on the stopwatch and pills) | HyperFrames | the look is blur and fast props; render.mjs gives 4-subframe motion blur | Claude |
| 2026-10-13 | Voice take 1 of 4 | takes 2-4 (35.2-35.4 s) | tightest pacing, closest to the reference's punch; transcript exact | Claude |
| 2026-10-13 | Adapt the reference's structure beat for beat, on ivory with one crimson accent | invert to charcoal; reel-02 S-path world | the user asked for the same concept and similar visuals; ivory + crimson is the brand's light system and keeps the reference's white, airy feel | Claude |
| 2026-10-13 | Add one StraightScale fact beat: ~1.800 active ads say "cilësi" | keep the reference's script shape only | makes "the winners aren't louder" concrete for Albania with a sourced number from the brief | Claude |
| 2026-10-13 | Ending line "Qartësia nuk është stoli. Është strategji." | literal "advantage / leverage" | the alliteration works in Albanian and says what StraightScale sells (strategy) | Claude |

## Approvals
| Date | What | By | Notes |
|---|---|---|---|

## Log
- 2026-10-13 · reference fetched through Apify (instagram-scraper metadata, transcript add-on, 48 + 16 frames) · ok; the video file itself could not be downloaded (Instagram CDN blocked), so no audio was measured
- 2026-10-13 · project folder, brand assets and fonts from reel 02 · ok
- 2026-10-13 · script v1, 4 ElevenLabs takes (flow zjE7Y8jCk3cAUhX5iqM5) · take 1 chosen (34.56 s, tightest), Scribe timings match the script word for word
- 2026-10-13 · beat sheet (treatment §5), canvas-engine build, styleframes round 0 · 6 fixes
- 2026-10-13 · score + foley (audio/score.py), word-timed ducking, master -14.0 LUFS / -1.5 dBTP · ok
- 2026-10-13 · review rounds 1-2 (docs/review_log.md) · stopwatch hand fixed; final render 60 fps x 4 subframes
- 2026-10-13 · English cut: script, 4 takes (take 2, 33.84 s, Scribe exact), page and score moved to named cues (Albanian proven unchanged), English styleframes, safezone ok, seekcheck PASS, mix -14.0 LUFS · rendering
- 2026-10-13 · final: 2220 frames, seams clean, -14.0 LUFS / -1.5 dBTP after AAC, round 3 · delivered v1 (master CRF 21, viewing copy CRF 23)
