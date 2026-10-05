import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
for e in d['entries']:
    if e['id']=='n9':e['body']+=' inventory config validation failed retry.backoff_ms=0 build 7.30.0 r09 inventory-svc.log:2,15,28,29,42-71 -> BAD_CONFIG_ROLLOUT. Next: advance to round 10.'
json.dump(d,open(p,'w'))
print('ok')