import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','pricing-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if not re.search('slow query|request ok|heartbeat|gc |health ok',l,re.I)]
  print(s,len(h),h[0][0] if h else '',h[-1][0] if h else '')
  for i,l in h[:2]: print(i,l[:150])