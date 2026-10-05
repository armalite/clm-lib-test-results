import json,re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(b+'logs')):
  hits=[str(i) for i,l in enumerate(open(b+'logs/'+s),1) if not re.search(r'slow query|INFO',l)]
  print(s,','.join(hits[:15]))
  if hits:print(' ex:',open(b+'logs/'+s).read().splitlines()[int(hits[0])-1][:160])
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open(p,'w'))