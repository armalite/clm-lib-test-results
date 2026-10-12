import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R10 logs: checkout-api ERROR config validation failed db.pool_max=-4 build 7.35.8 (round-10/logs/checkout-api.log:9,11,16,18,44,58,66,69,73,87) -> BAD_CONFIG_ROLLOUT real (CHG-113). auth-svc cert_expired (round-10/logs/auth-svc.log:1-84); ledger-svc now also cert_expired bank-api (round-10/logs/ledger-svc.log:7-67). search/shipping clean.'})
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  try:
    for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip()[:200])
  except Exception as e:print(f,e)