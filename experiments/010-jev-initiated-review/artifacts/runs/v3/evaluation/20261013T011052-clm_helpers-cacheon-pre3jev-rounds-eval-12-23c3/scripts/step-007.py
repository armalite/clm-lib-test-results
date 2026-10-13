import json
n1='R1: board empty. changes.md:3 CHG-110 APPLIED retry budget GETs=1; :4 CHG-113 APPLIED build 3.22.4 pricing-svc sets cache.ttl_s=-1 (BAD_CONFIG_ROLLOUT candidate, no errors yet); :5 CHG-114 APPLIED 3.22.4 ledger-svc no config. Logs only background slow query WARNs.'
n2='R2: board.md:3 Follow-up OPEN CAPACITY_REVIEW. changes.md:3 CHG-115 APPLIED retry budget GETs=1. search-api.log lines 11,15,19,24,27,33,57: ERROR tls handshake failed peer=sso.example.net reason=certificate_expired (CERT_EXPIRED candidate on search-api, not yet on board). Other logs clean. Next: advance to round 3.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))