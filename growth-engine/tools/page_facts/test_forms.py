"""Tests for forms.py: action, method, the fields a visitor fills, and email/phone asks."""
import unittest

from testbase import doc
from page_facts.forms import read
from page_facts.htmldoc import parse


class Forms(unittest.TestCase):
    def test_counts_only_fields_a_visitor_fills(self):
        quote, search = read(doc("pixel_gtm_form.html"))
        self.assertEqual((quote["action"], quote["method"], quote["where"]), ("/contact", "POST", "body"))
        self.assertEqual([(f["name"], f["type"]) for f in quote["fields"]],
                         [("full_name", "text"), ("email", "email"), ("phone", "tel"), ("service", "select"), ("message", "textarea")])
        self.assertEqual((quote["fields_to_fill"], quote["asks_email"], quote["asks_phone"]), (5, True, True))
        self.assertEqual([f["required"] for f in quote["fields"]], [True, True, False, False, False])
        self.assertEqual((search["method"], search["fields_to_fill"], search["asks_email"], search["asks_phone"]),
                         ("GET", 1, False, False))

    def test_email_and_phone_asks_from_names_and_placeholders(self):
        (f,) = read(parse('<form><input name="your-email"><input placeholder="Mobile number">'
                          '<input type="image" src="go.png"><input type="reset"><input type="button"></form>'))
        self.assertEqual((f["fields_to_fill"], f["asks_email"], f["asks_phone"], f["action"]), (2, True, True, ""))

    def test_fields_outside_a_form_are_not_a_form(self):
        self.assertEqual(read(parse('<input name="email" type="email"><button>Go</button>')), [])


if __name__ == "__main__":
    unittest.main()
