#!/usr/bin/env python3
"""Production pipeline: runs, Shot Specs, the gate ledger, the generation gate and the human queue.

Specs: growth-engine/production/AI-VIDEO-PIPELINE.md (the 16 steps), VISUAL-QA.md (gates and reviewers),
STANDARDS.md + standards.json (every number). One folder per post: clients/<slug>/runs/<post_id>/ holding
ledger.json, shots/, prompts/, qa/, assets/, audio/, edit/, final/ and calls.jsonl.

  pipeline.py init <slug> <post_id> --format F [--card PATH]          create the run folder and ledger
  pipeline.py status <slug> <post_id>                                 steps 0-15, gates, open items, next action
  pipeline.py step <slug> <post_id> <n> --status done|na|blocked [--note T]    close a step (its gates must pass)
  pipeline.py spec-check <slug> <post_id> [shot_id ...]               lint Shot Specs (the G-SPEC pre-check)
  pipeline.py asset <slug> <post_id> <asset_id> --type T [--shots A,B] [--depends X@v1,..] [--hero] [--hook] [--tool NAME]
                                                                      open the next version of an asset
  pipeline.py prompt <slug> <post_id> <asset>[@v] --file F [--media ID:role ...]   the exact prompt + reference order
                                                                      (an edit pass: --media <previous version's id>:edit_source,
                                                                      passed in the call as image_references or image)
  pipeline.py media <slug> <post_id> <asset>[@v] [--id ID ...] [--file PATH ...]   uploaded/generated ids and files
  pipeline.py record <slug> <post_id> <report.json>                   record a reviewer report (orchestrator only)
  pipeline.py gate <slug> <post_id> <GATE> --status PASS|FAIL --by WHO [--asset A@v] [--note T] [--score N] [--data JSON]
  pipeline.py budget <slug> <post_id> --planned USD --balance USD   G-BUDGET in Atlas USD: monthly cap, live balance
                                                                      (`atlas account balance`), 25% retakes
  pipeline.py ask <slug> <post_id> <CHECKPOINT> --note T [--asset A@v] [--files a,b]   queue a human checkpoint
  pipeline.py approve <slug> <post_id> <CHECKPOINT> --by NAME [--asset A@v] [--note T] [--reject]
  pipeline.py queue [--slug S] [--write]                              the daily human approval queue
  pipeline.py check-call <tool_name> <tool_input.json|->              what the PreToolUse hook runs (atlas_generate:
                                                                      what the atlas wrapper in tools/atlas/ runs)

Only this tool changes gate status (VISUAL-QA 9.3): reviewers return JSON, the orchestrator records it here.
Exit code 1 on a blocking problem.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path

import jsonschema
import yaml

import atlas_calls
import atlas_rules
import budget_usd

GE = Path(__file__).resolve().parents[1]
PROD = GE / "production"
ROOT = Path(os.environ.get("PIPELINE_ROOT") or GE.parent)
OUT = ROOT / "growth-engine" / "production"   # logs, failure log, queue (PROD unless tests move ROOT)
STANDARDS = json.loads((PROD / "standards.json").read_text())
SHOT_SCHEMA = yaml.safe_load((PROD / "schemas" / "shot-spec.schema.yaml").read_text())
ORGANIC = json.loads((GE / "config" / "organic.json").read_text())

PASS, FAIL, OVERRIDE, PENDING = "PASS", "FAIL", "OVERRIDE", "PENDING"
OK_STATES = (PASS, OVERRIDE)
SHEET_FORMATS = {"character_sheet", "prop_sheet", "set_sheet"}
REALISTIC = {"realistic_photo", "ugc", "talking_head", "podcast", "drama"}
VIDEO_FORMATS = {"realistic_photo", "ugc", "talking_head", "podcast", "animation_3d", "claymation", "crochet",
                 "animation_2d", "stop_motion", "song", "drama", "motion", "storyboard_panel"}
BLANKET_NO_TEXT = {"text", "no text", "any text", "no text anywhere", "no words", "no writing", "no letters"}
REVIEW_GATES = {"G-SPEC", "G-PROMPT-IMG", "G-PROMPT-VID", "G-VIS", "G-VIS-SHEET", "G-VIS-BOARD", "G-VIS-SLIDE",
                "G-CONTINUITY", "G-SET", "G-TAKE", "G-MOTION-TEXT", "G-MOTION-FRAMES", "G-FINAL"}
CHECK_IDS = {
    "prompt": [f"P{i}" for i in range(1, 13)],
    "visual": [f"V{i}" for i in range(1, 27)],
    "take": [f"T{i}" for i in range(1, 10)],
    "motion": [f"M{i}" for i in range(1, 8)],
    "motion_text": STANDARDS["review_gates_extra"]["G-MOTION-TEXT"]["checks"],
    "final": [f"F{i}" for i in range(1, 9)],
}
IMAGE_ROLES = tuple(STANDARDS["gate_policy"]["image_ref_roles"])
EDIT_SOURCE = STANDARDS["gate_policy"]["edit_source_role"]
EDIT_PASS_HINT = (f"(an edit pass may use this asset's own previous version as the single image reference: register it "
                  f"with role {EDIT_SOURCE}, VISUAL-QA 5.5 route 1)")


def now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def stamp() -> str:
    return now().replace(microsecond=0).isoformat()


def parse_ts(s: str) -> dt.datetime:
    t = dt.datetime.fromisoformat(s)
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)


def norm_prompt(text: str) -> str:
    return " ".join((text or "").split())


def sha_text(text: str) -> str:
    return hashlib.sha256(norm_prompt(text).encode()).hexdigest()


def sha_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


class PipelineError(Exception):
    pass


# ---- runs and the ledger -----------------------------------------------------------------------

def run_dir(slug: str, post_id: str) -> Path:
    return ROOT / "clients" / slug / "runs" / post_id


def ledger_path(slug: str, post_id: str) -> Path:
    return run_dir(slug, post_id) / "ledger.json"


def load_ledger(slug: str, post_id: str) -> dict:
    p = ledger_path(slug, post_id)
    if not p.exists():
        raise PipelineError(f"no run {slug}/{post_id}: start it with pipeline.py init {slug} {post_id} --format <format>")
    return json.loads(p.read_text())


def save_ledger(led: dict) -> None:
    p = ledger_path(led["slug"], led["post_id"])
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(led, indent=2, ensure_ascii=False) + "\n")
    tmp.replace(p)


def all_ledgers(slug: str | None = None):
    base = ROOT / "clients"
    pattern = f"{slug}/runs/*/ledger.json" if slug else "*/runs/*/ledger.json"
    for p in sorted(base.glob(pattern)):
        try:
            yield json.loads(p.read_text())
        except (OSError, json.JSONDecodeError) as e:
            raise PipelineError(f"unreadable ledger {p}: {e}")


def family_for(fmt: str, post_id: str) -> str:
    if post_id.split("-")[1:2] == ["LIB"]:
        return "library"
    if post_id.split("-")[1:2] == ["TEST"]:
        return "test"
    f = ORGANIC["formats"].get(fmt)
    if not f:
        raise PipelineError(f"unknown format {fmt!r}: add it to growth-engine/config/organic.json formats")
    for name, fam in STANDARDS["families"].items():
        if isinstance(fam, dict) and fmt in fam.get("formats", []):
            return name
    if f.get("production"):
        return f["production"]
    return {"image": "still", "carousel": "still"}.get(f["family"], "ai_video")


def init_run(slug: str, post_id: str, fmt: str, card: str | None = None) -> dict:
    if not (ROOT / "clients" / slug).is_dir():
        raise PipelineError(f"no client folder clients/{slug}")
    rd = run_dir(slug, post_id)
    if (rd / "ledger.json").exists():
        raise PipelineError(f"run {slug}/{post_id} exists")
    fam = family_for(fmt, post_id)
    for sub in ("shots", "prompts", "qa", "assets", "audio", "edit", "final"):
        (rd / sub).mkdir(parents=True, exist_ok=True)
    na = set(STANDARDS["families"].get(fam, {}).get("na_steps", []))
    steps = {}
    if fam not in ("library", "test"):
        for s in STANDARDS["steps"]:
            steps[str(s["n"])] = {"status": "na" if s["n"] in na else "todo", "note": "family" if s["n"] in na else ""}
    led = {"post_id": post_id, "slug": slug, "format": fmt, "family": fam, "card": card, "created": stamp(),
           "steps": steps, "run_gates": {}, "specs": {}, "assets": [], "queue": []}
    save_ledger(led)
    return led


def split_ref(ref: str) -> tuple[str, int | None]:
    if "@" in ref:
        a, v = ref.split("@", 1)
        return a, int(v.lstrip("v"))
    return ref, None


def versions(led: dict, asset_id: str) -> list[dict]:
    return [a for a in led["assets"] if a["asset_id"] == asset_id]


def get_asset(led: dict, ref: str) -> dict:
    aid, v = split_ref(ref)
    vs = versions(led, aid)
    if not vs:
        raise PipelineError(f"no asset {aid} in {led['post_id']}")
    if v is None:
        return max(vs, key=lambda a: a["version"])
    for a in vs:
        if a["version"] == v:
            return a
    raise PipelineError(f"no version {v} of {aid}")


def aref(a: dict) -> str:
    return f"{a['asset_id']}@v{a['version']}"


def latest(records: list[dict] | None, **match) -> dict | None:
    for r in reversed(records or []):
        if all(r.get(k) == v for k, v in match.items()):
            return r
    return None


def gate_ok(records: list[dict] | None, **match) -> bool:
    r = latest(records, **match)
    return bool(r and r.get("status") in OK_STATES)


def add_record(target: dict, gate: str, rec: dict) -> dict:
    rec = {"at": stamp(), **rec}
    target.setdefault(gate, []).append(rec)
    return rec


def type_info(t: str) -> dict:
    info = STANDARDS["asset_types"].get(t)
    if not info:
        raise PipelineError(f"unknown asset type {t!r} (standards.json asset_types)")
    return info


# ---- Shot Specs ----------------------------------------------------------------------------------

def spec_path(slug: str, post_id: str, shot_id: str) -> Path:
    return run_dir(slug, post_id) / "shots" / f"{shot_id}.spec.yaml"


def spec_lint(spec: dict, stem: str | None = None, post_id: str | None = None, known_shots: set | None = None) -> list[dict]:
    """The checks a schema can't express (VISUAL-QA 2 and 4.4). Errors block G-SPEC; warnings go to the reviewer."""
    out = []

    def err(code, msg):
        out.append({"level": "error", "code": code, "msg": msg})

    def warn(code, msg):
        out.append({"level": "warn", "code": code, "msg": msg})

    v = jsonschema.Draft202012Validator(SHOT_SCHEMA)
    for e in sorted(v.iter_errors(spec), key=lambda e: list(e.path)):
        err("schema", f"{'/'.join(str(x) for x in e.path) or '(root)'}: {e.message[:200]}")
    if out:
        return out
    fmt = spec["format"]
    if stem and spec["shot_id"] != stem:
        err("name", f"file name {stem} does not match shot_id {spec['shot_id']}")
    if post_id and spec["post_id"] != post_id:
        err("post", f"post_id {spec['post_id']} is not this run ({post_id})")
    sheetlike = fmt in SHEET_FORMATS
    if not sheetlike and (not spec["script_lines"] or not spec["line_text"].strip()):
        err("lines", "script_lines and line_text are required (only sheets have none)")
    if not spec["action_physics"] and not spec.get("static"):
        err("action", "action_physics is empty: write the action as contact points, or set static: true")
    crit = [p for p in spec["props"] if p["story_critical"]]
    for p in crit:
        content = (p.get("content") or "").split()
        if len(content) < 8:
            err("FL-04", f"{p['id']} is story-critical but its content line is missing or thin ({len(content)} words): "
                         "describe materials, layout, seal, colours and any exact short text (4.4)")
        if not p.get("ref") and fmt != "prop_sheet":
            err("prop-sheet", f"{p['id']} is story-critical and has no prop sheet ref (4.4 step 1)")
    texts = [] if spec["text_in_image"] == "none" else spec["text_in_image"]
    blanket = [m for m in spec["must_not"] if m.strip().lower().rstrip(".") in BLANKET_NO_TEXT]
    if blanket and (texts or crit):
        err("FL-04", f"blanket negative {blanket[0]!r} would empty the text or story props: name the unwanted text instead "
                     "('no text on walls', 'no captions')")
    for t in texts:
        if len(t["string"].split()) > 6:
            warn("P6", f"text {t['string']!r} is over 6 words on one surface: split or simplify")
    if fmt in REALISTIC and not (spec["setting"].get("background_action") or "").strip():
        err("FL-09", "realistic scene without setting.background_action (2 or 3 named people doing named actions)")
    if len(spec["must_read_in_1s"].split()) > 20:
        warn("1s", "must_read_in_1s is over 20 words: if it can't be said short, the shot isn't designed yet")
    aspect = spec["camera"]["aspect"]
    if fmt == "carousel_slide" and aspect not in ("4:5", "3:4", "1:1"):
        err("aspect", f"carousel slide at {aspect}: use 4:5 (Instagram feed)")
    if fmt in VIDEO_FORMATS and fmt != "storyboard_panel" and aspect != "9:16":
        warn("aspect", f"video shot at {aspect}: Reels are 9:16")
    hands = [] if spec["hands"] == "none visible" else spec["hands"]
    regions = spec.get("regions") or []
    kinds = {r.get("kind") for r in regions}
    for r in regions:
        x0, y0, x1, y1 = r["box"]
        if not (x0 < x1 and y0 < y1):
            err("region", f"region {r['name']} box {r['box']} is empty or inverted")
    need = []
    if hands and "hand" not in kinds:
        need.append("hand")
    if texts and "text" not in kinds:
        need.append("text")
    if crit and "prop" not in kinds:
        need.append("prop")
    if need:
        (err if spec["hero"] else warn)("regions", f"no region boxes for: {', '.join(need)} "
                                        f"({'hero assets need exact crops' if spec['hero'] else 'the crop script falls back to tiles'})")
    for h in hands:
        if not re.search(r"\b(five|5)\b", h["count_check"]):
            warn("V4", f"hands of {h['who']}: count_check should name five fingers per hand")
    prev = spec["continuity"]["previous_shot"]
    if prev and known_shots is not None and prev not in known_shots:
        warn("continuity", f"previous_shot {prev} has no spec in this run")
    for s in spec["subjects"]:
        if s.get("instances", 1) != 1:
            err("FL-11", f"{s['id']}: one instance per character")
    return out


def spec_check(slug: str, post_id: str, shots: list[str] | None = None) -> tuple[dict, dict]:
    led = load_ledger(slug, post_id)
    sd = run_dir(slug, post_id) / "shots"
    files = sorted(sd.glob("*.spec.yaml"))
    known = {f.name[: -len(".spec.yaml")] for f in files}
    if shots:
        files = [sd / f"{s}.spec.yaml" for s in shots]
    results = {}
    for f in files:
        stem = f.name[: -len(".spec.yaml")]
        if not f.exists():
            results[stem] = [{"level": "error", "code": "missing", "msg": f"no file {f}"}]
            continue
        try:
            spec = yaml.safe_load(f.read_text())
        except yaml.YAMLError as e:
            results[stem] = [{"level": "error", "code": "yaml", "msg": str(e)[:300]}]
            continue
        issues = spec_lint(spec or {}, stem, post_id, known)
        results[stem] = issues
        entry = led["specs"].setdefault(stem, {})
        entry.update({"sha256": sha_file(f), "lint": FAIL if any(i["level"] == "error" for i in issues) else PASS,
                      "lint_at": stamp(), "lint_issues": issues})
    save_ledger(led)
    return led, results


def spec_current_ok(led: dict, shot_id: str) -> tuple[bool, str]:
    p = spec_path(led["slug"], led["post_id"], shot_id)
    if not p.exists():
        return False, f"Shot Spec {shot_id} is missing (write {p.relative_to(ROOT)})"
    entry = led["specs"].get(shot_id)
    cur = sha_file(p)
    if not entry or entry.get("sha256") != cur or entry.get("lint") != PASS:
        return False, f"Shot Spec {shot_id} not linted in its current version (pipeline.py spec-check {led['slug']} {led['post_id']} {shot_id})"
    if not gate_ok(entry.get("G-SPEC"), sha256=cur):
        return False, f"Shot Spec {shot_id} has no G-SPEC PASS for its current version (Prompt Reviewer, spec mode)"
    return True, ""


# ---- assets, prompts, media ---------------------------------------------------------------------

def new_asset(slug, post_id, asset_id, atype, shots=None, depends=None, hero=None, hook=False, tool=None) -> dict:
    led = load_ledger(slug, post_id)
    info = type_info(atype)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{1,60}", asset_id):
        raise PipelineError("asset ids are letters, digits, - and _ (SB-SEQ03, CH-MIRA, SL01, SEQ03-video)")
    vs = versions(led, asset_id)
    if vs and vs[-1]["type"] != atype:
        raise PipelineError(f"{asset_id} is a {vs[-1]['type']}, not a {atype}")
    shots = shots or []
    if info["kind"] in ("image", "video") and not shots:
        raise PipelineError(f"a {atype} serves at least one Shot Spec (--shots)")
    a = {"asset_id": asset_id, "version": (max(x["version"] for x in vs) + 1) if vs else 1, "type": atype,
         "shots": shots, "depends_on": depends or [], "hero": info.get("hero", False) if hero is None else hero,
         "hook": hook, "created": stamp(), "prompt_sha256": None, "prompt_file": None, "prompt_history": [],
         "medias": [], "ids": [], "files": [], "gates": {}}
    if tool:
        a["tool"] = tool
    led["assets"].append(a)
    save_ledger(led)
    return a


def set_prompt(slug, post_id, ref, text: str, medias: list[dict]) -> dict:
    led = load_ledger(slug, post_id)
    a = get_asset(led, ref)
    if not norm_prompt(text):
        raise PipelineError("empty prompt")
    sha = sha_text(text)
    rel = Path("prompts") / f"{a['asset_id']}.v{a['version']}.{len(a['prompt_history']) + 1}.txt"
    (run_dir(slug, post_id) / rel).write_text(text)
    a["prompt_sha256"], a["prompt_file"], a["medias"] = sha, str(rel), medias
    a["prompt_history"].append({"at": stamp(), "sha256": sha, "file": str(rel), "medias": medias})
    save_ledger(led)
    return a


def parse_media(items: list[str] | None) -> list[dict]:
    out = []
    for it in items or []:
        if ":" not in it:
            raise PipelineError(f"--media wants ID:role, got {it!r}")
        v, role = it.split(":", 1)
        out.append({"value": v.strip(), "role": role.strip()})
    return out


def add_media(slug, post_id, ref, ids=None, files=None) -> dict:
    led = load_ledger(slug, post_id)
    a = get_asset(led, ref)
    for i in ids or []:
        if i not in a["ids"]:
            a["ids"].append(i)
    for f in files or []:
        if f not in a["files"]:
            a["files"].append(f)
    save_ledger(led)
    return a


# ---- recording reviews and gates ------------------------------------------------------------------

def _count(checks, result="FAIL"):
    c = {"critical": 0, "major": 0, "minor": 0}
    for ch in checks:
        if ch.get("result") == result:
            c[ch.get("severity") or "major"] = c.get(ch.get("severity") or "major", 0) + 1
    return c


def _require_checks(report: dict, kind: str) -> list[str]:
    ids = {c.get("id") for c in report.get("checks") or []}
    missing = [i for i in CHECK_IDS[kind] if i not in ids]
    return [f"report has no result for {', '.join(missing)}"] if missing else []


def _files_opened_ok(slug, post_id, report, a) -> list[str]:
    opened = set(report.get("files_opened") or [])
    if not opened:
        return ["report cites no files opened: a review that opened no crops is invalid (VISUAL-QA 9.3)"]
    man_p = run_dir(slug, post_id) / "qa" / "crops" / f"{a['asset_id']}.v{a['version']}" / "manifest.json"
    if not man_p.exists():
        return [f"no crop set for {aref(a)}: run growth-engine/tools/vqa_crops.py first (VISUAL-QA 5.1)"]
    man = json.loads(man_p.read_text())
    must = set(man.get("must_open", []))
    names = {Path(x).name for x in opened} | opened
    missing = sorted(m for m in must if m not in names and Path(m).name not in names)
    return [f"reviewer did not open: {', '.join(missing[:8])}{' ...' if len(missing) > 8 else ''}"] if missing else []


def failure_log(led, gate, asset, checks) -> None:
    p = OUT / "failure-log.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    new = not p.exists()
    with p.open("a") as f:
        if new:
            f.write("date,client,post,asset,gate,check,severity,evidence\n")
        for c in checks:
            if c.get("result") == FAIL:
                ev = (c.get("evidence") or "").replace('"', "'").replace("\n", " ")[:300]
                f.write(f"{stamp()[:10]},{led['slug']},{led['post_id']},{asset},{gate},{c.get('id')},{c.get('severity', '')},\"{ev}\"\n")


def _queue_add(led, checkpoint, note, asset=None, files=None, kind="decision"):
    qid = f"{checkpoint}:{asset or ''}"
    for q in led["queue"]:
        if q["id"] == qid and q["status"] == PENDING:
            q["note"] = note
            return q
    q = {"id": qid, "checkpoint": checkpoint, "asset": asset, "status": PENDING if kind == "decision" else "FYI",
         "note": note, "files": files or [], "asked_at": stamp()}
    led["queue"].append(q)
    return q


def record_report(slug: str, post_id: str, report: dict) -> tuple[str, list[str]]:
    """Validate a reviewer report and write the gate. Returns (recorded status, notes)."""
    led = load_ledger(slug, post_id)
    gate = report.get("gate", "")
    notes = []
    if report.get("independent") is not True:
        raise PipelineError("reports come from a fresh reviewer that never saw the producer's reasoning: set "
                            "\"independent\": true only when that is so (VISUAL-QA 9.3)")
    reviewer = report.get("reviewer") or "reviewer"
    status = report.get("status")
    if status not in (PASS, FAIL):
        raise PipelineError("status must be PASS or FAIL")
    pol = STANDARDS["gate_policy"]
    rel = report.get("_file")

    if gate == "G-SPEC":
        sid = report.get("shot_id")
        ok, why = True, ""
        p = spec_path(slug, post_id, sid or "?")
        if not p.exists():
            raise PipelineError(f"no spec {sid}")
        cur = sha_file(p)
        if report.get("spec_sha256") != cur:
            raise PipelineError(f"review is for spec hash {report.get('spec_sha256')}, the file is now {cur}: review again")
        entry = led["specs"].get(sid) or {}
        if entry.get("sha256") != cur or entry.get("lint") != PASS:
            status, why = FAIL, "lint has not passed for this version"
        if any(c.get("result") == FAIL for c in report.get("checks") or []):
            status = FAIL
        if why:
            notes.append(why)
        add_record(led["specs"].setdefault(sid, {}), "G-SPEC",
                   {"status": status, "sha256": cur, "by": reviewer, "report": rel})
        save_ledger(led)
        return status, notes

    if gate in ("G-CONTINUITY", "G-SET"):
        covers = report.get("covers") or []
        if not covers:
            raise PipelineError(f"{gate} names the asset versions it covers (covers: [SB-SEQ01@v2, ...])")
        for c in covers:
            a = get_asset(led, c)
            vg = type_info(a["type"]).get("visual_gate")
            if not gate_ok(a["gates"].get(vg)):
                status = FAIL
                notes.append(f"{c} has no {vg} PASS")
        if not report.get("files_opened"):
            status = FAIL
            notes.append("report cites no files opened")
        if any(c.get("result") == FAIL for c in report.get("checks") or []):
            status = FAIL
        add_record(led["run_gates"], gate, {"status": status, "by": reviewer, "report": rel,
                                            "covers": [aref(get_asset(led, c)) for c in covers]})
        if status == FAIL:
            failure_log(led, gate, ",".join(covers), report.get("checks") or [])
        save_ledger(led)
        return status, notes

    a = get_asset(led, f"{report.get('asset_id')}@v{report.get('version')}")
    info = type_info(a["type"])

    if gate in ("G-PROMPT-IMG", "G-PROMPT-VID"):
        if gate != info.get("prompt_gate"):
            raise PipelineError(f"{aref(a)} is a {a['type']}: its prompt gate is {info.get('prompt_gate')}")
        if report.get("prompt_sha256") != a["prompt_sha256"]:
            raise PipelineError(f"review is for prompt {report.get('prompt_sha256')}, the registered prompt is "
                                f"{a['prompt_sha256']}: review the registered prompt")
        miss = _require_checks(report, "prompt")
        if miss or any(c.get("result") == FAIL for c in report["checks"]):
            status = FAIL
        notes += miss
        add_record(a["gates"], gate, {"status": status, "by": reviewer, "report": rel, "prompt_sha256": a["prompt_sha256"]})
        if status == FAIL:
            loops = sum(1 for r in a["gates"][gate] if r["status"] == FAIL)
            failure_log(led, gate, aref(a), report.get("checks") or [])
            if loops >= pol["max_prompt_loops"]:
                notes.append(f"prompt loop limit reached ({loops} of {pol['max_prompt_loops']}): the Organic Director decides "
                             "(rewrite, simplify the shot, or send it to the owner as G-HUMAN-ESCALATE; VISUAL-QA 4.3, "
                             "STANDARDS 9)")
        save_ledger(led)
        return status, notes

    if gate.startswith("G-VIS"):
        if gate != info.get("visual_gate"):
            raise PipelineError(f"{aref(a)} is a {a['type']}: its visual gate is {info.get('visual_gate')}")
        miss = _require_checks(report, "visual") + _files_opened_ok(slug, post_id, report, a)
        hero = bool(a.get("hero") or report.get("hero"))
        lim = pol["visual_pass"]["hero" if hero else "other"]
        cnt = _count(report.get("checks") or [])
        over = [f"{k} {cnt[k]} > {lim[k]}" for k in ("critical", "major", "minor") if cnt[k] > lim[k]]
        if miss or over:
            status = FAIL
        notes += miss + ([f"pass rule ({'hero' if hero else 'other'}): " + ", ".join(over)] if over else [])
        add_record(a["gates"], gate, {"status": status, "by": reviewer, "report": rel, "defects": cnt, "hero": hero})
        if status == FAIL:
            failure_log(led, gate, aref(a), report.get("checks") or [])
            tries = len({x["version"] for x in versions(led, a["asset_id"]) if latest(x["gates"].get(gate), status=FAIL)})
            if tries >= pol["max_image_attempts"]:
                _queue_add(led, "G-HUMAN-ESCALATE", f"{a['asset_id']}: failed {tries} attempts at {gate}; best version and "
                                                    f"its report go to the owner (VISUAL-QA 5.5)", aref(a), a["files"])
                notes.append("escalated: attempt limit reached")
        save_ledger(led)
        return status, notes

    if gate == "G-MOTION-TEXT":
        if gate != info.get("text_gate"):
            raise PipelineError(f"{aref(a)} is a {a['type']}: G-MOTION-TEXT reviews a motion_render's text constants")
        miss = _require_checks(report, "motion_text")
        if not report.get("files_opened"):
            miss.append("report cites no files opened (the code's text constants, the spec, the released script)")
        if miss or any(c.get("result") == FAIL for c in report.get("checks") or []):
            status = FAIL
        notes += miss
        add_record(a["gates"], gate, {"status": status, "by": reviewer, "report": rel})
        if status == FAIL:
            failure_log(led, gate, aref(a), report.get("checks") or [])
        save_ledger(led)
        return status, notes

    if gate in ("G-TAKE", "G-MOTION-FRAMES", "G-FINAL"):
        kind = {"G-TAKE": "take", "G-MOTION-FRAMES": "motion", "G-FINAL": "final"}[gate]
        if gate != info.get("visual_gate"):
            raise PipelineError(f"{aref(a)} is a {a['type']}: its review gate is {info.get('visual_gate')}")
        miss = _require_checks(report, kind)
        if not report.get("files_opened"):
            miss.append("report cites no frames opened")
        cnt = _count(report.get("checks") or [])
        lim = pol["take_pass"]
        over = [f"{k} {cnt[k]} > {lim[k]}" for k in ("critical", "major") if cnt[k] > lim[k]]
        if gate == "G-MOTION-FRAMES" and info.get("text_gate") and not gate_ok(a["gates"].get(info["text_gate"])):
            miss.append(f"no {info['text_gate']} PASS on {aref(a)}: a fresh prompt-reviewer checks the code's text "
                        "constants before any render (VISUAL-QA 7.2)")
        if miss or over or (gate == "G-TAKE" and report.get("retake_needed")):
            status = FAIL
        notes += miss + over
        add_record(a["gates"], gate, {"status": status, "by": reviewer, "report": rel, "defects": cnt,
                                      "retake_needed": bool(report.get("retake_needed")),
                                      "edit_fixes": report.get("edit_fixes") or []})
        if gate == "G-FINAL":
            add_record(led["run_gates"], "G-FINAL", {"status": status, "by": reviewer, "report": rel, "covers": [aref(a)]})
        if status == FAIL:
            failure_log(led, gate, aref(a), report.get("checks") or [])
            tries = len({x["version"] for x in versions(led, a["asset_id"]) if latest(x["gates"].get(gate), status=FAIL)})
            if gate == "G-TAKE" and tries >= pol["max_video_attempts"]:
                _queue_add(led, "G-HUMAN-ESCALATE", f"{a['asset_id']}: {tries} takes failed; simplify the shot or decide "
                                                    f"(VISUAL-QA 7.1)", aref(a), a["files"])
        save_ledger(led)
        return status, notes

    raise PipelineError(f"unknown review gate {gate!r} (use pipeline.py gate for script, audio and human gates)")


def is_human(by: str) -> bool:
    return by.strip() in STANDARDS["humans"]


def record_gate(slug, post_id, gate, status, by, asset=None, note=None, score=None, data=None, covers=None) -> dict:
    led = load_ledger(slug, post_id)
    if status not in (PASS, FAIL, OVERRIDE):
        raise PipelineError("status is PASS, FAIL or OVERRIDE")
    hc = STANDARDS["human_checkpoints"].get(gate)
    if hc:
        if hc["mode"] == "delegable" and not is_human(by):
            if not by.startswith("claude (delegated)"):
                raise PipelineError(f"{gate} is the owner's call; Claude may take it only as 'claude (delegated)' with a --note")
        elif hc["mode"] == "director" and not (is_human(by) or by.startswith("organic-director")):
            raise PipelineError(f"{gate} is the Director's call (organic-director agent) or the owner's")
        elif hc["mode"] not in ("delegable", "director") and not is_human(by):
            raise PipelineError(f"{gate} is a human checkpoint: --by must be one of {STANDARDS['humans']} "
                                f"(record what the owner said; never approve on their behalf)")
        if not note:
            raise PipelineError(f"{gate}: say what was decided and where (--note)")
    if gate in REVIEW_GATES and status != OVERRIDE:
        raise PipelineError(f"{gate} is a reviewer gate: record the fresh reviewer's JSON with pipeline.py record "
                            "(only the owner can OVERRIDE it, with a reason)")
    if status == OVERRIDE and not (is_human(by) and note):
        raise PipelineError("an OVERRIDE needs the owner as --by and the reason as --note (hub G: confirm once, then follow)")
    if gate == "G-SCRIPT" and status == PASS:
        if score is None or score < STANDARDS["gate_policy"]["script_release_score"]:
            raise PipelineError(f"G-SCRIPT PASS needs --score of {STANDARDS['gate_policy']['script_release_score']}+ "
                                "from the Script Lab gate (organic carousels: the copy gate score)")
    rec = {"status": status, "by": by}
    if note:
        rec["note"] = note
    if score is not None:
        rec["score"] = score
    if data:
        rec["data"] = data
    if covers:
        rec["covers"] = covers
    if asset:
        a = get_asset(led, asset)
        add_record(a["gates"], gate, rec)
    else:
        add_record(led["run_gates"], gate, rec)
    if hc and hc["mode"] == "delegable" and not is_human(by):
        _queue_add(led, gate, f"FYI (delegated): {note}", asset, kind="fyi")
    for q in led["queue"]:
        if q["checkpoint"] == gate and q["status"] == PENDING and (asset is None or q.get("asset") in (None, asset)):
            if is_human(by):
                q.update({"status": "APPROVED" if status in OK_STATES else "REJECTED", "answered_at": stamp(), "by": by,
                          "answer": note})
    save_ledger(led)
    return rec


def budget(slug, post_id, planned: float, balance: float, el: float = 0.0) -> dict:
    """G-BUDGET in Atlas USD (budget_usd.py): planned and the live balance in USD. el: ElevenLabs credits, history."""
    return budget_usd.run(sys.modules[__name__], slug, post_id, planned, balance, el)


# ---- steps and status -----------------------------------------------------------------------------

def client_gate_ok(led: dict, gate: str, **match) -> bool:
    if gate_ok(led["run_gates"].get(gate), **match):
        return True
    for other in all_ledgers(led["slug"]):
        if other["family"] == "library" and gate_ok(other["run_gates"].get(gate), **match):
            return True
    return False


def step_gates(led: dict, n: int) -> list[str]:
    over = STANDARDS.get("step_gate_by_family", {}).get(led["family"], {})
    if str(n) in over:
        return over[str(n)]
    return next(s["gates"] for s in STANDARDS["steps"] if s["n"] == n)


def gate_state(led: dict, gate: str) -> tuple[bool, str]:
    if gate == "G-SPEC":
        specs = sorted(p.name[: -len(".spec.yaml")] for p in (run_dir(led["slug"], led["post_id"]) / "shots").glob("*.spec.yaml"))
        if not specs:
            return False, "no Shot Specs written"
        bad = [why for s in specs for ok, why in [spec_current_ok(led, s)] if not ok]
        return (not bad), "; ".join(bad[:3])
    if gate == "G-ASSETS":
        bad = []
        for aid in sorted({a["asset_id"] for a in led["assets"]}):
            a = max(versions(led, aid), key=lambda x: x["version"])
            info = type_info(a["type"])
            g = info.get("visual_gate") or info.get("audio_gate")
            if g and info["kind"] != "final" and not gate_ok(a["gates"].get(g)):
                bad.append(f"{aref(a)} {g}")
        return (not bad), ("open: " + ", ".join(bad[:6])) if bad else ""
    if gate == "G-MOTION-TEXT":
        renders = [max(versions(led, aid), key=lambda x: x["version"])
                   for aid in sorted({a["asset_id"] for a in led["assets"] if type_info(a["type"]).get("text_gate") == gate})]
        if not renders:
            return False, "no motion_render asset registered for G-MOTION-TEXT (the code's text constants review)"
        bad = [aref(a) for a in renders if not gate_ok(a["gates"].get(gate))]
        return (not bad), ("G-MOTION-TEXT open: " + ", ".join(bad)) if bad else ""
    hc = STANDARDS["human_checkpoints"].get(gate, {})
    if hc.get("mode") in ("per_series", "per_voice"):
        return client_gate_ok(led, gate), f"{gate} not recorded for this run or the client's LIB run"
    return gate_ok(led["run_gates"].get(gate)), f"{gate} has no PASS"


def budget_after_steps(led: dict, n: int) -> tuple[bool, str]:
    """Step 9 re-prices the whole video: its G-BUDGET PASS must be newer than every earlier step's close (D-a)."""
    b = latest(led["run_gates"].get("G-BUDGET"))
    if not b or b["status"] not in OK_STATES:
        return False, "G-BUDGET has no PASS"
    closed = [parse_ts(st["at"]) for k, st in led["steps"].items()
              if int(k) < n and st.get("status") == "done" and st.get("at")]
    if closed and parse_ts(b["at"]) < max(closed):
        return False, (f"the last G-BUDGET ({b['at']}) is older than step {n - 1}'s close: re-price the whole piece with "
                       f"pipeline.py budget {led['slug']} {led['post_id']} --planned USD --balance USD")
    return True, ""


def close_step(slug, post_id, n: int, status: str, note: str = "") -> dict:
    led = load_ledger(slug, post_id)
    st = led["steps"].get(str(n))
    if st is None:
        raise PipelineError(f"no step {n} in a {led['family']} run")
    if status == "done":
        for g in step_gates(led, n):
            ok, why = gate_state(led, g)
            if not ok:
                raise PipelineError(f"step {n} can't close: {why}")
            if g == "G-BUDGET":
                ok, why = budget_after_steps(led, n)
                if not ok:
                    raise PipelineError(f"step {n} can't close: {why}")
        for m in range(n):
            if led["steps"][str(m)]["status"] in ("todo", "blocked"):
                raise PipelineError(f"step {m} is still {led['steps'][str(m)]['status']}: the order is the point "
                                    "(words before sound, sound before pictures, plan before assets)")
    elif status == "na":
        if n not in STANDARDS["families"].get(led["family"], {}).get("na_steps", []) and not note:
            raise PipelineError(f"step {n} applies to {led['family']} runs: say why it is skipped (--note)")
    elif status != "blocked":
        raise PipelineError("status is done, na or blocked")
    st.update({"status": status, "note": note, "at": stamp()})
    save_ledger(led)
    return st


def status_report(slug, post_id) -> str:
    led = load_ledger(slug, post_id)
    lines = [f"{post_id} ({led['format']}, {led['family']})"]
    nxt = None
    for s in STANDARDS["steps"]:
        st = led["steps"].get(str(s["n"]))
        if not st:
            continue
        gates = step_gates(led, s["n"])
        gs = []
        for g in gates:
            ok, _ = gate_state(led, g)
            gs.append(f"{g} {'ok' if ok else '..'}")
        lines.append(f"  {s['n']:>2} {s['name']:<40} {st['status']:<8} {'  '.join(gs)}")
        if nxt is None and st["status"] in ("todo", "blocked"):
            nxt = s
    for aid in sorted({a["asset_id"] for a in led["assets"]}):
        a = max(versions(led, aid), key=lambda x: x["version"])
        gs = ", ".join(f"{g}:{(r[-1]['status'] if r else '-')}" for g, r in a["gates"].items()) or "no gates yet"
        lines.append(f"  asset {aref(a):<22} {a['type']:<15} {gs}")
    pend = [q for q in led["queue"] if q["status"] == PENDING]
    if pend:
        lines.append("  waiting on the owner: " + "; ".join(f"{q['checkpoint']} {q.get('asset') or ''}".strip() for q in pend))
    if nxt:
        lines.append(f"  next: step {nxt['n']} {nxt['name']}")
    return "\n".join(lines)


def queue_report(slug=None) -> tuple[str, int]:
    rows = []
    for led in all_ledgers(slug):
        for q in led["queue"]:
            if q["status"] in (PENDING, "FYI") and not q.get("seen"):
                rows.append((led["slug"], led["post_id"], q))
    pend = [r for r in rows if r[2]["status"] == PENDING]
    out = [f"# Approval queue, {now().date().isoformat()}", "",
           f"{len(pend)} decision(s) waiting. Answer in chat (\"approve SB-SEQ01\", \"reject, because ...\"); "
           "Claude records it with pipeline.py approve. Final approval of posts happens on the hub's Content page.", ""]
    for slug_, post, q in sorted(rows, key=lambda r: (r[2]["status"] != PENDING, r[0], r[1])):
        what = STANDARDS["human_checkpoints"].get(q["checkpoint"], {}).get("what", "")
        out.append(f"- [{q['status']}] {slug_} {post} {q['checkpoint']} {q.get('asset') or ''}: {q['note']}")
        if what:
            out.append(f"  - What it is: {what}")
        for f in q.get("files") or []:
            out.append(f"  - File: {f}")
    return "\n".join(out) + "\n", len(pend)


# ---- the generation gate (PreToolUse hook) -----------------------------------------------------------

def _params(x):
    if isinstance(x, str):
        try:
            x = json.loads(x)
        except json.JSONDecodeError:
            return None
    return x if isinstance(x, dict) else None


def extract_requests(tool_name: str, ti: dict, spec: dict) -> list[dict]:
    reqs = []
    if spec["service"] == "atlas":
        # built by growth-engine/tools/atlas/atlas_gate.py from an `atlas generate <kind> MODEL ...` command line
        if ti.get("kind") == "chat":
            return [{"error": "atlas chat is a billable LLM call outside the production pipeline: the gate blocks it "
                              "(prompts and scripts are written in the session)"}]
        medias, p = ti.get("medias") or [], ti.get("params") or {}
        if ti.get("kind") not in ("image", "video", "audio", "3d") or not isinstance(ti.get("model"), str) \
                or not isinstance(ti.get("prompt") or "", str) or not isinstance(p, dict) or not isinstance(medias, list) \
                or not all(isinstance(m, dict) and isinstance(m.get("value"), str) and isinstance(m.get("role"), str)
                           for m in medias):
            return [{"error": "atlas_generate input must be {kind, model, prompt, medias, params} "
                              "(growth-engine/tools/atlas/atlas_gate.py builds it)"}]
        return [{"kind": ti["kind"], "service": "atlas", "model": ti["model"], "prompt": ti.get("prompt") or "",
                 "medias": [{"value": m.get("value"), "role": m.get("role")} for m in medias], "params": dict(p),
                 "dry": False}]
    if spec["service"] == "higgs":
        items = (ti.get("requests") or []) if spec.get("batch") else [{"params": ti.get("params")}]
        for it in items:
            p = _params(it.get("params"))
            if p is None:
                reqs.append({"error": "params must be a JSON object so the gate can read the prompt and references"})
                continue
            reqs.append({"kind": spec["kind"], "model": p.get("model"), "prompt": p.get("prompt") or "",
                         "medias": [{"value": m.get("value"), "role": m.get("role")} for m in p.get("medias") or []],
                         "params": p, "dry": bool(p.get("get_cost"))})
        return reqs
    kind = spec["kind"]
    if kind == "nodes":
        return [{"kind": "nodes", "node_ids": ti.get("node_ids") or [], "dry": bool(ti.get("estimate_only")), "params": ti}]
    if kind == "by_node_type":
        kind = {"image-generation": "image", "image-transform": "image", "video-generation": "video", "tts": "tts",
                "music": "music", "sfx": "sfx", "audio-effects": "sfx", "composition": "music"}.get(ti.get("node_type"), "el_other")
    return [{"kind": kind, "model": ti.get("model_id"), "prompt": ti.get("prompt") or "",
             "medias": [{"value": n, "role": "node"} for n in ti.get("connect_from") or []],
             "params": ti, "dry": bool(ti.get("estimate_only"))}]


def find_by_prompt(sha: str):
    hits = []
    for led in all_ledgers():
        for a in led["assets"]:
            if a.get("prompt_sha256") == sha:
                hits.append((led, a))
    hits.sort(key=lambda h: (h[1]["created"], h[1]["version"]))
    return hits[-1] if hits else (None, None)


def find_by_id(slug: str, media_id: str):
    for led in all_ledgers(slug):
        for a in led["assets"]:
            if media_id in a.get("ids", []):
                return led, a
    return None, None


def calls_log(led: dict | None) -> Path:
    if led is None:
        p = OUT / "logs" / "gate-unmatched.jsonl"
        p.parent.mkdir(parents=True, exist_ok=True)
        return p
    return run_dir(led["slug"], led["post_id"]) / "calls.jsonl"


def generated_before(led: dict, a: dict) -> bool:
    p = calls_log(led)
    if not p.exists():
        return False
    for line in p.read_text().splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("decision") == "ALLOW" and not e.get("dry") and not e.get("analysis") and e.get("asset") == aref(a):
            return True
    return False


def attempts(led: dict, asset_id: str) -> int:
    p = calls_log(led)
    if not p.exists():
        return 0
    seen = set()
    for line in p.read_text().splitlines():
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("decision") == "ALLOW" and not e.get("dry") and not e.get("analysis") \
                and (e.get("asset") or "").split("@")[0] == asset_id:
            seen.add(e["asset"])
    return len(seen)


def _gate_any_version(led, a, gate, **match) -> bool:
    for x in versions(led, a["asset_id"]):
        if gate_ok(x["gates"].get(gate), **match):
            return True
    return False


def _spec_aspect(a: dict, led: dict, p: dict) -> list[str]:
    if a["type"] in ("storyboard", "style_ref") or a["type"].endswith("_sheet"):
        return []
    aspects = set()
    for s in a["shots"]:
        sp = spec_path(led["slug"], led["post_id"], s)
        if sp.exists():
            aspects.add((yaml.safe_load(sp.read_text()) or {}).get("camera", {}).get("aspect"))
    if len(aspects) == 1 and p.get("aspect_ratio") not in aspects:
        return [f"aspect_ratio {p.get('aspect_ratio')} differs from the Shot Spec ({aspects.pop()})"]
    return []


def _atlas_entry(model, kind: str) -> tuple[dict | None, list[str]]:
    """The owner's entry for an Atlas model (standards.json models.atlas.allowed; atlas_rules.py)."""
    return atlas_rules.find_entry(STANDARDS["models"]["atlas"]["allowed"], model, kind)


def _atlas_text(req: dict, e: dict) -> str:
    return atlas_rules.review_text(req, e)


def _atlas_checks(req: dict, a: dict, led: dict) -> list[str]:
    return atlas_calls.checks(sys.modules[__name__], req, a, led)


def _model_checks(req: dict, a: dict, led: dict) -> list[str]:
    why = []
    kind, model, p = req["kind"], req.get("model"), req["params"]
    std = STANDARDS["models"]
    if req.get("service") == "atlas":
        return _atlas_checks(req, a, led)
    exc = latest(a["gates"].get("G-EXCEPTION"))
    if exc and exc["status"] in OK_STATES and (exc.get("data") or {}).get("model") == model:
        return []
    tool_service = "elevenlabs" if "model_id" in p or "node_ids" in p else "higgs"
    if kind == "image":
        if tool_service == "elevenlabs":
            if model not in std["elevenlabs"]["image"]:
                why.append(f"image model {model} via ElevenLabs is not in the standards: stills come from Higgsfield "
                           f"({', '.join(std['image'])}); a one-off needs G-EXCEPTION")
            return why
        m = std["image"].get(model)
        if not m:
            why.append(f"image model {model} is not in standards.json models.image ({', '.join(std['image'])})")
        elif a["type"] not in m["use"]:
            why.append(f"{model} is not the standard model for a {a['type']} (STANDARDS.md 1; R1 for stylized sheets)")
        if m:
            for k, v in (m.get("params") or {}).items():
                if p.get(k) != v:
                    why.append(f"{model}: pass {k}: {v!r} (STANDARDS.md 1; the model default differs)")
            for k, opts in (m.get("params_one_of") or {}).items():
                if p.get(k) not in opts:
                    why.append(f"{model}: pass {k} as one of {opts} (STANDARDS.md 1), not {p.get(k)!r}")
            for k, opts in (m.get("params_if_given") or {}).items():
                if k in p and p[k] not in opts:
                    why.append(f"{model}: {k} must be one of {opts} (STANDARDS.md 1)")
            if m.get("aspect_ratios") and p.get("aspect_ratio") is not None and p.get("aspect_ratio") not in m["aspect_ratios"]:
                why.append(f"{model} has no {p.get('aspect_ratio')} output (STANDARDS.md 1: a 4:5 slide with a photoreal "
                           "person is made in gpt_image_2_5 with the person's approved still as a reference)")
            n_img = sum(1 for x in req.get("medias") or [] if x.get("role") in IMAGE_ROLES)
            if n_img < m.get("min_image_refs", 0):
                why.append(f"{model} always takes a reference photo (hub G7, STANDARDS.md 1)")
            if a["type"] in (m.get("refuse_people_for") or []):
                people = std.get("image_people_spec_formats") or []
                fmts = set()
                for s_ in a["shots"]:
                    sp = spec_path(led["slug"], led["post_id"], s_)
                    if sp.exists():
                        fmts.add((yaml.safe_load(sp.read_text()) or {}).get("format"))
                if fmts & set(people):
                    why.append(f"{model} is not used for realistic people in a {a['type']} ({', '.join(sorted(fmts & set(people)))}): "
                               "gpt_image_2 with a reference photo (STANDARDS.md 1, hub G7)")
        why += _spec_aspect(a, led, p)
    elif kind == "video":
        if tool_service == "elevenlabs":
            fb = std["elevenlabs"].get("video_fallback", {}).get(model)
            if fb and gate_ok(a["gates"].get(fb)):
                return []
            return [f"video via ElevenLabs ({model}) is outside the standards (hub G1): H3 only"
                    + (f"; {model} is a fallback that needs {fb} on {aref(a)}" if fb else ", or G-EXCEPTION")]
        m = std["video"].get(model)
        if not m:
            return [f"video model {model} is banned by the standards (hub G1/G2); a drama exception needs G-EXCEPTION "
                    f"with data {{\"model\": \"{model}\"}}"]
        if m.get("needs_gate") and not gate_ok(a["gates"].get(m["needs_gate"])):
            why.append(f"{model} is a fallback: record {m['needs_gate']} on {aref(a)} first (Director or owner)")
        if m.get("declined_preset_id") and p.get("declined_preset_id") != m["declined_preset_id"]:
            why.append(f"pass declined_preset_id {m['declined_preset_id']} (hub G1)")
        if m.get("resolution") and p.get("resolution") != m["resolution"]:
            why.append(f"pass resolution {m['resolution']!r} (hub G1)")
        if m.get("aspect_ratio") and p.get("aspect_ratio") != m["aspect_ratio"]:
            why.append(f"aspect_ratio must be {m['aspect_ratio']}")
        d = p.get("duration")
        if "min_s" in m and (not isinstance(d, (int, float)) or not m["min_s"] <= d <= m["max_s"]):
            why.append(f"duration {d!r} outside {m['min_s']} to {m['max_s']} s (STANDARDS.md clip rules)")
    elif kind in ("tts", "music", "sfx"):
        allowed = std["elevenlabs"].get(kind, [])
        if model not in allowed:
            why.append(f"{kind} model {model} is not in the standards ({', '.join(allowed)})")
    elif kind == "audio":
        why.append("Higgsfield speech and audio are retired for our content (hub G8): use ElevenLabs")
    elif kind == "el_other":
        why.append(f"ElevenLabs node type {p.get('node_type')} is not a production step here")
    return why


def _check_request(req: dict) -> tuple[bool, list[str], dict | None, dict | None]:
    if req.get("error"):
        return False, [req["error"]], None, None
    if req.get("dry"):
        return True, ["cost preflight"], None, None
    if req["kind"] == "nodes":
        why, led0, a0 = [], None, None
        for nid in req["node_ids"]:
            led, a = None, None
            for l in all_ledgers():
                for x in l["assets"]:
                    if nid in x.get("ids", []):
                        led, a = l, x
            if not a:
                why.append(f"flow node {nid} is not registered on an asset (pipeline.py media ... --id {nid})")
                continue
            ok, w, _, _ = _check_asset(led, a, req, prompt_sha=a.get("prompt_sha256"))
            why += w
            led0, a0 = led, a
        return (not why), why, led0, a0
    if norm_prompt(req.get("prompt")) == "GATE-SELFTEST":
        return False, ["self-test: the production gate is live in this session"], None, None
    if req.get("service") == "atlas":
        # the owner's list first, so nobody registers prompts for a model that can't pass
        e, why = _atlas_entry(req.get("model"), req["kind"])
        if why:
            return False, why, None, None
        if e.get("analysis"):
            return atlas_calls.analysis(sys.modules[__name__], req, e)
        req["atlas"], req["prompt"] = e, _atlas_text(req, e)
    if not norm_prompt(req.get("prompt")):
        return False, ["no prompt: every generation carries the reviewed prompt card"], None, None
    sha = sha_text(req["prompt"])
    led, a = find_by_prompt(sha)
    if not a:
        return False, [f"this prompt (sha256 {sha[:12]}) is not registered on any asset. Write the Shot Spec, register the "
                       "prompt (pipeline.py asset ... then pipeline.py prompt ... --file), get the Prompt Reviewer's PASS, "
                       "then call with exactly that text"], None, None
    ok, why, _, _ = _check_asset(led, a, req, prompt_sha=sha)
    return ok, why, led, a


def _role_match(registered: str, called: str) -> bool:
    if registered == EDIT_SOURCE:
        return called in IMAGE_ROLES
    return registered == called


def _check_asset(led: dict, a: dict, req: dict, prompt_sha: str | None):
    why = []
    info = type_info(a["type"])
    kind = req["kind"]
    want = {"image": "image", "video": "video", "tts": "audio", "music": "audio", "sfx": "audio", "audio": "audio",
            "nodes": info["kind"]}.get(kind, kind)
    pol = STANDARDS["gate_policy"]
    b = latest(led["run_gates"].get("G-BUDGET"))
    if not b or b["status"] not in OK_STATES:
        why.append(f"no G-BUDGET PASS for {led['post_id']} (pipeline.py budget {led['slug']} {led['post_id']} --planned USD --balance USD)")
    elif now() - parse_ts(b["at"]) > dt.timedelta(hours=pol["budget_fresh_hours"]):
        why.append(f"G-BUDGET is older than {pol['budget_fresh_hours']} h: check the live Atlas balance again (it is shared)")
    st9 = led.get("steps", {}).get("9")
    if info["kind"] == "video" and st9 and st9.get("status") != "done" and st9.get("status") != "na":
        why.append(f"step 9 (budget preflight) is not closed for {led['post_id']}: re-price the whole video "
                   f"(pipeline.py budget ...) and close step 9 before the first video call (STANDARDS 10)")
    if led.get("family") == "song" and info["kind"] in ("image", "video") and not gate_ok(led["run_gates"].get("G-HUMAN-SONG")):
        why.append(f"song {led['post_id']}: the owner listens to the song master before any picture (G-HUMAN-SONG)")
    if info["kind"] == "test":
        if not gate_ok(a["gates"].get("G-HUMAN-TEST")):
            why.append(f"test asset {aref(a)} needs G-HUMAN-TEST from the owner, with the reason")
        if generated_before(led, a):
            why.append(f"{aref(a)} already ran: a test is one call")
        return (not why), why, led, a
    if want != info["kind"]:
        why.append(f"{aref(a)} is a {a['type']} but the call makes {kind}")
    if generated_before(led, a):
        why.append(f"{aref(a)} was already generated: a retake is a new version (pipeline.py asset {led['slug']} "
                   f"{led['post_id']} {a['asset_id']} --type {a['type']} ...), so attempts are counted")
    maxa = pol["max_video_attempts"] if info["kind"] == "video" else pol["max_image_attempts"]
    if info["kind"] in ("image", "video") and attempts(led, a["asset_id"]) >= maxa \
            and not _gate_any_version(led, a, "G-HUMAN-ESCALATE"):
        why.append(f"{a['asset_id']} already used {maxa} attempts: simplify the shot or escalate (G-HUMAN-ESCALATE)")
    why += _model_checks(req, a, led)

    if info["kind"] == "audio":
        if not gate_ok(led["run_gates"].get("G-SCRIPT")) and led["family"] != "library":
            why.append(f"no released script for {led['post_id']} (G-SCRIPT, 85+): words before sound")
        if req.get("service") != "atlas":
            return (not why), why, led, a
        # Atlas audio can take reference audio (a voice clone): the spec, prompt-gate and reference checks below run too

    for s in a["shots"]:
        ok, w = spec_current_ok(led, s)
        if not ok:
            why.append(w)
    pg = info.get("prompt_gate")
    if pg and kind != "nodes" and not _gate_any_version(led, a, pg, prompt_sha256=prompt_sha):
        why.append(f"no {pg} PASS for this exact prompt on {a['asset_id']} (Prompt Reviewer, fresh agent)")
    call_m = req.get("medias") or []
    reg_m = a["medias"]
    if kind != "nodes" and (len(call_m) != len(reg_m) or not all(
            c["value"] == r["value"] and _role_match(r["role"], c["role"]) for c, r in zip(call_m, reg_m))):
        why.append(f"references differ from the reviewed reference map: registered {[m['value'] for m in reg_m]}, "
                   f"call {[m['value'] for m in call_m]} (same files, same order, same roles: P2; a registered "
                   f"{EDIT_SOURCE} goes in the call as {' or '.join(IMAGE_ROLES)})")
    n_img = sum(1 for m in call_m if m["role"] in IMAGE_ROLES or m["role"] == EDIT_SOURCE)
    refs = []
    for i, m in enumerate(call_m):
        reg_role = reg_m[i]["role"] if i < len(reg_m) and reg_m[i]["value"] == m["value"] else m["role"]
        rl, ra = find_by_id(led["slug"], m["value"])
        if reg_role == EDIT_SOURCE:
            if not ra:
                why.append(f"{EDIT_SOURCE} {m['value']} is not registered on a version of {a['asset_id']} "
                           f"(pipeline.py media ... {a['asset_id']}@v<n> --id {m['value']})")
            elif ra["asset_id"] != a["asset_id"] or rl["post_id"] != led["post_id"] or ra["version"] >= a["version"]:
                why.append(f"{EDIT_SOURCE} {m['value']} is {aref(ra)}: an edit pass edits a previous version of the same "
                           f"asset ({a['asset_id']} below v{a['version']}) in this run, nothing else")
            elif info["kind"] != "image":
                why.append(f"{EDIT_SOURCE} is for image edit passes; {aref(a)} is a {a['type']}")
            elif n_img != 1:
                why.append(f"an edit pass takes {aref(ra)} as the single image reference ({n_img} image references in "
                           "the call): VISUAL-QA 5.5 route 1")
            continue
        if not ra:
            why.append(f"reference {m['value']} ({m['role']}) is not a registered asset with a passed review "
                       f"(pipeline.py media ... --id {m['value']}) {EDIT_PASS_HINT}")
            continue
        refs.append((m, rl, ra))
        ri = type_info(ra["type"])
        g = ri.get("visual_gate") or ri.get("audio_gate")
        if g and not gate_ok(ra["gates"].get(g)):
            why.append(f"reference {aref(ra)} has no {g} PASS"
                       + (f" {EDIT_PASS_HINT}" if ra["asset_id"] == a["asset_id"] else ""))
        if ri.get("look") and not (gate_ok(rl["run_gates"].get("G-HUMAN-LOOK")) or client_gate_ok(rl, "G-HUMAN-LOOK")):
            why.append(f"reference {aref(ra)} is from a look bible the owner hasn't approved (G-HUMAN-LOOK)")
    if info["kind"] == "video":
        talking = any("audio" in (m["role"] or "") for m in call_m)
        multi = len(a["shots"]) > 1
        imgs = [(m, rl, ra) for m, rl, ra in refs if m["role"] in ("image_references", "image")]
        if talking or multi:
            if not imgs or imgs[0][2]["type"] != "storyboard" or call_m[0]["role"] not in ("image_references", "image"):
                why.append("talking or multi-shot clip without its storyboard as image 1 (VISUAL-QA 6, FL-07)")
            else:
                m, rl, sb = imgs[0]
                cont = latest(rl["run_gates"].get("G-CONTINUITY"))
                if not cont or cont["status"] not in OK_STATES or aref(sb) not in (cont.get("covers") or []):
                    why.append(f"storyboard {aref(sb)} is not covered by a G-CONTINUITY PASS")
                if sb.get("hook"):
                    hb = latest(rl["run_gates"].get("G-HUMAN-HOOKBOARD"))
                    if not hb or hb["status"] not in OK_STATES or aref(sb) not in (hb.get("covers") or []):
                        why.append(f"hook storyboard {aref(sb)} waits for the owner (G-HUMAN-HOOKBOARD)")
        for m, rl, ra in refs:
            if "audio" in (m["role"] or "") and type_info(ra["type"])["kind"] != "audio":
                why.append(f"{aref(ra)} given as audio is a {ra['type']}")
    return (not why), why, led, a


def check_call(tool_name: str, tool_input: dict) -> tuple[bool, list[str]]:
    spec = STANDARDS["gated_tools"].get(tool_name)
    if not spec:
        return True, ["not a gated tool"]
    if spec["kind"] == "other":
        return _check_other(tool_name, tool_input)
    reqs = extract_requests(tool_name, tool_input or {}, spec)
    if not reqs:
        return False, ["no requests in the call"]
    allowed, reasons, logs = True, [], []
    for i, r in enumerate(reqs):
        ok, why, led, a = _check_request(r)
        tag = f"request {i}: " if len(reqs) > 1 else ""
        if not ok:
            allowed = False
            reasons += [tag + w for w in why]
        logs.append((led, {"at": stamp(), "tool": tool_name, "asset": aref(a) if a else None, "dry": bool(r.get("dry")),
                           "analysis": bool(r.get("analysis")),
                           "sha": sha_text(r.get("prompt") or "")[:16] if r.get("prompt") else None, "why": why}))
    decision = "ALLOW" if allowed else "DENY"
    for led, e in logs:
        if e["dry"] and led is None:
            continue
        e["decision"] = decision
        with calls_log(led).open("a") as f:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    return allowed, reasons


def _check_other(tool_name: str, ti: dict) -> tuple[bool, list[str]]:
    for led in all_ledgers():
        for a in led["assets"]:
            if a["type"] == "test" and a.get("tool") == tool_name and gate_ok(a["gates"].get("G-HUMAN-TEST")) \
                    and not generated_before(led, a):
                b = latest(led["run_gates"].get("G-BUDGET"))
                if b and b["status"] in OK_STATES:
                    with calls_log(led).open("a") as f:
                        f.write(json.dumps({"at": stamp(), "tool": tool_name, "asset": aref(a), "decision": "ALLOW",
                                            "dry": False}) + "\n")
                    return True, []
    return False, [f"{tool_name} makes content outside the production pipeline. If the owner asked for it, register a "
                   f"test asset (pipeline.py asset <slug> <TEST-run> <ID> --type test --tool {tool_name}), record "
                   "G-HUMAN-TEST with the owner's words, and G-BUDGET"]


# ---- CLI ---------------------------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("--format", required=True); p.add_argument("--card")
    p = sub.add_parser("status"); p.add_argument("slug"); p.add_argument("post_id")
    p = sub.add_parser("step"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("n", type=int)
    p.add_argument("--status", required=True); p.add_argument("--note", default="")
    p = sub.add_parser("spec-check"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("shots", nargs="*")
    p = sub.add_parser("asset"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("asset_id")
    p.add_argument("--type", required=True); p.add_argument("--shots", default=""); p.add_argument("--depends", default="")
    p.add_argument("--hero", action="store_true", default=None); p.add_argument("--hook", action="store_true"); p.add_argument("--tool")
    p = sub.add_parser("prompt"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("asset")
    p.add_argument("--file", required=True); p.add_argument("--media", nargs="*")
    p = sub.add_parser("media"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("asset")
    p.add_argument("--id", nargs="*", dest="ids"); p.add_argument("--file", nargs="*", dest="files")
    p = sub.add_parser("record"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("report")
    p = sub.add_parser("gate"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("gate")
    p.add_argument("--status", required=True); p.add_argument("--by", required=True); p.add_argument("--asset")
    p.add_argument("--note"); p.add_argument("--score", type=float); p.add_argument("--data"); p.add_argument("--covers", default="")
    p = sub.add_parser("budget"); p.add_argument("slug"); p.add_argument("post_id")
    p.add_argument("--planned", type=float, required=True); p.add_argument("--balance", type=float, required=True); p.add_argument("--el", type=float, default=0)
    p = sub.add_parser("ask"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("checkpoint")
    p.add_argument("--note", required=True); p.add_argument("--asset"); p.add_argument("--files", default="")
    p = sub.add_parser("approve"); p.add_argument("slug"); p.add_argument("post_id"); p.add_argument("checkpoint")
    p.add_argument("--by", required=True); p.add_argument("--asset"); p.add_argument("--note", default="approved"); p.add_argument("--reject", action="store_true")
    p = sub.add_parser("queue"); p.add_argument("--slug"); p.add_argument("--write", action="store_true")
    p = sub.add_parser("check-call"); p.add_argument("tool_name"); p.add_argument("input")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "init":
            led = init_run(a.slug, a.post_id, a.format, a.card)
            print(f"run {a.slug}/{a.post_id} ({led['family']}) at {run_dir(a.slug, a.post_id).relative_to(ROOT)}")
        elif a.cmd == "status":
            print(status_report(a.slug, a.post_id))
        elif a.cmd == "step":
            st = close_step(a.slug, a.post_id, a.n, a.status, a.note)
            print(f"step {a.n}: {st['status']}")
        elif a.cmd == "spec-check":
            _, res = spec_check(a.slug, a.post_id, a.shots or None)
            bad = 0
            for sid, issues in res.items():
                errs = [i for i in issues if i["level"] == "error"]
                bad += bool(errs)
                print(f"{sid}: {'FAIL' if errs else 'PASS'}")
                for i in issues:
                    print(f"  {i['level']:<5} {i['code']}: {i['msg']}")
            if not res:
                print("no Shot Specs in shots/")
                return 1
            return 1 if bad else 0
        elif a.cmd == "asset":
            x = new_asset(a.slug, a.post_id, a.asset_id, a.type, [s for s in a.shots.split(",") if s],
                          [d for d in a.depends.split(",") if d], a.hero, a.hook, a.tool)
            print(f"{aref(x)} ({x['type']}{', hero' if x['hero'] else ''})")
        elif a.cmd == "prompt":
            text = Path(a.file).read_text()
            x = set_prompt(a.slug, a.post_id, a.asset, text, parse_media(a.media))
            print(f"{aref(x)} prompt sha256 {x['prompt_sha256']} ({len(x['medias'])} references) -> {x['prompt_file']}")
        elif a.cmd == "media":
            x = add_media(a.slug, a.post_id, a.asset, a.ids, a.files)
            print(f"{aref(x)} ids {x['ids']} files {x['files']}")
        elif a.cmd == "record":
            rp = Path(a.report)
            rep = json.loads(rp.read_text())
            try:
                rep["_file"] = str(rp.resolve().relative_to(run_dir(a.slug, a.post_id).resolve()))
            except ValueError:
                rep["_file"] = str(rp)
            st, notes = record_report(a.slug, a.post_id, rep)
            print(f"{rep.get('gate')} {rep.get('asset_id') or rep.get('shot_id') or ''}: {st}")
            for n in notes:
                print(f"  {n}")
            return 0 if st == PASS else 1
        elif a.cmd == "gate":
            rec = record_gate(a.slug, a.post_id, a.gate, a.status, a.by, a.asset, a.note, a.score,
                              json.loads(a.data) if a.data else None, [c for c in a.covers.split(",") if c] or None)
            print(f"{a.gate}: {rec['status']} by {rec['by']}")
        elif a.cmd == "budget":
            r = budget(a.slug, a.post_id, a.planned, a.balance, a.el)
            cap = f"${r['cap']:.2f}" if r["cap"] is not None else "no cap set"
            print(f"G-BUDGET {r['status']}: planned ${r['planned']:.2f} (+25% = ${r['with_buffer']:.2f}), balance "
                  f"${r['balance']:.2f}, month ${r['month_spent']:.2f} of {cap}")
            for n in r["notes"]:
                print(f"  {n}")
            return 0 if r["status"] == PASS else 1
        elif a.cmd == "ask":
            led = load_ledger(a.slug, a.post_id)
            q = _queue_add(led, a.checkpoint, a.note, a.asset, [f for f in a.files.split(",") if f])
            save_ledger(led)
            print(f"queued {q['id']}")
        elif a.cmd == "approve":
            covers = [a.asset] if a.asset and a.checkpoint == "G-HUMAN-HOOKBOARD" else None
            asset = a.asset if a.checkpoint in ("G-HUMAN-ESCALATE", "G-HUMAN-TEST", "G-EXCEPTION", "G-FALLBACK") else None
            if covers:
                led = load_ledger(a.slug, a.post_id)
                covers = [aref(get_asset(led, c)) for c in covers]
            rec = record_gate(a.slug, a.post_id, a.checkpoint, FAIL if a.reject else PASS, a.by, asset, a.note,
                              covers=covers)
            print(f"{a.checkpoint}: {rec['status']} by {rec['by']}")
        elif a.cmd == "queue":
            text, n = queue_report(a.slug)
            print(text)
            if a.write:
                p = OUT / "queue" / f"{now().date().isoformat()}.md"
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(text)
                print(f"wrote {p.relative_to(ROOT)}")
        elif a.cmd == "check-call":
            raw = sys.stdin.read() if a.input == "-" else Path(a.input).read_text()
            ok, why = check_call(a.tool_name, json.loads(raw))
            print("ALLOW" if ok else "DENY")
            for w in why:
                print(f"  {w}")
            return 0 if ok else 1
    except PipelineError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
