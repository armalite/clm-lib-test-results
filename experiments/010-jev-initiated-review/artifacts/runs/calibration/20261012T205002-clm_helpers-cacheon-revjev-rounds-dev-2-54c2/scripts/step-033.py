import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
for s in ['auth-svc','shipping-svc','search-api','checkout-api','inventory-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'ERROR|certificate|429|max_inflight|SERVFAIL',l)]
  print(s,len(hits),[h[0] for h in hits]);
  for h in hits[:2]:print(h)