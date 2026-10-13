import os
b='/task/fixtures/round-03/'
print(os.listdir(b))
if os.path.exists(b+'changes.md'):print(open(b+'changes.md').read())
for f in os.listdir(b+'logs'):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'ERROR' in l or 'error' in l.lower() and 'WARN' not in l: print(f,i,l.strip()[:130])