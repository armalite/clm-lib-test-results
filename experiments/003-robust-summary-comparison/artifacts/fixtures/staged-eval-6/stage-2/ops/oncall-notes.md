# On-call notes - billing-svc incident 2031-04-19

Informal running notes. Not reviewed; may be out of date.

- 09:48 pricing-core timeouts stopped after the mitigation, but front-proxy still shows 503s for billing-svc.
- 09:58 New errors look like db pool exhaustion, but config/billing-svc.yaml says max_size 48, so the pool should have plenty of room?
