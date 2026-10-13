import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: board Thread A mitigated (round-05/board.md:3) via CHG-143 APPLIED inventory-svc (round-05/changes.md:3); no DNS errors in checkout/inventory R5. Thread B adds shipping-svc (round-05/board.md:4). Follow-ups OPEN VENDOR_TICKET (board.md:5), ALERT_TUNING (board.md:6). CERT_EXPIRED continues auth round-05/logs/auth-svc.log:2,8,14,22; shipping round-05/logs/shipping-svc.log:9,11,34,36. search-api still clean. Next: advance to R6.'})
json.dump(c,open('/task/workspace/context.json','w'))