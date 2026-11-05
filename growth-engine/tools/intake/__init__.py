"""Onboarding stage O1 (growth-engine/ONBOARDING.md): bring a client's submitted intake into the repo.

hub.py intake-pull <slug> [--fixture file.json] [--dry-run] [--business B]. One job per module: questions (the question
set, growth-engine/onboarding/intake-questions.json), required (which required answers are missing), fetch (the hub
call), write (answers.json and files.json), cli (the command). hub.py owns the token and the HTTP call.

Tests: python3 -m unittest discover -s growth-engine/tools/intake -t growth-engine/tools
"""
