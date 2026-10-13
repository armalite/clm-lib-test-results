import re
b=open('/task/fixtures/round-07/board.md').read().splitlines()
for i,l in enumerate(b,1):print(i,l)
import glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  L=open(f).read().splitlines();h=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|FATAL|expired|SERVFAIL|429|refused|OOM|disk|max_inflight',l,re.I)]
  print(f.split('/')[-1],len(h),h[:1],h[-1:] if h else '')