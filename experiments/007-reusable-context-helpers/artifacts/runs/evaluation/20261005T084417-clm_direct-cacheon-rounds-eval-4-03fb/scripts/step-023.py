import re
b='/task/fixtures/round-08/'
print(open(b+'board.md').read())
for s in ['auth-svc','inventory-svc','notify-worker','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'429|pool|miss|memory|OOM|cert|DNS|lag|disk|config|ERROR',l,re.I)]
  print(s,h[:20])
  if h: print(L[h[0]-1][:200])