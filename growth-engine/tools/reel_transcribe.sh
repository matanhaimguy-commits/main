#!/usr/bin/env bash
# What was actually said in public reels or shorts, for free. Runs in the Higgsfield sandbox (mcp__Higgs__sandbox_exec),
# which has internet; this container does not. Paste the script there, then: bash reel_transcribe.sh URL [URL ...]
# Prints one JSON line per URL: {"url", "first_sentence", "transcript", "error"}. Tested 28 Oct 2026 on an Instagram
# reel (yt-dlp audio + faster-whisper tiny.en). Instagram profile listings need a login, so URLs come from elsewhere
# (YouTube Shorts listings via TranscriptAPI, or links the owner sends). YouTube blocks this sandbox (bot check, 28 Oct):
# for a Short use TranscriptAPI get_youtube_transcript instead; this script is for Instagram reels.
export HOME=/home/user
python3 -m yt_dlp --version >/dev/null 2>&1 || pip install -q yt-dlp >/dev/null 2>&1
for url in "$@"; do
  rm -f clip.mp3
  python3 -m yt_dlp -q -x --audio-format mp3 -o 'clip.%(ext)s' "$url" >/dev/null 2>err.txt
  URL="$url" python3 - <<'EOF'
import json, os, re
url = os.environ["URL"]
if not os.path.exists("clip.mp3"):
    print(json.dumps({"url": url, "error": open("err.txt").read()[-200:]}))
else:
    from faster_whisper import WhisperModel
    segs, _ = WhisperModel("tiny.en", compute_type="int8").transcribe("clip.mp3")
    text = " ".join(s.text.strip() for s in segs)
    first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    print(json.dumps({"url": url, "first_sentence": first, "transcript": text}))
EOF
done
