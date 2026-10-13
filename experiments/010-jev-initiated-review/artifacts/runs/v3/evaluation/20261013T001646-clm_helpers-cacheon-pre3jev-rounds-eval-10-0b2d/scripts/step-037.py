import re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|error|429|fail',l)]
  print(s,len(h),[x[0] for x in h][:8]);
  if h: print(h[0][1])