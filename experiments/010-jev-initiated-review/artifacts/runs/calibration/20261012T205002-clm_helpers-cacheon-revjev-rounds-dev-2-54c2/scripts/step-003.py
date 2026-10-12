import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-107 APPLIED retry budget GETs=1. Logs: ts LEVEL svc msg k=v. Services: shipping-svc checkout-api auth-svc inventory-svc search-api. Noise: slow query WARNs, gc, heartbeat. R1 anomalies: only inventory-svc dns SERVFAIL host=rates.internal at round-01/logs/inventory-svc.log:7,20,50-65,85-90 (DNS_RESOLUTION candidate). Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')