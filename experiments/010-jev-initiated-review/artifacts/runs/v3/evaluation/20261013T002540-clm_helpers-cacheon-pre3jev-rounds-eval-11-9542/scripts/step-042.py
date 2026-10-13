import re
print(open('/task/fixtures/round-11/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'slow query' in l: continue
    if re.search(r'ERROR|dns|batch|resolv|config',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])