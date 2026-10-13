for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-11/'+f),1):print(f,i,l.rstrip())
import re
for s in ['shipping-svc','search-api','inventory-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').readlines()
  h=[i+1 for i,l in enumerate(L) if re.search('429|validation|ERROR',l)]
  print(s,len(h),h[:3],h[-3:])