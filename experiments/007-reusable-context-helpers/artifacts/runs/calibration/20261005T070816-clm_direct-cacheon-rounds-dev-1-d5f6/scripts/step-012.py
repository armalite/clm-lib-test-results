import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*')):
  seen=set()
  for i,l in enumerate(open(f),1):
    if re.search('WARN|ERROR|fail|429|timeout|exhaust',l,re.I):
      k=re.sub(r'\d+','#',l)[30:110]
      if k in seen:continue
      seen.add(k);print(f.split('/')[-1],i,l.rstrip()[:180])