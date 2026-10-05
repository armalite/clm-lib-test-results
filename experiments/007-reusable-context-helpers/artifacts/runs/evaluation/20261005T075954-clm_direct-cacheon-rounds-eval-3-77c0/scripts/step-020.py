import re
b='/task/fixtures/round-07/'
for i,l in enumerate(open(b+'board.md'),1):print('board',i,l.rstrip())
for s in ['checkout-api','inventory-svc','ledger-svc','payments-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'ERROR|429|cert|disk|heap|rss|OOM|restart|level=error|"error"',l,re.I) and 'slow query' not in l]
  print(s,len(hits),[i for i,_ in hits][:40])
  for i,l in hits[:2]:print(' ',i,l[:200])
  if not hits:print(' first',L[0][:200])