import os
b='/task/fixtures/round-06/'
print(open(b+'board.md').read())
if os.path.exists(b+'changes.md'):print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=[];S=set()
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ' INFO ' in l or 'slow query' in l: continue
    L.append(i);S.add(l.strip()[21:130])
  print(f,len(L),L[:30]);[print(' ',s) for s in list(S)[:3]]
