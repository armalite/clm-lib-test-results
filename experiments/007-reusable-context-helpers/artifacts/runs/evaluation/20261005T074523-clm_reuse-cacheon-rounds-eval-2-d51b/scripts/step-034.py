import re
b='/task/fixtures/round-12/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['inventory-svc','ledger-svc','pricing-svc','auth-svc','payments-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if not re.search('slow query|INFO|/v1/health',l)]
  print(s,len(h),h[:3],h[-1:] if h else '', L[h[0]-1][:150] if h else '')