# On-call notes - shipping-api incident 2031-04-21

Informal running notes. Not reviewed; may be out of date.

- 08:12 Checked config/shipping-api.yaml: db pool max_size is 40; pool should not be a concern.
- 08:16 Cert warning for shipping-api.internal in logs - still weeks away, ignoring.
- 08:36 ingress-a showing 503s for shipping-api. Suspect rates-svc slowness?
- 08:46 Upstream dashboards look normal. Still investigating.
