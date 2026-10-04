# On-call notes - billing-svc incident 2031-04-19

Informal running notes. Not reviewed; may be out of date.

- 08:30 front-proxy 5xx for billing-svc since build 6.24.0-4314 rolled out. Many pricing-core timeouts.
- 08:40 Suspect the pricing-core timeout default change in 6.24.0-4314; asking for a mitigation.
