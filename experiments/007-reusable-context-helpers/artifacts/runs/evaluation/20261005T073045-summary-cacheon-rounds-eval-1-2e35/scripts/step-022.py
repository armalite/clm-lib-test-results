import os,glob
from collections import Counter
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):
    if l.strip(): print(f,i,l.rstrip()[:220])
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  c=Counter();n=0;cl=[]
  for i,l in enumerate(open(f),1):
    if 'INFO' in l or 'slow query' in l: continue
    if 'consumer lag' in l: c['lag']+=1; continue
    if 'certificate_expired' in l: c['cert']+=1; cl.append(i); continue
    n+=1
    if n<=4: print(os.path.basename(f),i,l.rstrip()[:150])
  print(os.path.basename(f),dict(c),cl[:6],'other',n)
open('/task/workspace/notes.md','a').write('\nR8 read step22\n')