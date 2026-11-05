"""Apify gate rules: only listed scrapers, only their real input keys, a spend cap per run, no personal-data add-ons.

The list is growth-engine/config/apify-actors.json; check(call, config) returns the reasons to refuse (none = allowed).
"""
import difflib


def find(actor: str, actors: dict) -> tuple[str, dict] | tuple[None, None]:
    name = actor.split(":")[0]
    for full, spec in actors.items():
        if name in (full, spec.get("id")):
            return full, spec
    return None, None


def key_reasons(inp: dict, spec: dict) -> list[str]:
    keys = spec.get("input_keys")
    if keys is None:
        return []
    out = []
    for k in inp:
        if k not in keys:
            near = difflib.get_close_matches(k, keys, n=1)
            out.append(f"input key '{k}' is not in the scraper's schema" + (f" (did you mean '{near[0]}'?)" if near else ""))
    return out


def spend_reasons(opts: dict, spec: dict) -> list[str]:
    cap = spec["max_charge_usd"]
    got = opts.get("maxTotalChargeUsd")
    if got is None:
        return [f"set callOptions.maxTotalChargeUsd (at most {cap}); this scraper bills per event, so maxItems does not cap it"]
    return [] if got <= cap else [f"callOptions.maxTotalChargeUsd {got} is over this scraper's cap of {cap}"]


def data_reasons(inp: dict, spec: dict) -> list[str]:
    out = [f"send {k}: {str(v).lower()} (personal data stays off)" for k, v in (spec.get("fixed") or {}).items() if inp.get(k) != v]
    out += [f"{k} must be off: it returns personal data" for k in spec.get("forbid") or [] if inp.get(k)]
    return out


def check(call: dict, config: dict) -> list[str]:
    full, spec = find(call.get("actor") or "", config["actors"])
    if not spec:
        allowed = ", ".join(config["actors"])
        return [f"'{call.get('actor')}' is not an allowed scraper ({allowed}); add one only with the owner's OK"]
    inp, opts = call.get("input") or {}, call.get("callOptions") or {}
    return key_reasons(inp, spec) + spend_reasons(opts, spec) + data_reasons(inp, spec)
