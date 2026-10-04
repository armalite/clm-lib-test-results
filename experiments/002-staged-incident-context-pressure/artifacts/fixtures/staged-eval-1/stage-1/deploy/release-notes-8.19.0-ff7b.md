# Release notes: quotes-api build 8.19.0-ff7b

Previous build: 8.18.6. Defaults below override repository config files.

- deps: http client library upgraded to a patch release
- scheduler: cron jitter added to cleanup job
- security: TLS session tickets rotated hourly
- metrics: db pool gauges renamed to `db_pool_*`
- clients: default `clients.risk-score.timeout_ms` lowered from 2500 to 800 (fail fast)
- cache: default `cache.ttl_s` unchanged (120)
- build: container base image refreshed
- tracing: sampling rate default 1% (unchanged)
- config: `log.level` default remains info
- metrics: new histogram for cache hit latency
- db: default connection pool `db.pool.max_size` lowered from 60 to 14 to fit the shared-db connection quota
- feature flags: `ff-legacy-export` removed (was 0%)
- locale: currency formatting fixes
- api: `/v1/status` returns build id
- logging: structured request ids added to access logs
- health: readiness probe timeout 2s (unchanged)
