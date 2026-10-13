import os
b='/task/fixtures/round-03/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'slow query' in l or ' INFO' in l or 'level=info' in l.lower(): continue
    print(f,i,l.strip()[:160])