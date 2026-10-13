# Stage 3 of 7: change notice

This notice lists decisions taken since the previous stage. An item does not say which earlier item it affects. A change wins over anything earlier that it conflicts with; every earlier requirement, obligation and exception, and every part of one, that it does not change stays in force.

## Changes

- [S3.1] Exports are now JSON text (json.dumps) of an object whose key "records" lists one object per exported record, in ascending id order, with exactly the keys "id" (int), "title", "owner" and "amount" (str, exactly as given). The hidden tests parse the JSON and compare values, not spacing or key order.
- [S3.2] The date filter now uses a record's 'updated' date when the record has one, and its 'created' date otherwise.

## Notes

- [S3.3] For information: the web interface will show record owners by display name; exports keep the stored 'owner' value.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
