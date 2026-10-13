import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  L=[(i+1,l.strip()) for i,l in enumerate(open(b+'logs/'+f)) if re.search('ERROR|WARN|FATAL|fail|429|SERVFAIL',l,re.I) and 'slow' not in l.lower()]
  print(f,len(L),L[0][0] if L else '',L[-1][0] if L else '');[print(' ',x) for x in L[:2]]