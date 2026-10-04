# Release notes: billing-svc build 6.24.0-4314

Previous build: 6.23.4. Defaults below override repository config files.

- deps: json serializer upgraded
- config: `log.level` default remains info
- metrics: db pool gauges renamed to `db_pool_*`
- logging: structured request ids added to access logs
- clients: default `clients.pricing-core.timeout_ms` lowered from 2500 to 800 (fail fast)
- docs: runbook links updated
- tracing: sampling rate default 1% (unchanged)
- health: readiness probe timeout 2s (unchanged)
- locale: currency formatting fixes
- build: container base image refreshed
- scheduler: cron jitter added to cleanup job
- metrics: new histogram for cache hit latency
- cache: default `cache.ttl_s` unchanged (120)
- db: default connection pool `db.pool.max_size` lowered from 48 to 10 to fit the shared-db connection quota
- feature flags: `ff-legacy-export` removed (was 0%)
- deps: http client library upgraded to a patch release
- batching: max batch size default 200 (unchanged)
- api: `/v1/status` returns build id
