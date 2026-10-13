### [014 – Jev as a primitive inside Claude's own context helpers](experiments/014-jev-helper-primitives/README.md)

- **Question:** can Claude's own context-management code call Jev during an execution and use the answer to edit its working context, with no extra Claude turn (`jev-primitive/1`)?
- **Offline:** the mechanism was verified with a scripted fake Jev.
- **Prompted live demonstration** (one run on `w2-dev-1`, **instructed use, not adoption**):
  - **The helper:** Claude wrote and saved `ctxhelper.py`, which asks Jev whether each note is changed by a new stage and marks the notes scoring above 0.5 for review.
  - **Use and reuse:** it ran at 4 stage updates, with 4 real Jev calls, all inside running executions. Claude improved it once.
  - **The edits:** they followed the answers and were accepted, and each next request held exactly the accepted context plus the runtime's step entries.
  - **The outcome:** 35/35 hidden checks, 14 model calls (none extra), USD 0.184 (TypeSafe USD 0.0002), 105 s.
- **What it means:** the capability works end to end with real models. Jev's role was small, a review marker on one or two notes, and Claude wrote the substantive notes itself. **No benefit is claimed or measured.**
