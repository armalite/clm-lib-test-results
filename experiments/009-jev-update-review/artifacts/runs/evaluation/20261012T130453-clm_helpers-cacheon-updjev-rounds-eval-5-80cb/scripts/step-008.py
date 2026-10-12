import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board.md:3 Thread B claims auth-svc MEMORY_LEAK, but logs show TLS certificate_expired peer=bank-api (round-03/logs/auth-svc.log:1,16,21,25,35,62) -> real cause CERT_EXPIRED; no mem evidence. checkout/ledger clean R3.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')