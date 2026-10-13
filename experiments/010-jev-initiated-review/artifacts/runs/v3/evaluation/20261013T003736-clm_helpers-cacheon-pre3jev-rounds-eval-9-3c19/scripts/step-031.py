import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  hits=[(i,l.strip()[:110]) for i,l in enumerate(open(p),1) if re.search('ERROR|disk|SERVFAIL|cert|429|max_inflight|no space',l,re.I)]
  print(p.split('/')[-1],len(hits))
  for h in hits[:4]:print(' ',h)