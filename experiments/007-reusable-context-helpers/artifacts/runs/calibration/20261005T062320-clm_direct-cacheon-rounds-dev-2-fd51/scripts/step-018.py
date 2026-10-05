import json
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]['body']
n=n.replace(' Next: advance to R6.','')
n+='\nR6: board adds Follow-up OPEN RUNBOOK_UPDATE (round-06/board.md:3). CHG-144 APPLIED log sampling (noise). CERT continues auth round-06/logs/auth-svc.log:4,79; shipping round-06/logs/shipping-svc.log:1,64. No DNS/search errs. Next: advance to R7.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))