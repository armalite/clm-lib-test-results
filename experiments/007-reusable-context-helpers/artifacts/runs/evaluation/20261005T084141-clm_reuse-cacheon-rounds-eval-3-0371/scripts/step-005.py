import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|429|cert|pool|OOM|lag|disk|dns|invalid|inflight',l,re.I) and 'slow query' not in l: print(f.split('/')[-1],i,l.rstrip()[:160])