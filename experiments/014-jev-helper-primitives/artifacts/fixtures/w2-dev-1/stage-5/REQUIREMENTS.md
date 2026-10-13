# Stage 5 of 5 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; every other earlier rule, obligation and exception stays in force.

## Changes

- [NEW] Record limit: params may contain 'max_records', an int of at least 1. Export only the first max_records records (in ascending id order) that remain after every other rule. The JSON object must also have the key "truncated": true if this limit left out at least one record, otherwise false (also when max_records is absent).

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
