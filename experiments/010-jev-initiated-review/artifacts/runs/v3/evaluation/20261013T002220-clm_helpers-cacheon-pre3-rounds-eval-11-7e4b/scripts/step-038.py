import subprocess
print(open('/task/fixtures/round-10/board.md').read());print(open('/task/fixtures/round-10/changes.md').read())
import re
for s in ['inventory-svc','shipping-svc','checkout-api']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|SERVFAIL|batch',l)]
  print(s,len(h),h[:3],h[-1:] if h else '', L[h[0]-1][:150] if h else '')