# On-call notes - payments-api incident 2031-03-06

Informal running notes. Not reviewed; may be out of date.

- 09:45 tax-engine timeouts stopped after the mitigation, but ingress-a still shows 503s for payments-api.
- 09:55 New errors look like db pool exhaustion, but config/payments-api.yaml says max_size 48, so the pool should have plenty of room?
