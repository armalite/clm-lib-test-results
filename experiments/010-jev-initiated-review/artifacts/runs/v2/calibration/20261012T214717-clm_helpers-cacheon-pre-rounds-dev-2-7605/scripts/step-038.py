import re
print(open('/task/fixtures/round-08/board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-08/logs/{s}.log'),1):
    if re.search(r'ERROR|429|certificate|SERVFAIL|max_inflight|FATAL',l) and 'slow query' not in l: print(s,i,l.strip()[:150])