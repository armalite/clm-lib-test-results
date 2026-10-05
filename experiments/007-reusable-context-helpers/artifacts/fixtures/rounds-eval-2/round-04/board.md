# Incident board: updates in round 04

- Thread A status: mitigated (errors reduced after the applied change; monitoring).
- Thread B opened: errors in ledger-svc. Suspected cause: cache miss storm after mass expiry (CACHE_STAMPEDE). Status: ongoing.
- Follow-up OPEN DATA_BACKFILL: backfill of records missed during the incident.
