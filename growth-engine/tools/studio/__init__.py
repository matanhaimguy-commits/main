"""The studio side of the app's Studio page (hub.py studio-push, studio-ask, studio-answers, studio-synced).

One job per module: labels (gate and asset-step names), gates and ledger_steps (a run's ledger as the page's
steps), summary (the one-line summary), manifest (the files to show), and one module per command (push, ask,
answers, synced). hub.py owns the token and the HTTP calls and hands them in; nothing here prints the token.

Tests: python3 -m unittest discover -s growth-engine/tools/studio -t growth-engine/tools
"""
