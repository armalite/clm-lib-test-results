import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  n=p.split('/')[-1]
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|error|429|fail',l):print(n,i,l.rstrip()[:150])