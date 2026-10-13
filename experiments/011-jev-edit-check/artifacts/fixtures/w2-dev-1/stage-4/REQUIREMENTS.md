# Stage 4 of 5 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; every other earlier rule, obligation and exception stays in force.

## Changes

- [CHANGED] Permissions (partly replaces the stage-1 rule): a user whose role is not 'admin' now also receives the records they own (record 'owner' equal to user['name']), even outside their projects. The 'viewer' rule (PermissionError) and the 'admin' rule from stage 1 are unchanged.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
