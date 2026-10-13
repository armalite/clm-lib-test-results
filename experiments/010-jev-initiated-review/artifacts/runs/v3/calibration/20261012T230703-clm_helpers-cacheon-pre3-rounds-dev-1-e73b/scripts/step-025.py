import re
b=open('/task/fixtures/round-07/board.md').read();print(b)
for s in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  L=open(f'/task/fixtures/round-07/logs/{s}.log').read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|429|exhaust|miss|inflight|cert|dns',l,re.I)]
  print(s,len(hits),[h[0] for h in hits][:3],[h[0] for h in hits][-1:] if hits else '')
  for h in hits[:2]: print(' ',h[1][:200])