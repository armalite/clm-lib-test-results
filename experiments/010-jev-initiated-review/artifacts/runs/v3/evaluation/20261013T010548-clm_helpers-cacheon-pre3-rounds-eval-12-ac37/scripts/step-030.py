import re
b='/task/fixtures/round-08/'
print(open(b+'board.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','pricing-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'error|ERROR|429|cert|fail|lag|expired|warn',l,re.I)]
  print(s,len(h),h[:3],h[-1:] if h else '')
  if h: print(L[h[0]-1][:200])