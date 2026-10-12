import re
b='/task/fixtures/round-08/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'WARN|ERROR|429|exhaust|fail|OOM|restart',l,re.I) and 'slow' not in l.lower():print(f,i,l.strip()[:150])