# Stage 2 of 5: further initial requirements

## Requirements

- [S2.1] Status: only records with status 'active' are exported, unless params.get('include_archived') is True; then records with status 'archived' are exported too.
- [S2.2] Compliance obligation (nothing to do while the format is CSV): if a later stage changes the export format from CSV, every export in the new format must include a top-level field "exported_by" equal to user['name']. It stays in force unless a later stage withdraws or changes it.
- [S2.3] Titles: export each record's title with leading and trailing whitespace removed.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
