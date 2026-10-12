import json,collections
r='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
import os
for s in sorted(os.listdir(r+'logs')):
  c=collections.Counter();ln=collections.defaultdict(list)
  for i,l in enumerate(open(r+'logs/'+s),1):
    if 'ERROR' in l or 'error' in l.lower():
      k=l[l.find('msg'):l.find('msg')+50];c[k]+=1;ln[k].append(i)
  for k in c:print(s,c[k],k,ln[k][:3],ln[k][-1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))