import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip()[:200])
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*')):
  hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|WARN|429|fail|expired|OOM|lag|disk|pool|inflight',l,re.I) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits),[h[0] for h in hits][:40])
  for h in hits[:2]:print('  ',h[0],h[1][:160])