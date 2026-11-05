"""Scorecard: job metric against the account median, candidate/template flags, diagnosis (ORGANIC-OS 9)."""
from __future__ import annotations

import statistics

from .config import CONFIG


def _f(v):
    try:
        return float(v) if v not in (None, "") else None
    except ValueError:
        return None


def _div(a, b):
    return a / b if a is not None and b else None


def _median(vals):
    vals = [v for v in vals if v is not None]
    return statistics.median(vals) if vals else None


def score(rows: list[dict]) -> list[dict]:
    d = []
    for r in rows:
        reach, views = _f(r.get("reach")), _f(r.get("views"))
        x = {k: _f(r.get(k)) for k in ("likes", "comments", "saves", "sends", "profile_visits", "follows", "skip_rate", "avg_watch_s",
                                       "keyword_comments", "dms", "qualified_dms", "booked")}
        m = {"sends_per_reach": _div(x["sends"], reach), "saves_per_reach": _div(x["saves"], reach),
             "follows_per_1k_reach": (_div(x["follows"], reach) or 0) * 1000 if reach and x["follows"] is not None else None,
             "profile_per_reach": _div(x["profile_visits"], reach),
             "comments_per_1k_views": (_div(x["comments"], views) or 0) * 1000 if views and x["comments"] is not None else None,
             "engagement": _div((x["likes"] or 0) + (x["comments"] or 0), views) if views else None,
             "qualified_dms": x["qualified_dms"] if x["qualified_dms"] is not None else x["dms"]}
        d.append({"row": r, "x": x, "m": m, "reach": reach, "views": views})
    med = {k: _median([e["m"][k] for e in d]) for k in d[0]["m"]} if d else {}
    med.update({"reach": _median([e["reach"] for e in d]), "views": _median([e["views"] for e in d]),
                "skip_rate": _median([e["x"]["skip_rate"] for e in d]), "avg_watch_s": _median([e["x"]["avg_watch_s"] for e in d])})
    job_med = {}
    for job, cfg in CONFIG["jobs"].items():
        job_med[job] = _median([e["m"].get(cfg["metric"]) for e in d if e["row"].get("job") == job])
    out = []
    for e in d:
        r, m, x = e["row"], e["m"], e["x"]
        job = r.get("job") or "reach"
        metric = CONFIG["jobs"][job]["metric"]
        val, base = m.get(metric), job_med.get(job)
        ratio = (val / base) if val is not None and base else None
        checks = {
            "views_3x": bool(e["views"] and med["views"] and e["views"] >= 3 * med["views"]),
            "comments_above_rate": bool(m["comments_per_1k_views"] is not None and med["comments_per_1k_views"] is not None and m["comments_per_1k_views"] > med["comments_per_1k_views"]),
            "saves_sends_good": bool((m["saves_per_reach"] or 0) >= (med["saves_per_reach"] or 0) and (m["sends_per_reach"] or 0) >= (med["sends_per_reach"] or 0)),
            "engagement_2pct": bool(m["engagement"] is not None and m["engagement"] >= 0.02),
        }
        booked = (x["booked"] or 0) > 0
        flag = "template" if booked or (ratio and ratio >= CONFIG["templates"]["template_x"] and all(checks.values())) \
            else "candidate" if ratio and ratio >= CONFIG["templates"]["candidate_x"] else ""
        out.append({"post_id": r.get("post_id"), "job": job, "metric": metric, "value": val, "job_median": base,
                    "x_median": round(ratio, 2) if ratio else None, "flag": flag, "diagnosis": diagnose(e, med, r)})
    return out


def diagnose(e: dict, med: dict, r: dict) -> str:
    """The first step of the 9.4 ladder that the numbers point at, or '' when nothing stands out."""
    m, x = e["m"], e["x"]
    low = lambda v, base, f=0.7: v is not None and base is not None and v < base * f
    if low(e["reach"], med.get("reach")) and x["skip_rate"] is not None and med.get("skip_rate") is not None and x["skip_rate"] > med["skip_rate"] * 1.15:
        return "low reach, high skip rate: the hook or first frame failed; rewrite hooks, test with trial reels"
    if x["avg_watch_s"] is not None and med.get("avg_watch_s") and x["avg_watch_s"] >= med["avg_watch_s"] and \
            low((m["sends_per_reach"] or 0) + (m["saves_per_reach"] or 0), (med.get("sends_per_reach") or 0) + (med.get("saves_per_reach") or 0)):
        return "good hold, low sends/saves: value not unique or not usable; narrow to level 4, add a usable step"
    if e["views"] and med.get("views") and e["views"] >= med["views"] and low(m["profile_per_reach"], med.get("profile_per_reach"), 0.5):
        return "views but few profile visits: angle off-target; back to the demand map"
    if m["profile_per_reach"] and med.get("profile_per_reach") and m["profile_per_reach"] >= med["profile_per_reach"] and \
            x["follows"] is not None and x["profile_visits"] and low(x["follows"] / x["profile_visits"], 0.1, 1):
        return "profile visits but few follows: profile or series promise weak; fix bio, pinned posts, series"
    if (x["follows"] or 0) > 0 and r.get("cta_keyword") and x["dms"] == 0:
        return "follows but no DMs: CTA or lead magnet weak"
    if (x["dms"] or 0) > 0 and x["qualified_dms"] is not None and x["qualified_dms"] / x["dms"] < 0.3:
        return "DMs but few qualified: wrong viewer; tighten avatar and pillars, 'who it is not for' posts"
    if (x["qualified_dms"] or 0) > 0 and x["booked"] == 0:
        return "qualified DMs but no bookings: an offer or sales problem, not content"
    return ""
