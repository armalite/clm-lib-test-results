import json
n1='Round1: services notify-worker, shipping-svc, ledger-svc, inventory-svc, search-api. Baseline WARN slow query ms 200-450 = noise. round-01/changes.md:3 CHG-108 APPLIED TLS session ticket rotation hourly.'
n2='Round2: board empty. changes: round-02/changes.md:4 CHG-120 APPLIED build 8.48.0 to search-api sets http.max_inflight=-1 (suspect BAD_CONFIG_ROLLOUT, no search-api errors yet); :5 CHG-121 shipping-svc no config; :3 CHG-117 log sampling. ledger-svc DNS SERVFAIL host=geo.internal round-02/logs/ledger-svc.log lines 3,22,27,34,35,41,48,52,59,71,77,81 (DNS_RESOLUTION candidate, ongoing). Next: advance to round 3.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')