import json
c=json.load(open('/task/workspace/context.json'))
note=[e for e in c['entries'] if e['id']=='n1'][0]
note['body']+=' But R3 logs: auth-svc tls handshake certificate_expired peer=bank-api (round-03/logs/auth-svc.log:1,16,21,62) -> likely CERT_EXPIRED (CHG-110 TLS rotation link?). Disk still high search-api (log:16-77, 98%) & shipping-svc (log:15,49 98%).'
c['entries']=[note]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read()[:800])