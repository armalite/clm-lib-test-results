import re
b='/task/fixtures/round-11/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['search-api','auth-svc','shipping-svc','inventory-svc','notify-worker']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search('ERROR|WARN|429|fail|pool',l,re.I):print(s,i,l.rstrip()[:110])