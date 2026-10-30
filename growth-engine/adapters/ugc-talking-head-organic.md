# UGC and talking head, organic adapter

For `reel_strategist_prop` (an AI presenter with a prop, H3), `reel_ugc_pov` (a phone-filmed POV of a business owner,
H3) and `reel_talking_head_real` (the owner films). Pass this file, the Post Card and
`growth-engine/production/STANDARDS.md` with the readymerce-ads-machine Part C / Section G method. Where they disagree,
this file and STANDARDS.md win for organic posts.

## 1. Who is on screen (truth rules first)
- The brain's `visual.face` decides: StraightScale is `ai_character` until the owner films real content (decision D1;
  filming clients is decision D5).
- **AI people until D1** (STANDARDS 7; brain.json D1 interim, verbatim: "AI people are only shown from behind or as
  clearly staged scenes; no AI person is presented as a real client."). AI label on per STANDARDS 7 (D1 decides whether
  to extend it).
- **An AI presenter** (the StraightScale strategist, `reel_strategist_prop`) faces the camera only as a presenter in his
  clearly staged studio set (the whiteboard). Never a client, owner or customer, never "I tried this and got X".
- **A UGC POV** (`reel_ugc_pov`) is a clearly framed POV dramatization of an owner's moment ("POV: it's 22:40 and a
  customer asks the price"). Until D1 the AI owner is shown from behind, as hands only (the POV camera on his phone), at
  a distance, or as stylized animation, never face to camera. No mouth on screen means no lip-sync: his lines are
  voice-over on the ElevenLabs master over silent keyframe shots (STANDARDS 2, modes). It never claims to be a real
  testimonial; no results, no numbers that aren't in the brain, and no confession (that needs real footage, below).
- **The real owner** (`reel_talking_head_real`): the strongest trust format, and the only route for a confession
  (`confession_pov`: real footage of the real owner in his own words). Claude writes the line table; the owner
  films 3 takes of the hook and 1 or 2 of the body on a phone at eye level, near a window; edit with
  `talking-head-recut`, captions with `embedded-captions`; no generation, so the gate isn't involved; G-TAKE and G-FINAL
  still run on the takes (frames, words, safe zones).

## 2. The pipeline for an AI presenter or POV
| Step | What | Gate |
|---|---|---|
| 0-1 | Brief from the brain, the card's angle and THE PICTURE (the one prop or demo that makes the cause visible: the phone lighting up again and again with messages nobody answers, a whiteboard with three short lines) | G-BRIEF, G-IDEA |
| 2 | Hook Lab with the B2B profile; frame 1 = the problem where it lives in the business | G-HOOK |
| 3 | Script Lab with `adapters/script-lab-organic.md`: O30 (myth buster ST6, objection crusher ST13, mistake ST7) or O60 (hidden cause ST3, case study ST11 only with a real case) | G-SCRIPT 85+, G-HUMAN-SPINE (delegated) |
| 4-5 | `pipeline.py budget` before the run's first generation (the voice, unless a concept frame came first; STANDARDS 10). ElevenLabs `eleven_v4`, the locked voice (StraightScale: `8oGKUMljR779HzpZBiE4`, "Strategist, male 45"), beats of 2 to 7 lines at 4 takes, human pauses never capped; word map, slices per STANDARDS 2 (4 to 14 s). Every voice and slice asset gets `pipeline.py gate <slug> <post_id> G-AUDIO --status PASS --by <who> --asset <ID>@v<n> --note "..."` before it is a reference or step 11 closes (STANDARDS 9) | G-BUDGET, G-AUDIO-MASTER, G-HUMAN-VOICE (once per voice), G-AUDIO, G-TIMELINE |
| 6 | Shot Specs: the presenter holds 4 to 6 s at most, then a cutaway (the room from another angle, the prop close-up, the team mid-action); every visible hand gets a line; every board or screen gets exact text and an occlusion rule; screens show states, never counts or a platform's name (STANDARDS 6) | G-PLAN, G-SPEC |
| 7 | Look bible on the client's LIB run (G-BUDGET before the first sheet): the presenter from a real reference photo (GPT Image 2, quality high, 2k, an iPhone 15 Pro candid with real skin), one master still per setting plus one cutaway still made from it; for a POV, the owner as hands, back and clothes only until D1; prop sheets for every story prop (the phone with the chat UI) | G-PROMPT-IMG, G-VIS-SHEET, G-HUMAN-LOOK once |
| 8 | A storyboard per sequence (2 to 3 panels), hook board first | G-PROMPT-IMG, G-VIS-BOARD, G-CONTINUITY, G-HUMAN-HOOKBOARD |
| 9 | Re-price the whole video (`pipeline.py budget`) and close step 9; the gate refuses every video call before it (STANDARDS 10) | G-BUDGET |
| 10 | R2 first (about 80 credits, G-HUMAN-TEST, STANDARDS 14) before the first presenter clip if it has not run. Presenter: H3 reference mode: storyboard image 1, presenter sheet, setting, the slice as audio 1; the 9-part video card; 30 to 35 words per 15 s clip; one gesture per shot; background action in every shot. POV: H3 keyframe mode, one shot per clip from its passed start frame (GPT Image 2 with the sheets as references), the voice laid in the edit | G-PROMPT-VID |
| 11-14 | Frames 1 per second, drift, Whisper words, face crops on talking takes (STANDARDS 11); edit on the ElevenLabs master; hook super 4 to 10 words; captions 1 to 4 words inside the Reels safe zone (STANDARDS 6); final checks per STANDARDS 9; then the owner on the hub | G-TAKE, G-ASSETS, G-FINAL, G-DIRECTOR, G-HUMAN-FINAL |

## 3. The traps this format has already hit
- **Writing on a board over the presenter's hand** (FL-01): the hand stays below or beside the last word with clear
  board between skin and letters; say "no letter touches his hand or sleeve".
- **A board built wrong** (FL-02): "a single wall-mounted whiteboard with one aluminium frame and one marker tray along
  its bottom edge only".
- **The phone vanishes mid-gesture** (FL-08): a hands and props line in every shot.
- **A frozen office** (FL-09): 2 or 3 named people doing named things in every shot, and the still already mid-action.
- **Gibberish on screens and banners** (FL-10): plain surfaces, no readable screens unless the prop sheet defines them.

## 4. Close and copy
- One organic CTA that fits the card's job (`adapters/script-lab-organic.md`; ORGANIC-OS 6.2): follow, save, send,
  comment (an answer to a question), keyword (only one live in the brain; StraightScale today: ANALIZA), dm, or book
  (convert posts only, said as the keyword or DM path: "comment ANALIZA; the booking button comes in the DM").
- No link, price, discount, guarantee or urgency, never "we answer within 1 hour", never "we chase the client's leads".
  The free analysis is named only on a convert post, as the keyword or DM path; no "what happens in the analysis" post
  until decision D3.
- Credits: O30 about 80 to 110 with the presenter's sheets already built; O60 about 150 to 200.
