import re
b='/task/fixtures/round-03/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'slow query' in l: continue
    if re.search(r'ERROR|WARN|429|fail|expired|OOM|lag|disk|pool|SERVFAIL',l,re.I): print(f,i,l.strip()[:150])