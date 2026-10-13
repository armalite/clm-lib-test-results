import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-11/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-11/logs/*')):
  n=0
  for i,l in enumerate(open(p),1):
    if re.search('ERROR|WARN|429|fail|restart',l,re.I) and n<4:n+=1;print(p[-20:],i,l.rstrip()[:150])