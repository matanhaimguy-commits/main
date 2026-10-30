"""Write the film's root index.html: every layer as a timed clip, back to front, and the root timeline that places
the twin per beat and whips the frame.

Back to front: set, B-roll and UI, grade, words behind the twin, the twin, words in front, captions, end card, flash.
Every move is a HyperFrames sub-composition from templates/, configured by data-variable-values.
"""
import html
import json
import re
from pathlib import Path

from . import stage, timings
from .moves import LAYERS, MOVES, SCENES, CUTS, FIXED

TEMPLATES = Path(__file__).resolve().parents[1] / "templates"


def comp_id(template):
    text = (TEMPLATES / template).read_text()
    return re.search(r'data-composition-id="([^"]+)"', text).group(1)


def host(el_id, template, start, dur, z, values, track):
    vals = html.escape(json.dumps(values, separators=(",", ":")), quote=True)
    return (f'<div id="{el_id}" class="clip" data-composition-id="{comp_id(template)}" '
            f'data-composition-src="compositions/{template}" data-start="{start:.3f}" data-duration="{dur:.3f}" '
            f'data-track-index="{track}" data-width="1080" data-height="1920" style="z-index:{z}" '
            f"data-variable-values='{vals}'></div>")


def clips(edl, face):
    """Every clip as (z, html). Kept as a list so tests can read it without parsing HTML."""
    dur = edl["duration"]
    out = [(LAYERS["set"], host("set", FIXED["stage"]["template"], 0, dur, LAYERS["set"],
                                dict(edl.get("set", {}), dur=dur), 0))]
    for b in edl["beats"]:
        bid, start, end = b["id"], b["start"], b["end"]
        scene = b.get("scene")
        if scene:
            v = scene.get("vars", {})
            s = start + float(v.get("at", 0))
            if scene["move"] == "broll":
                out.append((LAYERS["scene"],
                            f'<video id="{bid}-broll" class="clip broll" src="{v["src"]}" muted playsinline '
                            f'data-start="{s:.3f}" data-duration="{end - s:.3f}" data-media-start="{float(v.get("from", 0)):.3f}" '
                            f'data-track-index="1" style="z-index:{LAYERS["scene"]}"></video>'))
            else:
                out.append((LAYERS["scene"], host(f"{bid}-scene", SCENES[scene["move"]]["template"], s, end - s,
                                                  LAYERS["scene"], dict(v, dur=round(end - s, 3)), 1)))
        grade = b.get("grade")
        if grade:
            v = grade.get("vars", {})
            s = start + float(v.get("at", 0))
            out.append((LAYERS["grade"], host(f"{bid}-grade", MOVES["bw-grain"]["template"], s, end - s,
                                              LAYERS["grade"], dict(v, dur=round(end - s, 3)), 2)))
        hero = b.get("hero")
        if hero:
            spec = MOVES[hero["move"]]
            v = hero.get("vars", {})
            s = start + float(v.get("at", 0))
            vals = dict(v, dur=round(end - s, 3))
            if spec["layer"] == "split":
                for layer, z in (("back", LAYERS["words-back"]), ("front", LAYERS["words-front"])):
                    out.append((z, host(f"{bid}-hero-{layer}", spec["template"], s, end - s, z,
                                        dict(stage.orbit_geometry(edl, b, vals, face), layer=layer), 3 if layer == "back" else 5)))
            else:
                z = LAYERS[spec["layer"]]
                out.append((z, host(f"{bid}-hero", spec["template"], s, end - s, z, vals, 5)))
        if b.get("cut_in") == "flash":
            out.append((LAYERS["flash"], host(f"{bid}-flash", FIXED["flash"]["template"], max(0, start - 0.05), 0.3,
                                              LAYERS["flash"], edl.get("flash", {}), 8)))
    cap = edl.get("captions")
    if cap:
        words = timings.shift(timings.load(Path(edl["_dir"]) / edl["voice"]["words"])["words"],
                              float(edl["voice"].get("start", 0)))
        hide = [[b["start"], b["end"]] for b in edl["beats"] if b.get("no_captions")] + whip_windows(edl)
        vals = dict({k: v for k, v in cap.items() if k != "enabled"}, words=json.dumps(words), hide=json.dumps(hide),
                    dur=dur)
        out.append((LAYERS["captions"], host("captions", FIXED["captions"]["template"], 0, dur, LAYERS["captions"],
                                             vals, 6)))
    return out


def twin_track(edl, face):
    """GSAP lines that place the twin for each beat (a hard cut between modes)."""
    src_w = face["src_w"] if face else 1080
    lines = []
    for b in edl["beats"]:
        p = stage.placement(edl, b.get("twin", "off"), src_w)
        if p is None:
            lines.append(f'tl.set("#twin-wrap", {{opacity: 0}}, {b["start"]:.3f});')
        else:
            s, left, top = p
            fx, fy = stage.fades(edl, b.get("twin"))
            lines.append(f'tl.set("#twin-wrap", {{opacity: 1, x: {left:.1f}, y: {top:.1f}, scale: {s:.4f}, '
                         f'"--fx": "{fx * 100:.1f}%", "--fy": "{fy * 100:.1f}%"}}, {b["start"]:.3f});')
    return lines


def whip_track(edl):
    """The whip: the frame pushes in and slides sideways with blur, cuts, and the next beat arrives from the other side.
    The push-in (scale 1.25) is larger than the slide (110 px), so no edge of the frame ever shows: no seam."""
    lines = []
    for i, b in enumerate(edl["beats"]):
        if b.get("cut_in") != "whip":
            continue
        t, h = b["start"], CUTS["whip"]["half"]
        d = -1 if i % 2 == 0 else 1
        lines.append(f'tl.fromTo("#frame", {{x: 0, scale: 1, filter: "blur(0px)"}}, {{x: {d * 110}, scale: 1.25, '
                     f'filter: "blur(24px)", duration: {h}, ease: "power3.in", immediateRender: false}}, {t - h:.3f});')
        lines.append(f'tl.fromTo("#frame", {{x: {-d * 110}, scale: 1.25, filter: "blur(24px)"}}, {{x: 0, scale: 1, '
                     f'filter: "blur(0px)", duration: {h + 0.06:.3f}, ease: "power3.out", immediateRender: false}}, {t:.3f});')
    return lines


def whip_windows(edl):
    """[start, end] of every whip, when captions stay off screen."""
    h = CUTS["whip"]["half"]
    return [[round(b["start"] - h, 3), round(b["start"] + h + 0.06, 3)] for b in edl["beats"] if b.get("cut_in") == "whip"]


def font_faces(fonts):
    css = []
    for f in fonts:
        css.append(f'@font-face {{ font-family: "{f["family"]}"; src: url("{f["src"]}") format("woff2"); '
                   f'font-weight: {f.get("weight", 400)}; font-style: {f.get("style", "normal")}; }}')
    return "\n".join(css)


def index_html(edl, face, twin_src, fonts):
    dur, brand = edl["duration"], edl["brand"]
    voice_start = float(edl["voice"].get("start", 0))
    body = "\n      ".join(h for _, h in sorted(clips(edl, face), key=lambda c: c[0]) if True)
    src_w = face["src_w"] if face else 1080
    src_h = face["src_h"] if face else 1890
    script = "\n      ".join(twin_track(edl, face) + whip_track(edl))
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={edl['width']}, height={edl['height']}" />
    <script src="assets/vendor/gsap.min.js"></script>
    <script src="assets/vendor/motion-blur.js"></script>
    <style>
{font_faces(fonts)}
      html, body {{ margin: 0; width: {edl['width']}px; height: {edl['height']}px; overflow: hidden; background: {brand['bg']}; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: {brand['bg']};
        --kit-bg: {brand['bg']}; --kit-fg: {brand['fg']}; --kit-accent: {brand['accent']};
        --kit-display: "{brand['display_font']}", serif; --kit-ui: "{brand['ui_font']}", sans-serif; }}
      #frame {{ position: absolute; inset: 0; overflow: hidden; }}
      .clip {{ position: absolute; inset: 0; }}
      .broll {{ width: 100%; height: 100%; object-fit: cover; }}
      #twin-wrap {{ position: absolute; left: 0; top: 0; width: {src_w}px; height: {src_h}px; transform-origin: 0 0;
        z-index: {LAYERS["twin"]}; opacity: 0; --fx: 0%; --fy: 0%; }}
      #twin {{ position: absolute; inset: 0; width: 100%; height: 100%; }}
      /* soft edges per twin mode (--fx, --fy set on the root timeline): the clip's box never shows */
      #twin-soft {{ position: absolute; inset: 0;
        -webkit-mask-image: linear-gradient(90deg, transparent 0, #000 var(--fx), #000 calc(100% - var(--fx)), transparent 100%),
                            linear-gradient(180deg, #000 calc(100% - var(--fy)), transparent 100%);
        -webkit-mask-composite: source-in; mask-composite: intersect; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{dur:.3f}" data-width="{edl['width']}"
         data-height="{edl['height']}" data-fps="{edl['fps']}">
      <div id="frame">
      {body}
      <div id="twin-wrap"><div id="twin-soft"><video id="twin" class="clip" src="{twin_src}" muted playsinline data-start="{voice_start:.3f}"
           data-duration="{dur - voice_start:.3f}" data-media-start="0" data-track-index="4"></video></div></div>
      </div>
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      {script}
      tl.set({{}}, {{}}, {dur:.3f});
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
