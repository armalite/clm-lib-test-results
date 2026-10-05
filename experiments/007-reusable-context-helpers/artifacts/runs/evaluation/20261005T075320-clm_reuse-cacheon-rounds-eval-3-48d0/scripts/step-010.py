import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|error|429|cert|OOM|pool|disk|lag|invalid',l) and 'slow query' not in l:print(f.split('/')[-1],i,l.rstrip()[:150])