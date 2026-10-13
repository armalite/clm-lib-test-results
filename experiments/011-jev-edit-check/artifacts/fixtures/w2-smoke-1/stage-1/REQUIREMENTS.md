# Stage 1 of 2 requirements

## Package and API

Implement `exporter.export_records(records, user, params) -> str` in the package
/task/workspace/exporter/ (a starting skeleton is provided). Standard library only.

- `records`: a list of dicts with exactly these keys: "id" (int, unique in the list), "title"
  (str), "owner" (str), "project" (str), "status" ("active" or "archived"), "amount" (a
  decimal string such as "12.50"; keep it exactly as given), "confidential" (bool) and
  "created" (a date string "YYYY-MM-DD"). Do not modify the input.
- `user`: a dict with "name" (str), "role" (str) and "projects" (list of str).
- `params`: a dict of export options; it may be empty. Rules introduce the options; ignore keys
  that no rule in force mentions.
- Base behaviour, unless a rule says otherwise: every record is exported, in ascending id
  order, in the format that the format rule specifies.

## Rules introduced in stage 1

- [NEW] Format: return CSV text. The first row is the header `id,title,owner,amount`; then one row per exported record, in ascending id order, with those four fields. Produce it with Python's csv.writer (default dialect and quoting) and lineterminator='\n', writing id as an integer and amount exactly as given in the record. With no exported records the result is the header row alone (ending in '\n').
- [NEW] Permissions: if user['role'] is 'viewer', raise PermissionError (nothing is exported). A user whose role is 'admin' may export records of any project. Any other role exports only records whose 'project' is in user['projects']; other records are left out without an error.
- [NEW] Compliance obligation (no code change is needed while the format is CSV): if a later stage changes the export format from CSV, every export in the new format must also include a top-level field "exported_by" whose value is user['name']. This obligation stays in force unless a later stage withdraws it.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
