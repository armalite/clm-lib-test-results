import json,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1): print(f,i,l)
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  hits=[(i,l[:110]) for i,l in enumerate(L,1) if re.search(r'WARN|ERROR|429|pool|expired|DNS|lag|OOM|disk',l)]
  print(f,len(hits));[print(' ',h) for h in hits[:5]]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))