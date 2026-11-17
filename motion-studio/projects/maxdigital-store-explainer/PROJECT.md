# MaxDigital: "a store someone else builds and runs for you" (Hebrew, 16:9)

## Brief (2026-11-17)
- Ask (owner): watch the Readymerce explainer "How to own an online store without the hassle of building it yourself"
  (64 s, English, cartoon explainer) and recreate it in Hebrew as motion graphics with a voiceover, no talking head.
- Brand: MaxDigital (maxdigital.co.il). Owner: "yes it's the same" (same offer and claims as the original ad).
- Format: 16:9 like the original (owner's choice). Voice: male narrator (owner's choice). Look: motion graphics.
- CTA: "לחצו למטה" (points at the ad's own button), as in the original.

## Decisions taken by default (autopilot), logged
| Decision | Choice | Why |
|---|---|---|
| Grammatical person | plural אתם | maxdigital.co.il speaks to "אתם" throughout |
| Voice | ElevenLabs library voice "Nimrod - Warm and Confident" (ZiofZHcEBTn5sRySe5h8), eleven_v3, 2 takes, take 1 chosen | native Israeli male, made for commercials; take 1 clearer in the hearing pass |
| Claims | the original's claims only; no numbers, no income, no results | owner confirmed the offer is the same; no number appears on screen |
| Script edits for the voice | "שאף אחד אחר לא עושה" -> "שאחרים לא עושים"; "כמעט לא" -> "בקושי" | he_lint (homograph עושה) and the hedge check |
| Engine | motion-studio canvas engine, 1920x1080, 30 fps, 2 subframes | one style, pure function of time |
| Signature device | every object draws itself as a sky-blue outline, then fills | the original's sketch-to-colour reveal, translated to motion graphics |
| Music | ElevenLabs music_v1, instrumental bed (prompt in CREDITS.md) | no licensed track supplied |

## Brand capture (maxdigital.co.il, 2026-11-17, Firecrawl branding)
- Colours: primary #00A4F0, secondary #00172E; logo colours #7DCEF4 and #1D2088. Site font "Discovery" (not available
  to us): Heebo (OFL) used for Hebrew. Logo: https://maxdigital.co.il/logo_contract.png (official file, unmodified),
  mark: https://maxdigital.co.il/favicon.png.

## Open
- A native Hebrew speaker must listen to the voice (machine hearing is unreliable in Hebrew).
- Nobody has listened to the mix.

## v2 (2026-11-17), owner notes
Owner: add trust elements ("ולא מפסיקים עד שזה עובד" after "מנהלים לך את החנות", with a popup); the voice was tired and
flat; motion graphics alone were boring: make real-looking images on Higgsfield (a store, its products, Facebook ads of
the same store, layered with entrance animations); more SFX and camera moves.

| Decision | Choice |
|---|---|
| Script | one line added, the owner's words: "...מנהלים אותה בשבילכם, ולא מפסיקים עד שזה עובד." |
| Voice | 3 takes (eleven_v3, stability 0 "creative"): Nimrod, Dorian, Nimrod+[excited]. Energy score (organic-engine audio_energy_gate.py): Dorian 61.7, others 30.9 / 27.4. Dorian (PBHwEnXdzx0yfhIO2UCH) chosen; pauses tightened (hook 110 ms, body 180 ms), speed 1.14 (house ceiling 1.16). Final: 43.8 s, 3.35 words a second, energy 65.2 |
| Example store | "VELORA" (skincare), invented for the film and labelled "חנות לדוגמה" on screen; it is not a MaxDigital client |
| Images | Higgsfield GPT Image 2.6 (2k, high): store on a laptop, product page on a phone, 2 packshots, 2 Facebook ad creatives, a night desk, a packing station, an office desk with order notifications; backgrounds removed from the laptop and the packing box for layers. An invented "4.9 rating" badge was edited out of one ad |
| Trust popups (source: maxdigital.co.il, captured 2026-11-17) | "ולא מפסיקים עד שזה עובד" (owner's line); "צוות תפעול 24/7"; "מנהל תיק קבוע"; "חנות מוכנה תוך 7 עד 15 ימים" (site: "חנות מוכנה תוך 7–15 ימים"); "בבעלות מלאה שלכם" (site: "בבעלותכם המלאה"); "500+ חנויות נבנו ומנוהלות" (site: "500+ חנויות שנבנו ומנוהלות"); "דוח ביצועים כל יום" (site: "דוחות ביצועים יומיים") |
| Camera | hook punch-in at 0 s, 10 punch-ins on key words, shakes on 5 stamps, 8 whip pans with motion blur, slow pushes on photos, a push into the phone on "keep your job" |
| Sound | ElevenLabs music_v1 bed, 122 BPM, drop on the brand; 60 effect events (Earshot code-made bank + Kenney CC0) |

## v3 (2026-11-17), owner: "the voice sounds very rushed and robotic; use the Brandify Eagle voice with emotions"
| Decision | Choice |
|---|---|
| Voice | Brandify Eagle (Y5opOXX7EecGzeA6UzMF), eleven_v3, an emotion tag per line ([warmly] [curious], [serious], [frustrated], [sighs] [tired], [excited], [confident], [proudly], [emphatic], [relaxed], [sincere]), script in audio/v3/script_tagged.txt |
| Takes | 3 (stability 0.0, 0.0, 0.5). Energy: take 3 59.6, take 1 59.1, take 2 54.6; hearing match take 3 0.88, take 1 0.83; no tag read aloud. Take 3 chosen |
| Pace | pauses over 340 ms trimmed (hook 200 ms), speed 1.07 (v2 was 1.14). 56.7 s, speech pace 2.68 words a second (v1 2.2, v2 3.35), pitch spread 21 semitones, energy 63.4 |
| Music | new ElevenLabs music_v1 bed, 108 BPM, emotional build, drop on the brand at 18.7 s |
| Picture | unchanged from v2; every cue follows the new word timings |
