import os,glob
for f in sorted(glob.glob('/task/fixtures/stage-2/**/*',recursive=True)):print(f)
for f in glob.glob('/task/fixtures/stage-2/logs/*.log'):
  L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if 'pool exhausted' in l]
  print(f,len(h),h[:3]);
  if h:print(L[h[0]-1])