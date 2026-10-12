import json
n1='R1: changes.md:3 CHG-107 APPLIED retry budget GETs=1. Logs: ts LEVEL svc msg k=v. Services: shipping-svc checkout-api auth-svc inventory-svc search-api. Noise: slow query WARNs, gc, heartbeat. R1: inventory-svc dns SERVFAIL host=rates.internal round-01/logs/inventory-svc.log:7,20,50-65,85-90.'
n2='R2: board.md:3 Thread A DNS_RESOLUTION inventory-svc+checkout-api ongoing. changes.md:3 CHG-120 APPLIED search-api http.max_inflight=-1 (watch BAD_CONFIG_ROLLOUT; no search-api errors yet). changes.md:4 CHG-121 auth-svc no config. DNS errs round-02/logs/checkout-api.log:8-59, inventory-svc.log:8-74. Next: advance.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')