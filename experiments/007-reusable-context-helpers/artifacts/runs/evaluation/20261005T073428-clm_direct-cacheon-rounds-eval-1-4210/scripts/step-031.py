import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R10.','')
n+='\nR10: board.md:3 CLOSED CUSTOMER_COMMS. changes.md:3 CHG-173 PROPOSED only. Logs: auth-svc.log:9,17,18,21,23,24,26-28,39,40,46,60 ttl_s=-1; search-api.log:20,37 CERT; shipping-svc.log:58,61 CERT. Next: advance to R11.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')