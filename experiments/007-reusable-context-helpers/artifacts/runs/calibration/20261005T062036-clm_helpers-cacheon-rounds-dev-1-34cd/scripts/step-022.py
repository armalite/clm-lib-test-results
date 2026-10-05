import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|429|pool|exhaust|FATAL|x509|cert|dns|lag|OOM|disk|config',l,re.I) and 'slow' not in l:print(f.split('/')[-1],i,l.rstrip()[:150])