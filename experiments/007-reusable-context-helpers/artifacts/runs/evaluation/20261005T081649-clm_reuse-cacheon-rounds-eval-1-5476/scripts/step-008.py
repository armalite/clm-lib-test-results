import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  n=p.split('/')[-1]
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|error|lag|429|cert|dns|pool|ttl',l):print(n,i,l.rstrip()[:150])
