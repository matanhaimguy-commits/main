"""Reads a page's HTML once into a plain record the other modules query. Nothing in it is executed.

Doc.elements: every start tag as {"tag", "attrs", "where", "form"} plus "text" for title, h1, a, button and
label. `where` is header, footer or body (best effort: inside <header>/<footer>, role=banner/contentinfo, or
id="header"/"footer"); `form` is the index of the enclosing <form>, or None.
Doc.scripts: each <script> as {"attrs", "body"}. Doc.text: the page's visible text (outside script, style,
noscript, template and title), whitespace collapsed. Comments are dropped, so commented-out code never counts."""
from dataclasses import dataclass, field
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
NOT_TEXT = {"script", "style", "noscript", "template", "title"}
CAPTURE = {"title", "h1", "a", "button", "label"}
REGION_ROLES = {"banner": "header", "contentinfo": "footer"}


@dataclass
class Doc:
    elements: list = field(default_factory=list)
    scripts: list = field(default_factory=list)
    text: str = ""

    def find(self, *tags: str) -> list[dict]:
        return [el for el in self.elements if el["tag"] in tags]


def region(tag: str, attrs: dict, inherited: str) -> str:
    if tag in ("header", "footer"):
        return tag
    by_role = REGION_ROLES.get(attrs.get("role", ""))
    if by_role:
        return by_role
    return attrs["id"] if attrs.get("id") in ("header", "footer") else inherited


class Reader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.doc, self.stack, self.parts, self.forms = Doc(), [], [], 0

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        top = self.stack[-1] if self.stack else {"where": "body", "form": None, "hidden": False}
        form = top["form"]
        if tag == "form":
            form, self.forms = self.forms, self.forms + 1
        el = {"tag": tag, "attrs": a, "where": region(tag, a, top["where"]), "form": form}
        if tag in CAPTURE:
            el["text"] = ""
        self.doc.elements.append(el)
        if tag == "script":
            self.doc.scripts.append({"attrs": a, "body": ""})
        if tag not in VOID:
            self.stack.append({"tag": tag, "where": el["where"], "form": form, "el": el,
                               "hidden": top["hidden"] or tag in NOT_TEXT})

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]["tag"] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.stack and self.stack[-1]["tag"] == "script":
            self.doc.scripts[-1]["body"] += data
            return
        for entry in self.stack:
            if "text" in entry["el"]:
                entry["el"]["text"] += data
        if not (self.stack and self.stack[-1]["hidden"]):
            self.parts.append(data)


def squash(text: str) -> str:
    return " ".join(text.split())


def parse(html: str) -> Doc:
    r = Reader()
    r.feed(html)
    r.close()
    for el in r.doc.elements:
        if "text" in el:
            el["text"] = squash(el["text"])
    r.doc.text = squash(" ".join(r.parts))
    return r.doc
