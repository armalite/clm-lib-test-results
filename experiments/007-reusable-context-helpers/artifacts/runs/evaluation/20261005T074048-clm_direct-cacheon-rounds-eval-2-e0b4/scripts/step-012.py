import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip()[:200])
import glob,re
for p in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  hits=[(i,l) for i,l in enumerate(open(p),1) if re.search(r'ERROR|429|OOM|restart',l)]
  print(p.split('/')[-1],len(hits))
  for i,l in hits[:4]:print(' ',i,l.rstrip()[:140])