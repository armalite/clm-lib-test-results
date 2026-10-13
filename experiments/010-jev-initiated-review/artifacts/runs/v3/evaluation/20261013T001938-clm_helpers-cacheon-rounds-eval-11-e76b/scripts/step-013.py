import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*')):
  hits=[(i,l.strip()) for i,l in enumerate(open(f),1) if re.search(r'ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|SERVFAIL|lag|OOM|disk|batch',l,re.I)]
  n=f.split('/')[-1]
  if hits:print(n,len(hits),hits[0][0],hits[-1][0],hits[0][1][:160]);print('  last',hits[-1][1][:160])
  else:print(n,'clean')