# Release notes: payments-api build 5.36.1-f33d

Previous build: 5.35.4. Defaults below override repository config files.

- metrics: new histogram for cache hit latency
- security: TLS session tickets rotated hourly
- docs: runbook links updated
- scheduler: cron jitter added to cleanup job
- feature flags: `ff-legacy-export` removed (was 0%)
- locale: currency formatting fixes
- batching: max batch size default 200 (unchanged)
- health: readiness probe timeout 2s (unchanged)
- clients: default `clients.risk-score.timeout_ms` lowered from 2500 to 800 (fail fast)
- cache: default `cache.ttl_s` unchanged (120)
- tracing: sampling rate default 1% (unchanged)
- db: default connection pool `db.pool.max_size` lowered from 60 to 14 to fit the shared-db connection quota
- retry: idempotent GETs retried once on connect errors
- deps: http client library upgraded to a patch release
- logging: structured request ids added to access logs
- config: `log.level` default remains info
- build: container base image refreshed
- deps: json serializer upgraded
- api: `/v1/status` returns build id
