#!/usr/bin/env python3
"""Wave-end completion audit: (a) file exists non-partial, (b) ends with a coverage statement, (c) handoff JSON parses."""
import json, os, sys, re
F = "/home/user/main/runs/readymerce/foundation"
def check(agent, files, handoff):
    res = {"agent": agent, "ok": True, "notes": []}
    for f in files:
        p = os.path.join(F, f)
        if os.path.exists(p + ".partial") and not os.path.exists(p):
            res["ok"] = False; res["notes"].append(f"{f}: still .partial")
            continue
        if not os.path.exists(p):
            res["ok"] = False; res["notes"].append(f"{f}: MISSING"); continue
        if f.endswith(".md"):
            tail = open(p, encoding="utf-8", errors="replace").read()[-6000:]
            if not re.search(r"COVERAGE|CONFIDENCE|Coverage|Scope:", tail):
                res["ok"] = False; res["notes"].append(f"{f}: no coverage statement in tail")
            if "PARTIAL —" in tail or "PARTIAL -" in tail or "RESUME POINT" in tail:
                res["notes"].append(f"{f}: PARTIAL")
        sz = os.path.getsize(p); res["notes"].append(f"{f}: {sz} bytes")
    hp = os.path.join(F, handoff)
    if not os.path.exists(hp):
        res["ok"] = False; res["notes"].append(f"{handoff}: MISSING")
    else:
        try: json.load(open(hp, encoding="utf-8")); res["notes"].append(f"{handoff}: parses")
        except Exception as e: res["ok"] = False; res["notes"].append(f"{handoff}: JSON ERROR {e}")
    return res
if __name__ == "__main__":
    spec = json.loads(sys.argv[1])  # [{"agent":..,"files":[..],"handoff":..}]
    for s in spec:
        r = check(s["agent"], s["files"], s["handoff"])
        print(("AUDIT-PASS " if r["ok"] else "AUDIT-PARTIAL ") + r["agent"] + " · " + " · ".join(r["notes"]))
