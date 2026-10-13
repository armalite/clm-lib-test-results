import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for f in ['checkout-api','inventory-svc','ledger-svc','pricing-svc','search-api']:
  L=open(b+'logs/%s.log'%f).read().splitlines()
  e=[(i+1,l[:110]) for i,l in enumerate(L) if 'ERROR' in l or 'error' in l.lower()]
  print(f,len(e),e[:3])