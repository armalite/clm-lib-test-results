import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  hits=[(i,l.strip()) for i,l in enumerate(open(p),1) if re.search(r'ERROR|429|cert|lag|disk|oom|memory|dns|pool|stampede|invalid',l,re.I) and 'slow' not in l.lower()]
  print(p.split('/')[-1],len(hits),[h[0] for h in hits][:20])
  for h in hits[:2]:print('  ',h[0],h[1][:180])