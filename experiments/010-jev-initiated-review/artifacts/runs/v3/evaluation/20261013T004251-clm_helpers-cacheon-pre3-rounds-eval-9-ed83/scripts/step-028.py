import re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'disk|DNS|SERVFAIL|cert|inflight|pool',l,re.I)]
  print(f.split('/')[-1],len(L),h[:30])
  if h: print(L[h[0]-1][:200])