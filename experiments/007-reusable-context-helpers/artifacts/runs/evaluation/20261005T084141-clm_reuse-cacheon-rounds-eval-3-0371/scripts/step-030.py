import re
b=open('/task/fixtures/round-10/board.md').read().splitlines()
for i,l in enumerate(b,1):print(i,l)
for s in ['checkout-api','payments-svc','search-api']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i for i,l in enumerate(L,1) if re.search('heap|max_inflight|config|429|ERROR',l)]
  print(s,len(h),h[:3],h[-3:])
  if h:print(L[h[0]-1][:200])