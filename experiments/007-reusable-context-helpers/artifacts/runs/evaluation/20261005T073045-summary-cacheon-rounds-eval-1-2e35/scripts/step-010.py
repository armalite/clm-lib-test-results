import os,glob
from collections import Counter
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):
    if l.strip(): print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  c=Counter();n=0
  for i,l in enumerate(open(f),1):
    if 'INFO' in l or 'slow query' in l: continue
    if 'consumer lag' in l: c['lag']+=1; continue
    n+=1
    if n<=6: print(os.path.basename(f),i,l.rstrip()[:150])
  print(os.path.basename(f),dict(c),'other',n)