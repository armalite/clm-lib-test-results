import os
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  n=0;L=[]
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ' INFO ' in l or 'slow query' in l: continue
    n+=1;L.append(i)
    if n<=3: print(f,i,l.strip()[:130])
  print(f,'other',n,L[:30])
