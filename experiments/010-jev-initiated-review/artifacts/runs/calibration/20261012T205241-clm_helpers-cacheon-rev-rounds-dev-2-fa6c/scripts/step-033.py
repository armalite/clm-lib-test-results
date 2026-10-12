import re
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
for s in ['auth-svc','shipping-svc','search-api','checkout-api','inventory-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[i+1 for i,l in enumerate(L) if re.search('ERROR|error|fail|expired|429',l)]
  print(s,len(e),e[:12])
  if e:print(L[e[0]-1][:200])