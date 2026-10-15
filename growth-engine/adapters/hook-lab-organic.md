# Hook Lab, organic mode (adapter)

Pass this file and the full Post Card with every `readymerce-hook-lab` call for an organic post. Where this adapter and
the Hook Lab disagree, this adapter wins for organic posts; everything else in the Hook Lab (the 3-channel stack, the 9
gates, the A/A+ bar, the rubric, research) still applies. Source: ORGANIC-OS.md 7.3.

1. **Two jobs in 1 to 3 seconds:** topic clarity and on-target curiosity. Check the 4 S's: Subject, Stakes, Speed
   (compressed), Super clear.
2. **Kill the 4 mistakes:** delay (topic late), confusion (two readings, big words), irrelevance ("I/people" instead of
   "you/your"; nice-to-have pain), disinterest (no contrast between their belief A and our B). The card's `belief`
   says which A→B contrast to open.
3. **Triple hook:** visual, text and spoken hook say the same thing. Text hook: at most 2 lines, a specific number or
   power word, top third of the screen, about 3 s on screen. Carousels: the cover is the visual + text hook, and
   **slide 2 must work alone as a hook** (Instagram may show slide 2 first).
4. **10 hooks per post**, graded; ship only A or A+. Return the master stack plus 2 variants for trial reels.
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
  booking calendar, the shutter half down at 19:00, the boost button with 0 messages. Never a logo, a team photo or
  the happy result.
- **Persona cues:** an Albanian local business in frame (salon chair, clinic reception, shop counter, restaurant
  pass), the owner's age and clothes.
- **Rubric rows 5 and 8:** "a real body part" becomes **one real prop** (the phone, the calendar, the counter) and
  "a credibility anchor" becomes **one countable fact from the brain** (never invented).
- **Gate 9 for organic:** keep the tone rules (annoyed or comic, never ashamed), no guarantees, no invented results,
  the AI label rule in `growth-engine/production/STANDARDS.md`. The Meta ad-policy checks ("your [condition]", no
  side-by-side before and after) apply when the post may be boosted later; apply them by default.
- **Hook types with B2B shapes** (Hook Lab section 6): character in place (the unanswered DM speaks), villain mockery
  (the boost button mocks the owner's fix; mock the fix, never the owner), stop doing X ("Never answer 'Sa kushton?'
  with just a price"), hidden cause ("This is why your followers never become customers"), fear moment, named person +
  habit (a bakery owner in Tirana posting every day, zero orders), confession (real numbers only), workaround reveal
  ("She'd been answering DMs at midnight for two years"), witness ("The busiest salon on our street wasn't the one with
  the best posts"), impossible scale (a pile of unread DMs burying the counter), two futures, misdirection, challenge
  (a documented series, real tracked data only).

## Independent grading (G-HOOK)
Hook Lab grades its own stacks. For organic posts the hook-agent's top 3 stacks then go to a **fresh agent** that gets
only the persona card (AV-01 from the brain, scrolling at night, sound off first) and, per stack, the text hook, the
spoken line 1 and the concept frame. It answers: that's me / not me, what the post is about, would you keep watching,
and grades each channel. G-HOOK passes when the master stack is A or A+ on every channel from both graders.

## Concept frames are gated stills
A concept frame is frame 1 of the hook shot, so the hook shot's Shot Spec (`H-01`) is written at step 2, not step 6,
and the concept frame is a `still` asset that serves it (prompt review, crop review, as any still). The approved
concept frame becomes the start of the hook storyboard.

## Text hook length (one rule)
4 to 10 words on the reel's text hook and on a carousel cover headline (carousel-machine's "up to 12 words" is
overruled), plus an optional small label of 6 words or fewer. Drama keeps its own X7 rule (text hook optional, 6 words
at most).

## The organic Hook Library
One file per client category: `clients/<slug>/research/hook-library.md`, built from the research-scout's outliers (the
4 checks, breakout against the creator's median) instead of ad run time, with the same 3-line format entries
(label · views and breakout · spoken formula / text formula / visual formula with "where in the business"). Organic
LEARN (the analyst at 72 h and 7 d) adds each post's result per hook: skip rate, average watch time, sends, saves,
follows per reach.
