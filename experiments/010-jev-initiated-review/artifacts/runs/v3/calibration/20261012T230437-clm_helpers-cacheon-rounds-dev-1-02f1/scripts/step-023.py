import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1];hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if 'INFO' not in l]
  print(n,len(hits))
  for i,l in hits[:4]:print(' ',i,l[:150])