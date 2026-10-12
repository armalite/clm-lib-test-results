b='/task/fixtures/round-02/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import os
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: print(f,i,l.strip()[:130])