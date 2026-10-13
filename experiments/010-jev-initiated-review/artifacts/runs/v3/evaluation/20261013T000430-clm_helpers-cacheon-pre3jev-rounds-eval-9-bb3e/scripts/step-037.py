import re
print(open('/task/fixtures/round-10/board.md').read())
print(open('/task/fixtures/round-10/changes.md').read())
for s in ['search-api','shipping-svc','notify-worker']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i for i,l in enumerate(L,1) if re.search('max_inflight|disk|config',l)]
  print(s,h[:12])
  if h: print(L[h[-1]-1][:200])