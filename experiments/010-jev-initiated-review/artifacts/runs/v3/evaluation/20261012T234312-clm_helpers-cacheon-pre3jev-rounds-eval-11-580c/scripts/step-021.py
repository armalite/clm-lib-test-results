import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in['checkout-api','inventory-svc','pricing-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if 'INFO' not in l and 'slow query' not in l]
  print(s,len(h),h[:3],h[-1:] if h else '')
  for i in h[:2]:print(' ',L[i-1][:180])