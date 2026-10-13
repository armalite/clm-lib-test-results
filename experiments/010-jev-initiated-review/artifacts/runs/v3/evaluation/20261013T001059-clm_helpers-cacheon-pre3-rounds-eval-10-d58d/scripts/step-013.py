import re
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn|429|fail',l)]
  print(s,len(e))
  for i,l in e[:3]+e[-2:]: print(i,l[:150])