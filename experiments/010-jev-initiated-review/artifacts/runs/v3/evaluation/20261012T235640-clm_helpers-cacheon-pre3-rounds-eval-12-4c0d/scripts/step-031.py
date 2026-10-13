import glob,re
for f in ['board.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f).read().splitlines(),1):print(f,i,l[:200])
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'certificate|429|ttl|stampede|lag|oom|disk|dns|pool|ERROR',l,re.I)]
  print(f.split('/')[-1],h[:12])
  if h: print(L[h[0]-1][:150])