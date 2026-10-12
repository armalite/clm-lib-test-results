import re
b='/task/fixtures/round-03/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search('ERROR|FATAL|429|dns|cert|pool|OOM|disk|lag|inflight',l,re.I) and 'slow query' not in l:
      print(f,i,l.strip()[:150])