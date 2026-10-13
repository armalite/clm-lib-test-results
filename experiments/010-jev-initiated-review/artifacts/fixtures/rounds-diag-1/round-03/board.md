# Incident board: updates in round 03

- Thread A opened: database connection pool exhausted confirmed as the cause (code DB_POOL_EXHAUSTED) in notify-worker; impact also on ledger-svc. Status: ongoing.
- Thread B opened: errors in inventory-svc. Suspected cause: a data volume running out of space (DISK_PRESSURE). Status: ongoing.
