import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['checkout-api','search-api','payments-svc','inventory-svc','ledger-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|WARN|429|heap|inflight|cert',l)]
  print(s,len(h))
  for i,l in h[:3]+h[-1:]:print(' ',i,l[:150])