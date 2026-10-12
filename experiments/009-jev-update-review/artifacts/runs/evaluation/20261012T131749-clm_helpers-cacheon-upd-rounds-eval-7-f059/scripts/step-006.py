import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R2 logs: shipping-svc 429 upstream=tax-provider at round-02/logs/shipping-svc.log:7,22,35,38,41,60 (UPSTREAM_RATE_LIMIT candidate). R2 done; next: advance to R3.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')