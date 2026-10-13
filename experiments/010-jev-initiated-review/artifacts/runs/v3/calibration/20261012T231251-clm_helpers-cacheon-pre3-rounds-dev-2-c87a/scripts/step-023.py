import json,re,os
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:160])
for f in sorted(os.listdir(b+'logs')):
  hits=[]
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'ERROR|FATAL|uptime|restart|429|disk|memory|lag|max_inflight',l,re.I) and 'slow query' not in l.lower():hits.append((i,l.rstrip()[:110]))
  print(f,len(hits))
  for h in hits[:4]:print(' ',h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))