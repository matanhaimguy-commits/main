"""The twin route in the generation gate (D-T4, Twin reel machine plan T1): create_speech and create_video_from_avatar,
the only HeyGen tools that may generate. Finds the run and asset a call belongs to, applies heygen_rules.py, and logs
the call in the run's calls.jsonl. Takes the pipeline module as P, so this file never imports it.
Tests: growth-engine/tools/test_heygen_gate.py."""
from __future__ import annotations

import json

import yaml

import budget_heygen
import gate_budget
import heygen_rules


def rules(P) -> dict:
    return P.STANDARDS["models"]["heygen"]


def brain_host(P, slug: str):
    p = P.ROOT / "clients" / slug / "brain.json"
    return (json.loads(p.read_text()) if p.exists() else {}).get("host")


def card_problem(P, led: dict) -> str | None:
    """The run is for a card marked twin_host: only those may show the owner's twin (STANDARDS 7, D-T1)."""
    flag = rules(P)["card_flag"]
    p = P.ROOT / (led.get("card") or "")
    if not led.get("card") or not p.is_file():
        return f"run {led['post_id']} names no card file: the twin is only for cards marked {flag}"
    card = yaml.safe_load(p.read_text()) or {}
    if card.get(flag) is not True:
        return f"card {led['card']} is not marked {flag}: the twin hosts only those (D-T1)"
    return None


def run_problems(P, led: dict, a: dict, video: bool) -> list[str]:
    """What every twin call needs on its run: the card, a fresh budget priced in HeyGen credits, one call per version."""
    why = [w for w in (card_problem(P, led), gate_budget.fresh_problem(P, led)) if w]
    b = P.latest(led["run_gates"].get("G-BUDGET"))
    if b and b.get("status") == "PASS" and not budget_heygen.priced(b.get("data")):
        why.append(f"G-BUDGET for {led['post_id']} has no HeyGen credits planned: pipeline.py budget {led['slug']} "
                   f"{led['post_id']} --planned USD --balance USD --heygen CREDITS (D-T5: every call is logged in credits)")
    if P.generated_before(led, a):
        why.append(f"{P.aref(a)} was already generated: a retake is a new version (pipeline.py asset ...), so "
                   "attempts and credits are counted")
    st9 = led.get("steps", {}).get("9")
    if video and st9 and st9.get("status") not in ("done", "na"):
        why.append(f"step 9 (budget preflight) is not closed for {led['post_id']}: re-price the whole video and close "
                   "step 9 before the first video call (STANDARDS 10)")
    return why


def _own_asset(P, a: dict, rule: dict, tool: str) -> list[str]:
    if a["type"] not in rule["asset_types"] or a.get("tool") != tool:
        return [f"{P.aref(a)} is a {a['type']} for {a.get('tool')}: this call needs a {' or '.join(rule['asset_types'])} "
                f"asset registered with --tool {tool}"]
    return []


def speech(P, tool: str, ti: dict):
    rule = rules(P)["speech"]
    text = ti.get("text") if isinstance(ti.get("text"), str) else ""
    sha = P.sha_text(text)
    hits = [(led, a) for led in P.all_ledgers() for a in led["assets"]
            if a.get("prompt_sha256") == sha and a.get("tool") == tool]
    if not P.norm_prompt(text) or not hits:
        return [f"this speech text (sha256 {sha[:12]}) is not registered on a voice asset for {tool}: pipeline.py asset "
                f"<slug> <post> VO --type voice --tool {tool}, then pipeline.py prompt <slug> <post> VO --file "
                "<the released script>"], None, None
    led, a = max(hits, key=lambda h: (h[1]["created"], h[1]["version"]))
    host = brain_host(P, led["slug"])
    why = _own_asset(P, a, rule, tool)
    hp = heygen_rules.host_problem(host)
    why += [hp] if hp else heygen_rules.speech_checks(ti, host, rule)
    g = P.latest(led["run_gates"].get("G-SCRIPT"))
    if not g or g["status"] not in P.OK_STATES or (g.get("data") or {}).get("script_sha256") != sha:
        why.append(f"the text is not the released script of {led['post_id']}: its G-SCRIPT PASS (85+) must carry "
                   f"--data '{{\"script_sha256\": \"{sha}\"}}' for exactly this text")
    return why + run_problems(P, led, a, video=False), led, a


def video(P, tool: str, ti: dict):
    rule = rules(P)["avatar_video"]
    value = next((ti.get(k) for k in rule["audio_keys"] if isinstance(ti.get(k), str) and ti.get(k)), None)
    found = [(led, a) for led in P.all_ledgers() for a in led["assets"] if value and value in a.get("ids", [])]
    if not found:
        why, _ = heygen_rules.video_checks(ti, {"looks": []}, rule)
        return [f"audio {value!r} is not registered on a voice asset of a run (pipeline.py media <slug> <post> VO@v<n> "
                "--id <HeyGen asset id or audio URL>)"] + why, None, None
    led, voice = found[-1]
    host = brain_host(P, led["slug"])
    hp = heygen_rules.host_problem(host)
    why = [hp] if hp else heygen_rules.video_checks(ti, host, rule)[0]
    if P.type_info(voice["type"])["kind"] != "audio":
        why.append(f"{value} is {P.aref(voice)}, a {voice['type']}, not a voice")
    elif voice.get("tool") != rules(P)["speech"]["tool"]:
        why.append(f"voice {P.aref(voice)} was not made with {rules(P)['speech']['tool']}: the twin speaks only in "
                   "his own cloned voice (D-T2)")
    elif not P.gate_ok(voice["gates"].get(rule["audio_gate"])):
        why.append(f"voice {P.aref(voice)} has no {rule['audio_gate']} PASS (take check against the script)")
    clips = [a for a in led["assets"] if a.get("tool") == tool and a["type"] in rule["asset_types"]
             and [(m["value"], m["role"]) for m in a.get("medias") or []] == [(value, "audio")]]
    if not clips:
        return why + [f"no {' or '.join(rule['asset_types'])} asset in {led['post_id']} registered with --tool {tool} "
                      f"and this audio as its only reference (pipeline.py prompt ... --media {value}:audio)"], led, None
    a = max(clips, key=lambda x: (x["created"], x["version"]))
    why += _own_asset(P, a, rule, tool)
    maxa = P.STANDARDS["gate_policy"]["max_video_attempts"]
    if P.attempts(led, a["asset_id"]) >= maxa and not P._gate_any_version(led, a, "G-HUMAN-ESCALATE"):
        why.append(f"{a['asset_id']} already used {maxa} attempts: escalate (G-HUMAN-ESCALATE)")
    return why + run_problems(P, led, a, video=True), led, a


def check(P, tool: str, ti: dict, spec: dict, log: bool = True) -> tuple[bool, list[str]]:
    route = {"heygen_speech": speech, "heygen_avatar_video": video}.get(spec["kind"])
    why, led, a = route(P, tool, ti) if route else ([f"no twin route for kind {spec['kind']}"], None, None)
    if log:
        e = {"at": P.stamp(), "tool": tool, "asset": P.aref(a) if a else None, "dry": False, "service": "heygen_twin",
             "decision": "DENY" if why else "ALLOW", "why": why}
        with P.calls_log(led).open("a") as f:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    return (not why), why
