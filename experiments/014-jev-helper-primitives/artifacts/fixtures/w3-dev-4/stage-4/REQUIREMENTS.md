# Stage 4 of 7: change notice

This notice lists decisions taken since the previous stage. An item does not say which earlier item it affects. A change wins over anything earlier that it conflicts with; every earlier requirement, obligation and exception, and every part of one, that it does not change stays in force.

## Changes

- [S4.1] Confidential records may now also be exported when user['role'] is 'admin' and params.get('purpose') == 'regulator'.
- [S4.2] Users whose role is neither 'admin' nor 'viewer' may now also export the records they own (record 'owner' equal to user['name']), even outside their projects.

## Notes

- [S4.3] Decision record: the move to JSON was made for the new reporting API.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
