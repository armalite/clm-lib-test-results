print(open('/task/fixtures/round-11/board.md').read())
import re
for s in ['search-api','auth-svc','shipping-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('ERROR|config|cert|429',l)]
  print(s,len(h),h[:3])