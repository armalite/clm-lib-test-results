import json,re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
import os
for s in os.listdir(b+'logs'):
  L=open(b+'logs/'+s).read().splitlines()
  e=[i for i,l in enumerate(L,1) if re.search('ERROR|429|error|fatal|OOM|restart',l)]
  print(s,len(e),e[:12])
  if e:print(' ',L[e[0]-1][:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))