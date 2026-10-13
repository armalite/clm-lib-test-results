import re
b=open('/task/fixtures/round-08/board.md').read().splitlines()
for i,l in enumerate(b,1):print(i,l)
import glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
  L=open(f).read().splitlines();e=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|WARN|429|certif|SERVFAIL',l)]
  print(f.split('/')[-1],len(e),e[:1],e[-1:] if e else '')