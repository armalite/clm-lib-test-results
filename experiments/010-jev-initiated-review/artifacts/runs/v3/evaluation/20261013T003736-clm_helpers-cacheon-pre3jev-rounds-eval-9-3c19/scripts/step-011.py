import json
n1='Round1: board empty. round-01/changes.md:3 CHG-108 APPLIED TLS session ticket rotation hourly (possible later CERT link). Baseline WARN slow query noise.'
n2='Round2: round-02/changes.md:4 CHG-120 APPLIED build 8.48.0 search-api sets http.max_inflight=-1 (possible BAD_CONFIG_ROLLOUT; no search-api errors yet through round3). ledger-svc DNS SERVFAIL host=geo.internal round-02/logs/ledger-svc.log:3,22,27.'
n3='Round3: round-03/board.md:3 Thread A DNS_RESOLUTION ledger-svc + inventory-svc ongoing. board.md:4 follow-up OPEN POSTMORTEM_DRAFT. Evidence: round-03/logs/inventory-svc.log:1,10,11; round-03/logs/ledger-svc.log:14,17. Next: advance to round 4.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2},{'id':'n3','role':'note','body':n3}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')