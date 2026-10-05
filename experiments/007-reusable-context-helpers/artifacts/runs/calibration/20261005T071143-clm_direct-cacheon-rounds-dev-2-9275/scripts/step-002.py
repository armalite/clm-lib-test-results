import json,glob
note='R1: board empty. inventory-svc ERROR dns lookup failed host=rates.internal SERVFAIL lines 7,20,50,54,57,62,65 (round-01/logs/inventory-svc.log). slow query WARNs everywhere = noise.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read())
for p in glob.glob('/task/fixtures/round-01/logs/*'):
  for i,l in enumerate(open(p),1):
    if ('ERROR' in l or 'error' in l.lower()) and 'slow query' not in l and 'dns lookup' not in l: print(p.split('/')[-1],i,l.strip()[:140])