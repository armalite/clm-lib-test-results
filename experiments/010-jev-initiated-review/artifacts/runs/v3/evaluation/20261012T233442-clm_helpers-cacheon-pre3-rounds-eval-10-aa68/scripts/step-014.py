import re,glob
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|FATAL|429|SERVFAIL|pool|OOM|disk|expired|lag',l,re.I) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:3]+hits[-2:]: print(i,l[:150])