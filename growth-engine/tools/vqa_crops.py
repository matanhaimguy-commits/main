#!/usr/bin/env python3
"""Review packets for the fresh-agent reviewers (VISUAL-QA 5.1, 7.1 to 7.3). Pure PIL + numpy + ffmpeg, so it runs
here or in the Higgsfield sandbox (send it with a heredoc).

  vqa_crops.py image <file> (--run <slug>/<post_id> --asset A@vN | --out DIR [--spec S.yaml ...]) [--panels auto|3x1|2x2|2x3] [--ocr LANG]
      full image, 3x3 tiles at 2x, a 2x crop per region in the Shot Spec(s), storyboard panels, a 200 px thumbnail,
      optional tesseract OCR as a second opinion (it never passes text on its own: ë and ç get misread)
  vqa_crops.py frames <video> (--run ... --asset ... | --out DIR) [--fps N]     take frames: 1/s (2/s under 6 s) + first/last 0.1 s
  vqa_crops.py motion <video> (...)                 motion render: every 0.5 s + every cut's start, middle and end
  vqa_crops.py final <video> (...)                  final cut: every 1.5 s + every cut
  vqa_crops.py drift <clip> <slice> [--out report.json]   H3 lip-sync drift (hub G6): lag per 2 s window every 0.25 s
  vqa_crops.py loudness <file>                     integrated LUFS, true peak, loudness range, short-term max, pass vs STANDARDS 4

Every packet writes manifest.json with must_open: the files a reviewer has to open before its report counts
(pipeline.py record checks the report's files_opened against it).
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

try:
    import yaml
except ImportError:  # the sandbox may lack PyYAML: specs can be passed as JSON there
    yaml = None

ROOT = Path(__file__).resolve().parents[2]


def load_spec(p: Path) -> dict:
    txt = p.read_text()
    if p.suffix == ".json" or yaml is None:
        return json.loads(txt)
    return yaml.safe_load(txt)


def resolve_out(args, kind: str) -> tuple[Path, list[dict], bool]:
    """Output folder and the specs that apply, from --run/--asset (repo) or --out/--spec (sandbox)."""
    specs, hero = [], bool(getattr(args, "hero", False))
    if getattr(args, "run", None):
        slug, post = args.run.split("/", 1)
        rd = ROOT / "clients" / slug / "runs" / post
        led = json.loads((rd / "ledger.json").read_text())
        aid, v = args.asset.split("@")
        v = int(v.lstrip("v"))
        a = next(x for x in led["assets"] if x["asset_id"] == aid and x["version"] == v)
        hero = hero or a.get("hero", False)
        for s in a["shots"]:
            sp = rd / "shots" / f"{s}.spec.yaml"
            if sp.exists():
                specs.append(load_spec(sp))
        out = rd / "qa" / ("crops" if kind == "image" else "frames") / f"{aid}.v{v}"
    else:
        if not args.out:
            sys.exit("give --run <slug>/<post_id> --asset A@vN, or --out DIR")
        out = Path(args.out)
        for s in getattr(args, "spec", None) or []:
            specs.append(load_spec(Path(s)))
    hero = hero or any(s.get("hero") for s in specs)
    out.mkdir(parents=True, exist_ok=True)
    return out, specs, hero


def up2(im: Image.Image) -> Image.Image:
    return im.resize((im.width * 2, im.height * 2), Image.LANCZOS)


def find_gutters(im: Image.Image, axis: int, min_run: int = 6) -> list[tuple[int, int]]:
    """Runs of near-uniform rows (axis=1) or columns (axis=0): the gaps between storyboard panels."""
    g = ImageOps.grayscale(im)
    w, h = g.size
    px = g.load()
    n = w if axis == 0 else h
    flat = []
    for i in range(n):
        vals = [px[i, j] for j in range(0, h, max(1, h // 200))] if axis == 0 else [px[j, i] for j in range(0, w, max(1, w // 200))]
        flat.append(max(vals) - min(vals) < 12)
    runs, start = [], None
    for i, f in enumerate(flat + [False]):
        if f and start is None:
            start = i
        elif not f and start is not None:
            if i - start >= min_run and start > 0 and i < n:
                runs.append((start, i))
            start = None
    return runs


def split_panels(im: Image.Image, layout: str) -> list[tuple[int, int, int, int]]:
    w, h = im.size
    if layout and layout != "auto":
        cols, rows = (int(x) for x in layout.lower().split("x"))
        return [(round(c * w / cols), round(r * h / rows), round((c + 1) * w / cols), round((r + 1) * h / rows))
                for r in range(rows) for c in range(cols)]

    def cuts(runs, n):
        edges, prev = [], 0
        for a, b in runs:
            edges.append((prev, a))
            prev = b
        edges.append((prev, n))
        return [e for e in edges if e[1] - e[0] > n * 0.12]
    xs = cuts(find_gutters(im, 0), w)
    ys = cuts(find_gutters(im, 1), h)
    return [(x0, y0, x1, y1) for (y0, y1) in ys for (x0, x1) in xs]


def ocr(path: Path, lang: str) -> str | None:
    if not shutil.which("tesseract"):
        return None
    r = subprocess.run(["tesseract", str(path), "-", "-l", lang], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def cmd_image(args) -> dict:
    out, specs, hero = resolve_out(args, "image")
    src = Image.open(args.file)
    src.load()
    im = src.convert("RGB")
    w, h = im.size
    files, must = [], []

    ext = getattr(args, "ext", "png")

    def save(img, name, required=True):
        if ext != "png":
            name = name.rsplit(".", 1)[0] + "." + ext
        p = out / name
        img.save(p, quality=88) if ext == "jpg" else img.save(p)
        files.append(name)
        if required:
            must.append(name)
        return p

    save(im, "full.png")
    for r in range(3):
        for c in range(3):
            box = (c * w // 3, r * h // 3, (c + 1) * w // 3, (r + 1) * h // 3)
            save(up2(im.crop(box)), f"tile_r{r + 1}c{c + 1}.png")
    panels = []
    is_board = args.panels or any(s.get("format") == "storyboard_panel" for s in specs)
    if is_board:
        panels = split_panels(im, args.panels or "auto")
        for i, b in enumerate(panels, 1):
            save(im.crop(b), f"panel_{i}.png")
    ocr_out = {}
    for s in specs:
        for rg in s.get("regions") or []:
            base = (0, 0, w, h)
            if rg.get("panel") and panels and rg["panel"] <= len(panels):
                base = panels[rg["panel"] - 1]
            bw, bh = base[2] - base[0], base[3] - base[1]
            x0, y0, x1, y1 = rg["box"]
            pad = 0.03
            box = (int(base[0] + max(0, x0 - pad) * bw), int(base[1] + max(0, y0 - pad) * bh),
                   int(base[0] + min(1, x1 + pad) * bw), int(base[1] + min(1, y1 + pad) * bh))
            name = f"region_{s.get('shot_id', 'shot')}_{rg['name']}.png"
            p = save(up2(im.crop(box)), name)
            if args.ocr and rg.get("kind") == "text":
                ocr_out[p.name] = ocr(p, args.ocr)
    thumb = im.copy()
    thumb.thumbnail((200, 200 * h // w))
    save(thumb, "thumb_200.png", required=hero)
    if args.ocr and not ocr_out:
        ocr_out[files[0]] = ocr(out / files[0], args.ocr)
    man = {"kind": "image", "source": str(args.file), "size": [w, h], "hero": hero, "files": files, "must_open": must,
           "panels": len(panels), "ocr": ocr_out or None,
           "ocr_note": "OCR is a second opinion only; read every letter yourself (diacritics)" if args.ocr else None}
    (out / "manifest.json").write_text(json.dumps(man, indent=2, ensure_ascii=False))
    return {"out": str(out), **man}


def probe_duration(video: str) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def grab(video: str, t: float, dest: Path) -> None:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{max(0, t):.3f}", "-i", video, "-frames:v", "1", str(dest)],
                   check=True)


def scene_cuts(video: str, thresh: float = 0.3) -> list[float]:
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", video, "-vf", f"select='gt(scene,{thresh})',showinfo", "-f", "null", "-"],
                       capture_output=True, text=True)
    return [float(m) for m in re.findall(r"pts_time:([0-9.]+)", r.stderr)]


def contact(frames: list[tuple[float, Path]], dest: Path, cols: int = 4, width: int = 270) -> None:
    ims = []
    for t, p in frames:
        im = Image.open(p).convert("RGB")
        im.thumbnail((width, width * 3))
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 70, 18), fill=(0, 0, 0))
        d.text((4, 3), f"{t:6.2f}s", fill=(255, 255, 0))
        ims.append(im)
    if not ims:
        return
    cw, ch = max(i.width for i in ims), max(i.height for i in ims)
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cw, rows * ch), (20, 20, 20))
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * cw, (i // cols) * ch))
    sheet.save(dest)


def frame_packet(args, times: list[float], kind: str) -> dict:
    out, _, _ = resolve_out(args, kind)
    dur = probe_duration(args.video)
    frames = []
    for t in sorted({round(min(max(0.0, x), max(0.0, dur - 0.05)), 2) for x in times}):
        p = out / f"f_{t:07.2f}.png"
        grab(args.video, t, p)
        if p.exists():
            frames.append((t, p))
    sheets = []
    for i in range(0, len(frames), 12):
        s = out / f"contact_{i // 12 + 1}.jpg"
        contact(frames[i:i + 12], s)
        sheets.append(s.name)
    must = sheets + [frames[0][1].name, frames[-1][1].name] if frames else sheets
    man = {"kind": kind, "source": str(args.video), "duration": dur, "frames": [p.name for _, p in frames],
           "contact_sheets": sheets, "must_open": must}
    (out / "manifest.json").write_text(json.dumps(man, indent=2))
    return {"out": str(out), **man}


def cmd_frames(args) -> dict:
    dur = probe_duration(args.video)
    fps = args.fps or (2 if dur < 6 else 1)
    times = [0.0, 0.1] + [i / fps for i in range(int(dur * fps) + 1)] + [dur - 0.1]
    return frame_packet(args, times, "take")


def cmd_motion(args) -> dict:
    dur = probe_duration(args.video)
    times = [i * 0.5 for i in range(int(dur / 0.5) + 1)] + [dur - 0.1]
    cuts = scene_cuts(args.video)
    for c in cuts:
        times += [c - 0.25, c, c + 0.25]
    return frame_packet(args, times, "motion")


def cmd_final(args) -> dict:
    dur = probe_duration(args.video)
    times = [i * 1.5 for i in range(int(dur / 1.5) + 1)] + [0.0, dur - 0.1] + scene_cuts(args.video)
    return frame_packet(args, times, "final")


def pcm(path: str, sr: int = 16000):
    import numpy as np
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32)


def envelope(x, sr=16000, hop=0.01):
    import numpy as np
    n = int(sr * hop)
    m = len(x) // n
    e = np.sqrt((x[: m * n].reshape(m, n) ** 2).mean(axis=1) + 1e-12)
    return np.log(e + 1e-4)


def cmd_drift(args) -> dict:
    """Lag of the clip's audio against its ElevenLabs slice in 2 s windows every 0.25 s (hub G6)."""
    import numpy as np
    hop = 0.01
    a, b = envelope(pcm(args.clip)), envelope(pcm(args.slice))
    win, step, maxlag = int(2 / hop), int(0.25 / hop), int(1.5 / hop)
    rows = []
    for s in range(0, max(1, len(b) - win), step):
        ref = b[s:s + win]
        if ref.std() < 0.05:
            continue
        best, lag = -2.0, 0
        for L in range(-maxlag, maxlag + 1):
            lo = s + L
            if lo < 0 or lo + win > len(a):
                continue
            seg = a[lo:lo + win]
            c = float(np.corrcoef(ref, seg)[0, 1])
            if c > best:
                best, lag = c, L
        rows.append({"t": round(s * hop, 2), "lag_s": round(lag * hop, 2), "corr": round(best, 3)})
    lags = [r["lag_s"] for r in rows]
    steps = [{"at": rows[i]["t"], "from": lags[i - 1], "to": lags[i]} for i in range(1, len(rows))
             if abs(lags[i] - lags[i - 1]) >= 0.1]
    low = [r for r in rows if r["corr"] < 0.5]
    med = float(np.median(lags)) if lags else 0.0
    verdict = ("no usable windows" if not rows else
               "retake: correlation under 0.5 with no clear lag" if len(low) > len(rows) / 2 else
               "one median offset" if not steps or max(abs(x["to"] - x["from"]) for x in steps) < 0.15 else
               "cut at each step inside the nearest pause (retake only if a step sits inside a word)")
    rep = {"clip": args.clip, "slice": args.slice, "median_lag_s": round(med, 2), "windows": rows, "steps": steps,
           "low_corr_windows": len(low), "verdict": verdict}
    if args.out:
        Path(args.out).write_text(json.dumps(rep, indent=2))
    return {k: v for k, v in rep.items() if k != "windows"}


def cmd_loudness(args) -> dict:
    r = subprocess.run(["ffmpeg", "-nostats", "-i", args.file, "-filter_complex", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    tail = r.stderr[r.stderr.rfind("Summary:"):]
    i = re.search(r"I:\s+(-?[0-9.]+) LUFS", tail)
    tp = re.search(r"Peak:\s+(-?[0-9.]+) dBFS", tail)
    lra = re.search(r"LRA:\s+(-?[0-9.]+) LU", tail)
    st = [float(x) for x in re.findall(r"\bS:\s*(-?[0-9.]+)", r.stderr[: r.stderr.rfind("Summary:")])]
    res = {"file": args.file, "integrated_lufs": float(i.group(1)) if i else None,
           "true_peak_dbtp": float(tp.group(1)) if tp else None,
           "loudness_range_lu": float(lra.group(1)) if lra else None,
           "short_term_max_lufs": max(st) if st else None}
    try:  # STANDARDS.md section 4 (standards.json audio)
        std = json.loads((Path(__file__).resolve().parents[1] / "production" / "standards.json").read_text())["audio"]
        checks = {}
        if res["integrated_lufs"] is not None:
            checks["integrated"] = abs(res["integrated_lufs"] - std["loudness_lufs"]) <= std["loudness_tolerance"]
        if res["true_peak_dbtp"] is not None:
            checks["true_peak"] = res["true_peak_dbtp"] <= std["true_peak_dbtp_max"]
        if res["loudness_range_lu"] is not None:
            checks["loudness_range"] = res["loudness_range_lu"] <= std["loudness_range_lu_max"]
        if res["short_term_max_lufs"] is not None:
            checks["short_term"] = res["short_term_max_lufs"] <= std["short_term_max_lufs"]
        res["checks"] = checks
        res["pass"] = bool(checks) and all(checks.values())
    except (OSError, KeyError, ValueError):
        res["pass"] = None
    return res


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def where(p):
        p.add_argument("--run"); p.add_argument("--asset"); p.add_argument("--out"); p.add_argument("--hero", action="store_true")

    p = sub.add_parser("image"); p.add_argument("file"); where(p); p.add_argument("--spec", nargs="*")
    p.add_argument("--ext", choices=["png", "jpg"], default="png",
                   help="jpg keeps 4 crops under the sandbox's 512 KiB image_paths limit")
    p.add_argument("--panels"); p.add_argument("--ocr", help="tesseract language, e.g. sqi+eng")
    for name in ("frames", "motion", "final"):
        p = sub.add_parser(name); p.add_argument("video"); where(p)
        if name == "frames":
            p.add_argument("--fps", type=float)
    p = sub.add_parser("drift"); p.add_argument("clip"); p.add_argument("slice"); p.add_argument("--out")
    p = sub.add_parser("loudness"); p.add_argument("file")
    a = ap.parse_args(argv)
    res = {"image": cmd_image, "frames": cmd_frames, "motion": cmd_motion, "final": cmd_final, "drift": cmd_drift,
           "loudness": cmd_loudness}[a.cmd](a)
    print(json.dumps(res, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
