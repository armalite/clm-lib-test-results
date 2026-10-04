# On-call notes - payments-api incident 2031-04-14

Informal running notes. Not reviewed; may be out of date.

- 09:49 risk-score timeouts stopped after the mitigation, but ingress-a still shows 503s for payments-api.
- 09:59 New errors look like db pool exhaustion, but config/payments-api.yaml says max_size 60, so the pool should have plenty of room?
