#!/usr/bin/env python3
"""In-house edit engine: the editing half of a reel, nothing upstream of it.

Two inputs, one finish:

  footage  talking-head / to-camera clip  -> cut pauses, fillers and retakes, jump-cut punch-ins,
                                             reframe (9:16, 4:5, 1:1, 16:9), word-timed captions,
                                             voice polish, music bed ducked under the voice, master.
  voice    a voiceover with no footage    -> tightened VO + words.json/words.js master clock for a
                                             motion-graphics build (HyperFrames or the canvas engine),
           then `finish` on the silent render -> captions, mix, master, delivery.

Subcommands
  edit.py styles                                   list style presets
  edit.py transcribe <media> --out words.json      local Whisper via HyperFrames (needs model download)
  edit.py plan  <clip> --words w.json [--style s]  print the cut plan, render nothing
  edit.py run   <clip> --words w.json --out DIR [--style punchy] [--aspect 9x16] [--music bed.mp3]
  edit.py voice <vo.mp3> --words w.json --out PROJECT_DIR [--tighten]
  edit.py finish <silent.mp4> --voice vo.wav --words w.json --out DIR [--captions style] [--music bed]

Words files: HyperFrames/Whisper `[{text,start,end}]`, ElevenLabs Scribe `{words:[{text,start,end,type}]}`
and the studio's `{words:[{w,s,e}]}` are all accepted.

Only ffmpeg/ffprobe and the Python standard library are required.
"""
import argparse, json, math, os, re, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
PRESETS = os.path.join(HERE, "presets")
HF_VERSION = "0.8.150"

ASPECTS = {"9x16": (1080, 1920), "4x5": (1080, 1350), "1x1": (1080, 1080), "16x9": (1920, 1080)}
# Platform UI safe zones (px at the canvas size). 9:16 numbers are the studio's house rules.
SAFE = {"9x16": dict(top=250, bottom=400, left=96, right=140),
        "4x5": dict(top=120, bottom=200, left=80, right=80),
        "1x1": dict(top=80, bottom=120, left=80, right=80),
        "16x9": dict(top=60, bottom=90, left=120, right=120)}
FILLERS = {"um", "umm", "uh", "uhh", "uhm", "erm", "er", "ah", "ahh", "hmm", "hm", "mm", "mmm", "eh"}


# ---------------------------------------------------------------- helpers
def log(*a):
    print(*a, file=sys.stderr, flush=True)


def run(cmd, quiet=True):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        log("FAILED:", " ".join(cmd))
        log(r.stderr[-3000:])
        sys.exit(1)
    return r


def probe(path):
    r = run(["ffprobe", "-v", "error", "-show_entries",
             "stream=codec_type,width,height,r_frame_rate:format=duration", "-of", "json", path])
    j = json.loads(r.stdout)
    info = {"duration": float(j["format"]["duration"]), "has_audio": False, "has_video": False}
    for s in j["streams"]:
        if s["codec_type"] == "video" and not info["has_video"]:
            n, d = s["r_frame_rate"].split("/")
            info.update(has_video=True, width=s["width"], height=s["height"],
                        fps=float(n) / float(d) if float(d) else 30.0)
        if s["codec_type"] == "audio":
            info["has_audio"] = True
    return info


def load_style(name):
    if os.path.isfile(name):
        p = name
    else:
        p = os.path.join(PRESETS, name + ".json")
    if not os.path.isfile(p):
        sys.exit(f"unknown style '{name}'. Run: edit.py styles")
    with open(p) as f:
        st = json.load(f)
    st["_name"] = os.path.splitext(os.path.basename(p))[0]
    return st


def apply_overrides(st, a):
    cap = st.setdefault("captions", {})
    for k in ("font", "size", "color", "highlight"):
        v = getattr(a, k, None)
        if v is not None:
            cap[k] = v
    if getattr(a, "no_captions", False):
        st["captions"] = None
    if getattr(a, "no_punch", False):
        st["cut"]["punch"] = [1.0]
    return st


def norm_word(w):
    return re.sub(r"[^\w'%$€£]+", "", w.lower())


def load_words(path):
    """Return [{w,s,e}] sorted, from any of the accepted shapes."""
    with open(path) as f:
        j = json.load(f)
    arr = j.get("words", j) if isinstance(j, dict) else j
    out = []
    for x in arr:
        if x.get("type") not in (None, "word"):
            continue                       # Scribe spacing / audio events
        t = x.get("w", x.get("text", x.get("word", "")))
        s = x.get("s", x.get("start"))
        e = x.get("e", x.get("end"))
        if t is None or s is None or e is None or not str(t).strip():
            continue
        out.append({"w": str(t).strip(), "s": float(s), "e": float(max(e, s + 0.02))})
    out.sort(key=lambda x: x["s"])
    return out


def write_words(words, duration, source, dest_json):
    os.makedirs(os.path.dirname(os.path.abspath(dest_json)), exist_ok=True)
    doc = {"source": source, "duration": round(duration, 3),
           "words": [{"w": w["w"], "s": round(w["s"], 3), "e": round(w["e"], 3)} for w in words]}
    with open(dest_json, "w") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    with open(os.path.splitext(dest_json)[0] + ".js", "w") as f:
        f.write("export default " + json.dumps(doc, ensure_ascii=False) + ";\n")


# ---------------------------------------------------------------- cut planning
def sentences(words, gap=0.7):
    out, cur = [], []
    for i, w in enumerate(words):
        if cur and w["s"] - words[i - 1]["e"] > gap:
            out.append(cur); cur = []
        cur.append(i)
        if re.search(r"[.!?]$", w["w"]):
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out


def find_retakes(words):
    """A sentence immediately restarted (same opening words) is a retake: keep the later take."""
    drop, notes = set(), []
    sents = sentences(words)
    for a, b in zip(sents, sents[1:]):
        ka = [norm_word(words[i]["w"]) for i in a]
        kb = [norm_word(words[i]["w"]) for i in b]
        k = min(3, len(ka), len(kb))
        short_false_start = len(ka) <= 3 and ka and kb and ka[0] == kb[0]
        if (k >= 2 and ka[:k] == kb[:k]) or short_false_start:
            drop.update(a)
            notes.append({"dropped": " ".join(words[i]["w"] for i in a),
                          "kept": " ".join(words[i]["w"] for i in b),
                          "at": round(words[a[0]]["s"], 2)})
    return drop, notes


def silence_spans(path, noise_db, min_d):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af",
                        f"silencedetect=noise={noise_db}dB:d={min_d}", "-f", "null", "-"],
                       stderr=subprocess.PIPE, text=True)
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    return list(zip(starts, ends + [None] * (len(starts) - len(ends))))


def plan_cut(src, info, words, cut, keep_retakes=False):
    """Return (segments [(s,e,zoom)], report dict). Times snapped to the source frame grid."""
    fps = info["fps"]
    dur = info["duration"]
    pre, post, gap = cut["pad_in"], cut["pad_out"], cut["max_pause"]
    rep = {"fillers": [], "retakes": [], "pauses_removed": 0, "mode": "words" if words else "silence"}
    spans = []
    if words:
        drop = set()
        if cut.get("drop_fillers", True):
            for i, w in enumerate(words):
                if norm_word(w["w"]) in FILLERS:
                    drop.add(i); rep["fillers"].append(round(w["s"], 2))
        if cut.get("drop_retakes", True) and not keep_retakes:
            d2, notes = find_retakes(words)
            drop |= d2; rep["retakes"] = notes
        kept = [w for i, w in enumerate(words) if i not in drop]
        for w in kept:
            s, e = max(0.0, w["s"] - pre), min(dur, w["e"] + post)
            if spans and s - spans[-1][1] <= gap - pre - post:
                spans[-1][1] = max(spans[-1][1], e)
            else:
                if spans:
                    rep["pauses_removed"] += 1
                spans.append([s, e])
    else:
        sil = silence_spans(src, cut.get("noise_db", -35), max(0.15, gap))
        t = 0.0
        for s, e in sil:
            s2 = min(dur, s + post)
            if s2 - t > 0.12:
                spans.append([max(0.0, t), s2])
            t = (e if e is not None else dur) - pre
            rep["pauses_removed"] += 1
        if dur - t > 0.12:
            spans.append([max(0.0, t), dur])
    # snap to frames, drop slivers
    segs = []
    for s, e in spans:
        fs, fe = math.floor(s * fps), math.ceil(e * fps)
        if fe - fs >= max(2, round(cut.get("min_seg", 0.25) * fps)):
            segs.append([fs, fe])
    merged = []
    for fs, fe in segs:
        if merged and fs <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], fe)
        else:
            merged.append([fs, fe])
    # punch-ins: change zoom only at a real jump (a cut that removed time)
    punch = cut.get("punch", [1.0]) or [1.0]
    out, zi = [], 0
    for k, (fs, fe) in enumerate(merged):
        if k and fs - merged[k - 1][1] > round(0.12 * fps):
            zi = (zi + 1) % len(punch)
        out.append((fs / fps, fe / fps, punch[zi], fs, fe))
    new_len = sum((fe - fs) for *_, fs, fe in out) / fps
    rep.update(source_s=round(dur, 2), cut_s=round(new_len, 2), segments=len(out),
               removed_s=round(dur - new_len, 2))
    return out, rep


def remap_words(words, segs, fps):
    """Move word times from source time to the cut timeline."""
    res, t0 = [], 0.0
    for s, e, z, fs, fe in segs:
        for w in words:
            mid = (w["s"] + w["e"]) / 2
            if s <= mid < e:
                res.append({"w": w["w"], "s": t0 + max(0.0, w["s"] - s), "e": t0 + min(e, w["e"]) - s})
        t0 += (fe - fs) / fps
    return res


# ---------------------------------------------------------------- video
def vf_frame(info, W, H, zoom, push, frame_mode, focus_y, seg_dur):
    w, h = info["width"], info["height"]
    if frame_mode == "blur" and abs(w / h - W / H) > 0.05:
        fit = min(W / w, H / h) * zoom
        fw, fh = int(w * fit) // 2 * 2, int(h * fit) // 2 * 2
        return (f"split[bg][fg];[bg]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                f"boxblur=40:2,eq=brightness=-0.12[bgb];[fg]scale={fw}:{fh}[fgs];"
                f"[bgb][fgs]overlay=(W-w)/2:(H-h)/2,crop={W}:{H}")
    cover = max(W / w, H / h) * zoom
    if push:
        expr = f"(1+{push}*t/{max(seg_dur, 0.1):.3f})"
        sw, sh = f"trunc({w}*{cover:.5f}*{expr}/2)*2", f"trunc({h}*{cover:.5f}*{expr}/2)*2"
        return f"scale=w='{sw}':h='{sh}':eval=frame,crop={W}:{H}:(iw-{W})/2:(ih-{H})*{focus_y}"
    sw, sh = math.ceil(w * cover / 2) * 2, math.ceil(h * cover / 2) * 2
    return f"scale={sw}:{sh},crop={W}:{H}:(iw-{W})/2:(ih-{H})*{focus_y}"


def render_segments(src, info, segs, W, H, style, fps_out, tmp, jobs=4):
    cut = style["cut"]
    files = []

    def one(k):
        s, e, z, fs, fe = segs[k]
        n = fe - fs
        d = n / info["fps"]
        out = os.path.join(tmp, f"seg{k:04d}.mkv")
        vf = vf_frame(info, W, H, z, cut.get("push", 0), cut.get("frame", "crop"), cut.get("focus_y", 0.4), d)
        vf += f",fps={fps_out},setsar=1"
        af = (f"aresample=48000,atrim=0:{d:.6f},apad=whole_dur={d:.6f},"
              f"afade=t=in:d=0.012,afade=t=out:st={max(0, d - 0.012):.6f}:d=0.012")
        cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{s:.6f}", "-i", src, "-t", f"{d:.6f}",
               "-filter_complex", f"[0:v]{vf}[v];[0:a]{af}[a]", "-map", "[v]", "-map", "[a]",
               "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-pix_fmt", "yuv420p",
               "-c:a", "pcm_s16le", "-frames:v", str(max(1, round(d * fps_out))), out]
        run(cmd)
        return out

    with ThreadPoolExecutor(jobs) as ex:
        files = list(ex.map(one, range(len(segs))))
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{p}'\n" for p in files)
    joined = os.path.join(tmp, "cut.mkv")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined])
    return joined


# ---------------------------------------------------------------- captions
def ass_color(hexstr, alpha=0):
    h = hexstr.lstrip("#")
    r, g, b = h[0:2], h[2:4], h[4:6]
    return f"&H{alpha:02X}{b}{g}{r}".upper()


def chunk_words(words, cap):
    maxw, maxc = cap.get("words", 3), cap.get("max_chars", 22)
    chunks, cur = [], []
    for i, w in enumerate(words):
        txt = " ".join(x["w"] for x in cur + [w])
        brk = cur and (len(cur) >= maxw or len(txt) > maxc or w["s"] - cur[-1]["e"] > 0.35)
        if brk:
            chunks.append(cur); cur = []
        cur.append(w)
        if re.search(r"[.!?,;:]$", w["w"]) and len(cur) >= 1 and cap.get("break_on_punct", True):
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    return chunks


def clean_caption(t, cap):
    if cap.get("strip_punct", True):
        t = re.sub(r"[.,;:!?]+$", "", t) if not t.endswith("?") or cap.get("strip_q", True) else t
    if cap.get("case") == "upper":
        t = t.upper()
    elif cap.get("case") == "lower":
        t = t.lower()
    return t.replace("{", "(").replace("}", ")")


def ts_ass(t):
    t = max(0.0, t)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def ts_srt(t):
    ms = int(round(max(0.0, t) * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def build_captions(words, cap, aspect, W, H, total, ass_path, srt_path):
    safe = SAFE[aspect]
    words = [w for w in words if norm_word(w["w"]) not in FILLERS]
    chunks = chunk_words(words, cap)
    size = cap.get("size", 80)
    # caption block centre sits at `y` (fraction of height), clamped inside the safe zone
    y = cap.get("y", 0.68) * H
    y = min(max(y, safe["top"] + size), H - safe["bottom"] - size * 0.6)
    marg_v = int(H - y)
    outline, shadow = cap.get("outline", 0), cap.get("shadow", 0)
    box = cap.get("box")
    border_style = 3 if box else 1
    if box:
        outline = cap.get("box_pad", 18)       # BorderStyle 3: the outline width is the box padding
    back = ass_color(box, 0x40) if box else ass_color("#000000", 0x80)
    out_col = ass_color(box, 0x30) if box else ass_color(cap.get("outline_color", "#000000"))
    hdr = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{cap.get('font', 'Montserrat Black')},{size},{ass_color(cap.get('color', '#FFFFFF'))},&H000000FF,{out_col},{back},0,0,0,0,100,100,{cap.get('spacing', 0)},0,{border_style},{outline},{shadow},2,{safe['left']},{safe['right']},{marg_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    hi = cap.get("highlight")
    hi_tag = ("{\\c" + ass_color(hi) + "}") if hi else ""
    base_tag = "{\\c" + ass_color(cap.get("color", "#FFFFFF")) + "}"
    anim = cap.get("anim", "pop")
    lines, srt = [], []
    for ci, ch in enumerate(chunks):
        start = ch[0]["s"]
        nxt = chunks[ci + 1][0]["s"] if ci + 1 < len(chunks) else total
        end = min(total, nxt if nxt - ch[-1]["e"] < cap.get("hold", 0.3) else ch[-1]["e"] + 0.12)
        toks = [clean_caption(w["w"], cap) for w in ch]
        srt.append((start, end, " ".join(toks)))
        if anim == "pop":
            intro = "{\\fscx86\\fscy86\\t(0,110,\\fscx104\\fscy104)\\t(110,190,\\fscx100\\fscy100)}"
        elif anim == "rise":
            intro = "{\\an5\\fad(80,0)\\move(%d,%d,%d,%d,0,180)}" % (W // 2, int(y + 30), W // 2, int(y))
        else:
            intro = ""
        if not hi:
            lines.append(f"Dialogue: 0,{ts_ass(start)},{ts_ass(end)},Cap,,0,0,0,,{intro}{' '.join(toks)}")
            continue
        # one event per active word: the spoken word takes the highlight colour
        for k, w in enumerate(ch):
            ws = start if k == 0 else w["s"]
            we = end if k == len(ch) - 1 else ch[k + 1]["s"]
            if we <= ws:
                continue
            parts = [(hi_tag + t + base_tag) if j == k else t for j, t in enumerate(toks)]
            lead = intro if k == 0 else ("{\\an5\\pos(%d,%d)}" % (W // 2, int(y)) if anim == "rise" else "")
            lines.append(f"Dialogue: 0,{ts_ass(ws)},{ts_ass(we)},Cap,,0,0,0,,{lead}{' '.join(parts)}")
    with open(ass_path, "w") as f:
        f.write(hdr + "\n".join(lines) + "\n")
    with open(srt_path, "w") as f:
        for i, (s, e, t) in enumerate(srt, 1):
            f.write(f"{i}\n{ts_srt(s)} --> {ts_srt(e)}\n{t}\n\n")
    return len(chunks)


# ---------------------------------------------------------------- audio
VOICE_CHAIN = ("highpass=f=75,equalizer=f=230:t=q:w=1:g=-3,equalizer=f=3500:t=q:w=1:g=1.5,"
               "acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2")


def mix_audio(voice_src, music, total, tmp, music_db=-6.0, polish=True):
    """voice (+ optional music bed ducked under it) -> mix.wav, then two-pass loudnorm -> master.wav."""
    mix = os.path.join(tmp, "mix.wav")
    vchain = VOICE_CHAIN if polish else "anull"
    if music:
        fc = (f"[0:a]aresample=48000,{vchain},asplit[v1][v2];"
              f"[1:a]aresample=48000,atrim=0:{total:.3f},highpass=f=45,equalizer=f=220:t=q:w=1:g=-6,"
              f"equalizer=f=3200:t=q:w=1:g=-2,loudnorm=I=-28:TP=-4,volume={music_db}dB,"
              f"afade=t=in:d=0.3,afade=t=out:st={max(0, total - 1.2):.3f}:d=1.2[m];"
              f"[m][v2]sidechaincompress=threshold=0.015:ratio=9:attack=20:release=380:makeup=1[md];"
              f"[v1][md]amix=inputs=2:normalize=0:duration=first[out]")
        cmd = ["ffmpeg", "-y", "-v", "error", "-i", voice_src, "-stream_loop", "-1", "-i", music,
               "-filter_complex", fc, "-map", "[out]", "-t", f"{total:.3f}", "-c:a", "pcm_s24le", mix]
    else:
        cmd = ["ffmpeg", "-y", "-v", "error", "-i", voice_src, "-vn", "-af", f"aresample=48000,{vchain}",
               "-t", f"{total:.3f}", "-c:a", "pcm_s24le", mix]
    run(cmd)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mix, "-af",
                        "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                       stderr=subprocess.PIPE, text=True)
    m = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    master = os.path.join(tmp, "master.wav")
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    run(["ffmpeg", "-y", "-v", "error", "-i", mix, "-af", ln + ",aresample=48000", "-c:a", "pcm_s24le", master])
    return master


def measure(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true",
                        "-f", "null", "-"], stderr=subprocess.PIPE, text=True)
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
    p = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r.stderr)
    return {"lufs": float(i[-1]) if i else None, "true_peak_db": float(p[-1]) if p else None}


# ---------------------------------------------------------------- final encode + delivery
def encode_master(video_src, audio_wav, ass, total, out_mp4, draft=False):
    vf = "null"
    if ass:
        vf = f"ass='{ass}':fontsdir='{FONTS}'"
    q = ["-preset", "veryfast", "-crf", "26"] if draft else ["-preset", "medium", "-crf", "21"]
    run(["ffmpeg", "-y", "-v", "error", "-i", video_src, "-i", audio_wav, "-map", "0:v:0", "-map", "1:a:0",
         "-vf", vf + ",format=yuv420p", "-c:v", "libx264", *q, "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-t", f"{total:.3f}", "-movflags", "+faststart", out_mp4])


def deliver(master_mp4, out_dir, base):
    size_mb = os.path.getsize(master_mp4) / 1e6
    view = os.path.join(out_dir, base + "_view.mp4")
    if size_mb > 30:
        run(["ffmpeg", "-y", "-v", "error", "-i", master_mp4, "-c:v", "libx264", "-preset", "medium",
             "-crf", "25", "-maxrate", "6M", "-bufsize", "12M", "-c:a", "aac", "-b:a", "160k",
             "-movflags", "+faststart", view])
    else:
        shutil.copy(master_mp4, view)
    run(["ffmpeg", "-y", "-v", "error", "-ss", "0.6", "-i", master_mp4, "-frames:v", "1",
         os.path.join(out_dir, "poster.png")])
    return view


def write_report(out_dir, d):
    with open(os.path.join(out_dir, "report.json"), "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    L = [f"# Edit report: {d.get('base')}", "",
         f"- Style: `{d.get('style')}`, aspect {d.get('aspect')}",
         f"- Length: {d.get('source_s')} s in, **{d.get('cut_s')} s out** ({d.get('removed_s', 0)} s removed)" if 'cut_s' in d else f"- Length: {d.get('duration_s')} s",
         ]
    if "segments" in d:
        L.append(f"- Cuts: {d['segments']} kept pieces, {d['pauses_removed']} pauses tightened, "
                 f"{len(d['fillers'])} filler words removed, {len(d['retakes'])} retakes dropped")
    for r in d.get("retakes", []):
        L.append(f"  - retake at {r['at']} s: dropped \"{r['dropped']}\", kept \"{r['kept']}\"")
    if d.get("captions"):
        L.append(f"- Captions: {d['captions']} on-screen chunks; `captions.srt` included")
    a = d.get("loudness", {})
    L.append(f"- Loudness after AAC: {a.get('lufs')} LUFS, true peak {a.get('true_peak_db')} dBFS (target -14 / -1.5)")
    L.append(f"- Music: {d.get('music') or 'none'}")
    L += ["", "**Check by a person before posting:** listen with sound on, read every caption "
          "(transcription can mishear names and numbers), and confirm any retake the engine dropped."]
    with open(os.path.join(out_dir, "REPORT.md"), "w") as f:
        f.write("\n".join(L) + "\n")


# ---------------------------------------------------------------- commands
def cmd_styles(a):
    for fn in sorted(os.listdir(PRESETS)):
        if fn.endswith(".json"):
            with open(os.path.join(PRESETS, fn)) as f:
                st = json.load(f)
            print(f"{fn[:-5]:12s} {st.get('about', '')}")


def cmd_transcribe(a):
    tmp = tempfile.mkdtemp(prefix="edtr")
    wav = os.path.join(tmp, "audio.wav")
    run(["ffmpeg", "-y", "-v", "error", "-i", a.media, "-vn", "-ac", "1", "-ar", "16000", wav])
    model = a.model or ("small.en" if a.lang in (None, "en") else "small")
    env = dict(os.environ, HYPERFRAMES_NO_TELEMETRY="1", DO_NOT_TRACK="1", HYPERFRAMES_SKIP_SKILLS="1")
    cmd = ["npx", "-y", f"hyperframes@{HF_VERSION}", "transcribe", wav, "-d", tmp, "--json", "--model", model]
    if a.lang and a.lang != "en":
        cmd += ["--language", a.lang]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
    src = os.path.join(tmp, "transcript.json")
    if r.returncode != 0 or not os.path.isfile(src):
        log(r.stderr[-1500:])
        sys.exit("Local transcription failed (the Whisper model download is blocked in cloud sessions).\n"
                 "Use ElevenLabs Scribe instead: creative_transcribe_audio on the clip's audio, save the JSON "
                 "and pass it with --words. Scribe output is accepted as-is.")
    words = load_words(src)
    write_words(words, probe(a.media)["duration"], os.path.basename(a.media), a.out)
    log(f"{len(words)} words -> {a.out}")


def prep_footage(a):
    info = probe(a.clip)
    if not (info["has_video"] and info["has_audio"]):
        sys.exit("footage mode needs a clip with both picture and sound")
    st = apply_overrides(load_style(a.style), a)
    words = load_words(a.words) if a.words else []
    if not words:
        log("no words file: cutting on silence only, and no captions (run `transcribe` or pass --words)")
        st["captions"] = None
    segs, rep = plan_cut(a.clip, info, words, st["cut"], a.keep_retakes)
    return info, st, words, segs, rep


def cmd_plan(a):
    info, st, words, segs, rep = prep_footage(a)
    print(json.dumps({k: v for k, v in rep.items()}, indent=1))
    for s, e, z, *_ in segs:
        txt = " ".join(w["w"] for w in words if s <= (w["s"] + w["e"]) / 2 < e)
        print(f"{s:7.2f} -> {e:7.2f}  zoom {z:.2f}  {txt[:70]}")


def cmd_run(a):
    info, st, words, segs, rep = prep_footage(a)
    if not segs:
        sys.exit("nothing left after cutting; check the words file and the style's max_pause")
    W, H = ASPECTS[a.aspect]
    fps = a.fps or (60 if info["fps"] > 45 else 30)
    os.makedirs(a.out, exist_ok=True)
    base = a.name or os.path.splitext(os.path.basename(a.clip))[0]
    tmp = tempfile.mkdtemp(prefix="edit_", dir=a.work or None)
    log(f"cut plan: {rep['source_s']} s -> {rep['cut_s']} s in {rep['segments']} pieces ({rep['mode']} mode)")
    log("rendering pieces ...")
    cut_mkv = render_segments(a.clip, info, segs, W, H, st, fps, tmp, a.jobs)
    total = sum(fe - fs for *_, fs, fe in segs) / info["fps"]
    new_words = remap_words(words, segs, info["fps"]) if words else []
    ass = None
    rep["captions"] = 0
    if st.get("captions") and new_words:
        ass = os.path.join(tmp, "captions.ass")
        rep["captions"] = build_captions(new_words, st["captions"], a.aspect, W, H, total, ass,
                                         os.path.join(a.out, "captions.srt"))
    log("mixing and mastering audio ...")
    master_wav = mix_audio(cut_mkv, a.music, total, tmp, st.get("music_db", -6.0) if a.music_db is None else a.music_db)
    out_mp4 = os.path.join(a.out, f"{base}_{a.aspect}.mp4")
    log("encoding master ...")
    encode_master(cut_mkv, master_wav, ass, total, out_mp4, a.draft)
    deliver(out_mp4, a.out, f"{base}_{a.aspect}")
    if new_words:
        write_words(new_words, total, os.path.basename(out_mp4), os.path.join(a.out, "words_cut.json"))
    with open(os.path.join(a.out, "cutlist.json"), "w") as f:
        json.dump([{"src_in": round(s, 3), "src_out": round(e, 3), "zoom": z} for s, e, z, *_ in segs], f, indent=1)
    rep.update(base=base, style=st["_name"], aspect=a.aspect, music=os.path.basename(a.music) if a.music else None,
               loudness=measure(out_mp4), output=os.path.basename(out_mp4))
    write_report(a.out, rep)
    if a.keep_work:
        log("work files kept in", tmp)
    else:
        shutil.rmtree(tmp, ignore_errors=True)
    log(f"done -> {out_mp4}")


def cmd_voice(a):
    info = probe(a.vo)
    words = load_words(a.words)
    adir = os.path.join(a.out, "audio")
    os.makedirs(adir, exist_ok=True)
    if a.tighten:
        st = load_style(a.style)
        info["fps"] = 1000.0                                      # audio only: millisecond grid
        segs, rep = plan_cut(a.vo, info, words, st["cut"], a.keep_retakes)
        parts, t = [], 0
        for k, (s, e, *_r) in enumerate(segs):
            parts.append(f"[0:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,"
                         f"afade=t=out:st={max(0, e - s - 0.01):.3f}:d=0.01[a{k}]")
        fc = ";".join(parts) + ";" + "".join(f"[a{k}]" for k in range(len(segs))) + f"concat=n={len(segs)}:v=0:a=1[o]"
        out = os.path.join(adir, "vo.wav")
        run(["ffmpeg", "-y", "-v", "error", "-i", a.vo, "-filter_complex", fc, "-map", "[o]", "-ar", "48000", out])
        words = remap_words(words, segs, 1000.0)
        dur = probe(out)["duration"]
        log(f"tightened VO: {rep['source_s']} s -> {round(dur, 2)} s, {len(rep['fillers'])} fillers, "
            f"{len(rep['retakes'])} retakes, {rep['pauses_removed']} pauses")
    else:
        out = os.path.join(adir, "vo.wav")
        run(["ffmpeg", "-y", "-v", "error", "-i", a.vo, "-ar", "48000", out])
        dur = info["duration"]
    write_words(words, dur, "vo.wav", os.path.join(adir, "words.json"))
    log(f"master clock ready: {adir}/words.json (+ words.js), {len(words)} words, {dur:.2f} s.\n"
        f"Build the picture against it (HyperFrames or motion-studio canvas engine), render silent, then:\n"
        f"  edit.py finish <silent.mp4> --voice {out} --words {adir}/words.json --out <deliver dir>")


def cmd_finish(a):
    info = probe(a.video)
    total = info["duration"]
    W, H = info["width"], info["height"]
    aspect = min(ASPECTS, key=lambda k: abs(ASPECTS[k][0] / ASPECTS[k][1] - W / H))
    os.makedirs(a.out, exist_ok=True)
    base = a.name or os.path.splitext(os.path.basename(a.video))[0]
    tmp = tempfile.mkdtemp(prefix="finish_")
    ass, n = None, 0
    if a.captions:
        st = apply_overrides(load_style(a.captions), a)
        if not a.words:
            sys.exit("--captions needs --words")
        ass = os.path.join(tmp, "captions.ass")
        n = build_captions(load_words(a.words), st["captions"], aspect, W, H, total, ass,
                           os.path.join(a.out, "captions.srt"))
    master_wav = mix_audio(a.voice, a.music, total, tmp, a.music_db if a.music_db is not None else -6.0,
                           polish=not a.no_polish)
    out_mp4 = os.path.join(a.out, f"{base}_{aspect}.mp4")
    encode_master(a.video, master_wav, ass, total, out_mp4, a.draft)
    deliver(out_mp4, a.out, f"{base}_{aspect}")
    write_report(a.out, dict(base=base, style=a.captions or "no captions", aspect=aspect, duration_s=round(total, 2),
                             captions=n, music=os.path.basename(a.music) if a.music else None,
                             loudness=measure(out_mp4), output=os.path.basename(out_mp4)))
    shutil.rmtree(tmp, ignore_errors=True)
    log(f"done -> {out_mp4}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    def look(q):
        q.add_argument("--font"); q.add_argument("--size", type=int)
        q.add_argument("--color"); q.add_argument("--highlight")

    sp.add_parser("styles")
    t = sp.add_parser("transcribe"); t.add_argument("media"); t.add_argument("--out", required=True)
    t.add_argument("--lang"); t.add_argument("--model")
    for name in ("plan", "run"):
        q = sp.add_parser(name)
        q.add_argument("clip"); q.add_argument("--words"); q.add_argument("--style", default="punchy")
        q.add_argument("--keep-retakes", action="store_true"); q.add_argument("--no-captions", action="store_true")
        q.add_argument("--no-punch", action="store_true"); look(q)
        if name == "run":
            q.add_argument("--out", required=True); q.add_argument("--aspect", default="9x16", choices=ASPECTS)
            q.add_argument("--music"); q.add_argument("--music-db", type=float)
            q.add_argument("--fps", type=int); q.add_argument("--name"); q.add_argument("--draft", action="store_true")
            q.add_argument("--jobs", type=int, default=4); q.add_argument("--work"); q.add_argument("--keep-work", action="store_true")
    v = sp.add_parser("voice"); v.add_argument("vo"); v.add_argument("--words", required=True)
    v.add_argument("--out", required=True); v.add_argument("--tighten", action="store_true")
    v.add_argument("--style", default="clean"); v.add_argument("--keep-retakes", action="store_true")
    f = sp.add_parser("finish"); f.add_argument("video"); f.add_argument("--voice", required=True)
    f.add_argument("--words"); f.add_argument("--out", required=True); f.add_argument("--captions")
    f.add_argument("--music"); f.add_argument("--music-db", type=float); f.add_argument("--name")
    f.add_argument("--draft", action="store_true"); f.add_argument("--no-polish", action="store_true")
    f.add_argument("--no-captions", action="store_true"); f.add_argument("--no-punch", action="store_true"); look(f)
    a = p.parse_args()
    {"styles": cmd_styles, "transcribe": cmd_transcribe, "plan": cmd_plan, "run": cmd_run,
     "voice": cmd_voice, "finish": cmd_finish}[a.cmd](a)


if __name__ == "__main__":
    main()
