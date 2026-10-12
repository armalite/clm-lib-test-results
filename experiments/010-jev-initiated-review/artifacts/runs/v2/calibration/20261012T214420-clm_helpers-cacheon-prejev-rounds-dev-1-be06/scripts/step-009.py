import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  for i,l in enumerate(open(p),1):
    if 'slow query' in l or 'INFO' in l or 'level=info' in l:continue
    print(p.split('/')[-1],i,l.rstrip()[:150])