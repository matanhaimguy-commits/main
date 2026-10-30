"""Summary section: each form, where it sends, the fields a visitor fills, and whether it asks for an email
or a phone number."""
from .wording import page_read, plural


def yes(flag: bool) -> str:
    return "yes" if flag else "no"


def line(n: int, form: dict) -> str:
    action = f'"{form["action"]}"' if form["action"] else "this same page (no action set)"
    fields = ", ".join(f"{f['name'] or '(no name)'} ({f['type']})" for f in form["fields"])
    return (f"- Form {n} ({form['where']}): {form['method']} to {action}; "
            f"{plural(form['fields_to_fill'], 'field')} to fill{': ' + fields if fields else ''}. "
            f"Asks for email: {yes(form['asks_email'])}; phone: {yes(form['asks_phone'])}.")


def section(facts: dict) -> list[str]:
    forms = facts["forms"]
    if not forms:
        return ["## Forms", f"- No <form> in {page_read(facts)}."]
    return ["## Forms"] + [line(i, f) for i, f in enumerate(forms, 1)]
