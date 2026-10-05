import re
print(open('/task/fixtures/round-11/board.md').read())
for s in ['auth-svc','shipping-svc','search-api','checkout-api','inventory-svc']:
    L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search(r'cert|validation|429|SERVFAIL|ERROR',l,re.I)]
    print(s,h[:10])
    if h: print(L[h[0]-1][:200])