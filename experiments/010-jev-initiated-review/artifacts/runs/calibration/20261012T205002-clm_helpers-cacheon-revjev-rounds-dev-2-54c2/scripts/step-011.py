import re
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|FATAL|CRIT|error|fail',l) and 'slow query' not in l]
  print(s,len(h),[x[0] for x in h][:3],[x[0] for x in h][-2:])
  for x in h[:2]: print(' ',x)
  if not h: print(' first:',L[0][:150])