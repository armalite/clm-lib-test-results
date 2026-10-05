import glob,re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|WARN|error|fail|429|lag',l,re.I):print(f.split('/')[-1],i,l.rstrip()[:150])