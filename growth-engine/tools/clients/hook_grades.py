"""The piece's hook_grades: the hub wants a list of objects (`z.array(z.record(...))`, default [], never null).
A hook that carries a grade gives one entry; no grade gives an empty list."""


def of(hook: dict | None) -> list[dict]:
    grade = (hook or {}).get("grade")
    text = (hook or {}).get("text") or (hook or {}).get("spoken")
    if not grade or not text:
        return []
    return [{"hook": text, "grade": grade, "by": "hook-lab"}]
