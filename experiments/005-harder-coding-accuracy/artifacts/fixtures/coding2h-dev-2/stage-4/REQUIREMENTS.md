# Stage 4 of 8 requirements

Only the changes are listed. A CHANGED rule says which part of an earlier rule it replaces; everything else from earlier stages stays in force.

## Changes

- [NEW] Bulk and tier discounts do not stack: bulk lines are not tier-eligible. The tier-eligible amount is the sum of the line amounts of the lines that are not bulk lines.

Visible tests for all rules now in force: /task/fixtures/current-tests/test_invoice.py (this file is updated at each stage).
