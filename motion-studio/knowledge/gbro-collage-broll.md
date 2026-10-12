# gbro Collage B-roll: what it is, how it works, and how we do it without Codex or Gemini

Written 12 Oct 2026 from a full read of `references/gbro-collage-broll` (SKILL.md, README, `scripts/`,
`agents/`, `evals/`, the four demo GIFs). The skill is written in Chinese; everything quoted here is
translated except the English prompt templates, which are verbatim. Nothing was generated and no credits
were spent; the "how we'd do it" sections were planned against the live tool schemas in this session
(read-only `creative_get_model_guide` and `models_explore` calls).

---

## 1. What it is

- **Repo:** github.com/pyang5166/gbro-collage-broll. **License: MIT**, (c) 2026 狗哥笔记 ("Gouge Notes").
  It's free to use commercially, but keep the license notice if we copy its code or text.
- **What it does:** it takes one ~5 s line of voiceover (an opinion or abstract idea), compresses it into
  **one sharp visual metaphor**, and outputs a premium **editorial halftone paper-collage B-roll** clip.
  The clip assembles from an empty colour field: pieces slide in, snap into place and lock, with a
  stop-motion feel. It's meant to sit under the talking head or voiceover as a cutaway.
- **Default deliverable:** 9:16, 5 s, 720x1280, 24 fps, silent MP4.
- **Engine:** it's a prompt/process skill, not a renderer. The still comes from **Codex's built-in
  `image_gen` tool**. The video comes from **Google `gemini-omni-flash-preview`** (first-frame / last-frame
  interpolation), called through the google-genai Interactions API with the user's paid `GEMINI_API_KEY`.
  A legacy Veo 3.1 script is included but not used by default.
- **Its core idea is the process, not a prompt:** three mandatory approval gates. The human spends their
  attention on taste, and money is spent only after the cheap stages are approved.

### File map

| path | what it is |
|---|---|
| `SKILL.md` | The whole method: gate protocol, success criteria, visual-spec schema, colour rules, image and video prompt templates, QA, project layout, troubleshooting |
| `README.md` | Overview, requirements table, install, FAQ (all in Chinese) |
| `agents/openai.yaml` | Codex interface: display name "Collage B-roll", default prompt, `allow_implicit_invocation: true` |
| `evals/evals.json` | 4 behaviour evals, all about gate discipline (see section 2.8) |
| `scripts/check_setup.sh` | Self-check: GEMINI_API_KEY, ffmpeg/ffprobe, python >= 3.10, venv `~/hyperframes-projects/.omni-venv` with google-genai >= 2.10.0 |
| `scripts/generate_video.py` | Gemini Omni Flash client: single or batch jobs (JSON), thread-pool concurrency (default 3), uploads local images via the Files API, downloads the result |
| `scripts/upload_file.py` | Files API upload + poll until ACTIVE (exponential backoff); warns on videos > 25 MB |
| `scripts/generate_veo_first_last.py` | Legacy: Vertex AI `veo-3.1-fast-generate-001` with `last_frame`, output to GCS, `gcloud storage cp`, pads 8 s to 10 s with `tpad`, 5-frame contact sheet |
| `assets/demo-*.gif` | 4 demos, 240x427, 10 fps, 5.0 s each |

---

## 2. The method

### 2.1 The three gates (the heart of it)

1. **Gate 1: metaphor approval.** The skill writes the visual metaphor in words only. No image, no
   video, no model call. Then it stops and waits for "ok", "approved", "all approved", or notes per item.
2. **Gate 2: still approval.** Only after Gate 1 does it write the visual spec and image prompt, generate
   the final still, save it, build a **numbered contact sheet** of the stills, and stop again. Still no
   video.
3. **Gate 3: video.** Once the still is approved it goes straight to video generation without asking
   which model to use, then runs full QA.

- **Partial approval** works in batch mode: only the items that were approved advance (eval 4: "1, 2 and
  4 pass, 3 and 5 need changes" advances only 1, 2 and 4).
- **Why the gates exist** (README FAQ): a wrong metaphor or a wrong still that goes straight to video
  burns real API money. Changing words at Gate 1 is free, and regenerating a still is far cheaper than
  rerunning a video.

### 2.2 Phase 1: finding the visual metaphor

Compress the line into **one visual proposition**. Extract four things:

- **Core meaning:** what the viewer must finally understand.
- **Emotion:** calm, surprised, urgent, sudden clarity, absurd, ironic.
- **Action verb:** open, connect, leak, bind, archive, light up, compress, fork, assemble.
- **A visualisable metaphor object:** a machine, clock, film strip, filing cabinet, console, rulebook,
  funnel, track or chess piece.

Rules:

- **Never put the script on screen word for word.**
- **One line gets one metaphor**, built from **3 to 6 key objects**. More elements weaken the meaning
  and make the video model's assembly unstable.
- **In a batch, give the metaphors a narrative order**, e.g. first show manual effort and lost
  experience, then show standards settling in and the split between human and AI work.

Gate 1 output for each item: core meaning, emotion, a one-sentence visual proposition, 3 to 6 key
objects, background colour plus accent colours, and the assembly order. The skill's own example,
translated:

```text
1. Core meaning: experience gets used up again every single time
   Visual metaphor: a skilled editor circles a giant film-reel clock, cutting frame by frame; the clock
                    completes a full turn yet yields only one short strip of finished film
   Key objects: film clock, editor, scissors, short film strip
   Colour: burnt-orange field, cream and pale-teal accents
   Assembly order: clock -> editor with scissors -> film -> the final short output
```

### 2.3 Collage art direction (the success criteria)

- One line expresses **one clear metaphor**.
- A batch shares **one design language** but **not one background colour**: avoid all-blue.
- The **background is a strong, flat, even colour field**, chosen by meaning.
- The **subject's skeleton is black-and-white halftone photographic cut-outs.**
- **Key cards, buttons, film strips, rulebooks etc. may be coloured cardstock** (red, yellow, teal,
  orange, purple, cream), but colour must serve the information hierarchy, never decoration.
- **Every piece of paper has crisp cut edges, a cream keyline, a soft low-opacity shadow and paper
  grain.**
- **The motion is assemble-from-empty**, not a slight drift, wobble or slow zoom.
- **No captions, no full voiceover text, no logos, no watermark, no UI.**

**Colour semantics** (pick the field from the meaning):

| field | means |
|---|---|
| burnt orange / red | time being spent, labour, urgency |
| mustard yellow | tools, warnings, experience leaking away |
| deep (ink) green | cognition, taste, a system reset |
| deep purple | standards, consolidation, long-term memory |
| teal | judgement, collaboration, automatic execution |

### 2.4 The visual spec (written before any image prompt)

```json
{
  "script_meaning": "",
  "visual_metaphor": "",
  "style_signature": "flat bold color field, mixed black-and-white halftone cut-outs and colored cardstock accents, crisp cut edges, cream keylines, soft paper shadows, editorial paper collage",
  "aspect_ratio": "9:16",
  "color_field": { "background_hex": "", "accent_colors": [], "paper_grain": "fine uncoated-paper fiber" },
  "elements": [ { "what": "", "role": "", "motion": "", "placement": "" } ],
  "composition": { "layout": "", "negative_space": "", "final_frame": "" },
  "motion_plan": "structure first, subject or cards second, action and result last",
  "avoid": "typography, readable letters, numerals, logos, watermark, UI, subtitles, glossy 3D, photoreal environment"
}
```

### 2.5 Still prompt (verbatim template; fill the brackets)

```text
Use case: ads-marketing
Asset type: final still frame for a 9:16 image-to-video B-roll clip
Primary request: Create a finished editorial paper-collage image expressing [one-sentence visual proposition].
Scene/backdrop: perfectly flat [colour] paper field [hex] with subtle uncoated paper fiber.
Style/medium: premium editorial stop-motion paper collage; black-and-white halftone photographic cut-outs mixed with selective [accent colour] colored cardstock.
Composition/framing: vertical 9:16 locked poster frame; central subject within the middle 70 percent; generous clean color-field negative space; 3–6 large separable paper groups for later assemble-from-empty animation.
Materials/textures: visible printed halftone dots, crisp machine-cut edges, thin warm-cream paper keylines, soft low-opacity physical drop shadows.
Constraints: [the relationship this metaphor must make readable at a glance].
Avoid: no typography, no readable letters, no numerals, no logos, no watermark, no UI, no subtitles, no glossy 3D, no photoreal environment, no clutter.
```

Notice what does the work: "**3–6 large separable paper groups for later assemble-from-empty
animation**" makes the still animatable, and "**central subject within the middle 70 percent**" keeps
it safe under platform UI.

**Still QA:** Does the metaphor read at a glance? Is the subject concentrated? Is there any fake text,
logo, watermark or UI? Is there enough clean colour field to assemble from empty? Are there 3 to 6
clear large groups, not a screenful of fragments? Does the batch share a texture while varying colour?
Results go in `gate2-qa.md`. Regenerated stills get `still-contact-sheet-v2.jpg`, `-v3` and so on, and
old sheets are kept for comparison.

### 2.6 Video: first frame / last frame assembly

**Frames:**

```bash
# last frame = the approved still, normalised to 1080x1920
ffmpeg -y -i frames/last-frame-original.png -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" frames/last-frame.png
# first frame = an EMPTY sheet of the same background colour
ffmpeg -y -f lavfi -i color=c=0x<HEX>:s=1080x1920 -frames:v 1 frames/first-frame.png
```

The first frame keeps one base object only if the user explicitly asks not to start from empty.

**Assembly order:** base structure -> character or key card -> connectors -> action -> final result.

**Video prompt (verbatim template):**

```text
Paper-collage stop-motion assembly, using Image 1 as the exact empty first frame and Image 2 as the exact completed last frame. In one continuous locked-off vertical shot, open on the empty flat [color] paper field.

Assemble the scene piece by piece with crisp physical stop-motion timing: [describe, in order, how the 3–6 elements slide in, snap into place, connect and complete the action]. End by holding the supplied completed composition.

Preserve the exact 9:16 framing, [hex] color field, colored cardstock accents, uncoated paper grain, halftone dots, cream keylines, crisp cut edges and soft shadows. Restrained tactile 2D paper craft only.

No scene cuts, no camera movement, no zoom, no morphing, no new objects, no text, no letters, no numbers, no logos, no watermark, no UI, no sound.
```

**Batch job file** (`omni-jobs.json`, one object per clip):
`{ "prompt", "image": [first-frame.png, last-frame.png], "output": ".../omni/run-v01/final-5s.mp4", "aspect_ratio": "9:16", "duration": 5 }`.

**What `generate_video.py` actually does:**

- Uploads each local image through the Files API, then polls until it is ACTIVE.
- Calls `genai.Client(api_key).interactions.create(model="gemini-omni-flash-preview", input=[image, image, text], response_format={type: "video", aspect_ratio, duration: "5s", delivery: "uri"})`.
- Downloads `output_video.uri` with `?alt=media` and the `x-goog-api-key` header.
- Duration must be an integer from 3 to 10 s. Jobs run in a thread pool (`--concurrency 3`), and it
  prints a SUCCESS/FAILED summary.
- If you hit a legacy-SDK schema error, use the shared venv; never fall back to Veo.

**Force a silent deliverable** even though the prompt says "no sound":
`ffmpeg -y -i final-5s.mp4 -map 0:v:0 -c:v copy -an final-5s-noaudio.mp4`.

### 2.7 Video QA

- **Contact sheet:** `ffmpeg -i final-5s-noaudio.mp4 -vf "fps=1,scale=270:480,tile=5x1" -frames:v 1 contact-sheet.jpg`.
- **Pass criteria:**
  - The first frame is close to an empty field (a sliver of paper at the edge is acceptable).
  - The middle shows the structure, figures and cards arriving one by one, not everything fading in.
  - No cuts, zooms, 3D or drift into photoreal.
  - No fake text, logos, watermark or UI.
  - The final frame matches the approved still. Small pose or detail drift is a pass if the meaning is
    intact; don't rerun for it.
  - The file is 720x1280, 24 fps, 5 s, with no audio track.
- **End-frame comparison:** extract the video's last frame and place it side by side with the approved
  still (`end-frame-comparison.jpg`).
- **Batch overviews:** `omni-contact-sheet-all.jpg`, `video-first-frame-all.jpg` (proves every clip
  really starts empty) and `end-frame-comparison-all.jpg`. Per-item verdicts, including passes with
  flaws and why, go in `gate3-qa.md`.
- **Troubleshooting:**

  | problem | fix |
  |---|---|
  | Paper shows at the edge of the first frame | Tolerable. If it must be strictly empty, build the opening in a layered tool (HyperFrames) |
  | Weak assembly | Fewer elements, and spell out "slide in / snap into place" piece by piece |
  | The end frame drifts | Strengthen "Image 2 is the exact completed last frame" and "End by holding the supplied completed composition" |
  | Fake text appears | Go back and regenerate the still; never patch it with the video prompt |
  | One job fails | Rerun only that job |

### 2.8 Project layout and evals

- **Project folder:** `~/hyperframes-projects/YYYY-MM-DD-collage-broll-<title>/` (dated in Asia/Shanghai
  time).
- **Top-level files:** `brief.md`, `visual-spec.json`, `imagegen-prompts.md`, `omni-jobs.json`,
  `gate2-qa.md`, `gate3-qa.md`, the contact sheets and overview images.
- **Per item:** a folder `NN-<concept>/` holding `omni-prompt.txt`, `frames/{last-frame-original,first-frame,last-frame}.png`
  and `omni/run-v01/{final-5s.mp4, final-5s-noaudio.mp4, contact-sheet.jpg, video-last-frame.jpg, end-frame-comparison.jpg}`.
- **Evals** test only gate behaviour:
  1. Gate 1 gives one metaphor and stops, with no generation.
  2. Gate 2 makes the still and spec plus a numbered sheet, then stops, with no video. It honours "don't
     make every background blue".
  3. Gate 3 runs Omni automatically, with exact empty first and approved last frames, 5 s 9:16, audio
     stripped, contact sheets and an end-frame check, and never Veo.
  4. Partial approval advances only the approved items.

### 2.9 When the skill itself says not to use it

- When you need precise layer control, occlusion, camera moves through the scene or an editable
  timeline. Use a layered HTML/animation tool (HyperFrames) instead.
- When you only want a video prompt.
- When you need real people, product ads or an on-camera presenter.
- When the user wants transparent, editable layers (it never splits layers).

### 2.10 What the four demos show (frames sampled at 2 fps)

| demo | metaphor (README caption) | assembly |
|---|---|---|
| purple | "many people collaborate to press out a sci-fi film" | Empty field -> a halftone hand-press -> an orange cardstock funnel lands on top -> a figure climbs a ladder -> more figures -> halftone photos rain into the funnel -> a teal film strip curls out of the bottom |
| yellow | "a mistake gets mass-amplified by the printing press" | A press builds itself part by part -> a halftone landscape photo drops in -> a red crack splits it -> printed copies stream out and tile into a growing grid of cracked copies |
| red | "the director's hand blocks the moves on a chessboard" | A folded cream chessboard unfolds -> two halftone figures stand up as chess pieces -> a teal projector slides in -> a yellow light cone fans open -> a suited hand enters from the top and places a third piece |
| teal | "scissors cut the camera's track" | A folded map unfolds -> a halftone movie camera and a red pin drop on -> a yellow ladder-track snakes down -> a film strip slides in from the left -> red scissors snip it |

Patterns worth stealing:

- A new piece lands roughly every 0.4 to 0.6 s, and the finished composition holds for the last ~1 s.
- Pieces enter from the frame edges.
- **Fold-outs** (a map or board unfolding) are the opening move in half the demos.
- A **hand from off-frame** is a great closer.
- Photographic halftone grey carries the subject, and **one or two cardstock colours carry the
  meaning**: the red crack, the yellow light cone, the teal film.
- Everything is centred in the middle ~70%.

---

## 3. Dependencies, and what replaces each one here

| gbro needs | what for | in this Claude Code session |
|---|---|---|
| Codex built-in `image_gen` | the Gate 2 still | **ElevenLabs `creative_generate_image`** / `creative_edit_image`, or **Higgsfield `generate_image`** (both live here), or a code-built still (route C below) |
| `GEMINI_API_KEY` (paid, per use) | Gate 3 video billing | Not needed. **ElevenLabs offers the same Omni family** (`gemini-omni-1.1-flash`) on our ElevenLabs credits. Higgsfield has `kling3_0`, `minimax_h3`, `seedance_2_5` and `flux_3_video` with start and end frames |
| `google-genai >= 2.10` in `~/hyperframes-projects/.omni-venv` | the Interactions API client | Not needed: the MCP tools replace the script |
| ffmpeg / ffprobe | first frame, normalising, stripping audio, contact sheets | ffmpeg 6.1 is installed: all gbro ffmpeg commands work as written |
| Python >= 3.10 | the scripts | installed (not needed if we skip the scripts) |

### What the session's tools can do (checked read-only on 12 Oct 2026)

**ElevenLabs (`mcp__ElevenLabs__creative_*`):**

- **`creative_generate_image`:**
  - Default model `gpt-image-2.5-sunburst`, the closest match to Codex's image_gen (an OpenAI gpt-image
    model).
  - Also listed: `gpt-image-2` (layouts, up to 10 references), `gemini-3-pro-image` (editing, composing
    several images, keeping a character consistent across shots), `flux-3-image` / `flux-2-pro` (strict
    prompt adherence, multiple references), `recraft-v4.1` (graphic/vector looks) and
    `birefnet-v2-bg-removal` (cut-outs).
  - Default `generations_count: 4`: the user picks one, which is literally Gate 2. `estimate_only: true`
    prices a run first.
- **`creative_edit_image`:** edits an image node already on the flow (`connect_from` is required). Use
  it to fix fake text, recolour the field to a brand hex, or remove a piece.
- **`creative_generate_video`:**
  - The model guide says **`gemini-omni-1.1-flash` supports start/end frame interpolation**, at
    360p/720p/1080p/4k, 3 to 10 s.
  - **`gemini-omni-flash` (1.0) does not interpolate start/end frames**, so pick 1.1.
  - Start/end frames **cannot be combined with image references** on the same node.
  - It **generates audio**, so strip it with ffmpeg (gbro already does).
  - **360p is very fast**: use it as a cheap draft of the motion before paying for 1080p.
  - The guide says to keep prompts short (1 to 2 sentences for motion) and to "describe the starting
    view, the path between, and what the final frame reveals". gbro's long template still works, but
    trim it.
  - Generations are asynchronous: poll `creative_get_flow_run_status`.
  - Before wiring frames, check with `creative_get_model_schema` / `creative_get_flow` how this
    workspace names the start and end inputs on the node. That was not checked here.
- **Getting local files onto a flow:** `creative_create_asset_upload` -> PUT bytes ->
  `creative_finalize_asset_upload`, which returns a node_id for `connect_from`. To carry a picked image
  variation forward, use `creative_add_flow_asset_node`. Keep the still and the video on one flow
  (`creative_create_flow` first).

**Higgsfield (`mcp__Higgs__*`):**

- **`generate_image`, model `gpt_image_2_5`:**
  - Variants `flare`/`sunburst`, quality low to max, 1k/2k/4k, aspect ratios including 9:16.
  - **`background: "transparent"`**: this is what makes the hybrid route below possible.
  - `count` 1 to 4, `get_cost: true` to preflight.
- **`generate_video` models with both `start_image` and `end_image` roles:**

  | model | duration | resolution | audio | notes |
  |---|---|---|---|---|
  | `kling3_0` | 3–15 s | std / pro / 4k | `sound: "off"` (cheaper) | 9:16 |
  | `minimax_h3` | 4–15 s | 2K | n/a | 9:16 |
  | `minimax_h3_max` | 5–15 s | 480p / 768p | n/a | fast |
  | `seedance_2_5` | 4–30 s | 480p / 720p / 1080p | `generate_audio: false` | `draft: true` makes a 480p draft you can finalise at 1080p within 7 days via `draft_job_id`: a paid preview built in |
  | `flux_3_video` | 5–20 s | 720p / 1080p | `generate_audio: false` | |

- Upload local frames with `media_upload` -> PUT -> `media_confirm`, then pass the media_id with role
  `start_image` / `end_image`. Wait with `jobs_wait`.
- Other useful tools: `remove_background` (cut-outs) and `upscale_video` (if a clip comes back at 720p).

**Local, free:** `hyperframes remove-background` (in the hyperframes CLI) for cut-outs.

---

## 4. Four ways to make collage B-roll in our pipeline

### Route A: the gbro method, swapping the tools (closest to the original look)

1. **Gate 1 (free):** Claude writes the metaphor per section 2.2. The brief's approval stands in for
   "ok".
2. **Gate 2:**
   - Fill the still template (2.5) and set the field hex from the client's brand palette.
   - Generate with ElevenLabs `creative_generate_image` (`gpt-image-2.5-sunburst`, 4 variations) or
     Higgs `generate_image` (`gpt_image_2_5`, `aspect_ratio: "9:16"`, `resolution: "2k"`,
     `quality: "high"`).
   - Download it and run our own still QA, including zooming in for fake text.
   - The approved still becomes `last-frame.png`.
3. **Gate 3:**
   - Make the empty first frame with ffmpeg (as gbro does).
   - Upload both frames.
   - Generate with `gemini-omni-1.1-flash` (ElevenLabs; same family as gbro's default) or `kling3_0`
     with `sound: off` (Higgs).
   - **Draft first** (Omni at 360p, or Seedance `draft: true`), then finalise.
   - Strip audio, and run gbro's QA: contact sheet, first-frame check, end-frame comparison.
4. **Conform for the reel:**
   - `ffmpeg -i in.mp4 -vf "scale=1080:1920:flags=lanczos,fps=60" -an out.mp4`. Duplicated frames at
     60 fps keep the stop-motion look.
   - Or Higgs `upscale_video` if 720p looks soft.

**Strengths:** organic motion that code can't fake (hands entering, paper unfolding, pieces tumbling),
and real photographic halftone.
**Weaknesses:** costs credits per try, timing isn't frame-exact (you can't land the snap on a beat),
the first frame isn't guaranteed empty, the end frame drifts, fake text creeps in, and it isn't
editable after delivery.

### Route B: hybrid, generated pieces animated in code (recommended for premium client work)

This gets gbro's look with our timing control, and it is what the skill itself says to do when you
need layers and a timeline.

1. **Gate 1** as above, but write the **element list as separate layers** (3 to 6), each with its
   entry edge, landing spot and beat.
2. **Gate 2** generates two things:
   - The **composed still**, for client approval of the look.
   - **Each piece on its own as a transparent PNG**: Higgs `gpt_image_2_5` with
     `background: "transparent"`, or generate on a flat colour and cut out with `remove_background`,
     `birefnet-v2-bg-removal` or `hyperframes remove-background`. Same style prompt and the same
     "black-and-white halftone photographic cut-out, cream keyline" words, so the pieces match.
   - Real client photos (product, team, location) can be used instead: run them through the code
     halftone filter below and they become collage pieces, with no AI imagery at all.
3. **Animate in our canvas engine** (`window.seek(t)`, `render.mjs`): position, entry path, snap and
   shadow per piece, all closed-form (section 5). The final frame is exact and the first frame is truly
   empty.
4. **Time it to the beats.** Each snap lands on a beat from `beats.json` and fires a paper SFX.
5. **Text, if the reel needs it,** goes in our own type layer in the negative space, never inside the
   generated imagery.

**Cost:** only the image generations. No video credits, and everything is re-editable.

### Route C: code-only halftone collage (free, deterministic, fully on-brand)

This is all canvas 2D inside a motion-studio page (`<canvas id="c">`, 1080x1920, `window.seek(t)`).
Everything is pre-rendered once at load and only composited per frame.

1. **Colour field:**
   - A flat brand hex.
   - **Paper grain:** a static noise layer multiplied over everything, plus ~1,500 faint fibre strokes
     from a seeded LCG. Claude Animation Base's `makePaper()` / `makeGrain()` in `src/core.js` are
     exactly this and can be ported.
2. **Halftone pieces:**
   - **Source:** a photo (client asset, licensed stock, or an AI cut-out), or a vector shape for
     cardstock pieces.
   - **The filter:** convert to luminance, then on a **45° rotated grid** (cell 6–10 px at 1080 wide)
     draw an ink-coloured dot per cell with radius `r = cell * 0.5 * sqrt(1 - L)` (area proportional to
     darkness).
   - Do it once into an offscreen canvas per piece.
   - **Ink:** a near-black warm grey (`#1E1B18`), never pure black. **Paper:** cream (`#F4ECDD`), never
     pure white.
   - A slight levels curve first (contrast up) gives that newsprint punch.
3. **The cut:**
   - Each piece's outline is a polygon with tiny seeded jitter (machine-cut, slightly irregular), or a
     noisy torn edge for "torn" pieces.
   - **Cream keyline:** fill the outline grown by 5–8 px in cream, then clip to the outline and draw the
     halftone inside.
4. **Cardstock accents:**
   - A flat accent colour from the palette, with the grain multiplied on.
   - Optional: one faint fold crease (a thin lighter line beside a thin darker line).
5. **Shadow:**
   - `shadowColor rgba(20,15,10,.22)`, `shadowBlur ~10`, offset `(5, 7)` when the piece is lying flat.
   - While a piece is "lifted" (moving in), grow the offset and blur with its lift height, so it
     visibly lands.
6. **Motion: assemble-from-empty with stop-motion timing.**
   - **Quantise time to 12 fps** for the pieces (`tq = Math.floor(t * 12) / 12`, like Animation Base's
     `onTwos`). Let only the grain or nothing move on 60.
   - **Each piece:**
     - slides in from the nearest frame edge on a slight arc;
     - decelerates with a closed-form spring (`lib/motion.js` `spring()`), overshooting 1–3%;
     - **snaps:** the shadow tightens and the piece takes a 1-frame 2% squash;
     - then holds.
   - **Replacement-animation boil:** on each held 12 fps frame, add a ±0.6 px / ±0.25° seeded jitter
     (`hash(pieceId, frameIndex)`). That is what makes real stop-motion feel handmade.
   - **Fold-out reveal:** 2D only. Draw the piece as two halves, and scale the folding half's width by
     `cos` from 0 to 1 with a crease shadow. No perspective projection.
   - **Hands:** a halftone hand cut-out entering from off-frame to place the last piece.
   - **Order and pacing:** structure -> subject -> connectors -> action -> result, one new piece every
     0.4–0.6 s, and hold the finished composition at least 0.8–1 s.
7. **Render:**
   - `node render.mjs --fps 60 --sub 1 --dur 5 --w 1080 --h 1920`.
   - Use `--sub 1`: motion blur fights the crisp stop-motion look. If the slides look strobey, blend
     subframes only during a slide.

**Pros:** free, exact brand colours, frame-exact beat sync, a truly empty first frame and the exact
final frame, no fake text, editable forever, and reusable as a template across clients.
**Cons:** the photographic richness depends on the source photos, and organic motion (cloth, liquids,
hands articulating) is hard. Get those from route A or B.

### Route D: AI video only, with no approved still

This is the "just prompt Kling/Seedance for a collage" shortcut. It's not recommended: it skips Gate 2,
so the look, text-leaks and composition are all luck.

**Default choice:**

- **Route B** for hero client reels.
- **Route C** for templated or high-volume series, or any brand that bans AI imagery.
- **Route A** when the beat needs organic paper physics or hands.
- Keep gbro's gates in every route: words first, still second, motion last.

---

## 5. How collage B-roll inserts work inside a client reel

**Where it goes:**

- **The abstract claim.** Our reels have concrete beats (product, UI, stats, logo) and abstract beats
  ("we turn chaos into a system", "your ads are invisible"). Collage is for the abstract beat, cut in
  for 3 to 5 s under the VO line it illustrates.
- **Problem -> solution pairs.** Two inserts in different fields from the colour-semantics table, e.g.
  burnt orange "time wasted" then teal "automated", told as a mini-narrative (gbro's batch-ordering
  rule).
- **Chapter openers** in explainers: one metaphor per section, the same design language, a different
  field colour.
- **Ad hook (first 2 s):** start mid-assembly (the first piece already sliding in) rather than on an
  empty field. An empty first frame is a dead hook.

**Craft rules for using it in a reel:**

- **Brand-fit the palette:**
  - The colour field is a brand colour, or a brand-harmonious version of the semantic colour.
  - Use the brand accent for the one cardstock piece that carries the meaning.
  - Halftone stays neutral grey/cream, so it works with any brand.
- **One collage language per reel:** the same dot size, keyline width, shadow and grain on every
  insert. Mixing collage with the reel's other look (kinetic type, UI) works if the paper grain is
  shared across the whole film.
- **Seams:**
  - Cut **on the snap**: the last piece lands on a beat, then cut.
  - Or **match the colour field** to the next scene's background so the cut feels continuous.
  - Or disassemble: the pieces slide out, which reverses the build, as the transition out.
  - A brush or paper wipe made of a giant cardstock sheet sliding over also works.
- **Text:** gbro forbids text inside the art. That's right: our captions and kinetic type sit on top in
  the negative space the still prompt reserves.
- **Safe zones:** keep the subject in the middle 70% (gbro's rule), clear of IG/FB reel UI at the top
  (~220 px of 1920) and bottom (~420 px).
- **Sound:**
  - A soft paper slide on each entry, a crisp "tick" or cardboard tap on each snap, and a gentle rustle
    under the build. Synthesise them in `score.py` and place them on the snap times.
  - Duck the music under the VO.
  - Generated clips arrive with audio (Omni) or silent (gbro forces silent): always strip and use our
    own.
- **Specs:**
  - gbro's 720x1280 at 24 fps must be conformed to our 1080x1920 at 60 fps.
  - Upscale with lanczos or a video upscaler.
  - Raise to 60 fps by **duplicating frames, not interpolating**, which would smear the stop-motion.
  - In route C, render natively at 1080x1920.
- **QA in our loop:**
  - Add the gbro checks to `review.sh`: is the first frame of each insert empty (or deliberately mid-build
    for a hook)? Does the last frame match the approved still? Is there fake text anywhere (zoomed
    crops)?
  - Score readability at phone size: a halftone subject must still read at 360 px wide.

### Worked example (for a client line, Gate 1 format)

> VO: "You're posting every day, but nobody remembers your brand."

```text
Core meaning: volume without identity is forgettable
Emotion: dry irony
Visual proposition: a conveyor belt of identical grey halftone ad cards drops one after another into a
                    paper shredder, until one card in the brand's accent colour lands, stops the belt,
                    and a hand lifts it out
Key objects: conveyor belt, grey ad cards, shredder, brand-colour card, hand
Colour: mustard-yellow field (warning, things leaking away); the one accent card in the brand colour
Assembly order: belt -> shredder -> grey cards ride in and fall (on the beat) -> the accent card lands,
                the belt halts -> the hand enters from the top and lifts it (on the VO's last word)
```

Then: route B (generate the belt, shredder, cards and hand as transparent halftone cut-outs; animate
in code so each card drops on a beat), or route A (one still, then `kling3_0` or
`gemini-omni-1.1-flash` from the empty field to that still).
