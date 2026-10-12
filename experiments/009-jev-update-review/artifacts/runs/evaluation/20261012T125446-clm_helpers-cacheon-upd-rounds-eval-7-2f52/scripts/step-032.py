import re,glob
print(open('/task/fixtures/round-11/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
  h=[i for i,l in enumerate(open(f),1) if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l]
  print(f.split('/')[-1],len(h),h[:6])
  if h: print(open(f).readlines()[h[0]-1][:200])