import re,glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.strip()[:200])
for f in sorted(glob.glob(b+'logs/*.log')):
  seen=set()
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|fail|429|timeout|exhaust|inflight|lag|expired|disk|memory|oom',l,re.I):
      k=re.sub(r'\d+','',l)[-80:]
      if k in seen:continue
      seen.add(k);print(f.split('/')[-1],i,l.strip()[:160])