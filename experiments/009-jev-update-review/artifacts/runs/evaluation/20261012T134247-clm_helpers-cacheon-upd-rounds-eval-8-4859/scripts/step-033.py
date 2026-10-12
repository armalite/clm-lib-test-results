import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+=' R11 logs: inventory db pool exhausted 8,58; payments 23,60 (declining); notify config validation failed 11,17,20,27,35,42,55,69,74,82. NEXT: advance to R12.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')