import re
print(open('/task/fixtures/round-06/board.md').read())
for s in ['checkout-api','inventory-svc','ledger-svc','notify-worker','shipping-svc']:
  L=open(f'/task/fixtures/round-06/logs/{s}.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if not re.search(r'slow query|request ok|gc|health|heartbeat',l)]
  print(s,len(h));[print(i,l[:110]) for i,l in h[:3]]
  if h: print('last',h[-1][0])