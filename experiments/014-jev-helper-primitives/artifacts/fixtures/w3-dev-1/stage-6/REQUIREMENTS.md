# Stage 6 of 7: change notice

This notice lists decisions taken since the previous stage. An item does not say which earlier item it affects. A change wins over anything earlier that it conflicts with; every earlier requirement, obligation and exception, and every part of one, that it does not change stays in force.

## Changes

- [S6.1] The "exported_by" field is no longer required when user['role'] is 'admin'; admin exports omit it.
- [S6.2] A max_records value above 25 is treated as 25.

## Notes

- [S6.3] For information: the web interface now shows 50 records per page. This does not change exports.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
