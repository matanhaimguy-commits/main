"""Tests for say_forms.py: the form lines."""
import unittest

import testbase  # noqa: F401
from page_facts.say_forms import section


class SayForms(unittest.TestCase):
    def test_a_form_line(self):
        form = {"action": "", "method": "POST", "where": "footer", "fields_to_fill": 1, "asks_email": True, "asks_phone": False,
                "fields": [{"name": "", "type": "email", "required": True}]}
        self.assertEqual(section({"mode": "static", "forms": [form]})[1],
                         "- Form 1 (footer): POST to this same page (no action set); 1 field to fill: (no name) (email). "
                         "Asks for email: yes; phone: no.")

    def test_no_forms(self):
        self.assertEqual(section({"mode": "rendered", "forms": []}), ["## Forms", "- No <form> in the rendered page."])


if __name__ == "__main__":
    unittest.main()
