print(open('/task/fixtures/round-12/board.md').read())
import re
for s in ['checkout-api','inventory-svc','shipping-svc']:
  L=open(f'/task/fixtures/round-12/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|SERVFAIL|batch_size',l)]
  print(s,len(h),h[:3],h[-1:] if h else '')