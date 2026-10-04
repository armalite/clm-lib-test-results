# On-call notes - catalog-api incident 2031-05-17

Informal running notes. Not reviewed; may be out of date.

- 09:53 ledger-api timeouts stopped after the mitigation, but edge-gw still shows 503s for catalog-api.
- 10:03 New errors look like db pool exhaustion, but config/catalog-api.yaml says max_size 60, so the pool should have plenty of room?
