import re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','pricing-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if not re.search('heartbeat|health ok|gc cycle|slow query|request ok',l)]
  print(s,len(h),h[:3],h[-1:] if h else '', L[h[0]-1][:150] if h else '')