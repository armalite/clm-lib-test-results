import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for n in ['payments-svc','checkout-api','auth-svc','search-api','notify-worker']:
  L=open(b+'logs/'+n+'.log').readlines()
  h=[i for i,l in enumerate(L,1) if re.search(r'429|ERROR|pool|inflight|refused',l)]
  print(n,h[:12])
  if h: print(L[h[0]-1][:200])