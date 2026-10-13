import re
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
for s in ['auth-svc','shipping-svc','search-api','checkout-api','inventory-svc']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search(r'ERROR|cert|config|429|SERVFAIL',l,re.I): print(s,i,l.strip()[:150])