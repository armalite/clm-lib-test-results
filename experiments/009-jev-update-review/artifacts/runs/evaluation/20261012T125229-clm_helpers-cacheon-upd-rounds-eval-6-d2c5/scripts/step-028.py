import re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read())
for s in ['checkout-api','payments-svc','pricing-svc','ledger-svc','inventory-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|used_pct|batch_size|429|rss',l)]
  print(s,h[:15])