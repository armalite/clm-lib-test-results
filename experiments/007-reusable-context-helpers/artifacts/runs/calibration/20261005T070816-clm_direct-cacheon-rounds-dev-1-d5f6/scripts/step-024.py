import re,glob
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  seen=set()
  for i,l in enumerate(open(f),1):
    if re.search(r'WARN|ERROR|fail|429|timeout|exhaust|cert|dns|lag|memory|disk',l,re.I):
      k=re.sub(r'\d+','#',l)[30:110]
      if k in seen:continue
      seen.add(k);print(f.split('/')[-1],i,l.rstrip()[:160])