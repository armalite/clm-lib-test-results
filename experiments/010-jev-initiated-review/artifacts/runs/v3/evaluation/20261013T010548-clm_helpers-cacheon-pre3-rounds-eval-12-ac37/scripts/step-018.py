import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','pricing-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'ERROR|WARN|error|429|cert|fail|lag|ttl',l)]
  print(s,len(h))
  for x in h[:3]+h[-1:]: print(x)