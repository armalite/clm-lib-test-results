import re
b=open('/task/fixtures/round-10/board.md').read();print(b)
for s in ['checkout-api','payments-svc','search-api','ledger-svc','inventory-svc']:
    L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search('ERROR|heap|rss|max_inflight|cert|429',l,re.I)]
    print(s,len(h),h[:12])
    if h: print(L[h[0]-1][:200])