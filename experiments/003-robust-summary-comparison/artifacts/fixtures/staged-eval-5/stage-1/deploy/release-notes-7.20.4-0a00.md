# Release notes: quotes-api build 7.20.4-0a00

Previous build: 7.19.0. Defaults below override repository config files.

- build: container base image refreshed
- config: `log.level` default remains info
- health: readiness probe timeout 2s (unchanged)
- clients: default `clients.rates-svc.timeout_ms` lowered from 2500 to 600 (fail fast)
- api: `/v1/status` returns build id
- scheduler: cron jitter added to cleanup job
- locale: currency formatting fixes
- metrics: new histogram for cache hit latency
- feature flags: `ff-legacy-export` removed (was 0%)
- security: TLS session tickets rotated hourly
- batching: max batch size default 200 (unchanged)
- db: default connection pool `db.pool.max_size` lowered from 48 to 12 to fit the shared-db connection quota
- logging: structured request ids added to access logs
- deps: json serializer upgraded
- deps: http client library upgraded to a patch release
- metrics: db pool gauges renamed to `db_pool_*`
- tracing: sampling rate default 1% (unchanged)
- cache: default `cache.ttl_s` unchanged (120)
