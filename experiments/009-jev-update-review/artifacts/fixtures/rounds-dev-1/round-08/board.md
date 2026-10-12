# Incident board: updates in round 08

- Thread A status: resolved (no recurrence for two hours).
- Thread B root cause revised: an upstream provider rejecting requests with 429 (UPSTREAM_RATE_LIMIT); this supersedes the earlier suspicion of CACHE_STAMPEDE.
- Thread C opened: request failures on some notify-worker pods; cause not yet identified. Status: ongoing.
