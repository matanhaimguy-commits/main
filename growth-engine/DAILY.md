# Daily run: one post a day per client

Since 15 Oct 2026 StraightScale posts every day. A scheduled task ("StraightScale daily content",
`trig_01V1gzqwB9WdoBpTF1zyZVrZ`, every morning 06:49 Europe/Tirane) wakes the studio session that holds the
Lovable, Higgsfield and ElevenLabs connectors and runs this file. (A task that starts a fresh session gets no
connectors, so it cannot do this job.) It keeps the hub **4 days ahead**: every day from today to
today+3 has exactly one post for the client, as a draft with its time. A person approves on the Content page; the
hub's publisher posts approved items at their time (Auto-publish is on for StraightScale) and alerts about drafts due
within 24 hours.

Repo `matanhaimguy-commits/main`, branch `claude/ig-fb-chatbot-automation-zk8w44` (commit and push there).

## 0. Access
- Hub database: the Lovable connector, project `239a3368-f157-4af9-9f3c-129789693927`, `query_database`.
  `growth-engine/tools/hub.py` needs the hub host, which the cloud network blocks; write drafts with SQL instead.
- Images, video, sandbox (ffmpeg, ImageMagick, Whisper), media hosting: the Higgsfield connector. Upload a file with
  `media_upload`, PUT the bytes from the same `sandbox_exec` command that made them, then `media_confirm`; the public
  URL is `https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/<media_id>.<ext>`.
- Voice and music: the ElevenLabs connector.
- Never print or store tokens; never print `app_state` rows `settings` or `tick_target`.
- **The generation gate** (`.claude/hooks/generation_gate.py`, VISUAL-QA.md section 9) blocks every Higgsfield and
  ElevenLabs generation whose prompt, Shot Spec, references and budget haven't passed their gates. A session rooted
  above the repo runs `bash growth-engine/production/install-gate.sh` first, then proves it: `generate_image` with the
  prompt `GATE-SELFTEST` must come back blocked ("the production gate is live"). If it generates instead, stop and say
  so: never produce without the gate.

## 1. What is missing
```sql
select (scheduled_at at time zone 'Europe/Tirane')::date as day, id, kind, status, title
from content_items where business = 'straightscale'
  and scheduled_at >= date_trunc('day', now() at time zone 'Europe/Tirane') at time zone 'Europe/Tirane'
  and scheduled_at <  (date_trunc('day', now() at time zone 'Europe/Tirane') + interval '4 days') at time zone 'Europe/Tirane'
  and status <> 'failed' order by scheduled_at;
```
Every day in that window without a row gets one post. Also list `status = 'failed'` items from the last 2 days and
say why they failed in the summary (do not re-approve them).

## 2. What to make (Organic Growth OS: `growth-engine/ORGANIC-OS.md`)
1. `python3 growth-engine/tools/organic.py brain-check <slug>`: stop on blocking errors and report them.
2. The Post Card for the day: `clients/<slug>/cards/<yyyy-mm>-W<n>/` (week of the month by Monday). A day without a
   card: write one as the content-strategist agent would, from `content-map.json` (calendar template, pillars,
   series, belief focus), the idea bank / latest research, and `analytics/learnings.md`. Pick its format with
   `organic.py route <slug> <card> --prev-family <yesterday's family>`.
3. `organic.py card-check` on the card and `week-check` on its week must pass (warnings: fix or explain in the card).
   Week rules: 3 reels, 3 carousels, 1 image; no format or job two days in a row; 1+ contrarian and 1+ B7 post; a
   conversion CTA at least every 5 posts; mix near the stage target (new: reach 50, trust 35, convert 15).
4. Keyword CTAs only for keywords live in the brain (today: ANALIZA). No B8 "what happens in the analysis" post until
   decision D3; no B6 post without permitted proof or The Build; no behind-the-scenes formats without real footage.
5. Times: 19:30 Europe/Tirane, Sundays 18:00.
6. Monday run: research refresh (research-scout: 3-month window, `organic.py outliers`) and the Director memo
   (`organic.py score`, `growth-engine/GATES.md`). Friday run: next week's cards; the Director batch review.

## 3. Make it
Run the gates in `growth-engine/GATES.md` and the adapters in `growth-engine/adapters/`. Facts only from `brain.json` / `brand-kit.md` (never invent numbers, results, clients, reviews or prices; never "we answer within
1 hour", never "we chase the client's leads"; no em dashes, no hype words). Albanian, informal "ti", plain words.

**Every post runs through the production pipeline** (`growth-engine/production/README.md`; commands are
`python3 growth-engine/tools/pipeline.py ...`, run from the repo root):
1. `init straightscale <post_id> --format <format> --card <card path>`; record the early gates as they pass
   (`gate ... G-BRIEF`, `G-IDEA`, `G-HOOK`, `G-SCRIPT --score N`; the spine pick as `G-HUMAN-SPINE --by "claude (delegated)"`
   with the reason) and close steps with `step ... <n> --status done`.
2. The visual-planner agent writes one Shot Spec per slide or shot in `runs/<post_id>/shots/`; `spec-check` must pass;
   a fresh prompt-reviewer (spec mode) reviews each spec; record its JSON with `record`.
3. Per image or clip: `asset ... <ID> --type slide|cover|static|start_frame|video_clip --shots ...`, write the prompt to a
   file, `prompt ... --file F --media <ref id>:<role> ...` (the style reference is `90dad300-d86a-4173-acc2-5af7cba412a3`,
   registered as `STYLE@v1` in `runs/SS-LIB-STYLE`), a fresh prompt-reviewer checks it, `record` the report.
   Voice and music: `asset ... VO --type voice` / `--type music` and `prompt ... --file` with the exact text.
4. `budget straightscale <post_id> --planned <credits> --balance <Higgsfield balance right now>`.
5. Generate with exactly the registered prompt and references (the gate checks the hash and the order). Then
   `media ... <ID>@v<n> --id <job or media id> --file <local file>`.
6. `python3 growth-engine/tools/vqa_crops.py image <file> --run straightscale/<post_id> --asset <ID>@v<n>` (video:
   `frames`), a fresh visual-reviewer (or take-reviewer) opens every crop and writes its JSON; `record` it. A FAIL goes
   to the fix route in VISUAL-QA 5.5 as a new version (`asset` again). Carousels end with a G-SET review of the whole set.
7. `status` must show no open gates before step 14 (the hub draft). `queue --write` lists what waits for Matan.
The reviewers are fresh agents every time (agent files in `.claude/agents/`; if a type isn't registered in the session,
run a general-purpose agent told to read and follow that file). They get only the packet, never the producer's reasoning.

**Single image / carousel:** Higgsfield `gpt_image_2_5`, `aspect_ratio: "4:5"`, `resolution: "2k"`,
`quality: "medium"` (1 credit each), `medias: [{value: "e6bc8781-70fa-4450-aa10-989160b20a2e", role: "image_references"}]`
(`STYLE-TOP@v1` in `runs/SS-LIB-STYLE`: the top of the 15 Oct cover, for the type and the light; the old full cover
`90dad300` failed its review on 15 Oct: a model-drawn logo and blurred side bands, so it is no longer a reference).
**The model never draws the logo** (brand-kit: real files only): the prompt leaves the bottom-left corner calm and
empty, and after the review the real logo goes on with
`python3 growth-engine/tools/brand_overlay.py <in> <out> --client straightscale` (it refuses a busy or bright corner).
Prompt pattern (see `clients/straightscale/style-bible.md`):
> Instagram post, portrait 4:5. Match the look, type and layout of the reference image exactly: same photorealistic
> cinematic film still, 35mm, shallow depth of field, Tirana at night, warm tungsten light, deep shadows, fine film
> grain; deep red #BE0F18 is the only saturated colour. SCENE: ... a smartphone in a deep red case ... TEXT, in the
> calm dark upper area, left-aligned: small spaced capitals label '...' at top left [carousels: small gold #DD9A10
> counter 'n/N' at top right]. Headline in heavy bold geometric sans, off-white #F8F6EF: '...' with '...' inside a
> solid #BE0F18 highlight rectangle. [Smaller off-white line: '...'] Spell exactly, letter by letter: (every word with
> ë or ç, spelled out). Bottom-left corner (the lowest 9% of the height, the left 40% of the width): calm, dark,
> empty background with nothing in it: no logo, no letters, no objects (a logo is added later). [Carousels, slides 1 to
> N-1: bottom right a small #BE0F18 round button with a white arrow.] No logos anywhere, no other text, no numbers on
> screens or paper. Full-bleed photograph edge to edge: no borders, no side bars, no blurred margins.

QA: the visual-reviewer reads every letter at full size from the crop packet (step 6 above). Stray dots or specks next
to letters happen; the fix route is an edit pass (a new version, re-reviewed) or a local paint-out with the background
colour logged in `qa.md` (see `content/2026-w43-1b-carousel/qa.md`), then a fresh review of the fixed file. Export
`convert in.png -resize 1080x1350! -strip -quality 90 out.jpg`.

**Reel (quote, 12-15 s):** follow `clients/straightscale/content/2026-w42-6-reel/script.md`: a 9:16 still, a MiniMax H3
2K keyframe clip (`start_image` = an uploaded 1080x1920 JPEG, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`,
2 credits a second), an ElevenLabs `eleven_v4` voice (voice `8oGKUMljR779HzpZBiE4`, 4 takes, check each with Whisper,
keep the cleanest), burned captions and the end card with the real wordmark (`clients/straightscale/brand/wordmark-white.png`),
music ducked under the voice, -14 LUFS / -1 dBTP (STANDARDS.md). In the pipeline it is the `keyframe_reel` family: the
still is a `start_frame` (hero, zero defects), the clip a single-shot `video_clip` in keyframe mode (`start_image`, no
storyboard because nothing talks and there is one shot), the voice a `voice` asset after G-SCRIPT, the bed a `music`
asset; the take-reviewer checks the clip and the final cut (G-TAKE, G-FINAL). Story reels, animation, drama, song and
podcast pieces follow `growth-engine/production/STORY-FORMATS.md` and are made in a normal session, not in the daily
run; the daily run only places them when their run shows step 13 done.

Budget: the month's cap in `brain.json` (StraightScale 1,300 Higgsfield credits); check with `organic.py ledger <slug>` and
the Higgsfield balance before every batch, keep a 25% retake buffer, log every piece with `organic.py ledger-add`.
Tier A (song, animation) only with `angle_proven` or the month's wildcard. If the budget can't cover the card's
format, re-route to tier C and say so.

## 4. Ship
Insert one row per post (the hub refuses images outside 4:5 to 1.91:1; the SQL path skips that check, so keep 4:5):
```sql
insert into content_items (business, external_key, kind, status, title, caption, alt_text, keyword, funnel_id,
  media, cover_url, scheduled_at, notes, source)
values ('straightscale', '<yyyy>-w<ww>-<n>-<kind>', '<image|carousel|reel>', 'draft', $q$<title>$q$, $q$<caption>$q$,
  $q$<alt text, Albanian>$q$, <'ANALIZA' or NULL>, <'analiza' or NULL>,
  $q$[{"url": "...", "type": "image", "width": 1080, "height": 1350}]$q$::jsonb, '<first media or cover url>',
  '<UTC time>', $q$Native Albanian read needed (image text and caption). ...$q$, $q${"plan": "plans/<week>.md", ...}$q$::jsonb);
```
Never insert with status `scheduled` or `published`: only a person approves.

Then write `clients/<slug>/content/<key>/` (`caption.txt`, `alt-text.txt`, `hosted.json`, `item.json`, `qa.md`, and
`script.md` for reels), update the plan files, commit and push.

## 5. Report
End with three lines: what was made (days, formats, hooks), what waits for approval (with days), the spend. If
something blocked (a connector missing, a failed generation twice, credits low), say exactly what.
