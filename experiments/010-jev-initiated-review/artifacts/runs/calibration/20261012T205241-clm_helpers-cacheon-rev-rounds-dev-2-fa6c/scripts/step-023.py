import re
b='/task/fixtures/round-08/'
for i,l in enumerate(open(b+'board.md'),1):print(i,l.rstrip())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=[(i,l.strip()) for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('ERROR|error|429|SERVFAIL|cert',l,re.I) and 'slow' not in l.lower()]
  print(s,len(L),[i for i,_ in L]);
  if L:print(L[0][1][:200])