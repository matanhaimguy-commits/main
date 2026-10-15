# UGC and talking head, organic adapter

For `reel_strategist_prop` (an AI presenter with a prop, H3), `reel_ugc_pov` (a phone-filmed POV of a business owner,
H3) and `reel_talking_head_real` (the owner films). Pass this file, the Post Card and
`growth-engine/production/STANDARDS.md` with the readymerce-ads-machine Part C / Section G method. Where they disagree,
this file and STANDARDS.md win for organic posts.

## 1. Who is on screen (truth rules first)
- The brain's `visual.face` decides: StraightScale is `ai_character` until the owner films (decision D7).
- **An AI presenter** (the StraightScale strategist) is a presenter, never a client, never a customer, never "I tried
  this and got X". AI label on (STANDARDS section 7).
- **A UGC POV** is a dramatized owner's moment ("POV: it's 22:40 and a customer asks the price"). It never claims to be
  a real testimonial; no results, no numbers that aren't in the brain; AI label on.
- **The real owner** (`reel_talking_head_real`): the strongest trust format. Claude writes the line table; the owner
  films 3 takes of the hook and 1 or 2 of the body on a phone at eye level, near a window; edit with
  `talking-head-recut`, captions with `embedded-captions`; no generation, so the gate isn't involved; G-TAKE and G-FINAL
  still run on the takes (frames, words, safe zones).

## 2. The pipeline for an AI presenter or POV
| Step | What | Gate |
|---|---|---|
| 0-1 | Brief from the brain, the card's angle and THE PICTURE (the one prop or demo that makes the cause visible: the phone with 14 unanswered DMs, a whiteboard with 3 lines) | G-BRIEF, G-IDEA |
| 2 | Hook Lab with the B2B profile; frame 1 = the problem where it lives in the business | G-HOOK |
| 3 | Script Lab with `adapters/script-lab-organic.md`: O30 (myth buster ST6, objection crusher ST13, mistake ST7) or O60 (hidden cause ST3, case study ST11 only with a real case) | G-SCRIPT 85+ |
| 4-5 | ElevenLabs `eleven_v4`, the locked voice (StraightScale: `8oGKUMljR779HzpZBiE4`, "Strategist, male 45"), beats of 2 to 7 lines at 4 takes, human pauses never capped; word map, slices of 14 s or less | G-AUDIO-MASTER, G-TIMELINE |
| 6 | Shot Specs: the presenter holds 4 to 6 s at most, then a cutaway (the room from another angle, the prop close-up, the team mid-action); every visible hand gets a line; every board or screen gets exact text and an occlusion rule | G-SPEC |
| 7 | Look bible on the client's LIB run: the presenter from a real reference photo (GPT Image 2, quality high, 2k, an iPhone 15 Pro candid with real skin), one master still per setting plus one cutaway still made from it, prop sheets for every story prop (the phone with the chat UI) | G-VIS-SHEET, G-HUMAN-LOOK once |
| 8 | A storyboard per talking sequence (2 to 3 panels), hook board first | G-VIS-BOARD, G-CONTINUITY, G-HUMAN-HOOKBOARD |
| 9-10 | H3 reference mode: storyboard image 1, presenter sheet, setting, the slice as audio 1; the 9-part video card; 30 to 35 words per 15 s clip; one gesture per shot; background action in every shot | G-BUDGET, G-PROMPT-VID |
| 11-13 | Frames 1 per second, drift, Whisper words; edit on the ElevenLabs master; hook super 4 to 10 words; captions 1 to 4 words inside the Reels safe zone | G-TAKE, G-FINAL |

## 3. The traps this format has already hit
- **Writing on a board over the presenter's hand** (FL-01): the hand stays below or beside the last word with clear
  board between skin and letters; say "no letter touches his hand or sleeve".
- **A board built wrong** (FL-02): "a single wall-mounted whiteboard with one aluminium frame and one marker tray along
  its bottom edge only".
- **The phone vanishes mid-gesture** (FL-08): a hands and props line in every shot.
- **A frozen office** (FL-09): 2 or 3 named people doing named things in every shot, and the still already mid-action.
- **Gibberish on screens and banners** (FL-10): plain surfaces, no readable screens unless the prop sheet defines them.

## 4. Close and copy
- One organic CTA that fits the job; the keyword only if it's live in the brain (StraightScale today: ANALIZA).
- No price, no offer, no guarantee, never "we answer within 1 hour", never "we chase the client's leads".
- Credits: O30 about 80 to 110 with the presenter's sheets already built; O60 about 150 to 200.
