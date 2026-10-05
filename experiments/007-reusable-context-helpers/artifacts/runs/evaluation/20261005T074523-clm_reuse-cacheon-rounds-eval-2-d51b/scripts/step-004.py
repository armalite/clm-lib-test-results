import re,glob
r='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob(r+'logs/*')):
  for i,l in enumerate(open(p),1):
    if re.search('slow query|INFO|/v1/health',l,re.I):continue
    print(p.split('/')[-1],i,l.rstrip()[:150])