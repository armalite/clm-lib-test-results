import re
for s in ['search-api','auth-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-01/logs/{s}.log'),1):
    if ('INFO' not in l and 'slow query' not in l) or re.search('ttl|cache|ERROR',l): print(s,i,l.rstrip()[:150])