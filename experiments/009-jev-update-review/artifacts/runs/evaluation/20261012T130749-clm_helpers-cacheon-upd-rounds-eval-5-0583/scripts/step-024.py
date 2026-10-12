import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n14','role':'note','body':'R8 logs: auth-svc certificate_expired bank-api continues (round-08/logs/auth-svc.log:6,9,29,58,85); checkout-api no pool errors in R8. Next: advance to R9.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')