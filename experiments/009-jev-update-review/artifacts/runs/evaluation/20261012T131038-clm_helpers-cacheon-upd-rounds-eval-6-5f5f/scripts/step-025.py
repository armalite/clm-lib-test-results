import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n13','role':'note','body':'R9 logs: disk high checkout-api round-09/logs/checkout-api.log:31,53; payments-svc.log:11,38. Next: advance to R10.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')