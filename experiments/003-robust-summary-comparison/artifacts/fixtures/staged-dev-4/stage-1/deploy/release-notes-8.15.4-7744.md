# Release notes: profile-svc build 8.15.4-7744

Previous build: 8.14.8. Defaults below override repository config files.

- batching: max batch size default 200 (unchanged)
- build: container base image refreshed
- config: `log.level` default remains info
- scheduler: cron jitter added to cleanup job
- retry: idempotent GETs retried once on connect errors
- logging: structured request ids added to access logs
- clients: default `clients.ledger-api.timeout_ms` lowered from 2500 to 600 (fail fast)
- api: `/v1/status` returns build id
- security: TLS session tickets rotated hourly
- deps: json serializer upgraded
- metrics: new histogram for cache hit latency
- deps: http client library upgraded to a patch release
- db: default connection pool `db.pool.max_size` lowered from 48 to 14 to fit the shared-db connection quota
- tracing: sampling rate default 1% (unchanged)
- feature flags: `ff-legacy-export` removed (was 0%)
