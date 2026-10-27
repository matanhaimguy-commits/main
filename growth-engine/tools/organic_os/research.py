"""Outlier mining: the four checks per account (ORGANIC-OS 5.1).

The scraper gives likesCount -1 when an account hides its likes. Those likes are unknown, not zero: they are left
out of the account's medians, and a post that hides them can't pass the likes-in-proportion check automatically,
so it is never `trusted` but is flagged `partial_outlier` for a check by hand when its views and comments pass.
"""
from __future__ import annotations

import datetime as dt
import statistics


def _views(it: dict):
    v = it.get("videoViewCount") or it.get("videoPlayCount") or it.get("views")
    return float(v) if v else None


def _likes(it: dict):
    """The post's likes, or None when the account hides them (-1) or the scraper gave none."""
    v = it.get("likesCount")
    return None if v is None or v < 0 else v


def _recent(items: list[dict], days: int | None, now: dt.datetime) -> list[dict]:
    if not days:
        return items

    def recent(it):
        ts = it.get("timestamp")
        if not ts:
            return True
        return (now - dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))).days <= days
    return [it for it in items if recent(it)]


def _baseline(posts: list[dict]) -> dict:
    """The account's own rates, from the posts that show each number."""
    vid = [p for p in posts if _views(p)]
    tot_v = sum(_views(p) for p in vid)
    lpk = [_likes(p) / _views(p) * 1000 for p in vid if _likes(p) is not None]
    shown = [_likes(p) for p in posts if _likes(p) is not None]
    return {"med_views": statistics.median([_views(p) for p in vid]) if vid else None,
            "cpk": (sum(p.get("commentsCount") or 0 for p in vid) / tot_v * 1000) if tot_v else None,
            "med_lpk": statistics.median(lpk) if lpk else None,
            "med_likes": statistics.median(shown) if shown else 0}


def _view_checks(likes, comments: int, v: float, base: dict) -> dict:
    cpk = comments / v * 1000
    if likes is None:
        in_proportion = None
        eng = comments / v  # a floor: the hidden likes would only add to it
        eng_ok = True if eng >= 0.02 else None
    else:
        ratio = (likes / v * 1000) / base["med_lpk"] if base["med_lpk"] else None
        in_proportion = ratio is not None and 0.25 <= ratio <= 4
        eng = (likes + comments) / v
        eng_ok = eng >= 0.02
    checks = {"views_3x": v >= 3 * base["med_views"],
              "comments_above_rate": base["cpk"] is not None and cpk > base["cpk"],
              "likes_in_proportion": in_proportion, "engagement_2pct": eng_ok}
    trusted = all(c is True for c in checks.values())
    return {"basis": "views", "x_median": round(v / base["med_views"], 2), "comments_per_1k": round(cpk, 2),
            "account_comments_per_1k": round(base["cpk"], 2) if base["cpk"] is not None else None,
            "engagement": round(eng, 4), **checks, "trusted": trusted,
            "partial_outlier": likes is None and checks["views_3x"] and checks["comments_above_rate"]}


def _likes_only(likes, base: dict) -> dict:
    x = likes / base["med_likes"] if likes is not None and base["med_likes"] else None
    return {"basis": "likes_only", "x_median": round(x, 2) if x else None, "trusted": False,
            "partial_outlier": bool(x and x >= 3)}


def outliers(items: list[dict], days: int | None = 90, now: dt.datetime | None = None) -> list[dict]:
    items = _recent(items, days, now or dt.datetime.now(dt.timezone.utc))
    accounts: dict[str, list[dict]] = {}
    for it in items:
        if not it.get("isPinned"):
            accounts.setdefault(it.get("ownerUsername") or "?", []).append(it)
    rows = []
    for acct, posts in accounts.items():
        base = _baseline(posts)
        for p in posts:
            likes, comments, v = _likes(p), p.get("commentsCount") or 0, _views(p)
            row = {"account": acct, "url": p.get("url") or p.get("shortCode"), "type": p.get("type") or p.get("productType"),
                   "timestamp": p.get("timestamp"), "views": v, "likes": likes, "likes_hidden": likes is None,
                   "comments": comments}
            row.update(_view_checks(likes, comments, v, base) if v and base["med_views"] else _likes_only(likes, base))
            rows.append(row)
    return sorted(rows, key=lambda r: -(r.get("x_median") or 0))
