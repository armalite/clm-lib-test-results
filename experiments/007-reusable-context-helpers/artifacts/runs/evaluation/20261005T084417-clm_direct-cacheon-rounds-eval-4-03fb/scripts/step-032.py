import re
b='/task/fixtures/round-11/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['search-api','auth-svc','shipping-svc','inventory-svc','notify-worker']:
  L=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('ttl_s|429|pool|exhaust|config',l)]
  print(s,L[:15])