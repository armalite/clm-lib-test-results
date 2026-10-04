# On-call notes - shipping-api incident 2031-03-16

Informal running notes. Not reviewed; may be out of date.

- 08:28 ingress-a 5xx for shipping-api since build 7.25.4-e1b3 rolled out. Many pricing-core timeouts.
- 08:38 Suspect the pricing-core timeout default change in 7.25.4-e1b3; asking for a mitigation.
