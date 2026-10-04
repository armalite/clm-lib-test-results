# Release notes: returns-svc build 6.33.4-cb27

Previous build: 6.32.5. Defaults below override repository config files.

- clients: default `clients.tax-engine.timeout_ms` lowered from 2500 to 750 (fail fast)
- cache: default `cache.ttl_s` unchanged (120)
- build: container base image refreshed
- metrics: db pool gauges renamed to `db_pool_*`
- tracing: sampling rate default 1% (unchanged)
- retry: idempotent GETs retried once on connect errors
- config: `log.level` default remains info
- deps: http client library upgraded to a patch release
- metrics: new histogram for cache hit latency
- logging: structured request ids added to access logs
- api: `/v1/status` returns build id
- locale: currency formatting fixes
- deps: json serializer upgraded
- docs: runbook links updated
- db: default connection pool `db.pool.max_size` lowered from 48 to 10 to fit the shared-db connection quota
- security: TLS session tickets rotated hourly
- feature flags: `ff-legacy-export` removed (was 0%)
