import os,re
b='/task/fixtures/round-04/'
print(open(b+'board.md').read())
if os.path.exists(b+'changes.md'):print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if ('WARN' in l or 'ERROR' in l or 'warn' in l.lower()) and 'slow query' not in l: print(f[:6],i,l.strip()[:90])