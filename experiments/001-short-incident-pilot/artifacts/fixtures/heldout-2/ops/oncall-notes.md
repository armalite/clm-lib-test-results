# On-call notes - payments-api incident 2031-06-15

Informal running notes. Not reviewed; may be out of date.

- 07:51 pricing-core timeout is 2500ms per config/payments-api.yaml; upstream p99 is ~1.1s so timeouts are not a risk.
- 08:25 front-proxy reporting 503s from payments-api. Checking db pool.
- 08:33 db pool fine. Rate-limit headroom on pricing-core also fine.
