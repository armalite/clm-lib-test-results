import json
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
d['entries'].append({'id':'n7','role':'note','body':'R7: board.md:3 Thread B +pricing-svc; board.md:4 Thread D CERT_EXPIRED inventory-svc ongoing (but CHG-120 retry.backoff_ms=0 suspicious). changes.md:3 CHG-151 PROPOSED noise. inventory-svc.log tls handshake failed :7,8,12,21,64,67,68. ledger dns :4-73, pricing dns :6-61. Next: advance to round 8.'})
json.dump(d,open(p,'w'))
ls=open('/task/fixtures/round-07/logs/inventory-svc.log').read().splitlines()
for i in (7,8):print(i,ls[i-1][:300])