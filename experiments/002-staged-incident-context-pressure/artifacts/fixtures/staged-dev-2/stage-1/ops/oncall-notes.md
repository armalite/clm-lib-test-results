# On-call notes - catalog-api incident 2031-05-17

Informal running notes. Not reviewed; may be out of date.

- 08:29 edge-gw 5xx for catalog-api since build 8.26.3-35fd rolled out. Many ledger-api timeouts.
- 08:39 Suspect the ledger-api timeout default change in 8.26.3-35fd; asking for a mitigation.
