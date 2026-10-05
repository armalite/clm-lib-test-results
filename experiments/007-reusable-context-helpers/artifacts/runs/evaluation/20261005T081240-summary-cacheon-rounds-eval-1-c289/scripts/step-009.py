import os
b='/task/fixtures/round-03/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ' INFO ' in l or 'slow query' in l: continue
    if 'consumer lag' in l: continue
    print(f,i,l.strip()[:150])
