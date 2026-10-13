# Stage 5 of 7: change notice

This notice lists decisions taken since the previous stage. An item does not say which earlier item it affects. A change wins over anything earlier that it conflicts with; every earlier requirement, obligation and exception, and every part of one, that it does not change stays in force.

## Changes

- [S5.1] Confidential records may now also be exported when user['role'] is 'admin' and params.get('purpose') == 'litigation'.
- [S5.2] Viewers no longer receive an error: a viewer now exports only the records they own (record 'owner' equal to user['name']), in any project; every other rule still applies to those records.

## Notes

- [S5.3] Decision record: the move to JSON was made for the new reporting API.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
