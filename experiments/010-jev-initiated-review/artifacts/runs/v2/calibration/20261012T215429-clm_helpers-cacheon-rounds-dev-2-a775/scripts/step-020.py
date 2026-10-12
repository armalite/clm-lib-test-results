import re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ('ERROR' in l or 'error' in l.lower()) and 'slow query' not in l:
      print(f,i,l.strip()[:160])