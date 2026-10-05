import re
print(open('/task/fixtures/round-08/board.md').read())
for s in ['auth-svc','inventory-svc','notify-worker','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'ERROR|WARN|error|429|pool|memory|cache|ttl',l,re.I) and 'slow query' not in l]
  print(s,len(h));[print(x) for x in h[:4]]