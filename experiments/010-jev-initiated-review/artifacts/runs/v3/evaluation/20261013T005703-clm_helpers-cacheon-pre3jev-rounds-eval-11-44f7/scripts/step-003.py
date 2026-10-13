import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round1: board empty. logs (shipping,checkout,pricing,inventory,search) only routine WARN slow query ms 200-450; no ERRORs. Nothing incident-like yet.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read()[:1500])