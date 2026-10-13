import re,glob
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  L=open(f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if not re.search(r'slow query|INFO',l)]
  if hits:
    print(f.split('/')[-1],hits[0],hits[-1],len(hits),L[hits[0]-1][:160])