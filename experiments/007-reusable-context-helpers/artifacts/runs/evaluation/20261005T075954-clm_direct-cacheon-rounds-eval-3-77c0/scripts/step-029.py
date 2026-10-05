import re
p='/task/fixtures/round-10/'
print(open(p+'board.md').read())
for s in ['search-api','checkout-api','payments-svc','ledger-svc','inventory-svc']:
  L=open(p+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|heap|429|cert|config',l,re.I)]
  print(s,len(h),h[:12],L[h[0]-1][:150] if h else '')