import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
for e in c['entries']:
  if e['id']=='n3': e['body']='R3: board.md:3 Thread B says auth-svc DB_POOL_EXHAUSTED ongoing, BUT logs show CERT_EXPIRED: round-03/logs/auth-svc.log:6,9,15,21,25,26,33,48,64,72 tls handshake peer=sso.example.net certificate_expired; no pool errors. changes.md:3 CHG-126 PROPOSED (ignore). search-api R2/R3 no errors (CHG-120 maybe no effect yet).'
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')