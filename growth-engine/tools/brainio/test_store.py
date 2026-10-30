"""Tests for brainio/store.py and validate.py."""
from brainio import store, validate
from brainio.testbase import BrainCase


class Store(BrainCase):
    def test_template_passes_the_schema(self):
        self.assertEqual(validate.errors(store.load(self.slug, self.root)), [])

    def test_save_round_trips_and_leaves_no_temp_file(self):
        b = store.load(self.slug, self.root)
        b["client"] = "Acme"
        store.save(self.slug, b, self.root)
        self.assertEqual(store.load(self.slug, self.root)["client"], "Acme")
        self.assertEqual([p.name for p in self.dir.glob("brain.json*")], ["brain.json"])

    def test_missing_brain_stops(self):
        with self.assertRaisesRegex(SystemExit, "NO_BRAIN"):
            store.load("nobody", self.root)

    def test_schema_errors_are_reported(self):
        b = store.load(self.slug, self.root)
        b["package"]["monthly_usd_cap"] = -1
        self.assertTrue(any("monthly_usd_cap" in e for e in validate.errors(b)))

    def test_field_sources_is_in_the_schema(self):
        b = store.load(self.slug, self.root)
        b["field_sources"] = {"offer.main_offer": "brand-guide.pdf p.2"}
        self.assertEqual(validate.errors(b), [])
        b["field_sources"] = {"offer.main_offer": 5}
        self.assertTrue(validate.errors(b))
