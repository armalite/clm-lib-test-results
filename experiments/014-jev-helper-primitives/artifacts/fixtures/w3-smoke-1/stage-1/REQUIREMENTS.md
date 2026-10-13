# Stage 1 of 5: initial requirements

## Package and API

Implement `exporter.export_records(records, user, params) -> str` in the package
/task/workspace/exporter/ (a starting skeleton is provided). Standard library only.

- `records`: a list of dicts with the keys "id" (int, unique in the list), "title" (str),
  "owner" (str), "project" (str), "status" ("active" or "archived"), "amount" (a decimal string
  such as "12.50"; keep it exactly as given), "confidential" (bool), "created" (a date string
  "YYYY-MM-DD") and "region" (str). A record may also have "updated" (a date string). Do not
  modify the input.
- `user`: a dict with "name" (str), "role" (str), "projects" (list of str) and "regions" (list
  of str).
- `params`: a dict of export options; it may be empty. Rules introduce the options; ignore keys
  that no rule in force mentions.
- Base behaviour, unless a rule says otherwise: every record is exported, in ascending id
  order, with field values exactly as given, in the format that the format rule specifies.

## Requirements

- [S1.1] Format: return CSV text. The first row is the header id,title,owner,amount; then one row per exported record, in ascending id order, with those four fields. Produce it with Python's csv.writer (default dialect) and lineterminator='\n'. With no exported records, return the header row alone (ending in '\n').
- [S1.2] Scope: a user whose role is 'admin' may export records of any project. Any other role exports only records whose 'project' is in user['projects']; other records are left out without an error.
- [S1.3] Confidential records: a record whose 'confidential' is True is never exported, with one exception: it is exported when user['role'] is 'admin' and params.get('purpose') == 'audit'. Every other rule still applies to it.

## Notes

- [S1.4] Decision record: CSV was chosen for the first release because the finance team imports exports into spreadsheets.

Visible tests for the rules introduced or changed in this stage only: /task/fixtures/current-tests/test_stage.py (replaced at each stage). Earlier rules still apply and are checked by the hidden evaluation.
