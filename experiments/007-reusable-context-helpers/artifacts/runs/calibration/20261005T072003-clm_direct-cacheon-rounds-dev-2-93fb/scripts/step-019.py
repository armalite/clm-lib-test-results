import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if not re.search(r'INFO|slow query',l)]
  print(f.split('/')[-1],len(h),h[:3],h[-1:] if h else '')
  for i in h[:2]: print(' ',L[i-1][:200])