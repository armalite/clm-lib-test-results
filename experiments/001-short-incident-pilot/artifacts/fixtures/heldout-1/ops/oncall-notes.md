# On-call notes - payments-api incident 2031-05-05

Informal running notes. Not reviewed; may be out of date.

- 07:52 Renewal ticket says new cert 37:7A:88:5C:F6:0F:27:D0 rolled out for payments-api; cert expiry is not a concern.
- 08:53 edge-gw 503s for payments-api. Could be db pool? stats look normal though.
- 09:02 tax-engine latency fine. Still investigating.
