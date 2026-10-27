"""The run's one-line summary and its "waiting on the owner" flag, from its steps and its human queue."""


def pending_queue(led: dict) -> list[dict]:
    return [q for q in led.get("queue", []) if q.get("status") == "PENDING"]


def summarize(steps: list[dict], led: dict) -> str:
    """Where the piece is, and which checkpoints wait on the owner."""
    if steps and all(s["status"] in ("done", "na") for s in steps):
        text = "All steps done."
    else:
        cur = next((s for s in steps if s["status"] in ("active", "blocked")), None)
        if not cur:
            text = f"A {led.get('family', '')} run: no production steps."
        elif cur["status"] == "blocked":
            text = f"Step {cur['n']} {cur['name']}: blocked. {cur.get('note', '')}".rstrip()
        else:
            text = f"Step {cur['n']} {cur['name']}."
    pend = pending_queue(led)
    if pend:
        text += " Waiting on you: " + ", ".join(sorted({q["checkpoint"] for q in pend})) + "."
    return text[:300]
