---
name: edit-engine
description: The studio's in-house editing engine for a reel when the job is editing only, not research or script. Footage of someone talking goes in; out comes a cut with pauses, filler words and retakes removed, jump-cut punch-ins, vertical reframing, word-timed captions, music ducked under the voice and a -14 LUFS master. It also tightens a voiceover into the master clock for a motion-graphics build and finishes the silent render. Use for "edit my clip", "cut the pauses", "add captions", "make this a reel", "finish/mix this render". Full concept-to-delivery jobs go through motion-reel, which calls this for the edit.
---

# Edit engine

Engine: `motion-studio/edit-engine/edit.py` (needs only ffmpeg and Python). Read `motion-studio/edit-engine/README.md`
for every flag. Keep the user posted in plain words: they may not be technical.

## 1. Which route
- **Footage of a person talking** (talking head, interview, podcast clip): route A.
- **Voiceover with no footage** (motion graphics, explainer): route B.
- Both in one film: cut the footage with route A, build the graphics against `words_cut.json`, then `finish`.

## 2. Words file (both routes)
1. On the user's own machine: `python3 edit.py transcribe <media> --out words.json`.
2. In a cloud session (Whisper download blocked): extract the audio (`ffmpeg -i clip.mp4 -vn -ac 1 audio.mp3`), run the
   ElevenLabs `creative_transcribe_audio` on it, and save the JSON with its words array. It is accepted as-is.
3. Read the transcript and fix misheard names, brand words and numbers in place, keeping the times. Captions show
   exactly what the file says.

## 3. Route A: footage
1. Pick the style with the user (`edit.py styles`); default `punchy`. Brand colours go in `--color/--highlight`.
2. `edit.py plan <clip> --words words.json --style <s>`. Read the plan. Tell the user what will be cut,
   especially every **retake** dropped. If a drop is wrong, rerun with `--keep-retakes` or edit the words file.
3. `edit.py run ... --draft --out <dir>/draft`, then make a contact sheet (one frame per caption chunk) and look at it
   at phone size: captions readable, inside the safe zones, face not cropped, zooms not too tight.
4. The final run without `--draft`, into `deliver/vN/`. Never overwrite a previous version.
5. Report the numbers from `REPORT.md` in plain words (length before and after, what was cut, loudness), and send
   the `_view.mp4`.

## 4. Route B: voiceover
1. `edit.py voice vo.mp3 --words words.json --out <project> --tighten` gives `audio/vo.wav` and `audio/words.js`
   (the master clock).
2. Build the picture against `words.js` with the motion-reel engines (HyperFrames or the canvas engine), and render it
   silent.
3. `edit.py finish silent.mp4 --voice <project>/audio/vo.wav --words <project>/audio/words.json --captions <style>
   --music bed.mp3 --out <project>/deliver/vN`.

## Rules
- Music must be licensed, supplied, generated or sampled; never a ripped commercial track.
- Never post. A person listens with sound and reads every caption before anything goes live.
- Heavier looks on the same cut: `embedded-captions` (captions behind the subject; run `run` with `--no-captions`
  first) and `talking-head-recut` (graphic cards).
- After changing `edit.py` or a preset, run `motion-studio/edit-engine/selftest.sh` (needs `apt-get install flite`).
