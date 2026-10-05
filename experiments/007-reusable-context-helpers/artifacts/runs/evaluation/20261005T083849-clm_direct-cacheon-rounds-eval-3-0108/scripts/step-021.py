import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','payments-svc','search-api']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    h=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|429|disk|heap|cert|restart|OOM',l,re.I)]
    print(s,len(h))
    for i,l in h[:3]+h[-2:]: print(i,l[:150])