"""The composer: EDL in, a 1080x1920 MP4 with its sound mix out.

Steps: check the edit rules, build the HyperFrames project, render the picture silent, place a sound on every move,
mix voice, effects and the ducked music bed, master with a two-pass loudnorm to -14 LUFS, mux, write report.json.
"""
import json
import time
from pathlib import Path

from . import edl as edl_mod, face as face_mod, hf, mix, project, rules, sfx
from .edl import resolve


def load_face(edl):
    f = edl["twin"].get("face")
    if isinstance(f, dict):
        return f
    if isinstance(f, str):
        return json.loads(resolve(edl, f).read_text())
    return face_mod.run(resolve(edl, edl["twin"]["src"]))


def run(edl_path, out_dir, quality="looks", force=False, render=True, keep_picture=False):
    t0 = time.time()
    edl = edl_mod.load(edl_path)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    face = load_face(edl)
    findings = rules.check(edl, face)
    report = {"edl": str(edl_path), "face": face, "rules": [list(f) for f in findings],
              "summary": rules.summary(edl, face)}
    fails = [f for f in findings if f[0] == "FAIL"]
    if fails and not force:
        (out / "report.json").write_text(json.dumps(report, indent=2))
        raise SystemExit("edit rules failed:\n" + "\n".join(f"  {r}: {m}" for _, r, m in fails))

    build = project.build(edl, face, out / "build")
    cues = sfx.cues(edl)
    report["cues"] = cues
    if not render:
        (out / "report.json").write_text(json.dumps(report, indent=2))
        return report

    video = out / "picture.mp4"
    if not (keep_picture and video.is_file()):
        hf.render(build, video, quality=quality, fps=edl.get("fps"), log=out / "render.log")
        report["render_s"] = round(time.time() - t0, 1)

    music = None
    if edl.get("music"):
        music = dict(edl["music"], src=str(resolve(edl, edl["music"]["src"])))
    voice = resolve(edl, edl["voice"]["src"])
    mix.premix(voice, float(edl["voice"].get("start", 0)), music, cues, edl["duration"],
               out / "premix.wav", out / "stem-voice.wav", out / "stem-music.wav")
    measured, final = mix.master(out / "premix.wav", out / "master.wav")
    report["loudnorm"] = {"pass1": measured, "pass2": final}
    mix.mux(video, out / "master.wav", out / "final.mp4")
    report["output"] = str(out / "final.mp4")
    report["total_s"] = round(time.time() - t0, 1)
    (out / "report.json").write_text(json.dumps(report, indent=2))
    return report
