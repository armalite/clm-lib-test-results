import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e[1]['body']+=' R2 logs: search-api disk WARN used_pct 91-98 (round-02/logs/search-api.log:4-63), shipping-svc 91-98 (round-02/logs/shipping-svc.log:4-71). No other errors.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')