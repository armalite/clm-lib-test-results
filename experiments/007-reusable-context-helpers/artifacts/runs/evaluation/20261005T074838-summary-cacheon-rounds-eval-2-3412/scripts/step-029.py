import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f).read().splitlines(),1): print(f,i,l[:200])
for p in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
  L=open(p).read().splitlines();e=[i for i,l in enumerate(L,1) if 'ERROR' in l or 'WARN' in l]
  print(p.split('/')[-1],len(e),e[:8]);
  if e: print(L[e[0]-1][:200])