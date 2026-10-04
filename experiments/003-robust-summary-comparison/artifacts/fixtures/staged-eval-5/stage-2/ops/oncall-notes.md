# On-call notes - quotes-api incident 2031-05-15

Informal running notes. Not reviewed; may be out of date.

- 09:55 rates-svc timeouts stopped after the mitigation, but ingress-a still shows 503s for quotes-api.
- 10:05 New errors look like db pool exhaustion, but config/quotes-api.yaml says max_size 48, so the pool should have plenty of room?
