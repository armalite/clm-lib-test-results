import re
for f in ['board.md','changes.md']:
  try:
    for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
  except Exception as e:print(e)
import glob
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
  n=p.split('/')[-1]
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|429|cert|error',l,re.I) and 'slow' not in l:print(n,i,l.strip()[:110])