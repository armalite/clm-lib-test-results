import json,re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[i for i,l in enumerate(L,1) if re.search('ERROR|error|429|certificate|max_inflight|SERVFAIL',l) and 'slow' not in l]
  print(s,e[:15]);
  if e:print(L[e[0]-1][:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))