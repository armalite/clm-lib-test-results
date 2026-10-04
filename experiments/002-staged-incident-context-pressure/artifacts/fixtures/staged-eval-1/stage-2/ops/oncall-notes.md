# On-call notes - quotes-api incident 2031-05-22

Informal running notes. Not reviewed; may be out of date.

- 09:45 risk-score timeouts stopped after the mitigation, but api-gateway still shows 503s for quotes-api.
- 09:55 New errors look like db pool exhaustion, but config/quotes-api.yaml says max_size 60, so the pool should have plenty of room?
