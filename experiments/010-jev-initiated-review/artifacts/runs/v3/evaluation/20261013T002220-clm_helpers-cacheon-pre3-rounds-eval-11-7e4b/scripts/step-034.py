print(open('/task/fixtures/round-09/board.md').read())
import re
for s in ['checkout-api','inventory-svc','pricing-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('ERROR|FATAL|CRIT',l)]
  print(s,len(h),h[:3])