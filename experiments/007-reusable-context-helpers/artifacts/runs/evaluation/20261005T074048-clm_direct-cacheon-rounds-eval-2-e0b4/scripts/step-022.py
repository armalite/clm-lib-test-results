import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5','n6')]
c['entries'].append({'id':'n7','role':'note','body':'R7: Thread B adds pricing-svc, cause/status unchanged (round-07/board.md:3). Thread D CERT_EXPIRED inventory-svc ongoing (board.md:4); logs tls certificate_expired peer=partner-gw (round-07/logs/inventory-svc.log:7,8,12,21). DNS SERVFAIL continues ledger (round-07/logs/ledger-svc.log:4-21) and pricing (round-07/logs/pricing-svc.log:6-16). CHG-151 PROPOSED only. Next: advance to R8.'})
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')