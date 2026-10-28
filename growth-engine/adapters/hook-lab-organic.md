# Hook Lab, organic mode (adapter)

Pass this file and the full Post Card with every `readymerce-hook-lab` call for an organic post. Where this adapter and
the Hook Lab disagree, this adapter wins for organic posts; everything else in the Hook Lab (the 3-channel stack, the 9
gates, the A/A+ bar, the rubric, research) still applies. Source: ORGANIC-OS.md 7.3.

## Proven formats only (owner rule, 28 Oct 2026; this section wins over everything below)
Why: the EN 04 to 06 hooks were written from nothing, graded by AI readers, and came out in written English nobody
says in a reel ("decided before you ever quoted"). An AI grader's "A" is an opinion, not evidence. What counts as
proof is a post that already won with this buyer, and the buyers' own words.
1. **Every stack starts from a proven format.** Hook Lab's H3 List 3 ("original, written from the rubric") is off
   for organic until one of our own posts proves a new format in Live results. Every stack is List 2: a format entry
   from the client's Hook Library (`clients/<slug>/research/hook-library-en.md`, ids `HF-nn`) at 3x or more over its
   creator's median (prefer 10x+, the only ones whose structure may be copied), its mad-lib filled in. Cite the id.
   No library entry fits the topic: say "only N formats fit" and stop; never pad with invented formats.
2. **The words are the buyers' words.** Fill the slots from `clients/<slug>/research/buyer-phrases-en.md` (verbatim
   lines with ids) and cite the ids. The spoken line must share real words with the cited phrases.
3. **Say it out loud.** The spoken line is something an owner would say to a friend: 11 words or fewer, short common
   words, no written-register or marketing words ("quote", "solutions", "leverage", "framework", "proposal"...)
   unless the buyers wrote them. Read it aloud once; if you'd never hear it in a reel, cut it.
4. **Code check before any grader.** Write the stacks to `docs/hooks.json` (`id, text, spoken, visual, format_id,
   voc_ids, story`) and run `python3 growth-engine/tools/organic.py hooks <slug> docs/hooks.json`. Only PASS stacks
   go on. The tool fails a stack with no proven format, no buyer words, a long or stiff spoken line, a text hook outside
   4 to 10 words, no contrast or payoff word, or a banned word.
5. **Graders can fail a hook, never prove it.** The blind fresh-grader read (G-HOOK) stays, but only as a clarity
   check on stacks that already passed 1 to 4: what is this about, would you keep watching, which words were unclear.
   Report their grades as readers' opinions, next to the format's real numbers, never as the reason a hook is good.
6. **Organic first** (owner, 28 Oct 2026): a hook is proven by organic breakout videos (views far over the creator's
   own median), not by ads. HA ads (30+ days running) are a fallback only when no organic format fits, and say so.
   Where the organic proof comes from (Apify is too costly and unreliable; Instagram lists reels only behind a login):
   - **Views:** the same creators' YouTube Shorts, through TranscriptAPI `list_channel_videos` (`tab: "shorts"`,
     about 48 shorts and 1 credit per page). Save each page as JSON, then
     `organic.py yt-import @handle page1.json ... --out items.json` and `organic.py outliers items.json --days 0`.
   - **What was said:** TranscriptAPI `get_youtube_transcript` for a Short (1 credit), or free for any public reel or
     short with `growth-engine/tools/reel_transcribe.sh` in the Higgsfield sandbox (yt-dlp audio + faster-whisper).
   - Library entries from Shorts are `HF-nn` with the breakout, the spoken first sentence verbatim and its formula.
7. **The owner sees the evidence.** Each master stack is shown with its source post (creator, views, breakout, the
   original spoken line) and the buyer phrases it uses, so the owner can judge the proof, not our grade.

1. **Two jobs in 1 to 3 seconds:** topic clarity and on-target curiosity. Check the 4 S's: Subject, Stakes, Speed
   (compressed), Super clear.
2. **Kill the 4 mistakes:** delay (topic late), confusion (two readings, big words), irrelevance ("I/people" instead of
   "you/your"; nice-to-have pain), disinterest (no contrast between their belief A and our B). The card's `belief`
   says which A→B contrast to open.
3. **Triple hook:** visual, text and spoken hook say the same thing. Text hook: 4 to 10 words (STANDARDS 6 and "Text
   hook length" below) in 2 lines at most (a carousel cover 2 or 3 lines); a concrete noun, or the number of items the
   post itself lists ("3 mistakes"), never a result or any other number that is not in brain.json; no hype words; top
   third of the screen, frame 1 to about 3 s. Carousels: the cover is the visual + text hook, and
   **slide 2 must work alone as a hook** (Instagram may show slide 2 first).
4. **10 hooks per post**, graded; ship only A or A+ (at most 3 rounds, then the next idea: "Replace, don't escalate"). Return the master stack plus 2 variants for trial reels.
5. Rotate types across the week (the card's `hook_type`): contrarian, hidden cause, mistake / "never ever", case study,
   comparison or tier list, question, list, personal story, teaching.
6. Negativity aims at the **mistake**, never at the viewer.
7. **No offer in the hook** (gate 7 holds). The paid-ad "buyer lock" becomes **on-target reach**: the right owner thinks
   "that's me"; a stranger outside the avatar may scroll on, and that is fine.
8. Organic metrics replace ad metrics in H8: skip rate, average watch time, sends per reach (reach job), saves per
   reach (trust job), follows; not CPA or CTR.
9. Language: Albanian, "ti" until decision D2, about 5th-grade words, "you/your".

## B2B and services profile (replaces Hook Lab's DTC-health rules; AI-VIDEO-PIPELINE section 5, issue 15)
Hook Lab's visual rules were tuned on health products ("the body part already swollen", "one real-looking body part",
"never medical severity"). For service businesses, read them like this:
- **Frame 1 is the problem where it lives in the business:** the phone with the unanswered "Sa kushton?", the empty
  booking calendar, the shutter half down at 19:00, the boost button pressed again while the inbox stays empty. Never a
  logo, a team photo or the happy result. Screens show states, never counts, and no real platform's logo or name
  ("the inbox", "the phone"; STANDARDS 6).
- **Persona cues:** an Albanian business from the avatar in frame (AV-01: salon chair, clinic reception, kitchen
  showroom, private-school front desk), the owner's age and clothes. Until D1 an AI owner is seen from behind, as
  hands only, at a distance or as stylized animation (STANDARDS 7).
- **Rubric rows 5 and 8:** "a real body part" becomes **one real prop** (the phone, the calendar, the counter) and
  "a credibility anchor" becomes **one countable fact from the brain** (never invented).
- **Gate 9 for organic:** keep the tone rules (annoyed or comic, never ashamed), no guarantees, no invented results,
  the AI label per STANDARDS 7 (D1 decides whether to extend it). The Meta ad-policy checks ("your [condition]", no
  side-by-side before and after) apply when the post may be boosted later; apply them by default.
- **Hook types with B2B shapes** (Hook Lab section 6). Anecdotes in the brand's voice are clearly framed POV
  dramatizations ("POV: ..."), never stated as something that happened (STANDARDS 7): character in place (the
  unanswered DM speaks), villain mockery (the boost button mocks the owner's fix; mock the fix, never the owner), stop
  doing X ("Never answer 'Sa kushton?' with just a price"), hidden cause ("This is why your followers never become
  customers"), fear moment, named person + habit ("POV: Arta runs a clinic in Tirana, posts every day, and the booking
  calendar stays empty"), confession (only the real owner on real footage, with numbers from the brain; never an AI
  person), workaround reveal ("POV: you're answering messages at midnight again"), witness ("POV: two clinics on one
  street, and the busy one posts less"), impossible scale (a pile of unread messages burying the reception desk), two
  futures, misdirection, challenge (a documented series, real tracked data only).

## Replace, don't escalate (Matan, plan of 28 Oct; wins over Hook Lab's loops and the lines below)
- **At most 3 rounds** per post (a round: write or fix, code check, the blind grade). A hook passes only when **both** of
  2 fresh blind graders give A or A+ on **visual, text and spoken**. Short of that after round 3, or sooner when a round
  shows the idea itself is the problem, **replace it with the next idea in the bank** (the next `HF-nn` format with
  buyer phrases that fit the card); don't keep polishing it.
- **Never escalate to Matan.** A hook, script or take that runs out of rounds is replaced or simplified by the main
  session; nothing goes to the owner as G-HUMAN-ESCALATE for it. The owner sees hooks only at G-HUMAN-HOOKBOARD.
- A concept frame or take that fails 3 times gets **a simpler shot** (fewer elements, one subject, bigger in frame),
  as a new asset; if the simpler one fails 3 times too, the hook is replaced.

## Real-frame rule (plan of 28 Oct)
The **visual** grade comes only from a real concept frame image, made in the series look (`openai/gpt-image-2` on
Atlas, `/edit` with the series' look references or `/text-to-image`, at 1152x2048 for 9:16), never from a written
description of the frame. No frame yet, no visual grade: the graders grade text and spoken only, and the stack can't
pass G-HOOK until the frame exists and is graded.

## Pre-grade checklist (the graders' recurring failure reasons; check before every round)
1. **Frame 1 on a phone:** one subject, big, little clutter. View it at phone size (about 360 px wide); busy or small
   fails.
2. **Spoken line adds to the text,** never repeats it: the text hook and the spoken line say the same idea in different
   words (the triple hook), they don't read the same sentence twice.
3. **One reading only:** no word or phrase that can be read two ways ("quote", "close", "lead" in the wrong sense);
   swap it for a word with one meaning.
4. **Concrete payoff:** the payoff is a thing you can see or count (a full calendar, a booked call), not an abstract
   one ("growth", "clarity", "results").

## Independent grading (G-HOOK)
Hook Lab grades its own stacks. For organic posts the hook-agent's top 3 stacks then go to a **fresh agent** that gets
only the persona card (AV-01 from the brain, scrolling at night, sound off first) and, per stack, the text hook, the
spoken line 1 and the concept frame. It answers: that's me / not me, what the post is about, would you keep watching,
and grades each channel. G-HOOK passes when the master stack has passed `organic.py hooks` (proven format, buyer words,
plain spoken English: "Proven formats only" above) AND is A or A+ on every channel from both graders. A stack that
never passed the code check cannot pass G-HOOK however the graders score it.

## Concept frames are gated stills
A concept frame is frame 1 of the hook shot, so the hook shot's Shot Spec (`H-01`) is written at step 2, not step 6,
and the concept frame is a `still` asset that serves it (G-PROMPT-IMG before the call, G-VIS after, as any still).
It is frame 1, so it is hero (zero defects, STANDARDS 3 and 9): register it with `--hero`
(`pipeline.py asset <slug> <post_id> <ID> --type still --shots H-01 --hero`) or as a `start_frame`. The model is
`openai/gpt-image-2` on Atlas in the series look (the real-frame rule above; Higgsfield is off since 28 Oct). Its call is a generation, so it needs a G-BUDGET PASS from the last 24 h first
(`pipeline.py budget`, STANDARDS 10). The approved concept frame becomes the start of the hook storyboard.
Every finalist's concept frame passes G-VIS before the grader sees it, so a losing finalist's frame is already closed
for G-ASSETS (step 11). A frame that fails 3 attempts gets a simpler shot, then the hook is replaced ("Replace, don't escalate" above); a
dropped finalist's frame is closed with a G-VIS OVERRIDE, note "dropped finalist, not used", when the owner next
records one (never a question of its own).
Exceptions: a song run makes no picture before G-HUMAN-SONG, so text and spoken are graded first and the visual grade
waits for the concept frame made after step 4 (the real-frame rule; `song-organic.md` 1); podcast follows `podcast-organic.md` 3.

## Text hook length (one rule, STANDARDS 6)
4 to 10 words on the reel's text hook and on a carousel cover headline (carousel-machine's "up to 12 words" is
overruled), plus an optional small label of 6 words or fewer. Drama keeps its own X7 rule (text hook optional, 6 words
at most).

## The organic Hook Library
One file per client category: `clients/<slug>/research/hook-library.md`, built from the research-scout's outliers (the
4 checks, breakout against the creator's median) instead of ad run time, with the same 3-line format entries
(label · views and breakout · spoken formula / text formula / visual formula with "where in the business"). Organic
LEARN (the analyst at 72 h and 7 d) adds each post's result per hook: skip rate, average watch time, sends, saves,
follows per reach.
