import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*')):
  L=[(i,l.strip()) for i,l in enumerate(open(f),1) if 'ERROR' in l or 'error' in l.lower() or '429' in l or 'fail' in l.lower()]
  print(f.split('/')[-1],len(L),[x[0] for x in L][:3],[x[0] for x in L][-1:] if L else '',L[0][1][:150] if L else '')