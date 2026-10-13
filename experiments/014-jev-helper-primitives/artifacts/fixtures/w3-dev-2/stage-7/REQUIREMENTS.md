# Stage 7 of 7: change notice

This notice lists decisions taken since the previous stage. An item does not say which earlier item it affects. A change wins over anything earlier that it conflicts with; every earlier requirement, obligation and exception, and every part of one, that it does not change stays in force.

## Changes

- [S7.1] Each exported JSON record now also has the key "project" (the record's project).
- [S7.2] The "exported_by" field is no longer required when user['role'] is 'admin'; admin exports omit it.

## Notes

- [S7.3] Decision record: the residency restriction was lifted after the regional data agreement was signed.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
