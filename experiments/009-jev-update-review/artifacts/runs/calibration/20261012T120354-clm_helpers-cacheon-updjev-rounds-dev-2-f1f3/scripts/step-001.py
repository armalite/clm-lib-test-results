import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f: print(os.path.join(r,x))
print(open(b+'board.md').read())
c=b+'changes.md'
if os.path.exists(c): print(open(c).read())
for x in os.listdir(b+'logs'):
  L=open(b+'logs/'+x).read().splitlines()
  print(x,len(L))
  for i,l in enumerate(L,1):
    if any(k in l for k in ('ERROR','WARN','error','warn')): print(i,l[:160])