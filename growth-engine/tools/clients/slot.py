"""A card's slot in the brand's timezone: the local "YYYY-MM-DD HH:MM" and the same moment as ISO 8601 with offset."""
import datetime as dt
from zoneinfo import ZoneInfo


def slot(local: str | None, tz: str) -> dict:
    out = {"local": local, "timezone": tz, "at": None}
    try:
        t = dt.datetime.strptime(local or "", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo(tz))
    except (ValueError, KeyError):
        return out
    out["at"] = t.isoformat()
    return out
