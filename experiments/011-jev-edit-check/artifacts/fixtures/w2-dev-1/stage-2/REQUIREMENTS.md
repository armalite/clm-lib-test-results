# Stage 2 of 5 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; every other earlier rule, obligation and exception stays in force.

## Changes

- [NEW] Confidential records: a record whose 'confidential' is True is never exported, with one exception: it is exported when user['role'] is 'admin' and params.get('purpose') == 'audit' (every other rule still applies to it).
- [NEW] Date filter: params may contain 'since', a date string 'YYYY-MM-DD'. When it is present, only records whose 'created' date is on or after that date are exported.
- [NEW] Compliance obligation (no code change is needed while the format is CSV): if a later stage changes the export format from CSV, every export in the new format must also include a top-level field "exported_by" whose value is user['name']. This obligation stays in force unless a later stage withdraws it.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
