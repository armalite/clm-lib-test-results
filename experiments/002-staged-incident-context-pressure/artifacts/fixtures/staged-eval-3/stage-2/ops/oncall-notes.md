# On-call notes - returns-svc incident 2031-04-19

Informal running notes. Not reviewed; may be out of date.

- 09:54 tax-engine timeouts stopped after the mitigation, but edge-gw still shows 503s for returns-svc.
- 10:04 New errors look like db pool exhaustion, but config/returns-svc.yaml says max_size 48, so the pool should have plenty of room?
