import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R5 logs: auth-svc certificate_expired peer=bank-api continues (round-05/logs/auth-svc.log:1,3,13,75). No other errors. Next: advance to R6.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')