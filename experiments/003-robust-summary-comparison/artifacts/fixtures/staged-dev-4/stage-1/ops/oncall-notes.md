# On-call notes - profile-svc incident 2031-06-06

Informal running notes. Not reviewed; may be out of date.

- 08:28 api-gateway 5xx for profile-svc since build 8.15.4-7744 rolled out. Many ledger-api timeouts.
- 08:38 Suspect the ledger-api timeout default change in 8.15.4-7744; asking for a mitigation.
