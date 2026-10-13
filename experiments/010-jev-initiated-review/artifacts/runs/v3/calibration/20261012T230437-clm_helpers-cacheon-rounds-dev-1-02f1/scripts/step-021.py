import json,os,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R7: board empty. 429 fx-rates continue checkout-api (round-07/logs/checkout-api.log:11-25) & payments-svc (round-07/logs/payments-svc.log:1); no pool WARNs; notify clean.'})
json.dump(c,open('/task/workspace/context.json','w'))
print(os.path.exists('/task/fixtures/round-07/changes.md'))
if os.path.exists('/task/fixtures/round-07/changes.md'):print(open('/task/fixtures/round-07/changes.md').read())