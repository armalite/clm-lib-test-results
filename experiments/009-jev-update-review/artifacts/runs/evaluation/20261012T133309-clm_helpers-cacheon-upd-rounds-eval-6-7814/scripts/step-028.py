import re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read())
for s in ['checkout-api','payments-svc','pricing-svc','ledger-svc','inventory-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'WARN|ERROR|disk|batch|429|heap',l,re.I) and 'slow query' not in l]
  print(s,len(h),h[:1],h[-1:] if h else '', L[h[0]-1][:150] if h else '')