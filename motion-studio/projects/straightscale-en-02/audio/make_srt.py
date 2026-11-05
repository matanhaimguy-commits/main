"""SRT captions for the delivery, from the same word timings as the film: the on-screen caption chunks (assets/data.js)
plus chunks for line 1 (the hook, shown as the quote slip in the film) and line 10 (the CTA, shown as the CTA card).
python3 audio/make_srt.py deliver/v1/straightscale_en01.srt"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
W = json.load(open(os.path.join(HERE, "words.json")))["words"]
caps = json.loads(re.search(r"CAPTIONS = (\[.*?\]);", open(os.path.join(ROOT, "assets", "data.js")).read()).group(1))
EXTRA = {1: [(5, "Two years of posting content,"), (2, "running ads,"), (6, "and praying someone books a call.")],
         10: [(2, "Comment WORDS"), (6, "for the exact searches we use.")]}
rows = [(c["t0"] + 0.06, c["t1"], c["text"]) for c in caps]
for line, spec in EXTRA.items():
    ws = [w for w in W if w["line"] == line]
    assert sum(n for n, _ in spec) == len(ws), (line, len(ws))
    k = 0
    for n, text in spec:
        rows.append((ws[k]["s"], ws[k + n - 1]["e"] + 0.15, text)); k += n
rows.sort()
ts = lambda t: f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(round(t % 1 * 1000)) % 1000:03d}"
out = []
for i, (a, b, text) in enumerate(rows):
    b = min(b, rows[i + 1][0]) if i + 1 < len(rows) else b
    out.append(f"{i + 1}\n{ts(a)} --> {ts(b)}\n{text}\n")
open(sys.argv[1], "w").write("\n".join(out))
print(len(rows), "cues ->", sys.argv[1])
