# Stage 3 of 5 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; every other earlier rule, obligation and exception stays in force.

## Changes

- [NEW] Date filter: params may contain 'since', a date string 'YYYY-MM-DD'. When it is present, only records whose 'created' date is on or after that date are exported.
- [CHANGED] Format (replaces the whole CSV format rule from stage 1): return JSON text (json.dumps) of an object whose key "records" is a list with one object per exported record, in ascending id order, each with exactly the keys "id" (int), "title", "owner" and "amount" (str; amount exactly as given in the record). The hidden tests parse the JSON and compare values, not spacing or key order. Which records are exported does not change.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
