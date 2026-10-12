import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n12','role':'note','body':'R7 logs: checkout-api db pool exhausted continues (round-07/logs/checkout-api.log:2,8,33,47,66); auth-svc certificate_expired bank-api continues (round-07/logs/auth-svc.log:12,79). Next: advance to R8.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')