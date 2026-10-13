import json
d=json.load(open('/task/workspace/context.json'))
for e in d['entries']:
  if e['id']=='notes': e['body']+="\nR9 logs: shipping-svc.log:15+ ERROR config validation failed retry.backoff_ms=0 build 6.58.8 (=> Thread C BAD_CONFIG_ROLLOUT from CHG-113). inventory/search 429 still sporadic. Grep cmd: lines with '\"ERROR\"'."
d['entries']=[e for e in d['entries'] if e['id']=='notes']
json.dump(d,open('/task/workspace/context.json','w'))
L=[i for i,l in enumerate(open('/task/fixtures/round-09/logs/shipping-svc.log'),1) if '"ERROR"' in l]
print(L)