# Incident board: updates in round 06

- Thread A status: mitigated (errors reduced after the applied change; monitoring).
- Thread B root cause revised: an upstream provider rejecting requests with 429 (UPSTREAM_RATE_LIMIT); this supersedes the earlier suspicion of DB_POOL_EXHAUSTED.
- Follow-up OPEN ALERT_TUNING: tuning of noisy or late alerts.
