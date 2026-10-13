# Stage 3 of 5: change notice

This notice lists decisions taken since the previous stage. An item does not say which earlier item it affects. A change wins over anything earlier that it conflicts with; every earlier requirement, obligation and exception, and every part of one, that it does not change stays in force.

## Changes

- [S3.1] Exports are now JSON text (json.dumps) of an object whose key "records" lists one object per exported record, in ascending id order, with exactly the keys "id" (int), "title", "owner" and "amount" (str, exactly as given). The hidden tests parse the JSON and compare values, not spacing or key order.
- [S3.2] Users whose role is neither 'admin' nor 'viewer' may now also export the records they own (record 'owner' equal to user['name']), even outside their projects.

## Notes

- [S3.3] For information: storage for archived projects moves to a cheaper tier next quarter. This does not change what exports contain.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
