"""Tests for clients/registry.py."""
import json
import unittest

from clients import registry
from clients.testbase import BRAND, ClientsCase


class Registry(ClientsCase):
    def test_brand_by_slug(self):
        self.assertEqual(registry.brand("acme", self.registry)["hub_business"], "acme-app")

    def test_unknown_slug_and_bad_entries_stop(self):
        with self.assertRaises(registry.RegistryError):
            registry.brand("nope", self.registry)
        self.write(self.registry, json.dumps({"brands": [{**BRAND, "status": "sleeping"}]}))
        with self.assertRaises(registry.RegistryError):
            registry.brands(self.registry)
        self.write(self.registry, json.dumps({"brands": [{k: v for k, v in BRAND.items() if k != "timezone"}]}))
        with self.assertRaisesRegex(registry.RegistryError, "timezone"):
            registry.brands(self.registry)
        self.write(self.registry, json.dumps({"brands": [BRAND, BRAND]}))
        with self.assertRaisesRegex(registry.RegistryError, "twice"):
            registry.brands(self.registry)

    def test_the_repo_registry_is_valid(self):
        got = {b["slug"]: b for b in registry.brands()}
        self.assertEqual(got["straightscale-en"]["status"], "active")
        self.assertEqual(got["straightscale"]["status"], "paused")


if __name__ == "__main__":
    unittest.main()
