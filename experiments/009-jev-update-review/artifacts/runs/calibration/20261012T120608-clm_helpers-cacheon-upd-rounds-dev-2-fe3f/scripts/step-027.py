import json,re
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
L=open('/task/fixtures/round-10/logs/search-api.log').read().splitlines()
h=[i for i,l in enumerate(L,1) if '429' in l]
cf=[i for i,l in enumerate(L,1) if 'config validation' in l]
n['body']+=f'\nR10 logs: search-api 429 lines {h}; config err lines {cf}; cert auth round-10/logs/auth-svc.log:10,17; shipping round-10/logs/shipping-svc.log:3,60; no DNS. NEXT: advance to R11.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print(h,cf)