import re
b='/task/fixtures/round-08/'
for i,l in enumerate(open(b+'board.md'),1):print(i,l.rstrip())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=[(i,l.strip()) for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('ERROR|SERVFAIL|429|expired|FATAL',l)]
  print(s,len(L),[i for i,_ in L][:12]);
  for i,l in L[:2]:print(' ',i,l[:150])