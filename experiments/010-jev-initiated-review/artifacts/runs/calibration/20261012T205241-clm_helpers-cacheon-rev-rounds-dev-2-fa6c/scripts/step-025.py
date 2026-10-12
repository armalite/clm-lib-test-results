import json,re
b='/task/fixtures/round-08/logs/search-api.log'
L=[i for i,l in enumerate(open(b),1) if 'config validation' in l]
print(L)
for i,l in enumerate(open(b),1):
  if i==L[0]:print(l[:300])
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']+' search-api config validation failed (9) lines %s -> likely BAD_CONFIG_ROLLOUT CHG-120 (round-02/changes.md:3).'%L
c['entries']=[{'id':'notes','role':'note','body':n}]
json.dump(c,open('/task/workspace/context.json','w'))