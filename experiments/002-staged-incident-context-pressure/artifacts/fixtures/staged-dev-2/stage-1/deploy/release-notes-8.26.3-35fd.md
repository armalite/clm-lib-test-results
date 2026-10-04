# Release notes: catalog-api build 8.26.3-35fd

Previous build: 8.25.7. Defaults below override repository config files.

- security: TLS session tickets rotated hourly
- deps: http client library upgraded to a patch release
- cache: default `cache.ttl_s` unchanged (120)
- deps: json serializer upgraded
- feature flags: `ff-legacy-export` removed (was 0%)
- metrics: new histogram for cache hit latency
- clients: default `clients.ledger-api.timeout_ms` lowered from 2500 to 800 (fail fast)
- retry: idempotent GETs retried once on connect errors
- logging: structured request ids added to access logs
- scheduler: cron jitter added to cleanup job
- db: default connection pool `db.pool.max_size` lowered from 60 to 10 to fit the shared-db connection quota
- config: `log.level` default remains info
- tracing: sampling rate default 1% (unchanged)
- health: readiness probe timeout 2s (unchanged)
- locale: currency formatting fixes
- api: `/v1/status` returns build id
