import json,re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    e=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn',l) and 'slow' not in l]
    print(s,len(e))
    for i,l in e[:2]+e[-1:]: print(i,l[:220])