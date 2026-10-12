import json
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R5 logs: payments-svc disk usage high /var/data persists (payments-svc.log:1-74); others only slow-query WARNs.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
print('ok')