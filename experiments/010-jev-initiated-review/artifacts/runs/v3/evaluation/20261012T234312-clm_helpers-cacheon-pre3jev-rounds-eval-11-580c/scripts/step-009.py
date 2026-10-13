import os
b='/task/fixtures/round-03/'
for i,l in enumerate(open(b+'board.md'),1):print('board',i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'INFO' in l or 'slow query' in l: continue
    print(f,i,l.rstrip()[:160])