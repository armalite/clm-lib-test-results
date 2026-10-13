# Stage 4 of 5 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; every other earlier rule, obligation and exception stays in force.

## Changes

- [CHANGED] Status (partly replaces the stage-2 rule): include_archived is now honoured only when user['role'] is 'admin'; for every other role, archived records are never exported. The rest of the stage-2 status rule is unchanged.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
