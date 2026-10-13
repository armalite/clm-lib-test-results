import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if 'ERROR' in l or 'WARN' in l]
  print(f.split('/')[-1],len(L));[print(i,l[:150]) for i,l in L[:3]]