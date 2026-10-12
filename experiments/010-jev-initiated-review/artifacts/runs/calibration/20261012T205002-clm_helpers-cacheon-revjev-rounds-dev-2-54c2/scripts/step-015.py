import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
keep.append({'id':'n5','role':'note','body':'R5: board.md:3 Thread A mitigated; board.md:4 Thread B services +shipping-svc (cause still says DB_POOL on board, logs say CERT_EXPIRED). board.md:5-6 OPEN VENDOR_TICKET, ALERT_TUNING. changes.md:3 CHG-143 APPLIED mitigation inventory-svc (thread A). No DNS errors in checkout/inventory R5. CERT errs round-05/logs/auth-svc.log:2-64, shipping-svc.log:9-65. search-api no errors. Next: advance.'})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')