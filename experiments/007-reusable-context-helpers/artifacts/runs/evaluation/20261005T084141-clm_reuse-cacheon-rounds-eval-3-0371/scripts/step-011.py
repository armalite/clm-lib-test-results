import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-04/logs/*')):
  for i,l in enumerate(open(p),1):
    if re.search('ERROR|FATAL|429|cert|pool|inflight|OOM|disk|lag',l,re.I) and 'slow query' not in l:print(p.split('/')[-1],i,l.rstrip()[:150])