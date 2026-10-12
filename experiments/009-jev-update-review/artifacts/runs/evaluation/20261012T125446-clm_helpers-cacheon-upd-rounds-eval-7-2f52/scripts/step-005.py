import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e[1]['body']+=' Logs: shipping-svc 429 upstream=tax-provider at lines 7,22,35,38,41,60 (UPSTREAM_RATE_LIMIT candidate). R2 scanned; next: advance.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')