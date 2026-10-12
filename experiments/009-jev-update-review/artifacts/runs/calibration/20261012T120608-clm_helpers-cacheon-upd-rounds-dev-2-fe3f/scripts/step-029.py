import re
for s in ['auth-svc','shipping-svc','search-api','checkout-api','inventory-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
  for k in ['cert','429','config validation','SERVFAIL','DNS']:
    h=[i for i,l in enumerate(L,1) if k.lower() in l.lower()]
    if h: print(s,k,h[:6])
print(open('/task/fixtures/round-11/board.md').read())