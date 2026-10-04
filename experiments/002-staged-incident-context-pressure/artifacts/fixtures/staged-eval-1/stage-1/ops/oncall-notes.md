# On-call notes - quotes-api incident 2031-05-22

Informal running notes. Not reviewed; may be out of date.

- 08:36 api-gateway 5xx for quotes-api since build 8.19.0-ff7b rolled out. Many risk-score timeouts.
- 08:46 Suspect the risk-score timeout default change in 8.19.0-ff7b; asking for a mitigation.
