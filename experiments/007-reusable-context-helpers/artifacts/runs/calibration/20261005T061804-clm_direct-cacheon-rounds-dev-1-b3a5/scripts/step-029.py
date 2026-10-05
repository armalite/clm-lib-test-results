import json,os
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
for s in os.listdir(b+'logs'):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if 'slow query' in l or ' INFO' in l or 'level=info' in l.lower(): continue
    print(s,i,l.rstrip()[:110])
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open(p,'w'))