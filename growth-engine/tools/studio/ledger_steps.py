"""A run's ledger.json as the Studio page's steps 0-15."""
from .gates import asset_gates, run_gates


def step_note(st: dict, family: str) -> str:
    note = (st.get("note") or "").strip()
    if st.get("status") == "na" and note == "family":
        return f"Not part of a {family} piece."
    return note


def page_status(raw: str, current_found: bool) -> str:
    """Ledger todo/done/na/blocked to the page's done/na/active/blocked/pending: the first open step is the current one."""
    if raw in ("done", "na"):
        return raw
    if raw == "blocked":
        return "blocked"
    return "pending" if current_found else "active"


def build_steps(P, led: dict, extra: dict | None = None) -> list[dict]:
    """Every step of the run in order, with its status, note and gates (pipeline.py status's view).

    `extra` is the manifest's "steps": per step a note and gate records the ledger doesn't hold (loop history),
    shown before the ledger's records.
    """
    extra = extra or {}
    steps, current = [], False
    for s in P.STANDARDS["steps"]:
        n = s["n"]
        st = led.get("steps", {}).get(str(n))
        if st is None:
            continue
        status = page_status(st.get("status", "todo"), current)
        current = current or status in ("active", "blocked")
        x = extra.get(str(n)) or {}
        step = {"n": n, "name": s["name"], "status": status,
                "gates": [dict(g) for g in x.get("gates", [])] + run_gates(P, led, n) + asset_gates(P, led, n)}
        note = x.get("note") or step_note(st, led.get("family", ""))
        if note:
            step["note"] = note[:4000]
        if st.get("at"):
            step["at"] = st["at"]
        steps.append(step)
    return steps
