import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for s in ['auth-svc','inventory-svc','notify-worker','search-api','shipping-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|WARN|429|pool|memory|oom|cert|dns|disk|lag',l,re.I) and 'slow query' not in l]
    print(s,len(h))
    for x in h[:5]+h[-2:]: print(x)