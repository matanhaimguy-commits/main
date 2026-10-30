#!/usr/bin/env python3
"""Twin edit kit CLI (dispatcher only; the work is in kit/).

  python3 twinkit.py cutout clip.mp4 --out twin.webm        cut the person out (HyperFrames remove-background, $0, CPU)
  python3 twinkit.py face twin.webm --out face.json         where the head and face are (from the matte)
  python3 twinkit.py align voice.mp3 script.txt --out words.json   $0 word timings from the script and the pauses
  python3 twinkit.py check edl.json                         the edit rules on an EDL, no render
  python3 twinkit.py compose edl.json --out out/            render the film: picture, sound on every move, ducked bed,
                                                            two-pass loudnorm to -14 LUFS, final.mp4 + report.json
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kit import align, compose, edl as edl_mod, face, hf, rules  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cutout"); c.add_argument("src"); c.add_argument("--out", required=True)
    f = sub.add_parser("face"); f.add_argument("src"); f.add_argument("--out")
    a = sub.add_parser("align"); a.add_argument("audio"); a.add_argument("script"); a.add_argument("--out")
    k = sub.add_parser("check"); k.add_argument("edl")
    m = sub.add_parser("compose"); m.add_argument("edl"); m.add_argument("--out", required=True)
    m.add_argument("--quality", default="looks", choices=["draft", "looks", "delivery"])
    m.add_argument("--force", action="store_true", help="render even when an edit rule fails (logged in the report)")
    m.add_argument("--no-render", action="store_true", help="build the HyperFrames project and the cue list only")
    m.add_argument("--keep-picture", action="store_true", help="reuse out/picture.mp4 and redo the sound only")
    args = ap.parse_args(argv)

    if args.cmd == "cutout":
        hf.remove_background(args.src, args.out, log=str(args.out) + ".log")
        print(args.out)
    elif args.cmd == "face":
        _emit(face.run(args.src), args.out)
    elif args.cmd == "align":
        _emit(align.run(args.audio, Path(args.script).read_text()), args.out)
    elif args.cmd == "check":
        e = edl_mod.load(args.edl)
        findings = rules.check(e, compose.load_face(e))
        for level, rule, msg in findings:
            print(f"  {level:4}  {rule:10}  {msg}")
        print(json.dumps(rules.summary(e)))
        return 1 if any(f[0] == "FAIL" for f in findings) else 0
    elif args.cmd == "compose":
        r = compose.run(args.edl, args.out, quality=args.quality, force=args.force, render=not args.no_render,
                         keep_picture=args.keep_picture)
        print(json.dumps({k: r[k] for k in ("summary", "rules", "output", "total_s") if k in r}, indent=2))
    return 0


def _emit(data, out):
    text = json.dumps(data, indent=1)
    if out:
        Path(out).write_text(text + "\n")
    print(text if not out else out)


if __name__ == "__main__":
    sys.exit(main())
