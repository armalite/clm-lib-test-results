import re
p='/task/fixtures/round-07/'
print(open(p+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
    L=open(p+'logs/'+s+'.log').read().splitlines()
    e=[i+1 for i,l in enumerate(L) if re.search('ERROR|error|429|fail',l,re.I) and 'slow query' not in l]
    print(s,len(e),e[:1],e[-1:] if e else '', L[e[0]-1][:200] if e else '')