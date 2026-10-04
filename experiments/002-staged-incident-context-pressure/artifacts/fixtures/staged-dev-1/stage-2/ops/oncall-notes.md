# On-call notes - shipping-api incident 2031-03-16

Informal running notes. Not reviewed; may be out of date.

- 09:54 pricing-core timeouts stopped after the mitigation, but ingress-a still shows 503s for shipping-api.
- 10:04 New errors look like db pool exhaustion, but config/shipping-api.yaml says max_size 48, so the pool should have plenty of room?
