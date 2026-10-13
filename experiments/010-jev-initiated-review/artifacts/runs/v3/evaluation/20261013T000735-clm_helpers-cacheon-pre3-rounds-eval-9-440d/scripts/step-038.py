import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
for s in ['inventory-svc','ledger-svc','notify-worker','search-api','shipping-svc']:
  h=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('error|ERROR|fail|expired|disk|SERVFAIL|max_inflight|invalid|429|pool',l,re.I)]
  print(s,len(h),h[:15])
  if h:print(' ',open(b+'logs/'+s+'.log').readlines()[h[0]-1].strip()[:180])