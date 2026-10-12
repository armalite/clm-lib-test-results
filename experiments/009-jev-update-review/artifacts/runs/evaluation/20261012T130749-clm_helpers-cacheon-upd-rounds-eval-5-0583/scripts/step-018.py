import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R6 logs: checkout-api db pool exhausted WARNs (round-06/logs/checkout-api.log:8,25,27,44,72), pool sizes vary 10-20; no explicit invalid-config line yet. Next: advance to R7.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')