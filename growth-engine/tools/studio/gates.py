"""A step's gates as the Studio page shows them: ledger records, computed gates, and per-asset gates."""
from .labels import GATE_STATES, STEP_OF_TYPE, gate_label


def gate_entry(gate: str, rec: dict, asset: str | None = None) -> dict:
    """One ledger gate record: status, score, by, at, note (and the asset version for a per-asset gate)."""
    e = {"gate": gate, "label": gate_label(gate),
         "status": rec.get("status") if rec.get("status") in GATE_STATES else "PENDING"}
    score = rec.get("score")
    if isinstance(score, (int, float)) and not isinstance(score, bool):
        e["score"] = score
    for k, cap in (("by", 120), ("at", 40), ("note", 4000)):
        if rec.get(k):
            e[k] = str(rec[k])[:cap]
    if asset:
        e["asset"] = asset
    return e


def computed_gate(P, led: dict, gate: str) -> dict:
    """A gate with no record on this run, as pipeline.py status works it out (specs, assets, the client's LIB run)."""
    try:
        ok, why = P.gate_state(led, gate)
    except P.PipelineError as e:
        ok, why = False, str(e)
    if gate == "G-ASSETS" and not led.get("assets"):
        ok, why = False, "No takes yet."  # pipeline.py passes it with nothing to check; the page shows it open
    e = {"gate": gate, "label": gate_label(gate), "status": "PASS" if ok else "PENDING"}
    if ok:
        mode = P.STANDARDS["human_checkpoints"].get(gate, {}).get("mode")
        e["note"] = ("Recorded for the client or the voice, not on this run." if mode in ("per_series", "per_voice")
                     else "Worked out by pipeline.py from the run's specs and assets.")
    elif why and not why.endswith("has no PASS"):
        e["note"] = why
    return e


def run_gates(P, led: dict, n: int) -> list[dict]:
    """Step n's own gates (pipeline.step_gates): every record in order, or the computed state when there is none."""
    out = []
    for g in P.step_gates(led, n):
        recs = led.get("run_gates", {}).get(g) or []
        out += [gate_entry(g, r) for r in recs] if recs else [computed_gate(P, led, g)]
    return out


def latest_assets(led: dict) -> list[dict]:
    latest = {}
    for a in led.get("assets", []):
        if a["asset_id"] not in latest or a["version"] > latest[a["asset_id"]]["version"]:
            latest[a["asset_id"]] = a
    return sorted(latest.values(), key=lambda a: a["asset_id"])


def asset_gates(P, led: dict, n: int) -> list[dict]:
    """The gates of the assets made at step n (latest version of each): their records, and the expected ones still open."""
    out = []
    for a in latest_assets(led):
        if STEP_OF_TYPE.get(a.get("type")) != n:
            continue
        ref = P.aref(a)
        info = P.STANDARDS["asset_types"].get(a["type"], {})
        expected = [info[k] for k in ("prompt_gate", "text_gate", "visual_gate", "audio_gate") if info.get(k)]
        recorded = a.get("gates", {})
        for g in list(recorded) + [g for g in expected if g not in recorded]:
            recs = recorded.get(g) or []
            out += [gate_entry(g, r, ref) for r in recs] or [{"gate": g, "label": gate_label(g), "status": "PENDING", "asset": ref}]
    return out
