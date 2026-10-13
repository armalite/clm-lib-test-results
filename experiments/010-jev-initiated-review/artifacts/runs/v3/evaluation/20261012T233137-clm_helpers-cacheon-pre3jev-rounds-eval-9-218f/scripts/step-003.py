import json
b=open('/task/fixtures/round-01/changes.md').read()
print(b[:1500])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round1: board empty. Logs notify-worker,shipping-svc,ledger-svc,inventory-svc,search-api: only routine WARN slow query (200-450ms), no errors. Baseline noise. changes.md content printed in step 3 obs.'}]}
json.dump(c,open('/task/workspace/context.json','w'))