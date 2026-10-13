import json,re
print(open('/task/fixtures/round-11/board.md').read())
for s in ['search-api','auth-svc','shipping-svc','checkout-api','inventory-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'max_inflight|429|cert|x509|SERVFAIL|restart|OOM',l,re.I)]
  print(s,h[:12])
  if h: print(L[h[0]-1][:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))