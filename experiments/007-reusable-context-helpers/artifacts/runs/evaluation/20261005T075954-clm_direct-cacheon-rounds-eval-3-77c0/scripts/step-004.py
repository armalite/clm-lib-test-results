import json,os
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f)):print(f,i+1,l.strip()[:200])
out=[]
for x in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+x)):
    if ('ERROR' in l or 'WARN' in l or 'error' in l.lower()) and 'slow query' not in l:out.append(f'{x}:{i+1} {l.strip()[:130]}')
print(len(out));print('\n'.join(out[:35]))
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))