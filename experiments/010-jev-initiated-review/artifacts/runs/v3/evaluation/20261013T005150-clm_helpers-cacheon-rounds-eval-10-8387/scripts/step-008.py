import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|429|SERVFAIL|cert|OOM|lag|disk|pool',l,re.I):print(f.split('/')[-1],i,l.rstrip()[:150])