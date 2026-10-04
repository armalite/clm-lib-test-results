# Release notes: payments-api build 6.25.3-646f

Previous build: 6.24.1. Defaults below override repository config files.

- clients: default `clients.tax-engine.timeout_ms` lowered from 2500 to 800 (fail fast)
- cache: default `cache.ttl_s` unchanged (120)
- build: container base image refreshed
- deps: json serializer upgraded
- tracing: sampling rate default 1% (unchanged)
- metrics: db pool gauges renamed to `db_pool_*`
- deps: http client library upgraded to a patch release
- metrics: new histogram for cache hit latency
- api: `/v1/status` returns build id
- feature flags: `ff-legacy-export` removed (was 0%)
- docs: runbook links updated
- retry: idempotent GETs retried once on connect errors
- db: default connection pool `db.pool.max_size` lowered from 48 to 10 to fit the shared-db connection quota
- batching: max batch size default 200 (unchanged)
- scheduler: cron jitter added to cleanup job
- locale: currency formatting fixes
- security: TLS session tickets rotated hourly
