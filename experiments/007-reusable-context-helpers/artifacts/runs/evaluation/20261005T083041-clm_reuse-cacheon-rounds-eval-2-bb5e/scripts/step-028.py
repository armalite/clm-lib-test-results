import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['auth-svc','inventory-svc','ledger-svc','payments-svc','pricing-svc']:
  L=[(i,l) for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('ERROR|SERVFAIL|config|heap|cert|429|restart|disk|lag',l,re.I) and 'slow query' not in l]
  print(s,len(L),[i for i,_ in L][:3],[i for i,_ in L][-1:] if L else '');
  if L:print(L[0][1][:200])