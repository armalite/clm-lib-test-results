import re
print(open('/task/fixtures/round-09/board.md').read())
for s in ['search-api','shipping-svc','notify-worker']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  for i,l in enumerate(L,1):
    if re.search('ERROR|WARN|disk|max_inflight',l): print(s,i,l[:140])