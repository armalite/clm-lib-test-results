import os,re
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'slow query' in l.lower() or ' INFO' in l or 'info' in l.lower()[:40]: continue
    print(f,i,l.strip()[:150])