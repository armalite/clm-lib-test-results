# On-call notes - profile-svc incident 2031-06-06

Informal running notes. Not reviewed; may be out of date.

- 09:55 ledger-api timeouts stopped after the mitigation, but api-gateway still shows 503s for profile-svc.
- 10:05 New errors look like db pool exhaustion, but config/profile-svc.yaml says max_size 48, so the pool should have plenty of room?
