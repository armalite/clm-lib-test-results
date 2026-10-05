import os,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):
    if l.strip(): print(f,i,l.rstrip()[:200])
from collections import Counter
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  c=Counter()
  for i,l in enumerate(open(f),1):
    if 'INFO' in l or 'slow query' in l: continue
    if 'consumer lag' in l: c['lag']+=1; continue
    print(os.path.basename(f),i,l.rstrip()[:150])
  print(os.path.basename(f),dict(c))