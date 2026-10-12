import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
for e in c['entries']:
  if e['id']=='n8': e['body']+=' R8 logs: search-api config validation failed http.max_inflight=-1 (CHG-120 -> BAD_CONFIG_ROLLOUT, Thread C) round-08/logs/search-api.log:2,5,10,26,42,44,59,68,72; 429 tax-provider continues :1,12,14,20,25,66. Next: advance to R9.'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')