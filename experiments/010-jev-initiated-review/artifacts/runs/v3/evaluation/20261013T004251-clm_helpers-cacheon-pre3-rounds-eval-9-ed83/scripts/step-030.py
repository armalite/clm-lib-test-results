import re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l[:200])
import glob
for f in sorted(glob.glob(b+'logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|disk|DNS|SERVFAIL|cert|inflight|pool|429|fail',l,re.I)]
  print(f.split('/')[-1],h[:25])
  if h: print(L[h[0]-1][:180])