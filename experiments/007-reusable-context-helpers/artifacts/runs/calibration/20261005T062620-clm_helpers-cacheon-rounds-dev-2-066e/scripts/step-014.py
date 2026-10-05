import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
n.append({'id':'n5','role':'note','body':'R5: board.md:3 Thread A (DNS) mitigated; board.md:4 Thread B adds shipping-svc; board.md:5 OPEN VENDOR_TICKET; board.md:6 OPEN ALERT_TUNING. changes.md:3 CHG-143 APPLIED mitigation thread A inventory-svc. DNS lines gone in r5. cert_expired continues auth-svc 2-64, shipping-svc 9-65. Next: advance to round 6.'})
c['entries']=n
json.dump(c,open('/task/workspace/context.json','w'))