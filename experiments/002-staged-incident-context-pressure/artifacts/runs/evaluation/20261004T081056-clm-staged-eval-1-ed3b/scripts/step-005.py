import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' quotes-api.log:419 db pool wait in_use 14/14 (7 warns). Stage2 released.'
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md','UPDATE.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
n=0
for i,l in enumerate(open(b+'logs/quotes-api.log'),1):
  if 'ERROR' in l:
    n+=1
    if n<4:print(i,l.strip()[:180])
print(n)
for i,l in enumerate(open(b+'logs/api-gateway.log'),1):
  if '503' in l:print(i,l.strip()[:180]);break