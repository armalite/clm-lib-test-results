import json
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]['body']
n=n.replace(' Next: advance to R5.','')
n+='\nR5: Thread A mitigated round-05/board.md:3 after CHG-143 APPLIED inventory-svc (round-05/changes.md:3); no DNS errs R5. Thread B adds shipping-svc (round-05/board.md:4). Follow-ups OPEN VENDOR_TICKET (board:5), ALERT_TUNING (board:6). CERT errs auth round-05/logs/auth-svc.log:2,8; shipping round-05/logs/shipping-svc.log:9,11. Next: advance to R6.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))