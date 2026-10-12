import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'][-1]['body']+=' R5 logs: auth-svc cert_expired continues (round-05/logs/auth-svc.log:1-75); search/shipping disk clean now; others clean.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')