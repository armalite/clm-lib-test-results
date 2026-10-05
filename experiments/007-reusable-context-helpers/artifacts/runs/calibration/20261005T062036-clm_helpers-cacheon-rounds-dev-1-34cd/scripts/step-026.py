import re,glob
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'429|pool|config validation|ERROR|FATAL',l,re.I):print(f.split('/')[-1],i,l.rstrip()[:150])