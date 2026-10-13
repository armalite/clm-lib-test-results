import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
  L=open(p).read().splitlines()
  bad=[(i,l) for i,l in enumerate(L,1) if re.search('ERROR|WARN|FATAL|err',l)]
  print(p.split('/')[-1],len(bad))
  for i,l in bad[:3]:print(' ',i,l[:150])