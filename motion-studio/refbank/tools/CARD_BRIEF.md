# Brief for writing reference cards (used by the agents that build the bank; reuse it for refreshes)

You turn one proven viral reel into a breakdown card that a motion designer (or an autonomous reel machine) can
use to make a *new* film with the same grammar for a client. You never saw or heard the video itself: you work
from sampled frames, a time-segmented AI scene description (what is seen and heard), a transcript when there is a
voiceover, the caption and the stats. Be precise about what you can see; say "not visible in frames" rather than
inventing.

## Inputs per reference
A package JSON (path given to you) with: `id` (use it exactly), `url`, `platform`, `creator`, stats (`plays`,
`likes`, `shares`, `saves`, `comments`, `followers`), `posted`, `dur`, `caption`, `music`, `ai_segments` (list of
{startSecond, endSecond, description}), `transcript_key` (or null), and `frames` = {store, prefix, step, count}.

## Steps per reference
1. **Frames.** Read every frame with `ReadMcpResourceTool` (server `Apify`), URI
   `http://api.apify.internal:3333/v2/key-value-stores/<store>/records/<prefix><NNNN>.jpg` for NNNN = 0001 ..
   count (4 digits). Issue many reads in one message (they run in parallel). Each result says `blobSavedTo <path>`.
   Copy the files, in frame order, to `/home/user/main/motion-studio/refbank/frames/<id>/f_<NNNN>.jpg` with one
   bash command. If `count` is unknown or a read says the record is missing, list the keys first:
   `http://api.apify.internal:3333/v2/key-value-stores/<store>/keys?prefix=<prefix>&limit=200` (small JSON).
2. **Transcript** (if `transcript_key`): read
   `http://api.apify.internal:3333/v2/key-value-stores/<transcript_store>/records/<transcript_key>`.
3. **Metrics + sheet:** `python3 /home/user/main/motion-studio/refbank/tools/frames_metrics.py
   /home/user/main/motion-studio/refbank/frames/<id> --step <step> --id <id>
   --out /home/user/main/motion-studio/refbank/metrics/<id>.json`. It prints the numbers and writes `sheet.jpg`
   in the frames folder.
4. **Look** at `sheet.jpg` with the Read tool (and at 2-4 individual frames full size where the hook or the
   signature device needs a closer look). Combine with the AI segments and transcript to reconstruct the film.
5. **Write the card** to `/home/user/main/motion-studio/refbank/cards/<id>.md`, following
   `/home/user/main/motion-studio/refbank/TEMPLATE.md` exactly (front matter keys and section headings). Use slugs
   from `/home/user/main/motion-studio/refbank/TAGS.md` for category, hook, devices, energy, palette, sound,
   engine, fit. If you truly need a slug that isn't there, use it and list it in your final report (do not edit
   TAGS.md yourself). Copy pacing numbers from the metrics JSON (`cuts_per_10s`, `mean_s_between_big_changes`,
   `change_rhythm_cv`, `quiet_share_2fps`, `hook_change_0_2s`) and the top 3-5 `palette` hexes into `palette_hex`.

## Card quality bar
- **The film in one line**: concrete ("A giant SKIMS pillow drops onto a NYC street and a car bounces off it"),
  not generic ("a creative CGI video").
- **Why it stops the scroll**: what is on screen at 0, 0.5, 1 and 2 s, the hook text or first spoken line verbatim
  if known, and the mechanism.
- **Beat map**: 5-12 rows with real timestamps from frames/segments. Every row: what's on screen, what moves,
  sound (from the AI description: music, VO, SFX).
- **Signature device**: precise enough that someone could rebuild it without seeing the reference (geometry,
  timing, camera, material).
- **Pacing read**: interpret the numbers (rests, where energy peaks, how it ends, loop or not).
- **Why it works**: the retention mechanics (open loop, escalation, payoff timing, rewatch/loop trigger, comment
  or share trigger such as "guess", "tag a friend", relatability, awe).
- **Steal / Leave**: steal = grammar (structure, device, timing, camera, sound logic). Leave = their characters,
  IP, music, words, brand marks, exact layouts. We never ship third-party pixels, words or music.
- **Build it in our studio**: which engine (TAGS `engine`), scene plan in 3-6 steps, the hard part and how to
  solve it, and honest difficulty. Our stack: canvas 2D engine (60 fps, subframe motion blur, springs, any 2D
  drawing, fake-3D with projection math), HyperFrames (HTML+GSAP, 447 registry effects, WebGL via software only,
  ~16 s render per second), Lemo-Opuscar painterly styles, Claude Animation Base characters (slow), collage. No
  Blender, no GPU. Real 3D simulation (cloth, softbody, fluids, photoreal CGI over footage) is difficulty 4-5 and
  needs `gen-video`/`gen-3d` (paid, needs approval) or client footage, or a stylised 2D re-imagining (say which).
- **Business translations**: three one-line film ideas for real client types (agency, SaaS, local service,
  e-commerce, restaurant, health, finance, real estate...). No invented numbers or testimonials in them.
- **Scores**: `wow` 1-5 (how hard it stops the scroll: 5 = impossible not to watch); `relevance` 1-5 (how useful
  the grammar is for client marketing reels: 5 = directly usable for a business message, 1 = pure entertainment
  with nothing transferable); `difficulty` 1-5 for *our* stack.
- Write in plain English, no hype words, no em dashes. 400-900 words per card body.

## Final report (your last message)
One line per card: id, category, signature device, wow/relevance/difficulty. Then any new slugs you used, and
any reference you could not complete and why.
