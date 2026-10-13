import re
print(open('/task/fixtures/round-05/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|WARN|error|429|expired|fail',l)]
  print(f.split('/')[-1],len(hits),hits[:15])
  if hits: print(L[hits[0]-1][:200])