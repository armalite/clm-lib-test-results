import os
b='/task/fixtures/round-11/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1): print(f,i,l)
for s in os.listdir(b+'logs'):
  L=open(b+'logs/'+s).read().splitlines()
  h=[i for i,l in enumerate(L,1) if 'ERROR' in l or 'error' in l.lower()]
  print(s,len(h),h[:8], L[h[0]-1][:160] if h else '')