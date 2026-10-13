# Stage 2 of 2 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; every other earlier rule, obligation and exception stays in force.

## Changes

- [CHANGED] Format (replaces the whole CSV format rule from stage 1): return JSON text (json.dumps) of an object whose key "records" is a list with one object per exported record, in ascending id order, each with exactly the keys "id" (int), "title", "owner" and "amount" (str; amount exactly as given in the record). The hidden tests parse the JSON and compare values, not spacing or key order. Which records are exported does not change.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
