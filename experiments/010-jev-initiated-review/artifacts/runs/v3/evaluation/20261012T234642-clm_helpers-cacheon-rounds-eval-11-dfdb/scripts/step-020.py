import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  hits=[(i,l.strip()[:150]) for i,l in enumerate(open(f),1) if re.search('ERROR|FATAL|429|fail|SERVFAIL|cert|expired',l,re.I)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]:print(' ',h)
  print('  lines',[h[0] for h in hits])