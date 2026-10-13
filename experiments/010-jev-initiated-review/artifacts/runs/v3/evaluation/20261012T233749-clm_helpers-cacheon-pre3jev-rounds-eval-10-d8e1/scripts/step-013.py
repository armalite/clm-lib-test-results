import re
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    e=[i+1 for i,l in enumerate(L) if re.search('ERROR|error|FATAL',l)]
    print(s,len(e),e[:1],e[-1:] if e else '')
    if e: print(' ',L[e[0]-1][:200])