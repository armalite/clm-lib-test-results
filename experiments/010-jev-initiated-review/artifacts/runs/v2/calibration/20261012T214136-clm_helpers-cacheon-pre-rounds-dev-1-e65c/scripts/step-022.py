import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f).read().splitlines()):print(f,i+1,l[:200])
for s in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  L=open('/task/fixtures/round-06/logs/'+s+'.log').read().splitlines()
  e=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('ERROR|error|fail|429|exhaust|WARN',l) and 'slow query' not in l]
  print(s,[x[0] for x in e]);[print(x) for x in e[:2]]