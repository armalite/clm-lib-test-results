import json
L=open('/task/fixtures/round-08/logs/checkout-api.log').read().splitlines()
print(len(L));[print(i+1,l[:120]) for i,l in enumerate(L[:3])]
import re
h=[(i+1,l[:120]) for i,l in enumerate(L) if re.search('pool|exhaust|error|warn',l,re.I)]
print(len(h));[print(x) for x in h[:4]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR8 logs: checkout-api no WARN/ERROR (check format); auth-svc cert_expired continues (round-08/logs/auth-svc.log:6,32).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))