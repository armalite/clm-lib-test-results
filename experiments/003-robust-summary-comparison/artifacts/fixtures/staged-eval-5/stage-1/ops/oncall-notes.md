# On-call notes - quotes-api incident 2031-05-15

Informal running notes. Not reviewed; may be out of date.

- 08:31 ingress-a 5xx for quotes-api since build 7.20.4-0a00 rolled out. Many rates-svc timeouts.
- 08:41 Suspect the rates-svc timeout default change in 7.20.4-0a00; asking for a mitigation.
