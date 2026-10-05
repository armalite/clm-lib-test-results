import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if ('WARN' in l or 'ERROR' in l) and 'slow query' not in l:print(p.split('/')[-1],i,l.rstrip()[:150])