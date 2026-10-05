import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for s in ['search-api','auth-svc','shipping-svc']:
  h=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('config validation|429|tls handshake|memory|OOM',l)]
  print(s,h[:12],len(h))
for i,l in enumerate(open(b+'logs/search-api.log'),1):
  if 'slow query' not in l and i<4: print(i,l[:200].rstrip())