import json,re
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e[1]['body']+=' auth-svc DB_POOL_EXHAUSTED recurring R2 (round-02/logs/auth-svc.log:1-25,44-69).'
json.dump({'format':'clm-context/v1','entries':e},open(p,'w'))
for i,l in enumerate(open('/task/fixtures/round-02/logs/notify-worker.log'),1):
  if re.search('ERROR|inflight|reject|fail|lag',l,re.I):print(i,l.strip()[:150])