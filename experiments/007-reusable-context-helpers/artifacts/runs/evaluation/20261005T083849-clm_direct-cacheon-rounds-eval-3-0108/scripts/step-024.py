import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if 'ERROR' in l or 'error' in l or '429' in l]
  print(f.split('/')[-1],len(L))
  for x in L[:3]+L[-1:]:print(x[0],x[1][:200])