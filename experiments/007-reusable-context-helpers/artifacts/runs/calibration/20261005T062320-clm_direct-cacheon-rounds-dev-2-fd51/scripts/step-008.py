import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1): print(f,i,l.strip()[:300])
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  n=p.split('/')[-1]
  for i,l in enumerate(open(p),1):
    if 'slow query' in l or re.search(r'INFO|info',l): continue
    print(n,i,l.strip()[:140])