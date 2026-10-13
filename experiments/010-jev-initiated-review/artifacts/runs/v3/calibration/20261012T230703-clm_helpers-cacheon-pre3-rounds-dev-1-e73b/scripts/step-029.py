import re
b='/task/fixtures/round-08/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|429|exhaust|miss|inflight|cert|dns|disk|memory|lag',l,re.I)]
  print(s,len(hits),hits[:3],hits[-1:] if hits else '')
  if hits: print(L[hits[0]-1][:200])