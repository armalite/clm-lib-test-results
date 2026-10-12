import json,re
b='/task/fixtures/round-07/'
for i,l in enumerate(open(b+'board.md'),1):print('B',i,l.rstrip())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  hits=[i for i,l in enumerate(L,1) if re.search(r'ERROR|error|fail|expired|SERVFAIL|429|inflight',l)]
  print(s,len(hits),hits[:3],hits[-1:] if hits else '')
  if hits:print(' ',L[hits[0]-1][:220])