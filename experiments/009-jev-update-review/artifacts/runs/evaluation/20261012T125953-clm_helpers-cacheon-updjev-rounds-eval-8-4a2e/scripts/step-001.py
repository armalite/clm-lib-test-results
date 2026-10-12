import os
b='/task/fixtures/round-01/'
for f in sorted(os.listdir(b)):print(f)
for f in ['board.md','changes.md']:
  p=b+f
  if os.path.exists(p):
    for i,l in enumerate(open(p),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines();print(f,len(L))
  for i,l in enumerate(L,1):
    if any(k in l for k in ['ERROR','WARN','error','fail']):print(i,l[:160])