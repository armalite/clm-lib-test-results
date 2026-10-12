import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']+=' R9 logs: inventory db pool exhausted 11,24,36,49,55,59,68; payments-svc db pool exhausted NEW 3,5,13,17,32,72 (may join Thread B). Next: advance R10.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')