import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for s in ['auth-svc','inventory-svc','notify-worker','search-api','shipping-svc']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search(r'WARN|ERROR|429|pool|cache|memory|cert|dns|disk|lag',l,re.I) and 'slow query' not in l: print(s,i,l.strip()[:150])