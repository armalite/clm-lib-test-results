import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']=e['body'].replace('Next: R8 logs then advance R9.','R8 logs: inventory db pool exhausted 2,9,13,18,26,28,44,50,53,54,57; others routine. Next: advance R9.')
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')