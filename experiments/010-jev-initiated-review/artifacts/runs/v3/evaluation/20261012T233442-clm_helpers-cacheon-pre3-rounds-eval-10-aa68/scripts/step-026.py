import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|FATAL|429|SERVFAIL|backoff|retry',l,re.I)]
  print(s,len(hits),hits[:2],hits[-1:] if hits else '')