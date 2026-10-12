import json
note='''R1: board empty. Slow query WARNs (200-450ms) everywhere = noise. inventory-svc DNS SERVFAIL host=rates.internal at round-01/logs/inventory-svc.log:7,20,50. round-01/changes.md:3 CHG-107 APPLIED retry budget GETs=1.
R2: round-02/board.md:3 Thread A DNS_RESOLUTION inventory-svc+checkout-api ongoing. round-02/changes.md:3 CHG-120 APPLIED build 8.59.8 search-api sets http.max_inflight=-1 (possible BAD_CONFIG_ROLLOUT, watch search-api); changes.md:4 CHG-121 auth-svc no config. DNS errors round-02/logs/checkout-api.log:8,24,59; round-02/logs/inventory-svc.log:8,12,74. No other non-noise errors in R2.'''
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')