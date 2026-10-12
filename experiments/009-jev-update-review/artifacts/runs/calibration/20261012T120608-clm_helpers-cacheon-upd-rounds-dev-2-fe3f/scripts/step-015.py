import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR6 logs: cert errs auth round-06/logs/auth-svc.log:4,10; shipping round-06/logs/shipping-svc.log:1,18; no DNS, search-api no errs.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')