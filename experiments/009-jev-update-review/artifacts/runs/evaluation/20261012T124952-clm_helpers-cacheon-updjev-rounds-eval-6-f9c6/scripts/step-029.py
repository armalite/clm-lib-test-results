import re,glob
print(open('/task/fixtures/round-10/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'429|disk|batch_size|heap|ERROR',l,re.I)]
  print(f.split('/')[-1],len(hits),hits[:3],hits[-1:] , L[hits[0]-1][:160] if hits else '')