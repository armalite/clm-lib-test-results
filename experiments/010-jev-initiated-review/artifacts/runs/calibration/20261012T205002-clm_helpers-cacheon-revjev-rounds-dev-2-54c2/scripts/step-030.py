import json,re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'ERROR|429|certificate|validation|SERVFAIL',l)]
  print(s,len(e),[i for i,_ in e][:20]);
  if e: print(e[0][1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))