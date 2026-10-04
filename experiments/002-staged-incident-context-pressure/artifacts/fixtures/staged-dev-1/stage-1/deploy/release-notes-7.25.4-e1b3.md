# Release notes: shipping-api build 7.25.4-e1b3

Previous build: 7.24.0. Defaults below override repository config files.

- clients: default `clients.pricing-core.timeout_ms` lowered from 2500 to 750 (fail fast)
- security: TLS session tickets rotated hourly
- retry: idempotent GETs retried once on connect errors
- batching: max batch size default 200 (unchanged)
- metrics: db pool gauges renamed to `db_pool_*`
- logging: structured request ids added to access logs
- metrics: new histogram for cache hit latency
- deps: http client library upgraded to a patch release
- db: default connection pool `db.pool.max_size` lowered from 48 to 12 to fit the shared-db connection quota
- health: readiness probe timeout 2s (unchanged)
- api: `/v1/status` returns build id
- feature flags: `ff-legacy-export` removed (was 0%)
- deps: json serializer upgraded
- config: `log.level` default remains info
- build: container base image refreshed
- scheduler: cron jitter added to cleanup job
