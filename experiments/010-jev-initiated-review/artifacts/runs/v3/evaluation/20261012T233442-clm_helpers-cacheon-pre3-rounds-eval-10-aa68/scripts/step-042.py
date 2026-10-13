import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-11/'+f),1):print(f,i,l.rstrip())
for s in ['shipping-svc','search-api','inventory-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').readlines()
  h=[i for i,l in enumerate(L,1) if re.search('ERROR|429|valid|restart',l)]
  print(s,len(h),h[:3],h[-3:]);
  if h:print(L[h[0]-1].strip()[:200])