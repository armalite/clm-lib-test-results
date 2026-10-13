import re
print(open('/task/fixtures/round-04/board.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-04/logs/{s}.log'),1):
    if re.search(r'ERROR|FATAL|CRIT|error=|429|SERVFAIL|cert|pool|max_inflight',l,re.I) and 'slow query' not in l.lower():
      print(s,i,l.strip()[:150])