import re
b=open('/task/fixtures/round-11/board.md').read().splitlines()
for i,l in enumerate(b,1):print(i,l)
for s in ['search-api','auth-svc','shipping-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-11/logs/{s}.log'),1):
    if re.search(r'max_inflight|certificate|ERROR',l):print(s,i,l.strip()[:110])