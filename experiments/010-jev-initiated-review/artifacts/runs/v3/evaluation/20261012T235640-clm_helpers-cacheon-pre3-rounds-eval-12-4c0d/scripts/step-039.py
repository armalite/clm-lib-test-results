import re
print(open('/task/fixtures/round-10/board.md').read());print(open('/task/fixtures/round-10/changes.md').read())
for s in ['pricing-svc','checkout-api','ledger-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('429|ttl|config|restart|OOM',l)]
  print(s,h[:15]);
  if h: print(L[h[-1]-1][:200])