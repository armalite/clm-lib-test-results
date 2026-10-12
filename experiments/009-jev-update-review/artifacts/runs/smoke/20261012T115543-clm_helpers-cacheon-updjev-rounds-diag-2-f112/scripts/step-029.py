import json,re
for s in ['inventory-svc','ledger-svc','notify-worker','pricing-svc','search-api']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|disk|pool_max|cert|SERVFAIL|restart',l,re.I)]
  print(s,h[:8],L[h[0]-1][:150] if h else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))