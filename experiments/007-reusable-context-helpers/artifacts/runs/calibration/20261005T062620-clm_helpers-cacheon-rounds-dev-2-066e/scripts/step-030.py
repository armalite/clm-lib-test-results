import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
for f in['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.strip()[:200])
import re
for s in['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  d={}
  for i,l in enumerate(open(f'/task/fixtures/round-10/logs/{s}.log'),1):
    if 'slow query' in l or 'INFO' in l or 'info' in l: continue
    m=re.search(r'msg\W+([^\",]+)',l); k=m.group(1) if m else l[:60]
    d.setdefault(k,[]).append(i)
  for k,v in d.items():print(s,k,v[:12])