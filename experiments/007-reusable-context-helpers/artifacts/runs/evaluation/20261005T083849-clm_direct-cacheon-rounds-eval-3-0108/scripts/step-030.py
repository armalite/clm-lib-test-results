import re
print(open('/task/fixtures/round-10/board.md').read())
for s in ['search-api','checkout-api','payments-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|heap|max_inflight|429',l)]
  print(s,len(h),h[:3],h[-3:])
  if h: print(L[h[0]-1][:200])