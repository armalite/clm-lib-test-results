import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['search-api','shipping-svc','notify-worker','ledger-svc','inventory-svc']:
  L=[(i,l.rstrip()[:110]) for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('ERROR|disk|config|SERVFAIL|cert',l,re.I)]
  print(s,len(L));[print(i,l) for i,l in L[:4]]