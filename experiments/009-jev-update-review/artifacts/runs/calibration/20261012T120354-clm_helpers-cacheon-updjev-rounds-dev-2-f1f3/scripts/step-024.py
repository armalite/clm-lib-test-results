import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: board.md:3 Thread C still restarting. changes.md:3 CHG-166 retry budget (noise, like CHG-107).'})
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['search-api','auth-svc','shipping-svc','checkout-api','inventory-svc']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('max_inflight|429|certificate|SERVFAIL|ERROR',l)]
  print(s,h[:12])
  if h: print(L[h[0]-1][:200])