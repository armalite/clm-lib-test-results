import re,glob
print(open('/task/fixtures/round-08/board.md').read())
import os
if os.path.exists('/task/fixtures/round-08/changes.md'):print(open('/task/fixtures/round-08/changes.md').read())
p=re.compile(r'ERROR|FATAL|CRIT|SERVFAIL|429|refused|exhaust|OOM|expired|lag|disk|invalid',re.I)
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  hits=[(i,l.strip()) for i,l in enumerate(open(f),1) if p.search(l) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]:print(' ',h[0],h[1][:150])