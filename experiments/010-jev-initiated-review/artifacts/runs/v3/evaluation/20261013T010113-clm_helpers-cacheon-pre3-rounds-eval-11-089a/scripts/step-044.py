import re,glob
for l in open('/task/fixtures/round-09/board.md'):print(l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|error|memory|restart|OOM|429',l):print(f.split('/')[-1],i,l.strip()[:110])