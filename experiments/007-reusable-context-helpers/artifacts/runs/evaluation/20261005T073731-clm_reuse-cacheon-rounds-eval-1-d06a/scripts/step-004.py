import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f),1): print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if 'slow' in l.lower() or 'INFO' in l or 'level=info' in l.lower(): continue
    print(p.split('/')[-1],i,l.rstrip()[:150])