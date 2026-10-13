import re
b='/task/fixtures/round-12/'
print(open(b+'board.md').read())
for s in ['checkout-api','inventory-svc','shipping-svc','pricing-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('SERVFAIL|batch_size|429|config|heap',l)]
  print(s,len(h),h[:3],h[-1:] if h else '')
  if h: print(L[h[0]-1][:160])