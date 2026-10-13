import re
print(open('/task/fixtures/round-09/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|429|fail',l)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]: print(h[0],h[1][:160])