import re
L=open('/task/fixtures/round-07/logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'slow query' not in l and re.search(r'ERROR|429|inflight|rate',l,re.I):print(i,l[:180])