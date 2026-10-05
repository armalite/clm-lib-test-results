import os
b='/task/fixtures/round-04/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  n=0
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ' INFO ' in l or 'slow query' in l or 'consumer lag' in l: continue
    n+=1
    if n<=6: print(f,i,l.strip()[:140])
  print(f,'other',n)
