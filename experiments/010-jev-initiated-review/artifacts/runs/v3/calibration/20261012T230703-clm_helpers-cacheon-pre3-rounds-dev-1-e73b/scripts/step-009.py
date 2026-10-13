import re
b='/task/fixtures/round-03/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|FATAL|exhaust|inflight|429|cert|dns|OOM|disk|lag',l,re.I): print(f,i,l.strip()[:150])