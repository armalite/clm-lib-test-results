import subprocess
print(open('/task/fixtures/round-10/board.md').read())
import re
for s in ['shipping-svc','search-api','inventory-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('429|config|ERROR|error',l)]
  print(s,len(h),h[:3],h[-3:])
  if h: print(L[h[0]-1][:200])