import re
b='/task/fixtures/round-11/'
for i,l in enumerate(open(b+'board.md'),1): print(i,l.rstrip())
for s in ['search-api','auth-svc','shipping-svc']:
  h=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('config validation|tls handshake',l)]
  print(s,h[:10],len(h))