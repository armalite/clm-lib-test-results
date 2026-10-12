import json,re
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search(r'WARN|ERROR|exhaust|expired|disk|pool',l,re.I) and 'slow' not in l]
  print(s,len(h),[i for i,_ in h][:40]);
  for i,l in h[:2]: print(' ',i,l[:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 claims Thread D false alarm (synthetic monitor) - conflicts with R6/R7 real checkout-api pool-exhausted logs + CHG-113 pool_max=-4; verify in logs. changes.md:3 CHG-156 PROPOSED (ignore).'})
json.dump(c,open('/task/workspace/context.json','w'))