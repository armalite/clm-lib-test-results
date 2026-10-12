# Incident board: updates in round 07

- Thread B root cause revised: an expired TLS certificate on a dependency (CERT_EXPIRED); this supersedes the earlier suspicion of DB_POOL_EXHAUSTED.
- Thread D opened: an upstream provider rejecting requests with 429 alerts (UPSTREAM_RATE_LIMIT) on search-api. Status: ongoing.
