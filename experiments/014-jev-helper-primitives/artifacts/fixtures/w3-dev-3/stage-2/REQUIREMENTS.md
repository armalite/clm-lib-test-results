# Stage 2 of 7: further initial requirements

## Requirements

- [S2.1] Date filter: params may contain 'since', a date string 'YYYY-MM-DD'. When it is present, only records whose 'created' date is on or after that date are exported.
- [S2.2] Residency: a record whose 'region' is 'eu' is exported only when 'eu' is in user['regions']; this applies to admins too.
- [S2.3] Record limit: params may contain 'max_records', an int of at least 1. Export only the first max_records records, in ascending id order, that remain after every other rule.
- [S2.4] Compliance obligation (nothing to do while the format is CSV): if a later stage changes the export format from CSV, every export in the new format must include a top-level field "exported_by" equal to user['name']. It stays in force unless a later stage withdraws or changes it.
- [S2.5] Titles: export each record's title with leading and trailing whitespace removed.
- [S2.6] Audit-trail obligation (nothing to do today): if confidential records are ever exported for a purpose other than 'audit', every such export must include a top-level field "confidential_count" giving the number of confidential records it contains.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
