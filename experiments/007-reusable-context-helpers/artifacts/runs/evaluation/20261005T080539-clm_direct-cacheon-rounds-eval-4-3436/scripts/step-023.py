import re
b='/task/fixtures/round-08/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'WARN|ERROR|429|pool|cache|disk|cert|dns|lag',l,re.I) and 'slow query' not in l: print(f,i,l.strip()[:150])