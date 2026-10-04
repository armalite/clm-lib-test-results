# On-call notes - payments-api incident 2031-04-14

Informal running notes. Not reviewed; may be out of date.

- 08:33 ingress-a 5xx for payments-api since build 5.36.1-f33d rolled out. Many risk-score timeouts.
- 08:43 Suspect the risk-score timeout default change in 5.36.1-f33d; asking for a mitigation.
