import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-02/'+f).read().splitlines(),1): print(f,i,l)
import glob
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
  for i,l in enumerate(open(p).read().splitlines(),1):
    if 'slow query' not in l: print(p.split('/')[-1],i,l[:130])