import json
note='R1: board empty. changes: CHG-107 APPLIED retry budget idempotent GETs=1 (round-01/changes.md:3). inventory-svc ERROR dns lookup failed host=rates.internal SERVFAIL lines 7,20,50,54,57,62,65 (round-01/logs/inventory-svc.log). slow query WARNs = noise. No other errors.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))
print('ok')