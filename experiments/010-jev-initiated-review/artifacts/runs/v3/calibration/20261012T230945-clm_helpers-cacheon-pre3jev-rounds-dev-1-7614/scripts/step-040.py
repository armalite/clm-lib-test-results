import re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['notify-worker','payments-svc','checkout-api','auth-svc','search-api']:
  n=0
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if 'slow query' in l:continue
    if re.search('error|fail|429|expire|pool|inflight|ERROR',l,re.I):
      n+=1
      if n<=4:print(s,i,l.rstrip()[:150])
  print(s,'count',n)