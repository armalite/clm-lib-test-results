print(open('/task/fixtures/round-12/board.md').read())
import re
for s in ['checkout-api','inventory-svc','shipping-svc']:
  L=open(f'/task/fixtures/round-12/logs/{s}.log').read().splitlines()
  for i,l in enumerate(L,1):
    if re.search(r'ERROR|error|fail',l): print(s,i,l[:150])