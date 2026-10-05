import re
for s in ['auth-svc','checkout-api','inventory-svc','search-api']:
  p='/task/fixtures/round-03/logs/%s.log'%s
  ls=[(i,l.strip()[:120]) for i,l in enumerate(open(p),1) if re.search(r'ERROR',l)]
  print(s,len(ls),ls[:2],ls[-1:] if ls else '')
from ctx import keep_notes
import json
n=json.load(open('context.json'))['entries'][0]['body']
keep_notes(n.replace(' Next: advance to R3.','')+'\nR3: board.md:3 Thread B DB_POOL_EXHAUSTED auth-svc ongoing. changes CHG-126 PROPOSED only. WARN slow query all svcs.')