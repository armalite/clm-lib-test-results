import json,os
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' stage-2 quotes-api.log:136 db pool exhausted 14/14 (110 pool lines).'
json.dump(c,open('/task/workspace/context.json','w'))
for r,d,f in os.walk('/task/fixtures'):
  for x in f:print(os.path.join(r,x))
print(open('/task/fixtures/stage-2/UPDATE.md').read()[:600])
for p in ['/task/fixtures/stage-2/deploy/changes.log']:
  if os.path.exists(p):print(open(p).read()[:800])