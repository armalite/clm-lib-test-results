import json
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip()[:200])
import re,os
cnt={}
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|FATAL|OOM|429|disk|max_inflight|restart',l,re.I):
      k=(f,re.sub(r'\d','',l)[40:110]);cnt.setdefault(k,[]).append(i)
for k,v in cnt.items(): print(k[0],v[:5],len(v),k[1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))