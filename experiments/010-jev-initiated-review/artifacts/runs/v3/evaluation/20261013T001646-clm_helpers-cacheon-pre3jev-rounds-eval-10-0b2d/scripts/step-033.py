import re
b=open('/task/fixtures/round-09/board.md').read();print(b)
import os
for f in sorted(os.listdir('/task/fixtures/round-09/logs')):
  L=open('/task/fixtures/round-09/logs/'+f).read().splitlines()
  h=[(i+1,l[:140]) for i,l in enumerate(L) if re.search('ERROR|429|SERVFAIL|FATAL',l)]
  print(f,len(h));[print(x) for x in h[:4]]