# On-call notes - payments-api incident 2031-03-06

Informal running notes. Not reviewed; may be out of date.

- 08:29 ingress-a 5xx for payments-api since build 6.25.3-646f rolled out. Many tax-engine timeouts.
- 08:39 Suspect the tax-engine timeout default change in 6.25.3-646f; asking for a mitigation.
