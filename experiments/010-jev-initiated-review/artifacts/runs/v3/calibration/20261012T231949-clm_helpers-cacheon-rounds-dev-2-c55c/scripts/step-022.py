import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
for e in c['entries']:
  if e['id']=='n7': e['body']+=' VERIFIED real 429 tax-provider (not CHG-120). Next: advance to R8.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')