import re
b='/task/fixtures/round-07/'
for i,l in enumerate(open(b+'board.md'),1):print(i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|WARN|FATAL|429|disk|heap|cert',l,re.I) and 'slow' not in l.lower():print(f,i,l.rstrip()[:150])