import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n11b','role':'note','body':'R11 logs: checkout-api config validation failed pool_max=-4 (round-11/logs/checkout-api.log:3,17,24,64); auth-svc cert_expired reduced (round-11/logs/auth-svc.log:11,21); ledger cert_expired (round-11/logs/ledger-svc.log:7,32). R11 done; next: advance.'})
json.dump(c,open('/task/workspace/context.json','w'))