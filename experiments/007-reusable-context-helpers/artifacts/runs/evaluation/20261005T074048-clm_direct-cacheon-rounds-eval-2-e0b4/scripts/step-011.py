import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|error|fail|429|timeout|heap|OOM|restart',l):print(p.split('/')[-1],i,l.rstrip()[:160])