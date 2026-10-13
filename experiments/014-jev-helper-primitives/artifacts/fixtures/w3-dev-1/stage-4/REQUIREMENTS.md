# Stage 4 of 7: change notice

This notice lists decisions taken since the previous stage. An item does not say which earlier item it affects. A change wins over anything earlier that it conflicts with; every earlier requirement, obligation and exception, and every part of one, that it does not change stays in force.

## Changes

- [S4.1] include_archived is now honoured only when user['role'] is 'admin'; for every other role, archived records are never exported.
- [S4.2] Region values may now be written in upper or lower case, in records and in user['regions']; compare region values case-insensitively.
- [S4.3] Titles: in addition, replace every run of whitespace inside a title with a single space.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
