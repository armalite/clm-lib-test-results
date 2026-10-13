import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  n=p.split('/')[-1]
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|FATAL|429|SERVFAIL|cert|pool|OOM|disk|lag',l,re.I) and 'slow query' not in l:print(n,i,l.rstrip()[:150])