import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','pricing-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if not re.search('slow query|request ok|heartbeat|gc |health ok',l)]
  print(s,len(h),h[0][0] if h else '',h[-1][0] if h else '');[print(' ',x) for x in h[:2]]