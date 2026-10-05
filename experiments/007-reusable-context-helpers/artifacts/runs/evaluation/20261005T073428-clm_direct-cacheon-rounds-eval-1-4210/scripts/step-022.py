import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R7.','')
n+='\nR7: board.md:3 OPEN POSTMORTEM_DRAFT; :4 OPEN DATA_BACKFILL. changes.md:3 CHG-154 APPLIED retry budget. Logs: CERT_EXPIRED sso.example.net search-api.log:8,10,11,16,20,28,30,37,46,47,59,68,71; shipping-svc.log:3,16,21,35,36,41,52,66,75,76. Next: advance to R8.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')