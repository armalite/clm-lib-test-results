import os
b='/task/fixtures/round-01/'
for f in sorted(os.listdir(b)):print(f)
print(open(b+'board.md').read()[:1500])
import glob
for f in glob.glob(b+'*.md'):
  if 'changes' in f:print(open(f).read()[:1000])
for f in sorted(glob.glob(b+'logs/*')):
  L=open(f).read().splitlines();print(f,len(L))
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l:print(i,l[:160])