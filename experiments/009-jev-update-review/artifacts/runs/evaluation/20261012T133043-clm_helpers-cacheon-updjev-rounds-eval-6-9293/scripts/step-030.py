import re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read())
for s in ['checkout-api','payments-svc','pricing-svc','ledger-svc','inventory-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('disk|batch_size|429|heap|ERROR',l)]
  print(s,h[:12])