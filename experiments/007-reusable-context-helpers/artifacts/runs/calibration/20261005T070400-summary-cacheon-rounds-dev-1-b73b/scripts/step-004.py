b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1): print(f,i,l[:200])
import glob
for p in sorted(glob.glob(b+'logs/*')):
  n=0
  for i,l in enumerate(open(p).read().splitlines(),1):
    if 'slow query' in l or ' INFO ' in l: continue
    if n<6: print(p.split('/')[-1],i,l[:150])
    n+=1
  print(p.split('/')[-1],'other',n)
