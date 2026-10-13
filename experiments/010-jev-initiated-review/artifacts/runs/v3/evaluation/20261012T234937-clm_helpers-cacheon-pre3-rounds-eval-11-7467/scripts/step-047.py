import re
b='/task/fixtures/round-12/'
print(open(b+'board.md').read())
for s in ['checkout-api','inventory-svc','pricing-svc','search-api','shipping-svc']:
  L=[i+1 for i,l in enumerate(open(b+'logs/'+s+'.log')) if re.search('ERROR|SERVFAIL|429|batch_size',l)]
  print(s,len(L),L[:1],L[-1:])