import json
n1='R1: board empty; logs only routine WARN slow query noise. CHG-108 APPLIED (round-01/changes.md:3) TLS session ticket rotation hourly.'
n2='R2: board empty. changes round-02/changes.md: CHG-117 log sampling health 1%; CHG-120 APPLIED build 8.48.0 search-api sets http.max_inflight=-1 (line 4, suspicious BAD_CONFIG); CHG-121 shipping-svc 8.48.0 no config. ledger-svc DNS SERVFAIL host=geo.internal round-02/logs/ledger-svc.log:3,22,27,34,35,41,48,52,59,71,77,81 (09:02-09:54) -> DNS_RESOLUTION candidate. search-api no errors yet.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')