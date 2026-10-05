import re
b='/task/fixtures/round-06/'
for f in['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  x=[(i,l[:150]) for i,l in enumerate(L,1) if re.search('ERROR|FATAL|SERVFAIL|429|heap|restart|OOM',l)]
  print(f,len(x),x[:3])