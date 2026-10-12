import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['auth-svc','search-api','notify-worker','payments-svc','checkout-api']:
  h=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('pool|429|config validation|ERROR',l) and 'slow query' not in l]
  print(s,h[:20])