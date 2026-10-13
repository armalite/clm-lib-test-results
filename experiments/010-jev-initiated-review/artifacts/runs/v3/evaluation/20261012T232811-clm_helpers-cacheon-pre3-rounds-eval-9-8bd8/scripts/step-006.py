import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f).read().splitlines(),1):print(f,i,l)
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if 'INFO' in l or 'slow query' in l: continue
    print(p.split('/')[-1],i,l.strip()[:160])