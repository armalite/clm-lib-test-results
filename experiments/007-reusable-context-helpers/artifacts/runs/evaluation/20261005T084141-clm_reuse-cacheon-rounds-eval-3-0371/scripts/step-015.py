import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for s in ['checkout-api','search-api','inventory-svc','ledger-svc','payments-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    hits=[(i+1,l[:140]) for i,l in enumerate(L) if re.search(r'ERROR|WARN|429|heap|disk|cert|restart|OOM',l,re.I) and 'slow query' not in l]
    print(s,len(hits))
    for h in hits[:6]: print(' ',h)
    if hits: print('  last',hits[-1])