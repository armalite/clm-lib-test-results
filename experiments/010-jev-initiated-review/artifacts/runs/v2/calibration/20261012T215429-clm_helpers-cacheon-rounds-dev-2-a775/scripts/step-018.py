import json
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body'].replace(' Round 5 reviewed; next: advance.','')
n+=' R6: board.md:3 OPEN RUNBOOK_UPDATE. changes.md:3 CHG-144 log sampling (noise). CERT auth-svc.log:4,10 shipping-svc.log:1,18. No other errors. Round 6 reviewed; next: advance.'
c['entries']=[{'id':'notes','role':'note','body':n}]
json.dump(c,open('/task/workspace/context.json','w'))